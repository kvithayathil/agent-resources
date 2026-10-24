---
title: "Validation and YAML Quirks"
tags: ["gotchas", "yaml", "validation", "tooling"]
sources: []
contributors: ["Jm2A"]
created: 2026-04-18
updated: 2026-04-18
---

Common pitfalls discovered during skill development and validation.

## YAML Datetime Trap
YAML auto-parses unquoted ISO timestamps as datetime.datetime objects. This breaks the validator which expects strings.

Wrong: `fetched_at: 2026-01-01T00:00:00Z`
Right: `fetched_at: "2026-01-01T00:00:00Z"`

Always quote ISO timestamps in SKILL.md frontmatter.

## Validation Rules (sync-index.py)
- name: lowercase, hyphens only, max 64 chars, must match directory name
- description: max 1024 chars, non-empty
- source: block requires either `repo` or `gist` field
- All source.* values must be strings (not datetime objects)

## Path Spaces
The project path contains spaces (03 - Resources/agent-resources). Always quote paths in shell scripts and justfile recipes.

## sed on macOS
macOS sed -i requires an extension arg. Use `sed -i.bak ... && rm -f file.bak` or use python3 for complex replacements.

## codescanner detect_secrets Bug
The detect_secrets_engine module is missing from the codescanner upstream repo. Fix after cloning:
```bash
sed -i "" "/detect_secrets/d" src/scanner/engines/__init__.py src/scanner/engine.py main.py
```
