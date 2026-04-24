---
name: android-layouts
description: >
  Android layout best practices for XML/Views and Jetpack Compose. Covers hierarchy
  flattening, ConstraintLayout, merge/include, ViewStub, Compose layout phases,
  interop between View and Compose, adaptive layouts, and profiling tools. Use when
  creating, reviewing, or optimizing Android layouts in XML or Compose. Trigger on:
  layout, XML, ConstraintLayout, LinearLayout, RecyclerView, merge, include, ViewStub,
  compose layout, layout phases, LazyColumn, adaptive layout, WindowSizeClass, foldable,
  Layout Inspector, lint, profiling, hierarchy, double taxation, interop, AndroidView,
  ComposeView.
tags:
  - android
  - layouts
  - compose
  - xml
  - performance
license: Apache-2.0
metadata:
  author: kvithayathil
  version: "1.0.0"
  living: "true"
  self-learning: "true"
  self-updating: "true"
  update-policy: "evolve-on-evidence"
  last-reviewed: "2026-04-24"
---

# Android Layout Best Practices

Layout performance and structure guidance for XML/View systems and Jetpack Compose.

For Compose-specific concerns (stability, recomposition, side effects, animations, modifier
extensions), use the **android-compose-ui** skill. This skill focuses on layout hierarchy,
structure, and performance.

## Reference Index

| File | Topics |
|------|--------|
| [XML_LAYOUTS.md](references/XML_LAYOUTS.md) | ConstraintLayout, merge/include, ViewStub, double taxation, RecyclerView |
| [COMPOSE_LAYOUTS.md](references/COMPOSE_LAYOUTS.md) | Layout phases, custom layouts, SubcomposeLayout |
| [INTEROP.md](references/INTEROP.md) | View-to-Compose migration, AndroidView, ComposeView |
| [PROFILING_TOOLS.md](references/PROFILING_TOOLS.md) | Layout Inspector, Lint, Perfetto, benchmarking |
| [LESSONS_LEARNED.md](references/LESSONS_LEARNED.md) | Self-learning log |
| [CHANGELOG.md](references/CHANGELOG.md) | Update history |

---

## Core Principle

**Flat hierarchies are fast hierarchies.** Every widget in the tree pays init + measure + layout +
draw cost. Each nesting level multiplies that cost across all children. The single most impactful
layout optimization is reducing depth.

---

## XML Layout Rules

### Hierarchy Depth

- Target **max 10 levels** of nesting. Profile anything deeper.
- Replace nested `LinearLayout` (especially weighted) with a single `ConstraintLayout`.
- Use `<merge>` as root tag when the layout will be included in another — eliminates one
  nesting level.
- Use `<include>` to reuse layout fragments; combine with `<merge>` for zero-overhead inclusion.

### Double Taxation

Some layout containers measure children multiple times:

| Container | Double Measure? | Why |
|-----------|-----------------|-----|
| `LinearLayout` with weights | Yes | Weight distribution requires pre-measure |
| `RelativeLayout` | Yes | Constraints may reference each other |
| `GridLayout` with weights | Yes | Same as LinearLayout weights |
| `ConstraintLayout` | No | Single-pass constraint solver |

**Rule:** If a container triggers double measurement, replace it with `ConstraintLayout` or
restructure to avoid the multi-pass trigger.

### ViewStub

Use `ViewStub` for layouts that are rarely or conditionally visible (error states, empty states,
progress indicators). `ViewStub` is a zero-dimension placeholder that inflates the real layout
only when `setVisibility(VISIBLE)` or `inflate()` is called.

```xml
<ViewStub
    android:id="@+id/stub_error"
    android:layout="@layout/error_state"
    android:layout_width="match_parent"
    android:layout_height="wrap_content" />
```

```kotlin
val stub = findViewById<ViewStub>(R.id.stub_error)
stub.inflate()
```

After inflation, the `ViewStub` is replaced by the inflated view. It cannot be re-inflated.

### RecyclerView over ListView

Always use `RecyclerView`. `ListView` creates a new view for every item — no recycling.
`RecyclerView` reuses view holders and provides built-in diffing via `DiffUtil`.

### Compound Drawables

