from dataclasses import dataclass, field
from enum import Enum
from typing import Any

from security_layer.state_machine import InvalidTransition, StateMachine
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


class IncidentState(str, Enum):
    NORMAL = "NORMAL"
    ALERT = "ALERT"
    DEGRADED = "DEGRADED"
    LOCKED = "LOCKED"


class IncidentEvent(str, Enum):
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
    args = [context]# type: ignore
    kwargs = {**kwargs}# type: ignore
    return _mutmut_trampoline(x__log_failure__mutmut_orig, x__log_failure__mutmut_mutants, args, kwargs, None)


def x__log_failure__mutmut_orig(context: IncidentContext, **kwargs: Any) -> None:
    reason = kwargs.get("alert_reason", "unknown failure")
    context.log.append(f"mitigation failure: {reason}")


def x__log_failure__mutmut_1(context: IncidentContext, **kwargs: Any) -> None:
    reason = None
    context.log.append(f"mitigation failure: {reason}")


def x__log_failure__mutmut_2(context: IncidentContext, **kwargs: Any) -> None:
    reason = kwargs.get(None, "unknown failure")
    context.log.append(f"mitigation failure: {reason}")


def x__log_failure__mutmut_3(context: IncidentContext, **kwargs: Any) -> None:
    reason = kwargs.get("alert_reason", None)
    context.log.append(f"mitigation failure: {reason}")


def x__log_failure__mutmut_4(context: IncidentContext, **kwargs: Any) -> None:
    reason = kwargs.get("unknown failure")
    context.log.append(f"mitigation failure: {reason}")


def x__log_failure__mutmut_5(context: IncidentContext, **kwargs: Any) -> None:
    reason = kwargs.get("alert_reason", )
    context.log.append(f"mitigation failure: {reason}")


def x__log_failure__mutmut_6(context: IncidentContext, **kwargs: Any) -> None:
    reason = kwargs.get("XXalert_reasonXX", "unknown failure")
    context.log.append(f"mitigation failure: {reason}")


def x__log_failure__mutmut_7(context: IncidentContext, **kwargs: Any) -> None:
    reason = kwargs.get("ALERT_REASON", "unknown failure")
    context.log.append(f"mitigation failure: {reason}")


def x__log_failure__mutmut_8(context: IncidentContext, **kwargs: Any) -> None:
    reason = kwargs.get("alert_reason", "XXunknown failureXX")
    context.log.append(f"mitigation failure: {reason}")


def x__log_failure__mutmut_9(context: IncidentContext, **kwargs: Any) -> None:
    reason = kwargs.get("alert_reason", "UNKNOWN FAILURE")
    context.log.append(f"mitigation failure: {reason}")


def x__log_failure__mutmut_10(context: IncidentContext, **kwargs: Any) -> None:
    reason = kwargs.get("alert_reason", "unknown failure")
    context.log.append(None)

x__log_failure__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x__log_failure__mutmut_1': x__log_failure__mutmut_1, 
    'x__log_failure__mutmut_2': x__log_failure__mutmut_2, 
    'x__log_failure__mutmut_3': x__log_failure__mutmut_3, 
    'x__log_failure__mutmut_4': x__log_failure__mutmut_4, 
    'x__log_failure__mutmut_5': x__log_failure__mutmut_5, 
    'x__log_failure__mutmut_6': x__log_failure__mutmut_6, 
    'x__log_failure__mutmut_7': x__log_failure__mutmut_7, 
    'x__log_failure__mutmut_8': x__log_failure__mutmut_8, 
    'x__log_failure__mutmut_9': x__log_failure__mutmut_9, 
    'x__log_failure__mutmut_10': x__log_failure__mutmut_10
}
x__log_failure__mutmut_orig.__name__ = 'x__log_failure'


def _log_acknowledge(context: IncidentContext, **kwargs: Any) -> None:
    args = [context]# type: ignore
    kwargs = {**kwargs}# type: ignore
    return _mutmut_trampoline(x__log_acknowledge__mutmut_orig, x__log_acknowledge__mutmut_mutants, args, kwargs, None)


def x__log_acknowledge__mutmut_orig(context: IncidentContext, **kwargs: Any) -> None:
    who = kwargs.get("acknowledged_by", "unknown")
    context.log.append(f"acknowledged by {who}")


def x__log_acknowledge__mutmut_1(context: IncidentContext, **kwargs: Any) -> None:
    who = None
    context.log.append(f"acknowledged by {who}")


def x__log_acknowledge__mutmut_2(context: IncidentContext, **kwargs: Any) -> None:
    who = kwargs.get(None, "unknown")
    context.log.append(f"acknowledged by {who}")


def x__log_acknowledge__mutmut_3(context: IncidentContext, **kwargs: Any) -> None:
    who = kwargs.get("acknowledged_by", None)
    context.log.append(f"acknowledged by {who}")


def x__log_acknowledge__mutmut_4(context: IncidentContext, **kwargs: Any) -> None:
    who = kwargs.get("unknown")
    context.log.append(f"acknowledged by {who}")


def x__log_acknowledge__mutmut_5(context: IncidentContext, **kwargs: Any) -> None:
    who = kwargs.get("acknowledged_by", )
    context.log.append(f"acknowledged by {who}")


def x__log_acknowledge__mutmut_6(context: IncidentContext, **kwargs: Any) -> None:
    who = kwargs.get("XXacknowledged_byXX", "unknown")
    context.log.append(f"acknowledged by {who}")


def x__log_acknowledge__mutmut_7(context: IncidentContext, **kwargs: Any) -> None:
    who = kwargs.get("ACKNOWLEDGED_BY", "unknown")
    context.log.append(f"acknowledged by {who}")


def x__log_acknowledge__mutmut_8(context: IncidentContext, **kwargs: Any) -> None:
    who = kwargs.get("acknowledged_by", "XXunknownXX")
    context.log.append(f"acknowledged by {who}")


def x__log_acknowledge__mutmut_9(context: IncidentContext, **kwargs: Any) -> None:
    who = kwargs.get("acknowledged_by", "UNKNOWN")
    context.log.append(f"acknowledged by {who}")


def x__log_acknowledge__mutmut_10(context: IncidentContext, **kwargs: Any) -> None:
    who = kwargs.get("acknowledged_by", "unknown")
    context.log.append(None)

