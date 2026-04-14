---
title: Self-Learning Enhancement — Universal Hooks
status: proposed
created: 2026-04-14
updated: 2026-04-14
applies-to:
  - vdd
  - vsdd
---

# Self-Learning Enhancement — Universal Hooks

## Problem

Self-learning skills need to trigger on lifecycle events (task completion, errors, session end). The Agent Skills spec has no universal hooks standard — each agent implements its own mechanism. Skills that rely on hooks lock themselves into a single agent (currently only Claude Code). Skills that don't use hooks rely on the agent remembering to follow instructions, which is unreliable under context pressure or in long sessions.

## Proposed Solution

A **dual-trigger pattern** with two layers:

- **Layer 1 (Universal):** Instruction-based triggers embedded in SKILL.md. Works on every agent. Already implemented in vdd/vsdd.
- **Layer 2 (Agent-specific):** Optional hook configs and scripts in `references/hooks/`. Only wired up for agents that support hooks.

The agent uses Layer 1 by default. When hooks are available, Layer 2 provides more reliable auto-triggering.

### Layer 1: Universal — Works Everywhere

Already embedded in vdd/vsdd SKILL.md files:

```markdown
### Self-Update Triggers

Perform a self-update cycle when ANY of these occur:

- A test passed but a bug still shipped (verification gap)
- A new verification tool or technique proved useful
- A gotcha was discovered that wasn't in the skill
- A pattern was followed successfully 3+ times (promote to instruction)
- An instruction was ignored by the agent 3+ times (rewrite or remove it)
- A user corrected the agent's verification approach
```

**Pros:** Works on every agent. No config required.
**Cons:** Agent may skip triggers under context pressure.

### Layer 2: Agent-Specific Hooks

Pre-built hook configs in each skill's `references/hooks/` directory:

#### Claude Code

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "bash ${SKILL_DIR}/references/hooks/on-error.sh \"$TOOL_OUTPUT\" \"$EXIT_CODE\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "bash ${SKILL_DIR}/references/hooks/on-session-end.sh"
          }
        ]
      }
    ]
  }
}
```

Wire by merging into `~/.claude/settings.json`.

#### Hook Scripts

**`references/hooks/on-error.sh`** — Triggers self-correction on Bash failures:

```bash
#!/usr/bin/env bash
OUTPUT="$1"
EXIT_CODE="$2"

if [ "$EXIT_CODE" -ne 0 ]; then
  ERROR_LOG="$(mktemp)"
  cat > "$ERROR_LOG" <<EOF
{
  "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "exit_code": $EXIT_CODE,
  "output": $(echo "$OUTPUT" | head -100 | jq -Rs .)
}
EOF
  echo "[self-learning] Error captured. Agent should review and update skill if guidance was incorrect."
  echo "Error log: $ERROR_LOG"
fi
```

**`references/hooks/on-session-end.sh`** — Consolidates learning at session end:

```bash
#!/usr/bin/env bash
echo "[self-learning] Session ending. Review recent interactions for patterns to promote or correct."
echo "Check references/LESSONS_LEARNED.md for entries ready to promote (3+ validations)."
```

### Agent Hook Compatibility Matrix

| Agent | Hook Support | Mechanism | Config Location | Layer 2 Possible |
|-------|-------------|-----------|-----------------|-------------------|
| Claude Code | Yes | PreToolUse/PostToolUse/Stop | `~/.claude/settings.json` | Yes |
| OpenCode | No | — | — | No |
| Codex | No | — | — | No |
| Cursor | No | — | — | No |
| Gemini CLI | Partial | Extensions (different model) | `~/.gemini/` | Future |
| Roo Code | No | — | — | No |
| Windsurf | No | — | — | No |
| Cline | No | — | — | No |
| Amp | No | — | — | No |
| Goose | No | — | — | No |

## Alternatives Considered

1. **Hooks only (no Layer 1 instructions).** Rejected — locks skills into Claude Code, breaks portability.
2. **Instructions only (no hooks).** Already the default. Enhancement adds hooks as optional reliability layer.
3. **Wait for agentskills.io hooks spec.** Rejected — no indication this is coming soon, and skills need to work now.

## Impact

- **Skills modified:** vdd, vsdd (and any future self-learning skill)
- **New files:** `references/hooks/` directory in each skill, plus hook scripts
- **Dependencies:** `jq` for error log formatting in hook scripts (optional, degrades gracefully)
- **Breaking changes:** None — purely additive
- **Affected agents:** All (Layer 1), Claude Code specifically (Layer 2)

## Implementation Plan

- [ ] Create `references/hooks/` in vdd skill
- [ ] Create `references/hooks/` in vsdd skill
- [ ] Add `on-error.sh` to each skill's hooks directory
- [ ] Add `on-session-end.sh` to each skill's hooks directory
- [ ] Add `claude-code-settings.json` to each skill's hooks directory
- [ ] Update SKILL.md references section to mention hook scripts
- [ ] Test Layer 2 hooks with Claude Code
- [ ] Verify Layer 1 still works independently on other agents
- [ ] Update this enhancement status to `complete`

## Success Criteria

1. Self-learning triggers fire reliably on Claude Code with hooks wired
2. Self-learning triggers still work (manually) on agents without hooks
3. Hook scripts produce actionable output (error context, promotion candidates)
4. No regression in skill behavior when hooks are absent

## Open Questions

1. Should hook scripts write directly to `LESSONS_LEARNED.md` or only output to stdout for the agent to process? (Leaning: stdout only — keeps agent in control)
2. Is there value in a pre-task hook (Layer 2 equivalent of "load relevant patterns before starting")? — **Does not block implementation.**

## References

- [agentskills.io/specification](https://agentskills.io/specification)
- [charon-fan/agent-playbook — self-improving-agent](https://github.com/charon-fan/agent-playbook) (reference implementation using Claude Code hooks)
- [skills.sh leaderboard](https://skills.sh) — 24.3K installs of self-improving-agent
