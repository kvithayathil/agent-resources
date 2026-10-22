#!/usr/bin/env bash
# Security sweep — checks pip-audit blind spots against last-30-day OSV advisories.
# Monthly cadence (run via `just sweep`).
#
# Surfaces (fixed list, dynamic details resolved at runtime):
#   1. GitHub Actions referenced in .github/workflows/check.yml
#   2. Global jscpd (homebrew npm tool, outside any lockfile)
#   3. Node bundled via nodejs-wheel-binaries (inside the Python locks)
#   4. pip-audit re-run in both uv-managed Python trees
#
# Advisory source: OSV API (https://api.osv.dev), ecosystems PyPI + npm.
# POST /v1/query {"package":{"name":"<name>","ecosystem":"<ecosystem>"},"version":"<version>"}
# -> {"vulns":[{"id":...,"published":...,"summary":...}]}; full records are already
# included, so each `id` needs no extra GET /v1/vulns/{id} round trip. Recency is
# filtered client-side on the `published` timestamp.
#
# VERIFIED 2026-10-22: OSV declares a "GitHub Actions" ecosystem (Google Cloud Storage
# bucket osv-vulnerabilities/GitHub Actions/ holds GHSA records for it, e.g.
# GHSA-2487-9f55-2vg9 for OZI-Project/publish@1.13.2) but the live /v1/query returns
# 200 {} even when querying that exact package+version — osv.dev's ecosystem table
# lists 'GitHub Actions': None (no version-ordering implementation), so versioned
# API queries yield no actionable results. Documented fallback, implemented here:
# for each referenced action, compare against its latest release via
# `gh api repos/{owner}/{repo}/releases/latest` and flag any action >= 1 major
# version behind as a triage finding.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WINDOW_DAYS=30

RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
NC='\033[0m'

FINDINGS=0
SWEEP_TMPDIR=""
INCOMPLETE_COUNT=0
# Newline-separated per-surface reasons for checks that could not complete.
INCOMPLETE_LOG=""
# Tools required for the pip surface that are checked in preflight.
PREFLIGHT_MISSING=""

usage() {
    cat <<EOF
Usage: security-sweep.sh [surface ...]

Surfaces (run all when omitted):
  actions   Actions referenced in .github/workflows/check.yml
  jscpd     Globally installed jscpd (npm ecosystem)
  node      Node bundled via nodejs-wheel-binaries (PyPI ecosystem)
  pip       pip-audit in both uv-managed Python trees
EOF
}

needs() {
    command -v "$1" &>/dev/null || {
        echo -e "${RED}ERROR${NC}: required tool '$1' not found" >&2
        exit 2
    }
}

# Record a check that could not complete (tool failure, missing data);
# the final summary exits 2 so a partial run never looks clean.
incomplete() {
    echo -e "  ${YELLOW}INCOMPLETE${NC} $1: $2"
    INCOMPLETE_LOG="${INCOMPLETE_LOG}  - $1: $2\n"
    INCOMPLETE_COUNT=$((INCOMPLETE_COUNT + 1))
}

# ISO-8601 timestamp -> epoch seconds (UTC). Prints nothing and returns 1 on
# unparseable input so callers can fail closed (see check_osv).
epoch_of() {
    local ts="$1"
    local stripped
    # Drop fractional seconds and +HH:MM numeric offsets; for Z-suffixed
    # timestamps nothing before the suffix changes (offsets differ from UTC by
    # minutes only, far below the 30d decision granularity).
    stripped="${ts%%.*}"
    stripped="${stripped%%Z*}"
    date -u -j -f '%Y-%m-%dT%H:%M:%S' "$stripped" +%s 2>/dev/null && return 0 # BSD
    date -u -d "$ts" +%s 2>/dev/null && return 0 # GNU
    return 1
}

# Record a finding; increments FINDINGS.
finding() {
    local surface="$1" pkg="$2" id="$3" summary="$4" published="$5"
    echo -e "  ${RED}FIND${NC} $surface $pkg"
    echo "       $id  $(echo "$summary" | head -c 200)  published=$published"
    FINDINGS=$((FINDINGS + 1))
}

