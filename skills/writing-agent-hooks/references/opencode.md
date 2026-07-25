# OpenCode Plugin Hooks

**Canonical URL:** https://opencode.ai/docs/plugins/

## Where hooks live

OpenCode plugins are JavaScript/TypeScript modules loaded from:

- `.opencode/plugins/` — project-level plugins
- `~/.config/opencode/plugins/` — global plugins
- npm packages listed in `opencode.json`

## Format

A plugin exports a function that receives a context object and returns a hooks object:

```ts
import type { Plugin } from "@opencode-ai/plugin"

export const MyPlugin: Plugin = async ({ project, client, $, directory, worktree }) => {
  return {
    "tool.execute.before": async (input, output) => {
      // inspect or modify the tool call
    },
  }
}
```

## Common events

- Command: `command.executed`
- File: `file.edited`, `file.watcher.updated`
- Installation: `installation.updated`
- LSP: `lsp.client.diagnostics`, `lsp.updated`
- Message: `message.updated`, `message.removed`, `message.part.updated`, `message.part.removed`
- Permission: `permission.asked`, `permission.replied`
- Session: `session.created`, `session.compacted`, `session.updated`, `session.idle`, `session.error`, `session.diff`, `session.deleted`
- Shell: `shell.env`
- Tool: `tool.execute.before`, `tool.execute.after`
- TUI: `tui.prompt.append`, `tui.command.execute`, `tui.toast.show`

## Example: block reads of `.env`

```ts
// .opencode/plugins/env-protection.ts
export const EnvProtection = async () => {
  return {
    "tool.execute.before": async (input, output) => {
      if (input.tool === "read" && output.args.filePath.includes(".env")) {
        throw new Error("Do not read .env files")
      }
    },
  }
}
```

## Security notes

- Use `shescape` or equivalent when building shell commands from user input.
- Do not read or log secrets from `.env` files inside a plugin.
- Review npm dependencies in `.opencode/package.json` before installing them.
- Plugins run with the user's privileges; limit filesystem and network access.