x__log_acknowledge__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x__log_acknowledge__mutmut_1': x__log_acknowledge__mutmut_1, 
    'x__log_acknowledge__mutmut_2': x__log_acknowledge__mutmut_2, 
    'x__log_acknowledge__mutmut_3': x__log_acknowledge__mutmut_3, 
    'x__log_acknowledge__mutmut_4': x__log_acknowledge__mutmut_4, 
    'x__log_acknowledge__mutmut_5': x__log_acknowledge__mutmut_5, 
    'x__log_acknowledge__mutmut_6': x__log_acknowledge__mutmut_6, 
    'x__log_acknowledge__mutmut_7': x__log_acknowledge__mutmut_7, 
    'x__log_acknowledge__mutmut_8': x__log_acknowledge__mutmut_8, 
    'x__log_acknowledge__mutmut_9': x__log_acknowledge__mutmut_9, 
    'x__log_acknowledge__mutmut_10': x__log_acknowledge__mutmut_10
}
x__log_acknowledge__mutmut_orig.__name__ = 'x__log_acknowledge'


def _log_escalate(context: IncidentContext, **kwargs: Any) -> None:
    args = [context]# type: ignore
    kwargs = {**kwargs}# type: ignore
    return _mutmut_trampoline(x__log_escalate__mutmut_orig, x__log_escalate__mutmut_mutants, args, kwargs, None)


def x__log_escalate__mutmut_orig(context: IncidentContext, **kwargs: Any) -> None:
    reason = kwargs.get("escalation_reason", "escalated")
    context.log.append(f"escalated: {reason}")


def x__log_escalate__mutmut_1(context: IncidentContext, **kwargs: Any) -> None:
    reason = None
    context.log.append(f"escalated: {reason}")


def x__log_escalate__mutmut_2(context: IncidentContext, **kwargs: Any) -> None:
    reason = kwargs.get(None, "escalated")
    context.log.append(f"escalated: {reason}")


def x__log_escalate__mutmut_3(context: IncidentContext, **kwargs: Any) -> None:
    reason = kwargs.get("escalation_reason", None)
    context.log.append(f"escalated: {reason}")


def x__log_escalate__mutmut_4(context: IncidentContext, **kwargs: Any) -> None:
    reason = kwargs.get("escalated")
    context.log.append(f"escalated: {reason}")


def x__log_escalate__mutmut_5(context: IncidentContext, **kwargs: Any) -> None:
    reason = kwargs.get("escalation_reason", )
    context.log.append(f"escalated: {reason}")


def x__log_escalate__mutmut_6(context: IncidentContext, **kwargs: Any) -> None:
    reason = kwargs.get("XXescalation_reasonXX", "escalated")
    context.log.append(f"escalated: {reason}")


def x__log_escalate__mutmut_7(context: IncidentContext, **kwargs: Any) -> None:
    reason = kwargs.get("ESCALATION_REASON", "escalated")
    context.log.append(f"escalated: {reason}")


def x__log_escalate__mutmut_8(context: IncidentContext, **kwargs: Any) -> None:
    reason = kwargs.get("escalation_reason", "XXescalatedXX")
    context.log.append(f"escalated: {reason}")


def x__log_escalate__mutmut_9(context: IncidentContext, **kwargs: Any) -> None:
    reason = kwargs.get("escalation_reason", "ESCALATED")
    context.log.append(f"escalated: {reason}")


def x__log_escalate__mutmut_10(context: IncidentContext, **kwargs: Any) -> None:
    reason = kwargs.get("escalation_reason", "escalated")
    context.log.append(None)

x__log_escalate__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x__log_escalate__mutmut_1': x__log_escalate__mutmut_1, 
    'x__log_escalate__mutmut_2': x__log_escalate__mutmut_2, 
    'x__log_escalate__mutmut_3': x__log_escalate__mutmut_3, 
    'x__log_escalate__mutmut_4': x__log_escalate__mutmut_4, 
    'x__log_escalate__mutmut_5': x__log_escalate__mutmut_5, 
    'x__log_escalate__mutmut_6': x__log_escalate__mutmut_6, 
    'x__log_escalate__mutmut_7': x__log_escalate__mutmut_7, 
    'x__log_escalate__mutmut_8': x__log_escalate__mutmut_8, 
    'x__log_escalate__mutmut_9': x__log_escalate__mutmut_9, 
    'x__log_escalate__mutmut_10': x__log_escalate__mutmut_10
}
x__log_escalate__mutmut_orig.__name__ = 'x__log_escalate'


def _log_clear(context: IncidentContext, **kwargs: Any) -> None:
    args = [context]# type: ignore
    kwargs = {**kwargs}# type: ignore
    return _mutmut_trampoline(x__log_clear__mutmut_orig, x__log_clear__mutmut_mutants, args, kwargs, None)


def x__log_clear__mutmut_orig(context: IncidentContext, **kwargs: Any) -> None:
    who = kwargs.get("acknowledged_by", "unknown")
    context.log.append(f"cleared by {who}")


def x__log_clear__mutmut_1(context: IncidentContext, **kwargs: Any) -> None:
    who = None
    context.log.append(f"cleared by {who}")


def x__log_clear__mutmut_2(context: IncidentContext, **kwargs: Any) -> None:
    who = kwargs.get(None, "unknown")
    context.log.append(f"cleared by {who}")


def x__log_clear__mutmut_3(context: IncidentContext, **kwargs: Any) -> None:
    who = kwargs.get("acknowledged_by", None)
    context.log.append(f"cleared by {who}")


def x__log_clear__mutmut_4(context: IncidentContext, **kwargs: Any) -> None:
    who = kwargs.get("unknown")
    context.log.append(f"cleared by {who}")


def x__log_clear__mutmut_5(context: IncidentContext, **kwargs: Any) -> None:
    who = kwargs.get("acknowledged_by", )
    context.log.append(f"cleared by {who}")


def x__log_clear__mutmut_6(context: IncidentContext, **kwargs: Any) -> None:
    who = kwargs.get("XXacknowledged_byXX", "unknown")
    context.log.append(f"cleared by {who}")


def x__log_clear__mutmut_7(context: IncidentContext, **kwargs: Any) -> None:
    who = kwargs.get("ACKNOWLEDGED_BY", "unknown")
    context.log.append(f"cleared by {who}")


def x__log_clear__mutmut_8(context: IncidentContext, **kwargs: Any) -> None:
    who = kwargs.get("acknowledged_by", "XXunknownXX")
    context.log.append(f"cleared by {who}")


