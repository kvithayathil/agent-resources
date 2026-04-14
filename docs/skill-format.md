# Skill Format Reference

Based on the [AgentSkills specification](https://agentskills.io/specification) with extensions for discoverability and provenance.

## Directory Structure

```
skill-name/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
└── assets/           # Optional: templates, resources
```

## SKILL.md Format

```yaml
---
name: my-skill                  # Required. Max 64 chars, lowercase + hyphens
description: What and when.     # Required. Max 1024 chars. Include keywords.
triggers:                       # Extension. Keywords/phrases for discovery.
  - keyword one
  - phrase matching this skill
tags:                           # Extension. Categories for grouping/filtering.
  - category
  - subcategory
license: Apache-2.0             # Optional.
compatibility: Requires X       # Optional. Max 500 chars.
metadata:                       # Optional. String key-value pairs.
  author: your-name
  version: "1.0"
allowed-tools: Bash(git:*) Read # Optional. Experimental.
source:                         # Extension. For skills derived from a remote repo.
  repo: https://github.com/org/repo
  ref: main
  path: skills/my-skill
  commit: abc1234               # Auto-managed by provider
  fetched_at: "2026-01-01T00:00:00Z"
---

# My Skill

Instructions for the agent go here. Keep under 500 lines.
Move detailed reference material to separate files in references/.
```

## Frontmatter Field Reference

### Spec Fields

| Field | Required | Constraints |
|---|---|---|
| `name` | Yes | Max 64 chars, lowercase `[a-z0-9-]`, no leading/trailing/consecutive hyphens, must match directory name |
| `description` | Yes | Max 1024 chars, non-empty, describes what + when |
| `license` | No | License name or reference to bundled file |
| `compatibility` | No | Max 500 chars, environment requirements |
| `metadata` | No | Mapping of string → string |
| `allowed-tools` | No | Space-separated tool patterns (experimental) |

### Extension Fields

| Field | Purpose | Format |
|---|---|---|
| `triggers` | Keywords/phrases for fuzzy skill discovery | List of strings |
| `tags` | Categories for grouping and filtering | List of strings |
| `source` | Remote repo provenance | Mapping (see below) |

### Source Sub-fields

| Field | Required | Description |
|---|---|---|
| `source.repo` | Yes | Repository URL (e.g. `https://github.com/org/repo`) |
| `source.ref` | No | Branch or tag (e.g. `main`) |
| `source.path` | No | Subpath within repo (e.g. `skills/pdf`) |
| `source.commit` | No | Pinned commit hash (auto-managed) |
| `source.fetched_at` | No | ISO-8601 timestamp of last fetch |

## Progressive Disclosure

The spec uses three loading levels:

1. **Metadata** (~100 tokens): `name` + `description` loaded at startup
2. **SKILL.md body** (<5000 tokens recommended): Full instructions loaded on activation
3. **Resources** (as needed): Files in `scripts/`, `references/`, `assets/`

Keep SKILL.md under 500 lines. Move detailed reference material to separate files.
