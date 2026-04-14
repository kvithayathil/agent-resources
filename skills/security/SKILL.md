---
name: security
description: >
  Security best practices reference for cryptographic systems, secure design principles,
  vulnerability reporting, and threat modeling. Covers defense in depth, least privilege,
  fail-safe defaults, post-quantum cryptography, memory safety, supply chain security,
  and formal verification. Triggers on: security, cryptography, encryption, AES, Argon2,
  post-quantum, threat model, vulnerability, secure design, memory safety, supply chain,
  fuzz testing, formal verification.
tags:
  - security
  - cryptography
  - secure-design
  - threat-model
license: Apache-2.0
metadata:
  author: dollspace-gay
  version: "1.0.0"
  living: "true"
  self-learning: "true"
  self-updating: "true"
  update-policy: "periodic-remote-check"
  last-reviewed: "2026-04-14"
---

# Security Reference Skill

## Overview

Security best practices reference sourced from [Tesseract Vault's SECURITY.md](https://github.com/dollspace-gay/Tesseract-Vault/blob/main/SECURITY.md). Covers cryptographic design, threat modeling, vulnerability reporting, and verification methods.

## Self-Learning / Self-Updating Protocol

> This skill is self-updating. The source document lives in an external repository.
> The agent periodically checks for updates and refreshes the local reference.

### Update Mechanism

1. **Periodic freshness check**: Compare remote `pushed_at` timestamp with local `last-reviewed`
2. **Content diff**: If remote is newer, fetch the full SECURITY.md and diff against local cache
3. **Update if changed**: Overwrite `references/SECURITY-SOURCE.md` and update `last-reviewed` in frontmatter
4. **Record in changelog**: Add entry to `references/CHANGELOG.md`

### Freshness Check Command

```bash
gh api repos/dollspace-gay/Tesseract-Vault --jq '.pushed_at'
```

If the date is newer than the `last-reviewed` frontmatter value, run the full update.

### Update Command

```bash
gh api repos/dollspace-gay/Tesseract-Vault/contents/SECURITY.md --jq '.content' | base64 -d > references/SECURITY-SOURCE.md
```

### Self-Update Triggers

- `last-reviewed` is more than 7 days old — run freshness check
- User explicitly asks to update security references
- A security incident or vulnerability discussion occurs

### Self-Update Constraints

- Only update from the canonical source repository
- Log all updates in `references/CHANGELOG.md`
- Never remove the Self-Learning/Self-Updating Protocol section

## Instructions

### Step 1: Apply Secure Design Principles

Reference the full source at [references/SECURITY-SOURCE.md](references/SECURITY-SOURCE.md).

Core principles to apply:

| Principle | Description |
|-----------|-------------|
| Defense in Depth | Multiple independent security layers |
| Least Privilege | Only necessary permissions |
| Fail-Safe Defaults | Security on by default, no config needed |
| Complete Mediation | Every operation requires authentication |
| Separation of Duties | Keys never leave secure memory |
| Minimal Attack Surface | No network-facing code, no custom crypto |
| Economy of Mechanism | Simple designs, clear code paths |
| Open Design | No security through obscurity |

### Step 2: Verify Against Threat Model

When reviewing or designing a system, check:

**Protects against:**
- Brute-force password attacks
- Quantum computer attacks (post-quantum cryptography)
- Cold boot attacks (memory locking and scrubbing)
- Timing side-channel attacks (constant-time operations)
- Swap file exposure (memory locking)

**Does NOT protect against:**
- Malware on the host system
- Hardware keyloggers
- Physical access to running system with mounted volumes
- Rubber hose cryptanalysis

### Step 3: Cryptographic Checklist

- [ ] Using audited libraries only (RustCrypto, BoringSSL, etc.)
- [ ] No custom cryptographic algorithms
- [ ] Constant-time operations for sensitive comparisons
- [ ] Memory zeroization on deallocation
- [ ] Locked memory pages for key material
- [ ] Argon2id or equivalent memory-hard KDF for passwords
- [ ] AES-256-GCM or equivalent authenticated encryption
- [ ] Post-quantum key encapsulation where applicable

### Step 4: Supply Chain Security

- [ ] Dependency auditing (cargo-audit, npm audit, pip-audit)
- [ ] License compliance (cargo-deny, etc.)
- [ ] Reproducible builds where possible
- [ ] Minimal dependencies

### Step 5: Vulnerability Reporting

If a vulnerability is found:
1. Do NOT report through public GitHub issues
2. Report via the project's designated security contact
3. Include: type, file paths, reproduction steps, PoC, impact assessment
4. Expected response: acknowledgment in 48h, status in 7d, resolution in 90d

## References

- [references/SECURITY-SOURCE.md](references/SECURITY-SOURCE.md) — Full source document (auto-updated from remote)
- [references/CHANGELOG.md](references/CHANGELOG.md) — Update history
