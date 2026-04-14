"""Tests for BC-5: Least-Privilege Tool Enforcement.

All tests are written to FAIL until implementation exists in security_layer.permissions.
"""

import pytest

from security_layer.state_machine import InvalidTransition
from security_layer.models import (
    AgentCapabilities,
    TaintFlag,
    ToolPermission,
)


class TestCapabilityStateTransitions:
    """Test state machine transitions for capability levels."""

    def test_capability_can_decrease_from_full_to_standard(self):
        """FULL → STANDARD transition should succeed."""
        from security_layer.permissions import (
            CapabilityEvent,
            CapabilityState,
            capability_sm,
        )

        context = {
            "capabilities": AgentCapabilities(allowed_paths=frozenset(["/workspace"]))
        }
        new_state = capability_sm.handle(
            context, CapabilityState.FULL, CapabilityEvent.RESTRICT_STANDARD
        )
        assert new_state == CapabilityState.STANDARD

    def test_capability_can_decrease_from_standard_to_read_only(self):
        """STANDARD → READ_ONLY transition should succeed."""
        from security_layer.permissions import (
            CapabilityEvent,
            CapabilityState,
            capability_sm,
        )

        context = {
            "capabilities": AgentCapabilities(allowed_paths=frozenset(["/workspace"]))
        }
        new_state = capability_sm.handle(
            context, CapabilityState.STANDARD, CapabilityEvent.RESTRICT_READ_ONLY
        )
        assert new_state == CapabilityState.READ_ONLY

    def test_capability_can_decrease_from_read_only_to_locked(self):
        """READ_ONLY → LOCKED transition should succeed."""
        from security_layer.permissions import (
            CapabilityEvent,
            CapabilityState,
            capability_sm,
        )

        context = {
            "capabilities": AgentCapabilities(allowed_paths=frozenset(["/workspace"]))
        }
        new_state = capability_sm.handle(
            context, CapabilityState.READ_ONLY, CapabilityEvent.LOCK
        )
        assert new_state == CapabilityState.LOCKED

    def test_capability_cannot_increase_from_standard_to_full(self):
        """STANDARD → FULL transition should raise InvalidTransition."""
        from security_layer.permissions import (
            CapabilityEvent,
            CapabilityState,
            capability_sm,
        )

        context = {
            "capabilities": AgentCapabilities(allowed_paths=frozenset(["/workspace"]))
        }
        with pytest.raises(InvalidTransition):
            capability_sm.handle(
                context, CapabilityState.STANDARD, CapabilityEvent.FULL
            )

    def test_capability_cannot_increase_from_read_only_to_standard(self):
        """READ_ONLY → STANDARD transition should raise InvalidTransition."""
        from security_layer.permissions import (
            CapabilityEvent,
            CapabilityState,
            capability_sm,
        )

        context = {
            "capabilities": AgentCapabilities(allowed_paths=frozenset(["/workspace"]))
        }
        with pytest.raises(InvalidTransition):
            capability_sm.handle(
                context, CapabilityState.READ_ONLY, CapabilityEvent.STANDARD
            )

    def test_capability_cannot_skip_lock_to_read_only(self):
        """LOCKED → any state transition should raise InvalidTransition."""
        from security_layer.permissions import (
            CapabilityEvent,
            CapabilityState,
            capability_sm,
        )

        context = {
            "capabilities": AgentCapabilities(allowed_paths=frozenset(["/workspace"]))
        }
        with pytest.raises(InvalidTransition):
            capability_sm.handle(
                context, CapabilityState.LOCKED, CapabilityEvent.READ_ONLY
            )


