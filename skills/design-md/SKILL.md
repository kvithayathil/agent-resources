---
name: design-md
description: >
  Create, consume, and validate DESIGN.md files — the open format for describing visual identity
  to coding agents. DESIGN.md combines YAML design tokens (colors, typography, spacing, components)
  with Markdown design rationale. Triggers on: DESIGN.md, design system, design tokens, visual identity,
  brand tokens, UI styling, theme generation, color palette, typography tokens, WCAG contrast,
  design-token lint, style regression, component tokens, spacing scale, rounded corners.
tags:
  - design
  - design-system
  - design-tokens
  - ui
  - styling
  - agent-dx
license: Apache-2.0
metadata:
  author: kvithayathil
  version: "1.0.0"
  living: "true"
  self-learning: "true"
  self-updating: "true"
  update-policy: "periodic-remote-check+evolve-on-evidence"
  last-reviewed: "2026-04-27"
  spec-version: "alpha"
source:
  repo: https://github.com/google-labs-code/design.md
  ref: main
  path: docs/spec.md
  fetched_at: "2026-04-27T00:00:00Z"
---

# DESIGN.md Skill

DESIGN.md is a plain-text design system spec: **YAML front matter** (machine-readable tokens) +
**Markdown body** (human-readable rationale). Tokens are normative values. Prose explains intent.

## Mode Selection

Pick one mode based on task. Each mode has its own workflow below.

| Mode | Trigger Phrases | Start Here |
|------|----------------|------------|
| **consume** | "build UI", "style this", "apply design", "use the design system" | Consume Mode below |
| **create** | "create design system", "make a DESIGN.md", "design tokens for my project" | → [references/authoring-guide.md](references/authoring-guide.md) |
| **validate** | "lint", "check contrast", "validate design", "diff design" | CLI Tooling below |
| **convert** | "tailwind config", "css variables", "tokens.json", "style dictionary" | → [references/INDEX.md](references/INDEX.md) → conversions/ |

## Consume Mode

Default mode. Use whenever a DESIGN.md exists in the project root or a specified path.

1. **Parse** YAML front matter — extract all token groups (`colors`, `typography`, `rounded`, `spacing`, `components`)
2. **Resolve** `{path.to.token}` references before applying values
3. **Read** prose sections for design intent — prose answers "why" when tokens alone are ambiguous
4. **Apply** tokens to implementation using the project's CSS approach

Application rules by token group:

| Token Group | How to Apply |
|-------------|-------------|
| `colors` | Map to background, text, border values. Use descriptive names (primary, secondary) as semantic roles |
| `typography` | Bundle fontFamily + fontSize + fontWeight + lineHeight + letterSpacing as a unit |
| `components` | Assemble from sub-properties (`backgroundColor`, `textColor`, `rounded`, `padding`). Variant naming convention: `button-primary`, `button-primary-hover`, `button-primary-active` |
| `rounded` / `spacing` | Apply as sizing values using the scale levels (`sm`, `md`, `lg`, etc.) |

When tokens don't cover a specific need, defer to prose sections for intent, then make a decision consistent with the design personality.

## Create Mode

→ Full workflow in [references/authoring-guide.md](references/authoring-guide.md)

Quick start:
1. Collect brand personality, target audience, emotional response (Overview section)
2. Define color palettes → derive `colors` tokens
3. Choose typography levels → define `typography` tokens
4. Set spacing scale, rounding, elevation strategy
5. Define component tokens using `{path.to.token}` references
6. Write prose sections in required order
7. Run `lint` to validate

## Validate Mode

### CLI Tooling

All commands via `npx @google/design.md` or `bunx @google/design.md`.

```bash
npx @google/design.md lint DESIGN.md             # Structure + WCAG contrast validation
npx @google/design.md lint --format json          # Machine-readable JSON output
npx @google/design.md diff DESIGN.md v2.md        # Detect token + prose regressions
```

**When to run:**

