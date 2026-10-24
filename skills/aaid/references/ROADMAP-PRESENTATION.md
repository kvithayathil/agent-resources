# AAID Roadmap — Presentation

Load during planning, before any pure-presentation work starts. Presentation work —
visual styling, layout, animation, audio, haptics, and sensory accessibility properties
— is **not** cycled through RED/GREEN/REFACTOR. It is implemented against explicit,
pre-agreed criteria, then validated. This roadmap exists because "no TDD" must not mean
"no plan, no criteria, no review".

## Route confirmation first

Confirm the classification before using this document (`PHASES.md` §2). Two failure
patterns are common and both are wrong:

- **Forced unit TDD on presentation.** A test asserting a color, spacing, or transition
  value is coupled to appearance mechanics, breaks constantly, and verifies little.
  Pure sensory properties are validated by humans and targeted tooling, not a forced
  unit cycle.
- **Hidden behavior transported as presentation.** Form validation, state management,
  data transformation, or rendering logic driven by data is behavior; it leaves this
  route and goes into the behavioral or technical cycle (`PHASES.md` §2 requires the
  split and its explicit announcement).

When a component mixes both — a styled card whose visibility rule is data-driven —
split the tasks: the visibility rule is behavior; color, spacing, and motion are
presentation.

## Required roadmap sections

### 1. Sensory scope

What is being presented, from the audience's perspective. Reference artifacts rule
here: design specifications, style guides, motion or audio briefs. List what is
explicitly out of scope.

### 2. Explicit validation criteria

Each sensory property gets a criterion stated so a reviewer can judge it. Categories:

- **Manual review criteria** — "matches the archived-state design in the approved
  design file", "no animation exceeds the stated duration".
- **Visual regression criteria** — properties a snapshot or screenshot comparison can
  evidence, with the states to capture.
- **Accessibility criteria** — contrast, readable text alternatives, motion sensitivity
  affordances, and the announcement behaviors that carry information (announcements of
  outcomes are behavior-adjacent; the wording and timing belong in behavioral specs,
  their sensory execution here).
- **Environment criteria** — supported browsers, devices, and reduced-settings modes.

Every criterion must be stated before implementation, not improvised during review.

### 3. Boundaries and dependencies

Existing design system, tokens, and components to reuse; parts of the interface not
to touch. Any supporting technical work (a styling utility with actual logic) is split
out to the technical roadmap.

## Validation and closure

1. Implement against the approved criteria.
2. Evidence what can be evidenced automatically: capture visual-regression results and
   audit reports with the commands and outputs recorded.
3. **Human validation for everything sensory**: humans judge what automated checks
   cannot — the "does this feel right" dimension. Automated passes never substitute
   for this judgment.
4. Refine and repeat until every criterion is either evidenced, human-validated, or
   explicitly deferred by the human.

Completion is recorded as validated criteria plus recorded manual evidence, mirroring
the close-out standard in `CHECKLIST.md`. There are no RED/GREEN phase stops on this
route, but the final review is still a real human review — present the evidence, wait,
and record the outcome.
