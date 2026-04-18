#!/usr/bin/env bash
# VSDD freshness check — compares local skill against upstream gist.
# Usage: bash check-upstream.sh [--update]
#   --update  Download upstream and update skill metadata
set -euo pipefail

SKILL_DIR="$(cd "$(dirname "$0")/.." && pwd)"
GIST_ID="d8d3bc3ecf4188df049d7a4726bb2a00"
GIST_URL="https://gist.github.com/dollspace-gay/${GIST_ID}"
CACHE_DIR="$SKILL_DIR/references/.cache"
ASSET_FILE="$SKILL_DIR/assets/upstream-VSDD.md"
META_FILE="$CACHE_DIR/meta.json"
HASH_FILE="$CACHE_DIR/last-known-hash"
SKILL_MD="$SKILL_DIR/SKILL.md"

RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m'

mkdir -p "$CACHE_DIR" "$SKILL_DIR/assets"

if ! command -v gh &>/dev/null; then
    echo -e "${RED}ERROR${NC}: gh CLI required. Install: brew install gh"
    exit 1
fi

gh api "gists/$GIST_ID" > "$META_FILE"
gh gist view "$GIST_ID" --raw > "$ASSET_FILE.tmp"

upstream_updated=$(jq -r '.updated_at' "$META_FILE")
current_hash=$(shasum "$ASSET_FILE.tmp" | cut -d' ' -f1)
local_hash=$(cat "$HASH_FILE" 2>/dev/null || echo "")

echo "VSDD Upstream Check"
echo "  Gist:      $GIST_URL"
echo "  Updated:   $upstream_updated"

if [[ "$local_hash" == "$current_hash" ]]; then
    echo -e "  Status:    ${GREEN}UNCHANGED${NC}"
    rm -f "$ASSET_FILE.tmp"
    exit 0
fi

echo -e "  Status:    ${YELLOW}CHANGED${NC}"
[[ -n "$local_hash" ]] && echo "  Local:     ${local_hash:0:12}"
echo "  Upstream:  ${current_hash:0:12}"

if [[ "${1:-}" != "--update" ]]; then
    rm -f "$ASSET_FILE.tmp"
    echo ""
    echo -e "Run with ${CYAN}--update${NC} to sync."
    exit 0
fi

echo -e "${CYAN}Updating...${NC}"

mv "$ASSET_FILE.tmp" "$ASSET_FILE"
echo "$current_hash" > "$HASH_FILE"

today=$(date -u +"%Y-%m-%d")
fetched=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

python3 - "$SKILL_MD" "$today" "$fetched" "$GIST_URL" "$GIST_ID" <<'PYEOF'
import sys, re

path, today, fetched, gist_url, gist_id = sys.argv[1:6]
with open(path) as f:
    content = f.read()

content = re.sub(r'last-reviewed: ".*?"', f'last-reviewed: "{today}"', content)

    source_block = f"""source:
  gist: {gist_url}
  gist_id: {gist_id}
  fetched_at: "{fetched}" """

if re.search(r'^source:', content, re.M):
    content = re.sub(r'^source:.*?^(?=\S)', source_block + '\n', content, flags=re.M | re.S)
else:
    content = re.sub(r'^(---\n)', r'\1' + source_block + '\n', content, count=1)

with open(path, 'w') as f:
    f.write(content)
print("  Patched: SKILL.md (last-reviewed, source)")
PYEOF

echo -e "${GREEN}Done${NC}: assets/upstream-VSDD.md synced, SKILL.md updated"
