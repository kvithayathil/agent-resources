"""Doc sync: ensures docs/pii-detection.md stays accurate vs security_layer/pii.py.

Run: uv run --project security_layer pytest tests/test_pii_doc_sync.py -v
"""

import re
from pathlib import Path

from security_layer.pii import (
    _CUSTOM_RECOGNIZERS,
    _ENTITY_TYPE_MAP,
    _PERSON_MIN_LENGTH,
    _PERSON_STOPWORDS,
    _RECOGNIZER_ENTITIES,
    get_recognizer_info,
)

DOC_PATH = str(Path(__file__).resolve().parent.parent / "docs" / "pii-detection.md")


def _read_doc() -> str:
    with open(DOC_PATH) as f:
        return f.read()


class TestDocSyncRecognizerTable:
    """Custom recognizer table in docs matches _CUSTOM_RECOGNIZERS in code."""

    def test_all_custom_recognizers_documented(self):
        doc = _read_doc()
        for rec in _CUSTOM_RECOGNIZERS:
            assert rec.name in doc, f"Recognizer '{rec.name}' not in docs"

    def test_documented_custom_recognizers_exist_in_code(self):
        doc = _read_doc()
        code_names = {rec.name for rec in _CUSTOM_RECOGNIZERS}
        table_section = doc[doc.find("Custom (Registered") : doc.find("## PERSON")]
        for match in re.finditer(
            r"\| (`Custom\w+Recognizer`|Custom\w+Recognizer) \|", table_section
        ):
            name = match.group(1).strip("`")
            assert name in code_names, f"Doc mentions recognizer '{name}' not in code"

    def test_entity_types_match(self):
        doc = _read_doc()
        for entity in _RECOGNIZER_ENTITIES:
            assert entity in doc, f"Entity type '{entity}' not in docs"

    def test_entity_type_map_complete(self):
        assert set(_ENTITY_TYPE_MAP.keys()) == _RECOGNIZER_ENTITIES


class TestDocSyncPersonFilter:
    """PERSON filter params in docs match code constants."""

    def test_min_length_documented(self):
        doc = _read_doc()
        assert str(_PERSON_MIN_LENGTH) in doc, (
            f"PERSON min length {_PERSON_MIN_LENGTH} not in docs"
        )

    def test_stopword_count_consistent(self):
        doc = _read_doc()
        doc_stopwords = re.findall(
            r"(?:email|phone|ssn|card|name|key|address|number|token|authorization)",
            doc.lower(),
        )
        assert len(doc_stopwords) >= len(_PERSON_STOPWORDS), (
            "Doc stopword list doesn't cover code stopwords"
        )


class TestDocSyncDensityThreshold:
    """Density threshold in docs matches code default."""

    def test_default_threshold_documented(self):
        doc = _read_doc()
        assert "0.7" in doc
        assert "70%" in doc


class TestDocSyncRecognizerInfo:
    """get_recognizer_info() returns all custom recognizers."""

    def test_info_includes_all_custom(self):
        info = get_recognizer_info()
        info_names = {r["name"] for r in info}
        for rec in _CUSTOM_RECOGNIZERS:
            assert rec.name in info_names, f"get_recognizer_info() missing '{rec.name}'"