def x__log_clear__mutmut_9(context: IncidentContext, **kwargs: Any) -> None:
    who = kwargs.get("acknowledged_by", "UNKNOWN")
    context.log.append(f"cleared by {who}")


def x__log_clear__mutmut_10(context: IncidentContext, **kwargs: Any) -> None:
    who = kwargs.get("acknowledged_by", "unknown")
    context.log.append(None)

x__log_clear__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x__log_clear__mutmut_1': x__log_clear__mutmut_1, 
    'x__log_clear__mutmut_2': x__log_clear__mutmut_2, 
    'x__log_clear__mutmut_3': x__log_clear__mutmut_3, 
    'x__log_clear__mutmut_4': x__log_clear__mutmut_4, 
    'x__log_clear__mutmut_5': x__log_clear__mutmut_5, 
    'x__log_clear__mutmut_6': x__log_clear__mutmut_6, 
    'x__log_clear__mutmut_7': x__log_clear__mutmut_7, 
    'x__log_clear__mutmut_8': x__log_clear__mutmut_8, 
    'x__log_clear__mutmut_9': x__log_clear__mutmut_9, 
    'x__log_clear__mutmut_10': x__log_clear__mutmut_10
}
x__log_clear__mutmut_orig.__name__ = 'x__log_clear'


def _set_alert(context: IncidentContext, **kwargs: Any) -> None:
    args = [context]# type: ignore
    kwargs = {**kwargs}# type: ignore
    return _mutmut_trampoline(x__set_alert__mutmut_orig, x__set_alert__mutmut_mutants, args, kwargs, None)


def x__set_alert__mutmut_orig(context: IncidentContext, **kwargs: Any) -> None:
    context.alert_reason = kwargs.get("alert_reason")
    _log_failure(context, **kwargs)


def x__set_alert__mutmut_1(context: IncidentContext, **kwargs: Any) -> None:
    context.alert_reason = None
    _log_failure(context, **kwargs)


def x__set_alert__mutmut_2(context: IncidentContext, **kwargs: Any) -> None:
    context.alert_reason = kwargs.get(None)
    _log_failure(context, **kwargs)


def x__set_alert__mutmut_3(context: IncidentContext, **kwargs: Any) -> None:
    context.alert_reason = kwargs.get("XXalert_reasonXX")
    _log_failure(context, **kwargs)


def x__set_alert__mutmut_4(context: IncidentContext, **kwargs: Any) -> None:
    context.alert_reason = kwargs.get("ALERT_REASON")
    _log_failure(context, **kwargs)


def x__set_alert__mutmut_5(context: IncidentContext, **kwargs: Any) -> None:
    context.alert_reason = kwargs.get("alert_reason")
    _log_failure(None, **kwargs)


def x__set_alert__mutmut_6(context: IncidentContext, **kwargs: Any) -> None:
    context.alert_reason = kwargs.get("alert_reason")
    _log_failure(**kwargs)


def x__set_alert__mutmut_7(context: IncidentContext, **kwargs: Any) -> None:
    context.alert_reason = kwargs.get("alert_reason")
    _log_failure(context, )

x__set_alert__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x__set_alert__mutmut_1': x__set_alert__mutmut_1, 
    'x__set_alert__mutmut_2': x__set_alert__mutmut_2, 
    'x__set_alert__mutmut_3': x__set_alert__mutmut_3, 
    'x__set_alert__mutmut_4': x__set_alert__mutmut_4, 
    'x__set_alert__mutmut_5': x__set_alert__mutmut_5, 
    'x__set_alert__mutmut_6': x__set_alert__mutmut_6, 
    'x__set_alert__mutmut_7': x__set_alert__mutmut_7
}
x__set_alert__mutmut_orig.__name__ = 'x__set_alert'


def _set_degraded(context: IncidentContext, **kwargs: Any) -> None:
    args = [context]# type: ignore
    kwargs = {**kwargs}# type: ignore
    return _mutmut_trampoline(x__set_degraded__mutmut_orig, x__set_degraded__mutmut_mutants, args, kwargs, None)


def x__set_degraded__mutmut_orig(context: IncidentContext, **kwargs: Any) -> None:
    context.alert_reason = kwargs.get("alert_reason")
    context.degraded_mode = True
    _log_failure(context, **kwargs)


def x__set_degraded__mutmut_1(context: IncidentContext, **kwargs: Any) -> None:
    context.alert_reason = None
    context.degraded_mode = True
    _log_failure(context, **kwargs)


def x__set_degraded__mutmut_2(context: IncidentContext, **kwargs: Any) -> None:
    context.alert_reason = kwargs.get(None)
    context.degraded_mode = True
    _log_failure(context, **kwargs)


def x__set_degraded__mutmut_3(context: IncidentContext, **kwargs: Any) -> None:
    context.alert_reason = kwargs.get("XXalert_reasonXX")
    context.degraded_mode = True
    _log_failure(context, **kwargs)


def x__set_degraded__mutmut_4(context: IncidentContext, **kwargs: Any) -> None:
    context.alert_reason = kwargs.get("ALERT_REASON")
    context.degraded_mode = True
    _log_failure(context, **kwargs)


def x__set_degraded__mutmut_5(context: IncidentContext, **kwargs: Any) -> None:
    context.alert_reason = kwargs.get("alert_reason")
    context.degraded_mode = None
    _log_failure(context, **kwargs)


def x__set_degraded__mutmut_6(context: IncidentContext, **kwargs: Any) -> None:
    context.alert_reason = kwargs.get("alert_reason")
    context.degraded_mode = False
    _log_failure(context, **kwargs)


def x__set_degraded__mutmut_7(context: IncidentContext, **kwargs: Any) -> None:
    context.alert_reason = kwargs.get("alert_reason")
    context.degraded_mode = True
    _log_failure(None, **kwargs)


def x__set_degraded__mutmut_8(context: IncidentContext, **kwargs: Any) -> None:
    context.alert_reason = kwargs.get("alert_reason")
    context.degraded_mode = True
    _log_failure(**kwargs)


def x__set_degraded__mutmut_9(context: IncidentContext, **kwargs: Any) -> None:
    context.alert_reason = kwargs.get("alert_reason")
    context.degraded_mode = True
    _log_failure(context, )

