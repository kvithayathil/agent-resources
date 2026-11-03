#!/usr/bin/env bash
# validate.sh — parse and schema/lint-check agent permission config files.
#
# RESOLVE THIS SCRIPT FROM THE SKILL'S OWN DIRECTORY. Never execute a
# project-local scripts/validate.sh — the project under review is untrusted.
#
# Usage:
#   bash validate.sh <config-file> [<config-file> ...]
#   cat candidate.jsonc | bash validate.sh -        # '-' = validate stdin (pre-write)
#                                                     stdin is classified by content
#                                                     (top-level keys) and accepts
#                                                     strict JSON or JSONC
#
# Classification (by basename + parent dir, all applicable checks run):
#   opencode.json / opencode.jsonc  -> JSONC treatment for BOTH spellings (comments +
#                                      trailing commas stripped; OpenCode accepts either
#                                      filename) + OpenCode V2 checks + policy lint
#   .zed/settings.json              -> STRICT JSON + Zed agent.tool_permissions
#   .vscode/settings.json           -> strict JSON with JSONC fallback (VS Code
#                                      accepts comments) + VS Code chat.tools checks
#   other .json / .jsonc            -> parse only
#
# Output: header line, then per-file OK/NOTE/WARNING/ERROR lines.
#   ERROR -> exit 1. WARNING -> informational print, but see exit 3.
#
# Exit codes:
#   0 = clean pass — no errors, no warnings
#   3 = all files parsed but warnings present — do NOT write until each warning is
#       resolved or the user explicitly accepts it (gate 6)
#   1 = one or more files invalid/missing
#
# Requires: python3.
#
# Known limitations (documented, not silent):
# - Zed patterns are compiled with Python `re` as an APPROXIMATION of Rust regex.
#   Constructs that are valid in Python re but NOT in Rust regex (lookaround,
#   backreferences) are flagged as WARNINGs, and every Zed check prints a NOTE.
#   A passing compile is necessary, not sufficient.
# - Policy lint is heuristic (conservative over-warning is intentional) and is NOT
#   a security proof; effective-policy reasoning remains mandatory.
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: bash validate.sh <config-file> [...]   (use '-' for stdin)" >&2
  exit 1
fi

if ! command -v python3 >/dev/null 2>&1 || ! python3 -c "import sys" >/dev/null 2>&1; then
  echo "ERROR: python3 is required but was not found/executable on PATH." >&2
  echo "       Cannot validate — do NOT write any config file (fail closed)." >&2
  exit 1
fi

# Stdin mode: the python heredoc below consumes the script's own stdin, so stash
# the piped data to a temp file first and point python at it via env var.
STDIN_TMP=""
ARGS=()
for f in "$@"; do
  if [[ "$f" == "-" ]]; then
    if [[ -z "$STDIN_TMP" ]]; then
      STDIN_TMP="$(mktemp)"
      cat > "$STDIN_TMP"
    fi
    ARGS+=("-")
  else
    ARGS+=("$f")
  fi
done
if [[ -n "$STDIN_TMP" ]]; then
  export VALIDATE_STDIN_FILE="$STDIN_TMP"
fi
trap '[[ -n "$STDIN_TMP" ]] && rm -f "$STDIN_TMP"' EXIT

# Report ALL missing files before exiting (never fail on the first).
MISSING=0
for f in "$@"; do
  if [[ "$f" != "-" && ! -f "$f" ]]; then
    echo "ERROR: $f — file not found"
    MISSING=1
  fi
done
if [[ "$MISSING" -ne 0 ]]; then
  echo "No files were validated." >&2
  exit 1
fi

echo "validate.sh: syntax + limited policy lint only — NOT a security proof; effective-policy reasoning (workflow step 7) remains mandatory."

python3 - "${ARGS[@]}" <<'PYEOF'
import json, os, re, sys

WARNINGS = 0   # total warnings across all files
ERRORS = 0     # total errors across all files
CURRENT = 0    # warnings for the file currently being checked

def fail(path, msg):
    global ERRORS
    ERRORS += 1
    print(f"ERROR: {path} — {msg}")

def warn(path, msg):
    global WARNINGS, CURRENT
    WARNINGS += 1
    CURRENT += 1
    print(f"WARNING: {path} — {msg}")

