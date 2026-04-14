# Validation

## AgentSkills Spec Compliance

The `validate` command checks every skill directory against the [AgentSkills spec](https://agentskills.io/specification) plus our extensions.

### What It Checks

**Required fields (spec):**
- `name` — present, non-empty, lowercase, max 64 chars, no leading/trailing/consecutive hyphens, matches directory name
- `description` — present, non-empty, max 1024 chars

**Optional spec fields:**
- `compatibility` — max 500 chars
- `metadata` — must be a mapping with string values
- `allowed-tools` — present and valid

**Extension fields:**
- `triggers` — list of strings, non-empty if present
- `tags` — list of strings, non-empty if present
- `source` — must include `source.repo`, all values must be strings

**Structural checks:**
- `SKILL.md` exists (uppercase preferred, lowercase accepted with warning)
- Valid YAML frontmatter delimited by `---`
- Body is non-empty (should contain instructions)
- File is under 500 lines (spec recommendation)
- No unknown frontmatter fields

### Running

```bash
just validate              # all skills
just validate my-skill     # specific skill(s)
```

## Quality Toolchain

| Tool | Purpose | Config |
|---|---|---|
| ruff | Linting + formatting | `pyproject.toml [tool.ruff]` |
| basedpyright | Strict type checking | `pyproject.toml [tool.basedpyright]` |
| vulture | Dead code detection | `pyproject.toml [tool.vulture]` |
| pylint (duplicate-code) | Python code duplication | `pyproject.toml [tool.pylint]` |
| jscpd | Cross-language copy-paste detection | `.jscpd.json` |
| pip-audit | Dependency vulnerability scan | (defaults) |

### Full Gate

```bash
just check
```

Runs: lint → typecheck → deadcode → dupes → audit → validate

### Individual Checks

```bash
just lint          # ruff linter
just fmt           # ruff format check
just typecheck     # basedpyright
just deadcode      # vulture
just dupes         # pylint + jscpd
just audit         # pip-audit
just validate      # spec compliance
```

Auto-fix variants: `just lint-fix`, `just fmt-fix`

## Adding Skills to the Validation

Drop a new skill directory under `skills/` with a valid `SKILL.md` — the validator discovers it automatically. No registration needed (though `just sync` updates the index for search).
