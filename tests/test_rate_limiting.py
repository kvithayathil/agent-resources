"""Tests for BC-6: Rate Limiting and Resource Budgets."""

import pytest

from security_layer.budget import (
    add_tokens,
    check_budget,
    check_daily_budget,
    estimate_cost,
    record_error,
    record_success,
    record_tool_call,
)
from security_layer.models import BudgetLimits, BudgetState


class TestCheckBudget:
    """Tests for check_budget function."""

    def test_fresh_budget_is_within_limits(self):
        """Zero usage should be within budget."""
        state = BudgetState()
        limits = BudgetLimits()
        within_budget, reason = check_budget(state, limits)
        assert within_budget
        assert reason == ""

    def test_token_budget_exceeded(self):
        """Tokens used exceeding max_tokens should be over budget."""
        state = BudgetState(
            tokens_used=600_000, tool_calls=0, consecutive_errors=0, cost_usd=1.0
        )
        limits = BudgetLimits()
        within_budget, reason = check_budget(state, limits)
        assert not within_budget
        assert "token" in reason.lower()

    def test_tool_call_limit_per_turn_exceeded(self):
        """Tool calls exceeding max_tool_calls_per_turn should be over budget."""
        state = BudgetState(
            tokens_used=1000, tool_calls=21, consecutive_errors=0, cost_usd=1.0
        )
        limits = BudgetLimits()
        within_budget, reason = check_budget(state, limits)
        assert not within_budget
        assert "tool calls" in reason.lower()

    def test_consecutive_errors_exceeded(self):
        """Consecutive errors exceeding max_consecutive_errors should be over budget."""
        state = BudgetState(
            tokens_used=1000, tool_calls=0, consecutive_errors=6, cost_usd=1.0
        )
        limits = BudgetLimits()
        within_budget, reason = check_budget(state, limits)
        assert not within_budget
        assert "error" in reason.lower()

    def test_cost_budget_exceeded(self):
        """Cost exceeding max_cost_usd should be over budget."""
        state = BudgetState(
            tokens_used=1000, tool_calls=0, consecutive_errors=0, cost_usd=15.0
        )
        limits = BudgetLimits()
        within_budget, reason = check_budget(state, limits)
        assert not within_budget
        assert "cost" in reason.lower()

    def test_custom_limits_override_defaults(self):
        """Custom BudgetLimits should enforce custom thresholds."""
        state = BudgetState(
            tokens_used=600_000, tool_calls=0, consecutive_errors=0, cost_usd=1.0
        )
        limits = BudgetLimits(max_tokens=1_000_000)
        within_budget, reason = check_budget(state, limits)
        assert within_budget
        assert reason == ""

    def test_multiple_budgets_checked_independently(self):
        """Tokens OK but cost exceeded should still be over budget."""
        state = BudgetState(
            tokens_used=1000, tool_calls=0, consecutive_errors=0, cost_usd=15.0
        )
        limits = BudgetLimits()
        within_budget, reason = check_budget(state, limits)
        assert not within_budget
        assert "cost" in reason.lower()


class TestAddTokens:
    """Tests for add_tokens function."""

    def test_add_tokens_within_budget(self):
        """Adding 1000 tokens should succeed and stay within budget."""
        state = BudgetState(
            tokens_used=1000, tool_calls=0, consecutive_errors=0, cost_usd=0.5
        )
        limits = BudgetLimits()
        new_state, within_budget = add_tokens(state, 1000, limits)
        assert within_budget
        assert new_state.tokens_used == 2000

    def test_add_tokens_exact_limit(self):
        """Adding tokens to exactly max_tokens should be within budget."""
        state = BudgetState(
            tokens_used=400_000, tool_calls=0, consecutive_errors=0, cost_usd=1.0
        )
        limits = BudgetLimits()
        new_state, within_budget = add_tokens(state, 100_000, limits)
        assert within_budget
        assert new_state.tokens_used == 500_000

    def test_add_tokens_over_limit_hard_stop(self):
        """Adding tokens over max_tokens should hard stop (returns False)."""
        state = BudgetState(
            tokens_used=400_000, tool_calls=0, consecutive_errors=0, cost_usd=1.0
        )
        limits = BudgetLimits()
        new_state, within_budget = add_tokens(state, 200_000, limits)
        assert not within_budget
        assert new_state.tokens_used == 400_000


class TestRecordToolCall:
    """Tests for record_tool_call function."""

    def test_record_tool_call_increments(self):
        """Tool call counter should increment on each call."""
        state = BudgetState(
            tokens_used=1000, tool_calls=0, consecutive_errors=0, cost_usd=0.5
        )
        limits = BudgetLimits()
        new_state, within_budget = record_tool_call(state, limits)
        assert within_budget
        assert new_state.tool_calls == 1


class TestRecordError:
    """Tests for record_error function."""

    def test_record_error_increments(self):
        """Error counter should increment on each error."""
        state = BudgetState(
            tokens_used=1000, tool_calls=0, consecutive_errors=0, cost_usd=0.5
        )
        limits = BudgetLimits()
        new_state, within_budget = record_error(state, limits)
        assert within_budget
        assert new_state.consecutive_errors == 1


class TestRecordSuccess:
    """Tests for record_success function."""

    def test_record_success_resets_errors(self):
        """Success should reset consecutive errors to 0."""
        state = BudgetState(
            tokens_used=1000, tool_calls=0, consecutive_errors=3, cost_usd=0.5
        )
        new_state = record_success(state)
        assert new_state.consecutive_errors == 0
        assert new_state.tokens_used == 1000


class TestCheckDailyBudget:
    """Tests for check_daily_budget function."""

    def test_daily_budget_within(self):
        """Session cost + existing < daily limit should be allowed."""
        within_budget = check_daily_budget("user123", 2.0, 10.0)
        assert within_budget

    def test_daily_budget_exceeded(self):
        """Session cost + existing > daily limit should be denied."""
        within_budget = check_daily_budget("user123", 15.0, 10.0)
        assert not within_budget


class TestEstimateCost:
    """Tests for estimate_cost function."""

    def test_estimate_cost_default_model(self):
        """Estimate cost with default model."""
        cost = estimate_cost(1000)
        assert cost > 0
        assert isinstance(cost, float)

    def test_estimate_cost_custom_model(self):
        """Estimate cost with custom model."""
        cost = estimate_cost(1000, "gpt-4")
        assert cost > 0
        assert isinstance(cost, float)
