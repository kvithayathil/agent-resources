---
name: vdd
description: >
  Verification-Driven Development. Use when writing implementation code, refactoring, fixing bugs,
  or any task where correctness matters. Enforces a verify-before-trust discipline: every piece of
  behavior must have a verifiable check before it is considered done. Triggers on: verify, validation,
  correctness, testing, TDD, acceptance criteria, specification, contract, invariant, property-based.
tags:
  - development
  - verification
  - testing
  - correctness
  - methodology
license: Apache-2.0
metadata:
  author: kvithayathil
  version: "1.0.0"
  living: "true"
  self-learning: "true"
  self-updating: "true"
  update-policy: "evolve-on-evidence"
  last-reviewed: "2026-04-18"
source:
  gist: https://gist.github.com/dollspace-gay/45c95ebfb5a3a3bae84d8bebd662cc25
  gist_id: 45c95ebfb5a3a3bae84d8bebd662cc25
  fetched_at: "2026-04-18T02:25:22Z"
---

# Verification-Driven Development (VDD)
---

## Overview

Verification-Driven Development is a discipline where **verification is the primary driver of
design and implementation decisions**. Every behavior must be verifiable before it ships. Unlike
pure TDD (which focuses on unit tests), VDD spans the full verification spectrum: types, contracts,
properties, tests, linting, static analysis, and runtime checks.

Core principle: **If you cannot verify it, you do not ship it.**

## When to Use

- Writing new features or modifying existing code
- Refactoring or restructuring code
- Fixing bugs (verify the fix, verify no regression)
- Designing APIs, interfaces, or contracts
- Any task where correctness, reliability, or safety matters
- When reviewing code for quality and completeness

**Don't use when:**

- Pure exploration / prototyping (but apply before merging)
- Documentation-only changes

## Self-Learning / Self-Updating Protocol

> **This skill is self-learning and self-updating.** It improves itself through use.
> The agent is explicitly authorized and expected to modify this skill's files
> when new evidence warrants it.
>
> ### What "Self-Learning" Means Here
>
> This skill accumulates real-world experience. Every time the agent encounters
> a verification gap, a new pattern, a gotcha, or a better technique during actual
> work, that knowledge is fed back into the skill so it performs better next time.
>
> ### What "Self-Updating" Means Here
>
> The agent actively edits the skill's files to incorporate new knowledge — it does
> not just passively record lessons but restructures, prunes, and refines the skill
> itself based on accumulated evidence.
>
> ### Agent Instructions for Self-Update
>
> 1. **Append to Lessons Learned** — When you discover a verification gap, a new
>    gotcha, or a pattern that worked well, add it to
>    [references/LESSONS_LEARNED.md](references/LESSONS_LEARNED.md) with date
>    and context.
> 2. **Update Gotchas** — When you encounter a surprise or non-obvious behavior
>    during verification, add it to the Common Mistakes table in this file.
> 3. **Promote Lessons** — When a lessons-learned entry has been validated 3+
>    times across different tasks, promote it into the main SKILL.md instructions
>    and remove it from LESSONS_LEARNED.md.
> 4. **Prune Stale Content** — If an instruction proves unnecessary after repeated
>    use (agent handles it fine without), remove it. Lean skill > exhaustive skill.
> 5. **Increment Version** — After any substantive update, increment the `version`
>    in frontmatter and update `last-reviewed` to today's date.
> 6. **Record in Changelog** — Add an entry to
>    [references/CHANGELOG.md](references/CHANGELOG.md) describing what changed
>    and why, with the trigger (what task/situation prompted the update).
>
> ### Self-Update Triggers
>
> Perform a self-update cycle when ANY of these occur:
>
> - A test passed but a bug still shipped (verification gap)
> - A new verification tool or technique proved useful
> - A gotcha was discovered that wasn't in the skill
> - A pattern was followed successfully 3+ times (promote to instruction)
> - An instruction was ignored by the agent 3+ times (rewrite or remove it)
> - A user corrected the agent's verification approach
>
> ### Self-Update Constraints
>
> - Only update based on **evidence from real tasks**, not hypothetical improvements.
> - Keep the main SKILL.md under 500 lines; move detail to references/.
> - Never remove the Self-Learning/Self-Updating Protocol section itself.

## Instructions

### Step 1: Define Verifiable Specifications

Before writing code, establish what "correct" means:

