---
name: writing-agent-hooks
description: >
  Guide for writing agent hooks across OpenCode, VS Code:, Polytoken, and Claude.
  Use when creating, reviewing, or refactoring hooks; choosing a platform; setting up
  a cross-platform hook; or when the user mentions agent hooks, hook scripts,
  PreToolUse, PostToolUse, .github/hooks, .claude/settings.json, .polytoken/hooks.json,
  or OpenCode plugins.
triggers:
  - agent hook
  - hook script
  - write a hook
  - PreToolUse
  - PostToolUse
  - .github/hooks
  - .claude/settings.json
  - .polytoken/hooks.json
  - opencode plugin
  - agent customization
  - hook security
tags:
  - agent-hooks
  - hooks
  - security
  - cross-platform
  - customization
license: Apache-2.0
metadata:
  author: agent-resources
  version: "0.1.0"
  living: "true"
  self-learning: "true"
  self-updating: "true"
  update-policy: "periodic-remote-check"
  last-reviewed: "2026-07-25"
---

# Writing Agent Hooks

## Overview

Agent hooks are deterministic code that runs at specific lifecycle points in an agent session. They can observe events, add context, enforce policies, or stop actions outright.

Use this skill when the user wants to create, review, or refactor hooks for OpenCode, VS Code:, Polytoken, or Claude. For simple git commit hooks, use `setup-pre-commit` or `modern-git-patterns` instead.

## The universal hook pattern

To keep a hook maintainable across platforms, put the actual logic in a platform-agnostic script under `.agents/hooks/scripts/` and wire each platform-specific configuration to call it.

Benefits:
- One source of truth for the hook logic.
- Easier to test outside of the agent loop.
- Easier security review and audit.
- Simpler porting when the project needs to support a new platform.

See `references/universal-hook-pattern.md` for a complete example.

## Security checklist

- [ ] **Least privilege**: the hook runs with the user's shell permissions; limit filesystem and network access.
- [ ] **Input validation**: never trust the JSON passed on stdin; validate fields and escape commands/paths before using them.
- [ ] **No secrets in hooks**: use environment variables or a secret manager; never commit secrets to hook files or configs.
- [ ] **Restrict self-modification**: require manual approval for edits to `.agents/hooks/` and platform hook files.
- [ ] **Audit and logging**: log tool invocations, denials, and errors to a durable, append-only log.
- [ ] **Fail-safe defaults**: on blocking events, an error should deny or stop the guarded action, not silently allow it.
- [ ] **Supply-chain hygiene**: review any npm dependencies used by OpenCode plugins before adding them.

For a deeper threat model, see `references/security-for-hooks.md` and the `security` / `security-best-practices` skills.

## Platform-specific guidance

| Platform | Config file(s) | Reference |
|---|---|---|
| OpenCode | `.opencode/plugins/`, `opencode.json` | `references/opencode.md` |
| VS Code: | `.github/hooks/*.json`, `.claude/settings.json`, `~/.copilot/hooks` | `references/vscode.md` |
| Polytoken | `hooks.json`, `.polytoken/hooks.json` | `references/polytoken.md` |
| Claude | `.claude/settings.json`, plugin `hooks/hooks.json`, skill/agent frontmatter | `references/claude.md` |

## Self-improvement / freshness protocol

This skill is self-updating. Platform docs evolve, so periodically run `scripts/check-references.sh` to fetch the upstream pages and compare hashes.

```bash
bash skills/writing-agent-hooks/scripts/check-references.sh
```

On `CHANGED`, review the diff in `assets/` and update the curated `references/*.md` files. Record semantic updates in `references/CHANGELOG.md` and bump `last-reviewed` in `SKILL.md` frontmatter. Run with `--update` to refresh the cached upstream copies:

```bash
bash skills/writing-agent-hooks/scripts/check-references.sh --update
```

Trigger a freshness check when:
- `last-reviewed` is more than 7 days old.
- The user asks to update hook references.
- A platform announces hooks-related changes.

## Agent workflow

1. Identify the platform and the lifecycle event that should trigger the hook.
2. Decide whether the hook must **block** the action or can be **fire-and-forget**.
3. Write the platform-agnostic logic under `.agents/hooks/scripts/<hook-name>.sh` (or equivalent).
4. Wire the platform-specific configuration to call that script.
5. Test the hook manually by triggering the event and inspecting the platform's hook logs.
6. Run the security checklist above.

## Common mistakes

| Mistake | Fix |
|---|---|
| Duplicating logic across platform configs | Use the universal pattern and a shared script. |
| Letting the agent edit its own hook scripts | Require approval for edits under `.agents/hooks/` and platform hook directories. |
| Hardcoding secrets | Move secrets to environment variables or a secret manager. |
| Ignoring exit-code / JSON contracts | Match the platform's documented output format. |
| Using blocking hooks for long-running side effects | Use fire-and-forget events for logging, notifications, or telemetry. |

## References

- `references/opencode.md` — OpenCode plugin hooks
- `references/vscode.md` — VS Code: agent hooks
- `references/polytoken.md` — Polytoken hooks
- `references/claude.md` — Claude hooks
- `references/universal-hook-pattern.md` — Shared-script layout
- `references/security-for-hooks.md` — Hook-specific security guidance
- `references/CHANGELOG.md` — Reference update history
