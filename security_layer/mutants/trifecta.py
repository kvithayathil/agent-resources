from security_layer.models import (
    AgentCapabilities,
    ContentClassification,
    TaintFlag,
    ToolPermission,
)

TRIFECTA_COMPONENTS = frozenset({ToolPermission.READ, ToolPermission.WEBFETCH, ToolPermission.BASH})

_DESTRUCTIVE_CONTENT_FIELDS = frozenset({"content", "raw_content", "data", "body", "text", "payload"})
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


def check_trifecta_violation(capabilities: AgentCapabilities) -> bool:
    args = [capabilities]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_trifecta_violation__mutmut_orig, x_check_trifecta_violation__mutmut_mutants, args, kwargs, None)


def x_check_trifecta_violation__mutmut_orig(capabilities: AgentCapabilities) -> bool:
    has_read = ToolPermission.READ in capabilities.allowed_tools
    has_webfetch = ToolPermission.WEBFETCH in capabilities.allowed_tools
    has_bash = ToolPermission.BASH in capabilities.allowed_tools
    return has_read and has_webfetch and has_bash and capabilities.can_network


def x_check_trifecta_violation__mutmut_1(capabilities: AgentCapabilities) -> bool:
    has_read = None
    has_webfetch = ToolPermission.WEBFETCH in capabilities.allowed_tools
    has_bash = ToolPermission.BASH in capabilities.allowed_tools
    return has_read and has_webfetch and has_bash and capabilities.can_network


def x_check_trifecta_violation__mutmut_2(capabilities: AgentCapabilities) -> bool:
    has_read = ToolPermission.READ not in capabilities.allowed_tools
    has_webfetch = ToolPermission.WEBFETCH in capabilities.allowed_tools
    has_bash = ToolPermission.BASH in capabilities.allowed_tools
    return has_read and has_webfetch and has_bash and capabilities.can_network


def x_check_trifecta_violation__mutmut_3(capabilities: AgentCapabilities) -> bool:
    has_read = ToolPermission.READ in capabilities.allowed_tools
    has_webfetch = None
    has_bash = ToolPermission.BASH in capabilities.allowed_tools
    return has_read and has_webfetch and has_bash and capabilities.can_network


def x_check_trifecta_violation__mutmut_4(capabilities: AgentCapabilities) -> bool:
    has_read = ToolPermission.READ in capabilities.allowed_tools
    has_webfetch = ToolPermission.WEBFETCH not in capabilities.allowed_tools
    has_bash = ToolPermission.BASH in capabilities.allowed_tools
    return has_read and has_webfetch and has_bash and capabilities.can_network


def x_check_trifecta_violation__mutmut_5(capabilities: AgentCapabilities) -> bool:
    has_read = ToolPermission.READ in capabilities.allowed_tools
    has_webfetch = ToolPermission.WEBFETCH in capabilities.allowed_tools
    has_bash = None
    return has_read and has_webfetch and has_bash and capabilities.can_network


def x_check_trifecta_violation__mutmut_6(capabilities: AgentCapabilities) -> bool:
    has_read = ToolPermission.READ in capabilities.allowed_tools
    has_webfetch = ToolPermission.WEBFETCH in capabilities.allowed_tools
    has_bash = ToolPermission.BASH not in capabilities.allowed_tools
    return has_read and has_webfetch and has_bash and capabilities.can_network


def x_check_trifecta_violation__mutmut_7(capabilities: AgentCapabilities) -> bool:
    has_read = ToolPermission.READ in capabilities.allowed_tools
    has_webfetch = ToolPermission.WEBFETCH in capabilities.allowed_tools
    has_bash = ToolPermission.BASH in capabilities.allowed_tools
    return has_read and has_webfetch and has_bash or capabilities.can_network


def x_check_trifecta_violation__mutmut_8(capabilities: AgentCapabilities) -> bool:
    has_read = ToolPermission.READ in capabilities.allowed_tools
    has_webfetch = ToolPermission.WEBFETCH in capabilities.allowed_tools
    has_bash = ToolPermission.BASH in capabilities.allowed_tools
    return has_read and has_webfetch or has_bash and capabilities.can_network


def x_check_trifecta_violation__mutmut_9(capabilities: AgentCapabilities) -> bool:
    has_read = ToolPermission.READ in capabilities.allowed_tools
    has_webfetch = ToolPermission.WEBFETCH in capabilities.allowed_tools
    has_bash = ToolPermission.BASH in capabilities.allowed_tools
    return has_read or has_webfetch and has_bash and capabilities.can_network

