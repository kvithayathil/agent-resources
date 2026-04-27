# Full System Example: Atmospheric Glass

Complete DESIGN.md demonstrating all token groups and prose sections. Sourced from the `google-labs-code/design.md` examples.

```markdown
---
name: Atmospheric Glass
colors:
  surface: "#0b1326"
  surface-dim: "#0b1326"
  surface-bright: "#31394d"
  surface-container-lowest: "#060e20"
  surface-container-low: "#131b2e"
  surface-container: "#171f33"
  surface-container-high: "#222a3d"
  surface-container-highest: "#2d3449"
  on-surface: "#dae2fd"
  on-surface-variant: "#c4c7c8"
  inverse-surface: "#dae2fd"
  inverse-on-surface: "#283044"
  outline: "#8e9192"
  outline-variant: "#444748"
  surface-tint: "#c6c6c7"
  primary: "#ffffff"
  on-primary: "#2f3131"
  primary-container: "#e2e2e2"
  on-primary-container: "#636565"
  inverse-primary: "#5d5f5f"
  secondary: "#adc9eb"
  on-secondary: "#14324e"
  secondary-container: "#304b68"
  on-secondary-container: "#9fbbdd"
  tertiary: "#ffffff"
  on-tertiary: "#620040"
  tertiary-container: "#ffd8e7"
  on-tertiary-container: "#ab3779"
  error: "#ffb4ab"
  on-error: "#690005"
  error-container: "#93000a"
  on-error-container: "#ffdad6"
  primary-fixed: "#e2e2e2"
  primary-fixed-dim: "#c6c6c7"
  on-primary-fixed: "#1a1c1c"
  on-primary-fixed-variant: "#454747"
  secondary-fixed: "#d0e4ff"
  secondary-fixed-dim: "#adc9eb"
  on-secondary-fixed: "#001d35"
  on-secondary-fixed-variant: "#2d4965"
  tertiary-fixed: "#ffd8e7"
  tertiary-fixed-dim: "#ffafd3"
  on-tertiary-fixed: "#3d0026"
  on-tertiary-fixed-variant: "#85145a"
  background: "#0b1326"
  on-background: "#dae2fd"
  surface-variant: "#2d3449"
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 84px
    fontWeight: "700"
    lineHeight: 90px
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: "600"
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: "500"
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: "400"
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: "400"
    lineHeight: 24px
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: "600"
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 24px
  card-gap: 16px
  section-margin: 40px
  glass-padding: 20px
components:
  glass-card-standard:
    backgroundColor: rgba(255, 255, 255, 0.1)
    textColor: "{colors.primary}"
    rounded: "{rounded.lg}"
    padding: "{spacing.glass-padding}"
  glass-card-elevated:
    backgroundColor: rgba(255, 255, 255, 0.2)
    textColor: "{colors.primary}"
    rounded: "{rounded.xl}"
    padding: "{spacing.glass-padding}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xl}"
    height: 48px
    padding: 0 24px
  button-primary-hover:
    backgroundColor: "{colors.primary-fixed-dim}"
  button-ghost:
    backgroundColor: rgba(255, 255, 255, 0.05)
    textColor: "{colors.primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xl}"
  input-field:
    backgroundColor: rgba(255, 255, 255, 0.1)
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: 20px
    height: 48px
  weather-display-large:
    textColor: "{colors.primary}"
    typography: "{typography.display-lg}"
  metric-label:
    textColor: "{colors.on-surface-variant}"
    typography: "{typography.label-sm}"
  list-item-interactive:
    backgroundColor: transparent
    rounded: "{rounded.md}"
    padding: 12px
  list-item-interactive-hover:
    backgroundColor: rgba(255, 255, 255, 0.1)
---

## Brand & Style

This design system centers on a high-fidelity Glassmorphism aesthetic designed to evoke a
sense of clarity, depth, and modern sophistication. The brand personality is ethereal yet
functional, transforming complex meteorological data into a serene visual experience.

The UI relies on a "vibrant-minimalist" approach: the background provides the energy through
multi-colored abstract gradients (pinks, purples, and blues), while the interface elements act
as frosted crystalline lenses that focus the user's attention.

## Colors

The color strategy prioritizes luminosity and contrast. Because the background is a vibrant,
multi-colored abstract composition, the UI components utilize a monochromatic white palette
with varying alpha channels to maintain legibility.

- **Primary Canvas:** Multi-stop gradient background: Deep Blue (#1E3A8A), Vivid Purple (#7E22CE), Soft Pink (#DB2777).
- **Surface Alpha:** Component backgrounds range from `rgba(255, 255, 255, 0.1)` to `0.2`.
- **Text:** Strictly white (#FFFFFF) or high-tint silver (#E2E8F0).

## Typography

**Inter** for neutral, geometric clarity that balances organic blurred backgrounds.

- Large display sizes for temperature readings as clear focal points.
- Font weight increased by one tier on frosted glass to counteract background blur noise.
- Subtle text-shadows on small labels for legibility against lighter gradient areas.

## Layout & Spacing

Fluid, contextual model. Elements grouped in "Glass Containers" floating within viewport safe areas.

- 8px base grid governs all dimensions.
- Weather metrics housed in CSS grid/flex with 16px gaps.
- Generous outer margins (24px+) ensure vibrant background remains visible.

## Elevation & Depth

Depth through light and refraction, not darkness:

- **Level 1 (Base):** Dynamic background gradient with slight grain texture.
- **Level 2 (Standard Card):** `backdrop-filter: blur(20px)`, `background: rgba(255, 255, 255, 0.1)`.
- **Level 3 (Elevated/Modals):** `backdrop-filter: blur(40px)`, `background: rgba(255, 255, 255, 0.2)`.
- Every glass surface: 1px solid border at `rgba(255, 255, 255, 0.2)`.
- Shadows: extremely soft, spread-out (`0 8px 32px 0 rgba(0, 0, 0, 0.1)`).

## Shapes

Organic and approachable. Cards: `1rem`. Action elements: `rounded-xl` (1.5rem). Icons: line-based with rounded caps.

## Components

- **Glass Containers:** Standard 20px blur, elevated 40px blur. All glass: 1px white border.
- **Buttons:** Solid white primary, ghost with backdrop filters.
- **Inputs:** Subtle hover states with light blurs, preserving crystalline transparency.

## Do's and Don'ts

- Do use `backdrop-filter: blur()` on all glass surfaces
- Don't use solid backgrounds on interactive elements
- Do maintain WCAG AA contrast even with alpha transparency
- Don't apply heavy shadows — use blur and alpha for depth
- Do test against both light and dark areas of the gradient background
```
