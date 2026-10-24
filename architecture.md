---
title: "Project Architecture and Conventions"
tags: ["architecture", "conventions", "skills", "tooling"]
sources: []
contributors: ["Jm2A"]
created: 2026-04-18
updated: 2026-10-24
---

This project is a Python-based skill management system for AI coding agents following the AgentSkills spec.

## Commands
- **Justfile is source of truth** — use `just <recipe>` over raw commands
- `just check` — full quality gate (ruff, basedpyright, vulture, pylint, jscpd, pip-audit, validate)
- `just sync` — rebuild SKILL_INDEX.yaml
- `just provenance` — audit remote skills for SOURCE.md compliance
- `just upstream-check` — check VDD/VSDD gists for updates; security and aaid ship their own upstream checkers (skills/<skill>/scripts/check-upstream.sh)

## Skill Categories

| Category | Examples | Notes |
|----------|----------|-------|
| Authored (self-learning) | vdd, vsdd, security, aaid | Agent may modify references/ |
| Authored (tooling) | provenance-tracking, security-scan | Maintains skill lifecycle |
| Remote (modified) | vdd, vsdd | Adapt upstream gists, check for updates |
| Remote (unmodified) | qa, write-a-prd, grill-me | Installed from mattpocock/skills etc. |
| Android family | android/* | KMP patterns, 9 sub-skills (incl. android-layouts) |

## Conventions
- Commit messages follow `docs/agent/git-commit-convention.md` — Conventional Commits format, no internal tracking references in commits or CHANGELOG
- `AGENTS.md` is the entry point for agent rules, auto-update duties, and knowledge-page etiquette

## security_layer
- LLM agent security mitigation package (trifecta separation, presidio/spaCy PII detection)
- `requires-python = ">=3.14, <3.15"`; Renovate holds python below 3.15 until the spaCy/presidio stack supports it (renovate.json packageRules)

## Provider System
- Default: npx-skills (wraps npx skills add/update/check)
- Swap via SKILLS_PROVIDER env var
