# Security Patterns for LLM Agent Systems

> Context: OWASP LLM Top 10 + Lethal Trifecta mitigation for agent architectures
> Source: docs/security-mitigation-plan.md + implementation in security_layer/

## The Lethal Trifecta

An agent with all three capabilities simultaneously can be weaponized:
1. **Read** sensitive files (credentials, keys, configs)
2. **Fetch** external content (web, API responses)
3. **Act** with side effects (write files, execute shell, send network requests)

**Mitigation:** Trifecta separation — no single agent session holds all three. Sub-agents are isolated by capability domain. Orchestrator passes references, never raw content.

## Defense-in-Depth Pattern

Each security boundary is independent. Failure of one doesn't compromise others:

```
Input → [Classification] → [PII Detection] → [LLM] → [Output Validation] → Output
         gate 1             gate 2                      gate 3
```

All three gates must pass. Ordered from rawest to most processed form for early rejection.

## PII Density Escalation

Blanket redaction of high-PII-density content is a DoS vector. A config file with 20 API keys would be entirely redacted, destroying its utility.

**Pattern:** If PII density exceeds threshold (default 70%), escalate to human review instead of auto-redacting. The system flags it, a human decides.

## Taint Tracking for Tool Chains

Data from untrusted sources (web fetch, file reads of external content) carries a taint flag. Tainted data cannot flow into destructive tools (write, bash) without passing output validation.

```
web_fetch("https://evil.com/payload") → taint=UNTRUSTED
  → classify() → SUSPECTED_INJECTION → quarantined, never reaches LLM
```

## HITL Timeout = Default Deny

For destructive actions requiring human approval, timeout = deny. Never auto-approve. Never queue pending actions indefinitely.

## Agent Permission Reduction

Tool capabilities can only **decrease** during a session, never increase. Any escalation requires fresh user approval. This prevents privilege accumulation through context manipulation.

## Incident Response as Failsafe

Every mitigation will fail eventually. The incident response system (BC-9) is the safety net:
1. Log failure with full context
2. Alert security contact
3. Enter degraded-safe mode (read-only, no tools)
4. Remain degraded until human acknowledges

## Key Insight: Pure Core / Effectful Shell

Security *decisions* (redact/deny/allow/escalate) live in deterministic, side-effect-free functions. Security *detection* (PII via Presidio, classification via NLP) lives in the effectful shell. The pure core never depends on external state. Detection results flow in as typed data.

This separation means:
- Security logic is unit-testable without mocks
- Security logic is formally verifiable (Phase 5 target)
- Detection can be swapped (Presidio → GLiNER → custom) without touching decision logic
