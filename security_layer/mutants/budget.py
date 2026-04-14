from security_layer.models import BudgetLimits, BudgetState

_DEFAULT_COST_PER_1K_TOKENS: dict[str, float] = {
    "default": 0.03,
    "gpt-4": 0.03,
    "gpt-4o": 0.005,
    "gpt-3.5-turbo": 0.002,
    "claude-3-opus": 0.015,
    "claude-3-sonnet": 0.003,
}
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


def check_budget(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_budget__mutmut_orig, x_check_budget__mutmut_mutants, args, kwargs, None)


def x_check_budget__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_check_budget__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_check_budget__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_check_budget__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_check_budget__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_check_budget__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_check_budget__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_check_budget__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_check_budget__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_check_budget__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_check_budget__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_check_budget__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_check_budget__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_check_budget__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_check_budget__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_check_budget__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_check_budget__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_check_budget__mutmut_17(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_check_budget__mutmut_18(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_check_budget__mutmut_19(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_check_budget__mutmut_20(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_check_budget__mutmut_21(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_check_budget__mutmut_22(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"

x_check_budget__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_check_budget__mutmut_1': x_check_budget__mutmut_1, 
    'x_check_budget__mutmut_2': x_check_budget__mutmut_2, 
    'x_check_budget__mutmut_3': x_check_budget__mutmut_3, 
    'x_check_budget__mutmut_4': x_check_budget__mutmut_4, 
    'x_check_budget__mutmut_5': x_check_budget__mutmut_5, 
    'x_check_budget__mutmut_6': x_check_budget__mutmut_6, 
    'x_check_budget__mutmut_7': x_check_budget__mutmut_7, 
    'x_check_budget__mutmut_8': x_check_budget__mutmut_8, 
    'x_check_budget__mutmut_9': x_check_budget__mutmut_9, 
    'x_check_budget__mutmut_10': x_check_budget__mutmut_10, 
    'x_check_budget__mutmut_11': x_check_budget__mutmut_11, 
    'x_check_budget__mutmut_12': x_check_budget__mutmut_12, 
    'x_check_budget__mutmut_13': x_check_budget__mutmut_13, 
    'x_check_budget__mutmut_14': x_check_budget__mutmut_14, 
    'x_check_budget__mutmut_15': x_check_budget__mutmut_15, 
    'x_check_budget__mutmut_16': x_check_budget__mutmut_16, 
    'x_check_budget__mutmut_17': x_check_budget__mutmut_17, 
    'x_check_budget__mutmut_18': x_check_budget__mutmut_18, 
    'x_check_budget__mutmut_19': x_check_budget__mutmut_19, 
    'x_check_budget__mutmut_20': x_check_budget__mutmut_20, 
    'x_check_budget__mutmut_21': x_check_budget__mutmut_21, 
    'x_check_budget__mutmut_22': x_check_budget__mutmut_22
}
x_check_budget__mutmut_orig.__name__ = 'x_check_budget'


def add_tokens(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_add_tokens__mutmut_orig, x_add_tokens__mutmut_mutants, args, kwargs, None)


def x_add_tokens__mutmut_orig(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_add_tokens__mutmut_1(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_add_tokens__mutmut_2(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_add_tokens__mutmut_3(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_add_tokens__mutmut_4(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_add_tokens__mutmut_5(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_add_tokens__mutmut_6(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_add_tokens__mutmut_7(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_add_tokens__mutmut_8(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_add_tokens__mutmut_9(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_add_tokens__mutmut_10(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_add_tokens__mutmut_11(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_add_tokens__mutmut_12(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_add_tokens__mutmut_13(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_add_tokens__mutmut_14(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_add_tokens__mutmut_15(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_add_tokens__mutmut_16(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_add_tokens__mutmut_17(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_add_tokens__mutmut_18(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_add_tokens__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_add_tokens__mutmut_1': x_add_tokens__mutmut_1, 
    'x_add_tokens__mutmut_2': x_add_tokens__mutmut_2, 
    'x_add_tokens__mutmut_3': x_add_tokens__mutmut_3, 
    'x_add_tokens__mutmut_4': x_add_tokens__mutmut_4, 
    'x_add_tokens__mutmut_5': x_add_tokens__mutmut_5, 
    'x_add_tokens__mutmut_6': x_add_tokens__mutmut_6, 
    'x_add_tokens__mutmut_7': x_add_tokens__mutmut_7, 
    'x_add_tokens__mutmut_8': x_add_tokens__mutmut_8, 
    'x_add_tokens__mutmut_9': x_add_tokens__mutmut_9, 
    'x_add_tokens__mutmut_10': x_add_tokens__mutmut_10, 
    'x_add_tokens__mutmut_11': x_add_tokens__mutmut_11, 
    'x_add_tokens__mutmut_12': x_add_tokens__mutmut_12, 
    'x_add_tokens__mutmut_13': x_add_tokens__mutmut_13, 
    'x_add_tokens__mutmut_14': x_add_tokens__mutmut_14, 
    'x_add_tokens__mutmut_15': x_add_tokens__mutmut_15, 
    'x_add_tokens__mutmut_16': x_add_tokens__mutmut_16, 
    'x_add_tokens__mutmut_17': x_add_tokens__mutmut_17, 
    'x_add_tokens__mutmut_18': x_add_tokens__mutmut_18
}
x_add_tokens__mutmut_orig.__name__ = 'x_add_tokens'


def record_tool_call(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_tool_call__mutmut_orig, x_record_tool_call__mutmut_mutants, args, kwargs, None)


def x_record_tool_call__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_record_tool_call__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_record_tool_call__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_record_tool_call__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_record_tool_call__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_record_tool_call__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_record_tool_call__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_record_tool_call__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_record_tool_call__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_record_tool_call__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_record_tool_call__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls - 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_record_tool_call__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 2,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_record_tool_call__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_record_tool_call__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_record_tool_call__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_record_tool_call__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_record_tool_call__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_record_tool_call__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_record_tool_call__mutmut_1': x_record_tool_call__mutmut_1, 
    'x_record_tool_call__mutmut_2': x_record_tool_call__mutmut_2, 
    'x_record_tool_call__mutmut_3': x_record_tool_call__mutmut_3, 
    'x_record_tool_call__mutmut_4': x_record_tool_call__mutmut_4, 
    'x_record_tool_call__mutmut_5': x_record_tool_call__mutmut_5, 
    'x_record_tool_call__mutmut_6': x_record_tool_call__mutmut_6, 
    'x_record_tool_call__mutmut_7': x_record_tool_call__mutmut_7, 
    'x_record_tool_call__mutmut_8': x_record_tool_call__mutmut_8, 
    'x_record_tool_call__mutmut_9': x_record_tool_call__mutmut_9, 
    'x_record_tool_call__mutmut_10': x_record_tool_call__mutmut_10, 
    'x_record_tool_call__mutmut_11': x_record_tool_call__mutmut_11, 
    'x_record_tool_call__mutmut_12': x_record_tool_call__mutmut_12, 
    'x_record_tool_call__mutmut_13': x_record_tool_call__mutmut_13, 
    'x_record_tool_call__mutmut_14': x_record_tool_call__mutmut_14, 
    'x_record_tool_call__mutmut_15': x_record_tool_call__mutmut_15, 
    'x_record_tool_call__mutmut_16': x_record_tool_call__mutmut_16
}
x_record_tool_call__mutmut_orig.__name__ = 'x_record_tool_call'


def record_error(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_error__mutmut_orig, x_record_error__mutmut_mutants, args, kwargs, None)


def x_record_error__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_record_error__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_record_error__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_record_error__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_record_error__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_record_error__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_record_error__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_record_error__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_record_error__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_record_error__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_record_error__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors - 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_record_error__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 2,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_record_error__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_record_error__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_record_error__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_record_error__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_record_error__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_record_error__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_record_error__mutmut_1': x_record_error__mutmut_1, 
    'x_record_error__mutmut_2': x_record_error__mutmut_2, 
    'x_record_error__mutmut_3': x_record_error__mutmut_3, 
    'x_record_error__mutmut_4': x_record_error__mutmut_4, 
    'x_record_error__mutmut_5': x_record_error__mutmut_5, 
    'x_record_error__mutmut_6': x_record_error__mutmut_6, 
    'x_record_error__mutmut_7': x_record_error__mutmut_7, 
    'x_record_error__mutmut_8': x_record_error__mutmut_8, 
    'x_record_error__mutmut_9': x_record_error__mutmut_9, 
    'x_record_error__mutmut_10': x_record_error__mutmut_10, 
    'x_record_error__mutmut_11': x_record_error__mutmut_11, 
    'x_record_error__mutmut_12': x_record_error__mutmut_12, 
    'x_record_error__mutmut_13': x_record_error__mutmut_13, 
    'x_record_error__mutmut_14': x_record_error__mutmut_14, 
    'x_record_error__mutmut_15': x_record_error__mutmut_15, 
    'x_record_error__mutmut_16': x_record_error__mutmut_16
}
x_record_error__mutmut_orig.__name__ = 'x_record_error'


def record_success(state: BudgetState) -> BudgetState:
    args = [state]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_success__mutmut_orig, x_record_success__mutmut_mutants, args, kwargs, None)


def x_record_success__mutmut_orig(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=0,
        cost_usd=state.cost_usd,
    )


def x_record_success__mutmut_1(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=0,
        cost_usd=state.cost_usd,
    )


def x_record_success__mutmut_2(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=0,
        cost_usd=state.cost_usd,
    )


def x_record_success__mutmut_3(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )


def x_record_success__mutmut_4(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=0,
        cost_usd=None,
    )


def x_record_success__mutmut_5(state: BudgetState) -> BudgetState:
    return BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=0,
        cost_usd=state.cost_usd,
    )


def x_record_success__mutmut_6(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=0,
        cost_usd=state.cost_usd,
    )


def x_record_success__mutmut_7(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )


def x_record_success__mutmut_8(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=0,
        )


def x_record_success__mutmut_9(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=1,
        cost_usd=state.cost_usd,
    )

x_record_success__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_record_success__mutmut_1': x_record_success__mutmut_1, 
    'x_record_success__mutmut_2': x_record_success__mutmut_2, 
    'x_record_success__mutmut_3': x_record_success__mutmut_3, 
    'x_record_success__mutmut_4': x_record_success__mutmut_4, 
    'x_record_success__mutmut_5': x_record_success__mutmut_5, 
    'x_record_success__mutmut_6': x_record_success__mutmut_6, 
    'x_record_success__mutmut_7': x_record_success__mutmut_7, 
    'x_record_success__mutmut_8': x_record_success__mutmut_8, 
    'x_record_success__mutmut_9': x_record_success__mutmut_9
}
x_record_success__mutmut_orig.__name__ = 'x_record_success'


_daily_totals: dict[str, float] = {}


def check_daily_budget(user_id: str, session_cost: float, daily_limit: float) -> bool:
    args = [user_id, session_cost, daily_limit]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_daily_budget__mutmut_orig, x_check_daily_budget__mutmut_mutants, args, kwargs, None)


def x_check_daily_budget__mutmut_orig(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, 0.0)
    return (prior + session_cost) <= daily_limit


def x_check_daily_budget__mutmut_1(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = None
    return (prior + session_cost) <= daily_limit


def x_check_daily_budget__mutmut_2(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(None, 0.0)
    return (prior + session_cost) <= daily_limit


def x_check_daily_budget__mutmut_3(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, None)
    return (prior + session_cost) <= daily_limit


def x_check_daily_budget__mutmut_4(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(0.0)
    return (prior + session_cost) <= daily_limit


def x_check_daily_budget__mutmut_5(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, )
    return (prior + session_cost) <= daily_limit


def x_check_daily_budget__mutmut_6(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, 1.0)
    return (prior + session_cost) <= daily_limit


def x_check_daily_budget__mutmut_7(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, 0.0)
    return (prior - session_cost) <= daily_limit


def x_check_daily_budget__mutmut_8(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, 0.0)
    return (prior + session_cost) < daily_limit

x_check_daily_budget__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_check_daily_budget__mutmut_1': x_check_daily_budget__mutmut_1, 
    'x_check_daily_budget__mutmut_2': x_check_daily_budget__mutmut_2, 
    'x_check_daily_budget__mutmut_3': x_check_daily_budget__mutmut_3, 
    'x_check_daily_budget__mutmut_4': x_check_daily_budget__mutmut_4, 
    'x_check_daily_budget__mutmut_5': x_check_daily_budget__mutmut_5, 
    'x_check_daily_budget__mutmut_6': x_check_daily_budget__mutmut_6, 
    'x_check_daily_budget__mutmut_7': x_check_daily_budget__mutmut_7, 
    'x_check_daily_budget__mutmut_8': x_check_daily_budget__mutmut_8
}
x_check_daily_budget__mutmut_orig.__name__ = 'x_check_daily_budget'


def estimate_cost(tokens: int, model: str = "default") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_estimate_cost__mutmut_orig, x_estimate_cost__mutmut_mutants, args, kwargs, None)


def x_estimate_cost__mutmut_orig(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_estimate_cost__mutmut_1(tokens: int, model: str = "XXdefaultXX") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_estimate_cost__mutmut_2(tokens: int, model: str = "DEFAULT") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_estimate_cost__mutmut_3(tokens: int, model: str = "default") -> float:
    rate = None
    return (tokens / 1000) * rate


def x_estimate_cost__mutmut_4(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(None, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_estimate_cost__mutmut_5(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, None)
    return (tokens / 1000) * rate


def x_estimate_cost__mutmut_6(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(_DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_estimate_cost__mutmut_7(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, )
    return (tokens / 1000) * rate


def x_estimate_cost__mutmut_8(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["XXdefaultXX"])
    return (tokens / 1000) * rate


def x_estimate_cost__mutmut_9(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["DEFAULT"])
    return (tokens / 1000) * rate


def x_estimate_cost__mutmut_10(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) / rate


def x_estimate_cost__mutmut_11(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens * 1000) * rate


def x_estimate_cost__mutmut_12(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1001) * rate

x_estimate_cost__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_estimate_cost__mutmut_1': x_estimate_cost__mutmut_1, 
    'x_estimate_cost__mutmut_2': x_estimate_cost__mutmut_2, 
    'x_estimate_cost__mutmut_3': x_estimate_cost__mutmut_3, 
    'x_estimate_cost__mutmut_4': x_estimate_cost__mutmut_4, 
    'x_estimate_cost__mutmut_5': x_estimate_cost__mutmut_5, 
    'x_estimate_cost__mutmut_6': x_estimate_cost__mutmut_6, 
    'x_estimate_cost__mutmut_7': x_estimate_cost__mutmut_7, 
    'x_estimate_cost__mutmut_8': x_estimate_cost__mutmut_8, 
    'x_estimate_cost__mutmut_9': x_estimate_cost__mutmut_9, 
    'x_estimate_cost__mutmut_10': x_estimate_cost__mutmut_10, 
    'x_estimate_cost__mutmut_11': x_estimate_cost__mutmut_11, 
    'x_estimate_cost__mutmut_12': x_estimate_cost__mutmut_12
}
x_estimate_cost__mutmut_orig.__name__ = 'x_estimate_cost'