x__set_degraded__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x__set_degraded__mutmut_1': x__set_degraded__mutmut_1, 
    'x__set_degraded__mutmut_2': x__set_degraded__mutmut_2, 
    'x__set_degraded__mutmut_3': x__set_degraded__mutmut_3, 
    'x__set_degraded__mutmut_4': x__set_degraded__mutmut_4, 
    'x__set_degraded__mutmut_5': x__set_degraded__mutmut_5, 
    'x__set_degraded__mutmut_6': x__set_degraded__mutmut_6, 
    'x__set_degraded__mutmut_7': x__set_degraded__mutmut_7, 
    'x__set_degraded__mutmut_8': x__set_degraded__mutmut_8, 
    'x__set_degraded__mutmut_9': x__set_degraded__mutmut_9
}
x__set_degraded__mutmut_orig.__name__ = 'x__set_degraded'


def _clear_to_normal(context: IncidentContext, **kwargs: Any) -> None:
    args = [context]# type: ignore
    kwargs = {**kwargs}# type: ignore
    return _mutmut_trampoline(x__clear_to_normal__mutmut_orig, x__clear_to_normal__mutmut_mutants, args, kwargs, None)


def x__clear_to_normal__mutmut_orig(context: IncidentContext, **kwargs: Any) -> None:
    context.degraded_mode = False
    context.alert_reason = None
    _log_clear(context, **kwargs)


def x__clear_to_normal__mutmut_1(context: IncidentContext, **kwargs: Any) -> None:
    context.degraded_mode = None
    context.alert_reason = None
    _log_clear(context, **kwargs)


def x__clear_to_normal__mutmut_2(context: IncidentContext, **kwargs: Any) -> None:
    context.degraded_mode = True
    context.alert_reason = None
    _log_clear(context, **kwargs)


def x__clear_to_normal__mutmut_3(context: IncidentContext, **kwargs: Any) -> None:
    context.degraded_mode = False
    context.alert_reason = ""
    _log_clear(context, **kwargs)


def x__clear_to_normal__mutmut_4(context: IncidentContext, **kwargs: Any) -> None:
    context.degraded_mode = False
    context.alert_reason = None
    _log_clear(None, **kwargs)


def x__clear_to_normal__mutmut_5(context: IncidentContext, **kwargs: Any) -> None:
    context.degraded_mode = False
    context.alert_reason = None
    _log_clear(**kwargs)


def x__clear_to_normal__mutmut_6(context: IncidentContext, **kwargs: Any) -> None:
    context.degraded_mode = False
    context.alert_reason = None
    _log_clear(context, )

x__clear_to_normal__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x__clear_to_normal__mutmut_1': x__clear_to_normal__mutmut_1, 
    'x__clear_to_normal__mutmut_2': x__clear_to_normal__mutmut_2, 
    'x__clear_to_normal__mutmut_3': x__clear_to_normal__mutmut_3, 
    'x__clear_to_normal__mutmut_4': x__clear_to_normal__mutmut_4, 
    'x__clear_to_normal__mutmut_5': x__clear_to_normal__mutmut_5, 
    'x__clear_to_normal__mutmut_6': x__clear_to_normal__mutmut_6
}
x__clear_to_normal__mutmut_orig.__name__ = 'x__clear_to_normal'


def _set_escalated(context: IncidentContext, **kwargs: Any) -> None:
    args = [context]# type: ignore
    kwargs = {**kwargs}# type: ignore
    return _mutmut_trampoline(x__set_escalated__mutmut_orig, x__set_escalated__mutmut_mutants, args, kwargs, None)


def x__set_escalated__mutmut_orig(context: IncidentContext, **kwargs: Any) -> None:
    context.escalation_reason = kwargs.get("escalation_reason")
    _log_escalate(context, **kwargs)


def x__set_escalated__mutmut_1(context: IncidentContext, **kwargs: Any) -> None:
    context.escalation_reason = None
    _log_escalate(context, **kwargs)


def x__set_escalated__mutmut_2(context: IncidentContext, **kwargs: Any) -> None:
    context.escalation_reason = kwargs.get(None)
    _log_escalate(context, **kwargs)


def x__set_escalated__mutmut_3(context: IncidentContext, **kwargs: Any) -> None:
    context.escalation_reason = kwargs.get("XXescalation_reasonXX")
    _log_escalate(context, **kwargs)


def x__set_escalated__mutmut_4(context: IncidentContext, **kwargs: Any) -> None:
    context.escalation_reason = kwargs.get("ESCALATION_REASON")
    _log_escalate(context, **kwargs)


def x__set_escalated__mutmut_5(context: IncidentContext, **kwargs: Any) -> None:
    context.escalation_reason = kwargs.get("escalation_reason")
    _log_escalate(None, **kwargs)


def x__set_escalated__mutmut_6(context: IncidentContext, **kwargs: Any) -> None:
    context.escalation_reason = kwargs.get("escalation_reason")
    _log_escalate(**kwargs)


def x__set_escalated__mutmut_7(context: IncidentContext, **kwargs: Any) -> None:
    context.escalation_reason = kwargs.get("escalation_reason")
    _log_escalate(context, )

x__set_escalated__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x__set_escalated__mutmut_1': x__set_escalated__mutmut_1, 
    'x__set_escalated__mutmut_2': x__set_escalated__mutmut_2, 
    'x__set_escalated__mutmut_3': x__set_escalated__mutmut_3, 
    'x__set_escalated__mutmut_4': x__set_escalated__mutmut_4, 
    'x__set_escalated__mutmut_5': x__set_escalated__mutmut_5, 
    'x__set_escalated__mutmut_6': x__set_escalated__mutmut_6, 
    'x__set_escalated__mutmut_7': x__set_escalated__mutmut_7
}
x__set_escalated__mutmut_orig.__name__ = 'x__set_escalated'


