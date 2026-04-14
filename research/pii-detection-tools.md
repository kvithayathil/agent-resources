# PII/Secret Detection Tools for Inline String Analysis

> Researched: 2026-04-14
> Context: BC-2 PII detection — choosing detection stack for `security_layer/pii.py`

## Requirements

Inline string-level PII/secret detection with **character offsets** (not line numbers). Must work on arbitrary Python strings, not files. FOSS only.

## Tool Landscape

### Presidio (Microsoft) — Selected

- **License:** MIT
- **PyPI:** `presidio-analyzer` (2.2.362, released 2026-03-15)
- **Repo:** github.com/microsoft/presidio (7.6k stars, 1.4k commits)
- **Inline API:** Yes — `AnalyzerEngine.analyze(text=..., entities=..., language="en")`
- **Char offsets:** Yes — `RecognizerResult(start, end, entity_type, score)`
- **Extensibility:** Custom `PatternRecognizer` via regex + custom NLP recognizers
- **NLP backend:** spaCy (en_core_web_lg, ~382MB)
- **Built-in recognizers:** ~30+ (CC, SSN, phone, email, IBAN, crypto addresses, medical IDs)
- **Gotchas:**
  - Built-in CC/SSN recognizers require Luhn checksum + valid patterns. Fake/test values (like `4532-1234-5678-9010`) are **rejected**. Solution: register custom `PatternRecognizer` with relaxed regex.
  - spaCy NER produces false positives on short common words ("Email", "Phone" detected as PERSON). Solution: filter by min length + stopword list.
  - Model download is lazy — first `AnalyzerEngine()` call downloads `en_core_web_lg` (~382MB). Subsequent calls reuse cached model.
  - Python 3.13 supported, 3.14 not yet.

### GLiNER (urchade/GLiNER2)

- **License:** Apache-2.0
- **PyPI:** `gliner` (0.2.26, released 2026-03-19)
- **Repo:** github.com/urchade/GLiNER
- **Inline API:** Yes — `GLiNER.predict_entities(text, labels, threshold=0.5)`
- **Char offsets:** Yes
- **Method:** Zero-shot NER via bidirectional transformer encoder
- **Strength:** General-purpose — define any entity label at query time
- **Weakness for PII:** Not PII-specific. Heavy PyTorch dependency (~500MB+ model). Overkill when Presidio already handles PERSON + custom regex handles secrets.
- **Verdict:** Good for general NER. Not the right tool for structured PII detection where patterns are well-defined.

### detect-secrets (Yelp)

- **License:** Apache-2.0
- **PyPI:** `detect-secrets` (1.5.0)
- **Repo:** github.com/Yelp/detect-secrets
- **Inline API:** **No** — file scanner only (`SecretsCollection.scan_file()`)
- **Char offsets:** **No** — line-level only (`secret.line_number`)
- **Strength:** Best-in-class secret detection (high-entropy strings, AWS keys, JWTs, private keys)
- **Weakness for our use case:** No inline string API. Requires writing to temp file, scanning, reading back. No character offsets for redaction.
- **Verdict:** Rejected for inline analysis. Would be useful in a file-scanning CI pipeline (BC-8 security scanning).

### Bandit (PyCQA)

- **License:** Apache-2.0
- **PyPI:** `bandit` (1.9.4)
- **Method:** AST-only static analysis of Python source code
- **Verdict:** Rejected. AST analysis of source != runtime PII detection in arbitrary text. Finds `exec(input())` but not "john@example.com" in a string.

### phonenumbers (daviddrysdale)

- **License:** Apache-2.0
- **PyPI:** `phonenumbers`
- **Strength:** Phone number parsing + validation (libphonenumber port)
- **Verdict:** Useful for phone validation but not general PII detection. Presidio's built-in phone recognizer + custom regex sufficient.

## Decision

**Presidio + custom PatternRecognizers** — single unified pipeline for all 7 entity types. No detect-secrets (wrong API shape). No Bandit (wrong problem). No GLiNER (overkill).

## Pattern for Future PII Tools

When evaluating a PII/secret detection tool for inline string analysis:

1. Does it have an **inline string API** (not file-only)?
2. Does it return **character offsets** (not line numbers)?
3. Can it handle **test/fake data** (not just Luhn-valid CCs)?
4. Is it **extensible** (custom recognizers/patterns)?
5. What's the **cold-start cost** (model download, initialization)?
