---
name: provenance-tracking
description: >
  Ensures every remote-installed skill has a references/ folder citing its upstream source
  and can be checked for updates against that source. Runs as a post-install gate and
  on-demand freshness check. Triggers on: skill install, skill add, provenance, source
  tracking, update check, freshness, skill audit, sync, lock file, remote skill.
triggers:
  - skill install
  - skill add
  - provenance
  - source tracking
  - update check
  - freshness
  - skill audit
  - sync
  - lock file
  - remote skill
  - check for updates
tags:
  - tooling
  - skill-management
  - provenance
  - maintenance
license: Apache-2.0
metadata:
  author: kvithayathil
  version: "1.1.0"
---

# Provenance Tracking

## Overview

Every skill installed from a remote source must carry **source provenance** so the agent can
trace where it came from, detect when upstream changes, and decide how to integrate those
changes. This skill enforces three invariants:

1. **references/SOURCE.md exists** — cites the upstream source, ref, and install date.
2. **Freshness is checkable** — a `scripts/check-upstream.sh` can compare local vs upstream.
3. **Upstream content is preserved** — an `assets/` folder holds the canonical upstream source.

## When to Use

- Immediately after installing a skill from a remote repo (`just install`, `npx skills add`)
- When adapting a public methodology/gist into a local skill (like VDD/VSDD)
- During `just sync` to audit all remote skills for provenance compliance
- When the user asks "are any skills out of date?" or "check for updates"
- During periodic maintenance / skill audits
- When reviewing or modifying a skill that was installed from elsewhere

**Don't use when:**

- Authoring a new skill from scratch (no upstream source)
- Editing a skill that already has valid provenance and is up-to-date

## Skill Categories

Remote skills fall into two categories, each with different provenance requirements:

### Category A: Modified Third-Party Skills

The local skill **adapts** an upstream source (gist, repo, blog post) with local
modifications — additional instructions, project-specific patterns, self-learning protocol,
etc. The upstream is the methodology reference; the local SKILL.md is the working skill.

**Examples:** `vdd/` (adapts gist `45c95ebf...`), `vsdd/` (adapts gist `d8d3bc3e...`)

**Required structure:**

```
skill-name/
├── SKILL.md                    # Modified skill with local adaptations
├── assets/
│   └── upstream.md             # Raw upstream source (canonical reference)
├── scripts/
│   └── check-upstream.sh       # Fetches upstream, compares, updates assets/
└── references/
    ├── SOURCE.md               # Provenance metadata
    ├── CHANGELOG.md            # Skill update history
    └── LESSONS_LEARNED.md      # Evolving patterns (if self-learning)
```

**Source frontmatter pattern:**

```yaml
source:
  gist: https://gist.github.com/user/id
  gist_id: id
  fetched_at: "2026-01-01T00:00:00Z"
```

Or for a repo-based upstream:

```yaml
source:
  repo: https://github.com/org/repo
  ref: main
  path: subpath
  fetched_at: "2026-01-01T00:00:00Z"
```

### Category B: Unmodified Third-Party Skills

Skills installed verbatim from a remote repo via `npx skills add`, `just install`, or
manual copy. No local modifications — the SKILL.md is the upstream SKILL.md.

**Examples:** `qa/`, `write-a-prd/`, `grill-me/` (installed from mattpocock/skills)

**Required structure:**

```
skill-name/
├── SKILL.md                    # Unmodified upstream skill
├── assets/
│   └── upstream-SKILL.md       # Latest upstream SKILL.md for diff comparison
├── scripts/
│   └── check-upstream.sh       # Fetches upstream, compares, offers pull
└── references/
    └── SOURCE.md               # Provenance metadata
```

**Source frontmatter pattern:**

```yaml
source:
  repo: https://github.com/org/repo
  ref: main
  path: skill-name
```

## Instructions

### Step 1: Post-Install Provenance Gate

After any remote skill install, verify and create provenance metadata:

```
GIVEN: A skill directory exists at skills/<name>/
  AND: An entry exists in skills-lock.json for <name>

VERIFY:
  □ skills/<name>/references/ directory exists
  □ skills/<name>/references/SOURCE.md exists and is non-empty
  □ SOURCE.md contains: source URL, ref/branch, remote path, install date
  □ SKILL.md frontmatter has `source:` block
  □ skills/<name>/scripts/check-upstream.sh exists
  □ skills/<name>/assets/ directory exists

IF ANY CHECK FAILS:
  1. Create missing directories (references/, scripts/, assets/)
  2. Generate SOURCE.md from skills-lock.json entry
  3. Merge source metadata into SKILL.md frontmatter if absent
  4. Generate check-upstream.sh (see Step 6/7 for templates)
  5. Run check-upstream.sh --update to fetch initial assets/
```

### Step 2: Generate SOURCE.md

When creating or updating `references/SOURCE.md`, use this template:

```markdown
# Source Provenance

- **Repo**: {source URL}
- **Ref**: {branch or tag}
- **Path**: {subpath within repo, or "root"}
- **Installed**: {installed_at date}
- **Last Checked**: {today's date}
- **Provider**: {provider name, e.g. npx-skills, gh-api}
- **Lock Entry**: Recorded in `skills/skills-lock.json`

## Upstream Changes

This file is auto-maintained. Do not edit manually unless correcting errors.
Run `just sync` or the provenance check to refresh `Last Checked`.
```

