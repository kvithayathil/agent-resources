from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any

from security_layer.state_machine import InvalidTransition


class IncidentState(StrEnum):
    NORMAL = "NORMAL"
    ALERT = "ALERT"
    DEGRADED = "DEGRADED"
    LOCKED = "LOCKED"


class IncidentEvent(StrEnum):
    MITIGATION_FAILURE = "MITIGATION_FAILURE"
    ACKNOWLEDGE = "ACKNOWLEDGE"
    ESCALATE = "ESCALATE"
    CLEAR = "CLEAR"


@dataclass
class IncidentContext:
    state: IncidentState
    alert_reason: str | None = None
    degraded_mode: bool = False
    log: list[str] = field(default_factory=list)
    acknowledged_by: str | None = None
    escalation_reason: str | None = None


def _log_failure(context: IncidentContext, **kwargs: Any) -> None:
    reason = kwargs.get("alert_reason", "unknown failure")
    context.log.append(f"mitigation failure: {reason}")


def _log_acknowledge(context: IncidentContext, **kwargs: Any) -> None:
    who = kwargs.get("acknowledged_by", "unknown")
    context.log.append(f"acknowledged by {who}")


def _log_escalate(context: IncidentContext, **kwargs: Any) -> None:
    reason = kwargs.get("escalation_reason", "escalated")
    context.log.append(f"escalated: {reason}")


def _log_clear(context: IncidentContext, **kwargs: Any) -> None:
    who = kwargs.get("acknowledged_by", "unknown")
    context.log.append(f"cleared by {who}")


def _set_alert(context: IncidentContext, **kwargs: Any) -> None:
    context.alert_reason = kwargs.get("alert_reason")
    _log_failure(context, **kwargs)


def _set_degraded(context: IncidentContext, **kwargs: Any) -> None:
    context.alert_reason = kwargs.get("alert_reason")
    context.degraded_mode = True
    _log_failure(context, **kwargs)


def _clear_to_normal(context: IncidentContext, **kwargs: Any) -> None:
    context.degraded_mode = False
    context.alert_reason = None
    _log_clear(context, **kwargs)


def _set_escalated(context: IncidentContext, **kwargs: Any) -> None:
    context.escalation_reason = kwargs.get("escalation_reason")
    _log_escalate(context, **kwargs)


class _IncidentStateMachine:
    def transition(self, context: IncidentContext, event: IncidentEvent, **kwargs: Any) -> IncidentContext:
        key = (context.state, event)
        transitions = {
            (IncidentState.NORMAL, IncidentEvent.MITIGATION_FAILURE): (IncidentState.ALERT, _set_alert),
            (IncidentState.ALERT, IncidentEvent.ACKNOWLEDGE): (IncidentState.NORMAL, _log_acknowledge),
            (IncidentState.ALERT, IncidentEvent.MITIGATION_FAILURE): (IncidentState.DEGRADED, _set_degraded),
            (IncidentState.DEGRADED, IncidentEvent.ESCALATE): (IncidentState.LOCKED, _set_escalated),
            (IncidentState.DEGRADED, IncidentEvent.CLEAR): (IncidentState.NORMAL, _clear_to_normal),
            (IncidentState.LOCKED, IncidentEvent.CLEAR): (IncidentState.NORMAL, _clear_to_normal),
        }
        if key not in transitions:
            raise InvalidTransition(f"Invalid transition from {context.state!r} on event {event!r}")
        new_state, action = transitions[key]
        action(context, **kwargs)
        context.state = new_state
        return context


incident_state_machine = _IncidentStateMachine()


def report_failure(reason: str, severity: str = "high") -> IncidentContext:
    if severity == "critical":
        context = IncidentContext(state=IncidentState.DEGRADED, degraded_mode=True)
        context.alert_reason = reason
        context.log.append(f"critical failure: {reason}")
        return context
    context = IncidentContext(state=IncidentState.ALERT)
    context.alert_reason = reason
    context.log.append(f"failure: {reason}")
    return context


def is_read_only(context: IncidentContext) -> bool:
    return context.state in (IncidentState.DEGRADED, IncidentState.LOCKED)


def get_alert_message(context: IncidentContext) -> str:
    if context.state == IncidentState.ALERT:
        return f"ALERT: {context.alert_reason or 'Unknown alert'}"
    if context.state == IncidentState.DEGRADED:
        return f"DEGRADED MODE (read-only): {context.alert_reason or 'Multiple mitigation failures'}"
    if context.state == IncidentState.LOCKED:
        return f"LOCKED: System is locked due to security incident. {context.alert_reason or ''}"
    return "NORMAL: No active incidents"