# Query OSV for package@version; report vulns published within the window.
check_osv() {
    local surface="$1" eco="$2" name="$3" version="$4" body resp ids cutoff now
    echo "--- $surface: $eco $name@$version ---"

    body=$(jq -cn --arg n "$name" --arg e "$eco" --arg v "$version" \
        '$ARGS.named | {package:{name:$n,ecosystem:$e},version:$v}')
    resp=$(curl -sf --max-time 30 --retry 2 --data "$body" "https://api.osv.dev/v1/query") || {
        incomplete "$surface" "OSV query failed for $name@$version (curl/network error); not silently skipped"
        return 0
    }

    ids=$(echo "$resp" | jq -r '.vulns // [] | .[].id')
    if [[ -z "$ids" ]]; then
        echo -e "  ${GREEN}OK${NC} no vulns"
        return 0
    fi
    now=$(date +%s)
    cutoff=$((now - WINDOW_DAYS * 86400))

    local id published summary published_epoch
    for id in $ids; do
        published=$(echo "$resp" | jq -r --arg i "$id" \
            '.vulns[] | select(.id==$i) | .published // .modified // ""')
        summary=$(echo "$resp" | jq -r --arg i "$id" \
            '.vulns[] | select(.id==$i) | .summary // .details // ""')
        published_epoch=0
        if ! published_epoch=$(epoch_of "$published") || [[ -z "$published_epoch" ]]; then
            incomplete "$surface" "unparseable advisory timestamp for $id (published='$published'; modified fallback also used); record NOT evaluated"
            continue
        fi
        if [[ "$published_epoch" -ge "$cutoff" ]]; then
            finding "$surface" "$name@$version" "$id" "$summary" "$published"
        else
            echo "  NOTE $id published=$published (outside ${WINDOW_DAYS}d window)"
        fi
    done
}

