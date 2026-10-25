# AAID Dependencies Reference

Load whenever a mock/stub boundary must be chosen — during planning, during any RED or
GREEN phase, and whenever an acceptance suite's stubbing strategy is decided. The rule
set here is short and strict; it protects the difference between a test that provokes
the real system and one that provokes a costume.

## The boundary rule

**Stub only what you cannot control and what injects unpredictability. Use real
everything you own.**

Stub candidates:

- External third parties with independent lifecycles that you cannot coordinate: public
  SaaS APIs, payment gateways, external communication providers.
- Nondeterminism inside the system: the clock, randomness, and anything else that makes
  repeated test runs disagree for reasons unrelated to your code.

Never stub (in acceptance suites and any test that integrates real I/O — the
boundary these rules protect):

- Your own persistence (database, object store), your own cache, your own queues, and
  your own internal services. These are **owned**; they are part of the system being
  proven, not obstacles to it. Mocking an owned dependency there verifies a fiction:
  the test passes while the integration it should cover does not exist. At unit level,
  owned persistence may be mocked per the matrix below — a behavioral unit test's
  subject is business logic, and unit tests must not touch real I/O.
- Pure in-process logic. It is deterministic and free; replacing it with a fake weakens
  the test for no speed gain.

Impure in-process logic (logging, metrics, in-memory shared state) is judged on
stability and determinism, dependency by dependency; record the choice in the roadmap
(`ROADMAP-TECHNICAL.md` section 3) rather than deciding it silently per test.

## Category matrix by route

| Dependency | Unit (behavioral) | Technical contract | Acceptance |
| --- | --- | --- | --- |
| Owned persistence / cache / queue / service | Mocked — a unit test's subject is business logic | **Real** (integration tests target the adapter with its actual resource) | **Real** — core of the acceptance SUT |
| Governed external (partner, internal service elsewhere) | Mocked | Contract test, toggleable | Mocked, verified separately by contract tests |
| External third party | Mocked | Contract test, toggleable | Mocked |
| Clock / randomness | Stubbed/controlled | Stubbed/controlled | Stubbed only when a scenario depends on time; otherwise a dedicated starting context keeps runs deterministic |
| Pure in-process logic | **Real** | Real | Real |

Two properties follow from this table and are enforced repeatedly:

1. **Acceptance suites never stub owned infrastructure.** If an acceptance scenario
   cannot run against real owned dependencies, that failure is reported and reviewed
   (`ATDD-CHECKLIST.md`), never resolved by swapping in a fake.
2. **Unit tests never touch real I/O.** If a behavioral unit test needs a real database
   or network to pass, the test subject or the classification is wrong — raise it in
   the RED review, do not slowly convert the unit suite into an integration suite.

## Contract-test toggle rule

Contract tests against external systems alternate between two modes: deterministic
mocked interaction during development, and minimal real-API checks before releases to
detect drift in the provider's contract. Real checks prioritize read-only operations
(observe; never mutate remote state), run in a sandbox when one exists, and stay in a
separate suite so their slowness never contaminates fast feedback.

## Legacy and untested code: characterization first

Before any behavior change to code with no existing tests, **characterization evidence
is required**:

1. Write tests that record what the code currently does — including what looks wrong.
2. Run them; the suite must show the current behavior passing as-is.
3. Only then re-enter the normal cycle, changing behavior test by test with the usual
   review stops (`PHASES.md` §4), where a failing characterization test marks the
   intended behavior change.

Changing untested code without this evidence destroys the only record of what the code
actually did. A "temporary" direct edit defeats the whole discipline; the human review
at each stop is where scope creep into surrounding untested code gets caught.

## Speed expectations

The stubbing discipline exists partly for speed: unit tests in milliseconds, technical
tests in a manageable fraction of a second per case, acceptance tests slower but still
couple-of-seconds scale — any outlier above a minute signals a missing isolation or
stubbing decision and is investigated rather than accepted (`CHECKLIST.md` RED item 5).