class _IncidentStateMachine:
    def transition(self, context: IncidentContext, event: IncidentEvent, **kwargs: Any) -> IncidentContext:
        args = [context, event]# type: ignore
        kwargs = {**kwargs}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁ_IncidentStateMachineǁtransition__mutmut_orig'), object.__getattribute__(self, 'xǁ_IncidentStateMachineǁtransition__mutmut_mutants'), args, kwargs, self)
    def xǁ_IncidentStateMachineǁtransition__mutmut_orig(self, context: IncidentContext, event: IncidentEvent, **kwargs: Any) -> IncidentContext:
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
    def xǁ_IncidentStateMachineǁtransition__mutmut_1(self, context: IncidentContext, event: IncidentEvent, **kwargs: Any) -> IncidentContext:
        key = None
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
    def xǁ_IncidentStateMachineǁtransition__mutmut_2(self, context: IncidentContext, event: IncidentEvent, **kwargs: Any) -> IncidentContext:
        key = (context.state, event)
        transitions = None
        if key not in transitions:
            raise InvalidTransition(f"Invalid transition from {context.state!r} on event {event!r}")
        new_state, action = transitions[key]
        action(context, **kwargs)
        context.state = new_state
        return context
    def xǁ_IncidentStateMachineǁtransition__mutmut_3(self, context: IncidentContext, event: IncidentEvent, **kwargs: Any) -> IncidentContext:
        key = (context.state, event)
        transitions = {
            (IncidentState.NORMAL, IncidentEvent.MITIGATION_FAILURE): (IncidentState.ALERT, _set_alert),
            (IncidentState.ALERT, IncidentEvent.ACKNOWLEDGE): (IncidentState.NORMAL, _log_acknowledge),
            (IncidentState.ALERT, IncidentEvent.MITIGATION_FAILURE): (IncidentState.DEGRADED, _set_degraded),
            (IncidentState.DEGRADED, IncidentEvent.ESCALATE): (IncidentState.LOCKED, _set_escalated),
            (IncidentState.DEGRADED, IncidentEvent.CLEAR): (IncidentState.NORMAL, _clear_to_normal),
            (IncidentState.LOCKED, IncidentEvent.CLEAR): (IncidentState.NORMAL, _clear_to_normal),
        }
        if key in transitions:
            raise InvalidTransition(f"Invalid transition from {context.state!r} on event {event!r}")
        new_state, action = transitions[key]
        action(context, **kwargs)
        context.state = new_state
        return context
    def xǁ_IncidentStateMachineǁtransition__mutmut_4(self, context: IncidentContext, event: IncidentEvent, **kwargs: Any) -> IncidentContext:
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
            raise InvalidTransition(None)
        new_state, action = transitions[key]
        action(context, **kwargs)
        context.state = new_state
        return context
    def xǁ_IncidentStateMachineǁtransition__mutmut_5(self, context: IncidentContext, event: IncidentEvent, **kwargs: Any) -> IncidentContext:
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
        new_state, action = None
        action(context, **kwargs)
        context.state = new_state
        return context
    def xǁ_IncidentStateMachineǁtransition__mutmut_6(self, context: IncidentContext, event: IncidentEvent, **kwargs: Any) -> IncidentContext:
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
        action(None, **kwargs)
        context.state = new_state
        return context
    def xǁ_IncidentStateMachineǁtransition__mutmut_7(self, context: IncidentContext, event: IncidentEvent, **kwargs: Any) -> IncidentContext:
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
        action(**kwargs)
        context.state = new_state
        return context
    def xǁ_IncidentStateMachineǁtransition__mutmut_8(self, context: IncidentContext, event: IncidentEvent, **kwargs: Any) -> IncidentContext:
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
        action(context, )
        context.state = new_state
        return context
    def xǁ_IncidentStateMachineǁtransition__mutmut_9(self, context: IncidentContext, event: IncidentEvent, **kwargs: Any) -> IncidentContext:
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
        context.state = None
        return context
    
    xǁ_IncidentStateMachineǁtransition__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁ_IncidentStateMachineǁtransition__mutmut_1': xǁ_IncidentStateMachineǁtransition__mutmut_1, 
        'xǁ_IncidentStateMachineǁtransition__mutmut_2': xǁ_IncidentStateMachineǁtransition__mutmut_2, 
        'xǁ_IncidentStateMachineǁtransition__mutmut_3': xǁ_IncidentStateMachineǁtransition__mutmut_3, 
        'xǁ_IncidentStateMachineǁtransition__mutmut_4': xǁ_IncidentStateMachineǁtransition__mutmut_4, 
        'xǁ_IncidentStateMachineǁtransition__mutmut_5': xǁ_IncidentStateMachineǁtransition__mutmut_5, 
        'xǁ_IncidentStateMachineǁtransition__mutmut_6': xǁ_IncidentStateMachineǁtransition__mutmut_6, 
        'xǁ_IncidentStateMachineǁtransition__mutmut_7': xǁ_IncidentStateMachineǁtransition__mutmut_7, 
        'xǁ_IncidentStateMachineǁtransition__mutmut_8': xǁ_IncidentStateMachineǁtransition__mutmut_8, 
        'xǁ_IncidentStateMachineǁtransition__mutmut_9': xǁ_IncidentStateMachineǁtransition__mutmut_9
    }
    xǁ_IncidentStateMachineǁtransition__mutmut_orig.__name__ = 'xǁ_IncidentStateMachineǁtransition'


incident_state_machine = _IncidentStateMachine()


def report_failure(reason: str, severity: str = "high") -> IncidentContext:
    args = [reason, severity]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_report_failure__mutmut_orig, x_report_failure__mutmut_mutants, args, kwargs, None)


def x_report_failure__mutmut_orig(reason: str, severity: str = "high") -> IncidentContext:
    if severity == "critical":
        context = IncidentContext(state=IncidentState.DEGRADED, degraded_mode=True)
        context.alert_reason = reason
        context.log.append(f"critical failure: {reason}")
        return context
    context = IncidentContext(state=IncidentState.ALERT)
    context.alert_reason = reason
    context.log.append(f"failure: {reason}")
    return context


def x_report_failure__mutmut_1(reason: str, severity: str = "XXhighXX") -> IncidentContext:
    if severity == "critical":
        context = IncidentContext(state=IncidentState.DEGRADED, degraded_mode=True)
        context.alert_reason = reason
        context.log.append(f"critical failure: {reason}")
        return context
    context = IncidentContext(state=IncidentState.ALERT)
    context.alert_reason = reason
    context.log.append(f"failure: {reason}")
    return context


def x_report_failure__mutmut_2(reason: str, severity: str = "HIGH") -> IncidentContext:
    if severity == "critical":
        context = IncidentContext(state=IncidentState.DEGRADED, degraded_mode=True)
        context.alert_reason = reason
        context.log.append(f"critical failure: {reason}")
        return context
    context = IncidentContext(state=IncidentState.ALERT)
    context.alert_reason = reason
    context.log.append(f"failure: {reason}")
    return context


