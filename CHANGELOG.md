# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added
- Add provenance-tracking skill for remote skill installs
- Implement scanning.py CUSTOM_RULES stage
- Add writing-agent-hooks skill for creating hooks across OpenCode, VS Code:, Polytoken, and Claude
- Add tesseract-vault-security skill (Tesseract Vault security policy and secure-design reference)

### Fixed
- Resolve all known Python dependency advisories (cryptography, urllib3, anyio, idna, setuptools, certifi, pip); override cryptography to >=50.0.0 past the presidio-anonymizer cap, backed by Encrypt/Decrypt round-trip compat tests
- Fix duplicate-detection config incompatibility with jscpd 5.x (unsupported `format: text` key replaced with `reporters`)

### Changed
- Freeze security-best-practices skill as a vendored copy (upstream repo unreachable); provenance freshness now skips and explicitly reports frozen skills
- LLM Security Mitigation Stack — Team/Organizational
- Roast: Security Mitigation Spec
- Spec: Non-Functional Requirements — Performance & Ops
- Spec: Edge Case Catalog — LLM Attack Vectors
- Spec: Verification Architecture — Purity Boundaries & Tooling
- Spec: Behavioral Contract — Security Mitigation Pipeline
