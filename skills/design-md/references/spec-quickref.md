# DESIGN.md Spec Quick Reference

Derived from [spec-source.md](spec-source.md). Use this for fast token syntax and section lookups.

## YAML Front Matter Schema

```yaml
version: <string>          # optional, current: "alpha"
name: <string>              # required
description: <string>       # optional
colors:
  <token-name>: <Color>     # "#RRGGBB" hex format
typography:
  <token-name>: <Typography>
rounded:
  <scale-level>: <Dimension>
spacing:
  <scale-level>: <Dimension | number>
components:
  <component-name>:
    <property>: <string | token reference>
```

## Token Types

| Type | Format | Valid Values | Example |
|------|--------|-------------|---------|
| Color | hex string | `#` + 6-char hex (sRGB) | `"#1A1C1E"` |
| Dimension | string with unit | `px`, `em`, `rem` | `"48px"`, `"-0.02em"` |
| Token Ref | curly brace path | `{group.token-name}` | `"{colors.primary}"` |
| Number | bare number | Used for lineHeight, fontWeight | `1.6`, `600` |

## Typography Object Properties

| Property | Type | Required | Notes |
|----------|------|----------|-------|
| `fontFamily` | string | no | Font stack name |
| `fontSize` | Dimension | no | e.g., `"16px"` |
| `fontWeight` | number | no | 100–900, YAML bare or quoted |
| `lineHeight` | Dimension or number | no | Unitless = fontSize multiplier (recommended) |
| `letterSpacing` | Dimension | no | e.g., `"-0.02em"` |
| `fontFeature` | string | no | CSS `font-feature-settings` value |
| `fontVariation` | string | no | CSS `font-variation-settings` value |

## Component Properties

Valid property names: `backgroundColor`, `textColor`, `typography`, `rounded`, `padding`, `size`, `height`, `width`.

Variant naming: `button-primary`, `button-primary-hover`, `button-primary-active`.

Token references in components can point to primitives OR composites (e.g., `{typography.label-md}`).

## Prose Section Order

Use `##` headings. Omittable but must be sequential:

| # | Section | Aliases | Purpose |
|---|---------|---------|---------|
| 1 | Overview | Brand & Style | Brand personality, emotional response |
| 2 | Colors | | Palette rationale |
| 3 | Typography | | Font strategy |
| 4 | Layout | Layout & Spacing | Grid/spacing model |
| 5 | Elevation & Depth | Elevation | Shadow/depth approach |
| 6 | Shapes | | Border radius strategy |
| 7 | Components | | Per-component styling |
| 8 | Do's and Don'ts | | Guardrails |

## Recommended Token Names

Colors: `primary`, `secondary`, `tertiary`, `neutral`, `surface`, `on-surface`, `error`

Typography: `headline-display`, `headline-lg`, `headline-md`, `body-lg`, `body-md`, `body-sm`, `label-lg`, `label-md`, `label-sm`

Rounded: `none`, `sm`, `md`, `lg`, `xl`, `full`

Spacing: `xs`, `sm`, `md`, `lg`, `xl`, `base`, `gutter`, `margin`

## Error Handling

| Scenario | Behavior |
|----------|----------|
| Unknown section heading | Preserve silently |
| Unknown color token | Accept if value is valid hex |
| Unknown typography token | Accept as valid |
| Unknown component property | Accept with warning |
| Duplicate section heading | **Error — reject the file** |
