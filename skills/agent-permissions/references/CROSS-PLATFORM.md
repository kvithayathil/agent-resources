# Cross-Platform Permission Translation

Load when applying one intent across multiple tools, comparing policies, or porting
a policy between OpenCode V2, VS Code, and Zed.

## Intent → dialect table

One intent per row; syntax shown per tool in the JSON examples block below (patterns
are kept OUT of table cells — escaped pipes inside GFM cells decode wrong and
silently break regexes). Adapt to the user's actual commands; gate 1 diff approval
still applies. None of the "allow" rows below are read-only guarantees — see
Shell-pattern hazards in opencode.md/zed.md and the pitfalls checklist.

| Intent | OpenCode V2 (`opencode.jsonc`) | VS Code (`.vscode/settings.json`) | Zed (`.zed/settings.json`) |
| --- | --- | --- | --- |
| Auto-allow git view commands | allow rules for `git status *` etc., placed after a global ask baseline; residual write risk via output flags | autoApprove map entries set to `true` for the literal commands | `always_allow` regex anchored to the view subcommands |
| Block push | `deny` rule placed after any broader shell rules (last match wins) | settings cannot block: `false` forces a prompt; a real block needs a preToolUse hook denial | `always_deny` regex |
| Protect `.env` | `read` deny rules; note a read deny does not cover `cat .env` via shell — add shell denies too | NO file-level deny exists — approval feature or preToolUse hook (see vscode.md) | `edit_file`/`write_file` `always_deny` path regexes; terminal reads governed by the global default |
| Confirm `sudo` | `ask` rule | `false` entry (prompt, not block) | `always_confirm` regex |
| Allowlist one MCP tool | action is `<server>_<tool>` with resource `*` — NO MCP wildcard exists, list each tool individually; unlisted MCP tools fall through to the base policy (allowed unless you added the ask baseline) | `chat.tools.eligibleForAutoApproval` entry set to `false` (means: always ask this one) | `mcp:<server>:<tool>` with a `default` — default only, no patterns |
| Deny outside-project access | `external_directory` ask rule (default is silent allow — gap) | n/a — sandbox network/workspace limits cover this | n/a — worktree trust gate covers scope |

### Intent examples (full syntax)

```jsonc
// OpenCode V2 — ask baseline FIRST, allows after, denies last (last match wins)
{
  "permissions": [
    { "action": "*", "resource": "*", "effect": "ask" },
    { "action": "read", "resource": "*", "effect": "allow" },
    { "action": "read", "resource": "*.env", "effect": "deny" },
    { "action": "read", "resource": "*.env.*", "effect": "deny" },
    // whole-value matching: BOTH forms needed — bare covers root level,
    // */-prefixed covers nested directories (see opencode.md pitfall note)
    { "action": "read", "resource": ".secrets/*", "effect": "deny" },
    { "action": "read", "resource": "*/.secrets/*", "effect": "deny" },
    { "action": "read", "resource": "secrets/*", "effect": "deny" },
    { "action": "read", "resource": "*/secrets/*", "effect": "deny" },
    { "action": "shell", "resource": "git status *", "effect": "allow" },
    { "action": "shell", "resource": "git push*", "effect": "deny" },
    { "action": "shell", "resource": "sudo *", "effect": "deny" },
    { "action": "external_directory", "resource": "*", "effect": "ask" },
    { "action": "<server>_<tool>", "resource": "*", "effect": "allow" } // one per MCP tool
  ]
}
```

VS Code — prompts, not blocks; real blocking needs a hook (`.vscode/settings.json`,
JSONC tolerated):

```json
{
  "chat.tools.terminal.autoApprove": {
    "git status": true,
    "git diff": true,
    "/^(rm|sudo|git\\s+push)\\b/": false
  }
}
```

Zed — strict JSON, fixed ladder, file order irrelevant (`.zed/settings.json` — no
comments allowed in the file itself):

```json
{
  "agent": {
    "tool_permissions": {
      "default": "confirm",
      "tools": {
        "terminal": {
          "always_allow": [{ "pattern": "^(git (status|diff|show|log))($| )" }],
          "always_deny": [{ "pattern": "^git push\\b" }],
          "always_confirm": [{ "pattern": "^sudo\\b" }]
        },
        "edit_file": {
          "always_deny": [
            { "pattern": "\\.env($|\\.)" },
            { "pattern": "(^|/)\\.?secrets/" }
          ]
        },
        "mcp:<server>:<tool>": { "default": "confirm" }
      }
    }
  }
}
```

