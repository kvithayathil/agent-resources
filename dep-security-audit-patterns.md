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
