import os
from enum import StrEnum

from security_layer.models import AgentCapabilities, TaintFlag, ToolPermission
from security_layer.state_machine import StateMachine


class CapabilityState(StrEnum):
    FULL = "FULL"
    STANDARD = "STANDARD"
    READ_ONLY = "READ_ONLY"
    LOCKED = "LOCKED"


class CapabilityEvent(StrEnum):
    RESTRICT_STANDARD = "RESTRICT_STANDARD"
    RESTRICT_READ_ONLY = "RESTRICT_READ_ONLY"
    LOCK = "LOCK"
    FULL = "FULL"
    STANDARD = "STANDARD"
    READ_ONLY = "READ_ONLY"


def _noop(context):
    pass


capability_sm = StateMachine[CapabilityState, CapabilityEvent, dict]()
capability_sm.add_transition(CapabilityState.FULL, CapabilityEvent.RESTRICT_STANDARD, CapabilityState.STANDARD, _noop)
capability_sm.add_transition(
    CapabilityState.STANDARD, CapabilityEvent.RESTRICT_READ_ONLY, CapabilityState.READ_ONLY, _noop
)
capability_sm.add_transition(CapabilityState.READ_ONLY, CapabilityEvent.LOCK, CapabilityState.LOCKED, _noop)


def resolve_path(path: str, workspace_root: str) -> str:
    return os.path.normpath(path)


def is_path_allowed(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def check_path_traversal(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def is_symlink_escape(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = os.path.realpath(workspace_root)
    return not resolved.startswith(workspace)


def can_flow_to_destructive(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return True
    return target_tool not in (ToolPermission.WRITE, ToolPermission.BASH)


def escalate_capabilities(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True
