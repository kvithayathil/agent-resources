# PII Detection Architecture

> **Contract:** BC-2 (PII Detection and Redaction)
> **Module:** `security_layer/pii.py`
> **Sync test:** `tests/test_pii_doc_sync.py`

## Design

PII detection uses a **unified Presidio AnalyzerEngine** pipeline. All entity types — both NLP-detected (PERSON via spaCy) and pattern-matched (regex via custom recognizers) — go through a single `analyze()` call. This gives:

- Unified character offsets
- Consistent confidence scoring
- Built-in deduplication
- Single pipeline to extend

## Recognizer Inventory

Presidio's built-in recognizers handle structured PII where they have language support. Custom `PatternRecognizer` instances supplement for entity types where built-in recognizers are unavailable or don't match the project's patterns (e.g., fake/test CC numbers that fail Luhn checksum).

### Built-in (spaCy NLP)

| Recognizer | Entity | Method |
|:-----------|:-------|:-------|
| SpacyRecognizer | PERSON | Named Entity Recognition via `en_core_web_lg` |

### Custom (Registered at Startup)

| Recognizer Name | Entity | Pattern | Score |
|:----------------|:-------|:--------|:------|
| CustomCreditCardRecognizer | CREDIT_CARD | `\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b` | 0.92 |
| CustomSSNRecognizer | US_SSN | `\b\d{3}-\d{2}-\d{4}\b` | 0.93 |
| CustomEmailRecognizer | EMAIL_ADDRESS | `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}` | 0.95 |
| CustomPhoneRecognizer | PHONE_NUMBER | `(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}` | 0.90 |
| CustomAPIKeyRecognizer | API_KEY | `\bsk-[a-zA-Z0-9]{10,}\b`, `\bghp_[a-zA-Z0-9]{20,}\b` | 0.95 |
| CustomBearerTokenRecognizer | BEARER_TOKEN | `\bBearer\s+[a-zA-Z0-9\-._~+/]+=*` | 0.90 |

## PERSON Entity Filtering

spaCy's NER can produce false positives on short common words (e.g., "Email", "Phone", "SSN"). Two filters suppress these:

1. **Minimum length**: PERSON entities < 6 characters are discarded
2. **Stopword list**: Known PII label words (email, phone, ssn, card, name, key, address, number, token, authorization) are excluded

## Base64 Decoding

Text is decoded through up to 3 layers of base64 before scanning. Decoded entities get offsets in the concatenated search space and are deduplicated by `(entity_type, start, end)` tuple.

## Density Escalation

`check_pii_density()` computes the ratio of unique PII text characters to total text length. If density exceeds the configurable threshold (default 0.7 = 70%), `should_escalate()` returns `True`, triggering human review instead of blanket redaction.

## Pipeline

```
scan_and_redact(text, path, allowlist)
  │
  ├─ path in allowlist? → skip, return original
  │
  ├─ detect_pii(text)
  │   ├─ _analyze(text)          ← Presidio unified pipeline
  │   ├─ _decode_base64_layers   ← up to 3 layers
  │   ├─ _analyze(decoded)       ← scan decoded content
  │   └─ dedup by (type, start, end)
  │
  ├─ redact_pii(text, entities)  ← [REDACTED_{TYPE}] placeholders
  ├─ check_pii_density(text, entities)
  └─ should_escalate(density)
```

## Why Not detect-secrets / Bandit / GLiNER?

| Tool | Rejected Because |
|:-----|:-----------------|
| detect-secrets | File-scanner only, no inline string API, line-level offsets (no char offsets) |
| Bandit | AST-only static analysis, no runtime PII detection capability |
| GLiNER | General-purpose NER (not PII-focused), heavy PyTorch dependency, overkill for person name detection |

## Extending

To add a new entity type:

1. Define a `Pattern` with regex and score
2. Create a `PatternRecognizer` in `_CUSTOM_RECOGNIZERS`
3. Add the entity to `_RECOGNIZER_ENTITIES` and `_ENTITY_TYPE_MAP`
4. Add a test in `tests/test_pii_detection.py`
5. Run `pytest tests/test_pii_doc_sync.py` to verify doc stays in sync
