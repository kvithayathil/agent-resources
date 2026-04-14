# Agent Resources

![CI](https://github.com/kvithayathil/agent-resources/actions/workflows/check.yml/badge.svg)
![Tests](https://img.shields.io/badge/tests-208%2F208-brightgreen)
![Lint](https://img.shields.io/badge/ruff-clean-brightgreen)
![VSDD](https://img.shields.io/badge/VSDD-converged-blue)
![Python](https://img.shields.io/badge/python-3.12+-blue)
![License](https://img.shields.io/badge/license-AGPL--3.0-blue)

Agent skills management — install, index, search, validate, update. Follows the [AgentSkills](https://agentskills.io) spec.

## Quick Start

```bash
just setup                    # install deps (uv + Python)

# Skills workflow
just install anthropics/skills --skill pdf   # install from remote
just search "extract text from pdf"          # find a skill
just sync                                    # rebuild index
just check                                   # full quality gate
```

## Commands

| Recipe | What it does |
|---|---|
| `just setup` | Bootstrap Python deps via uv |
| `just install <source>` | Install skill(s) from remote repo |
| `just update` | Update installed skills |
| `just check-updates` | Check for available updates |
| `just sync` | Rebuild `SKILL_INDEX.yaml` |
| `just validate` | Validate skills against spec |
| `just check` | Full gate: lint + typecheck + deadcode + dupes + audit + validate |
| `just search <query>` | Fuzzy search by task description |
| `just lookup <name>` | Exact skill lookup |
| `just list` | List all indexed skills |

## Structure

```
skills/
├── SKILL_INDEX.yaml          # Auto-generated lookup index
├── skills-lock.json          # Remote skill provenance (committed)
├── scripts/
│   ├── skill-manager         # CLI entry point
│   ├── sync-index.py         # Index, search, validation
│   └── providers/
│       ├── common.sh         # Shared lock file helpers
│       └── npx-skills.sh     # Default provider (wraps `npx skills`)
├── .templates/               # Scaffold for new skills
└── <skill-name>/             # Installed or authored skills
```

## Adding a Skill

```bash
cp -r skills/.templates/skill-name-\(template\) skills/my-skill
# edit skills/my-skill/SKILL.md
just sync
just validate my-skill
```

## Provider System

Install/update/check delegates to a **provider** (default: `npx skills`). Swap via `SKILLS_PROVIDER` env var. See [docs/skill-manager.md](docs/skill-manager.md).

## Quality Tools

| Tool | What |
|---|---|
| ruff | Linting + formatting |
| basedpyright | Type checking |
| vulture | Dead code |
| pylint | Code duplication |
| jscpd | Copy-paste detection |
| pip-audit | Vulnerability scan |

## Documentation

- [Skill format reference](docs/skill-format.md) — SKILL.md frontmatter, extensions, progressive disclosure
- [Skill manager](docs/skill-manager.md) — provider interface, provenance, search scoring
- [Validation](docs/validation.md) — spec checks, quality toolchain details

## Requirements

- [just](https://github.com/casey/just) — task runner
- [uv](https://docs.astral.sh/uv/) — Python dependency management
- [jq](https://jqlang.org/) — lock file operations in provider scripts
- [npx](https://docs.npmjs.com/cli/v9/commands/npx) — default skill provider (`npx skills`)
