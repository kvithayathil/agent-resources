# AAID Lessons Learned

> Self-learning log per [SELF-IMPROVEMENT.md](SELF-IMPROVEMENT.md). Add entries only
> when real task or run evidence shows a gap, a new pattern, or a gotcha. Check this
> file before proposing lesson updates. Promote entries to SKILL.md or a reference
> after 3+ validations across different demonstrated tasks.

## Format

```
### [YYYY-MM-DD] Brief Title
- **Context**: What task/situation triggered this
- **Lesson**: What was learned
- **Validations**: N (starts at 1; count only different demonstrated tasks)
- **Evidence**: links to real task/run evidence (privacy-redacted per SELF-IMPROVEMENT.md §2)
```

---

 *(Entries below follow the format above.)*

### [2026-10-24] Passive gate prohibition failed to prevent mid-session crossing
- **Context**: Behavioral trials of the
  TDD workflow (pause/resume and override scenarios): in both, the agent crossed
  a pending `AWAITING` gate mid-session — GREEN implementation+run before the
  scripted re-approval in one scenario, and implementation
  written before the RED test existed in the other. Both were self-caught, reverted with
  `git checkout --`, re-run in the correct order, and disclosed; the recorded state
  machines ended clean. The gap was orchestration-layer drift, caught only by the
  agent's own after-the-fact honesty machinery, not by the rule text itself.
- **Lesson**: A passive prohibition ("approval must be cleared before the next
  phase", PHASES.md §6 item 2) did not force a check at the moment of writing code.
  Convert it into an active pre-work gate check: before writing any test or
  implementation, re-read the state summary and verify the prior gate's approval
  is recorded in this session; momentum or existing code never substitutes.
- **Validations**: 1
- **Evidence**: Both gate-crossings are retained as
  behavioral-trial transcripts in the local, untracked change-evidence tree.
  Privacy-redacted disposable-workspace transcripts; no production credentials.
  *(In progress at entry time; 1.0.1 amendment is the applied lesson.)*

### [2026-10-24] Fallback baselines can launder fetched state as integrated
- **Context**: Closure-gate adversarial review of the shipped
  `check-upstream.sh`: when references/SOURCE.md or its check-status block went
  missing after an authorized refresh, the checker silently fell back to the
  manifest `resolved_commit` — which a fetch has already advanced to the
  fetched tip — so tip-vs-itself reported UNCHANGED for content no human ever
  reviewed.
- **Lesson**: Verdict baselines must come from human-integrated records (the
  SOURCE check-status integrated pin), never from fetched state. Anything the
  fetch machinery advances is by definition unreviewed; a missing provenance
  record must fail closed with a remediation path, not degrade to a fallback.
- **Validations**: 1
- **Evidence**: Closure-gate 6.3 adversarial review (finding 1) and the
  fail-closed contract change + regression tests it drove (checker ERROR on
  missing provenance after a fetched-but-unreviewed refresh).

