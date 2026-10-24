# AAID Acceptance Phases — P1 / P2 / P3

Load as soon as the acceptance route is entered, after `ATDD.md`, and keep it in force
for every acceptance phase. Mirror of the TDD cycle but applied to the testing
infrastructure itself; every phase ends in a mandatory human stop. State is tracked
with the same summary format as `PHASES.md` §3, using P1/P2/P3 as phase values.

## Pre-phase requirements

Before P1 begins, all of the following must hold — otherwise report and ask:

1. Approved BDD scenarios exist (prerequisite gate, `PHASES.md` §1). Scenario ideas
   without approval do not qualify.
2. An approved acceptance strategy roadmap exists (`ROADMAP-ACCEPTANCE.md`).
3. A dedicated disposable test SUT exists or its production is planned and recorded
   (environment rules in `ATDD-CHECKLIST.md`).
4. Shared DSL utility infrastructure (alias context, parameter helper, driver
   interface) either exists in the codebase or is consciously planned into P1.

## P1 — executable specifications + DSL

**Produce:**

- Layer 1: one executable test per approved scenario, code-based Given/When/Then; each
  scenario's first action establishes its own data partition; each step maps to
  exactly one DSL call.
- Layer 2: DSL matching the scenario vocabulary — parameter objects with defaults, and
  alias translation for every uniqueness-bearing identifier, wired through a fresh
  context per scenario.
- DSL invokes driver operations that are not written yet. The resulting compile/import
  failure is the phase's expected RED state — demonstrate it.

**Demonstrate the failure:** run the specification test and capture the actual output
showing infrastructure absence (missing module/method), then record the state summary:

```
ROUTE acceptance · PHASE P1 · TEST "<scenario name>"
LAST OUTPUT: <actual compile/import failure evidence>
EXIT STATUS: <code>
AWAITING: human review of P1
```

**STOP for human review.** Review focus: DSL reads like the scenario, aliasing on all
identifiers that must be unique, no assertions or state smuggled into the DSL, 1:1
scenario/test and step/call mappings.

An anomaly here (specs execute without a driver) is a review anomaly per the general
stop rules: report it, propose nothing autonomously.

## P2 — driver, assertions, polling, stubs + SUT connection

**Produce:**

- Layer 3 driver implementing the agreed interface, with every assertion; success
  completes normally, failure raises a natural error with context.
- Bounded polling for any asynchronous SUT outcome — deadline plus explicit failure;
  no arbitrary sleeps. Stubs strictly for third parties and nondeterminism
  (`DEPENDENCIES.md`), never owned persistence.
- Connection to the real test SUT through its public interfaces.
- Stubs for third parties only, per strategy roadmap.

**Then demonstrate that the infrastructure executes** — run the specs (in a runner that
inherits the timeout safeguards) and show the outcome capture.

Two nuances that this phase lives or dies on:

- **P2 GREEN means infrastructure executes — not business success.** A run can be
  green-with-infrastructure while business assertions fail; conversely a test-first
  suite still fails business assertions here. Both are correct states and are reported
  truthfully. Test-first and SUT-first development orders are both valid; never
  massage an outcome to make the phase "look finished".
- Any infrastructure error remains a P2 defect: it is reported with real output and
  fixed, within the same review cycle, when the human directs the fix.

**STOP for human review.** Review focus: interface implemented, SUT connected, stubs
within bounds, assertions in the driver, polling bounded, real execution evidence.

## P3 — explicit refinement + isolation proof

**Refine:** evaluate every layer for duplication and clarity; explicitly state when no
change is needed (same standard as `PHASES.md` REFACTOR). Consolidate near-identical
driver methods before finishing a suite and keep scenario/step mapping intact.

**Prove isolation — the validation steps run every time, not once:**

1. Run scenarios **in parallel** — many at working concurrency.
2. Run the **same scenario twice** within the suite.
3. Record the evidence: outputs and exit statuses for both runs, demonstrating no
   cross-worker collisions and deterministic repeat results. On any collision or
   nondeterminism, name it, stop, and await direction.

Also record which business assertions failed along the way — as a separate list from
the infrastructure verdicts, so an SUT under active development is never confused with
a broken test kit.

**STOP for final review**, presenting the isolation evidence and the split lists.

## Incomplete SUT — report blocked, not proven

If the SUT is not yet able to satisfy a scenario's business expectations, phase work
does not end in a claim of success. Report:

```
ROUTE acceptance · PHASE P2 · TEST "<scenario name>"
LAST OUTPUT: infrastructure executed; business assertion failed: <message>
EXIT STATUS: <code>
AWAITING: human review — BLOCKED PROOF: isolation cannot be demonstrated without propagating unverified business behavior
```

Then stop. Never paper over a missing SUT behavior with a test-layer shortcut (extra
memory, weaker assertion, removed step); the gap is on the SUT side, and the human
decides whether to build it (behavioral route) or re-scope the scenario.

After final approval, feature completion is judged by `ATDD-CHECKLIST.md` close-out
rules: passing behavior tests plus recorded manual/visual evidence where applicable —
infrastructure readiness alone is never completion.