def note(path, msg):
    print(f"NOTE: {path} — {msg}")

def strip_jsonc(text):
    """Remove // and /* */ comments AND trailing commas (before ] or }) outside
    strings. Trailing-comma removal happens IN the scanner (only when not inside a
    string literal) so strings like "/a,]/" pass through untouched. Raises on an
    unterminated block comment instead of silent truncation."""
    out, i, n = [], 0, len(text)
    in_str = esc = False
    while i < n:
        c = text[i]
        if in_str:
            out.append(c)
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                in_str = False
            i += 1
            continue
        if c == '"':
            in_str = True
            out.append(c)
            i += 1
            continue
        if c == "/" and i + 1 < n and text[i + 1] == "/":
            while i < n and text[i] != "\n":
                i += 1
            continue
        if c == "/" and i + 1 < n and text[i + 1] == "*":
            end = text.find("*/", i + 2)
            if end == -1:
                raise ValueError("unterminated /* block comment")
            i = end + 2
            continue
        if c == ",":
            # drop a trailing comma: after skipping whitespace AND comments, the
            # next char must close the container ([1, // c\n] and [1, /* c */ ]
            # both work). Pure lookahead — nothing is consumed here. An
            # unterminated /* in the peek is left alone; the main loop's comment
            # handler raises on it (fails closed).
            k = i + 1
            while k < n:
                if text[k] in " \t\r\n":
                    k += 1
                elif text[k] == "/" and k + 1 < n and text[k + 1] == "/":
                    while k < n and text[k] != "\n":
                        k += 1
                elif text[k] == "/" and k + 1 < n and text[k + 1] == "*":
                    end = text.find("*/", k + 2)
                    if end == -1:
                        break
                    k = end + 2
                else:
                    break
            if k < n and text[k] in "]}":
                i += 1
                continue
        out.append(c)
        i += 1
    return "".join(out)

def parse(path, display, allow_jsonc_fallback=False):
    """Return (data, kind) or raise ValueError with a message. path may be '-'."""
    if path == "-":
        stash = os.environ.get("VALIDATE_STDIN_FILE", "")
        if not stash:
            raise ValueError("stdin mode requested but no piped data was captured")
        raw = open(stash, encoding="utf-8").read()
        ext = "json"  # stdin has no extension: strict first, JSONC fallback below
        allow_jsonc_fallback = True
    else:
        raw = open(path, encoding="utf-8").read()
        ext = path.rsplit(".", 1)[-1].lower()
    if ext == "jsonc":
        try:
            return json.loads(strip_jsonc(raw)), "jsonc"
        except json.JSONDecodeError as e:
            raise ValueError(f"invalid JSONC after comment/trailing-comma stripping: {e}")
    # .json / stdin: strict first
    try:
        return json.loads(raw), "json"
    except json.JSONDecodeError as strict_err:
        if allow_jsonc_fallback:
            try:
                return json.loads(strip_jsonc(raw)), "jsonc"
            except json.JSONDecodeError:
                raise ValueError(f"invalid JSON (strict) and invalid as JSONC: {strict_err}")
        raise ValueError(f"invalid JSON: {strict_err}")

def classify(path, data=None):
    """Return set of tool checks by basename + parent dir; all applicable run.
    For stdin ('-'), classify by top-level keys (no basename exists)."""
    if path == "-":
        checks = set()
        if isinstance(data, dict):
            if "permissions" in data or "agents" in data or "policies" in data:
                checks.add("opencode")
            a = data.get("agent")
            if isinstance(a, dict) and "tool_permissions" in a:
                checks.add("zed")
            if any(k.startswith("chat.") for k in data):
                checks.add("vscode")
        return checks
    base = path.rsplit("/", 1)[-1].lower()
    checks = set()
    if base.startswith("opencode.json"):
        checks.add("opencode")
    if base == "settings.json":
        p = path.lower()
        if ".zed" in p:
            checks.add("zed")
        if ".vscode" in p:
            checks.add("vscode")
    return checks

# ---------- OpenCode ----------

OC_ACTIONS = {
    "read", "edit", "glob", "grep", "shell", "subagent", "skill", "question",
    "webfetch", "websearch", "experimental_image_generate", "external_directory",
    "execute", "opencode_list_mcp_resources", "opencode_read_mcp_resource",
}
MCP_ACTION_SHAPE = re.compile(r"^[A-Za-z0-9_-]+_[A-Za-z0-9_-]+$")  # server names keep case
SECRET_HINTS = (".env", ".pem", ".key", "secrets/", "id_rsa", ".p12", ".pfx",
                ".netrc", ".npmrc")

