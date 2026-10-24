# Source Provenance — aaid

Category A (modified third-party methodology) provenance record.

- **Repository**: https://github.com/dawid-dahl-umain/augmented-ai-development
- **Ref**: `main` (default branch); **resolved pinned commit**: `54b4e5f0600f0d49131b74ffcb686876582ee20c`
  (tree `b0da7f19f18fb012df34ba43611a99482dbbc7ef`, commit author date `2026-08-30T19:51:46Z`)
- **Consumed paths**: 12 paths — canonical manifest at
  `openspec/changes/add-aaid-skill/evidence/source-manifest.md` (paths + git blob SHAs,
  all 12 cross-checked against the pinned tree). Raw snapshot pin: the same commit,
  held under `assets/upstream/` with original relative paths plus manifest/hashes
  (added by task 3.2).
- **Installed**: 2026-10-24
<!-- BEGIN CHECK-STATUS: checker-maintained — rewrite only via an authorized
     `check-upstream.sh --update` run (design D6); lines inside this block are
     data consumed by the checker's freshness report. -->
- Last successful check: **2026-10-24 — check-only: UNCHANGED** (`bash
  scripts/check-upstream.sh`, exit 0; pinned `resolved_commit` 54b4e5f0 was
  tip of `main` at check time). No authorized `--update` refresh has been
  executed yet; the integrated pin below is the only reviewed state.
- Fetched commit: none
- Integrated pin: `54b4e5f0600f0d49131b74ffcb686876582ee20c`
  (tree `b0da7f19f18fb012df34ba43611a99482dbbc7ef`, commit author date `2026-08-30T19:51:46Z`)
  — the reviewed/integrated content only; never advanced by a fetch (D6).
<!-- END CHECK-STATUS -->
- **Provider**: manual
- **Lock entry**: `skills/skills-lock.json` — present; the canonical `aaid` entry (ref
  `54b4e5f0600f0d49131b74ffcb686876582ee20c`, source_type `gh-api`, provider `manual`,
  installed_at `2026-10-24`, remote_path `.`) was added in task 3.2 and this record is
  kept consistent with it.

## Fetched vs integrated pins

Initially the fetched pin and the integrated pin are equal: both are the resolved
commit `54b4e5f0600f0d49131b74ffcb686876582ee20c`, because all consumed content was
reviewed and integrated during the change that created this skill. Thereafter the
distinction holds per the change design (D6): the **lock file pin represents
reviewed/integrated content only**, never merely the latest remote fetch. A fresh
fetch that is not yet semantically reviewed remains "unreviewed fetched" and keeps
being flagged by subsequent checks until a human reviews and integrates it.

## Secondary influence

A local user-provided draft (`~/Downloads/ADTT-SKILL.md`, a rendered-HTML export) was
treated as a **user synthesis**: semantic influence only (four-layer framing, phase
gates, divergence decisions D4). Nothing was copied from it and no redistribution
rights are claimed from it.

## Upstream changes

This record's check metadata is refreshed only by an authorized `--update` run of the
skill's checker (D6). Check-only runs leave this file untouched. Failed or partial
fetches preserve the last good data and never claim freshness.
