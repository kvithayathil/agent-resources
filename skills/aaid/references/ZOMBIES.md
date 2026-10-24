# AAID ZOMBIES Reference

Load when choosing the order of tests — at the start of a feature, when a test list is
created, or when the next test is selected. ZOMBIES is a sequencing heuristic for TDD:
it tells you which behaviors to reach for first so the implementation grows from simple
to rich in defensible steps.

## What the letters mean

| Step | Meaning | First test is about |
| --- | --- | --- |
| **Z** | Zero | The simplest possible situation: an empty collection, no inputs, nothing has happened yet |
| **O** | One | Exactly one item, one event, one invocation |
| **M** | Many | Several items interacting: lists, aggregation, repetition, ordering effects |
| **B** | Boundaries | Values at the edges of valid ranges and just outside them |
| **I** | Interface | Cross-cutting contracts: how consumers invoke this, parameter handling, error surfacing at the seam |
| **E** | Exceptions | Failure paths: invalid input, missing data, downstream errors, cancellations |
| **S** | Simple | A reminder to apply to both scenarios and the code: the simplest expression that is honest |

Z → O → M is the happy-path spine. B, I, and E are **interleaved**: after each spine step,
consider which of those three apply to what now exists, and take those tests before
advancing the spine further. Boundary and exception tests for a many-item behavior occur
after Many, not after One, because the behavior they probe only exists then.

## Why this order

- **Zero first** forces the empty/degenerate case to be handled deliberately, and gives
  the first test a trivially expressible expectation. A first test that starts on the
  happy path hides initial-state assumptions.
- **One before Many** keeps the first item's handling independent; aggregation logic
  never has to also explain single-item behavior.
- **Interleaving B/I/E** prevents building a multi-block happy path and then discovering
  its failure modes need a redesign. Each failure-path test lands while the code it
  stresses is still fresh and small.
- **Simple everywhere** guards against premature abstraction: ZOMBIES is an ordering
  tool, not a license to engineer ahead.

## Worked ordering example

Feature: a reading-list application tracks borrowed books.

A defensible test order:

1. **Z** — A fresh list with no items reports zero items.
2. **O** — One borrowed item is listed once.
3. **B** (for one) — Borrowing the same book twice is refused, not duplicated.
4. **I** (for one) — The listing API rejects an unknown borrower identifier with a
   well-formed error.
5. **M** — Three borrowed items are listed, all three present in the result.
6. **E** (for many) — A lost book is reported as overdue rather than silently re-listed.
7. **B** (for many) — A due date far in the past or absurdly far in the future is
   handled by the aggregation.
8. **E** (default instead of late) — If failures surfaced early in the domain, exchange
   steps as the behavior makes sense; the spine and the interleaving rule both still
   hold.

Notice what this order is not: it does not walk through every UI flow, and it does not
order tests by "what users do most". It orders by ascending shape of the data and rule
complexity.

## Interaction with route and test lists

- Behavioral route: ZOMBIES orders **unit tests directly; when a roadmap exists, the
  roadmap's scenario order is the starting outline, ZOMBIES refines the order of the
  tests within it**.
- Technical route: the same spine applies to integration/contract tests (`Z` = adapter
  with no stored state, `M` = multiple records/orders, `E` = provider error responses).
- With a test-list approach: write the outline in ZOMBIES order, then implement strictly
  one at a time (see `PHASES.md` §4). `skip`-style placeholders keep the outline visible
  without implementing ahead of the cycle.
- Never use ZOMBIES to justify test batches: the heuristic orders the queue; the cycle
  still processes it one test at a time with human review stops.
- Keep solutions simple at every step (`PHASES.md` GREEN rules hold throughout); when a
  Many step reveals a genuinely awkward abstraction, that finding goes to the human in
  the RED review rather than into speculative refactoring.
