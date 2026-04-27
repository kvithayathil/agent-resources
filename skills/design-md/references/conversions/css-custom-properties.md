# Conversion: CSS Custom Properties

Convert DESIGN.md YAML tokens to CSS custom properties (`:root` variables).

## Conversion Pattern

```css
:root {
  /* Colors */
  --color-primary: #1A1C1E;
  --color-secondary: #6C7278;
  --color-tertiary: #B8422E;
  --color-neutral: #F7F5F2;
  --color-surface: #FFFFFF;
  --color-on-surface: #1A1C1E;
  --color-error: #B3261E;

  /* Typography */
  --font-family-body: "Inter", system-ui, sans-serif;
  --font-size-h1: 3rem;
  --font-size-body-md: 1rem;
  --font-size-label-sm: 0.75rem;
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --line-height-h1: 1.1;
  --line-height-body-md: 1.6;
  --letter-spacing-h1: -0.02em;
  --letter-spacing-label-sm: 0.05em;

  /* Spacing */
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 2rem;
  --spacing-xl: 4rem;

  /* Rounded */
  --rounded-sm: 4px;
  --rounded-md: 8px;
  --rounded-lg: 12px;
  --rounded-xl: 1.5rem;
  --rounded-full: 9999px;
}
```

## Naming Convention

| DESIGN.md | CSS Variable |
|-----------|-------------|
| `colors.primary` | `--color-primary` |
| `typography.h1.fontFamily` | `--font-family-h1` |
| `typography.h1.fontSize` | `--font-size-h1` |
| `typography.h1.fontWeight` | `--font-weight-h1` |
| `typography.h1.lineHeight` | `--line-height-h1` |
| `typography.h1.letterSpacing` | `--letter-spacing-h1` |
| `spacing.md` | `--spacing-md` |
| `rounded.lg` | `--rounded-lg` |

## Component Tokens as Utility Classes

```css
.btn-primary {
  background-color: var(--color-primary);
  color: var(--color-neutral);
  border-radius: var(--rounded-md);
  padding: 12px;
  font-family: var(--font-family-body);
  font-size: var(--font-size-label-sm);
  font-weight: var(--font-weight-semibold);
  letter-spacing: var(----letter-spacing-label-sm);
}

.btn-primary:hover {
  background-color: var(--color-secondary);
}
```

## Dark Mode Pattern

DESIGN.md doesn't natively define dark mode, but the token structure supports it:

```css
:root {
  --color-primary: #1A1C1E;
  --color-surface: #FFFFFF;
  --color-on-surface: #1A1C1E;
}

@media (prefers-color-scheme: dark) {
  :root {
    --color-primary: #FFFFFF;
    --color-surface: #1A1C1E;
    --color-on-surface: #F5F5F5;
  }
}
```
