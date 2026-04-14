import json
import re

from security_layer.models import PIIEntity, ValidationResult

_INJECTION_OUTPUT_PATTERNS = [
    re.compile(r"ignore\s+previous", re.IGNORECASE),
    re.compile(r"ignore\s+above", re.IGNORECASE),
    re.compile(r"ignore\s+all\s+(prior|previous)\s+(constraints|instructions|rules)", re.IGNORECASE),
    re.compile(r"ignore\s+all\s+(?:prior|previous)", re.IGNORECASE),
    re.compile(r"system\s*override", re.IGNORECASE),
    re.compile(r"new\s+instructions", re.IGNORECASE),
    re.compile(r"you\s+are\s+now", re.IGNORECASE),
    re.compile(r"role\s+change", re.IGNORECASE),
    re.compile(r"disregard", re.IGNORECASE),
    re.compile(r"forget\s+everything", re.IGNORECASE),
    re.compile(r"act\s+as", re.IGNORECASE),
    re.compile(r"pretend\s+you\s+are", re.IGNORECASE),
    re.compile(r"jailbreak", re.IGNORECASE),
    re.compile(r"DAN\s+mode", re.IGNORECASE),
    re.compile(r"developer\s+mode", re.IGNORECASE),
    re.compile(r"^SYSTEM:", re.IGNORECASE | re.MULTILINE),
    re.compile(r"^system:", re.MULTILINE),
]

_SHELL_DANGEROUS = re.compile(r"rm\s+-rf|mkfs|dd\s+if=|>\s*/dev/sd|shutdown|reboot", re.IGNORECASE)
_SQL_INJECTION = re.compile(
    r"(?:DROP\s+TABLE|DELETE\s+FROM|INSERT\s+INTO|UPDATE\s+\w+\s+SET|UNION\s+SELECT|;\s*--)",
    re.IGNORECASE,
)

_EXTERNAL_URL_PATTERN = re.compile(r"!\[([^\]]*)\]\((https?://[^)]+)\)")
_MAX_OUTPUT_LENGTH = 100_000
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


def _detect_pii_in_text(text: str) -> list[dict]:
    args = [text]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x__detect_pii_in_text__mutmut_orig, x__detect_pii_in_text__mutmut_mutants, args, kwargs, None)


