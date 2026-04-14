#!/usr/bin/env bash
# Provider: npx-skills — wraps the `npx skills` CLI (https://github.com/vercel-labs/skills)
#
# Implements the provider interface:
#   _provider_install <source> [options]
#   _provider_update [skills...] [options]
#   _provider_check [options]

_provider_install() {
	require_cmd npx || return 1
	local source="$1"
	shift

	local agent_flag=""
	local skill_flag=""
	local global_flag=""
	local yes_flag=""

	while [[ $# -gt 0 ]]; do
		case "$1" in
		--agent | -a)
			agent_flag="$2"
			shift 2
			;;
		--skill | -s)
			skill_flag="$2"
			shift 2
			;;
		--global | -g)
			global_flag="--global"
			shift
			;;
		--yes | -y)
			yes_flag="--yes"
			shift
			;;
		*) shift ;;
		esac
	done

	local cmd="npx skills add $source"
	[[ -n "$global_flag" ]] && cmd+=" $global_flag"
	[[ -n "$yes_flag" ]] && cmd+=" $yes_flag"
	[[ -n "$agent_flag" ]] && cmd+=" --agent $agent_flag"
	[[ -n "$skill_flag" ]] && cmd+=" --skill $skill_flag"

	echo "--- Installing via npx skills ---"
	echo "  $cmd"
	eval "$cmd"

	# After install, update our lock file with provenance
	local skill_name=""
	if [[ -n "$skill_flag" && "$skill_flag" != "*" ]]; then
		skill_name="$skill_flag"
	else
		skill_name="$(basename "$source")"
	fi

	local ref=""
	if [[ "$source" == *"#"* ]]; then
		ref="${source##*#}"
		source="${source%#*}"
	fi

	local now
	now=$(iso_now)
	lock_set "$skill_name" \
		"source=$source" \
		"ref=${ref:-main}" \
		"source_type=github" \
		"provider=npx-skills" \
		"installed_at=$now" \
		"updated_at=$now"
}

_provider_update() {
	require_cmd npx || return 1

	local global_flag=""
	local yes_flag=""
	local skill_names=()

	while [[ $# -gt 0 ]]; do
		case "$1" in
		--global | -g)
			global_flag="--global"
			shift
			;;
		--yes | -y)
			yes_flag="--yes"
			shift
			;;
		--*) shift ;;
		*)
			skill_names+=("$1")
			shift
			;;
		esac
	done

	local cmd="npx skills update"
	[[ -n "$global_flag" ]] && cmd+=" $global_flag"
	[[ -n "$yes_flag" ]] && cmd+=" $yes_flag"
	[[ ${#skill_names[@]} -gt 0 ]] && cmd+=" ${skill_names[*]}"

	echo "--- Updating via npx skills ---"
	echo "  $cmd"
	eval "$cmd"

	local now
	now=$(iso_now)
	if [[ ${#skill_names[@]} -gt 0 ]]; then
		for name in "${skill_names[@]}"; do
			lock_set "$name" "updated_at=$now"
		done
	else
		for name in $(jq -r '.skills | keys[]' "$LOCK_FILE" 2>/dev/null); do
			lock_set "$name" "updated_at=$now"
		done
	fi
}

_provider_check() {
	require_cmd npx || return 1
	echo "--- Checking for updates via npx skills ---"
	npx skills check "$@"
}
