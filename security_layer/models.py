from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class ContentClassification(str, Enum):
    TRUSTED = "TRUSTED"
    UNTRUSTED_EXTERNAL = "UNTRUSTED_EXTERNAL"
    SUSPECTED_INJECTION = "SUSPECTED_INJECTION"


class TaintFlag(str, Enum):
    CLEAN = "CLEAN"
    UNTRUSTED = "UNTRUSTED"


class ToolPermission(str, Enum):
    READ = "READ"
    WRITE = "WRITE"
    BASH = "BASH"
    WEBFETCH = "WEBFETCH"
    GLOB = "GLOB"
    GREP = "GREP"


@dataclass(frozen=True)
class PIIEntity:
    entity_type: str
    start: int
    end: int
    text: str
    score: float


@dataclass(frozen=True)
class ValidationResult:
    passed: bool
    gate: str
    reason: str
    details: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class BudgetState:
    tokens_used: int = 0
    tool_calls: int = 0
    consecutive_errors: int = 0
    cost_usd: float = 0.0


@dataclass(frozen=True)
class BudgetLimits:
    max_tokens: int = 500_000
    max_tool_calls_per_turn: int = 20
    max_consecutive_errors: int = 5
    max_cost_usd: float = 10.0
    max_session_hours: float = 4.0


@dataclass(frozen=True)
class AgentCapabilities:
    allowed_tools: frozenset[ToolPermission] = frozenset()
    allowed_paths: frozenset[str] = frozenset()
    workspace_root: str = ""
    can_network: bool = False
    can_write: bool = False


@dataclass(frozen=True)
class HITLRequest:
    action: str
    target: str
    reason: str
    timeout_minutes: int = 30
    auto_deny: bool = True


@dataclass(frozen=True)
class ClassificationResult:
    classification: ContentClassification
    score: float
    patterns_matched: list[str] = field(default_factory=list)


DESTRUCTIVE_ACTIONS: frozenset[str] = frozenset(
    {
        "file_write_outside_workspace",
        "git_push",
        "git_force_push",
        "git_rebase",
        "shell_rm",
        "shell_drop",
        "shell_delete",
        "shell_truncate",
        "api_post",
        "api_put",
        "api_delete",
        "credential_operation",
        "bulk_operation",
    }
)

INJECTION_PATTERNS: frozenset[str] = frozenset(
    {
        "ignore previous",
        "ignore above",
        "system override",
        "new instructions",
        "you are now",
        "role change",
        "disregard",
        "forget everything",
        "act as",
        "pretend you are",
        "jailbreak",
        "DAN mode",
        "developer mode",
    }
)
