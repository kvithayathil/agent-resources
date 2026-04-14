# LLM Security Mitigation Plan — VSDD Behavioral Specification

> **Epic:** #1 — LLM Security Mitigation Stack (Team/Organizational)
> **Threat Model:** Team/organizational — shared codebases, sensitive repos, PII
> **Source Analysis:** `docs/llm-security-crosslink.md` (OWASP LLM Top 10 + Lethal Trifecta)
> **Methodology:** Verified Spec-Driven Development (VSDD)

---

## Phase 1a: Behavioral Specification

### System Boundary

This plan defines a **mitigation layer** for LLM-powered agent systems used by engineering teams. The system:

- Accepts user prompts and external content (web, files, documents)
- Routes them through an LLM with tool access (file I/O, shell, web fetch)
- Returns results to the user or downstream systems

**In scope:** Security mitigations applicable to this agent architecture.
**Out of scope:** Model training, fine-tuning pipeline security, deployment infrastructure hardening.

### Behavioral Contracts

#### BC-1: Trifecta Separation

**Precondition:** Agent has ≥2 of: file read access, web fetch capability, outbound communication.

**Postcondition:** No single agent session combines all three trifecta components without explicit per-session user authorization.

**Invariant:** File-reader agents never make outbound network calls. Web-fetcher agents never write to filesystem. Main agent orchestrates but delegates to isolated sub-agents for each capability domain.

| Component | Allowed Tools | Forbidden Tools |
|-----------|--------------|-----------------|
| File-reader agent | read, glob, grep | bash (network), webfetch, write |
| Web-fetcher agent | webfetch, fetch | bash, write, read (sensitive paths) |
| Writer agent | write, edit | webfetch, bash (network) |
| Orchestrator | All (read-only inspection only) | Direct execution of tools with untrusted data |

**Orchestrator-to-sub-agent protocol:** Communication uses **structured JSON only** — typed fields with metadata (URL, file path, query). The orchestrator passes *references*, never raw untrusted content. Sub-agents fetch their own data. This prevents the orchestrator from becoming a contamination vector.

#### BC-2: PII Detection and Redaction

**Precondition:** Any text enters the system (user input, file content, web content).

**Postcondition:** All PII (names, emails, SSNs, API keys, tokens, credentials, phone numbers) is detected and either redacted or flagged before LLM processing.

**Invariant:** No raw PII reaches the LLM context window without explicit opt-in per field type.

**Density escalation:** If >70% of content is flagged as PII, escalate to human review rather than blanket redaction. This prevents denial-of-service on legitimate config files, test fixtures, and data pipeline code.

**Context allowlist:** Recognized non-sensitive patterns (test fixtures in `tests/`, sample data in `samples/`, documented example data) are excluded from PII flagging via configurable path/glob patterns.

**PII Entity Types (Presidio recognizers):**
- CREDIT_CARD, EMAIL_ADDRESS, PHONE_NUMBER
- US_SSN, US_BANK_NUMBER, IBAN_CODE
- API_KEY (custom recognizer: patterns matching `sk-`, `ghp_`, `xoxb-`, `AKIA`, Bearer tokens)
- URL_WITH_CREDENTIALS (embedded auth in URLs)
- FILE_PATH_WITH_SECRETS (`.env`, `credentials.json`, `.pem` references)

#### BC-3: Input Classification (Prompt Injection Detection)

**Precondition:** User prompt or external content arrives.

**Postcondition:** Content is classified as `TRUSTED` (user-authored in secure context), `UNTRUSTED_EXTERNAL` (web, documents, emails), or `SUSPECTED_INJECTION` (classifier flags malicious patterns).

**Invariant:** Content classified as `SUSPECTED_INJECTION` is quarantined — never reaches the LLM context window. `UNTRUSTED_EXTERNAL` content is wrapped in segregation markers.

