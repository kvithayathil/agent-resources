import re
import time
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path


class ScanStage(StrEnum):
    GARAK = "GARAK"
    PIP_AUDIT = "PIP_AUDIT"
    SEMGREP = "SEMGREP"
    CUSTOM_RULES = "CUSTOM_RULES"


@dataclass(frozen=True)
class ScanResult:
    stage: ScanStage
    passed: bool
    findings: list[str]
    duration_seconds: float


_INJECTION_KEYWORDS = ["ignore", "override", "reveal", "secret", "password", "bypass"]
_SECRET_PATTERNS = ["sk-", "api_key", "apikey", "secret_key", "password=", "token="]
_EXCESSIVE_PERMS = ["sudo", "drop", "delete", "execute"]


def _check_injection_risk(config: dict) -> list[str]:
    findings: list[str] = []
    for key, value in config.items():
        text = str(value).lower()
        for kw in _INJECTION_KEYWORDS:
            if kw in text:
                findings.append(f"Injection keyword '{kw}' found in {key}")
                break
    return findings


def _check_secrets_in_text(text: str) -> list[str]:
    return [f"Secret/API key pattern detected: {pattern}" for pattern in _SECRET_PATTERNS if pattern in text.lower()]


def _check_excessive_permissions(text: str) -> list[str]:
    findings: list[str] = []
    lower = text.lower()
    count = sum(1 for p in _EXCESSIVE_PERMS if p in lower)
    if count >= 2:
        findings.append(f"Excessive permissions detected: {count} dangerous permissions")
    return findings


def run_scan(stage: ScanStage, config: dict) -> ScanResult:
    start = time.monotonic()
    findings: list[str] = []

    if stage == ScanStage.GARAK:
        findings = _check_injection_risk(config)
        for value in config.values():
            if isinstance(value, list):
                for item in value:
                    findings.extend(_check_secrets_in_text(str(item)))
    elif stage == ScanStage.PIP_AUDIT:
        requirements = config.get("requirements", [])
        if isinstance(requirements, list):
            for req in requirements:
                if "==" not in str(req):
                    findings.append(f"Unpinned dependency: {req}")
    elif stage == ScanStage.SEMGREP:
        target = config.get("target", "")
        if target and ".." not in Path(target).parts:
            try:
                with open(target) as f:
                    content = f.read()
                findings.extend(_check_secrets_in_text(content))
            except OSError:
                pass
    elif stage == ScanStage.CUSTOM_RULES:
        custom_rules = config.get("custom_rules")
        if isinstance(custom_rules, list):
            for rule in custom_rules:
                if not isinstance(rule, dict):
                    continue
                name = rule.get("name", "unnamed")
                pattern = rule.get("pattern", "")
                if not pattern:
                    continue
                try:
                    compiled = re.compile(pattern, re.IGNORECASE)
                except re.error:
                    findings.append(f"Invalid regex in custom rule '{name}': {pattern}")
                    continue
                for key, value in config.items():
                    if key == "custom_rules":
                        continue
                    text = str(value) if not isinstance(value, list) else " ".join(str(v) for v in value)
                    if compiled.search(text):
                        findings.append(f"Custom rule '{name}' matched in {key}: {pattern}")

    duration = time.monotonic() - start
    return ScanResult(
        stage=stage,
        passed=len(findings) == 0,
        findings=findings,
        duration_seconds=duration,
    )


def check_no_secrets_in_prompts(file_path: str) -> ScanResult:
    start = time.monotonic()
    findings: list[str] = []
    try:
        with open(file_path) as f:
            content = f.read()
        findings.extend(_check_secrets_in_text(content))
    except OSError:
        findings.append(f"Cannot read file: {file_path}")
    duration = time.monotonic() - start
    return ScanResult(
        stage=ScanStage.CUSTOM_RULES, passed=len(findings) == 0, findings=findings, duration_seconds=duration
    )


def validate_tool_permissions(file_path: str) -> ScanResult:
    start = time.monotonic()
    findings: list[str] = []
    try:
        with open(file_path) as f:
            content = f.read()
        findings.extend(_check_excessive_permissions(content))
    except OSError:
        findings.append(f"Cannot read file: {file_path}")
    duration = time.monotonic() - start
    return ScanResult(
        stage=ScanStage.CUSTOM_RULES, passed=len(findings) == 0, findings=findings, duration_seconds=duration
    )


def run_full_pipeline(config: dict | None = None) -> list[ScanResult]:
    if config is None:
        config = {}
    results: list[ScanResult] = []
    fail_fast = config.get("fail_fast", False)
    has_critical = config.get("has_critical_vulnerability", False)

    for stage in ScanStage:
        if has_critical and stage == ScanStage.GARAK and fail_fast:
            result = ScanResult(
                stage=stage, passed=False, findings=["Critical vulnerability detected"], duration_seconds=0.01
            )
            results.append(result)
            return results
        result = run_scan(stage, config)
        results.append(result)
        if fail_fast and not result.passed:
            return results

    return results
