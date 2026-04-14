import base64

from presidio_analyzer import AnalyzerEngine, Pattern, PatternRecognizer

from security_layer.models import PIIEntity

_API_KEY_SK_PATTERN = Pattern(
    name="openai_api_key",
    regex=r"\bsk-[a-zA-Z0-9]{10,}\b",
    score=0.95,
)
_API_KEY_GHP_PATTERN = Pattern(
    name="github_pat",
    regex=r"\bghp_[a-zA-Z0-9]{20,}\b",
    score=0.95,
)
_BEARER_PATTERN = Pattern(
    name="bearer_token",
    regex=r"\bBearer\s+[a-zA-Z0-9\-._~+/]+=*",
    score=0.90,
)
_CREDIT_CARD_PATTERN = Pattern(
    name="credit_card",
    regex=r"\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b",
    score=0.92,
)
_SSN_PATTERN = Pattern(
    name="us_ssn",
    regex=r"\b\d{3}-\d{2}-\d{4}\b",
    score=0.93,
)
_EMAIL_PATTERN = Pattern(
    name="email_address",
    regex=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    score=0.95,
)
_PHONE_PATTERN = Pattern(
    name="phone_number",
    regex=r"(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
    score=0.90,
)

_CUSTOM_RECOGNIZERS = [
    PatternRecognizer(
        supported_entity="CREDIT_CARD",
        patterns=[_CREDIT_CARD_PATTERN],
        name="CustomCreditCardRecognizer",
    ),
    PatternRecognizer(
        supported_entity="US_SSN",
        patterns=[_SSN_PATTERN],
        name="CustomSSNRecognizer",
    ),
    PatternRecognizer(
        supported_entity="EMAIL_ADDRESS",
        patterns=[_EMAIL_PATTERN],
        name="CustomEmailRecognizer",
    ),
    PatternRecognizer(
        supported_entity="PHONE_NUMBER",
        patterns=[_PHONE_PATTERN],
        name="CustomPhoneRecognizer",
    ),
    PatternRecognizer(
        supported_entity="API_KEY",
        patterns=[_API_KEY_SK_PATTERN, _API_KEY_GHP_PATTERN],
        name="CustomAPIKeyRecognizer",
    ),
    PatternRecognizer(
        supported_entity="BEARER_TOKEN",
        patterns=[_BEARER_PATTERN],
        name="CustomBearerTokenRecognizer",
    ),
]

_RECOGNIZER_ENTITIES = frozenset(
    {"PERSON", "CREDIT_CARD", "US_SSN", "EMAIL_ADDRESS", "PHONE_NUMBER", "API_KEY", "BEARER_TOKEN"}
)

_ENTITY_TYPE_MAP: dict[str, str] = {
    "PERSON": "PERSON",
    "CREDIT_CARD": "CREDIT_CARD",
    "US_SSN": "US_SSN",
    "EMAIL_ADDRESS": "EMAIL_ADDRESS",
    "PHONE_NUMBER": "PHONE_NUMBER",
    "API_KEY": "API_KEY",
    "BEARER_TOKEN": "BEARER_TOKEN",
}

_analyzer: AnalyzerEngine | None = None


def _get_analyzer() -> AnalyzerEngine:
    global _analyzer
    if _analyzer is None:
        engine = AnalyzerEngine()
        for recognizer in _CUSTOM_RECOGNIZERS:
            engine.registry.add_recognizer(recognizer)
        _analyzer = engine
    return _analyzer


def _decode_base64_layers(text: str) -> str:
    combined = text
    for _ in range(3):
        try:
            decoded = base64.b64decode(combined, validate=False).decode("utf-8", errors="ignore")
            combined = decoded
        except Exception:
            break
    return combined


_PERSON_MIN_LENGTH = 6

_PERSON_STOPWORDS: frozenset[str] = frozenset(
    {"email", "phone", "ssn", "card", "name", "key", "address", "number", "token", "authorization"}
)


def _analyze(text: str) -> list[PIIEntity]:
    analyzer = _get_analyzer()
    results = analyzer.analyze(text=text, entities=list(_RECOGNIZER_ENTITIES), language="en")
    entities: list[PIIEntity] = []
    for r in results:
        matched_text = text[r.start : r.end]
        entity_type = _ENTITY_TYPE_MAP.get(r.entity_type, r.entity_type)
        if entity_type == "PERSON":
            if len(matched_text) < _PERSON_MIN_LENGTH:
                continue
            if matched_text.lower() in _PERSON_STOPWORDS:
                continue
        entities.append(PIIEntity(entity_type=entity_type, start=r.start, end=r.end, text=matched_text, score=r.score))
    return entities


def detect_pii(text: str) -> list[PIIEntity]:
    entities = _analyze(text)

    decoded = _decode_base64_layers(text)
    if decoded != text:
        decoded_entities = _analyze(decoded)
        for e in decoded_entities:
            entities.append(
                PIIEntity(
                    entity_type=e.entity_type,
                    start=len(text) + 1 + e.start,
                    end=len(text) + 1 + e.end,
                    text=e.text,
                    score=e.score,
                )
            )

    seen: set[tuple[str, int, int]] = set()
    unique: list[PIIEntity] = []
    for e in entities:
        key = (e.entity_type, e.start, e.end)
        if key not in seen:
            seen.add(key)
            unique.append(e)
    return unique


def redact_pii(text: str, entities: list[PIIEntity]) -> str:
    if not entities:
        return text
    original = [e for e in entities if e.start < len(text)]
    if not original:
        return text
    sorted_entities = sorted(original, key=lambda e: e.start, reverse=True)
    result = text
    for entity in sorted_entities:
        placeholder = f"[REDACTED_{entity.entity_type}]"
        if entity.start <= len(result) and entity.end <= len(result):
            result = result[: entity.start] + placeholder + result[entity.end :]
    return result


def check_pii_density(text: str, entities: list[PIIEntity]) -> float:
    if not text:
        return 0.0
    seen_texts: set[str] = set()
    pii_chars = 0
    for e in entities:
        if e.text in seen_texts:
            continue
        seen_texts.add(e.text)
        pii_chars += len(e.text)
    return pii_chars / len(text)


def should_escalate(density: float, threshold: float = 0.7) -> bool:
    return density > threshold


def is_allowlisted_path(path: str, allowlist: list[str]) -> bool:
    return any(path.startswith(allowed) for allowed in allowlist)


def scan_and_redact(
    text: str,
    path: str | None = None,
    allowlist: list[str] | None = None,
) -> tuple[str, list[PIIEntity], bool]:
    if allowlist is not None and path is not None and is_allowlisted_path(path, allowlist):
        return text, [], False
    entities = detect_pii(text)
    if not entities:
        return text, entities, False
    redacted = redact_pii(text, entities)
    density = check_pii_density(text, entities)
    return redacted, entities, should_escalate(density)


def get_recognizer_info() -> list[dict[str, str | list[str]]]:
    analyzer = _get_analyzer()
    recognizers = analyzer.registry.recognizers
    info: list[dict[str, str | list[str]]] = []
    for rec in recognizers:
        supported = [e for e in rec.supported_entities if e in _RECOGNIZER_ENTITIES]
        if supported:
            info.append({"name": rec.name, "entities": supported})
    return info
