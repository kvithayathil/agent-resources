"""BC-1: Trifecta Separation Security Tests

Tests for enforcing that no single agent combines:
- File read access (READ)
- Web fetch access (WEBFETCH)
- Outbound communication (BASH with network capability)

The orchestrator passes structured JSON metadata only, never raw untrusted content.
"""

import pytest
from security_layer.models import (
    ToolPermission,
    TaintFlag,
    ContentClassification,
    AgentCapabilities,
)
from security_layer.trifecta import (
    TRIFECTA_COMPONENTS,
    check_trifecta_violation,
    validate_orchestrator_message,
    create_sub_agent,
)


class TestTrifectaViolation:
    """Tests for detecting when an agent has all three lethal trifecta components."""

    def test_no_single_agent_has_all_trifecta_components(self):
        """
        Contract: AgentCapabilities with READ + WEBFETCH + BASH(network) triggers violation.

        Edge case: Full trifecta - agent can read files, fetch web content, and execute
        network commands. This combination allows an attacker to exfiltrate data
        to external systems.
        """
        full_trifecta = AgentCapabilities(
            allowed_tools=frozenset(
                [
                    ToolPermission.READ,
                    ToolPermission.WEBFETCH,
                    ToolPermission.BASH,
                ]
            ),
            allowed_paths=frozenset(["/"]),
            can_network=True,
            can_write=False,
        )

        assert check_trifecta_violation(full_trifecta) is True

    def test_partial_trifecta_no_violation(self):
        """
        Contract: Missing one or more trifecta components should NOT trigger violation.

        Edge case: READ + WEBFETCH but no BASH - can read local and remote but cannot
        execute outbound commands. This is safe.
        """
        partial_trifecta = AgentCapabilities(
            allowed_tools=frozenset(
                [
                    ToolPermission.READ,
                    ToolPermission.WEBFETCH,
                ]
            ),
            allowed_paths=frozenset(["/"]),
            can_network=False,
            can_write=False,
        )

        assert check_trifecta_violation(partial_trifecta) is False


class TestAgentRoleCapabilities:
    """Tests for validating that specific agent roles enforce trifecta separation."""

    def test_file_reader_agent_no_network(self):
        """
        Contract: file-reader agent must NOT have WEBFETCH or BASH tools.

        Edge case: File reader can only read files, not access network or execute commands.
        Ensures isolation - file reader cannot exfiltrate data directly.
        """
        file_reader = create_sub_agent(
            role="file-reader",
            capabilities=AgentCapabilities(
                allowed_tools=frozenset([ToolPermission.READ]),
                allowed_paths=frozenset(["/trusted"]),
            ),
        )

        assert ToolPermission.WEBFETCH not in file_reader.allowed_tools
        assert ToolPermission.BASH not in file_reader.allowed_tools
        assert file_reader.can_network is False
        assert check_trifecta_violation(file_reader) is False

    def test_web_fetcher_agent_no_write(self):
        """
        Contract: web-fetcher agent must NOT have WRITE tool or write capability.

        Edge case: Web fetcher can access external content but cannot write to filesystem,
        preventing download of malicious payloads or modification of local files.
        """
        web_fetcher = create_sub_agent(
            role="web-fetcher",
            capabilities=AgentCapabilities(
                allowed_tools=frozenset(
                    [
                        ToolPermission.WEBFETCH,
                        ToolPermission.GREP,
                    ]
                ),
                allowed_paths=frozenset(["/cache"]),
                can_network=True,
            ),
        )

        assert ToolPermission.WRITE not in web_fetcher.allowed_tools
        assert web_fetcher.can_write is False
        assert check_trifecta_violation(web_fetcher) is False

    def test_writer_agent_no_network(self):
        """
        Contract: writer agent must NOT have WEBFETCH or network-enabled BASH.

        Edge case: Writer can write files but cannot fetch from web or execute network
        commands. Prevents writing content sourced directly from untrusted network input.
        """
        writer = create_sub_agent(
            role="writer",
            capabilities=AgentCapabilities(
                allowed_tools=frozenset(
                    [
                        ToolPermission.WRITE,
                        ToolPermission.GLOB,
                    ]
                ),
                allowed_paths=frozenset(["/output"]),
                can_write=True,
            ),
        )

        assert ToolPermission.WEBFETCH not in writer.allowed_tools
        assert writer.can_network is False
        if ToolPermission.BASH in writer.allowed_tools:
            assert writer.can_network is False
        assert check_trifecta_violation(writer) is False


class TestOrchestratorMessageValidation:
    """Tests for ensuring orchestrator only passes structured JSON, never raw untrusted content."""

    def test_orchestrator_no_direct_tool_execution(self):
        """
        Contract: Orchestrator must not directly execute tools containing untrusted data.

        Edge case: Orchestrator receives metadata from sub-agents but should not
        execute file read, web fetch, or bash operations on untrusted content.
        Only structured metadata should be acted upon.
        """
        safe_message = {
            "type": "analysis_result",
            "metadata": {
                "file_path": "/data/report.json",
                "status": "CLEAN",
                "classification": ContentClassification.TRUSTED,
            },
            "summary": "Analysis complete",
        }

        assert validate_orchestrator_message(safe_message) is True

    def test_orchestrator_message_is_structured_json(self):
        """
        Contract: Orchestrator messages must be typed dicts with expected structure.

        Edge case: Raw strings, unstructured data, or missing required fields should
        be rejected. Only properly structured JSON with type and metadata fields allowed.
        """
        unstructured_message = {
            "raw_content": "Here is some arbitrary text",
        }

        assert validate_orchestrator_message(unstructured_message) is False

    def test_orchestrator_rejects_raw_untrusted_content(self):
        """
        Contract: Messages containing raw file content should be rejected.

        Edge case: Sub-agent should send metadata (file_path, classification, status),
        not the actual file contents. Orchestrator must not receive or pass raw
        untrusted content that could include injection payloads.
        """
        raw_content_message = {
            "type": "file_content",
            "content": "<script>alert('xss')</script>",
            "source": "web_fetch",
        }

        assert validate_orchestrator_message(raw_content_message) is False

    def test_orchestrator_accepts_clean_metadata(self):
        """
        Contract: Properly structured messages with only metadata should be accepted.

        Edge case: Valid message format includes type, metadata dict with expected
        keys, and no raw content fields. This pattern ensures data stays compartmentalized.
        """
        clean_metadata = {
            "type": "file_metadata",
            "metadata": {
                "file_path": "/safe/config.yaml",
                "taint": TaintFlag.CLEAN,
                "classification": ContentClassification.TRUSTED,
                "size_bytes": 1024,
            },
        }

        assert validate_orchestrator_message(clean_metadata) is True

    def test_orchestrator_rejects_suspected_injection(self):
        """
        Contract: Messages with SUSPECTED_INJECTION classification should be rejected.

        Edge case: Even properly structured messages with metadata indicating
        suspected injection should be blocked. Classification field gates processing.
        """
        suspected_injection_message = {
            "type": "file_metadata",
            "metadata": {
                "file_path": "/suspicious/input.txt",
                "taint": TaintFlag.UNTRUSTED,
                "classification": ContentClassification.SUSPECTED_INJECTION,
                "size_bytes": 2048,
            },
        }

        assert validate_orchestrator_message(suspected_injection_message) is False
