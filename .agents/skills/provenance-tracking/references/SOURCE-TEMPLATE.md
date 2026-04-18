# Source Provenance Template

This directory should contain a `SOURCE.md` for every remote-installed skill.

## SOURCE.md Format

```markdown
# Source Provenance

- **Repo**: https://github.com/org/repo
- **Ref**: main
- **Path**: skill-subdir
- **Installed**: 2026-01-01
- **Last Checked**: 2026-01-15
- **Provider**: npx-skills
- **Lock Entry**: Recorded in `skills/skills-lock.json`

## Upstream Changes

This file is auto-maintained. Do not edit manually unless correcting errors.
Run `just sync` or the provenance check to refresh `Last Checked`.
```

## Generation

SOURCE.md is derived from `skills-lock.json`. To generate for a specific skill:

```bash
# Read lock entry
jq -r --arg name "SKILL_NAME" '.skills[$name]' skills/skills-lock.json

# Generate SOURCE.md
just sync  # provenance audit runs as part of sync
```

## Freshness Check

To compare local skill against upstream:

```bash
# Get latest commit on ref
gh api "repos/{owner}/{repo}/commits/{ref}?per_page=1" --jq '.sha'

# Compare pinned commit with ref
gh api "repos/{owner}/{repo}/compare/{pinned_sha}...{ref}" --jq '.status'
```