**Classification signals:**
- PurpleLlama Prompt Guard classifier score ≥ configurable threshold (default 0.7, must be calibrated against garak injection probe corpus with documented FP/FN rates) → `SUSPECTED_INJECTION`
- Known injection patterns (ignore previous, system override, role change) → `SUSPECTED_INJECTION`
- Content from web fetch without user typing → `UNTRUSTED_EXTERNAL`
- Content typed by authenticated user → `TRUSTED`

#### BC-4: Output Validation

**Precondition:** LLM generates output.

**Postcondition:** Output passes schema validation, PII scan, and injection-pattern check before delivery to user or downstream system.

**Invariant:** No LLM output reaches a downstream system (shell, file write, API call) without passing all three validation gates.

**Validation gates (ordered: PII first on raw form, then structural, then semantic):**
1. **PII scan** (Presidio): Output contains no PII not present in the original input
2. **Schema validation** (guardrails-ai): Output matches expected format (JSON schema, type constraints, allowed values)
3. **Injection pattern check**: Output contains no prompt-injection-like patterns targeting downstream consumers

**Combined guarantee:** The system's false-negative rate is bounded by the weakest gate. Gates are ordered from rawest to most processed form to maximize early rejection.

#### BC-5: Least-Privilege Tool Enforcement

**Precondition:** Agent session initializes.

**Postcondition:** Tool permissions are set to minimum required for the current task. No open-ended shell access. No unconstrained URL fetch.

**Invariant:** Tool capabilities are reduced, never expanded, during a session. Any capability escalation requires explicit user approval.

**Default permissions (restrictive):**

| Tool | Default | Escalation Required |
|------|---------|---------------------|
| read | Allowed: workspace dir only | Yes — paths outside workspace |
| write | Allowed: workspace dir only | Yes — always (human-in-the-loop) |
| bash | Blocked by default | Yes — whitelisted commands only |
| webfetch | Allowed: HTTPS only | Yes — non-HTTPS, auth-required URLs |
| glob/grep | Allowed: workspace dir only | Yes — system paths |

**Tool-chain taint tracking:** Data originating from untrusted sources (file reads of external content, web fetch results) cannot flow into destructive tools (write, bash) without passing through the output validation gate (BC-4). This is enforced via a taint flag on all data objects — `UNTRUSTED` data must be validated before mutation.

#### BC-6: Rate Limiting and Resource Budgets

**Precondition:** Agent session is active.

**Postcondition:** Resource consumption stays within defined budgets.

**Invariant:** No single session exceeds its budget without explicit override.

| Resource | Budget | Action on Exceed |
|----------|--------|-------------------|
| Tokens per session | 500K tokens | Hard stop + notify user |
| Tool calls per turn | 20 calls | Pause + request continuation |
| Consecutive errors | 5 errors | Pause + request guidance |
| Session duration | 4 hours | Warn at 3h, stop at 4h |
| Cost per session | $10 USD equivalent | Hard stop |

**Cross-session budgets:** Per-user daily budget spans sessions (configurable, default: 3x session budget). Session IDs bound to authenticated user. Prevents rate-limit bypass via session cycling.

#### BC-7: Human-in-the-Loop for Destructive Actions

**Precondition:** Agent intends to execute a destructive or irreversible action.

**Postcondition:** Action is blocked until user explicitly approves.

**Invariant:** No destructive action executes without affirmative user confirmation.

**Destructive actions (require HITL):**
- File writes outside designated workspace
- `git push`, `git push --force`, `git rebase`
- Shell commands with `rm`, `drop`, `delete`, `truncate`
- API calls with side effects (POST, PUT, DELETE to external services)
- Credential/secret operations (rotation, creation, deletion)
- Mass operations (bulk file operations, batch API calls)

**Timeout:** If user doesn't respond within N minutes (configurable, default 30), action is **denied by default**. No auto-approve on timeout. No pending queue accumulation.

#### BC-8: Security Scanning Pipeline

**Precondition:** Agent system is deployed/updated.

