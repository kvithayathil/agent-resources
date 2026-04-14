# CI/CD Automation Plan

Crosslink: maps `justfile` quality gates + security_layer test suite to GitHub Actions and GitLab CI pipelines.

## Check Matrix

| Check | Component | Command | CI Job |
|:------|:----------|:--------|:-------|
| Lint (ruff) | skills/scripts | `cd skills/scripts && uv run ruff check .` | `lint` |
| Lint (ruff) | security_layer | `cd security_layer && uv run ruff check . --exclude "*/mutants/*"` | `lint` |
| Format check | skills/scripts | `cd skills/scripts && uv run ruff format --check .` | `fmt` |
| Format check | security_layer | `cd security_layer && uv run ruff format --check .` | `fmt` |
| Typecheck | skills/scripts | `cd skills/scripts && uv run basedpyright sync-index.py` | `typecheck` |
| Typecheck | security_layer | `cd security_layer && uv run basedpyright .` | `typecheck` |
| Tests | skills/scripts | `cd skills/scripts && uv run pytest` | `test` |
| Tests | security_layer | `cd security_layer && uv run pytest ../tests/ -q` | `test-security` |
| Dead code | skills/scripts | `cd skills/scripts && uv run vulture sync-index.py` | `deadcode` |
| Dupes (pylint) | skills/scripts | `cd skills/scripts && uv run pylint --disable=all --enable=duplicate-code sync-index.py` | `dupes` |
| Dupes (jscpd) | skills/scripts | `jscpd sync-index.py` (needs Node) | `dupes` |
| Audit | skills/scripts | `cd skills/scripts && uv run pip-audit` | `audit` |
| Validate | skills/scripts | `cd skills/scripts && uv run python sync-index.py validate` | `validate` |

## Task Breakdown

### T1: GitHub Actions workflow — `.github/workflows/check.yml`

**Triggers:** push to `main`, PRs to `main`

**Jobs:**

```
lint:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - uses: astral-sh/setup-uv@v5
    - run: uv sync
      working-directory: skills/scripts
    - run: uv run ruff check .
      working-directory: skills/scripts
    - run: uv run ruff format --check .
      working-directory: skills/scripts
    - run: uv sync
      working-directory: security_layer
    - run: uv run ruff check . --exclude "*/mutants/*"
      working-directory: security_layer

typecheck:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - uses: astral-sh/setup-uv@v5
    - run: uv sync
      working-directory: skills/scripts
    - run: uv run basedpyright sync-index.py
      working-directory: skills/scripts
    - run: uv sync
      working-directory: security_layer
    - run: uv run basedpyright .
      working-directory: security_layer

test:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - uses: astral-sh/setup-uv@v5
    - run: uv sync
      working-directory: skills/scripts
    - run: uv run pytest
      working-directory: skills/scripts

test-security:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - uses: astral-sh/setup-uv@v5
    - run: uv sync
      working-directory: security_layer
    - run: uv run pytest ../tests/ -q
      working-directory: security_layer

audit:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - uses: astral-sh/setup-uv@v5
    - run: uv sync
      working-directory: skills/scripts
    - run: uv run pip-audit
      working-directory: skills/scripts

validate:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - uses: astral-sh/setup-uv@v5
    - run: uv sync
      working-directory: skills/scripts
    - run: uv run python sync-index.py validate
      working-directory: skills/scripts

deadcode:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - uses: astral-sh/setup-uv@v5
    - run: uv sync
      working-directory: skills/scripts
    - run: uv run vulture sync-index.py
      working-directory: skills/scripts
```

**Notes:**
- All jobs run in parallel (no dependencies between them)
- `dupes-jscpd` excluded (requires Node.js; low value in CI, pylint covers it)
- Python 3.12+ required (spec in both pyproject.toml)
- security_layer mutants excluded from lint via `--exclude`

### T2: GitLab CI pipeline — `.gitlab-ci.yml`

**Same check matrix, GitLab-native syntax:**

```yaml
variables:
  UV_CACHE_DIR: .uv-cache

cache:
  paths:
    - .uv-cache

.linux:
  image: python:3.12-slim
  before_script:
    - pip install uv
    - uv --version

lint:skills:
  extends: .linux
  script:
    - cd skills/scripts && uv sync && uv run ruff check . && uv run ruff format --check .

lint:security:
  extends: .linux
  script:
    - cd security_layer && uv sync && uv run ruff check . --exclude "*/mutants/*"

typecheck:skills:
  extends: .linux
  script:
    - cd skills/scripts && uv sync && uv run basedpyright sync-index.py

typecheck:security:
  extends: .linux
  script:
    - cd security_layer && uv sync && uv run basedpyright .

test:skills:
  extends: .linux
  script:
    - cd skills/scripts && uv sync && uv run pytest

test:security:
  extends: .linux
  script:
    - cd security_layer && uv sync && uv run pytest ../tests/ -q

audit:
  extends: .linux
  script:
    - cd skills/scripts && uv sync && uv run pip-audit

validate:
  extends: .linux
  script:
    - cd skills/scripts && uv sync && uv run python sync-index.py validate

deadcode:
  extends: .linux
  script:
    - cd skills/scripts && uv sync && uv run vulture sync-index.py
```

### T3: Update README badges to CI-driven

Replace static badges with live CI status:

```markdown
![CI](https://github.com/kvithayathil/agent-resources/actions/workflows/check.yml/badge.svg)
![Tests](https://img.shields.io/badge/tests-208%2F208-brightgreen)
![Lint](https://img.shields.io/badge/ruff-clean-brightgreen)
![VSDD](https://img.shields.io/badge/VSDD-converged-blue)
![Python](https://img.shields.io/badge/python-3.12+-blue)
![License](https://img.shields.io/badge/license-Apache--2.0-green)
```

### T4: Add `.gitignore` entries for CI artifacts

```
.uv-cache/
security_layer/.hypothesis/
```

## Execution Order

```
T1 (GitHub Actions) ──→ T3 (live badges)
                      ╲
T2 (GitLab CI)        ──→ T3
T4 (gitignore)        ── independent, do first
```

## Decisions Required

| # | Question | Default |
|---|----------|---------|
| 1 | Include jscpd in CI? (needs Node.js install step) | Skip |
| 2 | Python version pin? | 3.12 (lowest supported) |
| 3 | Run on PR only or also on push to main? | Both |
| 4 | Merge security_layer test into single `test` job? | Keep separate for clarity |
