# DESIGN.md Spec Source (Cached)

> Canonical source: [google-labs-code/design.md/docs/spec.md](https://github.com/google-labs-code/design.md/blob/main/docs/spec.md)
> Cached on: 2026-04-27 | Spec version: alpha
> Freshness: run `gh api repos/google-labs-code/design.md --jq '.pushed_at'` and compare with cached date

---

DESIGN.md is a self-contained, plain-text representation of a design system. It defines the visual
identity of a brand and product, thereby ensuring that these stylistic choices can be followed
across design sessions and between different AI agents and tools. As a human-readable, open-format
document, it serves as a living source of truth that both humans and AI can understand and refine.

A DESIGN.md file contains two parts: An optional YAML frontmatter, and a markdown body. The YAML
front matter contains machine-readable design tokens. The markdown body sections provide
human-readable design rationale and guidance. Prose may use descriptive color names (e.g.,
"Midnight Forest Green") that correspond to systematic token names (e.g., `primary`). The tokens
are the normative values; the prose provides context for how to apply them.

# Design Tokens

DESIGN.md may embed design tokens in a structured format. The system is inspired by the
[Design Token JSON spec](https://www.designtokens.org/tr/2025.10/format/#abstract). Specifically,
we adopt the concept of typed token groups (colors, typography, spacing) and the `{path.to.token}`
reference syntax for cross-referencing values.

These tokens are easily converted from or to `tokens.json`, Figma variables, and Tailwind theme
configs.

Design tokens are embedded as YAML front matter at the beginning of the file. The front matter
block must begin with a line containing exactly `---` and end with a line containing exactly
`---`. The YAML content between these delimiters is parsed according to the schema defined below.

Example:

```yaml
---
version: alpha
name: Daylight Prestige
colors:
  primary: "#1A1C1E"
  secondary: "#6C7278"
  tertiary: "#B8422E"
typography:
  h1:
    fontFamily: Public Sans
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.02em
---
```

## Schema

```yaml
version: <string>          # optional, current version: "alpha"
name: <string>
description: <string>      # optional
colors:
  <token-name>: <Color>
typography:
  <token-name>: <Typography>
rounded:
  <scale-level>: <Dimension>
spacing:
  <scale-level>: <Dimension | number>
components:
  <component-name>:
    <token-name>: <string|token reference>
```

The `<scale-level>` placeholder represents a named level in a sizing or spacing scale. Common
level names include `xs`, `sm`, `md`, `lg`, `xl`, and `full`. Any descriptive string key is valid.

**Color**: A color value must start with "#" followed by a hex color code in the SRGB color space.

**Typography**: An object with the following optional properties:

- `fontFamily` (string)
- `fontSize` (Dimension)
- `fontWeight` (number) — A numeric font weight value (e.g., `400`, `700`). In YAML, this may be
  expressed as either a bare number or a quoted string; both are equivalent.
- `lineHeight` (Dimension | number) — Accepts either a Dimension (e.g., `24px`, `1.5rem`) or a
  unitless number (e.g., `1.6`). A unitless number represents a multiplier of the element's
  `fontSize`, which is the recommended CSS practice.
- `letterSpacing` (Dimension)
- `fontFeature` (string) — configures
  [`font-feature-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-feature-settings).
- `fontVariation` (string) — configures
  [`font-variation-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings).

**Dimension**: A dimension value is a string with a unit suffix. Valid units are: px, em, rem.

**Token References**: A token reference must be wrapped in curly braces, and contain an object path
to another value in the YAML tree. For most token groups, the reference must point to a primitive
value (e.g., `colors.primary-60`), not a group (e.g., `colors`). Within the `components` section,
references to composite values (e.g., `{typography.label-md}`) are permitted.

# Sections

Every `DESIGN.md` follows the same structure. Sections can be omitted if they're not relevant to
your project, but those present should appear in the sequence listed below. All sections use
`<h2>` (`##`) headings. An optional `<h1>` heading may appear for document titling purposes but
is not parsed as a section.

### Section Order

1. **Overview** (also: "Brand & Style")
2. **Colors**
3. **Typography**
4. **Layout** (also: "Layout & Spacing")
5. **Elevation & Depth** (also: "Elevation")
6. **Shapes**
7. **Components**
8. **Do's and Don'ts**

## Overview

Also known as "Brand & Style". This section is a holistic description of a product's look and
feel. It defines the brand personality, target audience, and the emotional response the UI should
evoke. It serves as foundational context for guiding the agent's high-level stylistic decisions
when a specific rule or token isn't explicitly defined.

## Colors

This section defines the color palettes for the design system. At least the `primary` color
palette must be defined, and additional color palettes may be defined as needed.

When there are multiple color palettes, the design system may assign a semantic role for each
palette. A common convention is to name the palettes in this order: `primary`, `secondary`,
`tertiary`, and `neutral`.

### Design Tokens

The `colors` section defines all color design tokens. It is a map\<string, Color>, that maps the
name of the color token to its value.

## Typography

This section defines typography levels. Most design systems have 9–15 typography levels. A common
naming convention is to use semantic categories such as `headline`, `display`, `body`, `label`,
`caption`. Each category may further be divided into different sizes, such as `small`, `medium`,
and `large`.

### Design Tokens

The `typography` section defines the precise font properties. It is a map\<string, Typography>.

## Layout

Also known as "Layout & Spacing". This section describes the layout and spacing strategy.

### Design Tokens

The spacing section defines the spacing design tokens. It is a map\<string, Dimension | number>.

## Elevation & Depth

Also known as "Elevation". This section describes how visual hierarchy is conveyed. If elevation
is used, it defines the required styling (spread, blur, color). For flat designs, this section
explains the alternative methods used to convey visual hierarchy (e.g., borders, color contrast).

## Shapes

This section describes how visual elements are shaped.

### Design Tokens

The `rounded` section defines the design tokens for rounded corners. It is a map\<string,
Dimension>.

## Components

This section provides style guidance for component atoms within the design system. Common
component types: Buttons, Chips, Lists, Tooltips, Checkboxes, Radio buttons, Input fields.

> **Note:** The components specification is actively evolving. The current structure provides
> intentional flexibility for domain-specific component definitions while the spec matures.

### Design Tokens

The components section defines a collection of design tokens. It's a map\<string, map\<string,
string>> that maps a component identifier to a group of sub token names and values. Values may be
literal values, or references to previously defined design tokens.

**Variants**: A component may have a variant for different UI states (active, hover, pressed, etc.).
Those variant components are defined under a different but related key, for example,
"button-primary", "button-primary-hover", "button-primary-active".

### Component Property Tokens

Each component has properties that are themselves design tokens:

- backgroundColor: \<Color>
- textColor: \<Color>
- typography: \<Typography>
- rounded: \<Dimension>
- padding: \<Dimension>
- size: \<Dimension>
- height: \<Dimension>
- width: \<Dimension>

## Do's and Don'ts

This section provides practical guidelines and common pitfalls. These act as guardrails when
creating designs.

# Recommended Token Names (Non-Normative)

**Colors:** `primary`, `secondary`, `tertiary`, `neutral`, `surface`, `on-surface`, `error`

**Typography:** `headline-display`, `headline-lg`, `headline-md`, `body-lg`, `body-md`, `body-sm`,
`label-lg`, `label-md`, `label-sm`

**Rounded:** `none`, `sm`, `md`, `lg`, `xl`, `full`

# Consumer Behavior for Unknown Content

| Scenario | Behavior |
|---|---|
| Unknown section heading | Preserve; do not error |
| Unknown color token name | Accept if value is valid |
| Unknown typography token name | Accept as valid typography |
| Unknown spacing value | Accept; store as string if not a valid dimension |
| Unknown component property | Accept with warning |
| Duplicate section heading | Error; reject the file |
