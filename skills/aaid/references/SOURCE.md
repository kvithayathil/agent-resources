# Source Provenance — aaid

Category A (modified third-party methodology) provenance record.

- **Repository**: https://github.com/dawid-dahl-umain/augmented-ai-development
- **Ref**: `main` (default branch); **resolved pinned commit**: `54b4e5f0600f0d49131b74ffcb686876582ee20c`
  (tree `b0da7f19f18fb012df34ba43611a99482dbbc7ef`, commit author date `2026-08-30T19:51:46Z`)
- **Consumed paths**: 12 paths — machine-readable manifest with per-file git blob
  SHAs, byte sizes and content hashes at `assets/upstream/MANIFEST.json` (cross-
  checked against the pinned tree; regenerated only by an authorized
  `check-upstream.sh --update`). Consumed upstream documents at the pinned commit:
  the guide (`docs/aidd-workflow.md`), rules (`rules/aaid/aaid-development-rules.mdc`),
  workflow diagram (`aaid-workflow-diagram.mermaid`), appendix A (four-layer
  acceptance model), appendices B/D/E, both plugin workflow entrypoints
  (`plugins/aaid-tdd/`, `plugins/aaid-bdd/`), and their `.claude-plugin/` manifests.
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
  — the reviewed/integrated content only; never advanced by a fetch.
<!-- END CHECK-STATUS -->
- **Provider**: manual
- **Lock entry**: `skills/skills-lock.json` — present; the canonical `aaid` entry (ref
  `54b4e5f0600f0d49131b74ffcb686876582ee20c`, source_type `gh-api`, provider `manual`,
  installed_at `2026-10-24`, remote_path `.`) was added alongside this record and is
  kept consistent with it.

## Fetched vs integrated pins

Initially the fetched pin and the integrated pin are equal: both are the resolved
commit `54b4e5f0600f0d49131b74ffcb686876582ee20c`, because all consumed content was
reviewed and integrated during the change that created this skill. Thereafter the
distinction holds per the provenance policy: the **lock file pin represents
reviewed/integrated content only**, never merely the latest remote fetch. A fresh
fetch that is not yet semantically reviewed remains "unreviewed fetched" and keeps
being flagged by subsequent checks until a human reviews and integrates it.

## Secondary influence

A local user-provided draft (`~/Downloads/ADTT-SKILL.md`, a rendered-HTML export) was
treated as a **user synthesis**: semantic influence only (four-layer framing, phase
gates, the recorded divergence decisions). Nothing was copied from it and no redistribution
rights are claimed from it.

## Follow-up evaluator foundation

A generalized `skill-eval` change is a confirmed separate follow-up (not part of this
skill). Its foundation is `anthropics/skills` `skill-creator` — paired skill/baseline
runs, evidence-based grading, benchmark mean ± standard deviation, variance analysis,
and human review. Surveyed complements, none adopted here: `addyosmani/agent-skills`
eval architecture, the `dietrichgebert/ponytail` agentic benchmark (its harness
blocks agent Bash execution — unsuitable unchanged for behavioral trials), and the
`cursor/plugins` pstack blinded-eval playbook. Fuller research notes on methodology,
rights resolution, and evaluator sources live in the local-only `openspec/research/`
tree (not committed with the hub).

## Upstream changes

This record's check metadata is refreshed only by an authorized `--update` run of the
skill's checker. Check-only runs leave this file untouched. Failed or partial
fetches preserve the last good data and never claim freshness.