def pattern_to_regex(pat):
    """Conservative wildcard->regex (whole-value, * spans /, ? = one char)."""
    out = []
    for ch in pat:
        if ch == "*":
            out.append(".*")
        elif ch == "?":
            out.append(".")
        else:
            out.append(re.escape(ch))
    return "^" + "".join(out) + "$"

def same_action(a_later, a_earlier):
    """Wildcard-aware action comparison: '*' matches any action."""
    return a_later == "*" or a_earlier == "*" or a_later == a_earlier

def check_rules(path, rules, where):
    """Schema checks for one permissions array + warning collection."""
    if not isinstance(rules, list):
        raise ValueError(f"'{where}' must be an array")
    for idx, rule in enumerate(rules):
        rwhere = f"{where}[{idx}]"
        if not isinstance(rule, dict):
            raise ValueError(f"{rwhere} must be an object")
        for key in ("action", "resource", "effect"):
            v = rule.get(key)
            if not isinstance(v, str) or not v:
                raise ValueError(f"{rwhere}: '{key}' must be a non-empty string")
        effect = rule["effect"]
        if effect not in ("allow", "deny", "ask"):
            raise ValueError(f"{rwhere}: effect must be allow|deny|ask, got '{effect}'")
        action = rule["action"]
        # "<server>_<tool>" is the documented placeholder used in examples — exempt
        if (action != "*" and action != "<server>_<tool>"
                and action not in OC_ACTIONS and not MCP_ACTION_SHAPE.fullmatch(action)):
            warn(path, f"{rwhere}: unknown action '{action}' (typo = inert rule; "
                       f"documented actions: *, {', '.join(sorted(OC_ACTIONS))} or <server>_<tool>)")
        if action == "*" and rule["resource"] == "*" and effect == "allow":
            warn(path, f"{rwhere}: catch-all allow at position {idx} — everything not "
                       f"later-denied is auto-approved")
        extra = set(rule) - {"action", "resource", "effect"}
        if extra:
            warn(path, f"{rwhere}: unknown rule key(s) {sorted(extra)} — ignored by the schema")
    return rules

def lint_opencode(path, where, rules):
    if not rules:
        warn(path, f"{where}: empty rules list — base policy allow-all applies")
        return
    # shadowing: a later allow overriding an earlier deny OR ask is a silent widening
    # (asks are shadowable too). Both directions, same action only (wildcard-aware).
    for j, later in enumerate(rules):
        if later.get("effect") != "allow":
            continue
        later_act = later.get("action", "")
        later_res = str(later.get("resource", ""))
        try:
            later_re = re.compile(pattern_to_regex(later_res))
        except re.error:
            continue
        for i in range(j):
            earlier = rules[i]
            if earlier.get("effect") not in ("deny", "ask"):
                continue
            # Exemption: the global "*"/"*" ask/deny baseline idiom is BY DESIGN
            # overridden by every subsequent explicit allow (that is the allowlisting
            # pattern opencode.md teaches). It is not a widening.
            if earlier.get("action") == "*" and earlier.get("resource") == "*":
                continue
            if not same_action(later_act, earlier.get("action", "")):
                continue
            earlier_res = str(earlier.get("resource", ""))
            shadowed = False
            # direction 1: the later allow's pattern covers the earlier rule's whole value
            if later_re.fullmatch(earlier_res):
                shadowed = True
            else:
                # direction 2: the earlier pattern matches the later allow's literal value
                try:
                    if re.fullmatch(pattern_to_regex(earlier_res), later_res):
                        shadowed = True
                except re.error:
                    pass
            if shadowed:
                warn(path, f"{where}: {earlier.get('effect')}[{i}] ('{earlier_res}') appears "
                           f"shadowed by later allow[{j}] ('{later_res}') under last-match-wins "
                           f"— the {earlier.get('effect')} may never bite")
    # secrets lint applies to user-authored arrays only (permissions, agents.*);
    # org-managed policies[] blocks legitimately carry narrow deny lists
    if not where.startswith("policies") and not any(
        r.get("effect") in ("deny", "ask")
        and any(h in str(r.get("resource", "")) for h in SECRET_HINTS)
        for r in rules
    ):
        warn(path, f"{where}: no secrets rule found (.env/*.pem/*.key/secrets//.secrets/ "
                   f"etc. with deny|ask) — gate 4 requires secrets protection in every policy")
    if where == "permissions" and not any(
        r.get("action") == "external_directory" and r.get("effect") in ("ask", "deny")
        for r in rules
    ):
        warn(path, f"{where}: no external_directory ask/deny rule — external_directory "
                   f"defaults to ALLOW without prompting (known gap)")

