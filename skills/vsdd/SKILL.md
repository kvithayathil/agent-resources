---
name: vsdd
description: >
  Verification-Driven System Design. Use when designing systems, architectures, APIs, data models,
  service boundaries, or any cross-cutting structural decision. Extends VDD principles to the system
  level: every architectural decision must be verifiable against stated requirements and constraints
  before it is committed. Triggers on: architecture, system design, design review, API design,
  data model, service boundary, migration plan, tech spec, RFC, architectural decision record, ADR.
tags:
  - architecture
  - system-design
  - verification
  - design-review
  - methodology
license: Apache-2.0
metadata:
  author: kvithayathil
  version: "1.0.0"
  living: "true"
  self-learning: "true"
  self-updating: "true"
  update-policy: "evolve-on-evidence"
  last-reviewed: "2026-04-14"
---

# Verification-Driven System Design (VSDD)

## Overview

Verification-Driven System Design extends VDD principles to the **system and architecture level**.
Every structural decision — service boundaries, data models, API contracts, deployment topologies —
must be verifiable against stated requirements and constraints before it is committed.

Core principle: **If you cannot verify a design decision against your requirements, you are not
ready to implement it.**

Where VDD focuses on code-level correctness, VSDD focuses on **structural correctness**: does the
architecture actually satisfy the system's requirements, constraints, and quality attributes?

## When to Use

- Designing new systems, services, or modules
- Defining API contracts or data models
- Planning migrations, refactors, or decompositions
- Writing technical specs, RFCs, or Architecture Decision Records (ADRs)
- Evaluating architecture against quality attributes (performance, security, scalability)
- Reviewing system designs for completeness and consistency

**Don't use when:**

- Individual function-level implementation (use VDD instead)
- Pure UI/UX design decisions (no structural verification needed)
- Incidents requiring immediate action (design verification is post-incident)

## Self-Learning / Self-Updating Protocol

> **This skill is self-learning and self-updating.** It improves itself through use.
> The agent is explicitly authorized and expected to modify this skill's files
> when new evidence warrants it.
>
> ### What "Self-Learning" Means Here
>
> This skill accumulates real-world design experience. Every time the agent encounters
> a design flaw, a missing quality attribute check, a new architectural pattern, or a
> verification gap during actual system design work, that knowledge is fed back into the
> skill so future designs are more rigorous.
>
> ### What "Self-Updating" Means Here
>
> The agent actively edits the skill's files to incorporate new knowledge — restructuring
> the verification checklist, adding new anti-patterns, refining decision frameworks, and
> pruning advice that proved unhelpful in practice.
>
> ### Agent Instructions for Self-Update
>
> 1. **Append to Lessons Learned** — When a design flaw is discovered post-implementation,
>    a quality attribute was missed, or a pattern proved particularly effective, add it to
>    [references/LESSONS_LEARNED.md](references/LESSONS_LEARNED.md) with date and context.
> 2. **Update Anti-Patterns** — When you encounter a structural mistake that wasn't caught
>    by the current checklist, add it to the Design Anti-Patterns table in this file.
> 3. **Promote Lessons** — When a lessons-learned entry has been validated 3+ times across
>    different designs, promote it into the main SKILL.md instructions or the verification
>    checklist and remove it from LESSONS_LEARNED.md.
> 4. **Prune Stale Content** — If an instruction is consistently ignored or proves
>    unnecessary across multiple design sessions, rewrite or remove it.
> 5. **Update Verification Checklist** — When a new verification dimension proves important
>    (e.g., a regulatory requirement, a new failure mode), add it to the checklist in
>    [references/VERIFICATION_CHECKLIST.md](references/VERIFICATION_CHECKLIST.md).
> 6. **Increment Version** — After any substantive update, increment the `version` in
>    frontmatter and update `last-reviewed` to today's date.
> 7. **Record in Changelog** — Add an entry to
>    [references/CHANGELOG.md](references/CHANGELOG.md) describing what changed and why.
>
> ### Self-Update Triggers
>
> Perform a self-update cycle when ANY of these occur:
>
> - A design was approved but led to a production incident (verification gap)
> - A quality attribute was overlooked (e.g., security, observability, cost)
> - A new architectural pattern or technology proved useful
> - A design review caught something the checklist missed
> - A pattern was followed successfully 3+ times (promote to instruction)
> - An instruction was ignored by the agent 3+ times (rewrite or remove it)
> - A user corrected the agent's design approach
>
> ### Self-Update Constraints
>
> - Only update based on **evidence from real designs**, not hypothetical improvements.
> - Keep the main SKILL.md under 500 lines; move detail to references/.
> - Never remove the Self-Learning/Self-Updating Protocol section itself.

## Instructions

### Step 1: Elicit and Structure Requirements

Before any design work:

1. **Functional requirements**: What must the system do? (user-facing behaviors)
2. **Quality attributes**: How well must it do them? Rank these explicitly:
   - Performance (latency, throughput)
   - Reliability / Availability
   - Security
   - Scalability
   - Observability
   - Cost constraints
   - Regulatory / Compliance
3. **Constraints**: What is fixed? (tech stack, team, timeline, existing systems)
4. **Invariants**: What must ALWAYS be true? (data consistency guarantees, SLAs, auth requirements)

Write these down. Unstated requirements cannot be verified.

