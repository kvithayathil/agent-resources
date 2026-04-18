---
name: security-scan
description: >
  Run multi-engine security scans against any codebase using codescanner
  (Bandit, Semgrep, Gitleaks, Trivy, Checkov, etc.) with configurable engine
  profiles and severity gating. Triggers on: security scan, vulnerability scan,
  sast, secrets detection, dependency audit, code security, scan for vulnerabilities.
triggers:
  - security scan
  - vulnerability scan
  - sast
  - secrets detection
  - dependency audit
  - code security
  - scan for vulnerabilities
  - security audit
  - checkov
  - bandit
  - trivy
  - gitleaks
  - semgrep
tags:
  - security
  - scanning
  - sast
  - secrets
  - dependencies
  - iac
license: Apache-2.0
metadata:
  author: kvithayathil
  version: "1.0.0"
  living: "true"
  self-learning: "true"
  self-updating: "true"
  update-policy: "evolve-on-evidence"
  last-reviewed: "2026-04-17"
source:
  repo: https://github.com/dollspace-gay/codescanner
  ref: main
  path: root
---

# Security Scan

## Overview

Runs multi-engine security analysis against a target codebase. Wraps the
[codescanner](https://github.com/dollspace-gay/codescanner) tool — a Python
scanner that orchestrates 17 SAST engines behind a single CLI.

Supports **engine profiles** (preset combinations) and **severity gating**
(fail CI on critical/high findings).

## When to Use

- Scanning a codebase for vulnerabilities before release
- CI/CD security gate — fail pipeline on critical findings
- Secrets detection in git history or working tree
- Dependency vulnerability auditing
- Infrastructure-as-Code security review (Terraform, Docker, K8s)
- Pre-commit security checks on changed files

**Don't use when:**

- You only need one specific tool (run bandit/trivy directly instead)
- Reviewing code for style/quality (not security — use linting)
- The target is a binary or compiled artifact (scanner reads source)

## Tools

### Required (Install)

| Tool | Best For | Install |
|------|----------|---------|
| `codescanner` | **Primary** — orchestrates all engines | `git clone https://github.com/dollspace-gay/codescanner.git` |
| Python 3.11+ | Runtime | `brew install python@3.12` |

### Recommended Engines (Install as needed)

| Tool | Category | Install |
|------|----------|---------|
| `bandit` | Python SAST | `pip install bandit` |
| `semgrep` | Multi-lang SAST | `brew install semgrep` |
| `gitleaks` | Secrets detection | `brew install gitleaks` |
| `trivy` | Dependencies + IaC | `brew install trivy` |
| `checkov` | IaC (Terraform, K8s, CF) | `pip install checkov` |
| `safety` | Python deps | `pip install safety` |

Missing engines are skipped automatically — install what you need.

## Instructions

### Step 1: Ensure codescanner is available

```bash
# Clone if not present
CODESCAN_DIR="${PROJECT_ROOT:-.}/.agent-workspace/.external/codescanner"
if [[ ! -d "$CODESCAN_DIR" ]]; then
    git clone --depth 1 https://github.com/dollspace-gay/codescanner.git "$CODESCAN_DIR"
    cd "$CODESCAN_DIR" && python3 -m venv .venv && .venv/bin/pip install -e .
fi
```

### Step 2: Choose an engine profile

| Profile | Engines | Use When |
|---------|---------|----------|
| `full` | All available | Pre-release comprehensive scan |
| `fast` | Bandit, Gitleaks, Safety | Quick feedback during dev |
| `secrets` | Gitleaks, TruffleHog | Audit for leaked credentials |
| `deps` | Safety, Grype, Trivy | Dependency vulnerability audit |
| `iac` | Checkov, Hadolint | Terraform/Dockerfile review |
| `python` | Bandit, Safety, Semgrep | Python-focused project |

### Step 3: Run the scan

```bash
cd "$CODESCAN_DIR"

# Full scan
.venv/bin/python main.py scan /path/to/target -o /tmp/scan-report.md

# Fast profile (skip slow engines)
.venv/bin/python main.py scan /path/to/target \
    --no-semgrep --no-trivy --no-checkov --no-horusec \
    -o /tmp/scan-report.md

# With AI analysis (Gemini)
.venv/bin/python main.py scan /path/to/target \
    --api-key "$GEMINI_API_KEY" \
    -o /tmp/scan-report.md
```

### Step 4: Interpret results

- **Exit code 0** — no critical or high findings
- **Exit code 1** — critical or high severity findings detected
- Report groups by severity: CRITICAL > HIGH > MEDIUM > LOW > INFO
- Each finding: file, line, CWE, OWASP category, remediation guidance

### Step 5: Gate on severity (CI/CD)

```bash
cd "$CODESCAN_DIR"
.venv/bin/python main.py scan /path/to/target -o /tmp/scan-report.md
EXIT_CODE=$?

if [[ $EXIT_CODE -ne 0 ]]; then
    echo "::error::Critical or high security findings detected"
    cat /tmp/scan-report.md
    exit 1
fi
echo "Security scan passed — no critical/high findings."
```

## Engine Profiles

### Fast (dev feedback loop)

```bash
.venv/bin/python main.py scan /path/to/target \
    --no-semgrep --no-trivy --no-checkov --no-horusec \
    --no-grype --no-brakeman --no-spotbugs --no-phpstan \
    --no-gosec --no-shellcheck --no-hadolint --no-detect-secrets \
    -o /tmp/scan-fast.md
```

### Secrets-only

```bash
.venv/bin/python main.py scan /path/to/target \
    --no-bandit --no-semgrep --no-safety --no-trivy --no-grype \
    --no-checkov --no-shellcheck --no-hadolint --no-gosec \
    --no-brakeman --no-spotbugs --no-phpstan --no-horusec \
    --no-detect-secrets \
    -o /tmp/scan-secrets.md
```

### Dependencies-only

```bash
.venv/bin/python main.py scan /path/to/target \
    --no-bandit --no-semgrep --no-gitleaks --no-trufflehog \
    --no-checkov --no-shellcheck --no-hadolint --no-gosec \
    --no-brakeman --no-spotbugs --no-phpstan --no-horusec \
    --no-detect-secrets \
    -o /tmp/scan-deps.md
```

## Known Issues

| Issue | Fix |
|-------|-----|
| `ModuleNotFoundError: detect_secrets_engine` | Upstream bug — engine file missing from repo. Run: `sed -i '' '/detect_secrets/d' src/scanner/engines/__init__.py src/scanner/engine.py main.py` |
| Semgrep timeout on large repos | Use `--no-semgrep` or scan specific subdirs |
| `.venv/bin/python` not found | Run `python3 -m venv .venv && .venv/bin/pip install -e .` |

## Self-Learning / Self-Updating Protocol

> This skill is self-learning and self-updating. It improves through use.
> The agent is authorized to modify this skill when new evidence warrants it.

### Update Triggers

- A new engine is added to codescanner upstream
- A scan profile proves consistently useful (promote to profile table)
- A false positive pattern is identified (add suppression guidance)
- A severity gate threshold needs adjustment
- A new output format integration proves useful

### Agent Instructions

1. **Update engine table** when upstream adds/removes engines
2. **Promote scan profiles** after 3+ successful uses
3. **Add false positive patterns** to Known Issues
4. **Update last-reviewed** date after any modification
5. **Record in changelog** — see [references/CHANGELOG.md](references/CHANGELOG.md)

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Running all engines on a small Python project | Use `fast` or `python` profile |
| Ignoring exit code in CI | Always check exit code — 1 means findings |
| Scanning `node_modules/` or `.venv/` | Tool auto-ignores these; verify with `--help` |
| Using system Python instead of venv | Always use `.venv/bin/python` |
| Running without fixing detect_secrets bug | Apply the sed fix first |

## Checklist

- [ ] codescanner cloned and venv set up
- [ ] detect_secrets patch applied
- [ ] Appropriate profile selected for target
- [ ] Output format chosen (md/html/json)
- [ ] Exit code checked for severity gating
- [ ] Findings reviewed and triaged

## References

- [references/SOURCE.md](references/SOURCE.md) — Upstream provenance
- [references/CHANGELOG.md](references/CHANGELOG.md) — Skill update history
- [references/LESSONS_LEARNED.md](references/LESSONS_LEARNED.md) — Evolving scan patterns
