---
title: "Dependency Security Audit Patterns"
tags: ["security", "dependencies", "uv"]
sources: []
contributors: ["Jm2A"]
created: 2026-10-22
updated: 2026-10-22
---



2026-10-22 audit outcome and patterns (applies to skills/scripts + security_layer uv projects):

1. cryptography>=50.0.0 override: presidio-anonymizer 2.2.364 declares cryptography>=48.0.1,<49.0.0, but PYSEC-2026-3552 (CBC PKCS7 padding oracle — exactly presidio AESCipher's surface) is only fixed in 50.0.0; 3553/3554 in 49.0.0; GHSA-537c-gmf6-5ccf in 48.0.1. Solution: [tool.uv] override-dependencies in security_layer/pyproject.toml with floor at the ACTUAL fix line (>=50.0.0), compat proven by tests/test_crypto_compat.py (presidio Encrypt->Decrypt round-trip). Gotcha: dropping the override line silently reverts resolution to the cap — always re-check 'uv lock --check' and grep the lock for the resolved version after editing.

2. en-core-web-lg 3.8.0 (presidio spaCy model) is installed OUTSIDE uv.lock in security_layer venv. Plain 'uv sync' (exact) evicts it; 'uv run' default sync is inexact so it survives. Use 'uv sync --inexact' / 'uv run --no-sync' after lock upgrades. Reinstall URL if evicted: https://github.com/explosion/spacy-models/releases/download/en_core_web_lg-3.8.0/en_core_web_lg-3.8.0-py3-none-any.whl

3. jscpd is a GLOBAL homebrew binary (5.4.2), not in any Python env: config drift between repo .jscpd.json and global binary versions breaks 'just check' independently of Python deps. v5 wants reporters: ["console"] not format: text.

4. CI reality: remote is GitHub-only; .gitlab-ci.yml is dormant (no GitLab remote). GitHub Actions check.yml runs lint/typecheck/test; advisories cleared 2026-10-22 via full uv lock --upgrade in both projects (27 advisories). Renovate (config:recommended) is ACTIVE and opens PRs; as of 2026-10-22 open: actions/checkout v7 + astral-sh/setup-uv v10 (both green, fix Node-20-deprecation warnings), renovate/python-3.x rebasing.

5. Provenance freshness: GitHub API 404 for a dead repo returns {'message':'Not Found'} — provenance-check.sh previously stringified the blob and printed a false CURRENT. Any new API-dependent check must treat fetch failure as UNKNOWN, never CURRENT.

6. OWASP skill-scanner integration (reference recorded 2026-10-22, evaluation task pending in openspec change ci-warnings-cve-sweep): Guide https://owasp.github.io/www-project-agentic-skills-top-10/skill-scanner-integration recommends NVIDIA SkillSpector (github.com/NVIDIA/SkillSpector, Apache-2.0, 20.8k stars, active) for CI skill scanning: static mode --no-llm (no API key), 0-100 risk score, SARIF v2.1.0 output uploadable via codeql-action/upload-sarif@v3 to GitHub code scanning; maps AST01-04/08-10; AST09 risk score is the natural gate threshold. OWASP's own @owasp/ast10-scanner package is NOT published — map findings to the AST taxonomy manually. Best practice: non-blocking scans first; SARIF artifacts[] sha-256 hashes are the join key for multi-scanner report composition (layer-tagged findings). Applies here because skills/ contains 30 skills, several from remote installs with provenance records.

2026-10-22 monthly security sweep ("just sweep", scripts/security-sweep.sh, exit-nonzero-on-findings; run date printed when clean): audits the four pip-audit blind spots. (1) GitHub Actions used in the workflows — uses: refs are grepped at runtime (never hard-coded) and compared against each repo's latest release via gh api; any action >=1 major behind (e.g. dorny/paths-filter@v3 vs v4, codeql-action v3 vs v4 tag) is a triage finding; VERIFIED: OSV declares a GitHub Actions ecosystem (dumps exist in the osv-vulnerabilities GCS bucket) but live /v1/query returns 200 {} even for a package with a published advisory in it (osv exposes no version ordering: 'GitHub Actions': None) — so fall back to gh releases, never trust an OSV query for that ecosystem. (2) Global jscpd (homebrew npm tool, outside every lockfile) — npm jscpd@<resolved-version> queried on OSV. (3) Node bundled via nodejs-wheel-binaries (hidden inside both uv.locks as a PyPI package) — version read from each lock via awk (uv.lock is TOML, jq chokes) and checked against PyPI ecosystem. (4) pip-audit re-run: skills/scripts via just audit (reuse, justfile is source of truth); security_layer has NO pip-audit in its lock and CI never audits it, so sweep exports the locked deps (uv export --frozen --hashes, hashes required because pip-audit --disable-pip) and runs uvx pip-audit -r. Registering a new surface: add a check_* function + surface-list entry in scripts/security-sweep.sh, then update this page. OSV query payload used: POST /v1/query {package:{name,ecosystem},version} (batch: /v1/querybatch {queries:[...]}); recency filtered client-side on published — 30-day window.
