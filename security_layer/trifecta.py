from security_layer.models import (
    AgentCapabilities,
    ContentClassification,
    ToolPermission,
)

TRIFECTA_COMPONENTS = frozenset({ToolPermission.READ, ToolPermission.WEBFETCH, ToolPermission.BASH})

_DESTRUCTIVE_CONTENT_FIELDS = frozenset({"content", "raw_content", "data", "body", "text", "payload"})


def check_trifecta_violation(capabilities: AgentCapabilities) -> bool:
    has_read = ToolPermission.READ in capabilities.allowed_tools
    has_webfetch = ToolPermission.WEBFETCH in capabilities.allowed_tools
    has_bash = ToolPermission.BASH in capabilities.allowed_tools
    return has_read and has_webfetch and has_bash and capabilities.can_network


def create_sub_agent(role: str, capabilities: AgentCapabilities) -> AgentCapabilities:
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


def validate_orchestrator_message(message: dict) -> bool:
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