**Postcondition:** Automated security scan runs against the agent configuration and passes all checks.

**Invariant:** No deployment without passing security gate.

**Scan stages:**
1. **garak** — LLM vulnerability scan (injection, encoding attacks, data leakage)
2. **pip-audit** — dependency vulnerability check
3. **Semgrep** — static analysis for security patterns
4. **Custom rules** — agent-specific checks (no secrets in prompts, tool permission validation)

#### BC-9: Incident Response

**Precondition:** A mitigation fails (garak finds new injection, Presidio misses PII, classifier false-negative detected).

**Postcondition:** System logs the event, alerts the security contact, and enters degraded-safe mode.

**Invariant:** No mitigation failure is silently ignored. All failures are logged with full context.

**Degraded-safe mode:**
1. All operations restricted to read-only
2. No tool execution, no file writes, no network calls
3. User notified of degraded state with reason
4. Remains in degraded mode until security contact acknowledges and clears

**Alert channels:** Security contact via configured notification (email, Slack webhook, PagerDuty). Alert includes: timestamp, failing mitigation, sample input that triggered failure, severity assessment.

---

## Phase 1b: Verification Architecture

### Provable Properties Catalog

| ID | Property | Verification Method | Priority |
|----|----------|-------------------|----------|
| P1 | Trifecta separation invariant holds | Integration test — agent cannot access all three domains simultaneously | Test |
| P2 | PII detection recall ≥ 95% for defined entity types | Property-based test with Presidio + known PII corpus | Test |
| P3 | Input classifier false-negative rate < 1% on known injection corpus | Adversarial test suite from garak | Test |
| P4 | Output validation blocks 100% of schema-violating outputs | Deterministic test — invalid outputs rejected | Test |
| P5 | Least-privilege invariant — tool capabilities only reduce, never expand | State machine test — capability transitions | Test |
| P6 | Rate limits are enforced — no budget bypass | Concurrency + boundary test | Test |
| P7 | No destructive action executes without explicit approval | Integration test — attempt destructive action without approval | Test |
| P8 | No secrets/PII in agent configuration files | Static analysis rule (Semgrep custom) | Proof (static) |

### Purity Boundary Map

```
┌─────────────────────────────────────────────────┐
│                  PURE CORE                       │
│  (deterministic, side-effect-free, verifiable)  │
│                                                  │
│  • PII redaction logic (string substitution)     │
│  • Input classification (pattern matching)       │
│  • Output schema validation (JSON Schema)        │
│  • Budget arithmetic (addition, comparison)      │
│  • Permission evaluation (set operations)        │
│  • Content segregation marker injection          │
│  • Taint flag propagation (data-flow tracking)   │
│  • HITL timeout enforcement                      │
└──────────────────┬──────────────────────────────┘
                   │ (pure results flow out)
                   ▼
┌─────────────────────────────────────────────────┐
│               EFFECTFUL SHELL                    │
│  (I/O, network, stateful — tested, not proven)  │
│                                                  │
│  • PII detection (Presidio + spaCy model calls)  │
│  • LLM API calls (token counting, rate limiting)│
│  • File I/O (read, write, glob)                 │
│  • Web fetch (HTTP requests)                    │
│  • Shell execution (bash commands)              │
│  • User interaction (approval prompts)          │
│  • Session state management                     │
│  • Alert/notification dispatch                  │
└─────────────────────────────────────────────────┘
```

**Key rule:** The pure core makes all security *decisions* (redact/deny/allow/escalate). The effectful shell *detects* (PII via Presidio) and *executes* (file I/O, network). Security logic in the pure core never depends on external state. Detection results from the effectful shell flow into the pure core as typed data, where decisions are made deterministically.

### Verification Tooling Selection

