# AAID Acceptance Checklist

Load whenever an acceptance phase is reviewed (P1/P2/P3 reviews, `ATDD-PHASES.md`) or
an existing acceptance suite is reviewed within an active acceptance phase.
Structure: layer purity (A) first, then
environment and isolation safety (B), then completion rules (C).

## Evidence standard

Same as every AAID review (`CHECKLIST.md`): decisions rest on real commands, outputs,
and exit codes. Suite readiness claims, checked-box progress, or "the suite is fine"
summaries are not evidence.

## A. Layer purity

### A1. DSL purity (layer 2)

- Zero assertions anywhere in layer 2. Any keyword like an assertion helper, an
  expectation API, or a boolean pass/fail return in DSL code is a violation — reported
  even if currently harmless ("unconditionally, not as a style preference").
- No remembered business state: the DSL must not store values from a scenario step for
  a later step to assert against. Isolation context (fresh per scenario) is its
  permitted memory.
- No I/O and no protocol knowledge in the DSL: it composes calls and translates
  vocabulary only.
- Method names read as the scenario's business language, and driver methods match the
  DSL method names 1:1.

### A2. Driver correctness (layer 3)

- All assertions live here and nowhere else; on failure the driver raises the
  language's natural error with a context-bearing message (no boolean verdicts, no
  framework-specific fail helpers).
- Verification queries the SUT, always — no trusting remembered test-side state.
- Async outcomes awaited by bounded polling with an explicit deadline and failure
  message; no fixed sleeps anywhere.
- Reaches the SUT only through the interfaces real consumers use; no internal calls
  into application code, no direct database queries bypassing the SUT boundary.
- Adding a behavior means updating the driver interface, not only a concrete
  implementation.

### A3. Specification discipline (layer 1)

- One approved scenario = one executable test; one Given/When/Then step = one DSL
  call. Merged or half-mapped scenarios are violations.
- Business-readable: no endpoints, status codes, selectors, or storage names in tests.

### A4. SUT integrity (layer 4)

- Owned persistence, cache, queues, internal services: all real, all part of the SUT.
  A proposal to stub any of them is **rejected on the spot** (`DEPENDENCIES.md`) and
  the review records the rejection.
- Only uncontrolled third parties are stubbed, and the suite's business verification
  never depends on what a stub was fed.

## B. Environment and isolation safety

### B1. Dedicated disposable environment

- The suite runs exclusively against a dedicated, disposable test environment — a
  deployment that can be discarded and rebuilt, with its own database and cache.
- **Never production, and never real user or business data.** A configuration pointing
  anywhere else stops the suite before it starts.

### B2. Per-scenario data partition

- Each scenario's first action creates its own boundary (fresh DSL context + a
  partition unique per scenario), and everything the scenario does stays inside it.
- Identifier aliasing must remain **collision-safe across parallel workers and repeat
  runs**. A naive per-worker counter is NOT sufficient: with a shared database, two
  workers (or repeat runs) can derive identical values. Uniqueness must come from
  globally distinguishing inputs (seed, run identity, or equivalent), and the alias
  mechanism must document what makes its identifiers globally unique.

### B3. Accumulation, not per-scenario cleanup

- **No cleanup after individual scenarios or after suites.** Aliased data accumulates;
  that is by design.
- The only cleanup point is **before the next suite run**, inside the dedicated test
  environment. Any teardown attached per-scenario (which would destroy parallel safety)
  is a violation.

### B4. Isolation proof

- Parallel run and repeat-run evidence (`ATDD-PHASES.md` phase 3) exists for the
  current suite state, with outputs and exit codes. If either run is missing or not
  demonstrable, the isolation proof is **blocked, not proven** — reported as such, never
  claimed.

## C. Completion rules (close-out)

A feature is complete only when **all** of the following hold at final review:

- Behavior: the relevant automated behavior tests pass in the final recorded run.
- Isolation: the parallel/repeat proof stands (or the block is explicit).
- Manual/visual criteria with applicable recorded evidence exist for presentation-side
  aspects (per `ROADMAP-PRESENTATION.md`).
- Infrastructure readiness — "P2 executed without infrastructure errors" — explicitly
  does **not** count as feature delivery, however convenient it would be.

The final review's STOP applies: only a human accepts, after seeing the recorded
evidence listed above.
