from security_layer.models import BudgetLimits, BudgetState

_DEFAULT_COST_PER_1K_TOKENS: dict[str, float] = {
    "default": 0.03,
    "gpt-4": 0.03,
    "gpt-4o": 0.005,
    "gpt-3.5-turbo": 0.002,
    "claude-3-opus": 0.015,
    "claude-3-sonnet": 0.003,
}


def check_budget(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def add_tokens(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
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


def record_tool_call(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def record_error(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def record_success(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=0,
        cost_usd=state.cost_usd,
    )


_daily_totals: dict[str, float] = {}


def check_daily_budget(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, 0.0)
    return (prior + session_cost) <= daily_limit


def estimate_cost(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate
