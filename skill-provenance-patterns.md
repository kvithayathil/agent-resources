---
title: "Skill Provenance and Update Patterns"
tags: ["provenance", "skills", "updates", "maintenance", "patterns"]
sources: []
contributors: ["Jm2A"]
created: 2026-04-18
updated: 2026-04-18
---

## Two Categories of Remote Skills

### Category A: Modified Third-Party
Local skill adapts an upstream source (gist, repo) with custom instructions.
- Structure: SKILL.md + assets/upstream.md + scripts/check-upstream.sh + references/
- On upstream change: agent classifies as semantic vs cosmetic. Semantic -> agent updates SKILL.md preserving local adaptations. Cosmetic -> only bump last-reviewed.
- Examples: vdd/ (gist 45c95ebf), vsdd/ (gist d8d3bc3e)

### Category B: Unmodified Third-Party
Verbatim copy from remote repo.
- Structure: SKILL.md + assets/upstream-SKILL.md + scripts/check-upstream.sh + references/
- On upstream change: --update overwrites SKILL.md with upstream, re-applies source: frontmatter.
- Examples: qa/, write-a-prd/, grill-me/ (from mattpocock/skills)

## Provenance Files
| File | Purpose | Source |
|------|---------|--------|
| skills-lock.json | Canonical provenance | Provider writes on install |
| references/SOURCE.md | Human-readable per skill | Derived from lock file |
| SKILL.md source: block | Frontmatter for index/search | Agent patches on install |
| assets/upstream*.md | Raw upstream content | check-upstream.sh fetches |

## Update Commands
- `bash skills/<name>/scripts/check-upstream.sh` — check status
- `bash skills/<name>/scripts/check-upstream.sh --update` — pull updates
- `just upstream-check` — batch check VDD + VSDD
- `just provenance audit` — batch provenance audit

## Lessons Learned
- Provenance audit caught 13 skills missing SOURCE.md — generate-fixed all in one pass
- security-best-practices and skill-vetter used source-repo: in metadata instead of source: block
- tesseract-vault-security has lock entry but no skill directory (orphaned)
- Always quote ISO timestamps in YAML or fetched_at fails validation
