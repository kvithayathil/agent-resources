"""Tests for BC-9: Incident Response State Machine.

Tests the security_layer.incident module which manages incident states
and transitions using a state machine.
"""

import pytest
from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

# These imports will fail because the module doesn't exist yet
from security_layer.state_machine import StateMachine, InvalidTransition
from security_layer.incident import (
    IncidentState,
    IncidentEvent,
    IncidentContext,
    incident_state_machine,
    report_failure,
    is_read_only,
    get_alert_message,
)


class TestIncidentStateEnum:
    """Tests for IncidentState enum values."""

    def test_initial_state_is_normal(self):
        """IncidentState.NORMAL is the default/initial state."""
        assert IncidentState.NORMAL is not None
        context = IncidentContext(state=IncidentState.NORMAL)
        assert context.state == IncidentState.NORMAL


class TestIncidentStateTransitions:
    """Tests for state machine transitions."""

    def test_mitigation_failure_transitions_to_alert(self):
        """NORMAL + MITIGATION_FAILURE transitions to ALERT state."""
        context = IncidentContext(state=IncidentState.NORMAL)
        new_context = incident_state_machine.transition(
            context,
            IncidentEvent.MITIGATION_FAILURE,
            alert_reason="Mitigation failed to apply patch",
        )
        assert new_context.state == IncidentState.ALERT
        assert new_context.alert_reason == "Mitigation failed to apply patch"

    def test_acknowledge_returns_to_normal(self):
        """ALERT + ACKNOWLEDGE transitions back to NORMAL state."""
        context = IncidentContext(
            state=IncidentState.ALERT, alert_reason="Minor issue detected"
        )
        new_context = incident_state_machine.transition(
            context, IncidentEvent.ACKNOWLEDGE, acknowledged_by="security-team"
        )
        assert new_context.state == IncidentState.NORMAL

    def test_second_failure_transitions_to_degraded(self):
        """Second MITIGATION_FAILURE from ALERT transitions to DEGRADED state."""
        context = IncidentContext(
            state=IncidentState.ALERT, alert_reason="First failure occurred"
        )
        new_context = incident_state_machine.transition(
            context,
            IncidentEvent.MITIGATION_FAILURE,
            alert_reason="Critical: Mitigation failure repeated",
        )
        assert new_context.state == IncidentState.DEGRADED
        assert new_context.degraded_mode is True

    def test_escalate_from_degraded_to_locked(self):
        """DEGRADED + ESCALATE transitions to LOCKED state."""
        context = IncidentContext(state=IncidentState.DEGRADED, degraded_mode=True)
        new_context = incident_state_machine.transition(
            context,
            IncidentEvent.ESCALATE,
            escalation_reason="Security contact unavailable",
        )
        assert new_context.state == IncidentState.LOCKED

    def test_clear_from_degraded_to_normal(self):
        """DEGRADED + CLEAR transitions to NORMAL (requires acknowledgment)."""
        context = IncidentContext(
            state=IncidentState.DEGRADED,
            degraded_mode=True,
            alert_reason="System degraded",
        )
        new_context = incident_state_machine.transition(
            context, IncidentEvent.CLEAR, acknowledged_by="security-lead@example.com"
        )
        assert new_context.state == IncidentState.NORMAL
        assert new_context.degraded_mode is False

    def test_clear_from_locked_to_normal(self):
        """LOCKED + CLEAR transitions to NORMAL (requires acknowledgment)."""
        context = IncidentContext(state=IncidentState.LOCKED)
        new_context = incident_state_machine.transition(
            context, IncidentEvent.CLEAR, acknowledged_by="cto@example.com"
        )
        assert new_context.state == IncidentState.NORMAL

    def test_invalid_transition_normal_to_locked(self):
        """NORMAL + ESCALATE raises InvalidTransition."""
        context = IncidentContext(state=IncidentState.NORMAL)
        with pytest.raises(InvalidTransition):
            incident_state_machine.transition(
                context,
                IncidentEvent.ESCALATE,
                escalation_reason="Cannot escalate from normal",
            )

    def test_invalid_transition_normal_to_degraded(self):
        """NORMAL + CLEAR raises InvalidTransition."""
        context = IncidentContext(state=IncidentState.NORMAL)
        with pytest.raises(InvalidTransition):
            incident_state_machine.transition(
                context, IncidentEvent.CLEAR, acknowledged_by="test@example.com"
            )