def x_report_failure__mutmut_3(reason: str, severity: str = "high") -> IncidentContext:
    if severity != "critical":
        context = IncidentContext(state=IncidentState.DEGRADED, degraded_mode=True)
        context.alert_reason = reason
        context.log.append(f"critical failure: {reason}")
        return context
    context = IncidentContext(state=IncidentState.ALERT)
    context.alert_reason = reason
    context.log.append(f"failure: {reason}")
    return context


def x_report_failure__mutmut_4(reason: str, severity: str = "high") -> IncidentContext:
    if severity == "XXcriticalXX":
        context = IncidentContext(state=IncidentState.DEGRADED, degraded_mode=True)
        context.alert_reason = reason
        context.log.append(f"critical failure: {reason}")
        return context
    context = IncidentContext(state=IncidentState.ALERT)
    context.alert_reason = reason
    context.log.append(f"failure: {reason}")
    return context


def x_report_failure__mutmut_5(reason: str, severity: str = "high") -> IncidentContext:
    if severity == "CRITICAL":
        context = IncidentContext(state=IncidentState.DEGRADED, degraded_mode=True)
        context.alert_reason = reason
        context.log.append(f"critical failure: {reason}")
        return context
    context = IncidentContext(state=IncidentState.ALERT)
    context.alert_reason = reason
    context.log.append(f"failure: {reason}")
    return context


def x_report_failure__mutmut_6(reason: str, severity: str = "high") -> IncidentContext:
    if severity == "critical":
        context = None
        context.alert_reason = reason
        context.log.append(f"critical failure: {reason}")
        return context
    context = IncidentContext(state=IncidentState.ALERT)
    context.alert_reason = reason
    context.log.append(f"failure: {reason}")
    return context


def x_report_failure__mutmut_7(reason: str, severity: str = "high") -> IncidentContext:
    if severity == "critical":
        context = IncidentContext(state=None, degraded_mode=True)
        context.alert_reason = reason
        context.log.append(f"critical failure: {reason}")
        return context
    context = IncidentContext(state=IncidentState.ALERT)
    context.alert_reason = reason
    context.log.append(f"failure: {reason}")
    return context


def x_report_failure__mutmut_8(reason: str, severity: str = "high") -> IncidentContext:
    if severity == "critical":
        context = IncidentContext(state=IncidentState.DEGRADED, degraded_mode=None)
        context.alert_reason = reason
        context.log.append(f"critical failure: {reason}")
        return context
    context = IncidentContext(state=IncidentState.ALERT)
    context.alert_reason = reason
    context.log.append(f"failure: {reason}")
    return context


def x_report_failure__mutmut_9(reason: str, severity: str = "high") -> IncidentContext:
    if severity == "critical":
        context = IncidentContext(degraded_mode=True)
        context.alert_reason = reason
        context.log.append(f"critical failure: {reason}")
        return context
    context = IncidentContext(state=IncidentState.ALERT)
    context.alert_reason = reason
    context.log.append(f"failure: {reason}")
    return context


def x_report_failure__mutmut_10(reason: str, severity: str = "high") -> IncidentContext:
    if severity == "critical":
        context = IncidentContext(state=IncidentState.DEGRADED, )
        context.alert_reason = reason
        context.log.append(f"critical failure: {reason}")
        return context
    context = IncidentContext(state=IncidentState.ALERT)
    context.alert_reason = reason
    context.log.append(f"failure: {reason}")
    return context


def x_report_failure__mutmut_11(reason: str, severity: str = "high") -> IncidentContext:
    if severity == "critical":
        context = IncidentContext(state=IncidentState.DEGRADED, degraded_mode=False)
        context.alert_reason = reason
        context.log.append(f"critical failure: {reason}")
        return context
    context = IncidentContext(state=IncidentState.ALERT)
    context.alert_reason = reason
    context.log.append(f"failure: {reason}")
    return context


def x_report_failure__mutmut_12(reason: str, severity: str = "high") -> IncidentContext:
    if severity == "critical":
        context = IncidentContext(state=IncidentState.DEGRADED, degraded_mode=True)
        context.alert_reason = None
        context.log.append(f"critical failure: {reason}")
        return context
    context = IncidentContext(state=IncidentState.ALERT)
    context.alert_reason = reason
    context.log.append(f"failure: {reason}")
    return context


def x_report_failure__mutmut_13(reason: str, severity: str = "high") -> IncidentContext:
    if severity == "critical":
        context = IncidentContext(state=IncidentState.DEGRADED, degraded_mode=True)
        context.alert_reason = reason
        context.log.append(None)
        return context
    context = IncidentContext(state=IncidentState.ALERT)
    context.alert_reason = reason
    context.log.append(f"failure: {reason}")
    return context


def x_report_failure__mutmut_14(reason: str, severity: str = "high") -> IncidentContext:
    if severity == "critical":
        context = IncidentContext(state=IncidentState.DEGRADED, degraded_mode=True)
        context.alert_reason = reason
        context.log.append(f"critical failure: {reason}")
        return context
    context = None
    context.alert_reason = reason
    context.log.append(f"failure: {reason}")
    return context


def x_report_failure__mutmut_15(reason: str, severity: str = "high") -> IncidentContext:
    if severity == "critical":
        context = IncidentContext(state=IncidentState.DEGRADED, degraded_mode=True)
        context.alert_reason = reason
        context.log.append(f"critical failure: {reason}")
        return context
    context = IncidentContext(state=None)
    context.alert_reason = reason
    context.log.append(f"failure: {reason}")
    return context


def x_report_failure__mutmut_16(reason: str, severity: str = "high") -> IncidentContext:
    if severity == "critical":
        context = IncidentContext(state=IncidentState.DEGRADED, degraded_mode=True)
        context.alert_reason = reason
        context.log.append(f"critical failure: {reason}")
        return context
    context = IncidentContext(state=IncidentState.ALERT)
    context.alert_reason = None
    context.log.append(f"failure: {reason}")
    return context


def x_report_failure__mutmut_17(reason: str, severity: str = "high") -> IncidentContext:
    if severity == "critical":
        context = IncidentContext(state=IncidentState.DEGRADED, degraded_mode=True)
        context.alert_reason = reason
        context.log.append(f"critical failure: {reason}")
        return context
    context = IncidentContext(state=IncidentState.ALERT)
    context.alert_reason = reason
    context.log.append(None)
    return context