Values come from `skills-lock.json`:

```bash
jq -r --arg name "SKILL_NAME" '.skills[$name]' skills/skills-lock.json
```

### Step 3: Merge Source Metadata into SKILL.md Frontmatter

If the installed SKILL.md lacks a `source:` block in frontmatter, add one:

```yaml
source:
  repo: https://github.com/org/repo
  ref: main
  path: skill-name
```

This ensures the index (`SKILL_INDEX.yaml`) carries provenance without requiring
a separate lock-file lookup at search time.

### Step 4: Freshness Check

To check whether any remote skills have upstream changes:

```
FOR EACH skill with scripts/check-upstream.sh:
  1. Run: bash skills/<name>/scripts/check-upstream.sh
  2. Report status: UNCHANGED or CHANGED (with hash comparison)
  3. If CHANGED, prompt user to review and run --update
```

For skills without a check script, fall back to GitHub API:

```bash
gh api "repos/{owner}/{repo}/commits/{ref}?per_page=1" \
  --jq '.sha' 2>/dev/null
```

### Step 5: Batch Provenance Audit

Run as part of `just sync` or on demand:

```
FOR EACH skill directory:
  IF skill has entry in skills-lock.json OR source: in SKILL.md:
    IF no references/SOURCE.md:
      WARN → CREATE references/SOURCE.md
    IF no scripts/check-upstream.sh:
      WARN → GENERATE check-upstream.sh (see Step 6 or 7)
    IF no assets/ directory:
      WARN → CREATE assets/, run check-upstream.sh --update
    IF SKILL.md lacks source: block:
      WARN → PATCH SKILL.md frontmatter
  ELSE:
    IF references/SOURCE.md exists but no lock entry:
      WARN: orphaned provenance
```

### Step 6: Generate check-upstream.sh for Modified Skills (Category A)

When a skill adapts an upstream methodology (gist, article, repo) with local changes,
generate a `scripts/check-upstream.sh` that:

1. Fetches the upstream source via `gh api` or `gh gist view`
2. Compares content hash against cached version
3. On `--update`: saves raw upstream to `assets/upstream.md`, patches SKILL.md frontmatter
4. Preserves local SKILL.md modifications — never overwrites the skill itself

**Template structure:**

```bash
#!/usr/bin/env bash
set -euo pipefail

SKILL_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SOURCE_URL="..."           # gist URL, repo URL, etc.
CACHE_DIR="$SKILL_DIR/references/.cache"
ASSET_FILE="$SKILL_DIR/assets/upstream.md"
HASH_FILE="$CACHE_DIR/last-known-hash"
SKILL_MD="$SKILL_DIR/SKILL.md"

mkdir -p "$CACHE_DIR" "$SKILL_DIR/assets"

# Fetch upstream
gh api "gists/$GIST_ID" > "$CACHE_DIR/meta.json"      # for gists
# OR: gh api "repos/$OWNER/$REPO/contents/$PATH"       # for repos
# Save raw content to $ASSET_FILE.tmp

# Hash compare
current_hash=$(shasum "$ASSET_FILE.tmp" | cut -d' ' -f1)
local_hash=$(cat "$HASH_FILE" 2>/dev/null || echo "")

if [[ "$local_hash" == "$current_hash" ]]; then
    echo "UNCHANGED"; rm -f "$ASSET_FILE.tmp"; exit 0
fi

echo "CHANGED"
if [[ "${1:-}" != "--update" ]]; then
    rm -f "$ASSET_FILE.tmp"
    echo "Run with --update to sync."
    exit 0
fi

# Update: move tmp to asset, save hash, patch frontmatter
mv "$ASSET_FILE.tmp" "$ASSET_FILE"
echo "$current_hash" > "$HASH_FILE"

# Patch last-reviewed and fetched_at in SKILL.md using python3
# (see vdd/scripts/check-upstream.sh for full implementation)
```

**Key behavior for modified skills:**

- `assets/upstream.md` is the raw upstream — never modify it
- `SKILL.md` is the local adaptation — the agent reviews upstream changes and
  **manually integrates** relevant updates into the skill
- The agent should prompt: "Upstream changed. Review `assets/upstream.md` and
  merge relevant changes into SKILL.md, references/, etc."

### Step 7: Generate check-upstream.sh for Unmodified Skills (Category B)

When a skill is an unmodified copy from a remote repo, the update script should
offer to **pull the latest upstream directly**:

