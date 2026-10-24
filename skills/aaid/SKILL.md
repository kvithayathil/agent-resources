---
name: "aaid"
description: "Augmented AI Development (AAID): a human-gated, evidence-driven development methodology. What it covers: context and planning from approved behavioral scenarios or technical contracts, incremental RED → GREEN → REFACTOR TDD with a mandatory human review stop after every phase, and four-layer acceptance testing (executable spec → business DSL → protocol driver → production-like SUT). When to use: any development task needing this methodology, including unit TDD, acceptance/ATDD testing, technical contract testing, and presentation validation with explicit criteria."
license: "MIT — see references/ATTRIBUTION.md for the bundled attribution record"
source:
  repo: https://github.com/dawid-dahl-umain/augmented-ai-development
  ref: main
  path: .
metadata:
  version: "1.0.1"
  living: "true"
  self-learning: "true"
  self-updating: "true"
  update-policy: "evolve-on-evidence"
  last-reviewed: "2026-10-24"
tags:
  - development
  - testing
  - tdd
  - methodology
---

# Augmented AI Development (AAID)

Methodology skill: plan from approved scenarios, build incrementally with a test-first
cycle, stop for human review after every phase, and prove everything with real command
output. Detail lives in `references/` — route there deliberately, never load everything
at activation.

## Applicability

Activate when development work needs this methodology: unit TDD, acceptance testing,
technical contracts, or criterion-based presentation work.

Do **not** activate for general architecture discussion or Q&A with no development
task. Sharing context or requesting a plan only is authorization for thinking, never
for writing implementation code.

## Prerequisites (before any route)

- Approved behavioral scenarios or technical contracts exist. Unapproved scenarios are
  not invented; report the gap and ask.
- A working project with a runnable test runner and linter. Scaffolding a new project
  is outside the cycle — do it only as an explicitly requested separate task.
- Existing untested behavior about to change → characterization evidence first.
- Test-list vs single-test preference unknown → ask before the first test.
  (Planning conversation remains optional for a clear small request: there, the
  user's explicit request is the approved work definition; the test-list question
  above is still asked.)
- Missing prerequisites: report what is missing and ask for direction. Proceed no
  further without it.

## Route determination

Classify the behavioral unit before designing tests:

1. **Domain / behavioral** — observable business logic → unit TDD and/or acceptance
   testing.
2. **Technical contract** — non-observable infrastructure (adapters, gateways, cache,
   messaging) → integration/contract tests.
3. **Presentation** — purely sensory output → explicit pre-agreed visual/manual/
   accessibility criteria, not a forced TDD cycle.

Mixed task → split it, announce each subtask's route, and track them as separate
cycles. Ambiguous classification → ask, then record the answer.

## Conversational state summary

Maintain this summary in conversation and refresh it at every gate:

> Route: … | Phase: RED/GREEN/REFACTOR or P1/P2/P3 | Scenario/test: … |
> Pending test list: … | Latest command/output/exit: … | Approval awaited: …

An explicit user phase declaration wins over the standard sequence; otherwise strict
RED → GREEN → REFACTOR order applies. Ambiguous or lost state → ask, never infer
authorization. Elapsed turns do not authorize.

## Hard gates

- **STOP for human review after EVERY phase**, including an explicitly evaluated and
  no-op REFACTOR. Present evidence, then wait.
- **RED**: smallest failing test, run it, verify failure for the expected reason
  (including a relevant missing import/compilation failure). Unexpected pass → STOP
  and report the anomaly; do not invent another test or repair code silently.
- **GREEN**: minimum behavior for the current test only; run current AND existing
  tests. Any regression → report failures and await direction, never cross the gate.
- **REFACTOR**: explicitly evaluate; if no change is worthwhile, say so, rerun
  relevant tests, and STOP for review before the next test.
- Approval requires an explicit human statement. Silence, checked boxes, your own
  review, or a generic future-work plan is never approval; requested approval for a
  later phase approves only that transition.
