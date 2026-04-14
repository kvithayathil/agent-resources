import base64
import re
import unicodedata

from security_layer.models import (
    ClassificationResult,
    ContentClassification,
    INJECTION_PATTERNS,
)

_HOMOGLYPH_MAP = {
    "\u0456": "i",
    "\u0457": "i",
    "\u0458": "j",
    "\u0459": "s",
    "\u0430": "a",
    "\u0435": "e",
    "\u043e": "o",
    "\u0440": "p",
    "\u0441": "c",
    "\u0443": "y",
    "\u0445": "x",
    "\u0454": "e",
    "\u04bb": "h",
    "\u0269": "i",
}

_TRUSTED_SOURCES = frozenset({"user"})
_UNTRUSTED_SOURCES = frozenset({"web", "api", "external", "scraper", "http"})


def normalize_unicode(text: str) -> str:
    for homoglyph, replacement in _HOMOGLYPH_MAP.items():
        text = text.replace(homoglyph, replacement)
    normalized = unicodedata.normalize("NFC", text)
    return normalized


def _decode_base64_layers(text: str) -> str:
    combined = text
    for _ in range(3):
        try:
            decoded = base64.b64decode(combined, validate=False).decode("utf-8", errors="ignore")
            combined = decoded
        except Exception:
            break
    return combined


def is_injection_pattern(text: str) -> bool:
    normalized = normalize_unicode(text.lower())
    for pattern in INJECTION_PATTERNS:
        if pattern.lower() in normalized:
            return True
    return False


def _score_injection(text: str) -> tuple[float, list[str]]:
    normalized = normalize_unicode(text.lower())
    decoded = _decode_base64_layers(text)
    combined = f"{normalized} {normalize_unicode(decoded.lower())}"
    matched: list[str] = []
    for pattern in INJECTION_PATTERNS:
        if pattern.lower() in combined:
            matched.append(pattern)
    if not matched:
        return 0.0, []
    score = min(1.0, 0.8 + 0.05 * len(matched))
    return score, matched


def classify_content(
    content: str,
    source: str = "user",
    threshold: float = 0.7,
) -> ClassificationResult:
    score, patterns = _score_injection(content)
    if score >= threshold and patterns:
        return ClassificationResult(
            classification=ContentClassification.SUSPECTED_INJECTION,
            score=score,
            patterns_matched=patterns,
        )
    if source in _UNTRUSTED_SOURCES:
        return ClassificationResult(
            classification=ContentClassification.UNTRUSTED_EXTERNAL,
            score=score,
            patterns_matched=patterns,
        )
    return ClassificationResult(
        classification=ContentClassification.TRUSTED,
        score=score,
        patterns_matched=patterns,
    )


_UNTRUSTED_BEGIN = "<!-- UNTRUSTED_CONTENT_BEGIN -->"
_UNTRUSTED_END = "<!-- UNTRUSTED_CONTENT_END -->"


def segregate_untrusted(content: str) -> str:
    return f"{_UNTRUSTED_BEGIN}\n{content}\n{_UNTRUSTED_END}"
