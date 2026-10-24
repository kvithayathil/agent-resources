# AAID Review Checklist

Load before evaluating any phase review, or when asked to assess test or implementation
quality. This checklist structures the **human** review at each stop; the agent presents
the evidence and must never mark items complete on the human's behalf.

## Evidence standard (applies to every review)

A phase review is decided on **real execution evidence**, never on claims or bookkeeping:

- The exact command that was run (test name or filter included).
- The relevant condensed output: test counts, the failure or assertion message, timing
  where meaningful.
- The exit status of that run.
- Which artifacts changed since the previous review, if any.

Nothing else counts. A checked-off list, a summary sentence like "tests green", a
self-assessment, or a plan promising future verification is not evidence and does not
close a review. If any command output above is missing, the review is incomplete: re-run
and present it rather than describing what the run would have shown.

## RED review

Verification targets, in order:

1. **Smallest expression.** The test covers one behavior — no opportunistic extra
   assertions bundled in "while we're here".
2. **Behavioral naming.** The test name states what the system does from its consumer's
   perspective, free of design vocabulary (class, table, endpoint internals).
3. **Structure.** Arrange/act/assert sections are recognizable, with any mock wiring
   limited to what this behavior needs.
4. **Honest failure.** The recorded run shows failure **for the intended reason** —
   missing behavior, relevant missing import, or compile error. A failure caused by
   unrelated breakage is not a valid RED and must be reported as such.
5. **Speed and isolation.** External dependencies handled per `DEPENDENCIES.md` (loaded
   when mock boundaries are decided); the test runs in milliseconds, not seconds of I/O.
6. **No production code.** Zero implementation was written during this phase.
7. **Design pressure.** The test's would-be API reads like something a consumer of the
   element would want to call. If setup is painful, that is design feedback — raise it
   before approving.

Approve only when 1–7 hold **and** the evidence is real. An unexpected pass is reviewed
as an anomaly (see `PHASES.md` Example B): investigate cause with the human, never
continue autonomously.

## GREEN review

1. **Minimum implementation.** The code added does only what the current test demands.
   Naive or hard-coded responses that the next test will force to generalize are correct
   here; speculative generality is the defect to catch.
2. **Full-suite green.** Evidence shows the current test passing **and** existing tests
   passing. One run, current counts, exit status 0.
3. **Regression honesty.** If any test fails, the review closes with direction (minimal
   fix or revert), not with approval of the phase.
4. **Project conventions.** Structure matches the codebase's existing patterns; imports
   and file placement do not create surprise dependencies.
5. **No dead paths.** No code exists that no test has asked for (including logging,
   guards, and "obvious" edge handling — those arrive later or in REFACTOR when asked).

## REFACTOR review

REFACTOR closes the cycle for the current test. Review:

1. **Evaluation happened.** Even a "no refactoring needed" verdict must be explicit and
   reasoned — silence or an empty diff without the statement is an incomplete phase.
2. **Behavior preserved.** If code moved, evidence shows the full suite still green
   after the change.
3. **Design debt addressed.** Duplication, naming, cohesion, and readability were looked
   at, and any deferred concern was recorded rather than rediscovered later.
4. **Design-changing refactors updated tests deliberately.** Tests follow the current
   design, not a preserved legacy API kept green for its own sake (unless the human
   requested compatibility).
5. **Non-behavioral additions.** If this phase added logging, messages, or performance
   work, they were explicitly requested and are covered by review — this is the only
   phase where such additions may land.
6. **Security and hygiene pass.** No leftover debug output, no secrets, and no new
   attack surface introduced by the change.

## Close-out review (feature-level)

Before declaring any feature complete:

- Every planned test has completed its own RED → GREEN → REFACTOR cycle, or its absence
  is an explicitly accepted human decision.
- The relevant automated behavior tests pass with evidence from the **final** run.
- Any applicable manual verification is recorded with its results (who checked, what was
  observed), not merely noted as "should be fine".
- Pending outline items that were dropped are listed as dropped, not silently forgotten.
- Acceptance work instead follows the completion rules in `ATDD-CHECKLIST.md` (loaded
  when closing an acceptance suite): infrastructure executing is not feature delivery.

## Presentation route (no phases, but still a review)

Presentation work has no RED/GREEN cycle; its implicit review checklist requires the
explicit criteria from `ROADMAP-PRESENTATION.md`, evidence for each criterion that can be
evidenced automatically (visual regression, audit output), and recorded human judgment for
criteria that only people can judge.