- Test-list preference is a precondition, not optional planning conversation: if the
  user has not chosen between a pending test list and one single test, ask BEFORE
  writing any test and proceed no further without the answer. A test list is a
  pending outline; implement one test at a time.
- Human overrides are honored within user authorization and host safety, and are
  recorded with their scope.
- **Before writing any test or implementation**: re-check the state summary — the
  prior gate's approval must be recorded in this session. Momentum or existing code
  never substitutes (PHASES.md §6).

## Evidence rules

Every claim of a passing or failing run cites a real command, its real output, and its
real exit status. Checked boxes ask nothing and prove less. No silent repair.

## Reference map

Load only what the current step calls for — the matching phase file and its checklist
before any phase work, never all references at activation.

| Reference | Load when |
| --- | --- |
| [PHASES.md](references/PHASES.md) | Entering any RED/GREEN/REFACTOR phase work — route, prerequisites, gate format |
| [CHECKLIST.md](references/CHECKLIST.md) | Evaluating any phase review or assessing test/implementation quality |
| [ZOMBIES.md](references/ZOMBIES.md) | Ordering tests: feature start, test-list creation, or next-test selection |
| [DEPENDENCIES.md](references/DEPENDENCIES.md) | Choosing a mock/stub boundary in planning, any RED/GREEN, or acceptance stubbing |
| [ROADMAP-DOMAIN.md](references/ROADMAP-DOMAIN.md) | Planning formal roadmaps for behavioral work, before the first TDD cycle |
| [ROADMAP-TECHNICAL.md](references/ROADMAP-TECHNICAL.md) | Planning technical-contract work, before the first contract cycle |
| [ROADMAP-PRESENTATION.md](references/ROADMAP-PRESENTATION.md) | Planning pure-presentation work, before any presentation implementation |
| [ATDD.md](references/ATDD.md) | Entering any acceptance/ATDD work, before ATDD-PHASES.md — fixes the four-layer model |
| [ATDD-PHASES.md](references/ATDD-PHASES.md) | Immediately after ATDD.md, in force for every P1/P2/P3 phase |
| [ATDD-CHECKLIST.md](references/ATDD-CHECKLIST.md) | Reviewing any acceptance phase or reviewing a suite within an acceptance phase |
| [ROADMAP-ACCEPTANCE.md](references/ROADMAP-ACCEPTANCE.md) | Planning acceptance work — required strategy roadmap before P1 |
| [SELF-IMPROVEMENT.md](references/SELF-IMPROVEMENT.md) | Maintaining this skill — evidence capture, promotion, protected rules |
| [SOURCE.md](references/SOURCE.md) | Provenance questions: upstream source, pins, check status |
| [LESSONS_LEARNED.md](references/LESSONS_LEARNED.md) | Learning from real task evidence; check before proposing lesson updates |
| [CHANGELOG.md](references/CHANGELOG.md) | Reviewing or recording version history of this skill |
| [ATTRIBUTION.md](references/ATTRIBUTION.md) | Attribution/licensing questions; the record frontmatter `license` points to |

## Maintenance (compact protocol)

- **Learning**: lessons come only from real task evidence, in `LESSONS_LEARNED.md`
  (date, context, lesson, validations, links). Increment validations only across
  distinct demonstrated tasks; at three or more, promote the general lesson into the
  relevant instruction/reference and preserve the evidence in history.
- **Freshness triggers**: review older than 7 days, an explicit user request, or a
  relevant incident/upstream event → revalidate source before trusting content.
- **Protected rules** — review stops, layer ownership, evidence standard, learning
  protocol — are never weakened by learning. Substantive edits bump the version,
  refresh the review date, and record the change in the changelog.

For the full protocols (evidence format, promotion steps, bounded writes, provenance)
see [SELF-IMPROVEMENT.md](references/SELF-IMPROVEMENT.md),
[SOURCE.md](references/SOURCE.md), [LESSONS_LEARNED.md](references/LESSONS_LEARNED.md),
[CHANGELOG.md](references/CHANGELOG.md), and
[ATTRIBUTION.md](references/ATTRIBUTION.md). Load them for maintenance or attribution
work — not at activation.
