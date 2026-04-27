# CLI Guide: @google/design.md

Deep reference for the `@google/design.md` CLI tool. Validates DESIGN.md files and detects regressions.

## Installation

```bash
npm install @google/design.md
# Or run directly:
npx @google/design.md lint DESIGN.md
# Or with bun:
bunx @google/design.md lint DESIGN.md
```

## Commands

### `lint`

Validate a DESIGN.md file for structural correctness, token validity, and WCAG contrast.

```bash
npx @google/design.md lint DESIGN.md
npx @google/design.md lint --format json DESIGN.md
cat DESIGN.md | npx @google/design.md lint -
```

#### Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--format` | `json` or `text` | `json` | Output format |
| `-` (stdin) | | | Read from stdin instead of file |

#### JSON Output Structure

```json
{
  "findings": [
    {
      "severity": "error" | "warning" | "info",
      "path": "components.button-primary.backgroundColor",
      "message": "Description of the finding"
    }
  ],
  "summary": {
    "errors": 0,
    "warnings": 1,
    "info": 1
  }
}
```

#### Exit Codes

- `0` — No errors (warnings/info may exist)
- `1` — Errors found

### `diff`

Compare two DESIGN.md files to detect token-level and prose regressions.

```bash
npx @google/design.md diff DESIGN.md DESIGN-v2.md
```

#### JSON Output Structure

```json
{
  "tokens": {
    "colors": {
      "added": ["accent"],
      "removed": [],
      "modified": ["tertiary"]
    },
    "typography": {
      "added": [],
      "removed": [],
      "modified": []
    }
  },
  "regression": false
}
```

## Common Lint Findings

| Finding | Severity | Fix |
|---------|----------|-----|
| Duplicate section heading | error | Remove duplicate, each `##` heading must be unique |
| Invalid color format | error | Use `#RRGGBB` hex format |
| Missing `name` in frontmatter | error | Add `name: <string>` |
| Low contrast ratio | warning | → [wcag-contrast.md](wcag-contrast.md) |
| Unknown component property | warning | Check spelling, verify against valid properties |
| Token reference not found | error | Verify `{path.to.token}` points to existing token |

## CI/CD Integration

```bash
# In CI pipeline:
npx @google/design.md lint --format json DESIGN.md
# Check exit code and summary.errors count
```

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| `npx` not found | Node.js not installed | Install Node.js or use `bunx` |
| YAML parse error | Malformed frontmatter | Check `---` delimiters, YAML syntax |
| No findings but UI looks wrong | Lint checks structure, not aesthetics | Review prose sections for intent |
| Diff shows unexpected changes | Token renaming or reordering | Use `--format json` to inspect exact changes |