| Tool | Purpose | When |
|------|---------|------|
| pytest + hypothesis | Unit + property-based testing | Phase 2 |
| garak | LLM vulnerability scanning | Phase 2, CI/CD |
| pip-audit | Dependency scanning | Phase 2, CI/CD |
| Semgrep | Static analysis for security patterns | Phase 2, CI/CD |
| Presidio | PII detection runtime | Phase 2 |
| guardrails-ai | Schema validation runtime | Phase 2 |
| PurpleLlama Prompt Guard | Injection classification | Phase 2 |

---

## Phase 1c: Edge Case Catalog

### EC-1: Injection Edge Cases

| ID | Edge Case | Expected Behavior |
|----|-----------|-------------------|
| EC-1.1 | Base64-encoded injection payload in file content | Decoded content scanned, classified as injection |
| EC-1.2 | Injection in image EXIF/metadata | Metadata extracted and scanned before LLM processing |
| EC-1.3 | Multi-turn injection (spread across 3+ messages) | Per-turn classification + cumulative pattern detection |
| EC-1.4 | Injection via unicode homoglyphs (lookalike chars) | Normalize unicode before classification |
| EC-1.5 | Injection in code comments within fetched files | Content segregation — all file content treated as untrusted |
| EC-1.6 | Prompt wrapped in markdown code block to bypass filters | Classification operates on raw content, not rendered |

### EC-2: PII Edge Cases

| ID | Edge Case | Expected Behavior |
|----|-----------|-------------------|
| EC-2.1 | Partial PII split across multiple file reads | Per-read scan catches complete PII; partial logged for review |
| EC-2.2 | API key in environment variable expansion | Custom recognizer catches common key patterns |
| EC-2.3 | PII in non-English text | Presidio multilingual recognizers active |
| EC-2.4 | False positive on test fixture data | Allowlist mechanism for known test patterns |
| EC-2.5 | PII in base64-encoded content | Decode before scanning |

### EC-3: Permission Edge Cases

| ID | Edge Case | Expected Behavior |
|----|-----------|-------------------|
| EC-3.1 | Symlink pointing outside workspace | Resolve symlinks, deny if target outside workspace |
| EC-3.2 | Path traversal with `../` sequences | Normalize paths, deny traversal attempts |
| EC-3.3 | Concurrent sessions attempting same resource | Per-session isolation, no shared mutable state |
| EC-3.4 | Tool permission change mid-session | Capabilities can only decrease, never increase |
| EC-3.5 | Agent attempts to modify its own config | Config files are read-only to agent, require human change |

### EC-4: Resource Edge Cases

| ID | Edge Case | Expected Behavior |
|----|-----------|-------------------|
| EC-4.1 | Token budget reached mid-tool-call | Complete current call, then hard stop |
| EC-4.2 | LLM API latency spike causing timeout | Retry with exponential backoff, max 3 retries |
| EC-4.3 | Nested tool calls exceeding depth limit | Max nesting depth: 5, enforced per call |
| EC-4.4 | Agent loop (repeatedly calling same failing tool) | Consecutive error budget (5) triggers pause |

### EC-5: Output Edge Cases

| ID | Edge Case | Expected Behavior |
|----|-----------|-------------------|
| EC-5.1 | LLM outputs shell command in markdown | Output validation blocks, sanitizes before display |
| EC-5.2 | LLM outputs new system prompt attempting override | Output validation rejects prompt-like patterns |
| EC-5.3 | Output exceeds maximum length | Truncate with warning, validate before delivery |
| EC-5.4 | Output contains references to files user shouldn't access | Output PII scan catches unauthorized file paths |
| EC-5.5 | LLM outputs markdown image with external URL (exfiltration) | Output validation strips all external image URLs or replaces with placeholder. Pattern: `![...](https://...)` in output → sanitize |

---

## Non-Functional Requirements

