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


def _detect_pii_in_text(text: str) -> list[dict]:
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    phone_pattern = re.compile(r"\+?\d[\d\s\-().]{7,}\d")
    entities = [
        {"entity_type": "EMAIL", "text": m.group(), "start": m.start(), "end": m.end()}
        for m in email_pattern.finditer(text)
    ] + [
        {"entity_type": "PHONE", "text": m.group(), "start": m.start(), "end": m.end()}
        for m in phone_pattern.finditer(text)
    ]
    return entities


def check_output_pii(output: str, input_pii: list[PIIEntity]) -> ValidationResult:
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


def validate_schema(output: str, schema: dict | None) -> ValidationResult:
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


def _type_matches(value, expected_type: str) -> bool:
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


def check_injection_patterns(output: str) -> ValidationResult:
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
            reason="Injection patterns detected: system prompt override or jailbreak attempt",
            details={"patterns": matched_patterns, "confidence": 0.8},
        )
    return ValidationResult(
        passed=True,
        gate="injection",
        reason="No injection patterns detected",
        details={"patterns": [], "confidence": 0.0},
    )


def validate_for_downstream(output: str, target: str) -> ValidationResult:
    if target == "shell":
        if _SHELL_DANGEROUS.search(output):
            return ValidationResult(
                passed=False,
                gate="downstream",
                reason="Dangerous shell command detected",
                details={"target": target},
            )
    elif target == "database" and _SQL_INJECTION.search(output):
        return ValidationResult(
            passed=False,
            gate="downstream",
            reason="SQL injection pattern detected",
            details={"target": target},
        )
    return ValidationResult(
        passed=True, gate="downstream", reason="Downstream validation passed", details={"target": target}
    )


def strip_external_urls(output: str) -> str:
    def _replace_external(match: re.Match) -> str:
        alt_text = match.group(1)
        url = match.group(2)
        if url.startswith("data:"):
            return match.group(0)
        return f"![{alt_text}]([REDACTED_URL])"

    return _EXTERNAL_URL_PATTERN.sub(_replace_external, output)


def validate_output(output: str, schema: dict | None = None) -> list[ValidationResult]:
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
