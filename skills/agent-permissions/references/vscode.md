# VS Code (Copilot Agent Mode) Permissions

Verified against https://code.visualstudio.com/docs/agents/run/approvals and
https://code.visualstudio.com/docs/agents/reference/ai-settings. Re-verify with
`scripts/check-upstream.sh` before trusting details older than the snapshot date.

## Config location and enforcement caveat

- Project config: `.vscode/settings.json` (JSONC — comments and trailing commas
  allowed).
- Workspace settings are **shared by every user of the project**: a rule you write
  changes behavior on teammates' machines too. State this when presenting a diff.
- **CRITICAL CAVEAT**: enterprise-managed and device-policy settings always override
  workspace settings. A workspace rule is convenience, not enforcement — it cannot
  tighten what admin policy loosens. Say so when the user expects hard enforcement.

## Permission levels

`chat.permissions.default`: `"manual"` | `"assisted"` | `"allowAll"`.

- The level is picked per session by the user; `default` only sets the starting
  choice. `allowAll` + Autopilot skips prompts, but the **sandbox still restricts**
  execution — permission level and sandbox are independent layers.
- Never recommend `allowAll` as a project default without the user explicitly
  accepting the loss of confirmation prompts.

## Terminal auto-approve

```jsonc
{
  "chat.tools.terminal.autoApprove": {
    "git status": true,
    "git show": true,
    "/^(rm|del|Remove-Item)\\s+/": false,
    "sudo": false
  }
}
```

- Map of command → boolean. Literal strings match the command; `/…/` entries are
  regex patterns.
- **SEMANTIC TRAP**: a `false` entry means *requires approval* — it does **not**
  block. There is no terminal deny in settings; blocking requires a preToolUse hook
  denial. When the user asks to "block" a command in VS Code, the honest answer is:
  settings can force a prompt, a hook can hard-deny.
- Compound commands (`a && b`): auto-approved only when **all** subcommands match
  `true` entries and **none** matches a `false`. `false` takes precedence.
- `matchCommandLine: true` (object syntax) evaluates the full command line instead
  of per-command.
- Related settings:
  - `chat.tools.terminal.enableAutoApprove` — off means every command is approved
    manually.
  - `chat.tools.terminal.blockDetectedFileWrites` (experimental, default
    `outsideWorkspace`).
  - `chat.tools.terminal.autoApprove.ignoreDefaultAutoApproveRules` (experimental)
    — **dropping the built-in deny rules is dangerous**; never recommend enabling it.

### Common build-tool auto-approves

For "pre-approve the project's build/test entry points" (regex entries; compound
commands still need every subcommand to match a `true` entry):

```jsonc
{
  "chat.tools.terminal.autoApprove": {
    "/^(\\.\\/)?gradlew?\\s+(build|test|check)\\b/": true,
    "/^make\\b/": true,
    "/^cmake\\s+--build\\b/": true,
    "/^go\\s+(build|test|vet)\\b/": true,
    "/^just\\b/": true,
    "/^(npm|bun|pnpm|yarn)\\s+(run\\s+)?(test|lint|build)\\b/": true,
    "/^cargo\\s+(build|test|check)\\b/": true
  }
}
```

Same caveats as the other tools: every entry executes project-controlled code
(Makefiles, build.gradle, CMakeLists, justfiles, package scripts, tests) —
convenience for a trusted repo, never "read-only"; prefer narrow subcommands
over bare `cmake`/`go`; do not auto-approve `go run` (compiles and executes
arbitrary source). And remember `true` here auto-approves only — a `false`
entry forces approval, it never blocks.

**Setting-key caution**: a misspelled setting key is silently ignored, not reported
— verify key names against the settings UI or the upstream snapshot before trusting
a config.

## Tool approval

`chat.tools.eligibleForAutoApproval`: set a tool to `false` to always require manual
approval for that tool. Pre/post-approval state is managed via the
**Chat: Manage Tool Approval** command — send the user there to audit live approvals.

## URL approval (prompt-injection defense)

```jsonc
{
  "chat.tools.urls.autoApprove": {
    "https://example.com/docs/*": true,
    "https://internal.corp/*": {
      "approveRequest": true,
      "approveResponse": false
    }
  }
}
```

