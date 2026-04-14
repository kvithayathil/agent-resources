# Verification Levels Reference

## Detailed guide for choosing and applying verification strategies.

## Level 0: Type System

Let the compiler catch bugs. This is the cheapest and most reliable verification.

- Use discriminated unions instead of optional fields
- Use branded types for domain primitives (UserId, Email, Age)
- Make illegal states unrepresentable
- Prefer `Result<T, E>` over thrown exceptions for recoverable errors

## Level 1: Static Analysis

Automated tools that catch classes of bugs without writing tests.

- Linters (ESLint, Ruff, clippy)
- Type checkers (TypeScript strict, mypy --strict)
- Security scanners (SAST tools)
- Dependency audit (npm audit, pip audit)

## Level 2: Unit Tests

Verify individual functions and modules in isolation.

- Test behavior, not implementation
- Use descriptive test names that read as specifications
- Test at boundaries: empty, single, many, edge cases
- Keep tests fast and deterministic

## Level 3: Property-Based Tests

Verify invariants hold for ALL valid inputs, not just examples you thought of.

- Define properties (associativity, idempotency, round-trip)
- Use shrinking to find minimal failing cases
- Combine with unit tests for coverage

## Level 4: Integration Tests

Verify components work together correctly.

- Test at module/service boundaries
- Use real dependencies where feasible
- Test error propagation and recovery
- Verify contracts between components

## Level 5: End-to-End Tests

Verify the system as a whole satisfies user-facing requirements.

- Test critical user journeys
- Test against production-like environment
- Accept slower execution for higher confidence
- Keep count small; these are expensive

## Level 6: Formal Verification

Mathematically prove correctness for critical components.

- Model checking for concurrent systems
- Theorem proving for algorithms
- Use only when the cost of failure justifies the investment
