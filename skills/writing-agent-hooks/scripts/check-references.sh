#!/usr/bin/env bash
set -euo pipefail

SKILL_DIR="$(cd "$(dirname "$0")/.." && pwd)"
ASSETS_DIR="$SKILL_DIR/assets"
CACHE_DIR="$SKILL_DIR/references/.cache"
HASH_FILE="$CACHE_DIR/last-known-hashes"

URLS=(
  "opencode:https://opencode.ai/docs/plugins/"
  "vscode:https://code.visualstudio.com/raw/docs/agent-customization/hooks.md"
  "polytoken:https://docs.polytoken.dev/harness-engineering/hooks/"
  "claude:https://code.claude.com/docs/en/hooks.md"
)

mkdir -p "$ASSETS_DIR" "$CACHE_DIR"

UPDATE=false
if [ "${1:-}" = "--update" ]; then
  UPDATE=true
fi

compute_hash() {
  sha256sum "$1" | awk '{print $1}'
}

changed_any=false

for entry in "${URLS[@]}"; do
  name="${entry%%:*}"
  url="${entry#*:}"
  asset_file="$ASSETS_DIR/upstream-$name.md"
  tmp_file="$asset_file.tmp"

  echo "Checking $name..."

  if ! curl -fsSL --max-time 30 "$url" -o "$tmp_file"; then
    echo "  ERROR: failed to fetch $url" >&2
    rm -f "$tmp_file"
    continue
  fi

  current_hash=$(compute_hash "$tmp_file")
  previous_hash=""
  if [ -f "$HASH_FILE" ]; then
    previous_hash=$(grep "^$name " "$HASH_FILE" | awk '{print $2}' || true)
  fi

  if [ "$current_hash" = "$previous_hash" ]; then
    echo "  UNCHANGED"
    rm -f "$tmp_file"
  else
    echo "  CHANGED"
    changed_any=true
    if [ "$UPDATE" = true ]; then
      mv "$tmp_file" "$asset_file"
      if [ -f "$HASH_FILE" ]; then
        grep -v "^$name " "$HASH_FILE" > "$HASH_FILE.tmp" || true
        mv "$HASH_FILE.tmp" "$HASH_FILE"
      fi
      echo "$name $current_hash" >> "$HASH_FILE"
    else
      rm -f "$tmp_file"
    fi
  fi
done

if [ "$changed_any" = true ]; then
  if [ "$UPDATE" = true ]; then
    echo "Assets updated. Review the curated references and bump last-reviewed if needed."
  else
    echo "Upstream docs changed. Run with --update to refresh assets."
    exit 1
  fi
else
  echo "All upstream docs unchanged."
fi

exit 0
