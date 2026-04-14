# LLM Security Crosslink: OWASP Top 10 (2025) + Lethal Trifecta

Mapping of OWASP LLM Top 10 risks, Simon Willison's lethal trifecta, mitigations, and automated tooling. All tool entries verified via GitHub API on 2026-04-14.

## The Lethal Trifecta (Willison, June 2025)

Three capabilities that, when combined, enable data exfiltration attacks:

1. **Access to private data** — tools reading local files, emails, databases
2. **Exposure to untrusted content** — web pages, emails, documents, images processed by the LLM
3. **External communication** — any channel the LLM can use to send data out (HTTP, email, URLs, markdown images)

**Core insight:** LLMs cannot reliably distinguish instruction origin. Everything becomes tokens. Untrusted content can contain instructions that override user intent.

**Sources:**
- [The lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) (Willison, 2025)
- [Design Patterns for Securing LLM Agents against Prompt Injections](https://arxiv.org/abs/2506.08837) (Beurer-Kellner et al., 2025)
- [CaMeL: Defeating Prompt Injections by Design](https://arxiv.org/abs/2503.18813) (Google DeepMind, 2025)

### Trifecta → OWASP Crosslink

| Trifecta Component | OWASP Risks |
|---|---|
| Private data access | LLM02 (Info Disclosure), LLM06 (Excessive Agency), LLM08 (Embedding Weaknesses) |
| Untrusted content exposure | LLM01 (Prompt Injection), LLM04 (Data Poisoning), LLM07 (System Prompt Leakage) |
| External communication | LLM05 (Improper Output Handling), LLM06 (Excessive Agency), LLM10 (Unbounded Consumption) |

---

## OWASP LLM Top 10 (2025) — Risks, Mitigations, Tooling

### LLM01:2025 — Prompt Injection

**Description:** User/external prompts alter LLM behavior in unintended ways. Direct (user input) and indirect (external content: web, email, docs, images). RAG and fine-tuning do NOT fully mitigate this.

**OWASP Mitigations:**
1. Constrain model behavior via system prompts
2. Define and validate expected output formats
3. Implement input/output filtering (RAG Triad: context relevance, groundedness, Q/A relevance)
4. Enforce privilege control and least privilege
5. Require human approval for high-risk actions
6. Segregate and identify external content
7. Conduct adversarial testing and red teaming

**Lethal Trifecta Mitigations (architectural):**

| Pattern | Description | Trade-off |
|---|---|---|
| **Action-Selector** | LLM triggers tools but never sees tool output | Simple but limited — no feedback loops |
| **Plan-Then-Execute** | Plan tool calls before exposure to untrusted content | Untrusted content can corrupt content but not action targets |
| **LLM Map-Reduce** | Sub-agents process untrusted content, return structured booleans | Scalable but restricted to classification tasks |
| **Dual LLM** | Privileged LLM + quarantined LLM; symbolic variables bridge them | Good isolation but P-LLM never sees real data |
| **Code-Then-Execute (CaMeL)** | P-LLM generates sandboxed Python DSL; full data-flow tracking with capability tags | Strongest guarantees; user must manage policies |
| **Context-Minimization** | Strip user prompt from context before returning results to downstream | Prevents user-side injection but limited scope |

**Automated Tooling:**

| Tool | Type | Stars | Last Push | Notes |
|---|---|---|---|---|
| [NVIDIA/NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) | Guardrails/orchestration | 5,972 | 2026-04-14 | Most established open-source LLM guardrail framework. Programmable rails for topic control, input/output filtering, dialog flow. Python. |
| [meta-llama/PurpleLlama](https://github.com/meta-llama/PurpleLlama) | Scanning + benchmarks | 4,121 | 2026-04-13 | Meta's LLM security toolkit. CyberSecEval (injection/autocomplete benchmarks), Prompt Guard (classifier). Python. |
| [leondz/garak](https://github.com/leondz/garak) | LLM vulnerability scanner | 7,535 | 2026-04-13 | "Nmap for LLMs." Probes for injection, encoding attacks, hallucination, data leakage, many more. Plugin architecture. Actively maintained. |
| [guardrails-ai/guardrails](https://github.com/guardrails-ai/guardrails) | Input/output validation | 6,673 | 2026-04-03 | Schema-based output validation for LLMs. Spec validators, RAG-specific guards. Python. |
| [Giskard-AI/giskard](https://github.com/Giskard-AI/giskard) | Testing + evaluation | 5,256 | 2026-04-14 | ML model testing framework. Scans for injection, bias, performance, robustness. Generates test suites. |
| [UKGovernmentBEIS/inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai) | Evaluation framework | 1,901 | 2026-04-14 | UK AISI tool for LLM safety evaluations. Supports custom probes including injection tests. |

**Confidence:** L1 (Verified) — all GitHub stats confirmed 2026-04-14. MITRE ATLAS refs: AML.T0051.000 (direct), AML.T0051.001 (indirect), AML.T0054 (jailbreak).

---

### LLM02:2025 — Sensitive Information Disclosure

**Description:** PII, financial data, health records, credentials, proprietary algorithms leaked via LLM output. Includes model inversion/extraction attacks.

**OWASP Mitigations:**
1. Integrate data sanitization (scrub/mask sensitive content before training/inference)
2. Robust input validation
3. Enforce strict access controls (least privilege)
4. Restrict data sources
5. Federated learning / differential privacy
6. User education on safe LLM usage
7. Conceal system preamble
8. Homomorphic encryption / tokenization / redaction

**Automated Tooling:**

| Tool | Type | Stars | Last Push | Notes |
|---|---|---|---|---|
| [microsoft/presidio](https://github.com/microsoft/presidio) | PII detection + anonymization | 7,597 | 2026-04-14 | Industry standard for PII detection and anonymization. Python + .NET. Recognizers for names, SSN, credit cards, phone, email, etc. |
| [NVIDIA/NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) | Output filtering | 5,972 | 2026-04-14 | Can block sensitive data in outputs via configurable rails |
| [guardrails-ai/guardrails](https://github.com/guardrails-ai/guardrails) | Output validation | 6,673 | 2026-04-03 | Schema-based validation can enforce no-PII constraints |

**Confidence:** L1 (Verified) — Microsoft Presidio is the gold standard for PII handling. MITRE ATLAS: AML.T0024.000 (membership inference), AML.T0024.001 (model inversion), AML.T0024.002 (model extraction).

---

### LLM03:2025 — Supply Chain

**Description:** Vulnerabilities in third-party models, datasets, LoRA adapters, plugins, packages. Includes PoisonGPT-style model tampering, compromised HuggingFace repos, vulnerable dependencies.

**OWASP Mitigations:**
1. Vet data sources and suppliers; review T&Cs and privacy policies
2. Apply OWASP A06:2021 (Vulnerable and Outdated Components) — scanning, patching, SBOM
3. AI red teaming before adopting third-party models
4. Maintain SBOM/AI-BOM (OWASP CycloneDX)
5. License inventory via BOMs
6. Use verifiable sources + code signing + file hashes
7. Monitor collaborative model dev environments
8. Anomaly detection on supplied models/data
9. Patching policy for models and dependencies
10. Encrypt edge-deployed models with integrity checks

**Automated Tooling:**

| Tool | Type | Stars | Last Push | Notes |
|---|---|---|---|---|
| [OWASP CycloneDX](https://cyclonedx.org/) ([Python](https://github.com/CycloneDX/cyclonedx-python)) | SBOM generation | 370 | 2026-04-13 | OWASP standard for software/material BOMs. Emerging AI-BOM support. |
| [pip-audit](https://github.com/pypa/pip-audit) | Dependency scanning | — | — | Already in this repo's justfile. PyPA's official vulnerability scanner. |
| [CycloneDX/cyclonedx-python](https://github.com/CycloneDX/cyclonedx-python) | AI-BOM generation | 370 | 2026-04-13 | Generate SBOMs for Python projects; supports component hashing |

**Confidence:** L1 (Verified) for CycloneDX and pip-audit. MITRE ATLAS: AML.T0010 (ML Supply Chain Compromise).

---

### LLM04:2025 — Data and Model Poisoning

**Description:** Pre-training, fine-tuning, or embedding data manipulated to introduce backdoors, biases, or vulnerabilities.

**Mitigations:** (Cross-references LLM03 supply chain mitigations)
1. Vet training data sources
2. Anomaly detection in training pipelines
3. Red teaming and adversarial evaluation
4. Model provenance verification
5. Differential privacy during training

**Automated Tooling:**

| Tool | Type | Stars | Last Push | Notes |
|---|---|---|---|---|
| [leondz/garak](https://github.com/leondz/garak) | Vulnerability scanning | 7,535 | 2026-04-13 | Probes for backdoors, poisoning indicators, known-bad patterns |
| [Giskard-AI/giskard](https://github.com/Giskard-AI/giskard) | Model testing | 5,256 | 2026-04-14 | Detects bias, performance degradation from poisoned data |
| [meta-llama/PurpleLlama](https://github.com/meta-llama/PurpleLlama) | Security benchmarks | 4,121 | 2026-04-13 | CyberSecEval benchmarks for safety evaluation |

---

### LLM05:2025 — Improper Output Handling

**Description:** Insufficient validation/sanitization of LLM outputs before passing to downstream systems. Enables XSS, CSRF, SSRF, SQL injection, RCE.

**OWASP Mitigations:**
1. Treat model as untrusted user — zero-trust on model outputs
2. Follow OWASP ASVS for input validation
3. Encode outputs contextually (HTML, JS, SQL)
4. Parameterized queries for all DB operations
5. Strict Content Security Policies (CSP)
6. Robust logging and monitoring

**Automated Tooling:**

| Tool | Type | Stars | Last Push | Notes |
|---|---|---|---|---|
| [guardrails-ai/guardrails](https://github.com/guardrails-ai/guardrails) | Output validation | 6,673 | 2026-04-03 | Schema-based output validation; enforce types, formats, allowed values |
| [NVIDIA/NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) | Output rail enforcement | 5,972 | 2026-04-14 | Programmable output rails; block malicious patterns |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | LLM observability | 9,275 | 2026-04-14 | Monitor LLM outputs in production; trace anomalous responses |

---

### LLM06:2025 — Excessive Agency

**Description:** LLM granted too much functionality, permissions, or autonomy. Root causes: excessive functionality, excessive permissions, excessive autonomy.

**OWASP Mitigations:**
1. Minimize extensions (only necessary tools)
2. Minimize extension functionality (read-only where possible)
3. Avoid open-ended extensions (no raw shell/URL fetch)
4. Minimize extension permissions (least privilege on downstream systems)
5. Execute in user's context (OAuth with minimal scope)
6. Require user approval for high-impact actions (human-in-the-loop)
7. Complete mediation (authorization in downstream systems, not LLM)
8. Sanitize LLM inputs/outputs; apply SAST/DAST/IAST

**Lethal Trifecta Connection:** This is the PRIMARY risk enabling the trifecta. Excessive agency = too many tools with too much access. The trifecta is the exploitation path.

**Architectural Mitigations:** See CaMeL and design patterns above (LLM01). Key principle: **once an LLM has ingested untrusted input, it must be constrained so it is IMPOSSIBLE for that input to trigger consequential actions.**

**Automated Tooling:**

| Tool | Type | Stars | Last Push | Notes |
|---|---|---|---|---|
| [NVIDIA/NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) | Action constraint | 5,972 | 2026-04-14 | Can constrain which actions an LLM agent can take |
| [leondz/garak](https://github.com/leondz/garak) | Agent security testing | 7,535 | 2026-04-13 | Probe agents for unauthorized action capabilities |

---

### LLM07:2025 — System Prompt Leakage

**Description:** System prompts or internal instructions exposed to users/attackers. Reveals internal logic, API keys, infrastructure details.

**Mitigations:**
1. Never put secrets in system prompts
2. Treat system prompts as public — assume they will leak
3. Implement access controls independent of prompt content
4. Monitor for prompt extraction attempts

**Automated Tooling:**

| Tool | Type | Stars | Last Push | Notes |
|---|---|---|---|---|
| [leondz/garak](https://github.com/leondz/garak) | Leakage probing | 7,535 | 2026-04-13 | Includes probes for system prompt extraction |

---

### LLM08:2025 — Vector and Embedding Weaknesses

**Description:** Vulnerabilities in RAG systems — embedding inversion, data poisoning via vector stores, unauthorized access to embeddings.

**Mitigations:**
1. Access controls on vector stores
2. Input sanitization before embedding
3. Monitor embedding queries for extraction attempts
4. Encrypt sensitive embeddings

**Automated Tooling:**

| Tool | Type | Stars | Last Push | Notes |
|---|---|---|---|---|
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | RAG observability | 9,275 | 2026-04-14 | Trace RAG retrieval quality, detect anomalous embedding queries |
| [deepset-ai/haystack](https://github.com/deepset-ai/haystack) | RAG framework | 24,830 | 2026-04-14 | Built-in security controls for RAG pipelines |

---

### LLM09:2025 — Misinformation

**Description:** LLMs produce false, inaccurate, or misleading content (hallucinations/confabulations). Applications relying on factual accuracy are vulnerable.

**Mitigations:**
1. RAG with verified data sources
2. Output verification against source documents
3. Confidence scoring and human review
4. Clear disclaimers about AI-generated content

**Automated Tooling:**

| Tool | Type | Stars | Last Push | Notes |
|---|---|---|---|---|
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | Hallucination detection | 9,275 | 2026-04-14 | RAG triad evaluation (relevance, groundedness, Q/A relevance) |
| [Giskard-AI/giskard](https://github.com/Giskard-AI/giskard) | Hallucination testing | 5,256 | 2026-04-14 | Automated hallucination detection in test suites |
| [guardrails-ai/guardrails](https://github.com/guardrails-ai/guardrails) | Fact-checking validators | 6,673 | 2026-04-03 | Can validate outputs against reference documents |

---

### LLM10:2025 — Unbounded Consumption

**Description:** No limits on resource usage — token consumption, API calls, compute. Enables denial-of-service (cost or availability), data extraction via repeated queries.

**Mitigations:**
1. Rate limiting on LLM API calls
2. Token/cost budgets per user/session
3. Input length constraints
4. Monitor usage patterns for anomalies
5. Resource caps on inference infrastructure

**Automated Tooling:**

| Tool | Type | Stars | Last Push | Notes |
|---|---|---|---|---|
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | Usage observability | 9,275 | 2026-04-14 | Token usage tracking, cost monitoring, anomaly detection |
| [NVIDIA/NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) | Flow control | 5,972 | 2026-04-14 | Can limit conversation turns and action frequency |

---

## Tooling Summary — Verified Active Projects

| Tool | Category | Stars | Status | Last Active | Recommendation |
|---|---|---|---|---|---|
| **NeMo-Guardrails** (NVIDIA) | Guardrails/orchestration | 5,972 | Active | 2026-04-14 | **Primary** — most versatile, covers LLM01/02/05/06/10 |
| **garak** (leondz) | Vulnerability scanning | 7,535 | Active | 2026-04-13 | **Primary** — red teaming, covers LLM01/04/06/07 |
| **PurpleLlama** (Meta) | Benchmarks/scanning | 4,121 | Active | 2026-04-13 | **Recommended** — injection classification, safety eval |
| **guardrails-ai** | I/O validation | 6,673 | Active | 2026-04-03 | **Recommended** — schema-based output validation |
| **Presidio** (Microsoft) | PII handling | 7,597 | Active | 2026-04-14 | **Primary** for LLM02 — PII detection/anonymization |
| **Phoenix** (Arize) | Observability | 9,275 | Active | 2026-04-14 | **Recommended** — production monitoring, hallucination detection |
| **Giskard** | Testing/evaluation | 5,256 | Active | 2026-04-14 | **Recommended** — automated test suite generation |
| **CycloneDX** (OWASP) | SBOM/AI-BOM | 370 | Active | 2026-04-13 | **Primary** for LLM03 — supply chain inventory |
| **inspect_ai** (UK AISI) | Safety evaluation | 1,901 | Active | 2026-04-14 | **Recommended** — government-backed LLM eval framework |

### Archived / Abandoned

| Tool | Stars | Status | Note |
|---|---|---|---|
| [protectai/rebuff](https://github.com/protectai/rebuff) | 1,459 | **Archived** | Was prompt injection detection. Archived Aug 2024. Do not use. |

---

## Key Academic References

| Paper | Year | Key Contribution |
|---|---|---|
| [CaMeL: Defeating Prompt Injections by Design](https://arxiv.org/abs/2503.18813) | 2025 | Sandboxed Python DSL with capability-based data flow tracking. First "strong guarantees" claim. |
| [Design Patterns for Securing LLM Agents](https://arxiv.org/abs/2506.08837) | 2025 | Six architectural patterns (Action-Selector through Context-Minimization). Realistic trade-offs. |
| [The Dual LLM Pattern](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/) (Willison) | 2023 | Privileged + quarantined LLM architecture. Basis for CaMeL. |

---

## Mitigation Priority Matrix

For any agent system combining tools + LLMs:

```
HIGH PRIORITY (do first):
  ├── Never combine all three trifecta components in one agent
  ├── Human-in-the-loop for all destructive/irreversible actions
  ├── Least privilege on all tool permissions (read-only where possible)
  ├── PII scanning on all inputs/outputs (Presidio)
  └── Rate limiting and cost budgets

MEDIUM PRIORITY (architectural):
  ├── Implement one of the six design patterns (CaMeL strongest)
  ├── Separate trusted/untrusted content in prompt context
  ├── Output validation against schemas (guardrails-ai)
  └── Regular adversarial scanning (garak, PurpleLlama)

ONGOING (operational):
  ├── Production monitoring (Phoenix)
  ├── SBOM maintenance (CycloneDX)
  ├── Red team exercises (garak, Giskard, inspect_ai)
  └── Stay current on prompt injection research
```

---

## Implementation Status — Security Layer (`security_layer/`)

VSDD (Verified Spec-Driven Development) pipeline tracking via Chainlink. All OWASP mitigations mapped to implemented modules.

### Pipeline Progress

| VSDD Phase | Status | Evidence |
|:-----------|:-------|:---------|
| **Phase 1 — Spec Crystallization** | COMPLETE | #2-#5 closed (behavioral contract, verification architecture, edge cases, NFRs) |
| **Phase 2 — TDD Implementation** | COMPLETE | 172 tests, all GREEN |
| **Phase 3 — Adversarial Roast** | COMPLETE | #6 closed — 18/18 findings addressed (10 original + 8 secondary) |
| **Phase 4 — Feedback Integration** | COMPLETE | All findings fixed, deferred items resolved |
| **Phase 5 — Formal Hardening** | COMPLETE | #7 closed — 28 hypothesis fuzz tests passed, purity boundary audited. Mutation testing deferred (mutmut 3.5.0 crash, tooling defect). Formal proofs N/A for Python; property-based fuzz accepted as language-appropriate verification. |
| **Phase 6 — Convergence** | CONVERGED | All four dimensions met. See Convergence Check below. |

### Test Coverage

| Suite | Count | Status |
|:------|:------|:-------|
| Original spec-driven tests | 172 | GREEN |
| Phase 5 fuzz + purity tests | 28 | GREEN |
| CUSTOM_RULES stage tests | 8 | GREEN |
| **Total** | **208** | **GREEN** |

### OWASP Mitigation → Module Mapping

| OWASP Risk | Mitigation Module | Status |
|:-----------|:------------------|:-------|
| LLM01 (Prompt Injection) | `classifier.py`, `output_validation.py`, `scanning.py` (CUSTOM_RULES) | Implemented + fuzzed |
| LLM02 (Info Disclosure) | `pii.py` (Presidio), `output_validation.py` | Implemented |
| LLM03 (Supply Chain) | `scanning.py` (pip-audit stage) | Implemented |
| LLM04 (Data Poisoning) | `scanning.py` (GARAK stage) | Implemented |
| LLM05 (Output Handling) | `output_validation.py` | Implemented + fuzzed |
| LLM06 (Excessive Agency) | `permissions.py`, `trifecta.py` | Implemented + fuzzed |
| LLM07 (System Prompt Leakage) | `output_validation.py` (injection detection) | Implemented |
| LLM08 (Embedding Weaknesses) | Not in scope (no RAG) | — |
| LLM09 (Misinformation) | `output_validation.py` (schema validation) | Implemented |
| LLM10 (Unbounded Consumption) | `budget.py` | Implemented + fuzzed |

### Purity Boundary Map

```
PURE CORE (no I/O, deterministic, fuzz-tested):
  ├── budget.py            — check_budget, add_tokens, estimate_cost, check_daily_budget
  ├── output_validation.py — check_injection_patterns, validate_schema, strip_external_urls
  ├── models.py            — all frozen dataclasses (structural invariants verified)
  ├── state_machine.py     — generic StateMachine[S,E,C] transitions
  ├── permissions.py       — check_path_traversal, can_flow_to_destructive
  ├── trifecta.py          — check_trifecta_violation, create_sub_agent
  └── scanning.py          — CUSTOM_RULES stage (regex matching, no I/O)

EFFECTFUL SHELL (I/O, mutation, external deps):
  ├── pii.py               — detect_pii (Presidio analyzer), redact_pii (pure)
  ├── scanning.py          — SEMGREP stage (file read), check_no_secrets_in_prompts (file read)
  └── hitl.py              — request_approval/approve/deny (module-level dict mutation)
```

### Outstanding Work Items

| # | Item | Severity | Status |
|---|------|----------|--------|
| 1 | OSS license attribution (pip-licenses) | Low | **DONE** — `docs/THIRD_PARTY_LICENSES.md` |
| 2 | Pre-existing ruff lint (unused imports, StrEnum migration) | Low | **DONE** — 24 issues fixed, `ruff check` clean |

### Convergence Check

| Dimension | Signal |
|:----------|:-------|
| **Spec** | CONVERGED — adversary down to wording nitpicks |
| **Tests** | CONVERGED — 208/208 green, hypothesis fuzz testing passed |
| **Implementation** | CONVERGED — all findings fixed |
| **Verification** | CONVERGED — hypothesis fuzz + purity audit accepted as Python-appropriate. Formal proofs N/A for Python. Mutation testing deferred (mutmut 3.5.0 tooling bug). |
