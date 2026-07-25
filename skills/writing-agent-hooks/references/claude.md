# Claude Hooks

**Canonical URL:** https://code.claude.com/docs/en/hooks.md

## Where hooks live

- `~/.claude/settings.json` — all projects on the machine
- `.claude/settings.json` — single project, shareable
- `.claude/settings.local.json` — single project, gitignored by default
- Plugin `hooks/hooks.json` — when the plugin is enabled
- Skill or agent frontmatter — while the component is active

Enterprise admins can use `allowManagedHooksOnly` to restrict user/project/plugin hooks.

## Format

Three levels of nesting: event → matcher group → handler array.

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "if": "Bash(rm *)",
            "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/block-rm.sh",
            "args": []
          }
        ]
      }
    ]
  }
}
```

## Lifecycle events

| Event | When it fires |
|---|---|
| `SessionStart` | Session begins or resumes |
| `UserPromptSubmit` | User submits a prompt |
| `PreToolUse` | Before a tool call executes |
| `PostToolUse` | After a tool call succeeds |
| `PostToolUseFailure` | After a tool call fails |
| `PostToolBatch` | After a batch of parallel tool calls resolves |
| `Stop` | Claude finishes responding |
| `PreCompact` | Before context compaction |
| `SessionEnd` | Session terminates |
| `SubagentStart` / `SubagentStop` | Subagent lifecycle |
| `FileChanged` | A watched file changes on disk |

## Matcher patterns

| Matcher | Evaluated as |
|---|---|
| `"*"`, `""`, or omitted | Match all |
| Letters, digits, `_`, `-`, spaces, `,`, `\|` | Exact string or list of exact strings |
| Any other character | JavaScript regular expression, unanchored |

For `PreToolUse`, the matcher filters on tool name. Wrap the pattern in `^...$` when you need a whole-string match.

## Handler types

- `command` — shell command, JSON on stdin/stdout
- `http` — POST the event JSON to a URL
- `mcp-tool` — call an MCP tool
- `prompt` — run an LLM prompt
- `agent` — dispatch a subagent

## Output for `PreToolUse`

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Destructive command blocked by hook"
  }
}
```

`permissionDecision` can be `allow`, `deny`, or `ask`.

## Example: deny `rm -rf`

**.claude/hooks/block-rm.sh:**

```bash
#!/bin/bash
COMMAND=$(jq -r '.tool_input.command')

if echo "$COMMAND" | grep -q 'rm -rf'; then
  jq -n '{
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: "Destructive command blocked by hook"
    }
  }'
else
  exit 0
fi
```

**.claude/settings.json:**

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "if": "Bash(rm *)",
            "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/block-rm.sh"
          }
        ]
      }
    ]
  }
}
```

## Security notes

- Protect `.claude/hooks/` and `.claude/settings.json` from agent edits; use policy settings if available.
- Be careful with regex matchers; unanchored patterns can match more than intended.
- `if` conditions use the same matching syntax; validate them before relying on them for security decisions.
