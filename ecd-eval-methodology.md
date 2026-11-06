---
title: "ECD skill eval harness — iteration-2 methodology learnings"
tags: ["eval", "skills"]
sources: []
contributors: ["Jm2A"]
created: 2026-11-06
updated: 2026-11-06
---

Eval harness for skills/ecd benchmark (iterations 1-2, 2026-11-06). Durable learnings: (1) Probe specs must not encode canonical readings the eval prompt leaves ambiguous — eval-0 discount threshold basis (>100 on full total vs discountable subtotal) was graded by documented-consistency with the run's own QUESTIONS.md reading, not canonically (iteration-1 grader precedent). (2) git-init-in-outputs with per-phase commits gives tamper-resistant artifact-ordering evidence for TDD-process assertions (grader reads git log/show/numstat, not worklog narrative) — but never apply it to ceremony-sensitive near-miss evals, forcing commits is itself ceremony. (3) Assertion design: floor assertions (strong TDD baseline passes) waste discrimination budget — PTDD-distinctive assertions that carried the delta: driving-vs-verification split with marked verification tests, and prediction ledger with per-prediction verdicts + tally. (4) No-unprompted-capability assertion closes the assumptions-register laundering loophole (baseline shipped a coupon registry documented as assumptions and passed v1; fails v2). (5) Grader subagents may hit permission-denied shell — REA capture_process_scenario is a working fallback for git/pytest/probe execution. (6) aggregate_benchmark.py consumes run-N/grading.json + sibling timing.json; keep flat grading.json copy for viewer; patch benchmark.md metadata placeholders after aggregation. Full detail: openspec/research/ecd-handover.md + skills/ecd-workspace/iteration-2/PROTOCOL.md and benchmark.md.
