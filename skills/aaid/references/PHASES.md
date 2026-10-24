# AAID Phases Reference

Load when a development phase is about to start: this file carries the route
decision, prerequisite gate, state-tracking format, and the RED → GREEN → REFACTOR cycle
with its mandatory human review stops. Pair it with `CHECKLIST.md` for reviews.

## 1. Prerequisite gate (before any route is chosen)

Do not begin phase work until both of these hold:

1. **Approved work definition.** User stories with behavioral scenarios, or approved
   technical contracts for infrastructure work, that the human has accepted. Unapproved
   scenario ideas are suggestions for the human, never a license to invent targets.
2. **Working project tooling.** A project that builds, a functioning test runner, and a
   usable linter, on the branch being worked on.

Project scaffolding (framework generators, config files, package installation, commit
hooks) sits **outside** the cycle. It is plain setup: perform it only when asked, verify
it by running it, and never dress it up as a TDD phase. AAID phases apply once custom
code with testable behavior is the subject.

**If any prerequisite is missing:** report precisely what is missing, and ask the human
for direction. Do not scaffold on your own initiative, draft business scenarios to fill
the gap, or pick a route by guessing. Missing prerequisites produce questions, not work.

## 2. Route determination

Classify the request into exactly one of four routes before touching code. Read the
available architecture notes and project conventions first; they inform every route.

| Route | Signals | Testing approach |
| --- | --- | --- |
| **Behavioral TDD** | Business rules, use cases, domain logic; user-visible behavior expressible as scenarios | Unit tests (mock per `DEPENDENCIES.md`), and/or acceptance tests when commercially required |
| **Acceptance** | User asks for acceptance/ATDD work, supplies BDD scenarios, or the feature needs an executable definition of done | Four-layer suite per `ATDD.md` and `ATDD-PHASES.md` |
| **Technical contract** | Words like adapter, repository, controller, middleware, infrastructure; work that connects the domain to databases, caches, queues, or third-party APIs | Integration tests for managed dependencies, contract tests for unmanaged ones (`DEPENDENCIES.md`, `ROADMAP-TECHNICAL.md`) |
| **Presentation** | Styling, colors, spacing, animation, audio, haptics, some accessibility properties; no logic under test | Explicit manual / visual / accessibility criteria; never a forced unit test (`ROADMAP-PRESENTATION.md`) |

Rules for classification:

- Behavior is judged at each abstraction's own consumer: a cache adapter has behavior
  ("invalidates the entry when the source changes") — technical contract, not presentation.
- Mixed requests are **split** and the split is announced before starting either half:
  a story with "archives completed todos" (behavioral) plus "archived items render
  gray" (presentation) becomes a behavioral task cycled here and a presentation task
  per `ROADMAP-PRESENTATION.md`. Unclear routes go to the human as a question.

### Plan-only and context-only requests

Sharing architecture context, asking for a plan, or standing in a planning mode
authorizes **conversation and documents only** — even if the plan text names files.
Pre-staging code, stage changes, or TODO lists do not convert planning into an
implementation authorization.

## 3. Conversational state summary

Maintain one compact state summary, restated with every announcement and kept current
throughout the session. Use this shape:

```
ROUTE:        behavioral | acceptance | technical | presentation
PHASE:        context → planning → RED | GREEN | REFACTOR (or P1/P2/P3)
SCENARIO/TEST: <one-line name of the test currently in play>
PENDING TESTS: <numbered list of remaining planned tests; only with test-list route>
LAST COMMAND: <the exact command run, with its test name if relevant>
LAST OUTPUT:  <condensed but faithful result, incl. failure message if red>
EXIT STATUS:  0 | <code>
AWAITING:     <human review of <phase>> | nothing
```

Every summary statement without a fresh human approval names `AWAITING: human review of
<phase>`; once approval lands, record it before moving on.

## 4. The RED → GREEN → REFACTOR cycle

One test at a time. Full cycle per test. No phase skipping, no batching tests, no
pre-implemented suites: a pending test list is an outline of intent, not delivered work.

### RED — smallest failing test

- Write the smallest test that expresses the next requirement. When a test list exists,
  pick up the next outline item; otherwise write the next test from the approved plan.
- Order tests by the ZOMBIES progression (`ZOMBIES.md`, loaded when test order is chosen).
- Run the test. The expected result is failure — including a compile/import failure, which
  counts as a legitimate failing state.
- Verify that the failure is the *expected* failure (right test counts, message matching
  the intended missing behavior), then **STOP for human review**.
- If the test passes without implementation: unexpected result; STOP and report the
  anomaly immediately (`CHECKLIST.md`, "RED review"). Do not auto-repair code, rename the
  test to force it to fail, or invent a different test to chase a red result.