def x__detect_pii_in_text__mutmut_orig(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_1(text: str) -> list[dict]:
    entities: list[dict] = None
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_2(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = None
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_3(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(None)
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_4(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"XX[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}XX")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_5(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-za-z0-9._%+-]+@[a-za-z0-9.-]+\.[a-za-z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_6(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[A-ZA-Z0-9._%+-]+@[A-ZA-Z0-9.-]+\.[A-ZA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_7(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(None):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_8(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append(None)
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_9(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"XXentity_typeXX": "EMAIL", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_10(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"ENTITY_TYPE": "EMAIL", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_11(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "XXEMAILXX", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_12(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "email", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_13(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "XXtextXX": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_14(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "TEXT": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_15(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "XXstartXX": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_16(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "START": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_17(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "start": m.start(), "XXendXX": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_18(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "start": m.start(), "END": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_19(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = None
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_20(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(None)
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_21(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"XX\+?\d[\d\s\-().]{7,}\dXX")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_22(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(None):
        entities.append({"entity_type": "PHONE", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_23(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append(None)
    return entities


def x__detect_pii_in_text__mutmut_24(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"XXentity_typeXX": "PHONE", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_25(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"ENTITY_TYPE": "PHONE", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_26(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "XXPHONEXX", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_27(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "phone", "text": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_28(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "XXtextXX": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_29(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "TEXT": m.group(), "start": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_30(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "text": m.group(), "XXstartXX": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_31(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "text": m.group(), "START": m.start(), "end": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_32(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "text": m.group(), "start": m.start(), "XXendXX": m.end()})
    return entities


def x__detect_pii_in_text__mutmut_33(text: str) -> list[dict]:
    entities: list[dict] = []
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    for m in email_pattern.finditer(text):
        entities.append({"entity_type": "EMAIL", "text": m.group(), "start": m.start(), "end": m.end()})
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    for m in phone_pattern.finditer(text):
        entities.append({"entity_type": "PHONE", "text": m.group(), "start": m.start(), "END": m.end()})
    return entities

x__detect_pii_in_text__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x__detect_pii_in_text__mutmut_1': x__detect_pii_in_text__mutmut_1, 
    'x__detect_pii_in_text__mutmut_2': x__detect_pii_in_text__mutmut_2, 
    'x__detect_pii_in_text__mutmut_3': x__detect_pii_in_text__mutmut_3, 
    'x__detect_pii_in_text__mutmut_4': x__detect_pii_in_text__mutmut_4, 
    'x__detect_pii_in_text__mutmut_5': x__detect_pii_in_text__mutmut_5, 
    'x__detect_pii_in_text__mutmut_6': x__detect_pii_in_text__mutmut_6, 
    'x__detect_pii_in_text__mutmut_7': x__detect_pii_in_text__mutmut_7, 
    'x__detect_pii_in_text__mutmut_8': x__detect_pii_in_text__mutmut_8, 
    'x__detect_pii_in_text__mutmut_9': x__detect_pii_in_text__mutmut_9, 
    'x__detect_pii_in_text__mutmut_10': x__detect_pii_in_text__mutmut_10, 
    'x__detect_pii_in_text__mutmut_11': x__detect_pii_in_text__mutmut_11, 
    'x__detect_pii_in_text__mutmut_12': x__detect_pii_in_text__mutmut_12, 
    'x__detect_pii_in_text__mutmut_13': x__detect_pii_in_text__mutmut_13, 
    'x__detect_pii_in_text__mutmut_14': x__detect_pii_in_text__mutmut_14, 
    'x__detect_pii_in_text__mutmut_15': x__detect_pii_in_text__mutmut_15, 
    'x__detect_pii_in_text__mutmut_16': x__detect_pii_in_text__mutmut_16, 
    'x__detect_pii_in_text__mutmut_17': x__detect_pii_in_text__mutmut_17, 
    'x__detect_pii_in_text__mutmut_18': x__detect_pii_in_text__mutmut_18, 
    'x__detect_pii_in_text__mutmut_19': x__detect_pii_in_text__mutmut_19, 
    'x__detect_pii_in_text__mutmut_20': x__detect_pii_in_text__mutmut_20, 
    'x__detect_pii_in_text__mutmut_21': x__detect_pii_in_text__mutmut_21, 
    'x__detect_pii_in_text__mutmut_22': x__detect_pii_in_text__mutmut_22, 
    'x__detect_pii_in_text__mutmut_23': x__detect_pii_in_text__mutmut_23, 
    'x__detect_pii_in_text__mutmut_24': x__detect_pii_in_text__mutmut_24, 
    'x__detect_pii_in_text__mutmut_25': x__detect_pii_in_text__mutmut_25, 
    'x__detect_pii_in_text__mutmut_26': x__detect_pii_in_text__mutmut_26, 
    'x__detect_pii_in_text__mutmut_27': x__detect_pii_in_text__mutmut_27, 
    'x__detect_pii_in_text__mutmut_28': x__detect_pii_in_text__mutmut_28, 
    'x__detect_pii_in_text__mutmut_29': x__detect_pii_in_text__mutmut_29, 
    'x__detect_pii_in_text__mutmut_30': x__detect_pii_in_text__mutmut_30, 
    'x__detect_pii_in_text__mutmut_31': x__detect_pii_in_text__mutmut_31, 
    'x__detect_pii_in_text__mutmut_32': x__detect_pii_in_text__mutmut_32, 
    'x__detect_pii_in_text__mutmut_33': x__detect_pii_in_text__mutmut_33
}
x__detect_pii_in_text__mutmut_orig.__name__ = 'x__detect_pii_in_text'


def check_output_pii(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    args = [output, input_pii]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_output_pii__mutmut_orig, x_check_output_pii__mutmut_mutants, args, kwargs, None)


def x_check_output_pii__mutmut_orig(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_1(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_2(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=None, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_3(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate=None, reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_4(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason=None)
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_5(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_6(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_7(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", )
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_8(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=False, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_9(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="XXpiiXX", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_10(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="PII", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_11(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="XXEmpty outputXX")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_12(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_13(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="EMPTY OUTPUT")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_14(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = None
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_15(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(None)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_16(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = None
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_17(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = None
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_18(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["XXtextXX"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_19(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["TEXT"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_20(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_21(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=None,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_22(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate=None,
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_23(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=None,
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_24(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details=None,
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_25(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_26(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_27(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_28(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_29(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=True,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_30(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="XXpiiXX",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_31(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="PII",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_32(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(None)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_33(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {'XX, XX'.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_34(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['XXentity_typeXX'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_35(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['ENTITY_TYPE'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_36(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"XXfound_entitiesXX": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_37(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"FOUND_ENTITIES": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_38(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "XXnew_entitiesXX": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_39(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "NEW_ENTITIES": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_40(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=None,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_41(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate=None,
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_42(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason=None,
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_43(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details=None,
    )


def x_check_output_pii__mutmut_44(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_45(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_46(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_47(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        )


def x_check_output_pii__mutmut_48(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=False,
        gate="pii",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_49(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="XXpiiXX",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_50(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="PII",
        reason="No new PII detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_51(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="XXNo new PII detectedXX",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_52(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="no new pii detected",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_53(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="NO NEW PII DETECTED",
        details={"new_entities": []},
    )


def x_check_output_pii__mutmut_54(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"XXnew_entitiesXX": []},
    )


def x_check_output_pii__mutmut_55(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
    if not output:
        return ValidationResult(passed=True, gate="pii", reason="Empty output")
    output_entities = _detect_pii_in_text(output)
    input_texts = {e.text for e in input_pii}
    new_entities = [e for e in output_entities if e["text"] not in input_texts]
    if new_entities:
        return ValidationResult(
            passed=False,
            gate="pii",
            reason=f"New PII detected in output: {', '.join(e['entity_type'] for e in new_entities)}",
            details={"found_entities": new_entities, "new_entities": new_entities},
        )
    return ValidationResult(
        passed=True,
        gate="pii",
        reason="No new PII detected",
        details={"NEW_ENTITIES": []},
    )

x_check_output_pii__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_check_output_pii__mutmut_1': x_check_output_pii__mutmut_1, 
    'x_check_output_pii__mutmut_2': x_check_output_pii__mutmut_2, 
    'x_check_output_pii__mutmut_3': x_check_output_pii__mutmut_3, 
    'x_check_output_pii__mutmut_4': x_check_output_pii__mutmut_4, 
    'x_check_output_pii__mutmut_5': x_check_output_pii__mutmut_5, 
    'x_check_output_pii__mutmut_6': x_check_output_pii__mutmut_6, 
    'x_check_output_pii__mutmut_7': x_check_output_pii__mutmut_7, 
    'x_check_output_pii__mutmut_8': x_check_output_pii__mutmut_8, 
    'x_check_output_pii__mutmut_9': x_check_output_pii__mutmut_9, 
    'x_check_output_pii__mutmut_10': x_check_output_pii__mutmut_10, 
    'x_check_output_pii__mutmut_11': x_check_output_pii__mutmut_11, 
    'x_check_output_pii__mutmut_12': x_check_output_pii__mutmut_12, 
    'x_check_output_pii__mutmut_13': x_check_output_pii__mutmut_13, 
    'x_check_output_pii__mutmut_14': x_check_output_pii__mutmut_14, 
    'x_check_output_pii__mutmut_15': x_check_output_pii__mutmut_15, 
    'x_check_output_pii__mutmut_16': x_check_output_pii__mutmut_16, 
    'x_check_output_pii__mutmut_17': x_check_output_pii__mutmut_17, 
    'x_check_output_pii__mutmut_18': x_check_output_pii__mutmut_18, 
    'x_check_output_pii__mutmut_19': x_check_output_pii__mutmut_19, 
    'x_check_output_pii__mutmut_20': x_check_output_pii__mutmut_20, 
    'x_check_output_pii__mutmut_21': x_check_output_pii__mutmut_21, 
    'x_check_output_pii__mutmut_22': x_check_output_pii__mutmut_22, 
    'x_check_output_pii__mutmut_23': x_check_output_pii__mutmut_23, 
    'x_check_output_pii__mutmut_24': x_check_output_pii__mutmut_24, 
    'x_check_output_pii__mutmut_25': x_check_output_pii__mutmut_25, 
    'x_check_output_pii__mutmut_26': x_check_output_pii__mutmut_26, 
    'x_check_output_pii__mutmut_27': x_check_output_pii__mutmut_27, 
    'x_check_output_pii__mutmut_28': x_check_output_pii__mutmut_28, 
    'x_check_output_pii__mutmut_29': x_check_output_pii__mutmut_29, 
    'x_check_output_pii__mutmut_30': x_check_output_pii__mutmut_30, 
    'x_check_output_pii__mutmut_31': x_check_output_pii__mutmut_31, 
    'x_check_output_pii__mutmut_32': x_check_output_pii__mutmut_32, 
    'x_check_output_pii__mutmut_33': x_check_output_pii__mutmut_33, 
    'x_check_output_pii__mutmut_34': x_check_output_pii__mutmut_34, 
    'x_check_output_pii__mutmut_35': x_check_output_pii__mutmut_35, 
    'x_check_output_pii__mutmut_36': x_check_output_pii__mutmut_36, 
    'x_check_output_pii__mutmut_37': x_check_output_pii__mutmut_37, 
    'x_check_output_pii__mutmut_38': x_check_output_pii__mutmut_38, 
    'x_check_output_pii__mutmut_39': x_check_output_pii__mutmut_39, 
    'x_check_output_pii__mutmut_40': x_check_output_pii__mutmut_40, 
    'x_check_output_pii__mutmut_41': x_check_output_pii__mutmut_41, 
    'x_check_output_pii__mutmut_42': x_check_output_pii__mutmut_42, 
    'x_check_output_pii__mutmut_43': x_check_output_pii__mutmut_43, 
    'x_check_output_pii__mutmut_44': x_check_output_pii__mutmut_44, 
    'x_check_output_pii__mutmut_45': x_check_output_pii__mutmut_45, 
    'x_check_output_pii__mutmut_46': x_check_output_pii__mutmut_46, 
    'x_check_output_pii__mutmut_47': x_check_output_pii__mutmut_47, 
    'x_check_output_pii__mutmut_48': x_check_output_pii__mutmut_48, 
    'x_check_output_pii__mutmut_49': x_check_output_pii__mutmut_49, 
    'x_check_output_pii__mutmut_50': x_check_output_pii__mutmut_50, 
    'x_check_output_pii__mutmut_51': x_check_output_pii__mutmut_51, 
    'x_check_output_pii__mutmut_52': x_check_output_pii__mutmut_52, 
    'x_check_output_pii__mutmut_53': x_check_output_pii__mutmut_53, 
    'x_check_output_pii__mutmut_54': x_check_output_pii__mutmut_54, 
    'x_check_output_pii__mutmut_55': x_check_output_pii__mutmut_55
}
x_check_output_pii__mutmut_orig.__name__ = 'x_check_output_pii'


def validate_schema(output: str, schema: dict | None) -> ValidationResult:
    args = [output, schema]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_validate_schema__mutmut_orig, x_validate_schema__mutmut_mutants, args, kwargs, None)


def x_validate_schema__mutmut_orig(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_1(output: str, schema: dict | None) -> ValidationResult:
    if schema is not None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_2(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=None, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_3(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate=None, reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_4(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason=None)
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_5(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_6(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_7(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", )
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_8(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=False, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_9(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="XXschemaXX", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_10(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="SCHEMA", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_11(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="XXNo schema to validate againstXX")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_12(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="no schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_13(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="NO SCHEMA TO VALIDATE AGAINST")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_14(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = None
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_15(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(None)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_16(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=None, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_17(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate=None, reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_18(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason=None)
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_19(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_20(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_21(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", )
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_22(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=True, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_23(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="XXschemaXX", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_24(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="SCHEMA", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_25(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="XXInvalid JSON outputXX")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_26(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="invalid json output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_27(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="INVALID JSON OUTPUT")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_28(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_29(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=None, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_30(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate=None, reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_31(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason=None)
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_32(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_33(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_34(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", )
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_35(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=False, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_36(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="XXschemaXX", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_37(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="SCHEMA", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_38(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="XXSchema is not a dictXX")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_39(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_40(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="SCHEMA IS NOT A DICT")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_41(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = None
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_42(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get(None, [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_43(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", None)
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_44(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get([])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_45(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", )
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_46(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("XXrequiredXX", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_47(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("REQUIRED", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_48(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_49(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=None,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_50(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate=None,
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_51(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=None,
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_52(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_53(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_54(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_55(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=True,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_56(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="XXschemaXX",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_57(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="SCHEMA",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_58(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = None
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_59(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get(None, {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_60(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", None)
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_61(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get({})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_62(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", )
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_63(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("XXpropertiesXX", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_64(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("PROPERTIES", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_65(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) or isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_66(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed or isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_67(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key not in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_68(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = None
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_69(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get(None)
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_70(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("XXtypeXX")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_71(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("TYPE")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_72(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type or not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_73(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_74(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(None, expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_75(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], None):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_76(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_77(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], ):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_78(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=None,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_79(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate=None,
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_80(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=None,
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_81(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_82(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_83(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_84(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=True,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_85(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="XXschemaXX",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_86(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="SCHEMA",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_87(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=None, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_88(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate=None, reason="Schema validation passed")


def x_validate_schema__mutmut_89(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason=None)


def x_validate_schema__mutmut_90(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_91(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, reason="Schema validation passed")


def x_validate_schema__mutmut_92(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", )


def x_validate_schema__mutmut_93(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=False, gate="schema", reason="Schema validation passed")


def x_validate_schema__mutmut_94(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="XXschemaXX", reason="Schema validation passed")


def x_validate_schema__mutmut_95(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="SCHEMA", reason="Schema validation passed")


def x_validate_schema__mutmut_96(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="XXSchema validation passedXX")


def x_validate_schema__mutmut_97(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="schema validation passed")


def x_validate_schema__mutmut_98(output: str, schema: dict | None) -> ValidationResult:
    if schema is None:
        return ValidationResult(passed=True, gate="schema", reason="No schema to validate against")
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return ValidationResult(passed=False, gate="schema", reason="Invalid JSON output")
    if not isinstance(schema, dict):
        return ValidationResult(passed=True, gate="schema", reason="Schema is not a dict")
    required = schema.get("required", [])
    if isinstance(parsed, dict):
        for field_name in required:
            if field_name not in parsed:
                return ValidationResult(
                    passed=False,
                    gate="schema",
                    reason=f"Missing required field: {field_name}",
                )
    props = schema.get("properties", {})
    if isinstance(parsed, dict) and isinstance(props, dict):
        for key, prop_def in props.items():
            if key in parsed and isinstance(prop_def, dict):
                expected_type = prop_def.get("type")
                if expected_type and not _type_matches(parsed[key], expected_type):
                    return ValidationResult(
                        passed=False,
                        gate="schema",
                        reason=f"Field '{key}' has wrong type",
                    )
    return ValidationResult(passed=True, gate="schema", reason="SCHEMA VALIDATION PASSED")

x_validate_schema__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_validate_schema__mutmut_1': x_validate_schema__mutmut_1, 
    'x_validate_schema__mutmut_2': x_validate_schema__mutmut_2, 
    'x_validate_schema__mutmut_3': x_validate_schema__mutmut_3, 
    'x_validate_schema__mutmut_4': x_validate_schema__mutmut_4, 
    'x_validate_schema__mutmut_5': x_validate_schema__mutmut_5, 
    'x_validate_schema__mutmut_6': x_validate_schema__mutmut_6, 
    'x_validate_schema__mutmut_7': x_validate_schema__mutmut_7, 
    'x_validate_schema__mutmut_8': x_validate_schema__mutmut_8, 
    'x_validate_schema__mutmut_9': x_validate_schema__mutmut_9, 
    'x_validate_schema__mutmut_10': x_validate_schema__mutmut_10, 
    'x_validate_schema__mutmut_11': x_validate_schema__mutmut_11, 
    'x_validate_schema__mutmut_12': x_validate_schema__mutmut_12, 
    'x_validate_schema__mutmut_13': x_validate_schema__mutmut_13, 
    'x_validate_schema__mutmut_14': x_validate_schema__mutmut_14, 
    'x_validate_schema__mutmut_15': x_validate_schema__mutmut_15, 
    'x_validate_schema__mutmut_16': x_validate_schema__mutmut_16, 
    'x_validate_schema__mutmut_17': x_validate_schema__mutmut_17, 
    'x_validate_schema__mutmut_18': x_validate_schema__mutmut_18, 
    'x_validate_schema__mutmut_19': x_validate_schema__mutmut_19, 
    'x_validate_schema__mutmut_20': x_validate_schema__mutmut_20, 
    'x_validate_schema__mutmut_21': x_validate_schema__mutmut_21, 
    'x_validate_schema__mutmut_22': x_validate_schema__mutmut_22, 
    'x_validate_schema__mutmut_23': x_validate_schema__mutmut_23, 
    'x_validate_schema__mutmut_24': x_validate_schema__mutmut_24, 
    'x_validate_schema__mutmut_25': x_validate_schema__mutmut_25, 
    'x_validate_schema__mutmut_26': x_validate_schema__mutmut_26, 
    'x_validate_schema__mutmut_27': x_validate_schema__mutmut_27, 
    'x_validate_schema__mutmut_28': x_validate_schema__mutmut_28, 
    'x_validate_schema__mutmut_29': x_validate_schema__mutmut_29, 
    'x_validate_schema__mutmut_30': x_validate_schema__mutmut_30, 
    'x_validate_schema__mutmut_31': x_validate_schema__mutmut_31, 
    'x_validate_schema__mutmut_32': x_validate_schema__mutmut_32, 
    'x_validate_schema__mutmut_33': x_validate_schema__mutmut_33, 
    'x_validate_schema__mutmut_34': x_validate_schema__mutmut_34, 
    'x_validate_schema__mutmut_35': x_validate_schema__mutmut_35, 
    'x_validate_schema__mutmut_36': x_validate_schema__mutmut_36, 
    'x_validate_schema__mutmut_37': x_validate_schema__mutmut_37, 
    'x_validate_schema__mutmut_38': x_validate_schema__mutmut_38, 
    'x_validate_schema__mutmut_39': x_validate_schema__mutmut_39, 
    'x_validate_schema__mutmut_40': x_validate_schema__mutmut_40, 
    'x_validate_schema__mutmut_41': x_validate_schema__mutmut_41, 
    'x_validate_schema__mutmut_42': x_validate_schema__mutmut_42, 
    'x_validate_schema__mutmut_43': x_validate_schema__mutmut_43, 
    'x_validate_schema__mutmut_44': x_validate_schema__mutmut_44, 
    'x_validate_schema__mutmut_45': x_validate_schema__mutmut_45, 
    'x_validate_schema__mutmut_46': x_validate_schema__mutmut_46, 
    'x_validate_schema__mutmut_47': x_validate_schema__mutmut_47, 
    'x_validate_schema__mutmut_48': x_validate_schema__mutmut_48, 
    'x_validate_schema__mutmut_49': x_validate_schema__mutmut_49, 
    'x_validate_schema__mutmut_50': x_validate_schema__mutmut_50, 
    'x_validate_schema__mutmut_51': x_validate_schema__mutmut_51, 
    'x_validate_schema__mutmut_52': x_validate_schema__mutmut_52, 
    'x_validate_schema__mutmut_53': x_validate_schema__mutmut_53, 
    'x_validate_schema__mutmut_54': x_validate_schema__mutmut_54, 
    'x_validate_schema__mutmut_55': x_validate_schema__mutmut_55, 
    'x_validate_schema__mutmut_56': x_validate_schema__mutmut_56, 
    'x_validate_schema__mutmut_57': x_validate_schema__mutmut_57, 
    'x_validate_schema__mutmut_58': x_validate_schema__mutmut_58, 
    'x_validate_schema__mutmut_59': x_validate_schema__mutmut_59, 
    'x_validate_schema__mutmut_60': x_validate_schema__mutmut_60, 
    'x_validate_schema__mutmut_61': x_validate_schema__mutmut_61, 
    'x_validate_schema__mutmut_62': x_validate_schema__mutmut_62, 
    'x_validate_schema__mutmut_63': x_validate_schema__mutmut_63, 
    'x_validate_schema__mutmut_64': x_validate_schema__mutmut_64, 
    'x_validate_schema__mutmut_65': x_validate_schema__mutmut_65, 
    'x_validate_schema__mutmut_66': x_validate_schema__mutmut_66, 
    'x_validate_schema__mutmut_67': x_validate_schema__mutmut_67, 
    'x_validate_schema__mutmut_68': x_validate_schema__mutmut_68, 
    'x_validate_schema__mutmut_69': x_validate_schema__mutmut_69, 
    'x_validate_schema__mutmut_70': x_validate_schema__mutmut_70, 
    'x_validate_schema__mutmut_71': x_validate_schema__mutmut_71, 
    'x_validate_schema__mutmut_72': x_validate_schema__mutmut_72, 
    'x_validate_schema__mutmut_73': x_validate_schema__mutmut_73, 
    'x_validate_schema__mutmut_74': x_validate_schema__mutmut_74, 
    'x_validate_schema__mutmut_75': x_validate_schema__mutmut_75, 
    'x_validate_schema__mutmut_76': x_validate_schema__mutmut_76, 
    'x_validate_schema__mutmut_77': x_validate_schema__mutmut_77, 
    'x_validate_schema__mutmut_78': x_validate_schema__mutmut_78, 
    'x_validate_schema__mutmut_79': x_validate_schema__mutmut_79, 
    'x_validate_schema__mutmut_80': x_validate_schema__mutmut_80, 
    'x_validate_schema__mutmut_81': x_validate_schema__mutmut_81, 
    'x_validate_schema__mutmut_82': x_validate_schema__mutmut_82, 
    'x_validate_schema__mutmut_83': x_validate_schema__mutmut_83, 
    'x_validate_schema__mutmut_84': x_validate_schema__mutmut_84, 
    'x_validate_schema__mutmut_85': x_validate_schema__mutmut_85, 
    'x_validate_schema__mutmut_86': x_validate_schema__mutmut_86, 
    'x_validate_schema__mutmut_87': x_validate_schema__mutmut_87, 
    'x_validate_schema__mutmut_88': x_validate_schema__mutmut_88, 
    'x_validate_schema__mutmut_89': x_validate_schema__mutmut_89, 
    'x_validate_schema__mutmut_90': x_validate_schema__mutmut_90, 
    'x_validate_schema__mutmut_91': x_validate_schema__mutmut_91, 
    'x_validate_schema__mutmut_92': x_validate_schema__mutmut_92, 
    'x_validate_schema__mutmut_93': x_validate_schema__mutmut_93, 
    'x_validate_schema__mutmut_94': x_validate_schema__mutmut_94, 
    'x_validate_schema__mutmut_95': x_validate_schema__mutmut_95, 
    'x_validate_schema__mutmut_96': x_validate_schema__mutmut_96, 
    'x_validate_schema__mutmut_97': x_validate_schema__mutmut_97, 
    'x_validate_schema__mutmut_98': x_validate_schema__mutmut_98
}
x_validate_schema__mutmut_orig.__name__ = 'x_validate_schema'


def _type_matches(value, expected_type: str) -> bool:
    args = [value, expected_type]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x__type_matches__mutmut_orig, x__type_matches__mutmut_mutants, args, kwargs, None)


def x__type_matches__mutmut_orig(value, expected_type: str) -> bool:
    type_map = {
        "string": str,
        "integer": int,
        "number": (int, float),
        "boolean": bool,
        "array": list,
        "object": dict,
    }
    expected = type_map.get(expected_type)
    if expected is None:
        return True
    return isinstance(value, expected)


def x__type_matches__mutmut_1(value, expected_type: str) -> bool:
    type_map = None
    expected = type_map.get(expected_type)
    if expected is None:
        return True
    return isinstance(value, expected)


def x__type_matches__mutmut_2(value, expected_type: str) -> bool:
    type_map = {
        "XXstringXX": str,
        "integer": int,
        "number": (int, float),
        "boolean": bool,
        "array": list,
        "object": dict,
    }
    expected = type_map.get(expected_type)
    if expected is None:
        return True
    return isinstance(value, expected)


def x__type_matches__mutmut_3(value, expected_type: str) -> bool:
    type_map = {
        "STRING": str,
        "integer": int,
        "number": (int, float),
        "boolean": bool,
        "array": list,
        "object": dict,
    }
    expected = type_map.get(expected_type)
    if expected is None:
        return True
    return isinstance(value, expected)


def x__type_matches__mutmut_4(value, expected_type: str) -> bool:
    type_map = {
        "string": str,
        "XXintegerXX": int,
        "number": (int, float),
        "boolean": bool,
        "array": list,
        "object": dict,
    }
    expected = type_map.get(expected_type)
    if expected is None:
        return True
    return isinstance(value, expected)


def x__type_matches__mutmut_5(value, expected_type: str) -> bool:
    type_map = {
        "string": str,
        "INTEGER": int,
        "number": (int, float),
        "boolean": bool,
        "array": list,
        "object": dict,
    }
    expected = type_map.get(expected_type)
    if expected is None:
        return True
    return isinstance(value, expected)


def x__type_matches__mutmut_6(value, expected_type: str) -> bool:
    type_map = {
        "string": str,
        "integer": int,
        "XXnumberXX": (int, float),
        "boolean": bool,
        "array": list,
        "object": dict,
    }
    expected = type_map.get(expected_type)
    if expected is None:
        return True
    return isinstance(value, expected)


def x__type_matches__mutmut_7(value, expected_type: str) -> bool:
    type_map = {
        "string": str,
        "integer": int,
        "NUMBER": (int, float),
        "boolean": bool,
        "array": list,
        "object": dict,
    }
    expected = type_map.get(expected_type)
    if expected is None:
        return True
    return isinstance(value, expected)


def x__type_matches__mutmut_8(value, expected_type: str) -> bool:
    type_map = {
        "string": str,
        "integer": int,
        "number": (int, float),
        "XXbooleanXX": bool,
        "array": list,
        "object": dict,
    }
    expected = type_map.get(expected_type)
    if expected is None:
        return True
    return isinstance(value, expected)


def x__type_matches__mutmut_9(value, expected_type: str) -> bool:
    type_map = {
        "string": str,
        "integer": int,
        "number": (int, float),
        "BOOLEAN": bool,
        "array": list,
        "object": dict,
    }
    expected = type_map.get(expected_type)
    if expected is None:
        return True
    return isinstance(value, expected)


def x__type_matches__mutmut_10(value, expected_type: str) -> bool:
    type_map = {
        "string": str,
        "integer": int,
        "number": (int, float),
        "boolean": bool,
        "XXarrayXX": list,
        "object": dict,
    }
    expected = type_map.get(expected_type)
    if expected is None:
        return True
    return isinstance(value, expected)


def x__type_matches__mutmut_11(value, expected_type: str) -> bool:
    type_map = {
        "string": str,
        "integer": int,
        "number": (int, float),
        "boolean": bool,
        "ARRAY": list,
        "object": dict,
    }
    expected = type_map.get(expected_type)
    if expected is None:
        return True
    return isinstance(value, expected)


def x__type_matches__mutmut_12(value, expected_type: str) -> bool:
    type_map = {
        "string": str,
        "integer": int,
        "number": (int, float),
        "boolean": bool,
        "array": list,
        "XXobjectXX": dict,
    }
    expected = type_map.get(expected_type)
    if expected is None:
        return True
    return isinstance(value, expected)


def x__type_matches__mutmut_13(value, expected_type: str) -> bool:
    type_map = {
        "string": str,
        "integer": int,
        "number": (int, float),
        "boolean": bool,
        "array": list,
        "OBJECT": dict,
    }
    expected = type_map.get(expected_type)
    if expected is None:
        return True
    return isinstance(value, expected)


def x__type_matches__mutmut_14(value, expected_type: str) -> bool:
    type_map = {
        "string": str,
        "integer": int,
        "number": (int, float),
        "boolean": bool,
        "array": list,
        "object": dict,
    }
    expected = None
    if expected is None:
        return True
    return isinstance(value, expected)


def x__type_matches__mutmut_15(value, expected_type: str) -> bool:
    type_map = {
        "string": str,
        "integer": int,
        "number": (int, float),
        "boolean": bool,
        "array": list,
        "object": dict,
    }
    expected = type_map.get(None)
    if expected is None:
        return True
    return isinstance(value, expected)


def x__type_matches__mutmut_16(value, expected_type: str) -> bool:
    type_map = {
        "string": str,
        "integer": int,
        "number": (int, float),
        "boolean": bool,
        "array": list,
        "object": dict,
    }
    expected = type_map.get(expected_type)
    if expected is not None:
        return True
    return isinstance(value, expected)


def x__type_matches__mutmut_17(value, expected_type: str) -> bool:
    type_map = {
        "string": str,
        "integer": int,
        "number": (int, float),
        "boolean": bool,
        "array": list,
        "object": dict,
    }
    expected = type_map.get(expected_type)
    if expected is None:
        return False
    return isinstance(value, expected)

x__type_matches__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x__type_matches__mutmut_1': x__type_matches__mutmut_1, 
    'x__type_matches__mutmut_2': x__type_matches__mutmut_2, 
    'x__type_matches__mutmut_3': x__type_matches__mutmut_3, 
    'x__type_matches__mutmut_4': x__type_matches__mutmut_4, 
    'x__type_matches__mutmut_5': x__type_matches__mutmut_5, 
    'x__type_matches__mutmut_6': x__type_matches__mutmut_6, 
    'x__type_matches__mutmut_7': x__type_matches__mutmut_7, 
    'x__type_matches__mutmut_8': x__type_matches__mutmut_8, 
    'x__type_matches__mutmut_9': x__type_matches__mutmut_9, 
    'x__type_matches__mutmut_10': x__type_matches__mutmut_10, 
    'x__type_matches__mutmut_11': x__type_matches__mutmut_11, 
    'x__type_matches__mutmut_12': x__type_matches__mutmut_12, 
    'x__type_matches__mutmut_13': x__type_matches__mutmut_13, 
    'x__type_matches__mutmut_14': x__type_matches__mutmut_14, 
    'x__type_matches__mutmut_15': x__type_matches__mutmut_15, 
    'x__type_matches__mutmut_16': x__type_matches__mutmut_16, 
    'x__type_matches__mutmut_17': x__type_matches__mutmut_17
}
x__type_matches__mutmut_orig.__name__ = 'x__type_matches'


def check_injection_patterns(output: str) -> ValidationResult:
    args = [output]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_injection_patterns__mutmut_orig, x_check_injection_patterns__mutmut_mutants, args, kwargs, None)


def x_check_injection_patterns__mutmut_orig(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_1(output: str) -> ValidationResult:
    matched_patterns: list[str] = None
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_2(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(None):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_3(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = None
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_4(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["XXSYSTEM:XX", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_5(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["system:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_6(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "XXsystem:XX"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_7(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "SYSTEM:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_8(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate not in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_9(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(None)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_10(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    return
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_11(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(None)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_12(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=None,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_13(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate=None,
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_14(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=None,
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_15(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details=None,
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_16(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_17(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_18(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_19(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_20(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=True,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_21(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="XXinjectionXX",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_22(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="INJECTION",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_23(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"XXpatternsXX": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_24(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"PATTERNS": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_25(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "XXconfidenceXX": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_26(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "CONFIDENCE": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_27(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 1.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_28(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=None,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_29(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate=None,
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_30(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason=None,
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_31(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details=None,
    )


def x_check_injection_patterns__mutmut_32(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_33(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_34(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_35(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        )


def x_check_injection_patterns__mutmut_36(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=False,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_37(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="XXinjectionXX",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_38(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="INJECTION",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_39(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="XXNo injection patterns detectedXX",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_40(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="no injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_41(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="NO INJECTION PATTERNS DETECTED",
        details={"patterns": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_42(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"XXpatternsXX": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_43(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"PATTERNS": [], "confidence": 0.0},
    )


def x_check_injection_patterns__mutmut_44(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "XXconfidenceXX": 0.0},
    )


def x_check_injection_patterns__mutmut_45(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "CONFIDENCE": 0.0},
    )


def x_check_injection_patterns__mutmut_46(output: str) -> ValidationResult:
    matched_patterns: list[str] = []
    for pattern in _INJECTION_OUTPUT_PATTERNS:
        if pattern.search(output):
            pat_str = pattern.pattern
            for candidate in ["SYSTEM:", "system:"]:
                if candidate in pat_str:
                    matched_patterns.append(candidate)
                    break
            else:
                matched_patterns.append(pat_str)
    if matched_patterns:
        return ValidationResult(
            passed=False,
            gate="injection",
            reason=f"Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 1.0},
    )

x_check_injection_patterns__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_check_injection_patterns__mutmut_1': x_check_injection_patterns__mutmut_1, 
    'x_check_injection_patterns__mutmut_2': x_check_injection_patterns__mutmut_2, 
    'x_check_injection_patterns__mutmut_3': x_check_injection_patterns__mutmut_3, 
    'x_check_injection_patterns__mutmut_4': x_check_injection_patterns__mutmut_4, 
    'x_check_injection_patterns__mutmut_5': x_check_injection_patterns__mutmut_5, 
    'x_check_injection_patterns__mutmut_6': x_check_injection_patterns__mutmut_6, 
    'x_check_injection_patterns__mutmut_7': x_check_injection_patterns__mutmut_7, 
    'x_check_injection_patterns__mutmut_8': x_check_injection_patterns__mutmut_8, 
    'x_check_injection_patterns__mutmut_9': x_check_injection_patterns__mutmut_9, 
    'x_check_injection_patterns__mutmut_10': x_check_injection_patterns__mutmut_10, 
    'x_check_injection_patterns__mutmut_11': x_check_injection_patterns__mutmut_11, 
    'x_check_injection_patterns__mutmut_12': x_check_injection_patterns__mutmut_12, 
    'x_check_injection_patterns__mutmut_13': x_check_injection_patterns__mutmut_13, 
    'x_check_injection_patterns__mutmut_14': x_check_injection_patterns__mutmut_14, 
    'x_check_injection_patterns__mutmut_15': x_check_injection_patterns__mutmut_15, 
    'x_check_injection_patterns__mutmut_16': x_check_injection_patterns__mutmut_16, 
    'x_check_injection_patterns__mutmut_17': x_check_injection_patterns__mutmut_17, 
    'x_check_injection_patterns__mutmut_18': x_check_injection_patterns__mutmut_18, 
    'x_check_injection_patterns__mutmut_19': x_check_injection_patterns__mutmut_19, 
    'x_check_injection_patterns__mutmut_20': x_check_injection_patterns__mutmut_20, 
    'x_check_injection_patterns__mutmut_21': x_check_injection_patterns__mutmut_21, 
    'x_check_injection_patterns__mutmut_22': x_check_injection_patterns__mutmut_22, 
    'x_check_injection_patterns__mutmut_23': x_check_injection_patterns__mutmut_23, 
    'x_check_injection_patterns__mutmut_24': x_check_injection_patterns__mutmut_24, 
    'x_check_injection_patterns__mutmut_25': x_check_injection_patterns__mutmut_25, 
    'x_check_injection_patterns__mutmut_26': x_check_injection_patterns__mutmut_26, 
    'x_check_injection_patterns__mutmut_27': x_check_injection_patterns__mutmut_27, 
    'x_check_injection_patterns__mutmut_28': x_check_injection_patterns__mutmut_28, 
    'x_check_injection_patterns__mutmut_29': x_check_injection_patterns__mutmut_29, 
    'x_check_injection_patterns__mutmut_30': x_check_injection_patterns__mutmut_30, 
    'x_check_injection_patterns__mutmut_31': x_check_injection_patterns__mutmut_31, 
    'x_check_injection_patterns__mutmut_32': x_check_injection_patterns__mutmut_32, 
    'x_check_injection_patterns__mutmut_33': x_check_injection_patterns__mutmut_33, 
    'x_check_injection_patterns__mutmut_34': x_check_injection_patterns__mutmut_34, 
    'x_check_injection_patterns__mutmut_35': x_check_injection_patterns__mutmut_35, 
    'x_check_injection_patterns__mutmut_36': x_check_injection_patterns__mutmut_36, 
    'x_check_injection_patterns__mutmut_37': x_check_injection_patterns__mutmut_37, 
    'x_check_injection_patterns__mutmut_38': x_check_injection_patterns__mutmut_38, 
    'x_check_injection_patterns__mutmut_39': x_check_injection_patterns__mutmut_39, 
    'x_check_injection_patterns__mutmut_40': x_check_injection_patterns__mutmut_40, 
    'x_check_injection_patterns__mutmut_41': x_check_injection_patterns__mutmut_41, 
    'x_check_injection_patterns__mutmut_42': x_check_injection_patterns__mutmut_42, 
    'x_check_injection_patterns__mutmut_43': x_check_injection_patterns__mutmut_43, 
    'x_check_injection_patterns__mutmut_44': x_check_injection_patterns__mutmut_44, 
    'x_check_injection_patterns__mutmut_45': x_check_injection_patterns__mutmut_45, 
    'x_check_injection_patterns__mutmut_46': x_check_injection_patterns__mutmut_46
}
x_check_injection_patterns__mutmut_orig.__name__ = 'x_check_injection_patterns'


def validate_for_downstream(output: str, target: str) -> ValidationResult:
    args = [output, target]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_validate_for_downstream__mutmut_orig, x_validate_for_downstream__mutmut_mutants, args, kwargs, None)


def x_validate_for_downstream__mutmut_orig(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_1(output: str, target: str) -> ValidationResult:
    if target != "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_2(output: str, target: str) -> ValidationResult:
    if target == "XXshellXX":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_3(output: str, target: str) -> ValidationResult:
    if target == "SHELL":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_4(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(None):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_5(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=None,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_6(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate=None,
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_7(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason=None,
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_8(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details=None,
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_9(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_10(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_11(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_12(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_13(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=True,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_14(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="XXdownstreamXX",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_15(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="DOWNSTREAM",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_16(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="XXDangerous shell command detectedXX",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_17(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_18(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="DANGEROUS SHELL COMMAND DETECTED",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_19(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"XXtargetXX": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_20(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"TARGET": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_21(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target != "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_22(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "XXdatabaseXX":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_23(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "DATABASE":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_24(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(None):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_25(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=None,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_26(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate=None,
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_27(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason=None,
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_28(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details=None,
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_29(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_30(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_31(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_32(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_33(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=True,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_34(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="XXdownstreamXX",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_35(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="DOWNSTREAM",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_36(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="XXSQL injection pattern detectedXX",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_37(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="sql injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_38(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL INJECTION PATTERN DETECTED",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_39(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"XXtargetXX": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_40(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"TARGET": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_41(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=None, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_42(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate=None, reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_43(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason=None, details={"target": target}
    )


def x_validate_for_downstream__mutmut_44(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details=None
    )


def x_validate_for_downstream__mutmut_45(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_46(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_47(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", details={"target": target}
    )


def x_validate_for_downstream__mutmut_48(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", )


def x_validate_for_downstream__mutmut_49(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=False, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_50(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="XXdownstreamXX", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_51(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="DOWNSTREAM", reason="Downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_52(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="XXDownstream validation passedXX", details={"target": target}
    )


def x_validate_for_downstream__mutmut_53(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="downstream validation passed", details={"target": target}
    )


def x_validate_for_downstream__mutmut_54(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="DOWNSTREAM VALIDATION PASSED", details={"target": target}
    )


def x_validate_for_downstream__mutmut_55(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"XXtargetXX": target}
    )


def x_validate_for_downstream__mutmut_56(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database":
        if _SQL_INJECTION.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="SQL injection pattern detected",
                details={"target": target},
            )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"TARGET": target}
    )

x_validate_for_downstream__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_validate_for_downstream__mutmut_1': x_validate_for_downstream__mutmut_1, 
    'x_validate_for_downstream__mutmut_2': x_validate_for_downstream__mutmut_2, 
    'x_validate_for_downstream__mutmut_3': x_validate_for_downstream__mutmut_3, 
    'x_validate_for_downstream__mutmut_4': x_validate_for_downstream__mutmut_4, 
    'x_validate_for_downstream__mutmut_5': x_validate_for_downstream__mutmut_5, 
    'x_validate_for_downstream__mutmut_6': x_validate_for_downstream__mutmut_6, 
    'x_validate_for_downstream__mutmut_7': x_validate_for_downstream__mutmut_7, 
    'x_validate_for_downstream__mutmut_8': x_validate_for_downstream__mutmut_8, 
    'x_validate_for_downstream__mutmut_9': x_validate_for_downstream__mutmut_9, 
    'x_validate_for_downstream__mutmut_10': x_validate_for_downstream__mutmut_10, 
    'x_validate_for_downstream__mutmut_11': x_validate_for_downstream__mutmut_11, 
    'x_validate_for_downstream__mutmut_12': x_validate_for_downstream__mutmut_12, 
    'x_validate_for_downstream__mutmut_13': x_validate_for_downstream__mutmut_13, 
    'x_validate_for_downstream__mutmut_14': x_validate_for_downstream__mutmut_14, 
    'x_validate_for_downstream__mutmut_15': x_validate_for_downstream__mutmut_15, 
    'x_validate_for_downstream__mutmut_16': x_validate_for_downstream__mutmut_16, 
    'x_validate_for_downstream__mutmut_17': x_validate_for_downstream__mutmut_17, 
    'x_validate_for_downstream__mutmut_18': x_validate_for_downstream__mutmut_18, 
    'x_validate_for_downstream__mutmut_19': x_validate_for_downstream__mutmut_19, 
    'x_validate_for_downstream__mutmut_20': x_validate_for_downstream__mutmut_20, 
    'x_validate_for_downstream__mutmut_21': x_validate_for_downstream__mutmut_21, 
    'x_validate_for_downstream__mutmut_22': x_validate_for_downstream__mutmut_22, 
    'x_validate_for_downstream__mutmut_23': x_validate_for_downstream__mutmut_23, 
    'x_validate_for_downstream__mutmut_24': x_validate_for_downstream__mutmut_24, 
    'x_validate_for_downstream__mutmut_25': x_validate_for_downstream__mutmut_25, 
    'x_validate_for_downstream__mutmut_26': x_validate_for_downstream__mutmut_26, 
    'x_validate_for_downstream__mutmut_27': x_validate_for_downstream__mutmut_27, 
    'x_validate_for_downstream__mutmut_28': x_validate_for_downstream__mutmut_28, 
    'x_validate_for_downstream__mutmut_29': x_validate_for_downstream__mutmut_29, 
    'x_validate_for_downstream__mutmut_30': x_validate_for_downstream__mutmut_30, 
    'x_validate_for_downstream__mutmut_31': x_validate_for_downstream__mutmut_31, 
    'x_validate_for_downstream__mutmut_32': x_validate_for_downstream__mutmut_32, 
    'x_validate_for_downstream__mutmut_33': x_validate_for_downstream__mutmut_33, 
    'x_validate_for_downstream__mutmut_34': x_validate_for_downstream__mutmut_34, 
    'x_validate_for_downstream__mutmut_35': x_validate_for_downstream__mutmut_35, 
    'x_validate_for_downstream__mutmut_36': x_validate_for_downstream__mutmut_36, 
    'x_validate_for_downstream__mutmut_37': x_validate_for_downstream__mutmut_37, 
    'x_validate_for_downstream__mutmut_38': x_validate_for_downstream__mutmut_38, 
    'x_validate_for_downstream__mutmut_39': x_validate_for_downstream__mutmut_39, 
    'x_validate_for_downstream__mutmut_40': x_validate_for_downstream__mutmut_40, 
    'x_validate_for_downstream__mutmut_41': x_validate_for_downstream__mutmut_41, 
    'x_validate_for_downstream__mutmut_42': x_validate_for_downstream__mutmut_42, 
    'x_validate_for_downstream__mutmut_43': x_validate_for_downstream__mutmut_43, 
    'x_validate_for_downstream__mutmut_44': x_validate_for_downstream__mutmut_44, 
    'x_validate_for_downstream__mutmut_45': x_validate_for_downstream__mutmut_45, 
    'x_validate_for_downstream__mutmut_46': x_validate_for_downstream__mutmut_46, 
    'x_validate_for_downstream__mutmut_47': x_validate_for_downstream__mutmut_47, 
    'x_validate_for_downstream__mutmut_48': x_validate_for_downstream__mutmut_48, 
    'x_validate_for_downstream__mutmut_49': x_validate_for_downstream__mutmut_49, 
    'x_validate_for_downstream__mutmut_50': x_validate_for_downstream__mutmut_50, 
    'x_validate_for_downstream__mutmut_51': x_validate_for_downstream__mutmut_51, 
    'x_validate_for_downstream__mutmut_52': x_validate_for_downstream__mutmut_52, 
    'x_validate_for_downstream__mutmut_53': x_validate_for_downstream__mutmut_53, 
    'x_validate_for_downstream__mutmut_54': x_validate_for_downstream__mutmut_54, 
    'x_validate_for_downstream__mutmut_55': x_validate_for_downstream__mutmut_55, 
    'x_validate_for_downstream__mutmut_56': x_validate_for_downstream__mutmut_56
}
x_validate_for_downstream__mutmut_orig.__name__ = 'x_validate_for_downstream'


def strip_external_urls(output: str) -> str:
    args = [output]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_strip_external_urls__mutmut_orig, x_strip_external_urls__mutmut_mutants, args, kwargs, None)


def x_strip_external_urls__mutmut_orig(output: str) -> str:
    def _replace_external(match: re.Match) -> str:
        alt_text = match.group(1)
        url = match.group(2)
        if url.startswith("data:"):
            return match.group(0)
        return f"![{alt_text}]([REDACTED_URL])"

    return _EXTERNAL_URL_PATTERN.sub(_replace_external, output)


def x_strip_external_urls__mutmut_1(output: str) -> str:
    def _replace_external(match: re.Match) -> str:
        alt_text = None
        url = match.group(2)
        if url.startswith("data:"):
            return match.group(0)
        return f"![{alt_text}]([REDACTED_URL])"

    return _EXTERNAL_URL_PATTERN.sub(_replace_external, output)


def x_strip_external_urls__mutmut_2(output: str) -> str:
    def _replace_external(match: re.Match) -> str:
        alt_text = match.group(None)
        url = match.group(2)
        if url.startswith("data:"):
            return match.group(0)
        return f"![{alt_text}]([REDACTED_URL])"

    return _EXTERNAL_URL_PATTERN.sub(_replace_external, output)


def x_strip_external_urls__mutmut_3(output: str) -> str:
    def _replace_external(match: re.Match) -> str:
        alt_text = match.group(2)
        url = match.group(2)
        if url.startswith("data:"):
            return match.group(0)
        return f"![{alt_text}]([REDACTED_URL])"

    return _EXTERNAL_URL_PATTERN.sub(_replace_external, output)


def x_strip_external_urls__mutmut_4(output: str) -> str:
    def _replace_external(match: re.Match) -> str:
        alt_text = match.group(1)
        url = None
        if url.startswith("data:"):
            return match.group(0)
        return f"![{alt_text}]([REDACTED_URL])"

    return _EXTERNAL_URL_PATTERN.sub(_replace_external, output)


def x_strip_external_urls__mutmut_5(output: str) -> str:
    def _replace_external(match: re.Match) -> str:
        alt_text = match.group(1)
        url = match.group(None)
        if url.startswith("data:"):
            return match.group(0)
        return f"![{alt_text}]([REDACTED_URL])"

    return _EXTERNAL_URL_PATTERN.sub(_replace_external, output)


def x_strip_external_urls__mutmut_6(output: str) -> str:
    def _replace_external(match: re.Match) -> str:
        alt_text = match.group(1)
        url = match.group(3)
        if url.startswith("data:"):
            return match.group(0)
        return f"![{alt_text}]([REDACTED_URL])"

    return _EXTERNAL_URL_PATTERN.sub(_replace_external, output)


def x_strip_external_urls__mutmut_7(output: str) -> str:
    def _replace_external(match: re.Match) -> str:
        alt_text = match.group(1)
        url = match.group(2)
        if url.startswith(None):
            return match.group(0)
        return f"![{alt_text}]([REDACTED_URL])"

    return _EXTERNAL_URL_PATTERN.sub(_replace_external, output)


def x_strip_external_urls__mutmut_8(output: str) -> str:
    def _replace_external(match: re.Match) -> str:
        alt_text = match.group(1)
        url = match.group(2)
        if url.startswith("XXdata:XX"):
            return match.group(0)
        return f"![{alt_text}]([REDACTED_URL])"

    return _EXTERNAL_URL_PATTERN.sub(_replace_external, output)


def x_strip_external_urls__mutmut_9(output: str) -> str:
    def _replace_external(match: re.Match) -> str:
        alt_text = match.group(1)
        url = match.group(2)
        if url.startswith("DATA:"):
            return match.group(0)
        return f"![{alt_text}]([REDACTED_URL])"

    return _EXTERNAL_URL_PATTERN.sub(_replace_external, output)


def x_strip_external_urls__mutmut_10(output: str) -> str:
    def _replace_external(match: re.Match) -> str:
        alt_text = match.group(1)
        url = match.group(2)
        if url.startswith("data:"):
            return match.group(None)
        return f"![{alt_text}]([REDACTED_URL])"

    return _EXTERNAL_URL_PATTERN.sub(_replace_external, output)


def x_strip_external_urls__mutmut_11(output: str) -> str:
    def _replace_external(match: re.Match) -> str:
        alt_text = match.group(1)
        url = match.group(2)
        if url.startswith("data:"):
            return match.group(1)
        return f"![{alt_text}]([REDACTED_URL])"

    return _EXTERNAL_URL_PATTERN.sub(_replace_external, output)


def x_strip_external_urls__mutmut_12(output: str) -> str:
    def _replace_external(match: re.Match) -> str:
        alt_text = match.group(1)
        url = match.group(2)
        if url.startswith("data:"):
            return match.group(0)
        return f"![{alt_text}]([REDACTED_URL])"

    return _EXTERNAL_URL_PATTERN.sub(None, output)


def x_strip_external_urls__mutmut_13(output: str) -> str:
    def _replace_external(match: re.Match) -> str:
        alt_text = match.group(1)
        url = match.group(2)
        if url.startswith("data:"):
            return match.group(0)
        return f"![{alt_text}]([REDACTED_URL])"

    return _EXTERNAL_URL_PATTERN.sub(_replace_external, None)


def x_strip_external_urls__mutmut_14(output: str) -> str:
    def _replace_external(match: re.Match) -> str:
        alt_text = match.group(1)
        url = match.group(2)
        if url.startswith("data:"):
            return match.group(0)
        return f"![{alt_text}]([REDACTED_URL])"

    return _EXTERNAL_URL_PATTERN.sub(output)


def x_strip_external_urls__mutmut_15(output: str) -> str:
    def _replace_external(match: re.Match) -> str:
        alt_text = match.group(1)
        url = match.group(2)
        if url.startswith("data:"):
            return match.group(0)
        return f"![{alt_text}]([REDACTED_URL])"

    return _EXTERNAL_URL_PATTERN.sub(_replace_external, )

x_strip_external_urls__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_strip_external_urls__mutmut_1': x_strip_external_urls__mutmut_1, 
    'x_strip_external_urls__mutmut_2': x_strip_external_urls__mutmut_2, 
    'x_strip_external_urls__mutmut_3': x_strip_external_urls__mutmut_3, 
    'x_strip_external_urls__mutmut_4': x_strip_external_urls__mutmut_4, 
    'x_strip_external_urls__mutmut_5': x_strip_external_urls__mutmut_5, 
    'x_strip_external_urls__mutmut_6': x_strip_external_urls__mutmut_6, 
    'x_strip_external_urls__mutmut_7': x_strip_external_urls__mutmut_7, 
    'x_strip_external_urls__mutmut_8': x_strip_external_urls__mutmut_8, 
    'x_strip_external_urls__mutmut_9': x_strip_external_urls__mutmut_9, 
    'x_strip_external_urls__mutmut_10': x_strip_external_urls__mutmut_10, 
    'x_strip_external_urls__mutmut_11': x_strip_external_urls__mutmut_11, 
    'x_strip_external_urls__mutmut_12': x_strip_external_urls__mutmut_12, 
    'x_strip_external_urls__mutmut_13': x_strip_external_urls__mutmut_13, 
    'x_strip_external_urls__mutmut_14': x_strip_external_urls__mutmut_14, 
    'x_strip_external_urls__mutmut_15': x_strip_external_urls__mutmut_15
}
x_strip_external_urls__mutmut_orig.__name__ = 'x_strip_external_urls'


def validate_output(output: str, schema: dict | None = None) -> list[ValidationResult]:
    args = [output, schema]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_validate_output__mutmut_orig, x_validate_output__mutmut_mutants, args, kwargs, None)


def x_validate_output__mutmut_orig(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_1(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = None
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_2(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = None
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_3(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = True
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_4(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length >= _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_5(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = None
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_6(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = None

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_7(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = False

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_8(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = None
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_9(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(None, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_10(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, None)
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_11(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii([])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_12(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, )
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_13(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = None
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_14(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(None, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_15(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, None)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_16(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_17(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, )
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_18(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = None

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_19(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(None)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_20(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = None

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_21(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = None

    return results


def x_validate_output__mutmut_22(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=None,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_23(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=None,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_24(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=None,
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_25(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details=None,
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_26(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_27(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_28(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_29(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                )
            for r in results
        ]

    return results


def x_validate_output__mutmut_30(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_31(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "XXOutput truncated before validationXX",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_32(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "output truncated before validation",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_33(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "OUTPUT TRUNCATED BEFORE VALIDATION",
                details={**r.details, "original_length": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_34(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "XXoriginal_lengthXX": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_35(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "ORIGINAL_LENGTH": original_length, "truncated_length": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_36(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "XXtruncated_lengthXX": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results


def x_validate_output__mutmut_37(output: str, schema: dict | None = None) -> list[ValidationResult]:
    original_length = len(output)
    truncated = False
    if original_length > _MAX_OUTPUT_LENGTH:
        output = output[:_MAX_OUTPUT_LENGTH]
        truncated = True

    pii_result = check_output_pii(output, [])
    schema_result = validate_schema(output, schema)
    injection_result = check_injection_patterns(output)

    results = [pii_result, schema_result, injection_result]

    if truncated:
        results = [
            ValidationResult(
                passed=r.passed,
                gate=r.gate,
                reason=f"Output truncated: {r.reason}" if not r.passed else "Output truncated before validation",
                details={**r.details, "original_length": original_length, "TRUNCATED_LENGTH": _MAX_OUTPUT_LENGTH},
            )
            for r in results
        ]

    return results

x_validate_output__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_validate_output__mutmut_1': x_validate_output__mutmut_1, 
    'x_validate_output__mutmut_2': x_validate_output__mutmut_2, 
    'x_validate_output__mutmut_3': x_validate_output__mutmut_3, 
    'x_validate_output__mutmut_4': x_validate_output__mutmut_4, 
    'x_validate_output__mutmut_5': x_validate_output__mutmut_5, 
    'x_validate_output__mutmut_6': x_validate_output__mutmut_6, 
    'x_validate_output__mutmut_7': x_validate_output__mutmut_7, 
    'x_validate_output__mutmut_8': x_validate_output__mutmut_8, 
    'x_validate_output__mutmut_9': x_validate_output__mutmut_9, 
    'x_validate_output__mutmut_10': x_validate_output__mutmut_10, 
    'x_validate_output__mutmut_11': x_validate_output__mutmut_11, 
    'x_validate_output__mutmut_12': x_validate_output__mutmut_12, 
    'x_validate_output__mutmut_13': x_validate_output__mutmut_13, 
    'x_validate_output__mutmut_14': x_validate_output__mutmut_14, 
    'x_validate_output__mutmut_15': x_validate_output__mutmut_15, 
    'x_validate_output__mutmut_16': x_validate_output__mutmut_16, 
    'x_validate_output__mutmut_17': x_validate_output__mutmut_17, 
    'x_validate_output__mutmut_18': x_validate_output__mutmut_18, 
    'x_validate_output__mutmut_19': x_validate_output__mutmut_19, 
    'x_validate_output__mutmut_20': x_validate_output__mutmut_20, 
    'x_validate_output__mutmut_21': x_validate_output__mutmut_21, 
    'x_validate_output__mutmut_22': x_validate_output__mutmut_22, 
    'x_validate_output__mutmut_23': x_validate_output__mutmut_23, 
    'x_validate_output__mutmut_24': x_validate_output__mutmut_24, 
    'x_validate_output__mutmut_25': x_validate_output__mutmut_25, 
    'x_validate_output__mutmut_26': x_validate_output__mutmut_26, 
    'x_validate_output__mutmut_27': x_validate_output__mutmut_27, 
    'x_validate_output__mutmut_28': x_validate_output__mutmut_28, 
    'x_validate_output__mutmut_29': x_validate_output__mutmut_29, 
    'x_validate_output__mutmut_30': x_validate_output__mutmut_30, 
    'x_validate_output__mutmut_31': x_validate_output__mutmut_31, 
    'x_validate_output__mutmut_32': x_validate_output__mutmut_32, 
    'x_validate_output__mutmut_33': x_validate_output__mutmut_33, 
    'x_validate_output__mutmut_34': x_validate_output__mutmut_34, 
    'x_validate_output__mutmut_35': x_validate_output__mutmut_35, 
    'x_validate_output__mutmut_36': x_validate_output__mutmut_36, 
    'x_validate_output__mutmut_37': x_validate_output__mutmut_37
}
x_validate_output__mutmut_orig.__name__ = 'x_validate_output'