When a `TextView` has an adjacent `ImageView` (icon + text), replace both with a single
`TextView` using compound drawables:

```xml
<TextView
    android:drawableStart="@drawable/ic_search"
    android:drawablePadding="8dp"
    android:text="@string/search" />
```

This eliminates one view from the hierarchy.

---

## Compose Layout Rules

### Layout Phases

Compose rendering has three phases: **Composition → Layout → Drawing**. Each phase can be
skipped independently when inputs haven't changed.

- **Composition** runs when state read during composition changes.
- **Layout** runs when layout inputs (size, padding, constraints) change.
- **Drawing** runs when drawing inputs (color, graphics) change.

**Deferred reads** push state reads to later phases, skipping earlier ones:

```kotlin
// Layout-phase read only — skips composition
Modifier.offset { IntOffset(scrollOffset, 0) }

// Composition-phase read — triggers full recomposition on change
Modifier.offset(scrollOffset.dp, 0.dp)
```

For detailed stability and recomposition guidance, see the **android-compose-ui** skill.

### Custom Layouts

Use the `Layout` composable for custom measurement and positioning:

```kotlin
@Composable
fun FlowRow(
    modifier: Modifier = Modifier,
    content: @Composable () -> Unit
) {
    Layout(content, modifier) { measurables, constraints ->
        val placeables = measurables.map { it.measure(constraints) }
        var x = 0
        var y = 0
        var rowHeight = 0
        placeables.forEach { placeable ->
            if (x + placeable.width > constraints.maxWidth) {
                x = 0
                y += rowHeight
                rowHeight = 0
            }
            placeable.placeRelative(x, y)
            x += placeable.width
            rowHeight = maxOf(rowHeight, placeable.height)
        }
        layout(constraints.maxWidth, y + rowHeight) {}
    }
}
```

Prefer built-in `FlowRow`/`FlowColumn` from `androidx.compose.foundation.layout` when
they match your needs.

### SubcomposeLayout

Use `SubcomposeLayout` when child composables depend on measurement results of siblings
(e.g., `LazyRow` needs to know available width before composing items). Overuse adds overhead
— reach for it only when standard `Layout` cannot express the constraint.

---

## Adaptive Layouts

Use `WindowSizeClass` to adapt layout to screen size:

```kotlin
val windowSizeClass = calculateWindowSizeClass(activity)
when (windowSizeClass.widthSizeClass) {
    WindowWidthSizeClass.Compact -> CompactLayout()
    WindowWidthSizeClass.Medium -> MediumLayout()
    WindowWidthSizeClass.Expanded -> ExpandedLayout()
}
```

For foldables, use `WindowInfoTracker` to detect fold posture and adjust layout accordingly.
Always design for the smallest target first, then expand.

---

## Interop

See [references/INTEROP.md](references/INTEROP.md) for detailed View↔Compose migration
patterns.

Quick reference:

| Direction | API | Use Case |
|-----------|-----|----------|
| Compose in XML | `ComposeView` | Add Compose UI to existing XML screens |
| XML in Compose | `AndroidView` | Embed legacy Views inside Compose |
| XML in Compose | `AndroidViewBinding` | Embed inflated ViewBinding layouts |

---

## Profiling

See [references/PROFILING_TOOLS.md](references/PROFILING_TOOLS.md) for tool details and
citations.

| Tool | Best For |
|------|----------|
| Layout Inspector | Visual hierarchy, recomposition counts |
| Android Lint | Static analysis of layout issues |
| Perfetto | System-level layout trace |
| Macrobenchmark | Measure layout inflation time |

---

## Checklist

- [ ] Hierarchy depth ≤ 10 levels (XML)
- [ ] No weighted LinearLayout (use ConstraintLayout)
- [ ] `<merge>` used for included layouts
- [ ] `ViewStub` for conditional/rare layouts
- [ ] RecyclerView (not ListView) for lists
- [ ] Compound drawables replacing icon+TextView pairs
- [ ] Deferred state reads in Compose layout modifiers
- [ ] Stable keys in LazyColumn/LazyRow items
- [ ] Adaptive layout tested at Compact/Medium/Expanded
- [ ] Layout Inspector verified — no unexpected recompositions or deep nesting
