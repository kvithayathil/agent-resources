# Agent Resources

Skills management for AI coding agents following the [AgentSkills](https://agentskills.io) spec.

## Commands

```
just setup                     # Bootstrap deps
just install <source>          # Install skill(s)
just update                    # Update installed skills
just sync                      # Rebuild SKILL_INDEX.yaml
just validate [name]           # Validate skill(s)
just check                     # Full quality gate (lint+typecheck+audit+validate)
just search <query>            # Fuzzy search
just lookup <name>             # Exact lookup
just list                      # List indexed skills
```

## Structure

- `skills/` — Primary workspace. Skills live as `<name>/SKILL.md` or `<group>/<name>/SKILL.md`.
- `skills/android/` — Android/KMP skills (8 skills: compose-ui, data-layer, di-koin, error-handling, module-structure, navigation, presentation-mvi, testing).
- `skills/.templates/` — Scaffold for new skills. Copy, edit, `just sync`.
- `skills/scripts/` — CLI, sync, providers (recursive scanning supported).
- `docs/` — Reference docs. Start with `skill-format.md` and `skill-manager.md`.
- `docs/enhancements/` — Proposals. Copy `_template.md` to start new.
- `research/` — Notes & findings. See `research/README.md`.
- `security_layer/` — Python security module (own venv + pyproject.toml).
- `tests/` — Test suite.

## Conventions

- **Justfile** is the single source of truth. Prefer `just` over raw commands.
- **Quality gate**: ruff → basedpyright → vulture → pylint → jscpd → pip-audit → skill validation.
- **Self-learning skills** (vdd, vsdd): agent may modify `references/` files based on real-world evidence.
- **Enhancements**: frontmatter status tracking. See `docs/enhancements/_template.md`.

## Auto-Update

This file and related indexes should be kept in sync with reality. Update them when:

- **New skill added/removed** → update Structure list above, run `just sync`
- **New justfile recipe added/changed** → update Commands block above
- **New top-level directory created** → update Structure list above
- **New doc added to `docs/` or `docs/enhancements/`** → update `docs/enhancements/README.md` index
- **New research file added** → update `research/README.md` index
- **Enhancement status changes** → update frontmatter in the doc AND the index table in `docs/enhancements/README.md`

Do not wait to be asked. If you created the change, update the relevant index.
