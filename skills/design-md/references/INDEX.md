# Resource Index

Trigger-based routing to the right reference file. Load only what the task requires.

## Core References

| Trigger / Task | Resource | Description |
|---|---|---|
| Need the full token schema, types, section rules | [spec-quickref.md](spec-quickref.md) | Derived quick-reference of the DESIGN.md format |
| Check upstream spec for changes | [spec-source.md](spec-source.md) | Cached copy of canonical spec from `google-labs-code/design.md` |
| Creating a DESIGN.md from scratch | [authoring-guide.md](authoring-guide.md) | Step-by-step creation workflow with interview prompts |
| Running lint or diff commands | [cli-guide.md](cli-guide.md) | `@google/design.md` CLI deep usage, flags, troubleshooting |
| WCAG contrast warnings from lint | [wcag-contrast.md](wcag-contrast.md) | Contrast ratio rules, common fixes, AA/AAA thresholds |

## Conversion Guides

| Target Format | Resource | When to Load |
|---|---|---|
| Design Tokens JSON (Style Dictionary) | [conversions/design-tokens-json.md](conversions/design-tokens-json.md) | Output to tokens.json pipeline |
| Tailwind CSS config | [conversions/tailwind.md](conversions/tailwind.md) | Generating tailwind.config.js |
| CSS Custom Properties | [conversions/css-custom-properties.md](conversions/css-custom-properties.md) | Generating `:root` CSS variables |

## Examples

| Need | Resource | When to Load |
|---|---|---|
| Smallest valid DESIGN.md | [examples/minimal.md](examples/minimal.md) | Bootstrapping a new project |
| Complete design system reference | [examples/full-system.md](examples/full-system.md) | Comprehensive example with all token groups |
| Component token patterns | [examples/component-patterns.md](examples/component-patterns.md) | Authoring buttons, inputs, cards, etc. |

## Companion Ecosystem

| Tool | Resource | When to Use |
|---|---|---|
| json-render (UI from specs) | [https://json-render.dev/docs/skills](https://json-render.dev/docs/skills) | Rendering DESIGN.md tokens as interactive UIs. Install per-platform skills: `npx skills add vercel-labs/json-render --skill <react\|svelte\|vue\|solid\|shadcn\|...>` |

json-render converts JSON UI specs into component trees for React, Vue, Svelte, Solid, React Native, PDFs, emails, and images. DESIGN.md tokens can feed into json-render catalogs for end-to-end design-to-UI pipelines.

## Self-Learning Files

| File | Purpose |
|---|---|
| [CHANGELOG.md](CHANGELOG.md) | History of all spec + skill updates |
| [LESSONS_LEARNED.md](LESSONS_LEARNED.md) | Accumulated experience from real usage |
