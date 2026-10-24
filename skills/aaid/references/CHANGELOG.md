# AAID Changelog

> Record of all substantive updates to this skill. Every entry: trigger and change.

## Format

```
### [version] - YYYY-MM-DD
**Trigger**: What task/situation prompted the update
**Changes**: What was added, removed, or modified
```

---

### 1.0.1 - 2026-10-24
**Trigger**: Behavioral trials showed agents crossing a pending review gate before
approval (self-caught, reverted, and disclosed in the retained trial evidence): the
agent twice crossed a pending `AWAITING` gate mid-session before scripted
approval (GREEN implementation+run before segment-2 re-approval in one trial;
implementation written before the RED test existed in the other). Both self-caught, reverted,
disclosed; the passive §6.2 prohibition failed to prevent the drift in the moment.
**Changes**: PHASES.md §6 — added the pre-work gate check (re-read the state
summary and verify the prior gate's approval is recorded in this session before
writing any test or implementation; momentum/code never substitutes). SKILL.md
Hard gates — compact one-line echo of the same check. Version bump 1.0.0 → 1.0.1,
`last-reviewed` refreshed, LESSONS_LEARNED.md entry added (Validations: 1).

### 1.0.0 - 2026-10-24
**Trigger**: Initial creation.
**Changes**: Created the AAID skill: compact SKILL.md entrypoint with routing, hard
gates, evidence rules and maintenance protocol; methodology references
(PHASES, CHECKLIST, ZOMBIES, ROADMAP-DOMAIN/TECHNICAL/PRESENTATION/ACCEPTANCE,
DEPENDENCIES); acceptance Testing (four-layer) references (ATDD, ATDD-PHASES,
ATDD-CHECKLIST); maintenance/provenance references (SELF-IMPROVEMENT,
LESSONS_LEARNED, CHANGELOG, this file, ATTRIBUTION, SOURCE). Adapted from the pinned
upstream methodology per [ATTRIBUTION.md](ATTRIBUTION.md). The upstream checker
is added later in this change (pending at this entry's writing).
