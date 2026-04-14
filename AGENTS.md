# Agent Resources

Skills management for AI coding agents following the [AgentSkills](https://agentskills.io) spec.

## Quick Reference

- Commands: `just --list` or see `justfile`
- Skill catalog: `skills/SKILL_INDEX.yaml` (auto-generated, run `just sync` to rebuild)
- Provenance: `skills/skills-lock.json`
- Skill format: `docs/skill-format.md`
- Enhancement proposals: `docs/enhancements/` (see `_template.md` for spec)
- Research: `research/README.md`

## Agent-Specific Conventions

- **Justfile** is the command source of truth. Use `just` over raw commands.
- **Quality gate**: `just check` runs ruff → basedpyright → vulture → pylint → jscpd → pip-audit → skill validation.
- **Skills** may live as `skills/<name>/SKILL.md` or `skills/<group>/<name>/SKILL.md` (recursive scanning).
- **Self-learning skills** (vdd, vsdd, security): agent may modify `references/` files based on real-world evidence.
- **Self-updating skills** (security): run freshness checks when `last-reviewed` is >7 days old. See SKILL.md for update commands.

## Auto-Update

Keep indexes in sync when changes are made. Do not wait to be asked.

- **New skill added/removed** → run `just sync`
- **New justfile recipe** → no action needed (agent can run `just --list`)
- **New top-level directory** → update Structure list in `README.md`
- **New enhancement** → update `docs/enhancements/README.md` index
- **New research file** → update `research/README.md` index
- **Enhancement status change** → update frontmatter AND index table in `docs/enhancements/README.md`
