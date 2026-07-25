# Universal Hook Pattern

Instead of duplicating hook logic across platform-specific configs, keep the logic in a single platform-agnostic script under `.agents/hooks/scripts/` and point each platform at it.

## Recommended layout

```
<project-root>/
├── .agents/
│   └── hooks/
│       └── scripts/
│           └── block-dangerous.sh
├── .github/hooks/security.json       # VS Code:
├── .claude/settings.json             # Claude / VS Code:
├── .polytoken/hooks.json             # Polytoken
└── .opencode/plugins/security.ts     # OpenCode
```

## Shared script

`.agents/hooks/scripts/block-dangerous.sh` reads the event JSON from stdin and decides whether to allow a tool call. It returns the minimal output that each platform can interpret.

```bash
#!/usr/bin/env bash
set -euo pipefail

INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name // .tool // empty')
TOOL_INPUT=$(echo "$INPUT" | jq -r '.tool_input // .input // empty')

if [ "$TOOL_NAME" = "Bash" ] || [ "$TOOL_NAME" = "runTerminalCommand" ] || [ "$TOOL_NAME" = "bash" ]; then
  COMMAND=$(echo "$TOOL_INPUT" | jq -r '.command // empty')
  if echo "$COMMAND" | grep -qE 'rm\s+-rf|DROP\s+TABLE|DELETE\s+FROM'; then
    # VS Code: / Claude
    jq -n '{
      hookSpecificOutput: {
        hookEventName: "PreToolUse",
        permissionDecision: "deny",
        permissionDecisionReason: "Destructive command blocked by universal hook"
      }
    }'
    exit 0
  fi
fi

# Default: proceed
echo '{"continue":true}'
exit 0
```

Make the script executable:

```bash
chmod +x .agents/hooks/scripts/block-dangerous.sh
```

## Platform wiring

### VS Code:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "type": "command",
        "command": "../.agents/hooks/scripts/block-dangerous.sh",
        "cwd": "${workspaceFolder}/.github/hooks",
        "timeout": 5
      }
    ]
  }
}
```

### Claude

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
            "command": "${CLAUDE_PROJECT_DIR}/.agents/hooks/scripts/block-dangerous.sh"
          }
        ]
      }
    ]
  }
}
```

### Polytoken

```json
[
  {
    "name": "block-dangerous",
    "event": "pre_tool_use",
    "matcher": "bash|Bash|runTerminalCommand",
    "handler": {
      "bash": "${POLYTOKEN_PROJECT_DIR}/.agents/hooks/scripts/block-dangerous.sh"
    }
  }
]
```

### OpenCode

```ts
// .opencode/plugins/security.ts
import type { Plugin } from "@opencode-ai/plugin"

export const SecurityPlugin: Plugin = async (ctx) => {
  return {
    "tool.execute.before": async (input, output) => {
      const result = await ctx.$`.agents/hooks/scripts/block-dangerous.sh`
        .json(input) // passes the tool call as JSON to stdin
      if (result.hookSpecificOutput?.permissionDecision === "deny") {
        throw new Error(result.hookSpecificOutput.permissionDecisionReason)
      }
    },
  }
}
```

## Notes

- Normalize input differences across platforms in the shared script (e.g., `tool_name` vs `tool`, `tool_input` vs `input`).
- Keep the script fast and idempotent; it runs synchronously in the agent loop.
- Document the exit-code and JSON output contracts in the script header.
- Test the script from the shell first, then wire it into each platform.