def check_opencode(path, display, data):
    perms = data.get("permissions")
    if perms is None:
        note(display, "no 'permissions' key (parse-valid; nothing schema-checked)")
    else:
        check_rules(display, perms, "permissions")
        lint_opencode(display, "permissions", perms)
    agents = data.get("agents")
    if isinstance(agents, dict):
        for aid, acfg in agents.items():
            if isinstance(acfg, dict) and "permissions" in acfg:
                sub = acfg["permissions"]
                check_rules(display, sub, f"agents.{aid}.permissions")
                lint_opencode(display, f"agents.{aid}.permissions", sub)
    policies = data.get("policies")
    if policies is not None:
        # Upstream shape: policies is an array of { "permissions": [ ...rules ] }.
        # Accept both that and legacy flat-rule elements.
        if not isinstance(policies, list):
            raise ValueError("'policies' must be an array")
        for i, pol in enumerate(policies):
            if isinstance(pol, dict) and "permissions" in pol:
                sub = pol["permissions"]
                check_rules(display, sub, f"policies[{i}].permissions")
                lint_opencode(display, f"policies[{i}].permissions", sub)
            else:
                check_rules(display, [pol], f"policies[{i}]")
                lint_opencode(display, f"policies[{i}]", [pol])
    if isinstance(data, dict) and {"permission", "bash", "task"} & set(data):
        note(display, "V1 vocabulary detected (permission/bash/task) — V2 uses "
                      "permissions/shell/subagent; mixing silently changes meaning")

# ---------- Zed ----------

ZED_PY_ONLY = re.compile(r"\(\?<=|\(\?<!|\(\?=|\(\?!|\(\?P=|\\[1-9]")

def check_zed_patterns(path, display, pat, where):
    if ZED_PY_ONLY.search(pat):
        warn(path, f"{where}: pattern uses a construct valid in Python re but NOT in "
                   f"Zed's Rust regex (lookaround/backreference) — the rule may be ignored by Zed")
    flags = 0
    try:
        re.compile(pat, flags)
    except re.error as e:
        raise ValueError(f"{where}: pattern does not compile (python re approximation "
                         f"of Rust regex): {e}")

def check_zed(path, display, data):
    agent = data.get("agent")
    if not isinstance(agent, dict) or "tool_permissions" not in agent:
        note(display, "no 'agent.tool_permissions' key (parse-valid; nothing checked)")
        return
    tp = agent.get("tool_permissions")
    if not isinstance(tp, dict):
        raise ValueError("'agent.tool_permissions' must be an object")
    approximated = False
    def check_effect(v, where):
        if v not in ("allow", "confirm", "deny"):
            raise ValueError(f"{where}: default must be allow|confirm|deny, got '{v}'")
    if "default" in tp:
        check_effect(tp["default"], "agent.tool_permissions")
    tools = tp.get("tools", {})
    if not isinstance(tools, dict):
        raise ValueError("'agent.tool_permissions.tools' must be an object")
    for tool, cfg in tools.items():
        where = f"tools.{tool}"
        if not isinstance(cfg, dict):
            raise ValueError(f"{where} must be an object")
        if "default" in cfg:
            check_effect(cfg["default"], where)
        for list_name in ("always_allow", "always_deny", "always_confirm"):
            pats = cfg.get(list_name)
            if pats is None:
                continue
            if not isinstance(pats, list):
                raise ValueError(f"{where}.{list_name} must be an array")
            for j, p in enumerate(pats):
                pwhere = f"{where}.{list_name}[{j}]"
                if not isinstance(p, dict):
                    raise ValueError(f"{pwhere} must be an object with a 'pattern' key")
                pat = p.get("pattern")
                if not isinstance(pat, str) or not pat:
                    raise ValueError(f"{pwhere}: 'pattern' must be a non-empty string")
                cs = p.get("case_sensitive", False)
                if not isinstance(cs, bool):
                    raise ValueError(f"{pwhere}: 'case_sensitive' must be a boolean")
                check_zed_patterns(display, display, pat, pwhere)
                approximated = True
        extra = set(cfg) - {"default", "always_allow", "always_deny", "always_confirm"}
        if extra:
            warn(display, f"{where}: unknown key(s) {sorted(extra)}")
    if approximated:
        note(display, "Zed patterns were validated with Python re as an approximation "
                      "of Rust regex — a passing compile is necessary, not sufficient")