class TestReadOnlyDetection:
    """Tests for read-only mode detection."""

    def test_degraded_is_read_only(self):
        """DEGRADED state should return True for is_read_only."""
        context = IncidentContext(state=IncidentState.DEGRADED, degraded_mode=True)
        assert is_read_only(context) is True

    def test_locked_is_read_only(self):
        """LOCKED state should return True for is_read_only."""
        context = IncidentContext(state=IncidentState.LOCKED)
        assert is_read_only(context) is True

    def test_normal_is_not_read_only(self):
        """NORMAL state should return False for is_read_only."""
        context = IncidentContext(state=IncidentState.NORMAL)
        assert is_read_only(context) is False

    def test_alert_is_not_read_only(self):
        """ALERT state should return False for is_read_only."""
        context = IncidentContext(state=IncidentState.ALERT, alert_reason="Minor alert")
        assert is_read_only(context) is False


class TestReportFailure:
    """Tests for report_failure function."""

    def test_report_failure_creates_alert_context(self):
        """report_failure creates incident context in ALERT state."""
        context = report_failure(
            reason="Authentication bypass attempt detected", severity="high"
        )
        assert context.state == IncidentState.ALERT
        assert context.alert_reason == "Authentication bypass attempt detected"
        assert len(context.log) > 0
        assert "failure" in context.log[0].lower()

    def test_report_failure_with_critical_severity(self):
        """report_failure with critical severity transitions to DEGRADED."""
        context = report_failure(
            reason="Critical security vulnerability", severity="critical"
        )
        assert context.state == IncidentState.DEGRADED
        assert context.degraded_mode is True


class TestAlertMessages:
    """Tests for alert message formatting."""

    def test_alert_message_includes_reason(self):
        """get_alert_message contains the failure reason."""
        context = IncidentContext(
            state=IncidentState.ALERT,
            alert_reason="SQL injection vulnerability detected in user input",
        )
        message = get_alert_message(context)
        assert "SQL injection vulnerability" in message
        assert "user input" in message

    def test_alert_message_for_degraded_state(self):
        """get_alert_message indicates read-only mode for DEGRADED."""
        context = IncidentContext(
            state=IncidentState.DEGRADED,
            degraded_mode=True,
            alert_reason="Multiple mitigation failures",
        )
        message = get_alert_message(context)
        assert "read-only" in message.lower() or "degraded" in message.lower()

    def test_alert_message_for_locked_state(self):
        """get_alert_message indicates locked status."""
        context = IncidentContext(
            state=IncidentState.LOCKED, alert_reason="Security incident escalated"
        )
        message = get_alert_message(context)
        assert "locked" in message.lower()


class TestLogging:
    """Tests for log entry tracking."""

    def test_log_entries_accumulate(self):
        """Multiple transitions add to log entries."""
        context = IncidentContext(state=IncidentState.NORMAL)

        context = incident_state_machine.transition(
            context, IncidentEvent.MITIGATION_FAILURE, alert_reason="First failure"
        )

        context = incident_state_machine.transition(
            context, IncidentEvent.ACKNOWLEDGE, acknowledged_by="security-team"
        )

        assert len(context.log) >= 2
        assert any("failure" in entry.lower() for entry in context.log)
        assert any("acknowledge" in entry.lower() for entry in context.log)


class TestIncidentContextDataclass:
    """Tests for IncidentContext dataclass structure."""

    def test_incident_context_has_required_fields(self):
        """IncidentContext has state, alert_reason, degraded_mode, and log fields."""
        context = IncidentContext(
            state=IncidentState.NORMAL,
            alert_reason="Test alert",
            degraded_mode=False,
            log=["Entry 1", "Entry 2"],
        )
        assert context.state == IncidentState.NORMAL
        assert context.alert_reason == "Test alert"
        assert context.degraded_mode is False
        assert context.log == ["Entry 1", "Entry 2"]

    def test_incident_context_defaults(self):
        """IncidentContext has sensible default values."""
        context = IncidentContext(state=IncidentState.NORMAL)
        assert context.alert_reason is None
        assert context.degraded_mode is False
        assert context.log == []
