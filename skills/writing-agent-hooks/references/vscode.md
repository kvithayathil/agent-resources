# VS Code: Agent Hooks

**Canonical URL:** https://code.visualstudio.com/raw/docs/agent-customization/hooks.md

## Where hooks live

VS Code: searches for hook JSON files in several locations:

- `.github/hooks/*.json` — project workspace hooks
- `.claude/settings.json` and `.claude/settings.local.json` — Claude-compatible settings
- `~/.copilot/hooks` — user-level hooks
- `hooks` field in custom agent `.agent.md` frontmatter — agent-scoped hooks
- Plugin `hooks.json` or `hooks/hooks.json`

Workspace hooks take precedence over user hooks for the same event.

## Format

A JSON file with a `hooks` object mapping event names to arrays of command objects:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "type": "command",
        "command": "npx prettier --write .",
        "timeout": 30
      }
    ]
  }
}
```

## Lifecycle events

| Event | When it fires |
|---|---|
| `SessionStart` | First prompt of a new session |
| `UserPromptSubmit` | User submits a prompt |
| `PreToolUse` | Before a tool call runs |
| `PostToolUse` | After a tool call succeeds |
| `PreCompact` | Before context is compacted |
| `SubagentStart` | Subagent is spawned |
| `SubagentStop` | Subagent completes |
| `Stop` | Session ends |

## Input and output

The hook receives a JSON object on stdin with common fields:

| Field | Description |
|---|---|
| `timestamp` | ISO 8601 timestamp |
| `cwd` | Working directory |
| `session_id` | Session identifier |
| `hook_event_name` | Name of the event |
| `transcript_path` | Path to the session transcript (optional) |

The hook can return JSON on stdout:

```json
{
  "continue": false,
  "stopReason": "Security policy violation",
  "systemMessage": "This operation is not allowed"
}
```

## Exit codes

| Exit code | Meaning |
|---|---|
| `0` | Success; parse stdout as JSON |
| `2` | Blocking error; stop and show error to model |
| Other non-zero | Non-blocking warning; show warning to user and continue |

## Example: block dangerous shell commands

**.github/hooks/security.json:**

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "type": "command",
        "command": "./scripts/block-dangerous.sh",
        "timeout": 5
      }
    ]
  }
}
```

**scripts/block-dangerous.sh:**

```bash
#!/bin/bash
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name')
TOOL_INPUT=$(echo "$INPUT" | jq -r '.tool_input')

if [ "$TOOL_NAME" = "runTerminalCommand" ]; then
  COMMAND=$(echo "$TOOL_INPUT" | jq -r '.command // empty')
  if echo "$COMMAND" | grep -qE '(rm\s+-rf|DROP\s+TABLE|DELETE\s+FROM)'; then
    echo '{"hookSpecificOutput":{"permissionDecision":"deny","permissionDecisionReason":"Destructive command blocked by security policy"}}'
    exit 0
  fi
fi

echo '{"continue":true}'
```

## Security notes

- Use `chat.tools.edits.autoApprove` to prevent the agent from editing hook scripts without approval.
- Validate `tool_input` with `jq` before passing fields to the shell.
- Prefer exit code `2` for simple blocking errors; use JSON output only when you need fine-grained control.
