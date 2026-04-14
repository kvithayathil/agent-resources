"""Test BC-7: Human-in-the-Loop for Destructive Actions.

All tests are designed to FAIL initially and should pass after implementation.
"""

import time
from dataclasses import replace

import pytest

from security_layer.hitl import (
    approve,
    check_approval,
    check_timeout,
    deny,
    is_destructive,
    process_destructive_action,
    request_approval,
)
from security_layer.types import DESTRUCTIVE_ACTIONS, HITLRequest


class TestIsDestructive:
    """Test is_destructive function."""

    def test_git_push_is_destructive(self):
        """git_push should be classified as destructive."""
        assert is_destructive("git_push") is True

    def test_shell_rm_is_destructive(self):
        """shell_rm should be classified as destructive."""
        assert is_destructive("shell_rm") is True

    def test_file_write_outside_workspace_is_destructive(self):
        """file_write_outside_workspace should be classified as destructive."""
        assert is_destructive("file_write_outside_workspace") is True

    def test_bulk_operation_is_destructive(self):
        """bulk_operation should be classified as destructive."""
        assert is_destructive("bulk_operation") is True

    def test_file_read_is_not_destructive(self):
        """file_read should NOT be classified as destructive."""
        assert is_destructive("file_read") is False

    def test_glob_is_not_destructive(self):
        """glob should NOT be classified as destructive."""
        assert is_destructive("glob") is False


class TestRequestApproval:
    """Test request_approval function."""

    def test_request_approval_returns_id(self):
        """request_approval should create a request and return a non-empty ID."""
        request = HITLRequest(
            action="git_push",
            target="origin/main",
            reason="Pushing critical bugfix",
        )
        request_id = request_approval(request)
        assert request_id
        assert isinstance(request_id, str)
        assert len(request_id) > 0

    def test_pending_approval_blocks_action(self):
        """Unapproved request should block the action."""
        request = HITLRequest(
            action="git_push",
            target="origin/main",
            reason="Pushing changes",
        )
        request_id = request_approval(request)
        status = check_approval(request_id)
        assert status == "pending"


class TestApprovalActions:
    """Test approve and deny functions."""

    def test_approved_allows_action(self):
        """Approving a request should allow the action."""
        request = HITLRequest(
            action="git_push",
            target="origin/main",
            reason="Pushing changes",
        )
        request_id = request_approval(request)
        result = approve(request_id)
        assert result is True
        status = check_approval(request_id)
        assert status == "approved"

    def test_denied_blocks_action(self):
        """Denying a request should block the action."""
        request = HITLRequest(
            action="git_push",
            target="origin/main",
            reason="Pushing changes",
        )
        request_id = request_approval(request)
        result = deny(request_id)
        assert result is True
        status = check_approval(request_id)
        assert status == "denied"


class TestTimeout:
    """Test timeout handling."""

    def test_timeout_auto_denies(self):
        """Timeout should auto-deny when auto_deny=True (default)."""
        request = HITLRequest(
            action="git_push",
            target="origin/main",
            reason="Pushing changes",
            timeout_minutes=1,
            auto_deny=True,
        )
        created_at = time.time() - 61  # 61 seconds ago (1 minute + 1 second)
        current_time = time.time()
        is_timed_out = check_timeout(request, created_at, current_time)
        assert is_timed_out is True

    def test_no_timeout_auto_deny_when_disabled(self):
        """When auto_deny=False, timeout should still leave request pending."""
        request = HITLRequest(
            action="git_push",
            target="origin/main",
            reason="Pushing changes",
            timeout_minutes=1,
            auto_deny=False,
        )
        created_at = time.time() - 61  # 61 seconds ago
        current_time = time.time()
        is_timed_out = check_timeout(request, created_at, current_time)
        # The timeout check should return True (it IS timed out),
        # but the request should NOT be auto-denied
        assert is_timed_out is True

    def test_timeout_default_is_30_minutes(self):
        """Default HITLRequest should have timeout_minutes=30."""
        request = HITLRequest(
            action="git_push",
            target="origin/main",
            reason="Pushing changes",
        )
        assert request.timeout_minutes == 30


class TestMultipleRequests:
    """Test handling multiple independent requests."""

    def test_multiple_requests_tracked_independently(self):
        """Multiple requests should be tracked independently."""
        request1 = HITLRequest(
            action="git_push",
            target="origin/main",
            reason="First push",
        )
        request2 = HITLRequest(
            action="shell_rm",
            target="/tmp/test.txt",
            reason="Cleanup",
        )

        request_id1 = request_approval(request1)
        request_id2 = request_approval(request2)

        # Approve first request
        assert approve(request_id1) is True
        assert check_approval(request_id1) == "approved"

        # Deny second request
        assert deny(request_id2) is True
        assert check_approval(request_id2) == "denied"

        # Verify independence
        assert check_approval(request_id1) == "approved"
        assert check_approval(request_id2) == "denied"


class TestProcessDestructiveAction:
    """Test process_destructive_action combined function."""

    def test_process_destructive_action_with_approval(self):
        """Should allow action after approval."""
        request = HITLRequest(
            action="git_push",
            target="origin/main",
            reason="Pushing changes",
            timeout_minutes=1,
        )
        request_id = request_approval(request)
        approve(request_id)

        allowed, reason = process_destructive_action(
            "git_push", "origin/main", "Pushing changes"
        )
        assert allowed is True

    def test_process_destructive_action_with_denial(self):
        """Should block action when denied."""
        request = HITLRequest(
            action="git_push",
            target="origin/main",
            reason="Pushing changes",
        )
        request_id = request_approval(request)
        deny(request_id)

        allowed, reason = process_destructive_action(
            "git_push", "origin/main", "Pushing changes"
        )
        assert allowed is False

    def test_process_destructive_action_non_destructive(self):
        """Non-destructive actions should be allowed without approval."""
        allowed, reason = process_destructive_action(
            "file_read", "/path/to/file.txt", "Reading file"
        )
        assert allowed is True