### GREEN — minimal implementation

- Write the minimum behavior the current test demands. Naive or hard-coded responses are
  acceptable at this stage; later tests must force generality, never speculation.
- Run the current test **and** the existing suite. Both must be green before review.
- **STOP for human review.**
- Any failure in current or existing tests means: report which tests failed with real
  output, then await direction. Never cross the review checkpoint with a regression
  outstanding.

### REFACTOR — explicit, even when it is a no-op

- Explicitly evaluate whether the code just written deserves improvement: naming,
  duplication, cohesion, readability.
- If improvements are made, rerun the tests after each change and keep them green; a
  broken refactor is reported, then the human chooses between a minimal fix and a revert.
- If evaluation finds nothing worth changing, **state "no refactoring needed" explicitly**
  — the phase still happened. A silent skip is a rule violation.
- Rerun the relevant tests and **STOP for human review** before starting the next test.

A "later phase" comment approves that one transition only, if it names it explicitly.
Silence, your own self-assessment, a completed checklist, or a vague future promise is
not approval and must not move the state.

## 5. Worked phase-boundary examples

### Example A — RED stop with an expected failure

State before: `ROUTE behavioral · PHASE RED · TEST "empty cart shows zero total" ·
AWAITING nothing`.

The test is written and run:

```
$ npm test -- --filter cart-empty-total
FAIL cart.spec.ts › empty cart shows zero total
  AssertionError: expected 0 to equal undefined
9 passed, 1 failed, 10 total — exit status 1
```

The failure is exactly the intended one (no total exists yet) and the test name reads as
behavior. Announcement:

```
STATE: ROUTE behavioral · PHASE RED · TEST "empty cart shows zero total"
LAST COMMAND: npm test -- --filter cart-empty-total
LAST OUTPUT: AssertionError: expected 0 to equal undefined (9 passed, 1 failed)
EXIT STATUS: 1
AWAITING: human review of RED
```

Then stop; the next action belongs to the human.

### Example B — RED stop on an unexpected pass

The same test unexpectedly reports `10 passed, 0 failed — exit status 0`: either leftover
implementation covers this behavior or the test asserts nothing real. Neither can be
resolved by continuing. Announcement:

```
STATE: ROUTE behavioral · PHASE RED · TEST "empty cart shows zero total"
LAST COMMAND: npm test -- --filter cart-empty-total
LAST OUTPUT: 10 passed, 0 failed, 10 total — test passed with NO implementation written
EXIT STATUS: 0
AWAITING: human review of RED — ANOMALY: expected failure, observed pass
```

Then stop. Candidate causes may be *listed* as observations (pre-existing implementation,
dead assertion, wrong test file); no fix or replacement test until the human decides.

### Example C — GREEN regression stop

Implementation for the current test passes it but breaks two neighboring tests. Phase
cannot close:

```
STATE: ROUTE behavioral · PHASE GREEN · TEST "archived todo sort order"
LAST COMMAND: npm test
LAST OUTPUT: 11 passed, 2 failed — "empty cart shows zero total", "cannot archive incomplete todo"
EXIT STATUS: 1
AWAITING: human review of GREEN — REGRESSION: 2 existing tests now fail
```

Then stop. The human chooses: fix forward minimally, or revert to the last green state;
the choice is not made unilaterally.

## 6. Phase determination and overrides

Priority when deciding the current phase:

1. **Explicit human statement** ("we are in RED on this test", "skip planning, go straight
   to phase 3") wins over every stored state and sequence rule.
2. Otherwise, **strict sequence** governs: RED → GREEN → REFACTOR → next test, and the
   recorded `AWAITING` gate in the state summary must be cleared by an explicit approval
   before the next phase.
3. If the state summary is missing, contradicted, or the conversation resumed under
   ambiguous conditions, **ask**. Never infer a phase, an approval, or a permission from
   turn count, elapsed time, or the presence of code.

**Pre-work gate check**: before writing any production test or implementation, or
starting any phase's work, re-read the recorded state summary and verify the prior
gate's approval is recorded in this session. Existing code, momentum, or a planned
next step never substitutes for that approval (per the sequence and no-inference
rules above).

Overrides are allowed within their owner's authority: a human may re-order tests, declare
a phase directly, request presentation-first work, or defer a planned test. Record each
override with its scope in the state summary; no override extends host permissions,
safety rules, or a plan-only boundary.

Feature completion claims need passing relevant behavior tests plus any recorded manual
evidence; a full test list outline, or suite infrastructure that merely executes, is not
completion. For acceptance work, load `ATDD-PHASES.md` on entering the acceptance route
(and `ROADMAP-ACCEPTANCE.md` before its phase 1).
