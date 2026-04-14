# VSDD Lessons — Practical Findings

> Context: Running Verified Spec-Driven Development on LLM Security Mitigation Stack
> Project: agent-resources/security_layer (9 modules, 171 tests)

## Tool Selection

### Evaluating frameworks is a research task, not an implementation task

We spent significant context window investigating presidio vs detect-secrets vs GLiNER vs Bandit. The correct move: research → document decision → implement. Don't interleave research with implementation. The `research/` directory captures decisions so future sessions don't re-investigate.

### "Well-maintained" doesn't mean "right API shape"

detect-secrets (Yelp, 1.5.0, active releases) is excellent at what it does — file scanning for secrets. But it has no inline string API and returns line numbers, not character offsets. A tool being well-maintained and popular doesn't make it suitable for your specific integration point.

### Presidio built-in recognizers reject fake/test data

The built-in CreditCardRecognizer and UsSsnRecognizer validate checksums and format ranges. Test values like `4532-1234-5678-9010` and `123-45-6789` fail validation and produce zero results. Solution: custom PatternRecognizers with relaxed regex patterns registered alongside built-ins.

## Testing

### Density tests need mathematically correct test data

A test asserting "density > 0.7" with data that's only 64% PII will never pass. The test data must genuinely represent the scenario being tested. This seems obvious but was the longest-running blocker — the test was written before the detector existed, with an assumed detection model that didn't match reality.

### Test data correction is spec fidelity, not cheating

VSDD says tests serve spec. Adjusting test data to correctly represent the spec scenario (high PII density) is legitimate. Changing the threshold to make bad data pass would be cheating. The distinction: are you fixing the test's representation of the spec, or weakening the spec's requirement?

### Doc sync tests are cheap and valuable

8 tests that verify docs match code (recognizer names, entity types, thresholds, stopword lists) cost ~200 lines and catch documentation drift immediately. `get_recognizer_info()` in the module provides a programmatic API for the doc sync tests to query.

## Architecture

### `types.py` shadowing stdlib is a recurring pain point

Naming a module `types.py` shadows `import types` (stdlib). When running from inside `security_layer/`, every import chain that touches `enum` → `types` breaks. Workaround: run tests from project root with `conftest.py` adding `security_layer/` to `sys.path`. Proper fix: rename to `domain_types.py` or `security_types.py`.

### Single pipeline > multiple detection paths

The original approach (regex for secrets + presidio for persons + detect-secrets for high-entropy) had three separate detection paths with different offset handling, dedup strategies, and result types. The unified Presidio pipeline (custom recognizers registered into the same AnalyzerEngine) eliminated all those seams. One `analyze()` call, one result type, one offset space.

### Lazy singleton for heavy objects

`AnalyzerEngine()` loads spaCy model (~382MB). Lazy singleton (`_analyzer: AnalyzerEngine | None = None`) avoids reload per test. But it means tests share state — the analyzer registry persists across tests. For most cases this is fine (recognizers are read-only after registration). For tests that modify the registry, use a fixture to reset.

## Process

### Chainlink handoff notes survive context compression

The handoff notes from session 2 accurately described the PII blocker state. Session 3 picked up without re-investigation. Key practice: include decisions made (not just tasks done) in handoff notes. "Bandit evaluated — rejected (AST-only)" saves the next session from re-evaluating Bandit.

### Context window management matters

By session 3, the conversation had consumed significant context. Research-heavy tasks (evaluating 4 tools, testing each API, debugging density math) burn context fast. Delegate research to sub-agents when possible, or do research in dedicated sessions and hand off findings.
