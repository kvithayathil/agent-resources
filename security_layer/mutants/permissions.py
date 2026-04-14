import os
import re
from enum import Enum

from security_layer.state_machine import StateMachine
from security_layer.models import AgentCapabilities, TaintFlag, ToolPermission
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


class CapabilityState(str, Enum):
    FULL = "FULL"
    STANDARD = "STANDARD"
    READ_ONLY = "READ_ONLY"
    LOCKED = "LOCKED"


class CapabilityEvent(str, Enum):
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
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_resolve_path__mutmut_orig, x_resolve_path__mutmut_mutants, args, kwargs, None)


def x_resolve_path__mutmut_orig(path: str, workspace_root: str) -> str:
    return os.path.normpath(path)


def x_resolve_path__mutmut_1(path: str, workspace_root: str) -> str:
    return os.path.normpath(None)

x_resolve_path__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_resolve_path__mutmut_1': x_resolve_path__mutmut_1
}
x_resolve_path__mutmut_orig.__name__ = 'x_resolve_path'


def is_path_allowed(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_path_allowed__mutmut_orig, x_is_path_allowed__mutmut_mutants, args, kwargs, None)


def x_is_path_allowed__mutmut_orig(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_is_path_allowed__mutmut_1(path: str, workspace_root: str) -> str:
    resolved = None
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_is_path_allowed__mutmut_2(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(None)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_is_path_allowed__mutmut_3(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = None
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_is_path_allowed__mutmut_4(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(None)
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_is_path_allowed__mutmut_5(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(None):
        return False
    return resolved.startswith(workspace)


def x_is_path_allowed__mutmut_6(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return True
    return resolved.startswith(workspace)


def x_is_path_allowed__mutmut_7(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return False
    return resolved.startswith(None)

x_is_path_allowed__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_is_path_allowed__mutmut_1': x_is_path_allowed__mutmut_1, 
    'x_is_path_allowed__mutmut_2': x_is_path_allowed__mutmut_2, 
    'x_is_path_allowed__mutmut_3': x_is_path_allowed__mutmut_3, 
    'x_is_path_allowed__mutmut_4': x_is_path_allowed__mutmut_4, 
    'x_is_path_allowed__mutmut_5': x_is_path_allowed__mutmut_5, 
    'x_is_path_allowed__mutmut_6': x_is_path_allowed__mutmut_6, 
    'x_is_path_allowed__mutmut_7': x_is_path_allowed__mutmut_7
}
x_is_path_allowed__mutmut_orig.__name__ = 'x_is_path_allowed'


def check_path_traversal(path: str) -> bool:
    args = [path]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_path_traversal__mutmut_orig, x_check_path_traversal__mutmut_mutants, args, kwargs, None)


def x_check_path_traversal__mutmut_orig(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_check_path_traversal__mutmut_1(path: str) -> bool:
    normalized = None
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_check_path_traversal__mutmut_2(path: str) -> bool:
    normalized = os.path.normpath(None)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_check_path_traversal__mutmut_3(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = None
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_check_path_traversal__mutmut_4(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(None)
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_check_path_traversal__mutmut_5(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts and (normalized != path and ".." in normalized.split(os.sep))


def x_check_path_traversal__mutmut_6(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return "XX..XX" in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_check_path_traversal__mutmut_7(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." not in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_check_path_traversal__mutmut_8(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path or ".." in normalized.split(os.sep))


def x_check_path_traversal__mutmut_9(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized == path and ".." in normalized.split(os.sep))


def x_check_path_traversal__mutmut_10(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and "XX..XX" in normalized.split(os.sep))


def x_check_path_traversal__mutmut_11(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." not in normalized.split(os.sep))


def x_check_path_traversal__mutmut_12(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." in normalized.split(None))

x_check_path_traversal__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_check_path_traversal__mutmut_1': x_check_path_traversal__mutmut_1, 
    'x_check_path_traversal__mutmut_2': x_check_path_traversal__mutmut_2, 
    'x_check_path_traversal__mutmut_3': x_check_path_traversal__mutmut_3, 
    'x_check_path_traversal__mutmut_4': x_check_path_traversal__mutmut_4, 
    'x_check_path_traversal__mutmut_5': x_check_path_traversal__mutmut_5, 
    'x_check_path_traversal__mutmut_6': x_check_path_traversal__mutmut_6, 
    'x_check_path_traversal__mutmut_7': x_check_path_traversal__mutmut_7, 
    'x_check_path_traversal__mutmut_8': x_check_path_traversal__mutmut_8, 
    'x_check_path_traversal__mutmut_9': x_check_path_traversal__mutmut_9, 
    'x_check_path_traversal__mutmut_10': x_check_path_traversal__mutmut_10, 
    'x_check_path_traversal__mutmut_11': x_check_path_traversal__mutmut_11, 
    'x_check_path_traversal__mutmut_12': x_check_path_traversal__mutmut_12
}
x_check_path_traversal__mutmut_orig.__name__ = 'x_check_path_traversal'


def is_symlink_escape(path: str, workspace_root: str) -> bool:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_symlink_escape__mutmut_orig, x_is_symlink_escape__mutmut_mutants, args, kwargs, None)


def x_is_symlink_escape__mutmut_orig(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = os.path.realpath(workspace_root)
    return not resolved.startswith(workspace)


def x_is_symlink_escape__mutmut_1(path: str, workspace_root: str) -> bool:
    resolved = None
    workspace = os.path.realpath(workspace_root)
    return not resolved.startswith(workspace)


def x_is_symlink_escape__mutmut_2(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(None)
    workspace = os.path.realpath(workspace_root)
    return not resolved.startswith(workspace)


def x_is_symlink_escape__mutmut_3(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = None
    return not resolved.startswith(workspace)


def x_is_symlink_escape__mutmut_4(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = os.path.realpath(None)
    return not resolved.startswith(workspace)


def x_is_symlink_escape__mutmut_5(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = os.path.realpath(workspace_root)
    return resolved.startswith(workspace)


def x_is_symlink_escape__mutmut_6(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = os.path.realpath(workspace_root)
    return not resolved.startswith(None)

x_is_symlink_escape__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_is_symlink_escape__mutmut_1': x_is_symlink_escape__mutmut_1, 
    'x_is_symlink_escape__mutmut_2': x_is_symlink_escape__mutmut_2, 
    'x_is_symlink_escape__mutmut_3': x_is_symlink_escape__mutmut_3, 
    'x_is_symlink_escape__mutmut_4': x_is_symlink_escape__mutmut_4, 
    'x_is_symlink_escape__mutmut_5': x_is_symlink_escape__mutmut_5, 
    'x_is_symlink_escape__mutmut_6': x_is_symlink_escape__mutmut_6
}
x_is_symlink_escape__mutmut_orig.__name__ = 'x_is_symlink_escape'


def can_flow_to_destructive(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    args = [taint, target_tool]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_can_flow_to_destructive__mutmut_orig, x_can_flow_to_destructive__mutmut_mutants, args, kwargs, None)


def x_can_flow_to_destructive__mutmut_orig(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return True
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return True


def x_can_flow_to_destructive__mutmut_1(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint != TaintFlag.CLEAN:
        return True
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return True


def x_can_flow_to_destructive__mutmut_2(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return False
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return True


def x_can_flow_to_destructive__mutmut_3(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return True
    if target_tool not in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return True


def x_can_flow_to_destructive__mutmut_4(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return True
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return True
    return True


def x_can_flow_to_destructive__mutmut_5(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return True
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return False

x_can_flow_to_destructive__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_can_flow_to_destructive__mutmut_1': x_can_flow_to_destructive__mutmut_1, 
    'x_can_flow_to_destructive__mutmut_2': x_can_flow_to_destructive__mutmut_2, 
    'x_can_flow_to_destructive__mutmut_3': x_can_flow_to_destructive__mutmut_3, 
    'x_can_flow_to_destructive__mutmut_4': x_can_flow_to_destructive__mutmut_4, 
    'x_can_flow_to_destructive__mutmut_5': x_can_flow_to_destructive__mutmut_5
}
x_can_flow_to_destructive__mutmut_orig.__name__ = 'x_can_flow_to_destructive'


def escalate_capabilities(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_escalate_capabilities__mutmut_orig, x_escalate_capabilities__mutmut_mutants, args, kwargs, None)


def x_escalate_capabilities__mutmut_orig(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
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


def x_escalate_capabilities__mutmut_1(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
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


def x_escalate_capabilities__mutmut_2(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_escalate_capabilities__mutmut_3(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_escalate_capabilities__mutmut_4(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_escalate_capabilities__mutmut_5(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_escalate_capabilities__mutmut_6(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_escalate_capabilities__mutmut_7(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_escalate_capabilities__mutmut_8(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_escalate_capabilities__mutmut_9(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_escalate_capabilities__mutmut_10(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_escalate_capabilities__mutmut_11(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_escalate_capabilities__mutmut_12(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_escalate_capabilities__mutmut_13(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_escalate_capabilities__mutmut_14(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_escalate_capabilities__mutmut_15(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
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
    return requested, False

x_escalate_capabilities__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_escalate_capabilities__mutmut_1': x_escalate_capabilities__mutmut_1, 
    'x_escalate_capabilities__mutmut_2': x_escalate_capabilities__mutmut_2, 
    'x_escalate_capabilities__mutmut_3': x_escalate_capabilities__mutmut_3, 
    'x_escalate_capabilities__mutmut_4': x_escalate_capabilities__mutmut_4, 
    'x_escalate_capabilities__mutmut_5': x_escalate_capabilities__mutmut_5, 
    'x_escalate_capabilities__mutmut_6': x_escalate_capabilities__mutmut_6, 
    'x_escalate_capabilities__mutmut_7': x_escalate_capabilities__mutmut_7, 
    'x_escalate_capabilities__mutmut_8': x_escalate_capabilities__mutmut_8, 
    'x_escalate_capabilities__mutmut_9': x_escalate_capabilities__mutmut_9, 
    'x_escalate_capabilities__mutmut_10': x_escalate_capabilities__mutmut_10, 
    'x_escalate_capabilities__mutmut_11': x_escalate_capabilities__mutmut_11, 
    'x_escalate_capabilities__mutmut_12': x_escalate_capabilities__mutmut_12, 
    'x_escalate_capabilities__mutmut_13': x_escalate_capabilities__mutmut_13, 
    'x_escalate_capabilities__mutmut_14': x_escalate_capabilities__mutmut_14, 
    'x_escalate_capabilities__mutmut_15': x_escalate_capabilities__mutmut_15
}
x_escalate_capabilities__mutmut_orig.__name__ = 'x_escalate_capabilities'
