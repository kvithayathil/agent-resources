# AAID Roadmap — Technical Contracts

Load during planning, before any technical-contract TDD cycle starts, when work targets
infrastructure: adapters, repositories, controllers, gateways, clients, middleware,
caching, or messaging plumbing. Technical work runs the same RED → GREEN → REFACTOR
cycle as behavioral work (`PHASES.md` §4); only the test strategy differs, and the
roadmap is where that strategy is fixed and approved.

## Scope of this document

One roadmap per infrastructure element. The element is named by the contract it
fulfils for its consumer — "the archive-query adapter", "the outbound notification
gateway" — not by its eventual class name. Behavioral work has its own roadmap
(`ROADMAP-DOMAIN.md`); presentation work follows `ROADMAP-PRESENTATION.md`. If a
request mixes an element with its presentation or with domain logic, split it, as
required by classification (`PHASES.md` §2).

## Required sections

### 1. Contract statement

The behavioral promise from the element's *consumer's* perspective: another developer,
a calling module, or an external system. "Behavior" here means the technical promise —
parsing, formatting, persistence, error translation — because that is still behavior at
this abstraction level. Name what the element must guarantee and what it must never do
("returns a typed failure for malformed input; never writes partial state").

### 2. Boundaries

- The port (consumer-side contract) the adapter implements, if one exists — stated as a
  contract, not a type listing.
- What sits outside the test's scope: the domain above and unrelated infrastructure
  below are not exercised here.
- Single-responsibility check: if a domain test already proves a rule, the technical
  test must not re-prove it; this roadmap names the split.

### 3. Dependencies and test-type decision

For each dependency, classify it (`DEPENDENCIES.md`, loaded when mock boundaries are
chosen) and record the resulting test type:

| Dependency classification | Test approach on this route |
| --- | --- |
| Managed, owned (database, cache, queue) | **Integration tests with the real resource** |
| Governed third party (internal services, partner APIs) | Contract tests, toggleable between mock and real |
| External third party (public SaaS APIs) | Contract tests, consumer-side, mock in development |
| In-process collaborators | Real when pure; mocked when impure and unstable |

This section also records determinism measures (for example a controlled clock) so the
RED phase inherits them without re-litigating.

### 4. Ordered test-validation scenarios

The test plan, as WHAT not HOW: an ordered outline of contract behaviors to verify
("persists the record and returns its identifier", "corrupt cache entries are treated
as misses"), in ZOMBIES order (`ZOMBIES.md`). Each line names the promise, not the
mechanism — "persists with a generated identifier" survives a storage-engine change;
an SQL statement does not belong here.

## Approval

Same rule as every roadmap: proposed, **reviewed and approved by the human**, revised
on request, approval recorded before the first RED test on this element. The review
specifically checks that the real/mock decisions match `DEPENDENCIES.md` categories and
that scenario order accumulates from simple to complex.

## Relationship to acceptance

Infrastructure built here is exercised again, for real, inside the acceptance SUT
(`ATDD.md` layer 4): integration and contract tests prove the element's own contract;
acceptance tests later prove the whole system's business behavior. Neither substitutes
for the other, and infrastructure executing is never acceptance success (see
`ATDD-PHASES.md` phase 2 rules).