x_report_failure__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_report_failure__mutmut_1': x_report_failure__mutmut_1, 
    'x_report_failure__mutmut_2': x_report_failure__mutmut_2, 
    'x_report_failure__mutmut_3': x_report_failure__mutmut_3, 
    'x_report_failure__mutmut_4': x_report_failure__mutmut_4, 
    'x_report_failure__mutmut_5': x_report_failure__mutmut_5, 
    'x_report_failure__mutmut_6': x_report_failure__mutmut_6, 
    'x_report_failure__mutmut_7': x_report_failure__mutmut_7, 
    'x_report_failure__mutmut_8': x_report_failure__mutmut_8, 
    'x_report_failure__mutmut_9': x_report_failure__mutmut_9, 
    'x_report_failure__mutmut_10': x_report_failure__mutmut_10, 
    'x_report_failure__mutmut_11': x_report_failure__mutmut_11, 
    'x_report_failure__mutmut_12': x_report_failure__mutmut_12, 
    'x_report_failure__mutmut_13': x_report_failure__mutmut_13, 
    'x_report_failure__mutmut_14': x_report_failure__mutmut_14, 
    'x_report_failure__mutmut_15': x_report_failure__mutmut_15, 
    'x_report_failure__mutmut_16': x_report_failure__mutmut_16, 
    'x_report_failure__mutmut_17': x_report_failure__mutmut_17
}
x_report_failure__mutmut_orig.__name__ = 'x_report_failure'


def is_read_only(context: IncidentContext) -> bool:
    args = [context]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_read_only__mutmut_orig, x_is_read_only__mutmut_mutants, args, kwargs, None)


def x_is_read_only__mutmut_orig(context: IncidentContext) -> bool:
    return context.state in (IncidentState.DEGRADED, IncidentState.LOCKED)


def x_is_read_only__mutmut_1(context: IncidentContext) -> bool:
    return context.state not in (IncidentState.DEGRADED, IncidentState.LOCKED)

x_is_read_only__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_is_read_only__mutmut_1': x_is_read_only__mutmut_1
}
x_is_read_only__mutmut_orig.__name__ = 'x_is_read_only'


def get_alert_message(context: IncidentContext) -> str:
    args = [context]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_get_alert_message__mutmut_orig, x_get_alert_message__mutmut_mutants, args, kwargs, None)


def x_get_alert_message__mutmut_orig(context: IncidentContext) -> str:
    if context.state == IncidentState.ALERT:
        return f"ALERT: {context.alert_reason or 'Unknown alert'}"
    if context.state == IncidentState.DEGRADED:
        return f"DEGRADED MODE (read-only): {context.alert_reason or 'Multiple mitigation failures'}"
    if context.state == IncidentState.LOCKED:
        return f"LOCKED: System is locked due to security incident. {context.alert_reason or ''}"
    return "NORMAL: No active incidents"


def x_get_alert_message__mutmut_1(context: IncidentContext) -> str:
    if context.state != IncidentState.ALERT:
        return f"ALERT: {context.alert_reason or 'Unknown alert'}"
    if context.state == IncidentState.DEGRADED:
        return f"DEGRADED MODE (read-only): {context.alert_reason or 'Multiple mitigation failures'}"
    if context.state == IncidentState.LOCKED:
        return f"LOCKED: System is locked due to security incident. {context.alert_reason or ''}"
    return "NORMAL: No active incidents"


def x_get_alert_message__mutmut_2(context: IncidentContext) -> str:
    if context.state == IncidentState.ALERT:
        return f"ALERT: {context.alert_reason and 'Unknown alert'}"
    if context.state == IncidentState.DEGRADED:
        return f"DEGRADED MODE (read-only): {context.alert_reason or 'Multiple mitigation failures'}"
    if context.state == IncidentState.LOCKED:
        return f"LOCKED: System is locked due to security incident. {context.alert_reason or ''}"
    return "NORMAL: No active incidents"


def x_get_alert_message__mutmut_3(context: IncidentContext) -> str:
    if context.state == IncidentState.ALERT:
        return f"ALERT: {context.alert_reason or 'XXUnknown alertXX'}"
    if context.state == IncidentState.DEGRADED:
        return f"DEGRADED MODE (read-only): {context.alert_reason or 'Multiple mitigation failures'}"
    if context.state == IncidentState.LOCKED:
        return f"LOCKED: System is locked due to security incident. {context.alert_reason or ''}"
    return "NORMAL: No active incidents"


def x_get_alert_message__mutmut_4(context: IncidentContext) -> str:
    if context.state == IncidentState.ALERT:
        return f"ALERT: {context.alert_reason or 'unknown alert'}"
    if context.state == IncidentState.DEGRADED:
        return f"DEGRADED MODE (read-only): {context.alert_reason or 'Multiple mitigation failures'}"
    if context.state == IncidentState.LOCKED:
        return f"LOCKED: System is locked due to security incident. {context.alert_reason or ''}"
    return "NORMAL: No active incidents"


def x_get_alert_message__mutmut_5(context: IncidentContext) -> str:
    if context.state == IncidentState.ALERT:
        return f"ALERT: {context.alert_reason or 'UNKNOWN ALERT'}"
    if context.state == IncidentState.DEGRADED:
        return f"DEGRADED MODE (read-only): {context.alert_reason or 'Multiple mitigation failures'}"
    if context.state == IncidentState.LOCKED:
        return f"LOCKED: System is locked due to security incident. {context.alert_reason or ''}"
    return "NORMAL: No active incidents"


def x_get_alert_message__mutmut_6(context: IncidentContext) -> str:
    if context.state == IncidentState.ALERT:
        return f"ALERT: {context.alert_reason or 'Unknown alert'}"
    if context.state != IncidentState.DEGRADED:
        return f"DEGRADED MODE (read-only): {context.alert_reason or 'Multiple mitigation failures'}"
    if context.state == IncidentState.LOCKED:
        return f"LOCKED: System is locked due to security incident. {context.alert_reason or ''}"
    return "NORMAL: No active incidents"


def x_get_alert_message__mutmut_7(context: IncidentContext) -> str:
    if context.state == IncidentState.ALERT:
        return f"ALERT: {context.alert_reason or 'Unknown alert'}"
    if context.state == IncidentState.DEGRADED:
        return f"DEGRADED MODE (read-only): {context.alert_reason and 'Multiple mitigation failures'}"
    if context.state == IncidentState.LOCKED:
        return f"LOCKED: System is locked due to security incident. {context.alert_reason or ''}"
    return "NORMAL: No active incidents"


