#!/usr/bin/env bash
# Shared helpers for skill-manager and providers.
set -euo pipefail

SKILLS_DIR="${SKILLS_DIR:-$(cd "$(dirname "$0")/.." && pwd)}"
LOCK_FILE="$SKILLS_DIR/skills-lock.json"

# Read a value from our lock file (jq required)
lock_get() {
	local skill_name="$1"
	local field="$2"
	if [[ -f "$LOCK_FILE" ]]; then
		jq -r --arg name "$skill_name" --arg field "$field" \
			'.skills[$name][$field] // empty' "$LOCK_FILE" 2>/dev/null || echo ""
	fi
}

# Write/update a skill entry in our lock file
lock_set() {
	local skill_name="$1"
	shift
	# Remaining args are key=value pairs
	local tmp
	tmp=$(mktemp)
	if [[ ! -f "$LOCK_FILE" ]]; then
		echo '{"version": 1, "skills": {}}' >"$tmp"
	else
		cp "$LOCK_FILE" "$tmp"
	fi

	# Build the entry
	local entry_args=()
	for pair in "$@"; do
		key="${pair%%=*}"
		val="${pair#*=}"
		entry_args+=("--arg" "$key" "$val")
	done

	local set_expr=".skills[\"$skill_name\"] = ("
	set_expr+="{\"name\": \"$skill_name\""
	for pair in "$@"; do
		key="${pair%%=*}"
		val="${pair#*=}"
		set_expr+=", \"$key\": \$$(echo "$key" | tr '-' '_')"
	done
	set_expr+="})"

	jq "${entry_args[@]}" "$set_expr" "$tmp" >"$LOCK_FILE"
	rm -f "$tmp"
}

# Remove a skill from lock file
lock_remove() {
	local skill_name="$1"
	if [[ -f "$LOCK_FILE" ]]; then
		local tmp
		tmp=$(mktemp)
		jq --arg name "$skill_name" 'del(.skills[$name])' "$LOCK_FILE" >"$tmp" && mv "$tmp" "$LOCK_FILE"
	fi
}

# Get current ISO-8601 timestamp
iso_now() {
	date -u +"%Y-%m-%dT%H:%M:%SZ"
}

# Check if a CLI tool is available
require_cmd() {
	if ! command -v "$1" &>/dev/null; then
		echo "ERROR: '$1' is required but not found in PATH." >&2
		return 1
	fi
}
