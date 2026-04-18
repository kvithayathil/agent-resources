#!/usr/bin/env bash
# Provenance check — audits remote skills for SOURCE.md compliance and upstream freshness.
set -euo pipefail

SKILLS_DIR="${SKILLS_DIR:-$(cd "$(dirname "$0")/.." && pwd)}"
LOCK_FILE="$SKILLS_DIR/skills-lock.json"

RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
NC='\033[0m'

usage() {
    cat <<EOF
Usage: provenance-check.sh [command]

Commands:
  audit     Check all remote skills for SOURCE.md + frontmatter compliance
  fresh     Check upstream repos for updates (requires gh CLI)
  generate  Generate missing SOURCE.md files from lock entries
  report    Show summary of all remote skill provenance

Run without args for full audit + freshness report.
EOF
}

generate_source_md() {
    local skill_dir="$1"
    local name="$2"
    local source="$3"
    local ref="$4"
    local installed_at="$5"
    local provider="$6"
    local remote_path="${7:-root}"
    local today
    today=$(date -u +"%Y-%m-%d")

    mkdir -p "$skill_dir/references"
    cat > "$skill_dir/references/SOURCE.md" <<SOURCEEOF
# Source Provenance

- **Repo**: $source
- **Ref**: $ref
- **Path**: $remote_path
- **Installed**: $installed_at
- **Last Checked**: $today
- **Provider**: $provider
- **Lock Entry**: Recorded in \`skills/skills-lock.json\`

## Upstream Changes

This file is auto-maintained. Do not edit manually unless correcting errors.
Run \`just sync\` or the provenance check to refresh \`Last Checked\`.
SOURCEEOF
    echo -e "  ${GREEN}CREATED${NC} references/SOURCE.md"
}

patch_frontmatter() {
    local skill_md="$1"
    local source="$2"
    local ref="$3"
    local remote_path="$4"

    if grep -q "^source:" "$skill_md" 2>/dev/null; then
        return 0
    fi

    local block="
source:
  repo: $source
  ref: $ref
  path: $remote_path
"
    sed -i.bak "/^---$/!b;N;/^---$/!b;a\\
$block
" "$skill_md" 2>/dev/null && rm -f "$skill_md.bak" || true
    echo -e "  ${GREEN}PATCHED${NC} SKILL.md frontmatter with source block"
}

cmd_audit() {
    echo "=== Provenance Audit ==="
    local issues=0
    local total=0

    if [[ ! -f "$LOCK_FILE" ]]; then
        echo "No skills-lock.json found. Nothing to audit."
        return 0
    fi

    local skill_names
    skill_names=$(jq -r '.skills | keys[]' "$LOCK_FILE" 2>/dev/null)

    for name in $skill_names; do
        total=$((total + 1))
        local skill_dir="$SKILLS_DIR/$name"
        echo -e "\n--- $name ---"

        if [[ ! -d "$skill_dir" ]]; then
            echo -e "  ${RED}MISSING${NC} skill directory"
            issues=$((issues + 1))
            continue
        fi

        local has_source=false
        if [[ -f "$skill_dir/references/SOURCE.md" ]]; then
            has_source=true
            echo -e "  ${GREEN}OK${NC} references/SOURCE.md exists"
        else
            echo -e "  ${YELLOW}WARN${NC} references/SOURCE.md missing"
            issues=$((issues + 1))
        fi

        if [[ -f "$skill_dir/SKILL.md" ]]; then
            if grep -q "^source:" "$skill_dir/SKILL.md" 2>/dev/null; then
                echo -e "  ${GREEN}OK${NC} SKILL.md has source: block"
            else
                echo -e "  ${YELLOW}WARN${NC} SKILL.md missing source: block"
                issues=$((issues + 1))
            fi
        else
            echo -e "  ${RED}MISSING${NC} SKILL.md"
            issues=$((issues + 1))
        fi
    done

    echo -e "\n=== Summary: $total skills, $issues issues ==="
    return $issues
}

cmd_generate() {
    echo "=== Generating Missing SOURCE.md Files ==="

    if [[ ! -f "$LOCK_FILE" ]]; then
        echo "No skills-lock.json found."
        return 0
    fi

    local skill_names
    skill_names=$(jq -r '.skills | keys[]' "$LOCK_FILE" 2>/dev/null)

    for name in $skill_names; do
        local skill_dir="$SKILLS_DIR/$name"
        if [[ -f "$skill_dir/references/SOURCE.md" ]]; then
            echo "  SKIP $name (SOURCE.md exists)"
            continue
        fi

        local source ref installed_at provider remote_path
        source=$(jq -r --arg n "$name" '.skills[$n].source // ""' "$LOCK_FILE")
        ref=$(jq -r --arg n "$name" '.skills[$n].ref // "main"' "$LOCK_FILE")
        installed_at=$(jq -r --arg n "$name" '.skills[$n].installed_at // "unknown"' "$LOCK_FILE")
        provider=$(jq -r --arg n "$name" '.skills[$n].provider // "unknown"' "$LOCK_FILE")
        remote_path=$(jq -r --arg n "$name" '.skills[$n].remote_path // "root"' "$LOCK_FILE")

        generate_source_md "$skill_dir" "$name" "$source" "$ref" "$installed_at" "$provider" "$remote_path"
    done
}

cmd_fresh() {
    echo "=== Freshness Check ==="
    if ! command -v gh &>/dev/null; then
        echo -e "${RED}ERROR${NC}: gh CLI required for freshness checks. Install: brew install gh"
        return 1
    fi

    if [[ ! -f "$LOCK_FILE" ]]; then
        echo "No skills-lock.json found."
        return 0
    fi

    local skill_names
    skill_names=$(jq -r '.skills | keys[]' "$LOCK_FILE" 2>/dev/null)
    local today
    today=$(date -u +"%Y-%m-%d")

    for name in $skill_names; do
        local source ref
        source=$(jq -r --arg n "$name" '.skills[$n].source // ""' "$LOCK_FILE")
        ref=$(jq -r --arg n "$name" '.skills[$n].ref // "main"' "$LOCK_FILE")

        if [[ -z "$source" ]] || [[ "$source" != *"github.com"* ]]; then
            echo "  SKIP $name (not a GitHub source)"
            continue
        fi

        local owner_repo
        owner_repo=$(echo "$source" | sed 's|https://github.com/||')

        local latest_sha
        latest_sha=$(gh api "repos/$owner_repo/commits/$ref?per_page=1" --jq '.sha' 2>/dev/null || echo "UNKNOWN")

        if [[ "$latest_sha" == "UNKNOWN" ]]; then
            echo -e "  ${YELLOW}UNKNOWN${NC} $name — could not fetch upstream"
        else
            local pinned_sha
            pinned_sha=$(jq -r --arg n "$name" '.skills[$n].commit // ""' "$LOCK_FILE" 2>/dev/null)
            if [[ -n "$pinned_sha" && "$pinned_sha" == "$latest_sha" ]]; then
                echo -e "  ${GREEN}UNCHANGED${NC} $name ($latest_sha)"
            elif [[ -n "$pinned_sha" ]]; then
                echo -e "  ${YELLOW}BEHIND${NC} $name — pinned: ${pinned_sha:0:8}, latest: ${latest_sha:0:8}"
            else
                echo -e "  ${GREEN}CURRENT${NC} $name — ref: $ref, latest: ${latest_sha:0:8} (not pinned)"
            fi
        fi

        if [[ -f "$SKILLS_DIR/$name/references/SOURCE.md" ]]; then
            sed -i.bak "s/\*\*Last Checked\*\*: .*/\*\*Last Checked\*\*: $today/" \
                "$SKILLS_DIR/$name/references/SOURCE.md" 2>/dev/null && rm -f "$SKILLS_DIR/$name/references/SOURCE.md.bak"
        fi
    done
}

cmd_report() {
    echo "=== Provenance Report ==="
    if [[ ! -f "$LOCK_FILE" ]]; then
        echo "No skills-lock.json found."
        return 0
    fi

    jq -r '.skills | to_entries[] | "\(.key): \(.value.source) (\(.value.ref)) [\(.value.provider)]"' "$LOCK_FILE"
}

case "${1:-all}" in
    audit) cmd_audit ;;
    fresh) cmd_fresh ;;
    generate) cmd_generate ;;
    report) cmd_report ;;
    all)
        cmd_audit
        echo ""
        cmd_report
        ;;
    *)
        usage
        ;;
esac
