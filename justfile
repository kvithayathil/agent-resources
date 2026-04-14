set dotenv-load := false
set shell := ["bash", "-cu"]
fixdir := justfile_directory()

# Default: show available recipes
default:
    @just --list

# Bootstrap: install Python deps via uv
setup:
    cd "{{fixdir}}/skills/scripts" && uv sync

# Rebuild the skill index from all SKILL.md + lock file
sync:
    cd "{{fixdir}}/skills/scripts" && uv run python sync-index.py sync

# Validate all skills against AgentSkills spec
validate *skills="":
    cd "{{fixdir}}/skills/scripts" && uv run python sync-index.py validate {{skills}}

# Full quality gate: lint + typecheck + deadcode + dupes + audit + validate
check: lint typecheck deadcode dupes audit validate
    @echo "All checks passed."

# Run ruff linter
lint:
    cd "{{fixdir}}/skills/scripts" && uv run ruff check .

# Auto-fix ruff findings
lint-fix:
    cd "{{fixdir}}/skills/scripts" && uv run ruff check --fix .

# Run ruff formatter check
fmt:
    cd "{{fixdir}}/skills/scripts" && uv run ruff format --check .

# Auto-format with ruff
fmt-fix:
    cd "{{fixdir}}/skills/scripts" && uv run ruff format .

# Run basedpyright type checker
typecheck:
    cd "{{fixdir}}/skills/scripts" && uv run basedpyright sync-index.py

# Run vulture dead code scanner
deadcode:
    cd "{{fixdir}}/skills/scripts" && uv run vulture sync-index.py

# Check for code duplication (pylint + jscpd)
dupes: dupes-pylint dupes-jscpd

# pylint duplicate-code check
dupes-pylint:
    cd "{{fixdir}}/skills/scripts" && uv run pylint --disable=all --enable=duplicate-code sync-index.py

# jscpd copy-paste detector (language-agnostic)
dupes-jscpd:
    cd "{{fixdir}}/skills/scripts" && jscpd sync-index.py

# Audit Python deps for known vulnerabilities
audit:
    cd "{{fixdir}}/skills/scripts" && uv run pip-audit

# Run tests
test:
    cd "{{fixdir}}/skills/scripts" && uv run pytest

# Install a remote skill (delegates to provider)
install source *args="":
    "{{fixdir}}/skills/scripts/skill-manager" install {{source}} {{args}}

# Update installed skills
update *args="":
    "{{fixdir}}/skills/scripts/skill-manager" update {{args}}

# Check for available updates from provider
check-updates:
    "{{fixdir}}/skills/scripts/skill-manager" check

# Search skills by task description
search query:
    "{{fixdir}}/skills/scripts/skill-manager" search "{{query}}"

# Exact skill lookup
lookup name:
    "{{fixdir}}/skills/scripts/skill-manager" lookup {{name}}

# List all indexed skills
list:
    "{{fixdir}}/skills/scripts/skill-manager" list
