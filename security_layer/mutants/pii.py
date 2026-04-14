import base64
import re

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
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def _get_analyzer() -> AnalyzerEngine:
    args = []# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x__get_analyzer__mutmut_orig, x__get_analyzer__mutmut_mutants, args, kwargs, None)


def x__get_analyzer__mutmut_orig() -> AnalyzerEngine:
    global _analyzer
    if _analyzer is None:
        engine = AnalyzerEngine()
        for recognizer in _CUSTOM_RECOGNIZERS:
            engine.registry.add_recognizer(recognizer)
        _analyzer = engine
    return _analyzer


def x__get_analyzer__mutmut_1() -> AnalyzerEngine:
    global _analyzer
    if _analyzer is not None:
        engine = AnalyzerEngine()
        for recognizer in _CUSTOM_RECOGNIZERS:
            engine.registry.add_recognizer(recognizer)
        _analyzer = engine
    return _analyzer


def x__get_analyzer__mutmut_2() -> AnalyzerEngine:
    global _analyzer
    if _analyzer is None:
        engine = None
        for recognizer in _CUSTOM_RECOGNIZERS:
            engine.registry.add_recognizer(recognizer)
        _analyzer = engine
    return _analyzer


def x__get_analyzer__mutmut_3() -> AnalyzerEngine:
    global _analyzer
    if _analyzer is None:
        engine = AnalyzerEngine()
        for recognizer in _CUSTOM_RECOGNIZERS:
            engine.registry.add_recognizer(None)
        _analyzer = engine
    return _analyzer


def x__get_analyzer__mutmut_4() -> AnalyzerEngine:
    global _analyzer
    if _analyzer is None:
        engine = AnalyzerEngine()
        for recognizer in _CUSTOM_RECOGNIZERS:
            engine.registry.add_recognizer(recognizer)
        _analyzer = None
    return _analyzer

x__get_analyzer__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x__get_analyzer__mutmut_1': x__get_analyzer__mutmut_1, 
    'x__get_analyzer__mutmut_2': x__get_analyzer__mutmut_2, 
    'x__get_analyzer__mutmut_3': x__get_analyzer__mutmut_3, 
    'x__get_analyzer__mutmut_4': x__get_analyzer__mutmut_4
}
x__get_analyzer__mutmut_orig.__name__ = 'x__get_analyzer'


def _decode_base64_layers(text: str) -> str:
    args = [text]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x__decode_base64_layers__mutmut_orig, x__decode_base64_layers__mutmut_mutants, args, kwargs, None)


def x__decode_base64_layers__mutmut_orig(text: str) -> str:
    combined = text
    for _ in range(3):
        try:
            decoded = base64.b64decode(combined, validate=False).decode("utf-8", errors="ignore")
            combined = decoded
        except Exception:
            break
    return combined


def x__decode_base64_layers__mutmut_1(text: str) -> str:
    combined = None
    for _ in range(3):
        try:
            decoded = base64.b64decode(combined, validate=False).decode("utf-8", errors="ignore")
            combined = decoded
        except Exception:
            break
    return combined


def x__decode_base64_layers__mutmut_2(text: str) -> str:
    combined = text
    for _ in range(None):
        try:
            decoded = base64.b64decode(combined, validate=False).decode("utf-8", errors="ignore")
            combined = decoded
        except Exception:
            break
    return combined


def x__decode_base64_layers__mutmut_3(text: str) -> str:
    combined = text
    for _ in range(4):
        try:
            decoded = base64.b64decode(combined, validate=False).decode("utf-8", errors="ignore")
            combined = decoded
        except Exception:
            break
    return combined


def x__decode_base64_layers__mutmut_4(text: str) -> str:
    combined = text
    for _ in range(3):
        try:
            decoded = None
            combined = decoded
        except Exception:
            break
    return combined


def x__decode_base64_layers__mutmut_5(text: str) -> str:
    combined = text
    for _ in range(3):
        try:
            decoded = base64.b64decode(combined, validate=False).decode(None, errors="ignore")
            combined = decoded
        except Exception:
            break
    return combined


def x__decode_base64_layers__mutmut_6(text: str) -> str:
    combined = text
    for _ in range(3):
        try:
            decoded = base64.b64decode(combined, validate=False).decode("utf-8", errors=None)
            combined = decoded
        except Exception:
            break
    return combined


def x__decode_base64_layers__mutmut_7(text: str) -> str:
    combined = text
    for _ in range(3):
        try:
            decoded = base64.b64decode(combined, validate=False).decode(errors="ignore")
            combined = decoded
        except Exception:
            break
    return combined


def x__decode_base64_layers__mutmut_8(text: str) -> str:
    combined = text
    for _ in range(3):
        try:
            decoded = base64.b64decode(combined, validate=False).decode("utf-8", )
            combined = decoded
        except Exception:
            break
    return combined


def x__decode_base64_layers__mutmut_9(text: str) -> str:
    combined = text
    for _ in range(3):
        try:
            decoded = base64.b64decode(None, validate=False).decode("utf-8", errors="ignore")
            combined = decoded
        except Exception:
            break
    return combined


def x__decode_base64_layers__mutmut_10(text: str) -> str:
    combined = text
    for _ in range(3):
        try:
            decoded = base64.b64decode(combined, validate=None).decode("utf-8", errors="ignore")
            combined = decoded
        except Exception:
            break
    return combined


def x__decode_base64_layers__mutmut_11(text: str) -> str:
    combined = text
    for _ in range(3):
        try:
            decoded = base64.b64decode(validate=False).decode("utf-8", errors="ignore")
            combined = decoded
        except Exception:
            break
    return combined


def x__decode_base64_layers__mutmut_12(text: str) -> str:
    combined = text
    for _ in range(3):
        try:
            decoded = base64.b64decode(combined, ).decode("utf-8", errors="ignore")
            combined = decoded
        except Exception:
            break
    return combined


def x__decode_base64_layers__mutmut_13(text: str) -> str:
    combined = text
    for _ in range(3):
        try:
            decoded = base64.b64decode(combined, validate=True).decode("utf-8", errors="ignore")
            combined = decoded
        except Exception:
            break
    return combined


def x__decode_base64_layers__mutmut_14(text: str) -> str:
    combined = text
    for _ in range(3):
        try:
            decoded = base64.b64decode(combined, validate=False).decode("XXutf-8XX", errors="ignore")
            combined = decoded
        except Exception:
            break
    return combined


def x__decode_base64_layers__mutmut_15(text: str) -> str:
    combined = text
    for _ in range(3):
        try:
            decoded = base64.b64decode(combined, validate=False).decode("UTF-8", errors="ignore")
            combined = decoded
        except Exception:
            break
    return combined


def x__decode_base64_layers__mutmut_16(text: str) -> str:
    combined = text
    for _ in range(3):
        try:
            decoded = base64.b64decode(combined, validate=False).decode("utf-8", errors="XXignoreXX")
            combined = decoded
        except Exception:
            break
    return combined


def x__decode_base64_layers__mutmut_17(text: str) -> str:
    combined = text
    for _ in range(3):
        try:
            decoded = base64.b64decode(combined, validate=False).decode("utf-8", errors="IGNORE")
            combined = decoded
        except Exception:
            break
    return combined


def x__decode_base64_layers__mutmut_18(text: str) -> str:
    combined = text
    for _ in range(3):
        try:
            decoded = base64.b64decode(combined, validate=False).decode("utf-8", errors="ignore")
            combined = None
        except Exception:
            break
    return combined


def x__decode_base64_layers__mutmut_19(text: str) -> str:
    combined = text
    for _ in range(3):
        try:
            decoded = base64.b64decode(combined, validate=False).decode("utf-8", errors="ignore")
            combined = decoded
        except Exception:
            return
    return combined

x__decode_base64_layers__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x__decode_base64_layers__mutmut_1': x__decode_base64_layers__mutmut_1, 
    'x__decode_base64_layers__mutmut_2': x__decode_base64_layers__mutmut_2, 
    'x__decode_base64_layers__mutmut_3': x__decode_base64_layers__mutmut_3, 
    'x__decode_base64_layers__mutmut_4': x__decode_base64_layers__mutmut_4, 
    'x__decode_base64_layers__mutmut_5': x__decode_base64_layers__mutmut_5, 
    'x__decode_base64_layers__mutmut_6': x__decode_base64_layers__mutmut_6, 
    'x__decode_base64_layers__mutmut_7': x__decode_base64_layers__mutmut_7, 
    'x__decode_base64_layers__mutmut_8': x__decode_base64_layers__mutmut_8, 
    'x__decode_base64_layers__mutmut_9': x__decode_base64_layers__mutmut_9, 
    'x__decode_base64_layers__mutmut_10': x__decode_base64_layers__mutmut_10, 
    'x__decode_base64_layers__mutmut_11': x__decode_base64_layers__mutmut_11, 
    'x__decode_base64_layers__mutmut_12': x__decode_base64_layers__mutmut_12, 
    'x__decode_base64_layers__mutmut_13': x__decode_base64_layers__mutmut_13, 
    'x__decode_base64_layers__mutmut_14': x__decode_base64_layers__mutmut_14, 
    'x__decode_base64_layers__mutmut_15': x__decode_base64_layers__mutmut_15, 
    'x__decode_base64_layers__mutmut_16': x__decode_base64_layers__mutmut_16, 
    'x__decode_base64_layers__mutmut_17': x__decode_base64_layers__mutmut_17, 
    'x__decode_base64_layers__mutmut_18': x__decode_base64_layers__mutmut_18, 
    'x__decode_base64_layers__mutmut_19': x__decode_base64_layers__mutmut_19
}
x__decode_base64_layers__mutmut_orig.__name__ = 'x__decode_base64_layers'


