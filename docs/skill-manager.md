# Skill Manager

The skill manager is a thin CLI that delegates install/update/check operations to a **provider**, while handling index generation and spec validation itself.

## Architecture

```
skill-manager (CLI router)
    ├── providers/          # Pluggable install/update backends
    │   ├── common.sh       # Shared helpers (lock file ops)
    │   └── npx-skills.sh   # Default provider (wraps `npx skills`)
    ├── sync-index.py       # Index builder, search, validation
    └── pyproject.toml      # Python deps via uv
```

## Provider Interface

A provider is a shell script that must implement:

| Function | Purpose |
|---|---|
| `_provider_install <source> [options]` | Install skill(s) from a source |
| `_provider_update [skills...] [options]` | Update installed skills |
| `_provider_check [options]` | Check for available updates |

Providers use helpers from `common.sh`:
- `lock_set <name> key=val ...` — update provenance in skills-lock.json
- `lock_remove <name>` — remove a skill from the lock file
- `iso_now` — current UTC timestamp
- `require_cmd <tool>` — assert a CLI tool is available

### Switching Providers

```bash
# One-off via env var
SKILLS_PROVIDER=./my-provider.sh ./skills/scripts/skill-manager install org/repo

# Permanent: edit the default in skill-manager line 12
```

### Creating a Custom Provider

```bash
#!/usr/bin/env bash
source "$(dirname "$0")/common.sh"

_provider_install() {
    local source="$1"; shift
    # your install logic
    lock_set "$skill_name" "source=$source" "provider=my-provider" ...
}

_provider_update() {
    # your update logic
}

_provider_check() {
    # your check logic
}
```

## Provenance Tracking

`skills-lock.json` is the source of truth for remote skill provenance. It's committed to git so changes flow through normal PR review.

```json
{
  "version": 1,
  "skills": {
    "pdf": {
      "source": "anthropics/skills",
      "ref": "main",
      "source_type": "github",
      "provider": "npx-skills",
      "installed_at": "2026-04-14T10:00:00Z",
      "updated_at": "2026-04-14T10:00:00Z"
    }
  }
}
```

On `sync`, sync-index.py merges lock file provenance into SKILL_INDEX.yaml alongside SKILL.md frontmatter.

## Index Generation Flow

```
SKILL.md frontmatter ──┐
                       ├── sync-index.py sync ──► SKILL_INDEX.yaml
skills-lock.json ──────┘
```

1. Scan each skill directory for `SKILL.md`
2. Parse YAML frontmatter (name, description, triggers, tags, source)
3. Read `skills-lock.json` for remote provenance
4. Merge into a single entry per skill
5. Write `SKILL_INDEX.yaml`

## Search Scoring

Fuzzy search scores tokens against multiple fields:

| Field | Weight |
|---|---|
| Name exact match | 3.0x per token |
| Trigger match | 2.0x per token |
| Tag match | 2.0x per token |
| Description match | 1.0x per token |
| Trigger substring | +2.5 |
| Tag substring | +1.5 |
| Coverage ratio | +1.0 |

Results are sorted by score, max 10 returned.