# ---------- VS Code ----------

def check_vscode(path, display, data):
    ta = data.get("chat.tools.terminal.autoApprove")
    if ta is not None:
        if not isinstance(ta, dict):
            raise ValueError("'chat.tools.terminal.autoApprove' must be an object")
        for cmd, v in ta.items():
            if cmd.startswith("/") and cmd.endswith("/") and len(cmd) >= 2:
                try:
                    re.compile(cmd[1:-1])
                except re.error as e:
                    raise ValueError(f"terminal.autoApprove key '{cmd}': bad /regex/ key: {e}")
            if isinstance(v, bool):
                continue
            if isinstance(v, dict):
                if "matchCommandLine" in v and not isinstance(v["matchCommandLine"], bool):
                    raise ValueError(f"terminal.autoApprove['{cmd}']: 'matchCommandLine' must be boolean")
                extra = set(v) - {"matchCommandLine"}
                if extra:
                    warn(display, f"terminal.autoApprove['{cmd}']: unrecognized object key(s) {sorted(extra)}")
                continue
            raise ValueError(f"terminal.autoApprove['{cmd}']: value must be boolean or object "
                             f"(/regex/ patterns belong in the KEY, not the value)")
    ua = data.get("chat.tools.urls.autoApprove")
    if ua is not None:
        if not isinstance(ua, dict):
            raise ValueError("'chat.tools.urls.autoApprove' must be an object")
        for url, v in ua.items():
            if isinstance(v, bool):
                continue
            if isinstance(v, dict):
                for k in ("approveRequest", "approveResponse"):
                    if k in v and not isinstance(v[k], bool):
                        raise ValueError(f"urls.autoApprove['{url}']: '{k}' must be boolean")
                extra = set(v) - {"approveRequest", "approveResponse"}
                if extra:
                    warn(display, f"urls.autoApprove['{url}']: unknown key(s) {sorted(extra)} "
                                  f"(expected approveRequest/approveResponse)")
                continue
            raise ValueError(f"urls.autoApprove['{url}']: value must be boolean or object")

# ---------- run ----------

for path in sys.argv[1:]:
    CURRENT = 0  # per-file warning counter (reset by assignment at module scope)
    display = "<stdin>" if path == "-" else path
    checks = classify(path)
    is_zed = "zed" in checks
    is_vscode = "vscode" in checks
    is_opencode = "opencode" in checks
    kind = None
    had_error = False
    try:
        data, kind = parse(path, display,
                           allow_jsonc_fallback=(is_vscode or is_opencode or
                                                 path.endswith(".jsonc")))
        if path == "-":
            checks = classify(path, data)
            is_zed = "zed" in checks
            is_vscode = "vscode" in checks
            is_opencode = "opencode" in checks
            if checks:
                note(display, f"stdin classified by content as: {', '.join(sorted(checks))}")
        if is_opencode:
            check_opencode(path, display, data)
        if is_zed:
            check_zed(path, display, data)
        if is_vscode:
            check_vscode(path, display, data)
    except ValueError as e:
        fail(display, str(e))
        had_error = True
    except Exception as e:  # unreadable file, encoding error, etc.
        fail(display, f"{type(e).__name__}: {e}")
        had_error = True
    if not had_error:
        if CURRENT > 0:
            print(f"PASS-WITH-WARNINGS: {display} ({kind}; {CURRENT} warning(s))")
        else:
            print(f"OK: {display} ({kind})")

if ERRORS:
    sys.exit(1)
if WARNINGS:
    sys.exit(3)
sys.exit(0)
PYEOF
