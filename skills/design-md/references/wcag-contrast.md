# WCAG Contrast Reference

Quick reference for understanding and fixing contrast issues flagged by `@google/design.md lint`.

## Requirements

| Level | Normal Text (< 18px) | Large Text (≥ 18px or ≥ 14px bold) |
|-------|---------------------|-------------------------------------|
| AA | 4.5:1 | 3:1 |
| AAA | 7:1 | 4.5:1 |

## How to Calculate

Contrast ratio = (L1 + 0.05) / (L2 + 0.05) where L1 is the relative luminance of the lighter color and L2 is the darker.

Practical approach: use the lint tool. It computes ratios automatically.

## Common Fixes

### Text on background too low contrast

```
Warning: textColor (#999999) on backgroundColor (#FFFFFF) has contrast ratio 2.87:1 — fails WCAG AA.
```

**Fix**: Darken the text color until ratio ≥ 4.5:1. `#767676` is the lightest gray that passes AA on white.

### Primary button text hard to read

```
Warning: textColor (#FFFFFF) on backgroundColor (#FFD700) has contrast ratio 1.59:1 — fails WCAG AA.
```

**Fix**: Use dark text on bright backgrounds. `#1A1C1E` on `#FFD700` passes easily.

### Too many low-contrast pairs

**Fix**: Check if the palette has enough tonal range. A common mistake is using colors that are too close in lightness.

## Quick Dark Text on Common Backgrounds

| Background | Lightest passing text (AA) |
|-----------|--------------------------|
| `#FFFFFF` (white) | `#767676` |
| `#F5F5F5` (light gray) | `#6E6E6E` |
| `#000000` (black) | `#7F7F7F` |
| `#1A1C1E` (dark) | `#7A7C7E` |

## Quick Light Text on Common Backgrounds

| Background | Darkest passing text (AA) |
|-----------|--------------------------|
| `#000000` (black) | `#7F7F7F` |
| `#1A1C1E` (dark) | `#858789` |
| `#FFFFFF` (white) | `#767676` (for dark text) |

## Design Token Patterns for Good Contrast

When defining color tokens, create pairs that are guaranteed to pass:

```yaml
colors:
  primary: "#1A1C1E"           # Dark
  on-primary: "#FFFFFF"        # White on dark — always passes
  surface: "#FFFFFF"           # Light background
  on-surface: "#1A1C1E"        # Dark text on light — always passes
  error: "#B3261E"             # Dark red
  on-error: "#FFFFFF"          # White on dark red — passes
```

The `on-*` naming convention makes contrast pairs explicit in the token system.

## Tools

- `npx @google/design.md lint DESIGN.md` — automated contrast checking
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) — manual verification
- Browser DevTools — inspect element → color contrast ratio shown in accessibility panel