x_check_trifecta_violation__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_check_trifecta_violation__mutmut_1': x_check_trifecta_violation__mutmut_1, 
    'x_check_trifecta_violation__mutmut_2': x_check_trifecta_violation__mutmut_2, 
    'x_check_trifecta_violation__mutmut_3': x_check_trifecta_violation__mutmut_3, 
    'x_check_trifecta_violation__mutmut_4': x_check_trifecta_violation__mutmut_4, 
    'x_check_trifecta_violation__mutmut_5': x_check_trifecta_violation__mutmut_5, 
    'x_check_trifecta_violation__mutmut_6': x_check_trifecta_violation__mutmut_6, 
    'x_check_trifecta_violation__mutmut_7': x_check_trifecta_violation__mutmut_7, 
    'x_check_trifecta_violation__mutmut_8': x_check_trifecta_violation__mutmut_8, 
    'x_check_trifecta_violation__mutmut_9': x_check_trifecta_violation__mutmut_9
}
x_check_trifecta_violation__mutmut_orig.__name__ = 'x_check_trifecta_violation'


def create_sub_agent(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    args = [role, capabilities]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_create_sub_agent__mutmut_orig, x_create_sub_agent__mutmut_mutants, args, kwargs, None)


def x_create_sub_agent__mutmut_orig(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_1(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role != "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_2(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "XXfile-readerXX":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_3(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "FILE-READER":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_4(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=None,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_5(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=None,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_6(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=None,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_7(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=None,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_8(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=None,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_9(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_10(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_11(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_12(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_13(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_14(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=True,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_15(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=True,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_16(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role != "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_17(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "XXweb-fetcherXX":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_18(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "WEB-FETCHER":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_19(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=None,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_20(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=None,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_21(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=None,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_22(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=None,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_23(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=None,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_24(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_25(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_26(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_27(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_28(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_29(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=True,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_30(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role != "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_31(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "XXwriterXX":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_32(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "WRITER":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_33(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=None,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_34(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=None,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_35(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=None,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_36(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=None,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_37(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=None,
        )
    return capabilities


def x_create_sub_agent__mutmut_38(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_39(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_40(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            can_network=False,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_41(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_write=capabilities.can_write,
        )
    return capabilities


def x_create_sub_agent__mutmut_42(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            )
    return capabilities


def x_create_sub_agent__mutmut_43(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
    if role == "file-reader":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=False,
            can_write=False,
        )
    if role == "web-fetcher":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=capabilities.can_network,
            can_write=False,
        )
    if role == "writer":
        return AgentCapabilities(
            allowed_tools=capabilities.allowed_tools,
            allowed_paths=capabilities.allowed_paths,
            workspace_root=capabilities.workspace_root,
            can_network=True,
            can_write=capabilities.can_write,
        )
    return capabilities

x_create_sub_agent__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_create_sub_agent__mutmut_1': x_create_sub_agent__mutmut_1, 
    'x_create_sub_agent__mutmut_2': x_create_sub_agent__mutmut_2, 
    'x_create_sub_agent__mutmut_3': x_create_sub_agent__mutmut_3, 
    'x_create_sub_agent__mutmut_4': x_create_sub_agent__mutmut_4, 
    'x_create_sub_agent__mutmut_5': x_create_sub_agent__mutmut_5, 
    'x_create_sub_agent__mutmut_6': x_create_sub_agent__mutmut_6, 
    'x_create_sub_agent__mutmut_7': x_create_sub_agent__mutmut_7, 
    'x_create_sub_agent__mutmut_8': x_create_sub_agent__mutmut_8, 
    'x_create_sub_agent__mutmut_9': x_create_sub_agent__mutmut_9, 
    'x_create_sub_agent__mutmut_10': x_create_sub_agent__mutmut_10, 
    'x_create_sub_agent__mutmut_11': x_create_sub_agent__mutmut_11, 
    'x_create_sub_agent__mutmut_12': x_create_sub_agent__mutmut_12, 
    'x_create_sub_agent__mutmut_13': x_create_sub_agent__mutmut_13, 
    'x_create_sub_agent__mutmut_14': x_create_sub_agent__mutmut_14, 
    'x_create_sub_agent__mutmut_15': x_create_sub_agent__mutmut_15, 
    'x_create_sub_agent__mutmut_16': x_create_sub_agent__mutmut_16, 
    'x_create_sub_agent__mutmut_17': x_create_sub_agent__mutmut_17, 
    'x_create_sub_agent__mutmut_18': x_create_sub_agent__mutmut_18, 
    'x_create_sub_agent__mutmut_19': x_create_sub_agent__mutmut_19, 
    'x_create_sub_agent__mutmut_20': x_create_sub_agent__mutmut_20, 
    'x_create_sub_agent__mutmut_21': x_create_sub_agent__mutmut_21, 
    'x_create_sub_agent__mutmut_22': x_create_sub_agent__mutmut_22, 
    'x_create_sub_agent__mutmut_23': x_create_sub_agent__mutmut_23, 
    'x_create_sub_agent__mutmut_24': x_create_sub_agent__mutmut_24, 
    'x_create_sub_agent__mutmut_25': x_create_sub_agent__mutmut_25, 
    'x_create_sub_agent__mutmut_26': x_create_sub_agent__mutmut_26, 
    'x_create_sub_agent__mutmut_27': x_create_sub_agent__mutmut_27, 
    'x_create_sub_agent__mutmut_28': x_create_sub_agent__mutmut_28, 
    'x_create_sub_agent__mutmut_29': x_create_sub_agent__mutmut_29, 
    'x_create_sub_agent__mutmut_30': x_create_sub_agent__mutmut_30, 
    'x_create_sub_agent__mutmut_31': x_create_sub_agent__mutmut_31, 
    'x_create_sub_agent__mutmut_32': x_create_sub_agent__mutmut_32, 
    'x_create_sub_agent__mutmut_33': x_create_sub_agent__mutmut_33, 
    'x_create_sub_agent__mutmut_34': x_create_sub_agent__mutmut_34, 
    'x_create_sub_agent__mutmut_35': x_create_sub_agent__mutmut_35, 
    'x_create_sub_agent__mutmut_36': x_create_sub_agent__mutmut_36, 
    'x_create_sub_agent__mutmut_37': x_create_sub_agent__mutmut_37, 
    'x_create_sub_agent__mutmut_38': x_create_sub_agent__mutmut_38, 
    'x_create_sub_agent__mutmut_39': x_create_sub_agent__mutmut_39, 
    'x_create_sub_agent__mutmut_40': x_create_sub_agent__mutmut_40, 
    'x_create_sub_agent__mutmut_41': x_create_sub_agent__mutmut_41, 
    'x_create_sub_agent__mutmut_42': x_create_sub_agent__mutmut_42, 
    'x_create_sub_agent__mutmut_43': x_create_sub_agent__mutmut_43
}
x_create_sub_agent__mutmut_orig.__name__ = 'x_create_sub_agent'


def validate_orchestrator_message(message: dict) -> bool:
    args = [message]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_validate_orchestrator_message__mutmut_orig, x_validate_orchestrator_message__mutmut_mutants, args, kwargs, None)


def x_validate_orchestrator_message__mutmut_orig(message: dict) -> bool:
    if not isinstance(message, dict):
        return False
    if "type" not in message:
        return False
    for field in _DESTRUCTIVE_CONTENT_FIELDS:
        if field in message:
            return False
    metadata = message.get("metadata")
    if isinstance(metadata, dict):
        classification = metadata.get("classification")
        if classification is ContentClassification.SUSPECTED_INJECTION:
            return False
    return True


def x_validate_orchestrator_message__mutmut_1(message: dict) -> bool:
    if isinstance(message, dict):
        return False
    if "type" not in message:
        return False
    for field in _DESTRUCTIVE_CONTENT_FIELDS:
        if field in message:
            return False
    metadata = message.get("metadata")
    if isinstance(metadata, dict):
        classification = metadata.get("classification")
        if classification is ContentClassification.SUSPECTED_INJECTION:
            return False
    return True


def x_validate_orchestrator_message__mutmut_2(message: dict) -> bool:
    if not isinstance(message, dict):
        return True
    if "type" not in message:
        return False
    for field in _DESTRUCTIVE_CONTENT_FIELDS:
        if field in message:
            return False
    metadata = message.get("metadata")
    if isinstance(metadata, dict):
        classification = metadata.get("classification")
        if classification is ContentClassification.SUSPECTED_INJECTION:
            return False
    return True


def x_validate_orchestrator_message__mutmut_3(message: dict) -> bool:
    if not isinstance(message, dict):
        return False
    if "XXtypeXX" not in message:
        return False
    for field in _DESTRUCTIVE_CONTENT_FIELDS:
        if field in message:
            return False
    metadata = message.get("metadata")
    if isinstance(metadata, dict):
        classification = metadata.get("classification")
        if classification is ContentClassification.SUSPECTED_INJECTION:
            return False
    return True


def x_validate_orchestrator_message__mutmut_4(message: dict) -> bool:
    if not isinstance(message, dict):
        return False
    if "TYPE" not in message:
        return False
    for field in _DESTRUCTIVE_CONTENT_FIELDS:
        if field in message:
            return False
    metadata = message.get("metadata")
    if isinstance(metadata, dict):
        classification = metadata.get("classification")
        if classification is ContentClassification.SUSPECTED_INJECTION:
            return False
    return True


def x_validate_orchestrator_message__mutmut_5(message: dict) -> bool:
    if not isinstance(message, dict):
        return False
    if "type" in message:
        return False
    for field in _DESTRUCTIVE_CONTENT_FIELDS:
        if field in message:
            return False
    metadata = message.get("metadata")
    if isinstance(metadata, dict):
        classification = metadata.get("classification")
        if classification is ContentClassification.SUSPECTED_INJECTION:
            return False
    return True


def x_validate_orchestrator_message__mutmut_6(message: dict) -> bool:
    if not isinstance(message, dict):
        return False
    if "type" not in message:
        return True
    for field in _DESTRUCTIVE_CONTENT_FIELDS:
        if field in message:
            return False
    metadata = message.get("metadata")
    if isinstance(metadata, dict):
        classification = metadata.get("classification")
        if classification is ContentClassification.SUSPECTED_INJECTION:
            return False
    return True


def x_validate_orchestrator_message__mutmut_7(message: dict) -> bool:
    if not isinstance(message, dict):
        return False
    if "type" not in message:
        return False
    for field in _DESTRUCTIVE_CONTENT_FIELDS:
        if field not in message:
            return False
    metadata = message.get("metadata")
    if isinstance(metadata, dict):
        classification = metadata.get("classification")
        if classification is ContentClassification.SUSPECTED_INJECTION:
            return False
    return True


def x_validate_orchestrator_message__mutmut_8(message: dict) -> bool:
    if not isinstance(message, dict):
        return False
    if "type" not in message:
        return False
    for field in _DESTRUCTIVE_CONTENT_FIELDS:
        if field in message:
            return True
    metadata = message.get("metadata")
    if isinstance(metadata, dict):
        classification = metadata.get("classification")
        if classification is ContentClassification.SUSPECTED_INJECTION:
            return False
    return True


def x_validate_orchestrator_message__mutmut_9(message: dict) -> bool:
    if not isinstance(message, dict):
        return False
    if "type" not in message:
        return False
    for field in _DESTRUCTIVE_CONTENT_FIELDS:
        if field in message:
            return False
    metadata = None
    if isinstance(metadata, dict):
        classification = metadata.get("classification")
        if classification is ContentClassification.SUSPECTED_INJECTION:
            return False
    return True


def x_validate_orchestrator_message__mutmut_10(message: dict) -> bool:
    if not isinstance(message, dict):
        return False
    if "type" not in message:
        return False
    for field in _DESTRUCTIVE_CONTENT_FIELDS:
        if field in message:
            return False
    metadata = message.get(None)
    if isinstance(metadata, dict):
        classification = metadata.get("classification")
        if classification is ContentClassification.SUSPECTED_INJECTION:
            return False
    return True


def x_validate_orchestrator_message__mutmut_11(message: dict) -> bool:
    if not isinstance(message, dict):
        return False
    if "type" not in message:
        return False
    for field in _DESTRUCTIVE_CONTENT_FIELDS:
        if field in message:
            return False
    metadata = message.get("XXmetadataXX")
    if isinstance(metadata, dict):
        classification = metadata.get("classification")
        if classification is ContentClassification.SUSPECTED_INJECTION:
            return False
    return True


def x_validate_orchestrator_message__mutmut_12(message: dict) -> bool:
    if not isinstance(message, dict):
        return False
    if "type" not in message:
        return False
    for field in _DESTRUCTIVE_CONTENT_FIELDS:
        if field in message:
            return False
    metadata = message.get("METADATA")
    if isinstance(metadata, dict):
        classification = metadata.get("classification")
        if classification is ContentClassification.SUSPECTED_INJECTION:
            return False
    return True


def x_validate_orchestrator_message__mutmut_13(message: dict) -> bool:
    if not isinstance(message, dict):
        return False
    if "type" not in message:
        return False
    for field in _DESTRUCTIVE_CONTENT_FIELDS:
        if field in message:
            return False
    metadata = message.get("metadata")
    if isinstance(metadata, dict):
        classification = None
        if classification is ContentClassification.SUSPECTED_INJECTION:
            return False
    return True


def x_validate_orchestrator_message__mutmut_14(message: dict) -> bool:
    if not isinstance(message, dict):
        return False
    if "type" not in message:
        return False
    for field in _DESTRUCTIVE_CONTENT_FIELDS:
        if field in message:
            return False
    metadata = message.get("metadata")
    if isinstance(metadata, dict):
        classification = metadata.get(None)
        if classification is ContentClassification.SUSPECTED_INJECTION:
            return False
    return True


def x_validate_orchestrator_message__mutmut_15(message: dict) -> bool:
    if not isinstance(message, dict):
        return False
    if "type" not in message:
        return False
    for field in _DESTRUCTIVE_CONTENT_FIELDS:
        if field in message:
            return False
    metadata = message.get("metadata")
    if isinstance(metadata, dict):
        classification = metadata.get("XXclassificationXX")
        if classification is ContentClassification.SUSPECTED_INJECTION:
            return False
    return True


def x_validate_orchestrator_message__mutmut_16(message: dict) -> bool:
    if not isinstance(message, dict):
        return False
    if "type" not in message:
        return False
    for field in _DESTRUCTIVE_CONTENT_FIELDS:
        if field in message:
            return False
    metadata = message.get("metadata")
    if isinstance(metadata, dict):
        classification = metadata.get("CLASSIFICATION")
        if classification is ContentClassification.SUSPECTED_INJECTION:
            return False
    return True


def x_validate_orchestrator_message__mutmut_17(message: dict) -> bool:
    if not isinstance(message, dict):
        return False
    if "type" not in message:
        return False
    for field in _DESTRUCTIVE_CONTENT_FIELDS:
        if field in message:
            return False
    metadata = message.get("metadata")
    if isinstance(metadata, dict):
        classification = metadata.get("classification")
        if classification is not ContentClassification.SUSPECTED_INJECTION:
            return False
    return True


def x_validate_orchestrator_message__mutmut_18(message: dict) -> bool:
    if not isinstance(message, dict):
        return False
    if "type" not in message:
        return False
    for field in _DESTRUCTIVE_CONTENT_FIELDS:
        if field in message:
            return False
    metadata = message.get("metadata")
    if isinstance(metadata, dict):
        classification = metadata.get("classification")
        if classification is ContentClassification.SUSPECTED_INJECTION:
            return True
    return True


def x_validate_orchestrator_message__mutmut_19(message: dict) -> bool:
    if not isinstance(message, dict):
        return False
    if "type" not in message:
        return False
    for field in _DESTRUCTIVE_CONTENT_FIELDS:
        if field in message:
            return False
    metadata = message.get("metadata")
    if isinstance(metadata, dict):
        classification = metadata.get("classification")
        if classification is ContentClassification.SUSPECTED_INJECTION:
            return False
    return False

x_validate_orchestrator_message__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_validate_orchestrator_message__mutmut_1': x_validate_orchestrator_message__mutmut_1, 
    'x_validate_orchestrator_message__mutmut_2': x_validate_orchestrator_message__mutmut_2, 
    'x_validate_orchestrator_message__mutmut_3': x_validate_orchestrator_message__mutmut_3, 
    'x_validate_orchestrator_message__mutmut_4': x_validate_orchestrator_message__mutmut_4, 
    'x_validate_orchestrator_message__mutmut_5': x_validate_orchestrator_message__mutmut_5, 
    'x_validate_orchestrator_message__mutmut_6': x_validate_orchestrator_message__mutmut_6, 
    'x_validate_orchestrator_message__mutmut_7': x_validate_orchestrator_message__mutmut_7, 
    'x_validate_orchestrator_message__mutmut_8': x_validate_orchestrator_message__mutmut_8, 
    'x_validate_orchestrator_message__mutmut_9': x_validate_orchestrator_message__mutmut_9, 
    'x_validate_orchestrator_message__mutmut_10': x_validate_orchestrator_message__mutmut_10, 
    'x_validate_orchestrator_message__mutmut_11': x_validate_orchestrator_message__mutmut_11, 
    'x_validate_orchestrator_message__mutmut_12': x_validate_orchestrator_message__mutmut_12, 
    'x_validate_orchestrator_message__mutmut_13': x_validate_orchestrator_message__mutmut_13, 
    'x_validate_orchestrator_message__mutmut_14': x_validate_orchestrator_message__mutmut_14, 
    'x_validate_orchestrator_message__mutmut_15': x_validate_orchestrator_message__mutmut_15, 
    'x_validate_orchestrator_message__mutmut_16': x_validate_orchestrator_message__mutmut_16, 
    'x_validate_orchestrator_message__mutmut_17': x_validate_orchestrator_message__mutmut_17, 
    'x_validate_orchestrator_message__mutmut_18': x_validate_orchestrator_message__mutmut_18, 
    'x_validate_orchestrator_message__mutmut_19': x_validate_orchestrator_message__mutmut_19
}
x_validate_orchestrator_message__mutmut_orig.__name__ = 'x_validate_orchestrator_message'
