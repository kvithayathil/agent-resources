# Conversion: Tailwind CSS Config

Convert DESIGN.md YAML tokens to a `tailwind.config.js` file.

## Mapping Rules

| DESIGN.md Token Group | Tailwind Config Key |
|----------------------|-------------------|
| `colors` | `theme.colors` |
| `typography` | `theme.fontSize` + `theme.fontFamily` |
| `spacing` | `theme.spacing` |
| `rounded` | `theme.borderRadius` |

## Conversion Pattern

```javascript
// tailwind.config.js generation from DESIGN.md frontmatter
module.exports = {
  theme: {
    colors: {
      // Direct map from colors tokens
      primary: "#1A1C1E",
      secondary: "#6C7278",
      tertiary: "#B8422E",
      neutral: "#F7F5F2",
    },
    fontFamily: {
      // Extract unique fontFamilies from typography tokens
      sans: ['"Public Sans"', 'system-ui', 'sans-serif'],
      mono: ['"Space Grotesk"', 'monospace'],
    },
    fontSize: {
      // Map typography levels to fontSize arrays: [size, { lineHeight, letterSpacing, fontWeight }]
      "h1": ['3rem', { lineHeight: '1.1', letterSpacing: '-0.02em', fontWeight: '600' }],
      "body-md": ['1rem', { lineHeight: '1.6', fontWeight: '400' }],
      "label-sm": ['0.75rem', { lineHeight: '1', letterSpacing: '0.05em', fontWeight: '600' }],
    },
    spacing: {
      // Direct map from spacing tokens, strip units (Tailwind uses rem)
      xs: '0.25rem',
      sm: '0.5rem',
      md: '1rem',
      lg: '2rem',
      xl: '4rem',
    },
    borderRadius: {
      // Direct map from rounded tokens
      sm: '4px',
      md: '8px',
      lg: '12px',
      xl: '1.5rem',
      full: '9999px',
    },
  },
};
```

## Handling Token References

DESIGN.md component tokens use `{colors.primary}` references. In Tailwind config:

1. Define the referenced tokens in `theme.colors` first
2. Use Tailwind's built-in reference system in component plugins, not raw values

## Component Tokens → Tailwind Plugin

DESIGN.md `components` map to a Tailwind plugin:

```javascript
const designPlugin = require('tailwindcss/plugin');

module.exports = {
  plugins: [
    designPlugin(function ({ addComponents, theme }) {
      addComponents({
        '.btn-primary': {
          backgroundColor: theme('colors.primary'),
          color: theme('colors.neutral'),
          borderRadius: theme('borderRadius.md'),
          padding: '12px',
          fontWeight: theme('fontSize.label-sm.1.fontWeight'),
        },
        '.btn-primary:hover': {
          backgroundColor: theme('colors.secondary'),
        },
      });
    }),
  ],
};
```

## Unit Conversion Notes

| DESIGN.md Unit | Tailwind Convention |
|----------------|-------------------|
| `px` | Keep as `px` or convert to `rem` (÷ 16) |
| `rem` | Use directly |
| `em` | Use in letterSpacing, lineHeight contexts |