class TestPathSecurity:
    """Test path resolution and validation security checks."""

    def test_path_within_workspace_allowed(self):
        """Path within workspace should be allowed."""
        from security_layer.permissions import is_path_allowed, resolve_path

        path = "/workspace/src/main.py"
        workspace_root = "/workspace"
        resolved = resolve_path(path, workspace_root)
        assert resolved == "/workspace/src/main.py"
        assert is_path_allowed(path, workspace_root) is True

    def test_path_outside_workspace_denied(self):
        """Path outside workspace should be denied."""
        from security_layer.permissions import is_path_allowed

        path = "/etc/passwd"
        workspace_root = "/workspace"
        assert is_path_allowed(path, workspace_root) is False

    def test_path_traversal_denied(self):
        """Path traversal using ../ should be detected and denied."""
        from security_layer.permissions import check_path_traversal, is_path_allowed

        path = "/workspace/../../../etc/passwd"
        workspace_root = "/workspace"
        assert check_path_traversal(path) is True
        assert is_path_allowed(path, workspace_root) is False

    def test_symlink_escape_detected(self, tmp_path):
        """Symlink pointing outside workspace should be detected."""
        import os

        from security_layer.permissions import is_symlink_escape

        workspace = tmp_path / "workspace"
        workspace.mkdir()
        external = tmp_path / "external"
        external.mkdir()
        external_file = external / "secret.txt"
        external_file.write_text("secret")
        symlink_path = workspace / "escape_link"
        os.symlink(str(external_file), str(symlink_path))
        assert is_symlink_escape(str(symlink_path), str(workspace)) is True

    def test_symlink_inside_workspace_passes(self, tmp_path):
        """Symlink pointing inside workspace should not be flagged."""
        import os

        from security_layer.permissions import is_symlink_escape

        workspace = tmp_path / "workspace"
        workspace.mkdir()
        real_file = workspace / "real.txt"
        real_file.write_text("data")
        symlink_path = workspace / "link.txt"
        os.symlink(str(real_file), str(symlink_path))
        assert is_symlink_escape(str(symlink_path), str(workspace)) is False


class TestTaintTracking:
    """Test taint tracking for tool permissions."""

    def test_untrusted_data_cannot_flow_to_write(self):
        """UNTRUSTED data should not be allowed to flow to WRITE tools."""
        from security_layer.permissions import can_flow_to_destructive

        taint = TaintFlag.UNTRUSTED
        target_tool = ToolPermission.WRITE
        assert can_flow_to_destructive(taint, target_tool) is False

    def test_untrusted_data_cannot_flow_to_bash(self):
        """UNTRUSTED data should not be allowed to flow to BASH tools."""
        from security_layer.permissions import can_flow_to_destructive

        taint = TaintFlag.UNTRUSTED
        target_tool = ToolPermission.BASH
        assert can_flow_to_destructive(taint, target_tool) is False

    def test_untrusted_data_can_flow_to_read(self):
        """UNTRUSTED data should be allowed to flow to READ tools (non-destructive)."""
        from security_layer.permissions import can_flow_to_destructive

        taint = TaintFlag.UNTRUSTED
        target_tool = ToolPermission.READ
        assert can_flow_to_destructive(taint, target_tool) is True

    def test_clean_data_flows_to_any(self):
        """CLEAN data should be allowed to flow to any tool."""
        from security_layer.permissions import can_flow_to_destructive

        taint = TaintFlag.CLEAN
        for tool in ToolPermission:
            assert can_flow_to_destructive(taint, tool) is True


class TestCapabilityEscalation:
    """Test capability escalation (or lack thereof)."""

    def test_escalate_caps_decrease_succeeds(self):
        """Removing a tool from capabilities should succeed."""
        from security_layer.permissions import escalate_capabilities

        current = AgentCapabilities(
            allowed_tools=frozenset(
                [ToolPermission.READ, ToolPermission.WRITE, ToolPermission.BASH]
            ),
            allowed_paths=frozenset(["/workspace"]),
            workspace_root="/workspace",
            can_network=True,
            can_write=True,
        )
        requested = AgentCapabilities(
            allowed_tools=frozenset([ToolPermission.READ, ToolPermission.BASH]),
            allowed_paths=frozenset(["/workspace"]),
            workspace_root="/workspace",
            can_network=True,
            can_write=True,
        )
        new_caps, approved = escalate_capabilities(current, requested)
        assert approved is True
        assert ToolPermission.WRITE not in new_caps.allowed_tools

    def test_escalate_caps_increase_rejected(self):
        """Adding a tool to capabilities should be rejected."""
        from security_layer.permissions import escalate_capabilities

        current = AgentCapabilities(
            allowed_tools=frozenset([ToolPermission.READ, ToolPermission.BASH]),
            allowed_paths=frozenset(["/workspace"]),
            workspace_root="/workspace",
            can_network=False,
            can_write=False,
        )
        requested = AgentCapabilities(
            allowed_tools=frozenset(
                [ToolPermission.READ, ToolPermission.WRITE, ToolPermission.BASH]
            ),
            allowed_paths=frozenset(["/workspace"]),
            workspace_root="/workspace",
            can_network=False,
            can_write=False,
        )
        new_caps, approved = escalate_capabilities(current, requested)
        assert approved is False
        assert new_caps == current
