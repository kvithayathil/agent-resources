# Compose Layout Deep Reference

Layout-specific Compose guidance focused on structure, phases, and custom layouts.

For stability, recomposition, side effects, animations, modifiers, and accessibility,
see the **android-compose-ui** skill.

Sources:
- [Compose performance best practices](https://developer.android.com/develop/ui/compose/performance/bestpractices)
- [Compose phases](https://developer.android.com/develop/ui/compose/mental-model#phases)
- [Compose stability](https://developer.android.com/develop/ui/compose/performance/stability)
- [Compose modifiers](https://developer.android.com/develop/ui/compose/modifiers)
- [Compose lists](https://developer.android.com/develop/ui/compose/lists)
- [Compose system bars / WindowInsets](https://developer.android.com/develop/ui/compose/system-bars)
- [Compose pager](https://developer.android.com/develop/ui/compose/layouts/pager)

---

## Layout Phases in Detail

Every frame follows three phases. Each can be skipped independently:

```
State change
  │
  ├─ Composition (what to show)
  │    └─ Runs when state read during composition changes
  │
  ├─ Layout (where to put it)
  │    └─ Runs when size/position constraints change
  │
  └─ Drawing (how to render it)
       └─ Runs when visual properties (color, alpha, clip) change
```

### Skipping Phases

The key performance insight: **read state as late as possible** to skip earlier phases.

| Where state is read | Phases run on change |
|---------------------|----------------------|
| During composition | Composition + Layout + Drawing |
| In layout lambda | Layout + Drawing |
| In draw lambda | Drawing only |

### Deferred Reads in Layout Modifiers

```kotlin
// GOOD: Layout-phase read — skips composition
Modifier.offset { IntOffset(scrollX.value, 0) }

// BAD: Composition-phase read — triggers full recomposition
Modifier.offset(scrollX.value.dp, 0.dp)
```

### Deferred Reads in graphicsLayer

```kotlin
// GOOD: Drawing-phase read — skips composition and layout
Modifier.graphicsLayer { alpha = fadeState.value }

// BAD: Composition-phase read
Modifier.alpha(fadeState.value)
```

---

## Custom Layouts

### Layout Composable

When built-in containers don't match your needs:

```kotlin
@Composable
fun StaggeredGrid(
    modifier: Modifier = Modifier,
    rows: Int = 3,
    content: @Composable () -> Unit
) {
    Layout(content, modifier) { measurables, constraints ->
        val rowHeights = IntArray(rows)
        val placeables = measurables.mapIndexed { index, measurable ->
            val placeable = measurable.measure(constraints)
            val row = index % rows
            rowHeights[row] += placeable.height
            placeable
        }

        val totalHeight = rowHeights.maxOrNull() ?: 0
        val rowY = IntArray(rows)
        layout(constraints.maxWidth, totalHeight) {
            var currentRow = 0
            var x = 0
            placeables.forEachIndexed { index, placeable ->
                val row = index % rows
                placeable.placeRelative(x, rowY[row])
                rowY[row] += placeable.height
                x = if (row == rows - 1) { currentRow++; 0 } else x
            }
        }
    }
}
```

### Layout Modifiers

Use `Modifier.layout` to modify a single child's measurement/position:

```kotlin
fun Modifier.verticalCenter() = this.layout { measurable, constraints ->
    val placeable = measurable.measure(constraints)
    val y = (constraints.maxHeight - placeable.height) / 2
    layout(placeable.width, constraints.maxHeight) {
        placeable.placeRelative(0, y)
    }
}
```

### Measurement Invariants

- **Measure each child exactly once** per pass. Measuring a child twice is a runtime error.
- **Constraints can only tighten.** Never pass looser constraints to a child than you received.
- **Place every child.** Unplaced children are a runtime warning and waste measurement work.

---

## SubcomposeLayout

Composes children in phases — useful when the composition of later children depends on
the measurement of earlier ones.

```kotlin
@Composable
fun AdaptiveLayout(
    modifier: Modifier = Modifier,
    content: @Composable () -> Unit
) {
    SubcomposeLayout(modifier) { constraints ->
        val maxWidth = constraints.maxWidth

        val layoutType = if (maxWidth < 400.dp.roundToPx()) {
            LayoutType.Compact
        } else {
            LayoutType.Expanded
        }

        val placeables = subcompose(layoutType) {
            content()
        }.map { it.measure(constraints) }

        layout(maxWidth, placeables.maxOfOrNull { it.height } ?: 0) {
            placeables.forEachIndexed { index, placeable ->
                placeable.placeRelative(0, index * placeable.height)
            }
        }
    }
}
```

### When to Use SubcomposeLayout

- Measured layout must decide **which** composables to show (not just where).
- Content width/height determines the composable tree structure.
- Examples: `LazyRow`, tabs with dynamic sizing, responsive grid.

### Cost

SubcomposeLayout runs composition during the layout phase. It adds overhead because
composition happens synchronously during measure. Use only when `Layout` alone cannot
express the requirement.

---

## Lazy Layout Keys

Keys let Compose track item identity across reorderings, additions, and removals:

```kotlin
LazyColumn {
    items(
        items = notes,
        key = { it.id }
    ) { note ->
        NoteItem(note)
    }
}
```

### Key Requirements

- **Stable across operations.** Don't use positional indices as keys.
- **Unique within the list.** Duplicate keys cause undefined behavior.
- **Consistent type.** Don't mix key types in the same list.

### Without keys, reorder operations (drag, sort) cause full recomposition instead
of move operations.

---

## derivedStateOf in Layout Context

Use `derivedStateOf` to prevent rapidly-changing state (scroll position, drag offset) from
triggering excessive recomposition:

```kotlin
val showFab by remember {
    derivedStateOf { lazyListState.firstVisibleItemIndex > 0 }
}
```

This creates a new composition-scoped state that only changes when the derived value
crosses a meaningful threshold, instead of on every scroll pixel change.

See the **android-compose-ui** skill for full derivedStateOf guidance.

---

## Modifier Order

Modifiers are applied **outside-in**. The order changes both visual output and layout
behavior. Think of each modifier wrapping the previous one in a layer.

```kotlin
// Background extends to include padding area
Modifier
    .background(Color.Red)
    .padding(16.dp)

// Background is inset by padding — no color in padding area
Modifier
    .padding(16.dp)
    .background(Color.Red)
```

### Common Ordering Mistakes

| Order | Result | Fix |
|-------|--------|-----|
| `.clickable().padding()` | Click area includes padding | Swap to `.padding().clickable()` for smaller hit target |
| `.background().padding()` | Background fills padding area | Swap if background should not fill padding |
| `.size().padding()` | Padding reduces content area inside the size | Use `.padding().size()` if size should apply to content only |
| `.fillMaxWidth().wrapContentSize()` | Centers within max width | Use `.wrapContentSize().fillMaxWidth()` for different centering behavior |

### Rule of Thumb

Read modifiers outside-in. The first modifier is the outermost wrapper:

```
Modifier              visual layers (outside → inside):
  .padding(16.dp)     1. padding space
  .background(Red)    2. red background
  .clickable()        3. clickable area
  .padding(8.dp)      4. inner padding
  .size(48.dp)        5. 48dp content
```

### Performance Impact

Modifier order does not affect which compose phases run — it affects layout measurement
only. However, unnecessary wrapping modifiers add measure passes. Avoid redundant
`.fillMaxWidth()` on children of containers that already force max width.

---

## WindowInsets in Compose

WindowInsets represent the areas of the window obscured by system UI (status bar, navigation
bar, IME, display cutout).

### Automatic Inset Handling

Compose Material 3 components (`Scaffold`, `TopAppBar`, `NavigationBar`) handle insets
automatically when using `enableEdgeToEdge()` in your Activity.

### Manual Inset Consumption

```kotlin
Box(
    modifier = Modifier
        .fillMaxSize()
        .windowInsetsPadding(WindowInsets.systemBars.only(WindowInsetsSides.Vertical))
) {
    Content()
}
```

### Common Inset Types

| Inset | Source | Use Case |
|-------|--------|----------|
| `WindowInsets.systemBars` | Status bar + navigation bar | Main content padding |
| `WindowInsets.ime` | Keyboard | Chat input, forms |
| `WindowInsets.displayCutout` | Notch/cutout | Fullscreen content |
| `WindowInsets.safeDrawing` | Union of system bars + cutout | General safe area |
| `WindowInsets.waterfall` | Waterfall display edges | Edge-to-edge on curved screens |

### Inset Consumption Rules

- **Consume insets exactly once** per edge. If `Scaffold` consumes top inset via
  `TopAppBar`, don't add `statusBarsPadding()` to scaffold content.
- Use `WindowInsets.waterfall` only on devices with waterfall displays.
- `imePadding()` should be applied to the container closest to the input field —
  not to the root layout.

### Edge-to-Edge

```kotlin
// In Activity.onCreate()
enableEdgeToEdge()
```

After enabling edge-to-edge, all content draws behind system bars. You **must**
handle insets explicitly or via M3 components.

https://developer.android.com/develop/ui/compose/system-bars

---

## Content Padding in Lazy Layouts

### `contentPadding` vs `padding`

```kotlin
// GOOD: contentPadding — items scroll into the padding area
LazyColumn(
    contentPadding = PaddingValues(horizontal = 16.dp, vertical = 8.dp)
) {
    items(notes) { note ->
        NoteItem(note)
    }
}

// BAD: Modifier.padding — clips the scroll area, items can't scroll into padding
LazyColumn(
    modifier = Modifier.padding(16.dp)
) {
    items(notes) { note ->
        NoteItem(note)
    }
}
```

`contentPadding` adds padding **inside** the scroll viewport. Items scroll into and
through the padded area. `Modifier.padding` adds padding **outside** the scroll viewport,
reducing usable scroll space.

### WindowInsets as Content Padding

```kotlin
LazyColumn(
    contentPadding = WindowInsets.systemBars.asPaddingValues()
) {
    items(notes) { note -> NoteItem(note) }
}
```

This lets list items scroll behind the system bars while keeping the initial scroll
position below the status bar.

---

## HorizontalPager

The Compose equivalent of ViewPager2. Pages are composed lazily and recycled.

```kotlin
val pagerState = rememberPagerState { pageCount }

HorizontalPager(
    state = pagerState,
    modifier = Modifier.fillMaxSize()
) { page ->
    PageContent(page)
}
```

### Beyond Viewport Count

Control how many pages are kept composed on either side of the current page:

```kotlin
HorizontalPager(
    state = pagerState,
    beyondViewportPageCount = 3
) { page -> PageContent(page) }
```

Default is `0` (only current page composed). Increase for smoother swiping at the cost
of memory.

### Page Indicators

```kotlin
HorizontalPagerWithIndicator(
    pagerState = pagerState,
    modifier = Modifier.padding(bottom = 8.dp)
)
```

Or with M3 `PagerDefaults` for tab-style indicators.

### Key Difference from ViewPager2

`HorizontalPager` composes lazily by default — no adapter, no fragment management.
Page state survives recomposition via `pagerState`. For fragment-based pages, continue
using `ViewPager2`.

https://developer.android.com/develop/ui/compose/layouts/pager

---

## Layout Performance Rules

1. **Never write state after reading it** in the same composable (backwards writes).
2. **Defer state reads** to the latest possible phase via lambda modifiers.
3. **Use `key` in lazy layouts** to avoid unnecessary recomposition on reorder.
4. **Prefer `Layout` over `SubcomposeLayout`** unless composition must be conditional.
5. **Avoid allocating objects during composition** — lift allocations outside composables
   or use `remember`.
6. **Profile with Layout Inspector** — check recomposition counts and skip counts.
7. **Use `contentPadding`** not `Modifier.padding` on lazy layouts.
8. **Modifier order matters** — read outside-in, verify visual output matches intent.