### Step 2: Define Verifiable Design Criteria

For each requirement and quality attribute, define **how you will verify the design satisfies it**:

```
REQUIREMENT: "System must handle 10K requests/second"
VERIFICATION: Load test plan targeting 12K rps with p99 < 200ms
             Cost estimate for infrastructure at target load
             Identify bottleneck component via capacity analysis

QUALITY ATTRIBUTE: "Data consistency across services"
VERIFICATION: Define consistency model (eventual? strong? causal?)
             Map all write paths and identify race conditions
             Specify compensating actions for each failure mode
```

### Step 3: Design with Verification Points

Structure the design as a series of decisions, each with a verification gate:

```
DECISION: Use event-driven architecture with async messaging
VERIFICATION:
  - Message ordering guarantees documented and tested
  - Dead letter queue handling specified
  - Consumer idempotency verified
  - Backpressure strategy defined
  - Message schema evolution plan exists

DECISION: Separate read and write models (CQRS)
VERIFICATION:
  - Eventual consistency lag measured and acceptable
  - Read model rebuild strategy defined
  - Write model correctness verified independently
```

### Step 4: Verify Structural Soundness

Apply these structural verification checks:

| Dimension | Verify |
|-----------|--------|
| Coupling | Are service boundaries minimizing cascading failures? |
| Cohesion | Does each component have a single, clear responsibility? |
| Data flow | Are all data flows traced end-to-end with ownership? |
| Failure modes | Is there a failure mode for every component? Recovery defined? |
| Security boundaries | Are trust boundaries explicit? Auth/authz at each boundary? |
| Observability | Can you detect every failure mode from monitoring? |
| Evolution | Can the design accommodate likely changes without restructure? |

### Step 5: Verify Against Quality Attributes

For each ranked quality attribute, trace through the design:

1. **Performance**: Identify the critical path. Where is the latency budget spent?
2. **Reliability**: List single points of failure. What compensates for each?
3. **Security**: Trace the attack surface. Where are the trust boundaries?
4. **Scalability**: Which component hits its limit first? What scales independently?
5. **Cost**: Estimate cost at 1x, 10x, 100x current load. Where does it break?
6. **Compliance**: Which regulations apply? Where is personal data stored/processed?

### Step 6: Record and Review

1. Write an Architecture Decision Record (ADR) for each major decision
2. Include the verification criteria in the ADR
3. Have the design reviewed against the verification checklist:
   [references/VERIFICATION_CHECKLIST.md](references/VERIFICATION_CHECKLIST.md)
4. Mark each criterion as PASS, FAIL, or DEFERRED (with justification)

## Examples

### Example 1: Verifying a Service Boundary

**Design:** Split monolith into Order Service and Inventory Service

```
VERIFICATION:
  - [ ] Transaction boundaries: Can Order creation fail after Inventory
        reservation without inconsistency? (saga pattern verified)
  - [ ] Data ownership: No shared database tables between services
  - [ ] API contract: OpenAPI spec exists, backward-compat tested
  - [ ] Failure isolation: Inventory down → Orders can still be created
        (pending state) or gracefully rejected
  - [ ] Latency: Inter-service call adds < 50ms p99
```

### Example 2: Verifying a Data Model

**Design:** Event-sourced Order aggregate

```
VERIFICATION:
  - [ ] All state transitions represented as events
  - [ ] Events are immutable and append-only
  - [ ] Replay from events produces identical state
  - [ ] Schema evolution: new fields have defaults, old events replayable
  - [ ] Query performance: projection rebuild time < 5 minutes
```

## Design Anti-Patterns

| Anti-Pattern | Detection | Fix |
|-------------|-----------|-----|
| Distributed monolith | Services share a database or require sync calls for every operation | Own data, async communication |
| Hidden coupling | Change to service A breaks service B without obvious dependency | Map all integration points explicitly |
| Unbounded queues | Async processing with no backpressure or DLQ | Define capacity limits and overflow strategy |
| God service | One service handles too many responsibilities | Split by domain boundary, verify cohesion |
| Premature optimization | Designing for 100x load when current is 10x | Verify against actual + projected scale |
| Missing failure mode | No analysis of what happens when component X is down | Add failure analysis for every component |
| Implicit SLA | Performance/reliability targets exist only in conversations | Write them down, verify against them |

## Gotchas

- The #1 cause of architectural failures is not technical complexity but **missing quality attributes**.
  If nobody asked about security, cost, or observability, the design is incomplete.
- "It works on my machine" scales to "it works in staging" but not to "it works in production."
  Verify in environments that match production topology.
- Consistency models are not binary (strong vs eventual). Document the exact guarantees.
- A design that cannot be observed cannot be debugged. If you didn't design the monitoring,
  you didn't finish the design.
- Migration plans are part of the design. "We'll figure out migration later" is a design smell.

## References

- [references/LESSONS_LEARNED.md](references/LESSONS_LEARNED.md) — Evolving log of design patterns and failures
- [references/CHANGELOG.md](references/CHANGELOG.md) — History of skill updates
- [references/VERIFICATION_CHECKLIST.md](references/VERIFICATION_CHECKLIST.md) — Comprehensive design verification checklist
- [references/ADR_TEMPLATE.md](references/ADR_TEMPLATE.md) — Template for Architecture Decision Records