## Semantic differences

| Dimension | OpenCode V2 | VS Code (Copilot) | Zed |
| --- | --- | --- | --- |
| Precedence model | ordered list, **last** matching rule wins; unmatched actions are ALLOWED (base policy starts allow-all) — start with a global ask rule; layers append project → global → agent, so global/agent can override project; org policies hard-deny last | level (`manual`/`assisted`/`allowAll`) is session-picked; terminal map: `false` forces approval, `false` beats `true` in compounds | fixed ladder: built-in > always_deny > always_confirm > always_allow > tool default > global default; file order irrelevant; a project `always_allow` is beaten by built-in rules, `always_deny`, AND `always_confirm` from any layer |
| Pattern language | whole-value wildcards only: `*` (spans `/`), `?` | literal strings or `/regex/` in the autoApprove map | Rust regex, **case-insensitive by default**, explicit anchoring recommended |
| Deny availability | real `deny` effect | **no real deny in settings** — `false` = requires approval; blocking = preToolUse hook denial | real `always_deny`, but only built-in rules and denies beat project-level allows |
| MCP tool naming | action `<server>_<tool>` (unsupported chars → `_`), resource `*`; no wildcard — list each tool | tool IDs in `chat.tools.eligibleForAutoApproval` | `mcp:<server>:<tool>`, default-only |
| Compound commands | scanner extracts subcommands + `cd` targets; each matched whole-value; trailing ` *` also matches the bare command | auto-approve only when ALL subcommands `true` and none `false` | parsed per subcommand across shells |
| Merge layers | project → global → agent appended; project cannot override a global deny | workspace settings always yield to enterprise-managed/device policy | project merges ON TOP of user settings — project rules can widen too |
| Secrets defaults | asks on `*.env`/`*.env.*` reads; `.env.example` allowed | NO file-level read/edit deny exists — approval feature or preToolUse hook only | shipped examples commented out — inert until enabled |

## Translation pitfalls checklist

When porting one policy across tools, walk this list — each item is a real trap:

- [ ] **Deny availability**: a VS Code "block" is not a block. Translate OpenCode/Zed
      `deny` rules into prompts + note that only a preToolUse hook hard-blocks.
- [ ] **Direction of precedence**: OpenCode wants broad-then-narrow (last wins); Zed
      order doesn't matter (ladder); VS Code `false` beats `true` in compounds.
      Copy-pasting ordering assumptions across tools breaks intent silently.
- [ ] **Pattern dialect**: wildcard `*` spans `/` in OpenCode; `/…/` regex in VS Code;
      Rust regex in Zed is case-insensitive by default. Re-anchor and re-escape —
      never translate patterns literally.
- [ ] **MCP naming**: three different naming schemes; a tool name valid in one tool
      is meaningless in another. Sanitize per the target tool's scheme.
- [ ] **Merge direction**: porting a rule to Zed *project* config widens every
      clone; porting to OpenCode assumes global/agent rules may still override it;
      porting to VS Code assumes enterprise policy may still override it.
- [ ] **Secrets defaults differ**: OpenCode protects `.env` reads out of the box;
      VS Code and Zed protect nothing until you write it (gate 4 — always add it).
      A `read` deny does not cover shell access (`cat .env`) — shell is a separate
      action in OpenCode and governed by the global default in Zed.
- [ ] **"Read-only" claims**: allowlisted commands can still write via redirection,
      pipes, output flags (`git diff --output=`), or project-controlled scripts
      (`npm run`, `cargo build`). Test a redirection variant before describing any
      allow as read-only to the user.
- [ ] **Pattern placement in docs**: never embed regex patterns in GFM table cells —
      a JSON `"\\|"` alternation decodes to a literal-pipe regex and silently
      matches nothing. Use fenced code blocks (as in the examples above).
- [ ] **External-directory gap**: OpenCode's `external_directory` silently allows
      out-of-project access by default; the other tools scope by workspace/worktree.
- [ ] **Verify per tool**: each tool's verification steps differ (its reference file
      has them) — a policy port is not done until verified in the target tool.