def x_get_alert_message__mutmut_8(context: IncidentContext) -> str:
    if context.state == IncidentState.ALERT:
        return f"ALERT: {context.alert_reason or 'Unknown alert'}"
    if context.state == IncidentState.DEGRADED:
        return f"DEGRADED MODE (read-only): {context.alert_reason or 'XXMultiple mitigation failuresXX'}"
    if context.state == IncidentState.LOCKED:
        return f"LOCKED: System is locked due to security incident. {context.alert_reason or ''}"
    return "NORMAL: No active incidents"


def x_get_alert_message__mutmut_9(context: IncidentContext) -> str:
    if context.state == IncidentState.ALERT:
        return f"ALERT: {context.alert_reason or 'Unknown alert'}"
    if context.state == IncidentState.DEGRADED:
        return f"DEGRADED MODE (read-only): {context.alert_reason or 'multiple mitigation failures'}"
    if context.state == IncidentState.LOCKED:
        return f"LOCKED: System is locked due to security incident. {context.alert_reason or ''}"
    return "NORMAL: No active incidents"


def x_get_alert_message__mutmut_10(context: IncidentContext) -> str:
    if context.state == IncidentState.ALERT:
        return f"ALERT: {context.alert_reason or 'Unknown alert'}"
    if context.state == IncidentState.DEGRADED:
        return f"DEGRADED MODE (read-only): {context.alert_reason or 'MULTIPLE MITIGATION FAILURES'}"
    if context.state == IncidentState.LOCKED:
        return f"LOCKED: System is locked due to security incident. {context.alert_reason or ''}"
    return "NORMAL: No active incidents"


def x_get_alert_message__mutmut_11(context: IncidentContext) -> str:
    if context.state == IncidentState.ALERT:
        return f"ALERT: {context.alert_reason or 'Unknown alert'}"
    if context.state == IncidentState.DEGRADED:
        return f"DEGRADED MODE (read-only): {context.alert_reason or 'Multiple mitigation failures'}"
    if context.state != IncidentState.LOCKED:
        return f"LOCKED: System is locked due to security incident. {context.alert_reason or ''}"
    return "NORMAL: No active incidents"


def x_get_alert_message__mutmut_12(context: IncidentContext) -> str:
    if context.state == IncidentState.ALERT:
        return f"ALERT: {context.alert_reason or 'Unknown alert'}"
    if context.state == IncidentState.DEGRADED:
        return f"DEGRADED MODE (read-only): {context.alert_reason or 'Multiple mitigation failures'}"
    if context.state == IncidentState.LOCKED:
        return f"LOCKED: System is locked due to security incident. {context.alert_reason and ''}"
    return "NORMAL: No active incidents"


def x_get_alert_message__mutmut_13(context: IncidentContext) -> str:
    if context.state == IncidentState.ALERT:
        return f"ALERT: {context.alert_reason or 'Unknown alert'}"
    if context.state == IncidentState.DEGRADED:
        return f"DEGRADED MODE (read-only): {context.alert_reason or 'Multiple mitigation failures'}"
    if context.state == IncidentState.LOCKED:
        return f"LOCKED: System is locked due to security incident. {context.alert_reason or 'XXXX'}"
    return "NORMAL: No active incidents"


def x_get_alert_message__mutmut_14(context: IncidentContext) -> str:
    if context.state == IncidentState.ALERT:
        return f"ALERT: {context.alert_reason or 'Unknown alert'}"
    if context.state == IncidentState.DEGRADED:
        return f"DEGRADED MODE (read-only): {context.alert_reason or 'Multiple mitigation failures'}"
    if context.state == IncidentState.LOCKED:
        return f"LOCKED: System is locked due to security incident. {context.alert_reason or ''}"
    return "XXNORMAL: No active incidentsXX"


def x_get_alert_message__mutmut_15(context: IncidentContext) -> str:
    if context.state == IncidentState.ALERT:
        return f"ALERT: {context.alert_reason or 'Unknown alert'}"
    if context.state == IncidentState.DEGRADED:
        return f"DEGRADED MODE (read-only): {context.alert_reason or 'Multiple mitigation failures'}"
    if context.state == IncidentState.LOCKED:
        return f"LOCKED: System is locked due to security incident. {context.alert_reason or ''}"
    return "normal: no active incidents"


def x_get_alert_message__mutmut_16(context: IncidentContext) -> str:
    if context.state == IncidentState.ALERT:
        return f"ALERT: {context.alert_reason or 'Unknown alert'}"
    if context.state == IncidentState.DEGRADED:
        return f"DEGRADED MODE (read-only): {context.alert_reason or 'Multiple mitigation failures'}"
    if context.state == IncidentState.LOCKED:
        return f"LOCKED: System is locked due to security incident. {context.alert_reason or ''}"
    return "NORMAL: NO ACTIVE INCIDENTS"

x_get_alert_message__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_get_alert_message__mutmut_1': x_get_alert_message__mutmut_1, 
    'x_get_alert_message__mutmut_2': x_get_alert_message__mutmut_2, 
    'x_get_alert_message__mutmut_3': x_get_alert_message__mutmut_3, 
    'x_get_alert_message__mutmut_4': x_get_alert_message__mutmut_4, 
    'x_get_alert_message__mutmut_5': x_get_alert_message__mutmut_5, 
    'x_get_alert_message__mutmut_6': x_get_alert_message__mutmut_6, 
    'x_get_alert_message__mutmut_7': x_get_alert_message__mutmut_7, 
    'x_get_alert_message__mutmut_8': x_get_alert_message__mutmut_8, 
    'x_get_alert_message__mutmut_9': x_get_alert_message__mutmut_9, 
    'x_get_alert_message__mutmut_10': x_get_alert_message__mutmut_10, 
    'x_get_alert_message__mutmut_11': x_get_alert_message__mutmut_11, 
    'x_get_alert_message__mutmut_12': x_get_alert_message__mutmut_12, 
    'x_get_alert_message__mutmut_13': x_get_alert_message__mutmut_13, 
    'x_get_alert_message__mutmut_14': x_get_alert_message__mutmut_14, 
    'x_get_alert_message__mutmut_15': x_get_alert_message__mutmut_15, 
    'x_get_alert_message__mutmut_16': x_get_alert_message__mutmut_16
}
x_get_alert_message__mutmut_orig.__name__ = 'x_get_alert_message'
