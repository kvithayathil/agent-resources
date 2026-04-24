# Material Design 3 Layout Components

Layout-specific M3 Compose component guidance. Focuses on structural layout components
and their inset/size contracts. For theming, color, and typography, see the Android
Material 3 documentation.

Sources:
- [Material Design 3 in Compose](https://developer.android.com/develop/ui/compose/layouts/material)
- [Material 3 Components](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary)

---

## Scaffold

The primary layout structure for M3 screens. Handles top app bar, content, bottom bar,
floating action button, and snackbar positioning with automatic inset handling.

```kotlin
@Composable
fun AppScreen() {
    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Notes") },
                colors = TopAppBarDefaults.topAppBarColors(
                    scrolledContainerColor = MaterialTheme.colorScheme.surface
                )
            )
        },
        bottomBar = {
            NavigationBar {
                items.forEach { item ->
                    NavigationBarItem(
                        selected = item == selectedItem,
                        onClick = { selectedItem = item },
                        icon = { Icon(item.icon, contentDescription = item.label) },
                        label = { Text(item.label) }
                    )
                }
            }
        },
        floatingActionButton = {
            FloatingActionButton(
                onClick = { onAction(AddNote) }
            ) {
                Icon(Icons.Default.Add, contentDescription = "Add note")
            }
        }
    ) { innerPadding ->
        LazyColumn(
            contentPadding = innerPadding
        ) {
            items(notes) { note ->
                NoteItem(note)
            }
        }
    }
}
```

### Inner Padding

`Scaffold` provides `innerPadding` via the content lambda. This padding accounts for
the top app bar, bottom bar, and system insets. **Always apply `innerPadding` as
`contentPadding` on scrollable content** — not as `Modifier.padding`.

```kotlin
// GOOD: content padding — items scroll into padded area
Scaffold { innerPadding ->
    LazyColumn(contentPadding = innerPadding) { ... }
}

// BAD: modifier padding — content can't scroll behind app bar
Scaffold { innerPadding ->
    LazyColumn(modifier = Modifier.padding(innerPadding)) { ... }
}
```

---

## TopAppBar

Three variants with different scroll behaviors:

| Variant | Use Case |
|---------|----------|
| `TopAppBar` | Non-scrolling, always pinned |
| `MediumTopAppBar` | Collapses to pinned title on scroll |
| `LargeTopAppBar` | Collapses to pinned title with larger initial area |

### Scroll Behavior

```kotlin
val scrollBehavior = TopAppBarDefaults.enterAlwaysScrollBehavior(rememberTopAppBarState())

Scaffold(
    topBar = {
        MediumTopAppBar(
            title = { Text("Notes") },
            scrollBehavior = scrollBehavior
        )
    }
) { innerPadding ->
    LazyColumn(
        contentPadding = innerPadding,
        modifier = Modifier.nestedScroll(scrollBehavior.nestedScrollConnection)
    ) { ... }
}
```

Connect scroll behavior to the scrollable content via `Modifier.nestedScroll`.
Without this connection, the app bar won't respond to content scroll.

---

## NavigationBar / NavigationRail

### NavigationBar (bottom)

For Compact width screens. Fixed height of 80dp. Displays 3-5 destinations.

```kotlin
NavigationBar {
    destinations.forEach { dest ->
        NavigationBarItem(
            selected = dest == current,
            onClick = { navigate(dest) },
            icon = { Icon(dest.icon, contentDescription = dest.label) },
            label = { Text(dest.label) }
        )
    }
}
```

### NavigationRail (side)

For Medium/Expanded width screens. Fixed width of 80dp.

```kotlin
NavigationRail {
    destinations.forEach { dest ->
        NavigationRailItem(
            selected = dest == current,
            onClick = { navigate(dest) },
            icon = { Icon(dest.icon, contentDescription = dest.label) },
            label = { Text(dest.label) }
        )
    }
}
```

### Adaptive Navigation Pattern

```kotlin
val widthSizeClass = calculateWindowSizeClass(activity)

Scaffold(
    bottomBar = {
        if (widthSizeClass.widthSizeClass == WindowWidthSizeClass.Compact) {
            NavigationBar { ... }
        }
    }
) { innerPadding ->
    Row(
        modifier = Modifier
            .fillMaxSize()
            .padding(innerPadding)
    ) {
        if (widthSizeClass.widthSizeClass != WindowWidthSizeClass.Compact) {
            NavigationRail { ... }
        }
        Content()
    }
}
```

Use `NavigationBar` for Compact, `NavigationRail` for Medium+. The Scaffold
`bottomBar` slot should be empty when using `NavigationRail`.

---

## NavigationDrawer

### ModalNavigationDrawer (temporary)

Appears over content on Compact screens:

```kotlin
ModalNavigationDrawer(
    drawerContent = {
        ModalDrawerSheet {
            Text("Drawer title", modifier = Modifier.padding(16.dp))
            Divider()
            NavigationDrawerItem(
                label = { Text("Home") },
                selected = true,
                onClick = { },
                icon = { Icon(Icons.Default.Home, contentDescription = null) }
            )
        }
    }
) {
    ScaffoldContent()
}
```

### PermanentNavigationDrawer (always visible)

For Expanded screens:

```kotlin
PermanentNavigationDrawer(
    drawerContent = {
        PermanentDrawerSheet {
            Text("Drawer title", modifier = Modifier.padding(16.dp))
            NavigationDrawerItem(...)
        }
    }
) {
    ScaffoldContent()
}
```

---

## Snackbar with Scaffold

```kotlin
val snackbarHostState = remember { SnackbarHostState() }

Scaffold(
    snackbarHost = { SnackbarHost(snackbarHostState) }
) { innerPadding ->
    LaunchedEffect(snackbarEvent) {
        snackbarHostState.showSnackbar("Note saved")
    }
    Content(innerPadding)
}
```

Snackbar appears above the bottom bar and below the FAB automatically.

---

## Layout Contracts

| Component | Width | Height | Inset Handling |
|-----------|-------|--------|----------------|
| `TopAppBar` | Fill | 64dp (compact) / Variable (medium/large) | Consumes status bar |
| `NavigationBar` | Fill | 80dp | Consumes navigation bar |
| `NavigationRail` | 80dp | Fill | Consumes system bars on its edge |
| `NavigationBar` in Scaffold | Fill | 80dp + nav bar inset | Automatic |
| `Scaffold` content area | Fill | Fill minus bars | Provides `innerPadding` |

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Not using `innerPadding` from Scaffold | Apply as `contentPadding` on scrollable content |
| Not connecting `nestedScroll` | Add `Modifier.nestedScroll(scrollBehavior.nestedScrollConnection)` |
| Using both NavigationBar and NavigationRail | Switch based on `WindowSizeClass` |
| Applying `innerPadding` as `Modifier.padding` | Use `contentPadding` parameter on lazy layouts |
| Adding `statusBarsPadding()` inside Scaffold content | Scaffold already handles system insets via `innerPadding` |
