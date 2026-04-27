# Conversion: Design Tokens JSON

Convert DESIGN.md YAML tokens to a `tokens.json` file compatible with [Style Dictionary](https://amzn.github.io/style-dictionary/) and the [Design Token Community Group format](https://www.designtokens.org/).

## Mapping Rules

DESIGN.md YAML tokens map to the DTCG JSON format:

| DESIGN.md | tokens.json |
|-----------|-------------|
| `colors.primary: "#1A1C1E"` | `{ "colors": { "primary": { "$value": "#1A1C1E", "$type": "color" } } }` |
| `typography.h1.fontSize: "48px"` | `{ "typography": { "h1": { "fontSize": { "$value": "48px", "$type": "dimension" } } } }` |
| `spacing.md: "16px"` | `{ "spacing": { "md": { "$value": "16px", "$type": "dimension" } } }` |
| `rounded.lg: "12px"` | `{ "rounded": { "lg": { "$value": "12px", "$type": "dimension" } } }` |

## Conversion Pattern

```python
import yaml
import json

def design_md_to_tokens_json(frontmatter: dict) -> dict:
    output = {}

    # Colors
    if "colors" in frontmatter:
        output["colors"] = {}
        for name, value in frontmatter["colors"].items():
            output["colors"][name] = {"$value": value, "$type": "color"}

    # Typography
    if "typography" in frontmatter:
        output["typography"] = {}
        for name, props in frontmatter["typography"].items():
            token = {}
            for prop, val in props.items():
                if prop == "fontFamily":
                    token["fontFamily"] = {"$value": val, "$type": "fontFamily"}
                elif prop == "fontWeight":
                    token["fontWeight"] = {"$value": val, "$type": "fontWeight"}
                else:
                    token[prop] = {"$value": str(val), "$type": "dimension"}
            output["typography"][name] = token

    # Spacing
    if "spacing" in frontmatter:
        output["spacing"] = {}
        for name, value in frontmatter["spacing"].items():
            output["spacing"][name] = {"$value": str(value), "$type": "dimension"}

    # Rounded
    if "rounded" in frontmatter:
        output["rounded"] = {}
        for name, value in frontmatter["rounded"].items():
            output["rounded"][name] = {"$value": str(value), "$type": "dimension"}

    return output
```

## Token Reference Resolution

DESIGN.md uses `{colors.primary}` references. These must be resolved:

1. Parse all tokens into a flat map
2. For each `{path.to.token}` reference, replace with the resolved value
3. Output the resolved values in tokens.json (not the references)

## Style Dictionary Integration

```json
{
  "source": ["tokens.json"],
  "platforms": {
    "css": {
      "transformGroup": "css",
      "buildPath": "build/css/",
      "files": [{ "destination": "variables.css", "format": "css/variables" }]
    }
  }
}
```
