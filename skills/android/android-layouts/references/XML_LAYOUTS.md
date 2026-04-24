# XML Layout Deep Reference

Detailed guidance for Android View-system layouts. Based on official Android developer
documentation.

Sources:
- [Optimize layout hierarchy](https://developer.android.com/topic/performance/optimizing-layouts)
- [Optimize View hierarchies](https://developer.android.com/topic/performance/optimizing-view-hierarchies)
- [Reusing layouts](https://developer.android.com/develop/ui/views/layout/reusing-layouts)
- [CoordinatorLayout](https://developer.android.com/develop/ui/views/layout/coordinator-layout)
- [ViewPager2](https://developer.android.com/develop/ui/views/viewpager)
- [WindowInsets (Views)](https://developer.android.com/develop/ui/views/layout/edge-to-edge)

---

## ConstraintLayout

The preferred root-level container for complex layouts. Resolves all constraints in a single
measurement pass — no double taxation.

### Key Patterns

**Chains** for distributing views horizontally or vertically (replacement for LinearLayout weights):

```xml
<androidx.constraintlayout.widget.ConstraintLayout
    android:layout_width="match_parent"
    android:layout_height="wrap_content">

    <Button
        android:id="@+id/btn_cancel"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintEnd_toStartOf="@id/btn_confirm"
        app:layout_constraintHorizontal_chainStyle="spread" />

    <Button
        android:id="@+id/btn_confirm"
        app:layout_constraintStart_toEndOf="@id/btn_cancel"
        app:layout_constraintEnd_toEndOf="parent" />

</androidx.constraintlayout.widget.ConstraintLayout>
```

**Barriers** for aligning to the edge of dynamically-sized siblings:

```xml
<androidx.constraintlayout.widget.Barrier
    android:id="@+id/barrier"
    app:barrierDirection="end"
    app:constraint_referenced_ids="title,subtitle" />

<TextView
    android:id="@+id/value"
    app:layout_constraintStart_toEndOf="@id/barrier" />
```

**Guidelines** for consistent spacing:

```xml
<androidx.constraintlayout.widget.Guideline
    android:id="@+id/guide_start"
    android:orientation="vertical"
    app:layout_constraintGuide_begin="16dp" />
```

### When Not to Use ConstraintLayout

- Simple linear layouts (2-3 views in a row/column) — `LinearLayout` is fine and simpler.
- Deeply nested patterns that could use `<include>` with `LinearLayout` — evaluate if
  restructuring is better than a monolithic ConstraintLayout.

---

## Merge and Include

### `<include>`

Reuses a layout file inside another. Passes layout params from the inclusion site:

```xml
<include
    layout="@layout/user_header"
    android:layout_width="match_parent"
    android:layout_height="wrap_content" />
```

Override layout params at the `<include>` site, not in the included file.

### `<merge>`

Eliminates the root container when a layout is included. The children of `<merge>` are
directly inserted into the parent:

```xml
<!-- user_header.xml -->
<merge xmlns:android="http://schemas.android.com/apk/res/android">
    <ImageView android:id="@+id/avatar" ... />
    <TextView android:id="@+id/name" ... />
</merge>
```

**When to use `<merge>`:**
- The included layout will always be embedded in a parent container.
- The root element would otherwise be a redundant wrapper (e.g., a vertical LinearLayout
  inside another vertical LinearLayout).

**When NOT to use `<merge>`:**
- The layout is used standalone (e.g., as `setContentView`).
- You need to apply layout params to the root of the included layout at the inclusion site.

---

## ViewStub

A lightweight, zero-dimension placeholder that defers layout inflation until needed.

### Usage

```xml
<ViewStub
    android:id="@+id/stub_empty"
    android:inflatedId="@+id/empty_state"
    android:layout="@layout/empty_state"
    android:layout_width="match_parent"
    android:layout_height="match_parent" />
```

```kotlin
val stub = findViewById<ViewStub>(R.id.stub_empty)
val inflatedView = stub.inflate()
```

Alternatively, set visibility:

```kotlin
stub.viewStub!!.visibility = View.VISIBLE
```

### Behavior

- `ViewStub` is removed from the hierarchy after inflation — replaced by the inflated view.
- Cannot be re-inflated. For toggleable visibility, use a regular view with
  `View.GONE`/`View.VISIBLE`.
- `android:inflatedId` sets the ID of the inflated root (different from the stub's own ID).

### Best Candidates

- Empty/error/progress states shown conditionally
- Onboarding overlays
- Feature-gated UI sections
- Heavy layouts (WebViews, maps) that most users never see

---

## Double Taxation

When a layout container measures its children more than once, each child pays measure+layout
cost multiplied by the number of passes.

### Offenders

| Container | Trigger | Passes |
|-----------|---------|--------|
| `LinearLayout` | `layout_weight` on any child | 2 |
| `RelativeLayout` | Cross-referencing constraints | 2 |
| `GridLayout` | `android:layout_width="0dp"` with weights | 2 |

### Detection

Use Layout Inspector or Perfetto to spot double measurement. Look for `measure()` calls
exceeding expectations.

### Fixes

1. Replace weighted `LinearLayout` with `ConstraintLayout` chains.
2. Replace `RelativeLayout` with `ConstraintLayout`.
3. If `LinearLayout` is simple (no weights), it's single-pass — keep it.
4. Use `LinearLayout` with `fixed` heights/widths instead of weights when possible.

---

## RecyclerView

### Why Not ListView

`ListView` creates a new view for every item. `RecyclerView` maintains a view pool and
recycles off-screen holders. For a list of 1000 items, `ListView` creates 1000 views;
`RecyclerView` creates ~15 (screenful + buffer).

### ViewHolder Pattern

```kotlin
class NoteViewHolder(
    private val binding: ItemNoteBinding
) : RecyclerView.ViewHolder(binding.root) {

    fun bind(note: NoteUi) {
        binding.title.text = note.title
        binding.body.text = note.body
    }
}
```

### DiffUtil

Always use `DiffUtil` (or `ListAdapter` which wraps it) to compute minimal updates:

```kotlin
class NoteDiffCallback : DiffUtil.ItemCallback<NoteUi>() {
    override fun areItemsTheSame(oldItem: NoteUi, newItem: NoteUi): Boolean =
        oldItem.id == newItem.id

    override fun areContentsTheSame(oldItem: NoteUi, newItem: NoteUi): Boolean =
        oldItem == newItem
}
```

### Common Mistakes

| Mistake | Fix |
|---------|-----|
| Not using DiffUtil | Use `ListAdapter` with `DiffUtil.ItemCallback` |
| Setting `setHasStableIds(true)` with positional IDs | Use content-based IDs or don't use it |
| Creating listeners in `onBindViewHolder` | Set listener once in ViewHolder init, update reference |
| Using `notifyDataSetChanged()` | Use specific notify methods (`notifyItemChanged`, etc.) |

---

## Compound Drawables

Replace `ImageView` + `TextView` pairs with a single `TextView` using compound drawables:

```xml
<TextView
    android:drawableStart="@drawable/ic_check"
    android:drawablePadding="8dp"
    android:gravity="center_vertical"
    android:text="@string/confirmed" />
```

**Before:** 2 views (ImageView + TextView)
**After:** 1 view

For custom sizing, use `TextView.setCompoundDrawablesRelativeWithIntrinsicBounds()` or
wrap in an `InsetDrawable` via XML.

---

## Lint Rules for Layouts

Android Lint detects common layout issues:

| Rule | ID | Detects |
|------|----|---------|
| Nested weights | `NestedWeights` | Weighted LinearLayout inside weighted LinearLayout |
| Too deep layout | `TooDeepLayout` | Nesting > 10 levels |
| Too many views | `TooManyViews` | Total views > 80 in one layout |
| Useless parent | `UselessParent` | Layout with no siblings that doesn't add layout value |
| Hardcoded text | `HardcodedText` | Text not using string resources |

Run: `./gradlew :app:lint`

---

## CoordinatorLayout

A super-powered FrameLayout that coordinates dependent child views through `CoordinatorLayout.Behavior`.
The primary use case is coordinating scroll-dependent UI (collapsing toolbar, floating action button,
snackbar).

### Collapsing Toolbar Layout

```xml
<androidx.coordinatorlayout.widget.CoordinatorLayout
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <com.google.android.material.appbar.AppBarLayout
        android:layout_width="match_parent"
        android:layout_height="200dp">

        <com.google.android.material.appbar.CollapsingToolbarLayout
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            app:layout_scrollFlags="scroll|exitUntilCollapsed">

            <ImageView
                android:layout_width="match_parent"
                android:layout_height="match_parent"
                android:scaleType="centerCrop"
                app:layout_collapseMode="parallax" />

            <com.google.android.material.appbar.MaterialToolbar
                android:layout_width="match_parent"
                android:layout_height="?attr/actionBarSize"
                app:layout_collapseMode="pin" />

        </com.google.android.material.appbar.CollapsingToolbarLayout>

    </com.google.android.material.appbar.AppBarLayout>

    <androidx.recyclerview.widget.RecyclerView
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        app:layout_behavior="@string/appbar_scrolling_view_behavior" />

</androidx.coordinatorlayout.widget.CoordinatorLayout>
```

### Key Concepts

| Concept | Purpose |
|---------|---------|
| `layout_scrollFlags` | Controls how the AppBar responds to scroll (`scroll`, `exitUntilCollapsed`, `enterAlways`, `snap`) |
| `layout_collapseMode` | How child behaves during collapse (`pin` stays, `parallax` scrolls with ratio) |
| `layout_behavior` | Links a view's behavior to CoordinatorLayout dispatches |
| `AppBarLayout.ScrollingViewBehavior` | Positions the scrolling content below the AppBar |

### Scroll Flags

| Flag | Behavior |
|------|----------|
| `scroll` | Enables the view to scroll off screen |
| `exitUntilCollapsed` | Scrolls until minHeight is reached, then pins |
| `enterAlways` | Reappears immediately on downward scroll |
| `enterAlwaysCollapsed` | Reappears at minHeight first, then expands on further scroll |
| `snap` | Snaps to fully visible or fully hidden based on scroll threshold |

### Custom Behaviors

When you need view coordination beyond built-in behaviors:

```kotlin
class FadeOutBehavior(context: Context, attrs: AttributeSet) :
    CoordinatorLayout.Behavior<View>(context, attrs) {

    override fun onDependentViewChanged(
        parent: CoordinatorLayout,
        child: View,
        dependency: View
    ): Boolean {
        val maxScroll = dependency.height.toFloat()
        val currentScroll = dependency.translationY
        child.alpha = 1f - (currentScroll / maxScroll)
        return true
    }
}
```

Register in XML: `app:layout_behavior="com.example.FadeOutBehavior"`

### Performance Note

CoordinatorLayout dispatches scroll events to all children with behaviors on every scroll
frame. Keep `onDependentViewChanged` implementations lightweight — no allocations, no
layout requests.

https://developer.android.com/develop/ui/views/layout/coordinator-layout

---

## ViewPager2

RecyclerView-based paging container. Replaces the deprecated `ViewPager`.

### Setup

```xml
<androidx.viewpager2.widget.ViewPager2
    android:id="@+id/pager"
    android:layout_width="match_parent"
    android:layout_height="0dp"
    app:layout_constraintBottom_toBottomOf="parent" />
```

```kotlin
val adapter = FragmentStateAdapter(this)
viewPager.adapter = adapter
```

### Key Differences from ViewPager

| Feature | ViewPager | ViewPager2 |
|---------|-----------|------------|
| Adapter | `PagerAdapter` | `RecyclerView.Adapter` or `FragmentStateAdapter` |
| RTL support | Manual | Built-in |
| Vertical paging | No | `orientation="vertical"` |
| Offscreen limit | `setOffscreenPageLimit()` | Same, but default is `OFFSCREEN_PAGE_LIMIT_DEFAULT` (0) |
| Notify changes | `notifyDataSetChanged()` | Same, but backed by DiffUtil via RecyclerView |

### Common Patterns

**With TabLayout:**

```kotlin
TabLayoutMediator(tabLayout, viewPager) { tab, position ->
    tab.text = tabs[position].title
}.attach()
```

**Page transformation:**

```kotlin
viewPager.setPageTransformer { page, position ->
    page.alpha = 1f - abs(position)
}
```

### Migration to Compose

For new code, prefer `HorizontalPager` (Compose). Keep `ViewPager2` when:
- Pages are Fragments with complex lifecycle needs
- Integrating with existing TabLayout + Fragment architecture
- Page content requires View system features (SurfaceView, TextureView)

https://developer.android.com/develop/ui/views/viewpager

---

## WindowInsets in XML

### fitsSystemWindows

The simplest approach for edge-to-edge handling in XML:

```xml
<LinearLayout
    android:fitsSystemWindows="true"
    android:layout_width="match_parent"
    android:layout_height="match_parent">
</LinearLayout>
```

Sets padding to account for system bars. Only works for direct children of the window
decor view or when no parent has already consumed the insets.

### Manual Inset Handling

For precise control:

```kotlin
override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
    super.onViewCreated(view, savedInstanceState)

    ViewCompat.setOnApplyWindowInsetsListener(view) { v, insets ->
        val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
        v.updatePadding(
            top = systemBars.top,
            bottom = systemBars.bottom
        )
        insets
    }
}
```

### Inset Consumption Rules (XML)

- **Insets are consumed once.** If a parent handles `fitsSystemWindows`, children won't
  receive them unless the parent dispatches manually.
- Use `WindowInsetsCompat` for backward compatibility.
- `setOnApplyWindowInsetsListener` overrides `fitsSystemWindows` on the same view.

https://developer.android.com/develop/ui/views/layout/edge-to-edge
