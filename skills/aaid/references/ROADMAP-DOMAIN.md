# AAID Roadmap — Domain / Behavioral

Load during planning, **before any behavioral TDD cycle starts**, when a formal roadmap
is appropriate for business-behavior work. A roadmap is a shared alignment document: it
describes what will be built and in which order tests will verify it.

## When a roadmap is needed — and when it is not

- A short, unambiguous TDD request ("add a unit test that empty carts report a zero
  total, then make it pass") may proceed conversationally without a document. Planning
  still happens — as two or three exchanged sentences confirming scope and first test —
  it just produces no artifact.
- Everything larger, ambiguous, multi-scenario, or touching several parts of the system
  gets a formal roadmap and **explicit human approval before any test is written**.
- If the human asks for a roadmap, one is produced even for small requests.
- Acceptance testing is planned differently: `ROADMAP-ACCEPTANCE.md` is the requirement
  there, loaded before acceptance phase 1.

A conversational plan for a small request does not skip the prerequisite gate
(`PHASES.md` §1): approved scenarios and working tooling are still required first.

## What the roadmap contains

Four sections, in this order:

### 1. Scope

Which behavior is in, which is out. Name the user-facing capability in business
language and list any adjacent behaviors deliberately deferred. A scope statement that
includes technical tasks (adapters, persistence, styling) should split them out as
separate linked tasks for the technical or presentation roadmaps — this document covers
behavior only, and keeps behavioral specifications free of technical constraints.

### 2. Boundaries

Which parts of the system the work may touch and which it must respect. Existing
patterns, ports, and seams to build on; places not to change. This is where "the pricing
module stays untouched; the feature uses the existing quote port" is stated, so later
phases can be checked against it.

### 3. Dependencies

What the feature relies on: existing domain services, utilities, data shapes — and,
per `DEPENDENCIES.md`, which external things will be mocked in the unit tests and which
category they fall into. Not a design of new interfaces; a statement of what already
exists that this feature will ride on.

### 4. Ordered test scenarios

The test plan proper: an ordered outline of tests, described **as WHAT, not HOW**.

- Each entry names the behavior in one line ("empty cart reports total of zero",
  "borrowed title appears exactly once").
- Ordered by the ZOMBIES progression (`ZOMBIES.md`, loaded when ordering is decided).
- No class names, no method signatures, no data-structure choices, no prescribed
  architecture. The cycle discovers the design; the roadmap must not pre-empt it.
- State machine / rule tables are acceptable when they capture behavior, not structure.
- A diagram may accompany the outline, kept at the level of flow rather than design.

## What the roadmap must NOT contain

- Predesigned classes, interfaces, or file layouts.
- Concrete data models or schemas.
- Any design decision that no test has forced yet.
- Implementation steps ("first create X, then wire Y").

If a section drifts into any of these, replace it with the behavior-level statement it
was trying to say.

## Approval

The roadmap is proposed, then **the human reviews and approves it**. The review checks
that every approved scenario from the specification is addressed, that the order builds
from simple to complex, and that boundaries respect the existing system. Revisions are
made to the document; approval is re-asked after substantive changes. Implementation of
the first RED test may begin only after approval is recorded in the state summary
(`PHASES.md` §3).

The approved roadmap is an outline, a living document, not a contract for exact scope:
new tests discovered mid-cycle are added through the normal phase reviews. Dropping
planned items is an explicit human decision recorded with the state.