- Exact URLs, globs, and wildcards map to a boolean or an object.
- **TWO independent decisions**: `approveRequest` (agent may contact the URL) vs
  `approveResponse` (fetched content may enter the chat). Approving the request does
  NOT approve the response. Keep `approveResponse: false` for untrusted domains —
  fetched content is a prompt-injection channel into the conversation.

## Sandboxing (independent of permission level)

- `chat.agent.sandbox.enabled` — OS-level execution sandbox.
- `chat.agent.networkFilter`, `chat.agent.allowedNetworkDomains`,
  `chat.agent.deniedNetworkDomains` — network restrictions; **restart required**
  after changes.
- Recommend sandbox-on plus domain deny-lists as the actual hard boundary; prompts
  are the soft layer.

## What this is NOT (honest limits)

- Command detection is **best-effort, not a security boundary**: VS Code parses
  commands through a bash grammar even for zsh/fish shells, and obfuscation
  (quoting, substitutions, line continuations) can evade matching entirely.
- **Defaults already auto-approve** a set of common read-only commands even with an
  empty autoApprove map — audit the effective behavior, not just your rules.
- **Cloned-repo warning** (mirror of the Zed widening warning): a cloned repo can
  ship a `.vscode/settings.json` that turns on auto-approves on YOUR machine.
  Audit these files when entering any repo (gate 8).

## Secrets: what workspace settings cannot do

There is NO file-level read/edit deny mechanism in workspace settings. Protecting
sensitive files (`.env`, `*.env.*`, `*.pem`, `*.key`, `id_rsa`, `*.p12`, `*.pfx`,
`.netrc`, `.npmrc`, secrets directories) requires either:

- the "require approval before sensitive edits" capability (permission levels /
  sensitive-edit approval), or
- a **preToolUse hook denial** — the only real block. Shape is illustrative; consult
  the hooks doc for the current schema:

```jsonc
// preToolUse hook that denies a tool call — see
// https://code.visualstudio.com/docs/agent-customization/hooks
{
  "preToolUse": [
    { "tool": "terminal", "command": "secret-file-guard" } // deny when the call touches secret files
  ]
}
```

Do not overpromise: hooks are code the user must own and maintain, and the
sensitive-edit feature detects common cases, not all paths.

## Harness modes (out of scope for this file)

Claude/Codex harness permission modes are harness-level, not workspace-file driven.
The one workspace-visible exception, `allowDangerouslySkipPermissions`, must never
be recommended — flag it if present. Likewise never recommend
`chat.tools.global.autoApprove` or `/yolo` for project config.

## Worked example

Intent: frictionless git view commands, prompt before anything destructive, prompt
before untrusted fetch content.

```jsonc
{
  // git view commands run without asking — NOT read-only in any strict sense
  // (output flags can write files); keep the auto-approve set minimal
  "chat.tools.terminal.autoApprove": {
    "git status": true,
    "git show": true,
    "git diff": true,
    "git log": true,
    // false = approval required — NOT a block (use a preToolUse hook to block)
    "/^(rm|sudo|git\\s+push)\\b/": false
  },
  // internal docs may be fetched, but their content still needs a human OK
  "chat.tools.urls.autoApprove": {
    "https://docs.internal.example.com/*": {
      "approveRequest": true,
      "approveResponse": false
    }
  },
  "chat.tools.eligibleForAutoApproval": {
    "apply_patch": false
  },
  "chat.agent.sandbox.enabled": true
}
```

Effective policy: the four git view commands auto-run (not truly read-only — see
What this is NOT); `rm`/`sudo`/`git push` prompt; internal docs are fetchable but
content requires approval each time; `apply_patch` always asks; sandbox on. Remind
the user: these are prompts, not blocks — workspace settings also yield to
enterprise-managed policy, and defaults already auto-approve common read-only
commands beyond what this file lists.

## Verification steps (give the user these after writing)

1. **Developer: Reload Window** (settings changes apply on reload).
2. Run **Chat: Manage Tool Approval** — review the live approval table.
3. In agent mode, run a command matching a `true` rule (`git status`) — it executes
   without prompting.
4. Run a non-matching command — it prompts.
5. Run a `false`-matched command (`git push --dry-run`) — it prompts (approval
   required), confirming the rule matched.
