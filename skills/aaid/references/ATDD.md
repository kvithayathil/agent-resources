# AAID Acceptance Testing Reference — Four Layers

Load when entering any acceptance/ATDD work, before `ATDD-PHASES.md`. This file fixes
the architectural model of an acceptance suite and its non-negotiable rules.

## Purpose and shape

An acceptance suite is an executable business specification: every commercially
approved scenario becomes a test that runs the whole system from outside and decides
pass or fail. Three questions define the design discipline:

1. **What does the system do?** — in language a stakeholder can read (layers 1–2).
2. **How do we reach and observe it?** — through its real interfaces (layer 3).
3. **What is actually being tested?** — the running system itself (layer 4).

## The four layers

| Layer | Owns | Never contains |
| --- | --- | --- |
| 1. **Executable specification** | Business language; one approved scenario = one test; Given/When/Then flow | Implementation detail — endpoints, status codes, selectors, table names, explanatory comments |
| 2. **Business DSL** | Domain vocabulary, parameter defaults, alias-translation for isolation, delegation to the driver | Assertions, business logic, remembered assertion/boundary state, I/O, driver choice |
| 3. **Protocol driver (+ third-party stubs)** | All protocol handling and **all assertions**; bounded polling; multi-step flows hidden; stubs for uncontrolled external parties | Business state; boolean verdicts; framework-specific assertion calls |
| 4. **System under test (SUT)** | The production-like running application with real managed dependencies (database, cache, queues, internal services) | Being stubbed — it is the target, not part of the test kit |

Every action flows test → DSL → driver → SUT. Human-readable business intent at the
top; concrete protocol mechanics at the bottom; a strict translation layer between.

## Binding divergence from the upstream BDD plugin

The upstream repository ships an `aaid-bdd` plugin whose model differs from the one
bound for this skill. **The divergence is adopted deliberately here and recorded so it
is not silently "fixed":**

| Concern | This skill (binding, four layers) | Upstream BDD plugin (not adopted) |
| --- | --- | --- |
| Layer count | **Four**: spec, DSL, driver, SUT | **Three** test-infrastructure layers (Gherkin spec, DSL, driver), with SUT as a target rather than a layer |
| Spec format | Executable tests in code; Given/When/Then expressed as test structure and DSL calls | Mandatory `.feature` files in Gherkin plus framework step definitions |
| DSL state | Stateless: no business or remembered state at all | Permits temporary "bridging state" inside the DSL for multi-step scenario sequences |
| Assertions | All in layer 3 | Same — this part is adopted |

Consequences of the binding choice:

- **Gherkin/`.feature` files are NOT mandatory.** A code-based Given/When/Then
  executable spec that maps approved scenarios to DSL calls is fully acceptable. Do not
  require, generate, or demand step-definition infrastructure to satisfy the upstream
  plugin shape.
- **Approved BDD scenarios remain a prerequisite** (design D2): the scenario content is
  the input, whatever representation the executable layer then takes.
- **One scenario → one executable test.** One Given/When/Then step → one DSL call. No
  combined or partial mappings.
- **No DSL bridging state.** Where the upstream plugin would stash scenario-local state
  in the DSL, this skill carries what is needed through DSL parameters and isolation
  context, and computes verification through the driver against the SUT.

## Layer rules in detail

### Layer 1 — executable specification

- Read back the approved scenario verbatim in intent: given, when, then, and each.
- One scenario, one test; name the test by the expected outcome.
- Nothing technical leaks in: no URLs, field names, wait strategies.

### Layer 2 — business DSL

- Method names mirror the scenario wording; parameter objects with defaults keep call
  sites to what the behavior actually needs.
- The DSL holds vocabulary, defaults, and alias translation, and only that. It owns no
  business state, no remembered values to assert on later, does no I/O, and never
  asserts. Its only "memory" is tool-level isolation context (fresh per scenario).
- It depends on the driver **interface**, never a concrete driver, which is what lets
  one specification run unchanged over different protocols.

### Layer 3 — protocol driver and stubs

- One driver per protocol (API/UI/CLI/messaging), all implementing the shared
  interface; the DSL could run a scenario through any of them.
- The driver talks to the SUT only through the interfaces real consumers use — no
  reaching into internals or the database directly.
- **All assertions live here.** Verification is performed by querying the SUT, never by
  trusting anything the test layers remember. On success, the method completes
  normally; on failure it raises its own natural error with a context-bearing message.
- Asynchronous outcomes are awaited via **bounded polling** — retry the SUT query until
  a deadline, then fail explicitly. Arbitrary fixed sleeps are forbidden.
- Stubs are written only for uncontrolled third parties, chosen in planning and
  recorded in the strategy roadmap (`ROADMAP-ACCEPTANCE.md`).

### Layer 4 — SUT

- Deployed like production: the real application with its real owned database, cache,
  and services, in a **dedicated disposable test environment** (see `ATDD-CHECKLIST.md`
  for the environment and isolation rules).
- Transient protocol/session handles may live at the driver; **business state lives
  only in the SUT**, which is the single source of truth.

## Safety rules that bound the whole model

- Verification flows only through layer 3; a suite asserting "directly" on wire formats
  or internals is mis-layered.
- Sut-side behavior gaps are findings, not obstacles to script around: a business
  failure is reported as a business failure (`ATDD-PHASES.md` phase 3).
- Exception-polling loops always have a deadline and a distinguishing error message.
- New scenario ideas surfaced while working go to the human as suggestions — they are
  never silently added to the suite.

Phase-by-phase rules: on entering acceptance work, load `ATDD-PHASES.md`; for the
review checklist, `ATDD-CHECKLIST.md`; for planning prerequisites, `ROADMAP-ACCEPTANCE.md`.