```bash
#!/usr/bin/env bash
set -euo pipefail

SKILL_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SOURCE_URL="..."           # e.g. https://github.com/org/repo
SOURCE_PATH="..."          # subpath within repo, e.g. "skill-name"
CACHE_DIR="$SKILL_DIR/references/.cache"
ASSET_FILE="$SKILL_DIR/assets/upstream-SKILL.md"
HASH_FILE="$CACHE_DIR/last-known-hash"
SKILL_MD="$SKILL_DIR/SKILL.md"

mkdir -p "$CACHE_DIR" "$SKILL_DIR/assets"

# Fetch latest SKILL.md from upstream
OWNER_REPO=$(echo "$SOURCE_URL" | sed 's|https://github.com/||')
gh api "repos/$OWNER_REPO/contents/$SOURCE_PATH/SKILL.md" \
  --jq '.content' | base64 -d > "$ASSET_FILE.tmp"

# Hash compare
current_hash=$(shasum "$ASSET_FILE.tmp" | cut -d' ' -f1)
local_hash=$(cat "$HASH_FILE" 2>/dev/null || echo "")

if [[ "$local_hash" == "$current_hash" ]]; then
    echo "UNCHANGED"; rm -f "$ASSET_FILE.tmp"; exit 0
fi

echo "CHANGED"
if [[ "${1:-}" != "--update" ]]; then
    rm -f "$ASSET_FILE.tmp"
    echo "Run with --update to sync."
    exit 0
fi

# Update: save upstream SKILL.md to assets/
mv "$ASSET_FILE.tmp" "$ASSET_FILE"
echo "$current_hash" > "$HASH_FILE"

# For unmodified skills: also update SKILL.md itself
cp "$ASSET_FILE" "$SKILL_MD"

# Re-apply local source: frontmatter patch
# (python3 regex to add/update source block)
echo "Updated: SKILL.md pulled from upstream, assets/upstream-SKILL.md saved"
```

**Key behavior for unmodified skills:**

- `assets/upstream-SKILL.md` preserves the exact upstream version
- `SKILL.md` is overwritten with upstream on `--update` (no local modifications to preserve)
- Source frontmatter is re-applied after the pull

### Step 8: Agent Workflow on Upstream Change

When `check-upstream.sh` reports CHANGED, the agent should:

**For modified skills (Category A):**

```
1. Read assets/upstream.md (the new upstream content)
2. Compare against current SKILL.md and references/
3. Identify material changes (new phases, renamed concepts, added sections)
4. Prompt user: "Upstream <name> changed. Changes: <summary>. Merge into skill?"
5. If yes: integrate relevant changes into SKILL.md, references/, scripts/
6. Update last-reviewed in SKILL.md frontmatter
7. Record change in references/CHANGELOG.md
```

**For unmodified skills (Category B):**

```
1. Run check-upstream.sh --update (pulls latest into SKILL.md)
2. Run just validate <skill-name> to verify spec compliance
3. Run just sync to rebuild index
4. Report: "<skill> updated to latest upstream version"
```

## Common Mistakes

| Mistake | Fix |
| ------- | --- |
| Installing skill without running provenance gate | Always run provenance check after install |
| Editing SOURCE.md manually | Regenerate from lock file to avoid drift |
| Skipping freshness for manual installs | All remote skills need check-upstream.sh |
| Overwriting modified SKILL.md with upstream | Modified skills: only update assets/, never overwrite SKILL.md |
| Not creating check-upstream.sh for new installs | Generate it as part of post-install gate |
| Checking freshness without `gh` CLI | Fall back to git ls-remote or skip with warning |
| Forgetting to quote ISO timestamps in YAML | Always quote fetched_at values to avoid datetime parsing |

## Gotchas

- `skills-lock.json` is the canonical provenance source. SOURCE.md is derived for readability.
- The `npx-skills` provider and manual installs may store slightly different fields. SOURCE.md
  should normalize both.
- Skills authored locally (no lock entry, no source URL) should NOT have a SOURCE.md.
- Commit hashes are only available after a pin/fetch. First freshness check pins the commit.
- YAML auto-parses unquoted ISO timestamps as `datetime` objects. Always quote them:
  `fetched_at: "2026-01-01T00:00:00Z"` not `fetched_at: 2026-01-01T00:00:00Z`.
- `assets/` should contain raw upstream content only — never mix with local modifications.
- `scripts/check-upstream.sh` must be idempotent — running twice without upstream changes
  must produce UNCHANGED both times.
- `.cache/` directories inside `references/` are local state and should be gitignored.

## Checklist

- [ ] references/ directory exists for each remote skill
- [ ] references/SOURCE.md cites upstream source, ref, path, install date
- [ ] SKILL.md frontmatter has `source:` block
- [ ] scripts/check-upstream.sh exists for each remote skill
- [ ] assets/ directory exists with upstream content preserved
- [ ] Freshness check runs against source (GitHub API / gist)
- [ ] ISO timestamps quoted in YAML frontmatter
- [ ] `.cache/` gitignored in each skill
- [ ] Orphaned SOURCE.md (no lock entry) flagged as warning
- [ ] Lock file remains canonical — SOURCE.md is derived

## References

- [references/SOURCE-TEMPLATE.md](references/SOURCE-TEMPLATE.md) — SOURCE.md template
- [references/CHANGELOG.md](references/CHANGELOG.md) — Skill update history
- [scripts/provenance-check.sh](scripts/provenance-check.sh) — Batch audit/freshness tool
- [AgentSkills spec](https://agentskills.io/specification#optional-directories) — `scripts/`, `assets/`, `references/` spec
