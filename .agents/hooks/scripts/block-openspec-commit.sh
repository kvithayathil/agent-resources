#!/usr/bin/env bash
# block-openspec-commit.sh — universal agent hook: deny git commits that
# would include files under openspec/.
#
# Input contract (stdin JSON):
#   { "tool_name": "bash|Bash|shell|runTerminalCommand",
#     "tool_input": { "command": "..." } }
#   (also accepts .tool/.input/.command variants for other platforms)
#
# Output contract:
#   ALLOW: {"continue":true} on stdout, exit 0
#   DENY:  {"hookSpecificOutput":{"hookEventName":"PreToolUse",
#           "permissionDecision":"deny","permissionDecisionReason":"..."}}
#          on stdout, exit 0
#
# Fail-safe: if a git commit is intended but the staged-path check cannot
# run (git error / not a repo), the commit is DENIED — never silently allowed.
#
# Scope: blocks only commits touching openspec/. Staging (git add) is allowed.
set -euo pipefail

INPUT=$(cat)

TOOL_NAME=$(printf '%s' "$INPUT" | jq -r '.tool_name // .tool // empty' 2>/dev/null) || TOOL_NAME=""
COMMAND=$(printf '%s' "$INPUT" | jq -r '.tool_input.command // .input.command // .command // empty' 2>/dev/null) || COMMAND=""

LOG_DIR="${BLOCK_LOG_DIR:-.agents/local/hooks/logs}"

allow() {
    printf '{"continue":true}\n'
    exit 0
}

deny() {
    local reason="$1"
    local ts
    ts=$(date -u +%Y-%m-%dT%H:%M:%SZ)
    mkdir -p "$LOG_DIR" 2>/dev/null || true
    printf '%s blocked git commit: %s\n' "$ts" "$reason" >>"$LOG_DIR/block-openspec-commit.log" 2>/dev/null || true
    jq -n --arg r "$reason" '{
        hookSpecificOutput: {
            hookEventName: "PreToolUse",
            permissionDecision: "deny",
            permissionDecisionReason: $r
        }
    }'
    exit 0
}

# Only shell-like tools carry a command to inspect.
case "$TOOL_NAME" in
bash | Bash | shell | runTerminalCommand) ;;
*) allow ;;
esac

[ -n "$COMMAND" ] || allow

# Does the command contain a `git commit` invocation?
# Splits on shell operators, then walks tokens after `git`, skipping global
# flags (and the value tokens of -C/--git-dir/--work-tree/-c/--namespace) so
# `git -C . commit` cannot slip past.
is_git_commit() {
    local seg tok i j
    # Split on && ; || | and newlines into candidate segments.
    while IFS= read -r seg; do
        # Tokenize on whitespace (quoted-path edge cases are not a bypass risk
        # for detecting the subcommand itself).
        read -ra toks <<<"$seg"
        for ((i = 0; i < ${#toks[@]}; i++)); do
            [ "${toks[i]}" = "git" ] || continue
            j=$((i + 1))
            while [ "$j" -lt "${#toks[@]}" ]; do
                case "${toks[j]}" in
                -C | --git-dir | --work-tree | -c | --namespace)
                    j=$((j + 2)) # flag + its value
                    ;;
                -*)
                    j=$((j + 1)) # other global flag
                    ;;
                commit)
                    return 0
                    ;;
                *)
                    break # some other subcommand
                    ;;
                esac
            done
        done
    done < <(printf '%s\n' "$COMMAND" | sed 's/&&/\n/g; s/||/\n/g; s/;/\n/g; s/|/\n/g')
    return 1
}

is_git_commit || allow

# A commit is intended. Determine what it would commit.
REPO=$(git rev-parse --show-toplevel 2>/dev/null) || REPO=""
if [ -z "$REPO" ]; then
    deny "openspec commit guard: cannot determine repository (git rev-parse failed) — commit blocked fail-closed."
fi

STAGED=$(git -C "$REPO" diff --cached --name-only -- openspec/ 2>/dev/null) || STAGED=""
if [ -n "$STAGED" ]; then
    deny "openspec/ files are staged for this commit: $(printf '%s ' $STAGED). The openspec/ tree stays local-only — unstage them (git restore --staged openspec/) and commit without it."
fi

# Would the commit auto-stage openspec/ paths? (-a/--all, or a chained git add)
if printf '%s' "$COMMAND" | grep -qE '(^|[[:space:]])(-a|--all)([[:space:]]|$)' ||
    printf '%s' "$COMMAND" | grep -qE 'git[[:space:]]+(-[A-Za-z-]+[[:space:]]+)*add([[:space:]]|$)'; then
    PENDING=$(git -C "$REPO" status --porcelain -- openspec/ 2>/dev/null) || PENDING=""
    if [ -n "$PENDING" ]; then
        deny "this commit (-a/--all or chained git add) would include openspec/ changes ($(printf '%s ' $PENDING)). The openspec/ tree stays local-only — omit those paths."
    fi
fi

allow
