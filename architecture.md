---
title: "Project Architecture and Conventions"
tags: ["architecture", "conventions", "skills", "tooling"]
sources: []
contributors: ["Jm2A"]
created: 2026-04-18
updated: 2026-04-25
---


This project is a Python-based skill management system for AI coding agents following the AgentSkills spec.

## Commands
- **Justfile is source of truth** — use \`just <recipe>\` over raw commands
- \`just check\` — full quality gate (ruff, basedpyright, vulture, pylint, jscpd, pip-audit, validate)
- \`just sync\` — rebuild SKILL_INDEX.yaml
- \`just provenance\` — audit remote skills for SOURCE.md compliance
- \`just upstream-check\` — check VDD/VSDD gists for updates

## Skill Categories

| Category | Examples | Notes |
|----------|----------|-------|
| Authored (self-learning) | vdd, vsdd, security | Agent may modify references/ |
| Authored (tooling) | provenance-tracking, security-scan | Maintains skill lifecycle |
| Remote (modified) | vdd, vsdd | Adapt upstream gists, check for updates |
| Remote (unmodified) | qa, write-a-prd, grill-me | Installed from mattpocock/skills etc. |
| Android family | android/* | KMP patterns, 9 sub-skills (incl. android-layouts) |

## Provider System
- Default: npx-skills (wraps npx skills add/update/check)
- Swap via SKILLS_PROVIDER env var
- All providers use common.sh helpers for lock file ops

## Gotchas
- Path has spaces (03 - Resources/agent-resources) — always quote paths
- YAML auto-parses unquoted ISO timestamps as datetime — always quote them
- skills-lock.json is canonical provenance; SOURCE.md is derived
- .cache/ dirs inside skills are local state, gitignored
- detect_secrets_engine missing from codescanner upstream — needs sed fix