| ID | Requirement | Constraint | Verification |
|----|-------------|-----------|--------------|
| NFR-1 | PII scan latency | < 50ms per 1KB text | Benchmark test |
| NFR-2 | Input classification latency | < 100ms per prompt | Benchmark test |
| NFR-3 | Output validation latency | < 30ms per output | Benchmark test |
| NFR-4 | Security scan CI pipeline | < 10 minutes total | CI timing measurement |
| NFR-5 | Memory overhead of security layer | < 200MB additional | Runtime profiling |
| NFR-6 | Agent response latency impact | < 20% overhead vs. unsecured agent | A/B benchmark |
| NFR-7 | Configuration changes require restart | No hot-reload of security rules | Design enforcement |

---

## Implementation Phases (from Crosslink Priority Matrix)

### Tier 1: Immediate (Week 1-2)

| Task | Contract | Tool | Priority |
|------|----------|------|----------|
| PII scanning on all inputs/outputs | BC-2 | Presidio | P1 |
| Rate limiting and cost budgets | BC-6 | Custom middleware | P1 |
| Human-in-the-loop for destructive actions | BC-7 | Agent hooks | P1 |
| Least privilege tool permissions | BC-5 | Agent config | P1 |

### Tier 2: Architectural (Week 3-4)

| Task | Contract | Tool | Priority |
|------|----------|------|----------|
| Trifecta separation — sub-agent architecture | BC-1 | Agent orchestration | P2 |
| Input classification pipeline | BC-3 | PurpleLlama Prompt Guard | P2 |
| Output validation with schemas | BC-4 | guardrails-ai | P2 |
| Content segregation markers | BC-3 | Custom middleware | P2 |

### Tier 3: Operational (Week 5+)

| Task | Contract | Tool | Priority |
|------|----------|------|----------|
| Automated security scanning pipeline | BC-8 | garak + Semgrep + pip-audit | P3 |
| Production monitoring | NFR-4, NFR-6 | Arize Phoenix | P3 |
| SBOM maintenance | BC-8 (supply chain) | CycloneDX | P3 |
| Regular red team exercises | BC-8 | garak + Giskard + inspect_ai | P3 |

---

## Contract Chain Traceability

```
OWASP LLM01 (Prompt Injection)
  → BC-3 (Input Classification)
  → EC-1.1–EC-1.6 (Injection edge cases)
  → P3 (Classifier false-negative < 1%)
  → Test: injection_corpus_test.py
  → Tool: PurpleLlama Prompt Guard

OWASP LLM02 (Info Disclosure)
  → BC-2 (PII Detection)
  → EC-2.1–EC-2.5 (PII edge cases)
  → P2 (PII recall ≥ 95%)
  → Test: pii_detection_test.py
  → Tool: Presidio

OWASP LLM05 (Improper Output Handling)
  → BC-4 (Output Validation)
  → EC-5.1–EC-5.5 (Output edge cases including markdown exfil)
  → P4 (100% schema violation blocking)
  → Test: output_validation_test.py
  → Tool: guardrails-ai

OWASP LLM06 (Excessive Agency)
  → BC-1 (Trifecta Separation)
  → BC-5 (Least Privilege + Tool-Chain Taint Tracking)
  → BC-7 (HITL for Destructive Actions + Timeout)
  → EC-3.1–EC-3.5 (Permission edge cases)
  → P1, P5, P7 (Separation, permission, HITL invariants)
  → Test: permission_test.py, trifecta_separation_test.py, taint_tracking_test.py

OWASP LLM10 (Unbounded Consumption)
  → BC-6 (Rate Limiting + Cross-Session Budgets)
  → EC-4.1–EC-4.4 (Resource edge cases)
  → P6 (Budget enforcement)
  → Test: rate_limit_test.py

Lethal Trifecta
  → BC-1 (Trifecta Separation) — breaks the trifecta by design
  → BC-5 (Tool-Chain Taint Tracking) — prevents data flow from untrusted to destructive
  → P1 (Separation invariant holds)

All OWASP Risks
  → BC-9 (Incident Response) — failsafe when mitigations fail
  → BC-8 (Security Scanning Pipeline) — ongoing verification
```
