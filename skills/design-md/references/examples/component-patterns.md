# Component Token Patterns

Common component token definitions for DESIGN.md. Use as reference when authoring the `components` section.

## Button Variants

```yaml
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-md}"
    rounded: "{rounded.md}"
    padding: "12px 24px"
    height: "48px"
  button-primary-hover:
    backgroundColor: "{colors.secondary}"
  button-primary-active:
    backgroundColor: "{colors.tertiary}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.label-md}"
    rounded: "{rounded.md}"
    padding: "12px 24px"
    height: "48px"
  button-secondary-hover:
    backgroundColor: "{colors.surface}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.label-md}"
    rounded: "{rounded.md}"
  button-icon:
    backgroundColor: transparent
    textColor: "{colors.on-surface}"
    rounded: "{rounded.full}"
    size: "40px"
```

## Input Fields

```yaml
components:
  input-field:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "12px 16px"
    height: "48px"
  input-field-error:
    textColor: "{colors.error}"
  input-label:
    textColor: "{colors.on-surface-variant}"
    typography: "{typography.label-sm}"
  input-helper:
    textColor: "{colors.on-surface-variant}"
    typography: "{typography.body-sm}"
```

## Cards

```yaml
components:
  card-standard:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.lg}"
    padding: "{spacing.md}"
  card-elevated:
    backgroundColor: "{colors.surface-container-high}"
    rounded: "{rounded.lg}"
    padding: "{spacing.md}"
  card-outlined:
    backgroundColor: transparent
    rounded: "{rounded.lg}"
    padding: "{spacing.md}"
```

## Chips / Tags

```yaml
components:
  chip:
    backgroundColor: "{colors.surface-container}"
    textColor: "{colors.on-surface}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.sm}"
    padding: "4px 12px"
    height: "32px"
  chip-selected:
    backgroundColor: "{colors.secondary-container}"
    textColor: "{colors.on-secondary-container}"
```

## List Items

```yaml
components:
  list-item:
    backgroundColor: transparent
    rounded: "{rounded.md}"
    padding: "12px 16px"
  list-item-hover:
    backgroundColor: "{colors.surface-container}"
  list-item-active:
    backgroundColor: "{colors.surface-container-high}"
```

## Tooltip

```yaml
components:
  tooltip:
    backgroundColor: "{colors.inverse-surface}"
    textColor: "{colors.inverse-on-surface}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
```

## Pattern: State Variants

State variants use a consistent naming convention:

| State | Suffix | Example |
|-------|--------|---------|
| Default | (none) | `button-primary` |
| Hover | `-hover` | `button-primary-hover` |
| Active/Pressed | `-active` | `button-primary-active` |
| Focused | `-focus` | `button-primary-focus` |
| Disabled | `-disabled` | `button-primary-disabled` |
| Error | `-error` | `input-field-error` |
| Selected | `-selected` | `chip-selected` |

## Pattern: Size Variants

Size variants use prefix conventions:

| Size | Prefix | Example |
|------|--------|---------|
| Small | `sm-` | `sm-button-primary` |
| Default | (none) | `button-primary` |
| Large | `lg-` | `lg-button-primary` |
