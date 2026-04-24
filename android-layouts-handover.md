---
title: "Handover: Android Layouts Skill Authoring"
tags: ["android", "layouts", "compose", "xml", "handover", "session"]
sources: []
contributors: ["Jm2A"]
created: 2026-04-24
updated: 2026-04-24
---


# Handover: Android Layouts Best Practices Skill Authoring

**Date**: 2026-04-24
**Status**: In Progress — research complete, files not yet written
**Agent**: glm-5.1 via opencode

## Summary

Researched Android layout best practices from 9 Android developer documentation pages. Skill written and pushed (commit 6896d65). Covers XML/View layouts, Compose layout phases, View↔Compose interop, adaptive layouts, and profiling tools. MATERIAL_DESIGN.md was replaced with INTEROP.md (no research source for M3; interop is layout-critical). Deduplicated against android-compose-ui skill. All quality gates pass.

## Research Completed

| Source | Size | Key Topics |
|--------|------|------------|
| developer.android.com/.../optimizing-layouts.md.txt | 8.5KB | Flatten hierarchy, ConstraintLayout, lint rules, Layout Inspector |
| developer.android.com/.../performance.md.txt | 4.4KB | Compose perf overview: phases, baseline profiles, stability |
| developer.android.com/.../bestpractices.md.txt | 13.7KB | remember, lazy keys, derivedStateOf, deferred reads, backwards writes |
| developer.android.com/.../phases.md.txt | 2.8KB | Composition/Layout/Drawing phases — skip unnecessary phases |
| developer.android.com/.../stability.md.txt | 7.3KB | Stable vs unstable types, skippable/restartable, collections, @Stable |
| developer.android.com/.../tooling.md.txt | 2KB | Layout Inspector recomposition counts, composition tracing |
| developer.android.com/.../optimizing-view-hierarchies.md.txt | 13.3KB | Double taxation, ConstraintLayout vs LinearLayout, Perfetto, Profile GPU |
| developer.android.com/.../reusing-layouts.md.txt | 5.2KB | <include> and <merge> tags, compound drawables |
| developer.android.com/.../benchmarking-overview.md.txt | 3.7KB | Macrobenchmark vs Microbenchmark, Baseline Profiles |

**Note**: Medium article (https://medium.com/@rajabhandari100/views-layouts-optimizations-14a73621504f) blocked by Cloudflare — content not retrievable.

## Planned Skill Structure

```
skills/android/android-layouts/
├── SKILL.md                       # Main concise skill (~200 lines)
└── references/
    ├── XML_LAYOUTS.md             # ConstraintLayout, merge/include, double taxation, RecyclerView
    ├── COMPOSE_LAYOUTS.md         # Phases, stability, deferred reads, lazy keys, derivedStateOf
    ├── MATERIAL_DESIGN.md         # Material 3 component guidance, theming
    ├── PROFILING_TOOLS.md         # Layout Inspector, Lint, Perfetto, benchmarking (with citations)
    ├── LESSONS_LEARNED.md         # Self-learning log (empty template)
    └── CHANGELOG.md               # Update history
```

## Key Principles Extracted from Research

1. **Flat hierarchies** — each widget needs init+layout+draw; snip nesting = multiplied cost
2. **ConstraintLayout over nested LinearLayout** — especially avoid weighted LinearLayout (double measure)
3. **Double taxation** — RelativeLayout, weighted LinearLayout, GridLayout with weights all cause multiple passes
4. **Compose phases** — composition → layout → drawing; snip skip phases when possible via deferred reads
5. **Stability** — immutable data classes = skippable; snip List/Map/Set = unstable by default
6. **Deferred state reads** — lambda modifiers (e.g., `Modifier.offset { }`) skip composition phase
7. **Lazy keys** — stable keys prevent recomposition when items reorder
8. **derivedStateOf** — limit recomposition from rapidly changing state (scroll position)
9. **No backwards writes** — never write state after reading it in same composable
10. **RecyclerView over ListView** — recycles item layouts, better scrolling perf

## Frontmatter Design

```yaml
name: android-layouts
description: >
  Android layout best practices for XML/Views, Jetpack Compose, and Material Design 3.
  Covers hierarchy flattening, ConstraintLayout, merge/include, Compose phases, stability,
  deferred reads, lazy layout keys, profiling tools, and benchmarking. Use when creating,
  reviewing, or optimizing Android layouts in XML or Compose. Trigger on: layout, XML,
  ConstraintLayout, LinearLayout, RecyclerView, merge, include, ViewStub, compose layout,
  recomposition, stability, LazyColumn, derivedStateOf, deferred reads, Layout Inspector,
  lint, Material 3, Material You, profiling, benchmark.
tags: [android, layouts, compose, xml, material, performance]
license: Apache-2.0
metadata:
  author: kvithayathil
  version: "1.0.0"
  living: "true"
  self-learning: "true"
  self-updating: "true"
  update-policy: "evolve-on-evidence"
  last-reviewed: "2026-04-24"
```

## Conventions to Follow

- Follow vdd skill pattern: self-learning protocol, LESSONS_LEARNED.md, CHANGELOG.md
- Follow android-compose-ui skill conventions: Kotlin examples, no comments
- Main SKILL.md under 250 lines; snip detail goes in references/
- Every profiler/tool reference must cite the official Android docs URL
- Edge cases called out explicitly

## Verification Needed After Creation

- Run `just sync` to register in SKILL_INDEX.yaml
- Run `just check` for quality gates
- Verify SKILL.md < 500 lines
- Verify all reference links resolve

## Gotchas for Continuation

- snip tool filters mkdir — use plain mkdir without snip wrapper
- Medium articles behind Cloudflare — use curl + text extraction as fallback
- Android .md.txt URLs sometimes redirect — check response size > 0
- AgentSkills spec: no `sources` in frontmatter
- The existing android-compose-ui skill already covers some Compose topics — android-layouts should focus on layout-specific perf and not duplicate

## Next Steps

1. Create directory: `mkdir -p skills/android/android-layouts/references`
2. Write SKILL.md — concise main skill
3. Write references/XML_LAYOUTS.md
4. Write references/COMPOSE_LAYOUTS.md
5. Write references/MATERIAL_DESIGN.md
6. Write references/PROFILING_TOOLS.md (with citations)
7. Write references/LESSONS_LEARNED.md (empty template)
8. Write references/CHANGELOG.md (initial entry)
9. Run `just sync`
10. Run `just check`
