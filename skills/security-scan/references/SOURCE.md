# Source Provenance

- **Repo**: https://github.com/dollspace-gay/codescanner
- **Ref**: main
- **Path**: root
- **Installed**: 2026-04-17
- **Last Checked**: 2026-04-17
- **Provider**: manual
- **Lock Entry**: Not in skills-lock.json (skill wraps external tool, not installed via provider)

## Relationship

This skill wraps the codescanner tool as an external dependency. The tool is cloned
on demand into `.agent-workspace/.external/codescanner/`, not into the skills directory.

A separate global skill exists at `~/.config/agent-skills/skills/security/codescanner.md`
that also wraps this tool via the `$LLM_AGENT_PLUGINS_DIR` external dependency system.

## Upstream Changes

This file is auto-maintained. Do not edit manually unless correcting errors.
Run `just sync` or the provenance check to refresh `Last Checked`.
