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
- **Context**: Block-4 behavioral trials (M5 pause/resume, M6 override) of the TDD
  workflow: in both, the agent crossed a pending `AWAITING` gate mid-session —
  GREEN implementation+run before the scripted re-approval (M5), and implementation
  written before the RED test existed (M6). Both were self-caught, reverted with
  `git checkout --`, re-run in the correct order, and disclosed; the recorded state
  machines ended clean. The gap was orchestration-layer drift, caught only by the
  agent's own after-the-fact honesty machinery, not by the rule text itself.
- **Lesson**: A passive prohibition ("approval must be cleared before the next
  phase", PHASES.md §6.2) did not force a check at the moment of writing code.
  Convert it into an active pre-work gate check: before writing any test or
  implementation, re-read the state summary and verify the prior gate's approval
  is recorded in this session; momentum or existing code never substitutes.
- **Validations**: 1
- **Evidence**: M5 breach at
  `openspec/changes/add-aaid-skill/evidence/trials/trial-4.1-M5.md` line 109; M6
  breach at `evidence/trials/trial-4.1-M6.md` line 91 (block-4 grading:
  `evidence/reviews/grading-4.md`, § "M5/M6 adjudication"). Both files
  privacy-redacted disposable-workspace transcripts; no production credentials.
  *(In progress at entry time; 1.0.1 amendment is the applied lesson.)*