_PERSON_MIN_LENGTH = 6

_PERSON_STOPWORDS: frozenset[str] = frozenset(
    {"email", "phone", "ssn", "card", "name", "key", "address", "number", "token", "authorization"}
)


def _analyze(text: str) -> list[PIIEntity]:
    args = [text]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x__analyze__mutmut_orig, x__analyze__mutmut_mutants, args, kwargs, None)


def x__analyze__mutmut_orig(text: str) -> list[PIIEntity]:
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


def x__analyze__mutmut_1(text: str) -> list[PIIEntity]:
    analyzer = None
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


def x__analyze__mutmut_2(text: str) -> list[PIIEntity]:
    analyzer = _get_analyzer()
    results = None
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


def x__analyze__mutmut_3(text: str) -> list[PIIEntity]:
    analyzer = _get_analyzer()
    results = analyzer.analyze(text=None, entities=list(_RECOGNIZER_ENTITIES), language="en")
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


def x__analyze__mutmut_4(text: str) -> list[PIIEntity]:
    analyzer = _get_analyzer()
    results = analyzer.analyze(text=text, entities=None, language="en")
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


def x__analyze__mutmut_5(text: str) -> list[PIIEntity]:
    analyzer = _get_analyzer()
    results = analyzer.analyze(text=text, entities=list(_RECOGNIZER_ENTITIES), language=None)
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


def x__analyze__mutmut_6(text: str) -> list[PIIEntity]:
    analyzer = _get_analyzer()
    results = analyzer.analyze(entities=list(_RECOGNIZER_ENTITIES), language="en")
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


def x__analyze__mutmut_7(text: str) -> list[PIIEntity]:
    analyzer = _get_analyzer()
    results = analyzer.analyze(text=text, language="en")
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


def x__analyze__mutmut_8(text: str) -> list[PIIEntity]:
    analyzer = _get_analyzer()
    results = analyzer.analyze(text=text, entities=list(_RECOGNIZER_ENTITIES), )
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


def x__analyze__mutmut_9(text: str) -> list[PIIEntity]:
    analyzer = _get_analyzer()
    results = analyzer.analyze(text=text, entities=list(None), language="en")
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


def x__analyze__mutmut_10(text: str) -> list[PIIEntity]:
    analyzer = _get_analyzer()
    results = analyzer.analyze(text=text, entities=list(_RECOGNIZER_ENTITIES), language="XXenXX")
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


def x__analyze__mutmut_11(text: str) -> list[PIIEntity]:
    analyzer = _get_analyzer()
    results = analyzer.analyze(text=text, entities=list(_RECOGNIZER_ENTITIES), language="EN")
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


def x__analyze__mutmut_12(text: str) -> list[PIIEntity]:
    analyzer = _get_analyzer()
    results = analyzer.analyze(text=text, entities=list(_RECOGNIZER_ENTITIES), language="en")
    entities: list[PIIEntity] = None
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


def x__analyze__mutmut_13(text: str) -> list[PIIEntity]:
    analyzer = _get_analyzer()
    results = analyzer.analyze(text=text, entities=list(_RECOGNIZER_ENTITIES), language="en")
    entities: list[PIIEntity] = []
    for r in results:
        matched_text = None
        entity_type = _ENTITY_TYPE_MAP.get(r.entity_type, r.entity_type)
        if entity_type == "PERSON":
            if len(matched_text) < _PERSON_MIN_LENGTH:
                continue
            if matched_text.lower() in _PERSON_STOPWORDS:
                continue
        entities.append(PIIEntity(entity_type=entity_type, start=r.start, end=r.end, text=matched_text, score=r.score))
    return entities


def x__analyze__mutmut_14(text: str) -> list[PIIEntity]:
    analyzer = _get_analyzer()
    results = analyzer.analyze(text=text, entities=list(_RECOGNIZER_ENTITIES), language="en")
    entities: list[PIIEntity] = []
    for r in results:
        matched_text = text[r.start : r.end]
        entity_type = None
        if entity_type == "PERSON":
            if len(matched_text) < _PERSON_MIN_LENGTH:
                continue
            if matched_text.lower() in _PERSON_STOPWORDS:
                continue
        entities.append(PIIEntity(entity_type=entity_type, start=r.start, end=r.end, text=matched_text, score=r.score))
    return entities


def x__analyze__mutmut_15(text: str) -> list[PIIEntity]:
    analyzer = _get_analyzer()
    results = analyzer.analyze(text=text, entities=list(_RECOGNIZER_ENTITIES), language="en")
    entities: list[PIIEntity] = []
    for r in results:
        matched_text = text[r.start : r.end]
        entity_type = _ENTITY_TYPE_MAP.get(None, r.entity_type)
        if entity_type == "PERSON":
            if len(matched_text) < _PERSON_MIN_LENGTH:
                continue
            if matched_text.lower() in _PERSON_STOPWORDS:
                continue
        entities.append(PIIEntity(entity_type=entity_type, start=r.start, end=r.end, text=matched_text, score=r.score))
    return entities


def x__analyze__mutmut_16(text: str) -> list[PIIEntity]:
    analyzer = _get_analyzer()
    results = analyzer.analyze(text=text, entities=list(_RECOGNIZER_ENTITIES), language="en")
    entities: list[PIIEntity] = []
    for r in results:
        matched_text = text[r.start : r.end]
        entity_type = _ENTITY_TYPE_MAP.get(r.entity_type, None)
        if entity_type == "PERSON":
            if len(matched_text) < _PERSON_MIN_LENGTH:
                continue
            if matched_text.lower() in _PERSON_STOPWORDS:
                continue
        entities.append(PIIEntity(entity_type=entity_type, start=r.start, end=r.end, text=matched_text, score=r.score))
    return entities


def x__analyze__mutmut_17(text: str) -> list[PIIEntity]:
    analyzer = _get_analyzer()
    results = analyzer.analyze(text=text, entities=list(_RECOGNIZER_ENTITIES), language="en")
    entities: list[PIIEntity] = []
    for r in results:
        matched_text = text[r.start : r.end]
        entity_type = _ENTITY_TYPE_MAP.get(r.entity_type)
        if entity_type == "PERSON":
            if len(matched_text) < _PERSON_MIN_LENGTH:
                continue
            if matched_text.lower() in _PERSON_STOPWORDS:
                continue
        entities.append(PIIEntity(entity_type=entity_type, start=r.start, end=r.end, text=matched_text, score=r.score))
    return entities


def x__analyze__mutmut_18(text: str) -> list[PIIEntity]:
    analyzer = _get_analyzer()
    results = analyzer.analyze(text=text, entities=list(_RECOGNIZER_ENTITIES), language="en")
    entities: list[PIIEntity] = []
    for r in results:
        matched_text = text[r.start : r.end]
        entity_type = _ENTITY_TYPE_MAP.get(r.entity_type, )
        if entity_type == "PERSON":
            if len(matched_text) < _PERSON_MIN_LENGTH:
                continue
            if matched_text.lower() in _PERSON_STOPWORDS:
                continue
        entities.append(PIIEntity(entity_type=entity_type, start=r.start, end=r.end, text=matched_text, score=r.score))
    return entities


def x__analyze__mutmut_19(text: str) -> list[PIIEntity]:
    analyzer = _get_analyzer()
    results = analyzer.analyze(text=text, entities=list(_RECOGNIZER_ENTITIES), language="en")
    entities: list[PIIEntity] = []
    for r in results:
        matched_text = text[r.start : r.end]
        entity_type = _ENTITY_TYPE_MAP.get(r.entity_type, r.entity_type)
        if entity_type != "PERSON":
            if len(matched_text) < _PERSON_MIN_LENGTH:
                continue
            if matched_text.lower() in _PERSON_STOPWORDS:
                continue
        entities.append(PIIEntity(entity_type=entity_type, start=r.start, end=r.end, text=matched_text, score=r.score))
    return entities


def x__analyze__mutmut_20(text: str) -> list[PIIEntity]:
    analyzer = _get_analyzer()
    results = analyzer.analyze(text=text, entities=list(_RECOGNIZER_ENTITIES), language="en")
    entities: list[PIIEntity] = []
    for r in results:
        matched_text = text[r.start : r.end]
        entity_type = _ENTITY_TYPE_MAP.get(r.entity_type, r.entity_type)
        if entity_type == "XXPERSONXX":
            if len(matched_text) < _PERSON_MIN_LENGTH:
                continue
            if matched_text.lower() in _PERSON_STOPWORDS:
                continue
        entities.append(PIIEntity(entity_type=entity_type, start=r.start, end=r.end, text=matched_text, score=r.score))
    return entities


