# XML Layout Deep Reference

Detailed guidance for Android View-system layouts. Based on official Android developer
documentation.

Sources:
- [Optimize layout hierarchy](https://developer.android.com/topic/performance/optimizing-layouts)
- [Optimize View hierarchies](https://developer.android.com/topic/performance/optimizing-view-hierarchies)
- [Reusing layouts](https://developer.android.com/develop/ui/views/layout/reusing-layouts)

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