# 1. GitHub Actions: `uses:` refs are extracted at runtime so future workflow
#    edits are automatically covered. Full-SHA pins cannot be release-checked
#    automatically and are reported as explicit manual-verification entries.
check_actions() {
    echo "--- actions: referenced in .github/workflows/*.yml/*.yaml ---"
    local refs pkg ref_tag local_major latest_tag latest_major
    refs=$(grep 'uses:' "$ROOT"/.github/workflows/*.yml "$ROOT"/.github/workflows/*.yaml 2>/dev/null |
        grep -v '^[[:space:]]*#' | # skip commented-out uses: lines
        awk '{for (i=1; i<=NF; i++) if ($i == "uses:") {print $(i+1)}}' |
        tr -d '"'"'"'#' |
        grep -v '^\./' | sort -u || true)
    if [[ -z "$refs" ]]; then
        echo -e "  ${GREEN}OK${NC} no reusable actions referenced"
        return 0
    fi
    for ref in $refs; do
        pkg="${ref%%@*}"
        # repo is the first two path segments (actions may have subpaths,
        # e.g. github/codeql-action/upload-sarif)
        repo=$(echo "$pkg" | awk -F/ '{print $1"/"$2}')
        ref_tag="${ref#*@}"
        if [[ "$ref_tag" == "$ref" ]]; then
            finding "actions" "$pkg" "none (unpinned ref)" \
                "$pkg is referenced without any version tag (supply-chain risk)" "-"
            continue
        fi
        if [[ "$ref_tag" =~ ^[0-9a-f]{40}$ ]]; then
            echo "  MANUAL $pkg pinned to full SHA — release staleness not automatically checked; manual verification needed"
            continue
        fi
        if [[ ! "$ref_tag" =~ ^v?[0-9]+ ]]; then
            finding "actions" "$pkg@$ref_tag" "none (floating ref)" \
                "$pkg is pinned to mutable non-version ref '$ref_tag' (supply-chain risk)" "-"
            continue
        fi
        local_major=$(echo "$ref_tag" | sed -E 's/^v?([0-9]+).*/\1/')
        latest_tag=$(gh api "repos/$repo/releases/latest" --jq '.tag_name' 2>/dev/null) || true
        # Some action repos (e.g. github/codeql-action) tag releases as
        # codeql-bundle-vX or lack a /releases/latest entry; fall back to tags.
        if [[ ! "$latest_tag" =~ ^v?[0-9]+ ]]; then
            latest_tag=$(gh api "repos/$repo/tags?per_page=1" --jq '.[0].name' 2>/dev/null) || true
        fi
        if [[ ! "$latest_tag" =~ ^v?[0-9]+ ]]; then
            incomplete "actions" "$pkg: could not fetch latest release/tag via gh (API failure); staleness unknown"
            continue
        fi
        latest_major=$(echo "$latest_tag" | sed -E 's/^v?([0-9]+).*/\1/')
        if [[ "$latest_major" -le "$local_major" ]]; then
            echo -e "  ${GREEN}OK${NC} $pkg@$ref_tag (latest $latest_tag)"
        else
            finding "actions" "$pkg@$ref_tag" "none (stale major version)" \
                "$pkg is >=1 major version behind latest release $latest_tag" "-"
        fi
    done
}

# 2. Global jscpd (homebrew npm tool, outside any lockfile)
check_jscpd() {
    local version
    echo "--- jscpd ---"
    version=$(jscpd --version 2>/dev/null | awk '{print $NF}') || true
    if [[ -z "$version" ]]; then
        incomplete "jscpd" "jscpd not installed globally outside any lockfile; ecosystem not checked"
        return 0
    fi
    check_osv "jscpd" "npm" "jscpd" "$version"
}

# 3. Node bundled via nodejs-wheel-binaries (inside the Python locks)
check_node() {
    echo "--- nodejs-wheel-binaries ---"
    local lock version
    for lock in "$ROOT/skills/scripts/uv.lock" "$ROOT/security_layer/uv.lock"; do
        if [[ ! -f "$lock" ]]; then
            incomplete "node" "lockfile '$lock' not found; nodejs-wheel-binaries version unchecked"
            continue
        fi
        version=$(awk '/^name = "nodejs-wheel-binaries"$/ {found=1; next}
            found && /^version = / {print $3; exit}' "$lock" | tr -d '"')
        if [[ -z "$version" ]] || [[ "$version" == "null" ]]; then
            incomplete "node" "nodejs-wheel-binaries not pinned in $lock; version unknown"
            continue
        fi
        check_osv "node (via nodejs-wheel-binaries)" "PyPI" "nodejs-wheel-binaries" "$version"
    done
}

# 4. pip-audit re-run in both uv-managed Python trees
#    skills/scripts via `just audit` (justfile is the command source of truth);
#    security_layer has no recipe, so replicate the CI audit commands exactly.
#    pip-audit exit codes: 1 = advisories found, >=2 = tool error. Tool errors
#    are recorded as incomplete, never as "advisories found".
#    pip-audit version is pinned to the version the repo's uv.lock environments
#    run under `just audit` for consistency.
PIP_AUDIT_VERSION="2.10.1"
check_pip() {
    if [[ -n "$PREFLIGHT_MISSING" ]]; then
        incomplete "pip" "required tools missing during preflight:$PREFLIGHT_MISSING; surface not run"
        return 0
    fi
    local tmpdir rc
    tmpdir=$(mktemp -d) || {
        incomplete "pip" "mktemp failed; requirements file could not be created"
        return 0
    }
    SWEEP_TMPDIR="$tmpdir"
    # Cleanup applies on any exit path; only this path uses a temp file.
    trap 'rm -rf "$SWEEP_TMPDIR"' EXIT

    echo "--- pip-audit: skills/scripts (via just audit) ---"
    rc=0
    (cd "$ROOT" && just audit) || rc=$?
    if [[ "$rc" -eq 0 ]]; then
        echo -e "  ${GREEN}OK${NC} no advisories reported"
    elif [[ "$rc" -eq 1 ]]; then
        finding "pip" "skills/scripts" "pip-audit reported advisories" \
            "inspect with: cd skills/scripts && uv run pip-audit" "-"
    else
        incomplete "pip" "skills/scripts audit FAILED (exit $rc); tool error, not advisories"
    fi

    echo "--- pip-audit: security_layer (locked deps exported from uv.lock) ---"
    rc=0
    (cd "$ROOT/security_layer" &&
        uv export --frozen --format requirements-txt --no-dev \
            --hashes -o "$tmpdir/requirements.txt") || rc=$?
    if [[ "$rc" -ne 0 ]]; then
        incomplete "pip" "security_layer uv export FAILED (exit $rc); locked requirements not produced"
        return 0
    fi
    rc=0
    (cd "$ROOT/security_layer" &&
        uvx --from "pip-audit==$PIP_AUDIT_VERSION" pip-audit \
            -r "$tmpdir/requirements.txt" --disable-pip --strict) || rc=$?
    if [[ "$rc" -eq 0 ]]; then
        echo -e "  ${GREEN}OK${NC} no advisories reported"
    elif [[ "$rc" -eq 1 ]]; then
        finding "pip" "security_layer" "pip-audit reported advisories" \
            "inspect with: cd security_layer && uv export ... && uvx pip-audit -r ..." "-"
    else
        incomplete "pip" "security_layer audit FAILED (exit $rc); tool error, not advisories"
    fi
}

# --- main ---
for tool in curl jq gh; do needs "$tool"; done
for tool in just uv uvx; do
    command -v "$tool" &>/dev/null || PREFLIGHT_MISSING="$PREFLIGHT_MISSING $tool"
done

run_surface() {
    case "$1" in
        actions) check_actions ;;
        jscpd) check_jscpd ;;
        node) check_node ;;
        pip) check_pip ;;
        -h | --help | help) usage; exit 0 ;;
        *) echo "Unknown surface '$1'" >&2; usage >&2; exit 2 ;;
    esac
}

if [[ $# -gt 0 ]]; then
    for surface in "$@"; do run_surface "$surface"; done
else
    run_surface actions
    run_surface jscpd
    run_surface node
    run_surface pip
fi

echo
if [[ "$FINDINGS" -gt 0 ]]; then
    echo -e "=== Security sweep: ${RED}$FINDINGS finding(s)${NC} — triage required ==="
    exit 1
fi
if [[ "$INCOMPLETE_COUNT" -gt 0 ]]; then
    echo -e "=== Security sweep: ${YELLOW}incomplete${NC} — $INCOMPLETE_COUNT check(s) could not complete (non-blocking, but the sweep is NOT clean): ==="
    printf '%b' "$INCOMPLETE_LOG"
    exit 2
fi
echo -e "=== Security sweep: ${GREEN}zero findings${NC}, all surfaces complete, on run date: $(date -u +"%Y-%m-%d") ==="
