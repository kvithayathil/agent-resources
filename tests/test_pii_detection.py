"""BC-2: PII Detection and Redaction Tests

Tests for PII detection, redaction, density escalation, and path allowlisting.
All tests FAIL until security_layer.pii module is implemented.
"""

import base64

import pytest

from security_layer.pii import (
    check_pii_density,
    detect_pii,
    is_allowlisted_path,
    redact_pii,
    scan_and_redact,
    should_escalate,
)
from security_layer.types import PIIEntity


class TestDetectPII:
    """Contract: BC-2 — all defined PII entity types must be detected."""

    def test_detect_email_address(self):
        text = "Contact john@example.com for info"
        entities = detect_pii(text)
        assert len(entities) > 0
        assert any(e.entity_type == "EMAIL_ADDRESS" for e in entities)

    def test_detect_phone_number(self):
        text = "Call 555-123-4567"
        entities = detect_pii(text)
        assert len(entities) > 0
        assert any(e.entity_type == "PHONE_NUMBER" for e in entities)

    def test_detect_credit_card(self):
        text = "Card: 4532-1234-5678-9010"
        entities = detect_pii(text)
        assert len(entities) > 0
        assert any(e.entity_type == "CREDIT_CARD" for e in entities)

    def test_detect_ssn(self):
        text = "SSN: 123-45-6789"
        entities = detect_pii(text)
        assert len(entities) > 0
        assert any(e.entity_type == "US_SSN" for e in entities)

    def test_detect_api_key_sk(self):
        """EC-2.2: Custom recognizer for OpenAI-style keys."""
        text = "Key: sk-abc123def456ghi789jkl012mno345"
        entities = detect_pii(text)
        assert len(entities) > 0
        assert any(e.entity_type == "API_KEY" for e in entities)

    def test_detect_api_key_ghp(self):
        """EC-2.2: Custom recognizer for GitHub PATs."""
        text = "Token: ghp_ABCDEFGHIJKLMNOPqrstuvwxyz01"
        entities = detect_pii(text)
        assert len(entities) > 0
        assert any(e.entity_type == "API_KEY" for e in entities)

    def test_detect_bearer_token(self):
        """EC-2.2: Custom recognizer for Bearer tokens."""
        text = "Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.test.sig"
        entities = detect_pii(text)
        assert len(entities) > 0
        assert any(e.entity_type in ("BEARER_TOKEN", "API_KEY") for e in entities)


class TestRedactPII:
    """Contract: BC-2 — PII replaced with typed placeholders."""

    def test_redact_replaces_email_with_placeholder(self):
        text = "Email: john@example.com and Phone: 555-123-4567"
        entities = detect_pii(text)
        redacted = redact_pii(text, entities)
        assert "john@example.com" not in redacted
        assert "[REDACTED_" in redacted

    def test_redact_preserves_non_pii(self):
        text = "Hello world, email is john@example.com end"
        entities = detect_pii(text)
        redacted = redact_pii(text, entities)
        assert "Hello world" in redacted
        assert "end" in redacted

    def test_redact_empty_entities_returns_original(self):
        text = "No PII here"
        redacted = redact_pii(text, [])
        assert redacted == text


class TestPIIDensity:
    """Contract: BC-2 — density escalation prevents blanket redaction DOS."""

    def test_high_pii_density_triggers_escalation(self):
        text = (
            "Name: John Doe, Email: john@example.com, Phone: 555-123-4567, "
            "SSN: 123-45-6789, Card: 4532-1234-5678-9010, Key: sk-test123456789"
        )
        entities = detect_pii(text)
        density = check_pii_density(text, entities)
        assert density > 0.7
        assert should_escalate(density, threshold=0.7) is True

    def test_low_pii_density_no_escalation(self):
        text = "This is a normal document about software engineering patterns."
        entities = detect_pii(text)
        density = check_pii_density(text, entities)
        assert density < 0.7
        assert should_escalate(density, threshold=0.7) is False

    def test_density_threshold_is_configurable(self):
        density = 0.5
        assert should_escalate(density, threshold=0.3) is True
        assert should_escalate(density, threshold=0.7) is False


class TestAllowlist:
    """Contract: BC-2 — test fixtures excluded from PII flagging."""

    def test_allowlisted_test_fixture_path(self):
        """EC-2.4: False positive on test fixture data."""
        path = "tests/fixtures/sample.json"
        allowlist = ["tests/fixtures/", "tests/data/", "samples/"]
        assert is_allowlisted_path(path, allowlist) is True

    def test_allowlisted_samples_path(self):
        path = "samples/example_output.json"
        allowlist = ["tests/fixtures/", "tests/data/", "samples/"]
        assert is_allowlisted_path(path, allowlist) is True

    def test_non_allowlisted_path_not_skipped(self):
        path = "src/config.py"
        allowlist = ["tests/fixtures/", "tests/data/", "samples/"]
        assert is_allowlisted_path(path, allowlist) is False

    def test_empty_allowlist_denies_all(self):
        path = "tests/fixtures/sample.json"
        assert is_allowlisted_path(path, []) is False


class TestScanAndRedact:
    """Contract: BC-2 — combined scan, redact, escalation pipeline."""

    def test_pii_in_base64_detected(self):
        """EC-2.5: PII in base64-encoded content."""
        encoded = base64.b64encode(b"john@example.com").decode()
        text = f"Data: {encoded}"
        redacted_text, entities, needs_escalation = scan_and_redact(text)
        assert len(entities) > 0

    def test_scan_returns_redacted_text(self):
        text = "Contact john@example.com for details"
        redacted_text, entities, needs_escalation = scan_and_redact(text)
        assert "john@example.com" not in redacted_text
        assert len(entities) > 0

    def test_scan_allowlisted_path_skips_redaction(self):
        """EC-2.4: Test fixtures should not trigger blanket redaction."""
        text = "email: test@example.com"
        redacted_text, entities, needs_escalation = scan_and_redact(
            text, path="tests/fixtures/users.json", allowlist=["tests/fixtures/"]
        )
        assert "test@example.com" in redacted_text

    def test_partial_pii_logged_for_review(self):
        """EC-2.1: Partial PII split across multiple file reads."""
        text = "Contact me at john@"
        redacted_text, entities, needs_escalation = scan_and_redact(text)
        assert isinstance(entities, list)
        assert isinstance(needs_escalation, bool)
