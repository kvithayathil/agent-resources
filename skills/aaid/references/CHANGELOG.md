# AAID Changelog

> Record of all substantive updates to this skill. Every entry: trigger and change.

## Format

```
### [version] - YYYY-MM-DD
**Trigger**: What task/situation prompted the update
**Changes**: What was added, removed, or modified
```

---

### 1.0.2 - 2026-10-24
**Trigger**: Closure-gate reviews (6.2 code review, 6.3 adversarial) plus two
post-merge adversarial iterations on the shipped checker.
**Changes**: check-upstream.sh — provenance integrity: UNCHANGED always
requires a human-integrated baseline. ABSENCE OF PROVENANCE NEVER
AUTHENTICATES: the SOURCE.md check-status pin when SOURCE exists, otherwise
the manifest integrated_commit; a manifest WITHOUT integrated_commit and
without SOURCE.md is an ERROR fail-closed (the legacy first-run
resolved_commit default is REMOVED — it could launder a fetched-only
manifest after the provenance directories were renamed away; genuine
first-run vendoring REQUIRES the new-schema manifest, which the shipped
assets/upstream/MANIFEST.json now carries with integrated_commit set to
54b4e5f0). A fetch advances only resolved_commit. Integration sync: when
the SOURCE pin already equals the previously resolved commit, the next
authorized update syncs integrated_commit to it (check-only never writes;
the sync piggybacks on the next --update). Boundary/write discipline: the
skill root is pinned ONCE as a dirfd (identity anchor; a symlinked root's
final component is an ERROR) and re-verified before EVERY write
(persistent root rename+symlink swap → ERROR, external tree untouched),
plus .cache identity verification; a pivot detected at the lock path
(symlinked update.lock) gets a tamper-aware reason; all containment checks
and ALL writes (live and staging) are dirfd-relative with O_NOFOLLOW temps
and entry-replacing os.replace; ancestor levels are revalidated
immediately after their mkdir; the staging TEMP is verified at replace
time and a substituted temp is a verdict-fatal ERROR (NOT a cleanup
warning), while the staged dir itself and every staging-cleanup CHILD
have their (dev, ino) verified at enumeration→open — BEFORE recursion
(a pre-open substitution — including a renamed-away child replaced by a
foreign populated dir under the SAME name — refuses the cleanup; the
foreign tree is spared with ONE sanitized WARNING); the child
rmdir(name, dir_fd=parent) then acts on the already-verified name with
no fresh comparison; snapshot read INTERMEDIATE
components are nofollow-walked dirfd-relative (a pre-open pivot of a
nested directory even with matching-hash content is an ERROR before any
bytes are read), and only the final component is opened (the pinned
replace-not-follow read contract, SHA-disciplined); staging cleanup is
fd-anchored end-to-end (contents deleted via the held staging fd — the
staging name is never resolved for the contents — and the top name is
rmdir'ed dir_fd-relative ONLY after a final identity re-stat: a
substituted foreign dir is spared with one sanitized WARNING, and a
POPULATED substitute fails the rmdir (ENOTEMPTY → refuse + warn)). Contract: no borrowed dirfd is
ever returned by the walk helper (empty chains dup the base) — a
top-level-file manifest path exercises the full --update flow in tests.
Read discipline: trusted reads (manifest, SOURCE.md) open O_NOFOLLOW and
fstat the SAME fd, requiring S_ISREG — symlinked records are tampered
provenance, FIFOs/devices refused fast (no unbounded read). Local snapshot
reads follow a final-component symlink by pinned contract
(replace-not-follow) and are SIZE-CAPPED at the manifest-declared bytes +
64KB slack (sanitized ERROR beyond — /dev/zero redirection cannot drive an
unbounded read). Error contract: exactly ONE sanitized ERROR line on
stderr for every failure (a spurious UnboundLocalError-mask failure mode
is regression-pinned as single-line). Transport: every gh call is bounded
END-TO-END — AAID_CHECK_TIMEOUT (default 30s, clamped ≤600s,
nan/inf/non-numeric rejected as sanitized ERRORs) covering BOTH stdout
streaming (select over both pipes so stderr can never fill) and the
post-EOF wait (a gh closing stdout then blocking is killed and reported),
a 4MB raw-stdout cap enforced before any JSON parse or decode (exact
boundary pinned by test), a stderr cap, and a 2MB decoded-payload cap.
stale-lock errors report the lock age with manual-removal instructions
and never auto-remove; lock unlinks are dirfd-relative and inode-matched
against the HELD lock fd. Supported-interpreter policy: the checker
preflights CPython >= 3.11 beside gh (a supported-interpreter policy, not
a single-primitive attribution; 3.10 is EOL); stock macOS
/usr/bin/python3 3.9 fails sanitized BEFORE any update — no fallback
path. Environment: AAID_SKILL_ROOT is
honored ONLY when AAID_FAKE_ROOT is set (test harness marker); production
derives the root strictly from the script's own location.
DEPENDENCIES.md — scoped the "Never stub" prose to acceptance/integration
tests (unit-level mocking of owned persistence stays allowed per the
matrix). ATTRIBUTION.md — flagged the openspec evidence path as
local-only, pointing committed consumers at assets/upstream/MANIFEST.json.
Fixed loose "PHASES.md §6.2" citations to §6 item 2. Test suite extended
to the new contracts (93 tests).

### 1.0.1 - 2026-10-24
**Trigger**: Behavioral trials showed agents crossing a pending review gate before
approval (self-caught, reverted, and disclosed in the retained trial evidence): the
agent twice crossed a pending `AWAITING` gate mid-session before scripted
approval (GREEN implementation+run before segment-2 re-approval in one trial;
implementation written before the RED test existed in the other). Both self-caught, reverted,
disclosed; the passive PHASES.md §6 item 2 prohibition failed to prevent the drift in the moment.
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
