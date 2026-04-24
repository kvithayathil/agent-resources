# Layout Profiling Tools

Tools for measuring, inspecting, and diagnosing Android layout performance.

All URLs reference official Android developer documentation.

Sources:
- [Optimize layout hierarchy](https://developer.android.com/topic/performance/optimizing-layouts)
- [Compose tooling](https://developer.android.com/develop/ui/compose/tooling)
- [Benchmarking overview](https://developer.android.com/topic/performance/benchmarking/overview)
- [Optimize View hierarchies](https://developer.android.com/topic/performance/optimizing-view-hierarchies)

---

## Layout Inspector (Android Studio)

Visual tool for inspecting the view/compose tree at runtime.

### What It Shows

- **Component Tree**: Full hierarchy with nesting depth
- **Layout Attributes**: Constraints, sizes, margins
- **Recomposition Counts** (Compose): How many times each composable recomposed
- **Render time**: Per-node draw time

### Using for Compose

1. Run app with debuggable build
2. Open Android Studio → Tools → Layout Inspector
3. Select process
4. Enable "Show recomposition counts" in the inspector settings
5. Interact with the screen and watch for unnecessary recompositions

### Key Metrics

| Metric | What to look for |
|--------|-----------------|
| Recomposition count | Should match user actions — not spike on scroll |
| Skip count | Higher is better (means recomposition was skipped) |
| Nesting depth | XML: ≤10, Compose: watch for unexpected nesting |
| Layout time per frame | <16ms for 60fps |

https://developer.android.com/studio/debug/layout-inspector

---

## Android Lint

Static analysis for layout issues. Runs at build time or on demand.

### Layout-Specific Rules

```bash
./gradlew :app:lint
```

| Rule ID | Detects |
|---------|---------|
| `NestedWeights` | Weighted LinearLayout inside another weighted LinearLayout |
| `TooDeepLayout` | Nesting depth > 10 |
| `TooManyViews` | Total view count > 80 |
| `UselessParent` | Layout that adds no value (single child LinearLayout with match_parent) |
| `HardcodedText` | Text not using `@string/` resources |
| `RtlHardcoded` | Left/right instead of start/end |
| `InefficientWeight` | Weight used when fixed dimensions would work |

### Suppressing False Positives

```xml
<LinearLayout
    tools:ignore="UselessParent" >
```

Suppress only when you've verified the layout is intentional.

https://developer.android.com/studio/write/lint

---

## Perfetto

System-level trace for measuring layout performance across the entire rendering pipeline.

### Setup

```kotlin
// In your build.gradle
implementation("androidx.tracing:tracing-ktx:1.2.0")
```

### Capturing a Trace

1. Run app on device/emulator
2. Open Android Studio → View → Tool Windows → Profiler
3. Select CPU → Record
4. Interact with the screen
5. Stop recording
6. Search for `Choreographer#doFrame` to find layout frames

Or via command line:

```bash
adb shell perfetto \
  -c - --txt \
  -o /data/misc/perfetto-traces/trace \
<<EOF
buffers: {
    size_kb: 63488
}
data_sources: {
    config {
        name: "linux.ftrace"
        ftrace_config {
            ftrace_events: "sched/sched_switch"
            ftrace_events: "power/cpu_frequency"
            atrace_categories: "view"
            atrace_categories: "gfx"
        }
    }
}
duration_ms: 10000
EOF
```

### What to Look For

- Frame times exceeding 16ms (60fps) or 11ms (90fps)
- Long `measure` and `layout` passes
- Main thread blocks during layout

https://perfetto.dev/docs/

---

## Macrobenchmark

Measure layout inflation time and frame performance from instrumentation tests.

### Setup

```kotlin
// build.gradle (androidTest)
implementation("androidx.benchmark:benchmark-macro-junit4:1.2.4")
```

### Benchmark Layout Inflation

```kotlin
@RunWith(AndroidJUnit4::class)
class LayoutInflationBenchmark {
    @get:Rule
    val benchmarkRule = MacrobenchmarkRule()

    @Test
    fun measureStartupLayoutInflation() = benchmarkRule.measureRepeated(
        packageName = "com.example.app",
        metrics = listOf(StartupTimingMetric(), FrameTimingMetric()),
        iterations = 10,
        startupMode = StartupMode.COLD
    ) {
        pressHome()
        startActivityAndWait()
    }
}
```

### Key Metrics

| Metric | What it measures |
|--------|-----------------|
| `StartupTimingMetric` | Time to first frame draw |
| `FrameTimingMetric` | Frame duration (p50, p90, p95, p99) |
| `TraceSectionMetric` | Duration of specific trace sections |

https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview

---

## Microbenchmark

For measuring specific layout operations (measure pass, draw pass) in isolation:

```kotlin
@RunWith(AndroidJUnit4::class)
class LayoutOperationBenchmark {
    @get:Rule
    val benchmarkRule = BenchmarkRule()

    @Test
    fun measureConstraintLayoutInflation() = benchmarkRule.measureRepeatedOnMainThread {
        val inflater = LayoutInflater.from(context)
        inflater.inflate(R.layout.complex_constraint_layout, null)
    }
}
```

https://developer.android.com/topic/performance/benchmarking/microbenchmark-overview

---

## Baseline Profiles

Pre-compile layout inflation paths to avoid JIT overhead on first run:

```kotlin
class BaselineProfileGenerator {
    @get:Rule
    val baselineProfileRule = BaselineProfileRule()

    @Test
    fun generateBaselineProfile() = baselineProfileRule.collect(
        packageName = "com.example.app"
    ) {
        startActivityAndWait()
        // Navigate through screens with complex layouts
    }
}
```

Include Baseline Profiles in your release builds to reduce layout inflation time by
20-30% on first launch.

https://developer.android.com/topic/performance/baselineprofiles/overview

---

## Quick Diagnostic Flow

```
Layout feels slow?
  │
  ├─ Open Layout Inspector → check nesting depth & recomposition counts
  │    ├─ Deep nesting (>10)? → Flatten with ConstraintLayout / <merge>
  │    ├─ High recomposition? → Defer state reads, check stability
  │    └─ Looks OK → Continue
  │
  ├─ Run Lint → check TooDeepLayout, NestedWeights, TooManyViews
  │
  ├─ Capture Perfetto trace → find long measure/layout passes
  │
  └─ Write Macrobenchmark → measure frame timing (p90 < 16ms?)
```