1. Extract acceptance criteria from the task description
2. Identify invariants: properties that must always hold
3. Define contracts: preconditions, postconditions, and invariants for each boundary
4. Choose verification levels:
   - **Type-level**: Can the type system enforce this? (preferred)
   - **Compile-time**: Can static analysis catch violations?
   - **Test-time**: Does a test cover this behavior?
   - **Runtime**: Must this be checked at runtime? (last resort)

### Step 2: Write Verification First

Follow this order (not strict TDD — broader verification spectrum):

```
SPECIFY → VERIFY (red) → IMPLEMENT (green) → REFIN
```

1. Write the specification (types, contracts, property descriptions)
2. Write the verification (test, property test, lint rule, type constraint)
3. Confirm it fails (the "red" state)
4. Write minimal implementation to pass
5. Confirm it passes (the "green" state)
6. Refactor while keeping verification green

### Step 3: Layer Verification Strategically

Not everything needs a unit test. Match verification strength to risk:

| Risk Level | Verification Approach | Examples |
|------------|----------------------|----------|
| Low | Type signatures, linter | Helper formatting, simple transforms |
| Medium | Unit tests, property tests | Business logic, data transformations |
| High | Integration tests, contracts | Payment flows, auth, data integrity |
| Critical | Formal specs, fuzz testing | Crypto, consensus, safety-critical paths |

### Step 4: Verify the Verification

After implementation:

1. **Mutation testing**: Does the test actually catch bugs? Change implementation, see if tests fail.
2. **Coverage check**: Are uncovered paths acceptable risks or gaps?
3. **Boundary analysis**: Test at edges — empty, single, maximum, negative, null/undefined.
4. **Property invariants**: For any valid input, does the output satisfy stated properties?

### Step 5: Gate Completion on Verification

A task is NOT done until:

- [ ] Every acceptance criterion has a passing verification
- [ ] Verification runs in CI (not just locally)
- [ ] Edge cases are covered or explicitly documented as accepted risk
- [ ] No verification is skipped, commented out, or marked `.skip`
- [ ] Verification failures produce actionable error messages

## Examples

### Example 1: Type-Level Verification (Preferred)

**Input:** A function that processes user age
**Output:** Type signature that makes invalid states unrepresentable

```typescript
// Instead of: function processAge(age: number): Result
// Use a type that prevents negative ages at compile time:
type Age = number & { readonly __brand: unique symbol };
function createAge(n: number): Result<Age, Error> {
  return n >= 0 && n <= 150 ? ok(n as Age) : err("Invalid age");
}
```

### Example 2: Contract-Based Verification

**Input:** An API endpoint
**Output:** Pre/postconditions documented and tested

```
PRE: request.user is authenticated
PRE: request.body.id matches UUID format
POST: response contains updated resource with server-generated timestamp
POST: response.status is 200 or 201 (never 500 for valid input)
INVARIANT: created resources always have an id, createdAt, updatedAt
```

### Example 3: Property-Based Verification

**Input:** A sort function
**Output:** Properties that hold for ALL inputs

```
PROPERTY: sort(sort(x)) === sort(x)          -- idempotent
PROPERTY: sort(x).length === x.length        -- preserves length
PROPERTY: for i in 0..n-1: sort(x)[i] <= sort(x)[i+1]  -- ordered
PROPERTY: every element in x appears in sort(x)          -- no loss
```

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Writing tests after implementation | Write verification first — it shapes better design |
| Testing only the happy path | Add boundary and error cases to acceptance criteria |
| 100% code coverage obsession | Cover behavior, not lines; accept risk trade-offs |
| Brittle snapshot tests | Test properties and invariants, not exact output |
| Mocking everything | Mock at boundaries; test real logic with real dependencies |
| Skipping mutation testing | Verify your tests actually catch bugs |
| Trusting type `any` / unchecked casts | Use narrow types and runtime guards at boundaries |
| One assertion per test dogma | Group related assertions; test one behavior, not one assert |

## Gotchas

- A passing test suite does NOT mean the code is correct — it means the tested properties hold.
- Coverage percentage is a smell metric, not a quality metric. 80% meaningful coverage > 100% shallow.
- Mocking external systems but not testing the real integration is a common source of production failures.
- Property-based tests find bugs unit tests miss, but are slower. Use both strategically.
- Runtime validation at system boundaries (API input, file parsing) is non-negotiable even with types.

## References

- [references/LESSONS_LEARNED.md](references/LESSONS_LEARNED.md) — Evolving log of patterns and anti-patterns
- [references/CHANGELOG.md](references/CHANGELOG.md) — History of skill updates
- [references/VERIFICATION_LEVELS.md](references/VERIFICATION_LEVELS.md) — Detailed verification strategy guide
