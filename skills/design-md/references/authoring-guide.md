# Authoring Guide: Creating DESIGN.md

Step-by-step workflow for creating a DESIGN.md from scratch.

## Workflow

```
INTERVIEW → TOKENS → PROSE → LINT → ITERATE
```

## Step 1: Interview

Before writing tokens, understand the brand. Ask the user:

1. **Brand personality** — What 3 adjectives describe the look/feel? (e.g., "calm, premium, trustworthy")
2. **Target audience** — Who uses this product?
3. **Emotional response** — How should users feel? (e.g., "confident", "playful")
4. **Color preferences** — Existing brand colors? Any colors to avoid?
5. **Typography feel** — Formal or casual? Dense or spacious? Monospace elements?
6. **Shape language** — Rounded/soft or sharp/angular?
7. **Depth strategy** — Flat, elevated, or glassmorphic?
8. **Reference sites** — Any designs they admire?

## Step 2: Define Tokens

### Colors (required: at least `primary`)

```yaml
colors:
  primary: "#1A1C1E"      # Main brand color
  secondary: "#6C7278"     # Supporting elements
  tertiary: "#B8422E"      # Accent/CTA
  neutral: "#F7F5F2"       # Background/foundation
  surface: "#FFFFFF"        # Card/container backgrounds
  on-surface: "#1A1C1E"    # Text on surfaces
  error: "#B3261E"          # Error states
```

Naming convention: `primary`, `secondary`, `tertiary`, `neutral`, then semantic names (`surface`, `on-surface`, `error`).

### Typography (9–15 levels recommended)

```yaml
typography:
  headline-display:
    fontFamily: Inter
    fontSize: 84px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.05em
```

### Spacing

```yaml
spacing:
  base: 8px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
```

### Rounded

```yaml
rounded:
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
  full: 9999px
```

### Components

Use `{path.to.token}` references to stay DRY:

```yaml
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.md}"
    padding: "12px"
  button-primary-hover:
    backgroundColor: "{colors.secondary}"
```

## Step 3: Write Prose

Follow the required section order with `##` headings. Each section should be 2–5 sentences explaining the "why."

```markdown
## Overview

[Brand personality, target audience, emotional response]

## Colors

[Palette rationale, what each color communicates]

## Typography

[Font strategy, hierarchy, readability choices]

## Layout

[Grid system, spacing rhythm, responsive approach]

## Elevation & Depth

[How depth is achieved — shadows, tonal layers, borders]

## Shapes

[Border radius strategy, organic vs geometric]

## Components

[Per-component styling guidance and interaction patterns]

## Do's and Don'ts

- Do use primary color for the single most important action per screen
- Don't mix rounded and sharp corners in the same view
- Do maintain WCAG AA contrast ratios (4.5:1 for normal text)
- Don't use more than two font weights on a single screen
```

## Step 4: Validate

```bash
npx @google/design.md lint DESIGN.md
```

Fix any errors. Review warnings. Re-run until clean.

## Minimal Template

When a full design system isn't needed, start with the minimum:

```yaml
---
name: My Project
colors:
  primary: "#000000"
  neutral: "#FFFFFF"
typography:
  body-md:
    fontFamily: system-ui
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
---

## Overview

Brief brand description.
```

→ See [examples/minimal.md](examples/minimal.md) and [examples/full-system.md](examples/full-system.md)