def x__analyze__mutmut_21(text: str) -> list[PIIEntity]:
    analyzer = _get_analyzer()
    results = analyzer.analyze(text=text, entities=list(_RECOGNIZER_ENTITIES), language="en")
    entities: list[PIIEntity] = []
    for r in results:
        matched_text = text[r.start : r.end]
        entity_type = _ENTITY_TYPE_MAP.get(r.entity_type, r.entity_type)
        if entity_type == "person":
            if len(matched_text) < _PERSON_MIN_LENGTH:
                continue
            if matched_text.lower() in _PERSON_STOPWORDS:
                continue
        entities.append(PIIEntity(entity_type=entity_type, start=r.start, end=r.end, text=matched_text, score=r.score))
    return entities


def x__analyze__mutmut_22(text: str) -> list[PIIEntity]:
    analyzer = _get_analyzer()
    results = analyzer.analyze(text=text, entities=list(_RECOGNIZER_ENTITIES), language="en")
    entities: list[PIIEntity] = []
    for r in results:
        matched_text = text[r.start : r.end]
        entity_type = _ENTITY_TYPE_MAP.get(r.entity_type, r.entity_type)
        if entity_type == "PERSON":
            if len(matched_text) <= _PERSON_MIN_LENGTH:
                continue
            if matched_text.lower() in _PERSON_STOPWORDS:
                continue
        entities.append(PIIEntity(entity_type=entity_type, start=r.start, end=r.end, text=matched_text, score=r.score))
    return entities


def x__analyze__mutmut_23(text: str) -> list[PIIEntity]:
    analyzer = _get_analyzer()
    results = analyzer.analyze(text=text, entities=list(_RECOGNIZER_ENTITIES), language="en")
    entities: list[PIIEntity] = []
    for r in results:
        matched_text = text[r.start : r.end]
        entity_type = _ENTITY_TYPE_MAP.get(r.entity_type, r.entity_type)
        if entity_type == "PERSON":
            if len(matched_text) < _PERSON_MIN_LENGTH:
                break
            if matched_text.lower() in _PERSON_STOPWORDS:
                continue
        entities.append(PIIEntity(entity_type=entity_type, start=r.start, end=r.end, text=matched_text, score=r.score))
    return entities


def x__analyze__mutmut_24(text: str) -> list[PIIEntity]:
    analyzer = _get_analyzer()
    results = analyzer.analyze(text=text, entities=list(_RECOGNIZER_ENTITIES), language="en")
    entities: list[PIIEntity] = []
    for r in results:
        matched_text = text[r.start : r.end]
        entity_type = _ENTITY_TYPE_MAP.get(r.entity_type, r.entity_type)
        if entity_type == "PERSON":
            if len(matched_text) < _PERSON_MIN_LENGTH:
                continue
            if matched_text.upper() in _PERSON_STOPWORDS:
                continue
        entities.append(PIIEntity(entity_type=entity_type, start=r.start, end=r.end, text=matched_text, score=r.score))
    return entities


def x__analyze__mutmut_25(text: str) -> list[PIIEntity]:
    analyzer = _get_analyzer()
    results = analyzer.analyze(text=text, entities=list(_RECOGNIZER_ENTITIES), language="en")
    entities: list[PIIEntity] = []
    for r in results:
        matched_text = text[r.start : r.end]
        entity_type = _ENTITY_TYPE_MAP.get(r.entity_type, r.entity_type)
        if entity_type == "PERSON":
            if len(matched_text) < _PERSON_MIN_LENGTH:
                continue
            if matched_text.lower() not in _PERSON_STOPWORDS:
                continue
        entities.append(PIIEntity(entity_type=entity_type, start=r.start, end=r.end, text=matched_text, score=r.score))
    return entities


def x__analyze__mutmut_26(text: str) -> list[PIIEntity]:
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
                break
        entities.append(PIIEntity(entity_type=entity_type, start=r.start, end=r.end, text=matched_text, score=r.score))
    return entities


def x__analyze__mutmut_27(text: str) -> list[PIIEntity]:
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
        entities.append(None)
    return entities


def x__analyze__mutmut_28(text: str) -> list[PIIEntity]:
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
        entities.append(PIIEntity(entity_type=None, start=r.start, end=r.end, text=matched_text, score=r.score))
    return entities


def x__analyze__mutmut_29(text: str) -> list[PIIEntity]:
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
        entities.append(PIIEntity(entity_type=entity_type, start=None, end=r.end, text=matched_text, score=r.score))
    return entities


def x__analyze__mutmut_30(text: str) -> list[PIIEntity]:
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
        entities.append(PIIEntity(entity_type=entity_type, start=r.start, end=None, text=matched_text, score=r.score))
    return entities


def x__analyze__mutmut_31(text: str) -> list[PIIEntity]:
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
        entities.append(PIIEntity(entity_type=entity_type, start=r.start, end=r.end, text=None, score=r.score))
    return entities


def x__analyze__mutmut_32(text: str) -> list[PIIEntity]:
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
        entities.append(PIIEntity(entity_type=entity_type, start=r.start, end=r.end, text=matched_text, score=None))
    return entities


def x__analyze__mutmut_33(text: str) -> list[PIIEntity]:
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
        entities.append(PIIEntity(start=r.start, end=r.end, text=matched_text, score=r.score))
    return entities


def x__analyze__mutmut_34(text: str) -> list[PIIEntity]:
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
        entities.append(PIIEntity(entity_type=entity_type, end=r.end, text=matched_text, score=r.score))
    return entities


def x__analyze__mutmut_35(text: str) -> list[PIIEntity]:
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
        entities.append(PIIEntity(entity_type=entity_type, start=r.start, text=matched_text, score=r.score))
    return entities


def x__analyze__mutmut_36(text: str) -> list[PIIEntity]:
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
        entities.append(PIIEntity(entity_type=entity_type, start=r.start, end=r.end, score=r.score))
    return entities


def x__analyze__mutmut_37(text: str) -> list[PIIEntity]:
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
        entities.append(PIIEntity(entity_type=entity_type, start=r.start, end=r.end, text=matched_text, ))
    return entities

x__analyze__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x__analyze__mutmut_1': x__analyze__mutmut_1, 
    'x__analyze__mutmut_2': x__analyze__mutmut_2, 
    'x__analyze__mutmut_3': x__analyze__mutmut_3, 
    'x__analyze__mutmut_4': x__analyze__mutmut_4, 
    'x__analyze__mutmut_5': x__analyze__mutmut_5, 
    'x__analyze__mutmut_6': x__analyze__mutmut_6, 
    'x__analyze__mutmut_7': x__analyze__mutmut_7, 
    'x__analyze__mutmut_8': x__analyze__mutmut_8, 
    'x__analyze__mutmut_9': x__analyze__mutmut_9, 
    'x__analyze__mutmut_10': x__analyze__mutmut_10, 
    'x__analyze__mutmut_11': x__analyze__mutmut_11, 
    'x__analyze__mutmut_12': x__analyze__mutmut_12, 
    'x__analyze__mutmut_13': x__analyze__mutmut_13, 
    'x__analyze__mutmut_14': x__analyze__mutmut_14, 
    'x__analyze__mutmut_15': x__analyze__mutmut_15, 
    'x__analyze__mutmut_16': x__analyze__mutmut_16, 
    'x__analyze__mutmut_17': x__analyze__mutmut_17, 
    'x__analyze__mutmut_18': x__analyze__mutmut_18, 
    'x__analyze__mutmut_19': x__analyze__mutmut_19, 
    'x__analyze__mutmut_20': x__analyze__mutmut_20, 
    'x__analyze__mutmut_21': x__analyze__mutmut_21, 
    'x__analyze__mutmut_22': x__analyze__mutmut_22, 
    'x__analyze__mutmut_23': x__analyze__mutmut_23, 
    'x__analyze__mutmut_24': x__analyze__mutmut_24, 
    'x__analyze__mutmut_25': x__analyze__mutmut_25, 
    'x__analyze__mutmut_26': x__analyze__mutmut_26, 
    'x__analyze__mutmut_27': x__analyze__mutmut_27, 
    'x__analyze__mutmut_28': x__analyze__mutmut_28, 
    'x__analyze__mutmut_29': x__analyze__mutmut_29, 
    'x__analyze__mutmut_30': x__analyze__mutmut_30, 
    'x__analyze__mutmut_31': x__analyze__mutmut_31, 
    'x__analyze__mutmut_32': x__analyze__mutmut_32, 
    'x__analyze__mutmut_33': x__analyze__mutmut_33, 
    'x__analyze__mutmut_34': x__analyze__mutmut_34, 
    'x__analyze__mutmut_35': x__analyze__mutmut_35, 
    'x__analyze__mutmut_36': x__analyze__mutmut_36, 
    'x__analyze__mutmut_37': x__analyze__mutmut_37
}
x__analyze__mutmut_orig.__name__ = 'x__analyze'


def detect_pii(text: str) -> list[PIIEntity]:
    args = [text]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_detect_pii__mutmut_orig, x_detect_pii__mutmut_mutants, args, kwargs, None)


def x_detect_pii__mutmut_orig(text: str) -> list[PIIEntity]:
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


def x_detect_pii__mutmut_1(text: str) -> list[PIIEntity]:
    entities = None

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


def x_detect_pii__mutmut_2(text: str) -> list[PIIEntity]:
    entities = _analyze(None)

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


def x_detect_pii__mutmut_3(text: str) -> list[PIIEntity]:
    entities = _analyze(text)

    decoded = None
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


def x_detect_pii__mutmut_4(text: str) -> list[PIIEntity]:
    entities = _analyze(text)

    decoded = _decode_base64_layers(None)
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


