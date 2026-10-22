// OpenCode plugin: deny git commits that include openspec/ paths.
// Wired to the shared, platform-agnostic hook script (universal pattern):
//   .agents/hooks/scripts/block-openspec-commit.sh
// The script owns the decision; this plugin only normalizes the tool call
// shape and enforces the script's deny verdict by throwing.
import type { Plugin } from "@opencode-ai/plugin"

export const OpenspecCommitGuard: Plugin = async ({ $ }) => {
  return {
    "tool.execute.before": async (input, output) => {
      // Only shell-like tools carry a command worth inspecting.
      if (input.tool !== "shell" && input.tool !== "bash") return

      // Normalize to the shared script's stdin contract. Args live in
      // output.args for OpenCode; fall back defensively to input.args.
      const args = (output?.args ?? (input as any)?.args ?? {}) as Record<string, unknown>
      if (!("command" in args) || typeof args.command !== "string") return

      const payload = { tool_name: input.tool, tool_input: args }

      const result = (await $`.agents/hooks/scripts/block-openspec-commit.sh`.json(payload)) as {
        hookSpecificOutput?: { permissionDecision?: string; permissionDecisionReason?: string }
      }

      const decision = result?.hookSpecificOutput?.permissionDecision
      if (decision === "deny") {
        throw new Error(
          result.hookSpecificOutput.permissionDecisionReason ??
            "openspec commit guard: commit denied",
        )
      }
    },
  }
}
