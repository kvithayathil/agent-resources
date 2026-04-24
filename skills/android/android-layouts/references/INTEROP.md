# View ↔ Compose Interop

Migration patterns for mixing View-system and Compose layouts.

Sources:
- [Compose in Views](https://developer.android.com/develop/ui/compose/migrate/interoperability-views/compose-in-views)
- [Views in Compose](https://developer.android.com/develop/ui/compose/migrate/interoperability-views/views-in-compose)

---

## Compose in XML (ComposeView)

Embed Compose content inside an XML layout or existing View-based screen:

```xml
<androidx.compose.ui.platform.ComposeView
    android:id="@+id/compose_header"
    android:layout_width="match_parent"
    android:layout_height="wrap_content" />
```

```kotlin
val composeView = findViewById<ComposeView>(R.id.compose_header)
composeView.setViewCompositionStrategy(
    ViewCompositionStrategy.DisposeOnViewTreeLifecycleDestroyed
)
composeView.setContent {
    AppTheme {
        HeaderComposable()
    }
}
```

### ViewCompositionStrategy

| Strategy | Disposes when |
|----------|---------------|
| `DisposeOnViewTreeLifecycleDestroyed` | Lifecycle destroyed (recommended for Activity/Fragment) |
| `DisposeOnDetachedFromWindowOrReleasedFromPool` | View detached (for RecyclerView items) |
| `DisposeOnLifecycleDestroyed` | Specific lifecycle event |

### ComposeView in RecyclerView

Use `DisposeOnDetachedFromWindowOrReleasedFromPool` for items in a RecyclerView pool:

```kotlin
class ComposeViewHolder(view: View) : RecyclerView.ViewHolder(view) {
    val composeView = view as ComposeView

    init {
        composeView.setViewCompositionStrategy(
            ViewCompositionStrategy.DisposeOnDetachedFromWindowOrReleasedFromPool
        )
    }

    fun bind(content: @Composable () -> Unit) {
        composeView.setContent { content() }
    }
}
```

---

## XML in Compose (AndroidView)

Embed a View-system widget inside Compose:

```kotlin
@Composable
fun LegacyMapWidget(location: LatLng) {
    AndroidView(
        factory = { context ->
            MapView(context).apply {
                onCreate(null)
                getMapAsync { googleMap ->
                    googleMap.moveCamera(
                        CameraUpdateFactory.newLatLngZoom(location, 15f)
                    )
                }
            }
        },
        update = { mapView ->
            mapView.getMapAsync { googleMap ->
                googleMap.moveCamera(
                    CameraUpdateFactory.newLatLngZoom(location, 15f)
                )
            }
        }
    )
}
```

### factory vs update

- **`factory`**: Called once to create the View. Runs on the main thread.
- **`update`**: Called on every recomposition. Use to push new state to the View.

### AndroidViewBinding

For inflating a layout via ViewBinding inside Compose:

```kotlin
@Composable
fun LegacyProfileCard(user: User) {
    AndroidViewBinding(
        factory = ItemProfileBinding::inflate
    ) {
        nameText.text = user.name
        emailText.text = user.email
    }
}
```

### Lifecycle-Aware Views

Views that need lifecycle (MapView, VideoView) require explicit lifecycle management:

```kotlin
@Composable
fun MapContainer() {
    val lifecycleOwner = LocalLifecycleOwner.current
    AndroidView(
        factory = { context ->
            MapView(context).also { mapView ->
                lifecycleOwner.lifecycle.addObserver(LifecycleEventObserver { _, event ->
                    when (event) {
                        Lifecycle.Event.ON_RESUME -> mapView.onResume()
                        Lifecycle.Event.ON_PAUSE -> mapView.onPause()
                        Lifecycle.Event.ON_DESTROY -> mapView.onDestroy()
                        else -> Unit
                    }
                })
            }
        }
    )
}
```

---

## Migration Strategy

### Incremental Approach

1. **New screens in Compose** — all new UI uses Compose.
2. **Shared composables in XML screens** — use `ComposeView` for individual components
   (toolbar, cards, bottom sheets).
3. **Wrap existing XML fragments** — replace Fragment-by-Fragment, starting with leaf screens.
4. **Replace RecyclerView with LazyColumn** — last step, since list adapters often hold
   significant logic.

### Common Pitfalls

| Pitfall | Fix |
|---------|-----|
| ComposeView not showing | Check `setViewCompositionStrategy` is set before `setContent` |
| Memory leak in RecyclerView | Use `DisposeOnDetachedFromWindowOrReleasedFromPool` |
| AndroidView not updating | Use `update` block, don't rely on `factory` for state changes |
| Theme mismatch | Wrap Compose content in `AppTheme` inside `setContent` |
| Touch event conflicts | Use `AndroidView`'s `modifier` parameter for Compose-level gestures |

### Performance Considerations

- `AndroidView` factory runs on the main thread — avoid heavy inflation.
- Each `ComposeView` creates its own composition. Sharing compositions across items in
  a RecyclerView requires careful `ViewCompositionStrategy`.
- Interop boundaries are **not free** — minimize state passing across the boundary.
  Keep related UI in one system when possible.