def x_detect_pii__mutmut_5(text: str) -> list[PIIEntity]:
    entities = _analyze(text)

    decoded = _decode_base64_layers(text)
    if decoded == text:
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


def x_detect_pii__mutmut_6(text: str) -> list[PIIEntity]:
    entities = _analyze(text)

    decoded = _decode_base64_layers(text)
    if decoded != text:
        decoded_entities = None
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


def x_detect_pii__mutmut_7(text: str) -> list[PIIEntity]:
    entities = _analyze(text)

    decoded = _decode_base64_layers(text)
    if decoded != text:
        decoded_entities = _analyze(None)
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


def x_detect_pii__mutmut_8(text: str) -> list[PIIEntity]:
    entities = _analyze(text)

    decoded = _decode_base64_layers(text)
    if decoded != text:
        decoded_entities = _analyze(decoded)
        for e in decoded_entities:
            entities.append(
                None
            )

    seen: set[tuple[str, int, int]] = set()
    unique: list[PIIEntity] = []
    for e in entities:
        key = (e.entity_type, e.start, e.end)
        if key not in seen:
            seen.add(key)
            unique.append(e)
    return unique


def x_detect_pii__mutmut_9(text: str) -> list[PIIEntity]:
    entities = _analyze(text)

    decoded = _decode_base64_layers(text)
    if decoded != text:
        decoded_entities = _analyze(decoded)
        for e in decoded_entities:
            entities.append(
                PIIEntity(
                    entity_type=None,
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


def x_detect_pii__mutmut_10(text: str) -> list[PIIEntity]:
    entities = _analyze(text)

    decoded = _decode_base64_layers(text)
    if decoded != text:
        decoded_entities = _analyze(decoded)
        for e in decoded_entities:
            entities.append(
                PIIEntity(
                    entity_type=e.entity_type,
                    start=None,
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


def x_detect_pii__mutmut_11(text: str) -> list[PIIEntity]:
    entities = _analyze(text)

    decoded = _decode_base64_layers(text)
    if decoded != text:
        decoded_entities = _analyze(decoded)
        for e in decoded_entities:
            entities.append(
                PIIEntity(
                    entity_type=e.entity_type,
                    start=len(text) + 1 + e.start,
                    end=None,
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


def x_detect_pii__mutmut_12(text: str) -> list[PIIEntity]:
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
                    text=None,
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


def x_detect_pii__mutmut_13(text: str) -> list[PIIEntity]:
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
                    score=None,
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


def x_detect_pii__mutmut_14(text: str) -> list[PIIEntity]:
    entities = _analyze(text)

    decoded = _decode_base64_layers(text)
    if decoded != text:
        decoded_entities = _analyze(decoded)
        for e in decoded_entities:
            entities.append(
                PIIEntity(
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


def x_detect_pii__mutmut_15(text: str) -> list[PIIEntity]:
    entities = _analyze(text)

    decoded = _decode_base64_layers(text)
    if decoded != text:
        decoded_entities = _analyze(decoded)
        for e in decoded_entities:
            entities.append(
                PIIEntity(
                    entity_type=e.entity_type,
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


def x_detect_pii__mutmut_16(text: str) -> list[PIIEntity]:
    entities = _analyze(text)

    decoded = _decode_base64_layers(text)
    if decoded != text:
        decoded_entities = _analyze(decoded)
        for e in decoded_entities:
            entities.append(
                PIIEntity(
                    entity_type=e.entity_type,
                    start=len(text) + 1 + e.start,
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


def x_detect_pii__mutmut_17(text: str) -> list[PIIEntity]:
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


def x_detect_pii__mutmut_18(text: str) -> list[PIIEntity]:
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


def x_detect_pii__mutmut_19(text: str) -> list[PIIEntity]:
    entities = _analyze(text)

    decoded = _decode_base64_layers(text)
    if decoded != text:
        decoded_entities = _analyze(decoded)
        for e in decoded_entities:
            entities.append(
                PIIEntity(
                    entity_type=e.entity_type,
                    start=len(text) + 1 - e.start,
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


def x_detect_pii__mutmut_20(text: str) -> list[PIIEntity]:
    entities = _analyze(text)

    decoded = _decode_base64_layers(text)
    if decoded != text:
        decoded_entities = _analyze(decoded)
        for e in decoded_entities:
            entities.append(
                PIIEntity(
                    entity_type=e.entity_type,
                    start=len(text) - 1 + e.start,
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


def x_detect_pii__mutmut_21(text: str) -> list[PIIEntity]:
    entities = _analyze(text)

    decoded = _decode_base64_layers(text)
    if decoded != text:
        decoded_entities = _analyze(decoded)
        for e in decoded_entities:
            entities.append(
                PIIEntity(
                    entity_type=e.entity_type,
                    start=len(text) + 2 + e.start,
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


def x_detect_pii__mutmut_22(text: str) -> list[PIIEntity]:
    entities = _analyze(text)

    decoded = _decode_base64_layers(text)
    if decoded != text:
        decoded_entities = _analyze(decoded)
        for e in decoded_entities:
            entities.append(
                PIIEntity(
                    entity_type=e.entity_type,
                    start=len(text) + 1 + e.start,
                    end=len(text) + 1 - e.end,
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


def x_detect_pii__mutmut_23(text: str) -> list[PIIEntity]:
    entities = _analyze(text)

    decoded = _decode_base64_layers(text)
    if decoded != text:
        decoded_entities = _analyze(decoded)
        for e in decoded_entities:
            entities.append(
                PIIEntity(
                    entity_type=e.entity_type,
                    start=len(text) + 1 + e.start,
                    end=len(text) - 1 + e.end,
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


def x_detect_pii__mutmut_24(text: str) -> list[PIIEntity]:
    entities = _analyze(text)

    decoded = _decode_base64_layers(text)
    if decoded != text:
        decoded_entities = _analyze(decoded)
        for e in decoded_entities:
            entities.append(
                PIIEntity(
                    entity_type=e.entity_type,
                    start=len(text) + 1 + e.start,
                    end=len(text) + 2 + e.end,
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


def x_detect_pii__mutmut_25(text: str) -> list[PIIEntity]:
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

    seen: set[tuple[str, int, int]] = None
    unique: list[PIIEntity] = []
    for e in entities:
        key = (e.entity_type, e.start, e.end)
        if key not in seen:
            seen.add(key)
            unique.append(e)
    return unique


def x_detect_pii__mutmut_26(text: str) -> list[PIIEntity]:
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
    unique: list[PIIEntity] = None
    for e in entities:
        key = (e.entity_type, e.start, e.end)
        if key not in seen:
            seen.add(key)
            unique.append(e)
    return unique


def x_detect_pii__mutmut_27(text: str) -> list[PIIEntity]:
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
        key = None
        if key not in seen:
            seen.add(key)
            unique.append(e)
    return unique


def x_detect_pii__mutmut_28(text: str) -> list[PIIEntity]:
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
        if key in seen:
            seen.add(key)
            unique.append(e)
    return unique


def x_detect_pii__mutmut_29(text: str) -> list[PIIEntity]:
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
            seen.add(None)
            unique.append(e)
    return unique


def x_detect_pii__mutmut_30(text: str) -> list[PIIEntity]:
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
            unique.append(None)
    return unique

x_detect_pii__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_detect_pii__mutmut_1': x_detect_pii__mutmut_1, 
    'x_detect_pii__mutmut_2': x_detect_pii__mutmut_2, 
    'x_detect_pii__mutmut_3': x_detect_pii__mutmut_3, 
    'x_detect_pii__mutmut_4': x_detect_pii__mutmut_4, 
    'x_detect_pii__mutmut_5': x_detect_pii__mutmut_5, 
    'x_detect_pii__mutmut_6': x_detect_pii__mutmut_6, 
    'x_detect_pii__mutmut_7': x_detect_pii__mutmut_7, 
    'x_detect_pii__mutmut_8': x_detect_pii__mutmut_8, 
    'x_detect_pii__mutmut_9': x_detect_pii__mutmut_9, 
    'x_detect_pii__mutmut_10': x_detect_pii__mutmut_10, 
    'x_detect_pii__mutmut_11': x_detect_pii__mutmut_11, 
    'x_detect_pii__mutmut_12': x_detect_pii__mutmut_12, 
    'x_detect_pii__mutmut_13': x_detect_pii__mutmut_13, 
    'x_detect_pii__mutmut_14': x_detect_pii__mutmut_14, 
    'x_detect_pii__mutmut_15': x_detect_pii__mutmut_15, 
    'x_detect_pii__mutmut_16': x_detect_pii__mutmut_16, 
    'x_detect_pii__mutmut_17': x_detect_pii__mutmut_17, 
    'x_detect_pii__mutmut_18': x_detect_pii__mutmut_18, 
    'x_detect_pii__mutmut_19': x_detect_pii__mutmut_19, 
    'x_detect_pii__mutmut_20': x_detect_pii__mutmut_20, 
    'x_detect_pii__mutmut_21': x_detect_pii__mutmut_21, 
    'x_detect_pii__mutmut_22': x_detect_pii__mutmut_22, 
    'x_detect_pii__mutmut_23': x_detect_pii__mutmut_23, 
    'x_detect_pii__mutmut_24': x_detect_pii__mutmut_24, 
    'x_detect_pii__mutmut_25': x_detect_pii__mutmut_25, 
    'x_detect_pii__mutmut_26': x_detect_pii__mutmut_26, 
    'x_detect_pii__mutmut_27': x_detect_pii__mutmut_27, 
    'x_detect_pii__mutmut_28': x_detect_pii__mutmut_28, 
    'x_detect_pii__mutmut_29': x_detect_pii__mutmut_29, 
    'x_detect_pii__mutmut_30': x_detect_pii__mutmut_30
}
x_detect_pii__mutmut_orig.__name__ = 'x_detect_pii'


def redact_pii(text: str, entities: list[PIIEntity]) -> str:
    args = [text, entities]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_redact_pii__mutmut_orig, x_redact_pii__mutmut_mutants, args, kwargs, None)


def x_redact_pii__mutmut_orig(text: str, entities: list[PIIEntity]) -> str:
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


def x_redact_pii__mutmut_1(text: str, entities: list[PIIEntity]) -> str:
    if entities:
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


def x_redact_pii__mutmut_2(text: str, entities: list[PIIEntity]) -> str:
    if not entities:
        return text
    original = None
    if not original:
        return text
    sorted_entities = sorted(original, key=lambda e: e.start, reverse=True)
    result = text
    for entity in sorted_entities:
        placeholder = f"[REDACTED_{entity.entity_type}]"
        if entity.start <= len(result) and entity.end <= len(result):
            result = result[: entity.start] + placeholder + result[entity.end :]
    return result


def x_redact_pii__mutmut_3(text: str, entities: list[PIIEntity]) -> str:
    if not entities:
        return text
    original = [e for e in entities if e.start <= len(text)]
    if not original:
        return text
    sorted_entities = sorted(original, key=lambda e: e.start, reverse=True)
    result = text
    for entity in sorted_entities:
        placeholder = f"[REDACTED_{entity.entity_type}]"
        if entity.start <= len(result) and entity.end <= len(result):
            result = result[: entity.start] + placeholder + result[entity.end :]
    return result


def x_redact_pii__mutmut_4(text: str, entities: list[PIIEntity]) -> str:
    if not entities:
        return text
    original = [e for e in entities if e.start < len(text)]
    if original:
        return text
    sorted_entities = sorted(original, key=lambda e: e.start, reverse=True)
    result = text
    for entity in sorted_entities:
        placeholder = f"[REDACTED_{entity.entity_type}]"
        if entity.start <= len(result) and entity.end <= len(result):
            result = result[: entity.start] + placeholder + result[entity.end :]
    return result


def x_redact_pii__mutmut_5(text: str, entities: list[PIIEntity]) -> str:
    if not entities:
        return text
    original = [e for e in entities if e.start < len(text)]
    if not original:
        return text
    sorted_entities = None
    result = text
    for entity in sorted_entities:
        placeholder = f"[REDACTED_{entity.entity_type}]"
        if entity.start <= len(result) and entity.end <= len(result):
            result = result[: entity.start] + placeholder + result[entity.end :]
    return result


def x_redact_pii__mutmut_6(text: str, entities: list[PIIEntity]) -> str:
    if not entities:
        return text
    original = [e for e in entities if e.start < len(text)]
    if not original:
        return text
    sorted_entities = sorted(None, key=lambda e: e.start, reverse=True)
    result = text
    for entity in sorted_entities:
        placeholder = f"[REDACTED_{entity.entity_type}]"
        if entity.start <= len(result) and entity.end <= len(result):
            result = result[: entity.start] + placeholder + result[entity.end :]
    return result


def x_redact_pii__mutmut_7(text: str, entities: list[PIIEntity]) -> str:
    if not entities:
        return text
    original = [e for e in entities if e.start < len(text)]
    if not original:
        return text
    sorted_entities = sorted(original, key=None, reverse=True)
    result = text
    for entity in sorted_entities:
        placeholder = f"[REDACTED_{entity.entity_type}]"
        if entity.start <= len(result) and entity.end <= len(result):
            result = result[: entity.start] + placeholder + result[entity.end :]
    return result


def x_redact_pii__mutmut_8(text: str, entities: list[PIIEntity]) -> str:
    if not entities:
        return text
    original = [e for e in entities if e.start < len(text)]
    if not original:
        return text
    sorted_entities = sorted(original, key=lambda e: e.start, reverse=None)
    result = text
    for entity in sorted_entities:
        placeholder = f"[REDACTED_{entity.entity_type}]"
        if entity.start <= len(result) and entity.end <= len(result):
            result = result[: entity.start] + placeholder + result[entity.end :]
    return result


def x_redact_pii__mutmut_9(text: str, entities: list[PIIEntity]) -> str:
    if not entities:
        return text
    original = [e for e in entities if e.start < len(text)]
    if not original:
        return text
    sorted_entities = sorted(key=lambda e: e.start, reverse=True)
    result = text
    for entity in sorted_entities:
        placeholder = f"[REDACTED_{entity.entity_type}]"
        if entity.start <= len(result) and entity.end <= len(result):
            result = result[: entity.start] + placeholder + result[entity.end :]
    return result


def x_redact_pii__mutmut_10(text: str, entities: list[PIIEntity]) -> str:
    if not entities:
        return text
    original = [e for e in entities if e.start < len(text)]
    if not original:
        return text
    sorted_entities = sorted(original, reverse=True)
    result = text
    for entity in sorted_entities:
        placeholder = f"[REDACTED_{entity.entity_type}]"
        if entity.start <= len(result) and entity.end <= len(result):
            result = result[: entity.start] + placeholder + result[entity.end :]
    return result


def x_redact_pii__mutmut_11(text: str, entities: list[PIIEntity]) -> str:
    if not entities:
        return text
    original = [e for e in entities if e.start < len(text)]
    if not original:
        return text
    sorted_entities = sorted(original, key=lambda e: e.start, )
    result = text
    for entity in sorted_entities:
        placeholder = f"[REDACTED_{entity.entity_type}]"
        if entity.start <= len(result) and entity.end <= len(result):
            result = result[: entity.start] + placeholder + result[entity.end :]
    return result


def x_redact_pii__mutmut_12(text: str, entities: list[PIIEntity]) -> str:
    if not entities:
        return text
    original = [e for e in entities if e.start < len(text)]
    if not original:
        return text
    sorted_entities = sorted(original, key=lambda e: None, reverse=True)
    result = text
    for entity in sorted_entities:
        placeholder = f"[REDACTED_{entity.entity_type}]"
        if entity.start <= len(result) and entity.end <= len(result):
            result = result[: entity.start] + placeholder + result[entity.end :]
    return result


def x_redact_pii__mutmut_13(text: str, entities: list[PIIEntity]) -> str:
    if not entities:
        return text
    original = [e for e in entities if e.start < len(text)]
    if not original:
        return text
    sorted_entities = sorted(original, key=lambda e: e.start, reverse=False)
    result = text
    for entity in sorted_entities:
        placeholder = f"[REDACTED_{entity.entity_type}]"
        if entity.start <= len(result) and entity.end <= len(result):
            result = result[: entity.start] + placeholder + result[entity.end :]
    return result


def x_redact_pii__mutmut_14(text: str, entities: list[PIIEntity]) -> str:
    if not entities:
        return text
    original = [e for e in entities if e.start < len(text)]
    if not original:
        return text
    sorted_entities = sorted(original, key=lambda e: e.start, reverse=True)
    result = None
    for entity in sorted_entities:
        placeholder = f"[REDACTED_{entity.entity_type}]"
        if entity.start <= len(result) and entity.end <= len(result):
            result = result[: entity.start] + placeholder + result[entity.end :]
    return result


def x_redact_pii__mutmut_15(text: str, entities: list[PIIEntity]) -> str:
    if not entities:
        return text
    original = [e for e in entities if e.start < len(text)]
    if not original:
        return text
    sorted_entities = sorted(original, key=lambda e: e.start, reverse=True)
    result = text
    for entity in sorted_entities:
        placeholder = None
        if entity.start <= len(result) and entity.end <= len(result):
            result = result[: entity.start] + placeholder + result[entity.end :]
    return result


def x_redact_pii__mutmut_16(text: str, entities: list[PIIEntity]) -> str:
    if not entities:
        return text
    original = [e for e in entities if e.start < len(text)]
    if not original:
        return text
    sorted_entities = sorted(original, key=lambda e: e.start, reverse=True)
    result = text
    for entity in sorted_entities:
        placeholder = f"[REDACTED_{entity.entity_type}]"
        if entity.start <= len(result) or entity.end <= len(result):
            result = result[: entity.start] + placeholder + result[entity.end :]
    return result


def x_redact_pii__mutmut_17(text: str, entities: list[PIIEntity]) -> str:
    if not entities:
        return text
    original = [e for e in entities if e.start < len(text)]
    if not original:
        return text
    sorted_entities = sorted(original, key=lambda e: e.start, reverse=True)
    result = text
    for entity in sorted_entities:
        placeholder = f"[REDACTED_{entity.entity_type}]"
        if entity.start < len(result) and entity.end <= len(result):
            result = result[: entity.start] + placeholder + result[entity.end :]
    return result


def x_redact_pii__mutmut_18(text: str, entities: list[PIIEntity]) -> str:
    if not entities:
        return text
    original = [e for e in entities if e.start < len(text)]
    if not original:
        return text
    sorted_entities = sorted(original, key=lambda e: e.start, reverse=True)
    result = text
    for entity in sorted_entities:
        placeholder = f"[REDACTED_{entity.entity_type}]"
        if entity.start <= len(result) and entity.end < len(result):
            result = result[: entity.start] + placeholder + result[entity.end :]
    return result


def x_redact_pii__mutmut_19(text: str, entities: list[PIIEntity]) -> str:
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
            result = None
    return result


def x_redact_pii__mutmut_20(text: str, entities: list[PIIEntity]) -> str:
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
            result = result[: entity.start] + placeholder - result[entity.end :]
    return result


def x_redact_pii__mutmut_21(text: str, entities: list[PIIEntity]) -> str:
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
            result = result[: entity.start] - placeholder + result[entity.end :]
    return result

x_redact_pii__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_redact_pii__mutmut_1': x_redact_pii__mutmut_1, 
    'x_redact_pii__mutmut_2': x_redact_pii__mutmut_2, 
    'x_redact_pii__mutmut_3': x_redact_pii__mutmut_3, 
    'x_redact_pii__mutmut_4': x_redact_pii__mutmut_4, 
    'x_redact_pii__mutmut_5': x_redact_pii__mutmut_5, 
    'x_redact_pii__mutmut_6': x_redact_pii__mutmut_6, 
    'x_redact_pii__mutmut_7': x_redact_pii__mutmut_7, 
    'x_redact_pii__mutmut_8': x_redact_pii__mutmut_8, 
    'x_redact_pii__mutmut_9': x_redact_pii__mutmut_9, 
    'x_redact_pii__mutmut_10': x_redact_pii__mutmut_10, 
    'x_redact_pii__mutmut_11': x_redact_pii__mutmut_11, 
    'x_redact_pii__mutmut_12': x_redact_pii__mutmut_12, 
    'x_redact_pii__mutmut_13': x_redact_pii__mutmut_13, 
    'x_redact_pii__mutmut_14': x_redact_pii__mutmut_14, 
    'x_redact_pii__mutmut_15': x_redact_pii__mutmut_15, 
    'x_redact_pii__mutmut_16': x_redact_pii__mutmut_16, 
    'x_redact_pii__mutmut_17': x_redact_pii__mutmut_17, 
    'x_redact_pii__mutmut_18': x_redact_pii__mutmut_18, 
    'x_redact_pii__mutmut_19': x_redact_pii__mutmut_19, 
    'x_redact_pii__mutmut_20': x_redact_pii__mutmut_20, 
    'x_redact_pii__mutmut_21': x_redact_pii__mutmut_21
}
x_redact_pii__mutmut_orig.__name__ = 'x_redact_pii'


def check_pii_density(text: str, entities: list[PIIEntity]) -> float:
    args = [text, entities]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_pii_density__mutmut_orig, x_check_pii_density__mutmut_mutants, args, kwargs, None)


def x_check_pii_density__mutmut_orig(text: str, entities: list[PIIEntity]) -> float:
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


def x_check_pii_density__mutmut_1(text: str, entities: list[PIIEntity]) -> float:
    if text:
        return 0.0
    seen_texts: set[str] = set()
    pii_chars = 0
    for e in entities:
        if e.text in seen_texts:
            continue
        seen_texts.add(e.text)
        pii_chars += len(e.text)
    return pii_chars / len(text)


def x_check_pii_density__mutmut_2(text: str, entities: list[PIIEntity]) -> float:
    if not text:
        return 1.0
    seen_texts: set[str] = set()
    pii_chars = 0
    for e in entities:
        if e.text in seen_texts:
            continue
        seen_texts.add(e.text)
        pii_chars += len(e.text)
    return pii_chars / len(text)


def x_check_pii_density__mutmut_3(text: str, entities: list[PIIEntity]) -> float:
    if not text:
        return 0.0
    seen_texts: set[str] = None
    pii_chars = 0
    for e in entities:
        if e.text in seen_texts:
            continue
        seen_texts.add(e.text)
        pii_chars += len(e.text)
    return pii_chars / len(text)


def x_check_pii_density__mutmut_4(text: str, entities: list[PIIEntity]) -> float:
    if not text:
        return 0.0
    seen_texts: set[str] = set()
    pii_chars = None
    for e in entities:
        if e.text in seen_texts:
            continue
        seen_texts.add(e.text)
        pii_chars += len(e.text)
    return pii_chars / len(text)


def x_check_pii_density__mutmut_5(text: str, entities: list[PIIEntity]) -> float:
    if not text:
        return 0.0
    seen_texts: set[str] = set()
    pii_chars = 1
    for e in entities:
        if e.text in seen_texts:
            continue
        seen_texts.add(e.text)
        pii_chars += len(e.text)
    return pii_chars / len(text)


def x_check_pii_density__mutmut_6(text: str, entities: list[PIIEntity]) -> float:
    if not text:
        return 0.0
    seen_texts: set[str] = set()
    pii_chars = 0
    for e in entities:
        if e.text not in seen_texts:
            continue
        seen_texts.add(e.text)
        pii_chars += len(e.text)
    return pii_chars / len(text)


def x_check_pii_density__mutmut_7(text: str, entities: list[PIIEntity]) -> float:
    if not text:
        return 0.0
    seen_texts: set[str] = set()
    pii_chars = 0
    for e in entities:
        if e.text in seen_texts:
            break
        seen_texts.add(e.text)
        pii_chars += len(e.text)
    return pii_chars / len(text)


def x_check_pii_density__mutmut_8(text: str, entities: list[PIIEntity]) -> float:
    if not text:
        return 0.0
    seen_texts: set[str] = set()
    pii_chars = 0
    for e in entities:
        if e.text in seen_texts:
            continue
        seen_texts.add(None)
        pii_chars += len(e.text)
    return pii_chars / len(text)


def x_check_pii_density__mutmut_9(text: str, entities: list[PIIEntity]) -> float:
    if not text:
        return 0.0
    seen_texts: set[str] = set()
    pii_chars = 0
    for e in entities:
        if e.text in seen_texts:
            continue
        seen_texts.add(e.text)
        pii_chars = len(e.text)
    return pii_chars / len(text)


def x_check_pii_density__mutmut_10(text: str, entities: list[PIIEntity]) -> float:
    if not text:
        return 0.0
    seen_texts: set[str] = set()
    pii_chars = 0
    for e in entities:
        if e.text in seen_texts:
            continue
        seen_texts.add(e.text)
        pii_chars -= len(e.text)
    return pii_chars / len(text)


def x_check_pii_density__mutmut_11(text: str, entities: list[PIIEntity]) -> float:
    if not text:
        return 0.0
    seen_texts: set[str] = set()
    pii_chars = 0
    for e in entities:
        if e.text in seen_texts:
            continue
        seen_texts.add(e.text)
        pii_chars += len(e.text)
    return pii_chars * len(text)

x_check_pii_density__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_check_pii_density__mutmut_1': x_check_pii_density__mutmut_1, 
    'x_check_pii_density__mutmut_2': x_check_pii_density__mutmut_2, 
    'x_check_pii_density__mutmut_3': x_check_pii_density__mutmut_3, 
    'x_check_pii_density__mutmut_4': x_check_pii_density__mutmut_4, 
    'x_check_pii_density__mutmut_5': x_check_pii_density__mutmut_5, 
    'x_check_pii_density__mutmut_6': x_check_pii_density__mutmut_6, 
    'x_check_pii_density__mutmut_7': x_check_pii_density__mutmut_7, 
    'x_check_pii_density__mutmut_8': x_check_pii_density__mutmut_8, 
    'x_check_pii_density__mutmut_9': x_check_pii_density__mutmut_9, 
    'x_check_pii_density__mutmut_10': x_check_pii_density__mutmut_10, 
    'x_check_pii_density__mutmut_11': x_check_pii_density__mutmut_11
}
x_check_pii_density__mutmut_orig.__name__ = 'x_check_pii_density'


def should_escalate(density: float, threshold: float = 0.7) -> bool:
    args = [density, threshold]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_should_escalate__mutmut_orig, x_should_escalate__mutmut_mutants, args, kwargs, None)


def x_should_escalate__mutmut_orig(density: float, threshold: float = 0.7) -> bool:
    return density > threshold


def x_should_escalate__mutmut_1(density: float, threshold: float = 1.7) -> bool:
    return density > threshold


def x_should_escalate__mutmut_2(density: float, threshold: float = 0.7) -> bool:
    return density >= threshold

x_should_escalate__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_should_escalate__mutmut_1': x_should_escalate__mutmut_1, 
    'x_should_escalate__mutmut_2': x_should_escalate__mutmut_2
}
x_should_escalate__mutmut_orig.__name__ = 'x_should_escalate'


def is_allowlisted_path(path: str, allowlist: list[str]) -> bool:
    args = [path, allowlist]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_allowlisted_path__mutmut_orig, x_is_allowlisted_path__mutmut_mutants, args, kwargs, None)


def x_is_allowlisted_path__mutmut_orig(path: str, allowlist: list[str]) -> bool:
    for allowed in allowlist:
        if path.startswith(allowed):
            return True
    return False


def x_is_allowlisted_path__mutmut_1(path: str, allowlist: list[str]) -> bool:
    for allowed in allowlist:
        if path.startswith(None):
            return True
    return False


def x_is_allowlisted_path__mutmut_2(path: str, allowlist: list[str]) -> bool:
    for allowed in allowlist:
        if path.startswith(allowed):
            return False
    return False


def x_is_allowlisted_path__mutmut_3(path: str, allowlist: list[str]) -> bool:
    for allowed in allowlist:
        if path.startswith(allowed):
            return True
    return True

x_is_allowlisted_path__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_is_allowlisted_path__mutmut_1': x_is_allowlisted_path__mutmut_1, 
    'x_is_allowlisted_path__mutmut_2': x_is_allowlisted_path__mutmut_2, 
    'x_is_allowlisted_path__mutmut_3': x_is_allowlisted_path__mutmut_3
}
x_is_allowlisted_path__mutmut_orig.__name__ = 'x_is_allowlisted_path'


def scan_and_redact(
    text: str,
    path: str | None = None,
    allowlist: list[str] | None = None,
) -> tuple[str, list[PIIEntity], bool]:
    args = [text, path, allowlist]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_scan_and_redact__mutmut_orig, x_scan_and_redact__mutmut_mutants, args, kwargs, None)


def x_scan_and_redact__mutmut_orig(
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


def x_scan_and_redact__mutmut_1(
    text: str,
    path: str | None = None,
    allowlist: list[str] | None = None,
) -> tuple[str, list[PIIEntity], bool]:
    if allowlist is not None and path is not None or is_allowlisted_path(path, allowlist):
        return text, [], False
    entities = detect_pii(text)
    if not entities:
        return text, entities, False
    redacted = redact_pii(text, entities)
    density = check_pii_density(text, entities)
    return redacted, entities, should_escalate(density)


def x_scan_and_redact__mutmut_2(
    text: str,
    path: str | None = None,
    allowlist: list[str] | None = None,
) -> tuple[str, list[PIIEntity], bool]:
    if allowlist is not None or path is not None and is_allowlisted_path(path, allowlist):
        return text, [], False
    entities = detect_pii(text)
    if not entities:
        return text, entities, False
    redacted = redact_pii(text, entities)
    density = check_pii_density(text, entities)
    return redacted, entities, should_escalate(density)


def x_scan_and_redact__mutmut_3(
    text: str,
    path: str | None = None,
    allowlist: list[str] | None = None,
) -> tuple[str, list[PIIEntity], bool]:
    if allowlist is None and path is not None and is_allowlisted_path(path, allowlist):
        return text, [], False
    entities = detect_pii(text)
    if not entities:
        return text, entities, False
    redacted = redact_pii(text, entities)
    density = check_pii_density(text, entities)
    return redacted, entities, should_escalate(density)


def x_scan_and_redact__mutmut_4(
    text: str,
    path: str | None = None,
    allowlist: list[str] | None = None,
) -> tuple[str, list[PIIEntity], bool]:
    if allowlist is not None and path is None and is_allowlisted_path(path, allowlist):
        return text, [], False
    entities = detect_pii(text)
    if not entities:
        return text, entities, False
    redacted = redact_pii(text, entities)
    density = check_pii_density(text, entities)
    return redacted, entities, should_escalate(density)


def x_scan_and_redact__mutmut_5(
    text: str,
    path: str | None = None,
    allowlist: list[str] | None = None,
) -> tuple[str, list[PIIEntity], bool]:
    if allowlist is not None and path is not None and is_allowlisted_path(None, allowlist):
        return text, [], False
    entities = detect_pii(text)
    if not entities:
        return text, entities, False
    redacted = redact_pii(text, entities)
    density = check_pii_density(text, entities)
    return redacted, entities, should_escalate(density)


def x_scan_and_redact__mutmut_6(
    text: str,
    path: str | None = None,
    allowlist: list[str] | None = None,
) -> tuple[str, list[PIIEntity], bool]:
    if allowlist is not None and path is not None and is_allowlisted_path(path, None):
        return text, [], False
    entities = detect_pii(text)
    if not entities:
        return text, entities, False
    redacted = redact_pii(text, entities)
    density = check_pii_density(text, entities)
    return redacted, entities, should_escalate(density)


def x_scan_and_redact__mutmut_7(
    text: str,
    path: str | None = None,
    allowlist: list[str] | None = None,
) -> tuple[str, list[PIIEntity], bool]:
    if allowlist is not None and path is not None and is_allowlisted_path(allowlist):
        return text, [], False
    entities = detect_pii(text)
    if not entities:
        return text, entities, False
    redacted = redact_pii(text, entities)
    density = check_pii_density(text, entities)
    return redacted, entities, should_escalate(density)


def x_scan_and_redact__mutmut_8(
    text: str,
    path: str | None = None,
    allowlist: list[str] | None = None,
) -> tuple[str, list[PIIEntity], bool]:
    if allowlist is not None and path is not None and is_allowlisted_path(path, ):
        return text, [], False
    entities = detect_pii(text)
    if not entities:
        return text, entities, False
    redacted = redact_pii(text, entities)
    density = check_pii_density(text, entities)
    return redacted, entities, should_escalate(density)


def x_scan_and_redact__mutmut_9(
    text: str,
    path: str | None = None,
    allowlist: list[str] | None = None,
) -> tuple[str, list[PIIEntity], bool]:
    if allowlist is not None and path is not None and is_allowlisted_path(path, allowlist):
        return text, [], True
    entities = detect_pii(text)
    if not entities:
        return text, entities, False
    redacted = redact_pii(text, entities)
    density = check_pii_density(text, entities)
    return redacted, entities, should_escalate(density)


def x_scan_and_redact__mutmut_10(
    text: str,
    path: str | None = None,
    allowlist: list[str] | None = None,
) -> tuple[str, list[PIIEntity], bool]:
    if allowlist is not None and path is not None and is_allowlisted_path(path, allowlist):
        return text, [], False
    entities = None
    if not entities:
        return text, entities, False
    redacted = redact_pii(text, entities)
    density = check_pii_density(text, entities)
    return redacted, entities, should_escalate(density)


def x_scan_and_redact__mutmut_11(
    text: str,
    path: str | None = None,
    allowlist: list[str] | None = None,
) -> tuple[str, list[PIIEntity], bool]:
    if allowlist is not None and path is not None and is_allowlisted_path(path, allowlist):
        return text, [], False
    entities = detect_pii(None)
    if not entities:
        return text, entities, False
    redacted = redact_pii(text, entities)
    density = check_pii_density(text, entities)
    return redacted, entities, should_escalate(density)


def x_scan_and_redact__mutmut_12(
    text: str,
    path: str | None = None,
    allowlist: list[str] | None = None,
) -> tuple[str, list[PIIEntity], bool]:
    if allowlist is not None and path is not None and is_allowlisted_path(path, allowlist):
        return text, [], False
    entities = detect_pii(text)
    if entities:
        return text, entities, False
    redacted = redact_pii(text, entities)
    density = check_pii_density(text, entities)
    return redacted, entities, should_escalate(density)


def x_scan_and_redact__mutmut_13(
    text: str,
    path: str | None = None,
    allowlist: list[str] | None = None,
) -> tuple[str, list[PIIEntity], bool]:
    if allowlist is not None and path is not None and is_allowlisted_path(path, allowlist):
        return text, [], False
    entities = detect_pii(text)
    if not entities:
        return text, entities, True
    redacted = redact_pii(text, entities)
    density = check_pii_density(text, entities)
    return redacted, entities, should_escalate(density)


def x_scan_and_redact__mutmut_14(
    text: str,
    path: str | None = None,
    allowlist: list[str] | None = None,
) -> tuple[str, list[PIIEntity], bool]:
    if allowlist is not None and path is not None and is_allowlisted_path(path, allowlist):
        return text, [], False
    entities = detect_pii(text)
    if not entities:
        return text, entities, False
    redacted = None
    density = check_pii_density(text, entities)
    return redacted, entities, should_escalate(density)


def x_scan_and_redact__mutmut_15(
    text: str,
    path: str | None = None,
    allowlist: list[str] | None = None,
) -> tuple[str, list[PIIEntity], bool]:
    if allowlist is not None and path is not None and is_allowlisted_path(path, allowlist):
        return text, [], False
    entities = detect_pii(text)
    if not entities:
        return text, entities, False
    redacted = redact_pii(None, entities)
    density = check_pii_density(text, entities)
    return redacted, entities, should_escalate(density)


def x_scan_and_redact__mutmut_16(
    text: str,
    path: str | None = None,
    allowlist: list[str] | None = None,
) -> tuple[str, list[PIIEntity], bool]:
    if allowlist is not None and path is not None and is_allowlisted_path(path, allowlist):
        return text, [], False
    entities = detect_pii(text)
    if not entities:
        return text, entities, False
    redacted = redact_pii(text, None)
    density = check_pii_density(text, entities)
    return redacted, entities, should_escalate(density)


def x_scan_and_redact__mutmut_17(
    text: str,
    path: str | None = None,
    allowlist: list[str] | None = None,
) -> tuple[str, list[PIIEntity], bool]:
    if allowlist is not None and path is not None and is_allowlisted_path(path, allowlist):
        return text, [], False
    entities = detect_pii(text)
    if not entities:
        return text, entities, False
    redacted = redact_pii(entities)
    density = check_pii_density(text, entities)
    return redacted, entities, should_escalate(density)


def x_scan_and_redact__mutmut_18(
    text: str,
    path: str | None = None,
    allowlist: list[str] | None = None,
) -> tuple[str, list[PIIEntity], bool]:
    if allowlist is not None and path is not None and is_allowlisted_path(path, allowlist):
        return text, [], False
    entities = detect_pii(text)
    if not entities:
        return text, entities, False
    redacted = redact_pii(text, )
    density = check_pii_density(text, entities)
    return redacted, entities, should_escalate(density)


def x_scan_and_redact__mutmut_19(
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
    density = None
    return redacted, entities, should_escalate(density)


def x_scan_and_redact__mutmut_20(
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
    density = check_pii_density(None, entities)
    return redacted, entities, should_escalate(density)


def x_scan_and_redact__mutmut_21(
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
    density = check_pii_density(text, None)
    return redacted, entities, should_escalate(density)


def x_scan_and_redact__mutmut_22(
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
    density = check_pii_density(entities)
    return redacted, entities, should_escalate(density)


def x_scan_and_redact__mutmut_23(
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
    density = check_pii_density(text, )
    return redacted, entities, should_escalate(density)


def x_scan_and_redact__mutmut_24(
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
    return redacted, entities, should_escalate(None)

x_scan_and_redact__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_scan_and_redact__mutmut_1': x_scan_and_redact__mutmut_1, 
    'x_scan_and_redact__mutmut_2': x_scan_and_redact__mutmut_2, 
    'x_scan_and_redact__mutmut_3': x_scan_and_redact__mutmut_3, 
    'x_scan_and_redact__mutmut_4': x_scan_and_redact__mutmut_4, 
    'x_scan_and_redact__mutmut_5': x_scan_and_redact__mutmut_5, 
    'x_scan_and_redact__mutmut_6': x_scan_and_redact__mutmut_6, 
    'x_scan_and_redact__mutmut_7': x_scan_and_redact__mutmut_7, 
    'x_scan_and_redact__mutmut_8': x_scan_and_redact__mutmut_8, 
    'x_scan_and_redact__mutmut_9': x_scan_and_redact__mutmut_9, 
    'x_scan_and_redact__mutmut_10': x_scan_and_redact__mutmut_10, 
    'x_scan_and_redact__mutmut_11': x_scan_and_redact__mutmut_11, 
    'x_scan_and_redact__mutmut_12': x_scan_and_redact__mutmut_12, 
    'x_scan_and_redact__mutmut_13': x_scan_and_redact__mutmut_13, 
    'x_scan_and_redact__mutmut_14': x_scan_and_redact__mutmut_14, 
    'x_scan_and_redact__mutmut_15': x_scan_and_redact__mutmut_15, 
    'x_scan_and_redact__mutmut_16': x_scan_and_redact__mutmut_16, 
    'x_scan_and_redact__mutmut_17': x_scan_and_redact__mutmut_17, 
    'x_scan_and_redact__mutmut_18': x_scan_and_redact__mutmut_18, 
    'x_scan_and_redact__mutmut_19': x_scan_and_redact__mutmut_19, 
    'x_scan_and_redact__mutmut_20': x_scan_and_redact__mutmut_20, 
    'x_scan_and_redact__mutmut_21': x_scan_and_redact__mutmut_21, 
    'x_scan_and_redact__mutmut_22': x_scan_and_redact__mutmut_22, 
    'x_scan_and_redact__mutmut_23': x_scan_and_redact__mutmut_23, 
    'x_scan_and_redact__mutmut_24': x_scan_and_redact__mutmut_24
}
x_scan_and_redact__mutmut_orig.__name__ = 'x_scan_and_redact'


def get_recognizer_info() -> list[dict[str, str | list[str]]]:
    args = []# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_get_recognizer_info__mutmut_orig, x_get_recognizer_info__mutmut_mutants, args, kwargs, None)


def x_get_recognizer_info__mutmut_orig() -> list[dict[str, str | list[str]]]:
    analyzer = _get_analyzer()
    recognizers = analyzer.registry.recognizers
    info: list[dict[str, str | list[str]]] = []
    for rec in recognizers:
        supported = [e for e in rec.supported_entities if e in _RECOGNIZER_ENTITIES]
        if supported:
            info.append({"name": rec.name, "entities": supported})
    return info


def x_get_recognizer_info__mutmut_1() -> list[dict[str, str | list[str]]]:
    analyzer = None
    recognizers = analyzer.registry.recognizers
    info: list[dict[str, str | list[str]]] = []
    for rec in recognizers:
        supported = [e for e in rec.supported_entities if e in _RECOGNIZER_ENTITIES]
        if supported:
            info.append({"name": rec.name, "entities": supported})
    return info


def x_get_recognizer_info__mutmut_2() -> list[dict[str, str | list[str]]]:
    analyzer = _get_analyzer()
    recognizers = None
    info: list[dict[str, str | list[str]]] = []
    for rec in recognizers:
        supported = [e for e in rec.supported_entities if e in _RECOGNIZER_ENTITIES]
        if supported:
            info.append({"name": rec.name, "entities": supported})
    return info


def x_get_recognizer_info__mutmut_3() -> list[dict[str, str | list[str]]]:
    analyzer = _get_analyzer()
    recognizers = analyzer.registry.recognizers
    info: list[dict[str, str | list[str]]] = None
    for rec in recognizers:
        supported = [e for e in rec.supported_entities if e in _RECOGNIZER_ENTITIES]
        if supported:
            info.append({"name": rec.name, "entities": supported})
    return info


def x_get_recognizer_info__mutmut_4() -> list[dict[str, str | list[str]]]:
    analyzer = _get_analyzer()
    recognizers = analyzer.registry.recognizers
    info: list[dict[str, str | list[str]]] = []
    for rec in recognizers:
        supported = None
        if supported:
            info.append({"name": rec.name, "entities": supported})
    return info


def x_get_recognizer_info__mutmut_5() -> list[dict[str, str | list[str]]]:
    analyzer = _get_analyzer()
    recognizers = analyzer.registry.recognizers
    info: list[dict[str, str | list[str]]] = []
    for rec in recognizers:
        supported = [e for e in rec.supported_entities if e not in _RECOGNIZER_ENTITIES]
        if supported:
            info.append({"name": rec.name, "entities": supported})
    return info


def x_get_recognizer_info__mutmut_6() -> list[dict[str, str | list[str]]]:
    analyzer = _get_analyzer()
    recognizers = analyzer.registry.recognizers
    info: list[dict[str, str | list[str]]] = []
    for rec in recognizers:
        supported = [e for e in rec.supported_entities if e in _RECOGNIZER_ENTITIES]
        if supported:
            info.append(None)
    return info


def x_get_recognizer_info__mutmut_7() -> list[dict[str, str | list[str]]]:
    analyzer = _get_analyzer()
    recognizers = analyzer.registry.recognizers
    info: list[dict[str, str | list[str]]] = []
    for rec in recognizers:
        supported = [e for e in rec.supported_entities if e in _RECOGNIZER_ENTITIES]
        if supported:
            info.append({"XXnameXX": rec.name, "entities": supported})
    return info


def x_get_recognizer_info__mutmut_8() -> list[dict[str, str | list[str]]]:
    analyzer = _get_analyzer()
    recognizers = analyzer.registry.recognizers
    info: list[dict[str, str | list[str]]] = []
    for rec in recognizers:
        supported = [e for e in rec.supported_entities if e in _RECOGNIZER_ENTITIES]
        if supported:
            info.append({"NAME": rec.name, "entities": supported})
    return info


def x_get_recognizer_info__mutmut_9() -> list[dict[str, str | list[str]]]:
    analyzer = _get_analyzer()
    recognizers = analyzer.registry.recognizers
    info: list[dict[str, str | list[str]]] = []
    for rec in recognizers:
        supported = [e for e in rec.supported_entities if e in _RECOGNIZER_ENTITIES]
        if supported:
            info.append({"name": rec.name, "XXentitiesXX": supported})
    return info


def x_get_recognizer_info__mutmut_10() -> list[dict[str, str | list[str]]]:
    analyzer = _get_analyzer()
    recognizers = analyzer.registry.recognizers
    info: list[dict[str, str | list[str]]] = []
    for rec in recognizers:
        supported = [e for e in rec.supported_entities if e in _RECOGNIZER_ENTITIES]
        if supported:
            info.append({"name": rec.name, "ENTITIES": supported})
    return info

x_get_recognizer_info__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_get_recognizer_info__mutmut_1': x_get_recognizer_info__mutmut_1, 
    'x_get_recognizer_info__mutmut_2': x_get_recognizer_info__mutmut_2, 
    'x_get_recognizer_info__mutmut_3': x_get_recognizer_info__mutmut_3, 
    'x_get_recognizer_info__mutmut_4': x_get_recognizer_info__mutmut_4, 
    'x_get_recognizer_info__mutmut_5': x_get_recognizer_info__mutmut_5, 
    'x_get_recognizer_info__mutmut_6': x_get_recognizer_info__mutmut_6, 
    'x_get_recognizer_info__mutmut_7': x_get_recognizer_info__mutmut_7, 
    'x_get_recognizer_info__mutmut_8': x_get_recognizer_info__mutmut_8, 
    'x_get_recognizer_info__mutmut_9': x_get_recognizer_info__mutmut_9, 
    'x_get_recognizer_info__mutmut_10': x_get_recognizer_info__mutmut_10
}
x_get_recognizer_info__mutmut_orig.__name__ = 'x_get_recognizer_info'
