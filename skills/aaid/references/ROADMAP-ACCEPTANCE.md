# AAID Roadmap — Acceptance Strategy

Load during planning of acceptance work — before phase P1 of `ATDD-PHASES.md`. This is
the strategy roadmap for the acceptance suite itself: how the executable tests will
reach the SUT and keep each other from colliding. Without it, acceptance work does not
start (`ATDD-PHASES.md` pre-phase requirement 2).

## The one required document

Every acceptance effort — new suite, or a substantial extension of an existing one —
begins with this roadmap and requires its **explicit human approval**. It complements
rather than replaces the other roadmaps: behavioral features also get their roadmap
(`ROADMAP-DOMAIN.md`), technical elements theirs (`ROADMAP-TECHNICAL.md`).

## Required sections

### 1. System understanding

- The business capability the suite verifies and what "done" means for it — capability
  phrased for stakeholders, not for developers.
- The audience: who consumes the verified system and for what goal.

### 2. Connection strategy

- **Protocol** of the SUT's public interface (HTTP/UI/CLI/messaging) and the tool that
  speaks it, recorded per interface the suite plans to exercise.
- **Entry points** — concrete interfaces the suite will drive (naming entry points is a
  strategy statement, not implementation detail).
- **Authentication approach** — how each scenario establishes and records identity.
- A note on protocol selection mechanism, so the same specifications can later run via
  different drivers without edits.

### 3. Isolation strategy

The heart of the document. Three named isolation levels (`ATDD-CHECKLIST.md` §B):

- **System-level**: which external third parties are stubbed (with justification per
  stub), and the explicit list of owned dependencies that will run **real** — database,
  cache, queues, internal services. Any temptation to stub an owned dependency is
  flagged here and rejected (`DEPENDENCIES.md`).
- **Functional**: the natural per-scenario data boundaries (accounts, tenants,
  workspaces) each scenario creates as its first act, and what stays inside them.
- **Temporal / cross-worker**: which identifiers must be unique across workers and
  repeat runs, and the **collision-safe** alias mechanism. State explicitly why the
  chosen scheme is globally unique even when workers share one database — a bare
  per-worker counter is insufficient and must be named as insufficient if proposed.

### 4. Environment declaration

The dedicated disposable test environment for the SUT, with its own database and
cache — never production and never real business/user data — plus how cleanliness is
achieved (clear **before** the next run, `ATDD-CHECKLIST.md` §B3).

### 5. Ordered scenario outline

The scenarios the suite will encode, as a pending outline ordered from simplest
behavior outward (`ZOMBIES.md` logic applies). WHAT-not-classes throughout: no
predesigned classes, no signature lists, no data models — the four-layer cycle
discovers structure; the roadmap only fixes strategy and order.

## Approval

Propose → human reviews → revise → approval recorded in state, before P1. The review
checks above all the isolation section and the real/stub split, since those are the
costliest mistakes to discover late. Substantive later changes to the strategy (new
stub, changed protocol, changed uniqueness scheme) go back through review.

## Relation to the suite's subsequent phases

Once approved, the strategy roadmap is the reference point for P2 choices (stubs,
polling, connection) and for P3's isolation proof — which must be demonstrable exactly
as this roadmap describes. A gap between roadmap and proof (for example, a uniqueness
scheme that cannot deliver parallel safety) is reported as a blocked proof, not
papered over with a weaker demonstration (`ATDD-CHECKLIST.md` §B4).