| Situation | Command |
|-----------|---------|
| After authoring a new DESIGN.md | `lint` |
| Before committing design changes | `diff` against previous version |
| Contrast warnings from lint | → [references/wcag-contrast.md](references/wcag-contrast.md) |
| CI/CD integration | `lint --format json` and check `summary.errors` |

→ Full CLI reference: [references/cli-guide.md](references/cli-guide.md)

## Quick Reference

Token types:

| Type | Format | Example |
|------|--------|---------|
| Color | `#` + hex (sRGB) | `"#1A1C1E"` |
| Dimension | number + unit (`px`, `em`, `rem`) | `48px`, `1.5rem` |
| Token Reference | `{path.to.token}` | `{colors.primary}` |
| Typography | object with font properties | `fontFamily`, `fontSize`, `fontWeight`, `lineHeight`, `letterSpacing` |

Prose section order (use `##` headings, can omit but must be in sequence):
1. Overview — brand personality, emotional response
2. Colors — palette rationale
3. Typography — font strategy
4. Layout — grid/spacing model
5. Elevation & Depth — shadow/depth approach
6. Shapes — border radius strategy
7. Components — per-component styling guidance
8. Do's and Don'ts — guardrails

Component token properties: `backgroundColor`, `textColor`, `typography`, `rounded`, `padding`, `size`, `height`, `width`.

→ Full schema: [references/spec-quickref.md](references/spec-quickref.md)

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Omitting prose sections | Prose gives intent — agent needs "why" not just "what" |
| Hardcoding colors instead of token references | Use `{colors.primary}` in components, not `"#1A1C1E"` |
| Wrong section order | Must follow: Overview → Colors → Typography → Layout → Elevation → Shapes → Components → Do's/Don'ts |
| Duplicate section headings | Rejected by spec — each heading must be unique |
| Missing `name` in frontmatter | Required field — design system must have a name |
| Ignoring WCAG contrast | Run `lint` — AA requires 4.5:1 for normal text, 3:1 for large |
| Mixing units inconsistently | Pick `px` or `rem` per token group, stay consistent |

## Self-Learning / Self-Updating Protocol

> This skill tracks the DESIGN.md spec at `google-labs-code/design.md` (currently alpha).
> Agent may modify `references/` files when new evidence or spec changes warrant it.

### Spec Freshness

If `last-reviewed` > 7 days, run freshness check:

```bash
gh api repos/google-labs-code/design.md --jq '.pushed_at'
gh api 'repos/google-labs-code/design.md/commits?path=docs/spec.md' --jq '.[0].sha'
```

If changed → update [references/spec-source.md](references/spec-source.md), diff against previous,
update [references/spec-quickref.md](references/spec-quickref.md) if schema changed,
log in [references/CHANGELOG.md](references/CHANGELOG.md), bump `last-reviewed`.

### Usage Self-Learning

| Trigger | Action |
|---------|--------|
| Lint finding not in Common Mistakes | Add to table above |
| New component pattern discovered | Add to [references/examples/component-patterns.md](references/examples/component-patterns.md) |
| Conversion produces unexpected output | Append to [references/LESSONS_LEARNED.md](references/LESSONS_LEARNED.md) |
| Lesson validated 3+ times | Promote into SKILL.md, prune from LESSONS_LEARNED |
| Instruction unnecessary after repeated use | Prune it — lean skill > exhaustive skill |

### Constraints

- Only update spec-source from canonical `google-labs-code/design.md` repo
- Log all changes in [references/CHANGELOG.md](references/CHANGELOG.md)
- Keep SKILL.md under 500 lines; move detail to references/
- Never remove this Self-Learning/Self-Updating Protocol section

## Companion Ecosystem

**json-render** — render DESIGN.md tokens as interactive UIs across frameworks (React, Vue, Svelte, Solid, React Native, PDF, email, image).
Skill docs: [https://json-render.dev/docs/skills](https://json-render.dev/docs/skills)
Install: `npx skills add vercel-labs/json-render --skill <platform>`

## Resources

→ [references/INDEX.md](references/INDEX.md) — complete resource catalog with trigger → file routing
