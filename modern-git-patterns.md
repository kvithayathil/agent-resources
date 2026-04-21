---
title: "Modern Git Patterns, Commands & Approaches Research"
tags: ["git", "patterns", "research", "commands", "handover", "session"]
sources: []
contributors: ["Jm2A"]
created: 2026-04-21
updated: 2026-04-21
---

# Session Handover: Modern Git Patterns Skill

**Date**: 2026-04-21
**Session type**: Research → Skill authoring

## What Was Done

1. **Research phase**: Downloaded subtitles from 6 YouTube talks via `yt-dlp --cookies-from-browser brave`
2. **Release notes**: Fetched git 2.50–2.54 release notes via `glab api` from gitlab.com/git-scm/git
3. **Blog analysis**: Fetched GitHub Blog "Highlights from Git 2.54" (covers 2.53 + 2.54)
4. **Synthesis**: Compiled evidence into structured skill with version-aware annotations
5. **Skill authored**: `skills/modern-git-patterns/` — 489 lines, self-learning, VDD/VSDD-aligned
6. **Quality gate**: `just check` passes (all 26 skills valid)

## Skill Location

```
skills/modern-git-patterns/
├── SKILL.md                              (489 lines — main skill)
└── references/
    ├── VERSION_FEATURE_MAP.md            (feature availability by git version)
    ├── DETAILED_PATTERNS.md              (expanded diff, merge, worktree, stash, etc.)
    ├── COMMAND_QUICK_REFERENCE.md        (one-liner commands)
    ├── SOURCES.md                        (full bibliography)
    ├── LESSONS_LEARNED.md                (empty — populated via real-world use)
    └── CHANGELOG.md                      (v1.0.0 entry)
```

## Sources Analyzed

| Source | Type | Key Contributions |
|--------|------|-------------------|
| Git 2.50.0 RelNotes | Release notes | Incremental MIDX, reflog expire, maintenance tasks |
| Git 2.51.0 RelNotes | Release notes | Stash import/export, reftable announcement, switch/restore stable |
| Git 2.52.0 RelNotes | Release notes | `git last-modified`, `git repo`, geometric maintenance, sparse index |
| Git 2.53.0 RelNotes | Release notes | `git replay` atomic refs, `blame --diff-algorithm`, `maintenance is-needed` |
| Git 2.54.0 RelNotes | Release notes | `git history`, config-based hooks, geometric default, `log -L` + pickaxe |
| GitHub Blog 2.54 | Curated highlights | Detailed explanations of `git history`, hooks, geometric repack, HTTP 429 |
| Edward Thomson (NDC 2025) | Video talk | Git internals, libgit2, usability patterns |
| "15ish git commands" | Video talk | Essential command set, practical workflow |
| "10 Little-Known Features" | Video talk | Notes, worktree, reflog, bisect, rev-list, format-patch, request-pull |
| "So You Think You Know Git Pt2" (DevWorld) | Video talk | Advanced patterns, internals |
| Scott Chacon (FOSDEM 2024) | Video talk | blame -C, sparse checkout, partial clone, maintenance, SSH signing, rerere, fsmonitor |
| "Why everyone hates submodules" | Video talk | Submodule problems, alternatives |

## VDD/VSDD Verification

- Every feature claim annotated with minimum git version (`[2.XX+]`)
- Version annotations sourced directly from release notes (primary evidence)
- GitHub Blog used as secondary interpretation layer
- Video talks used for pattern/workflow guidance (not version claims)
- Common Mistakes table grounded in repeated expert recommendations
- No claims made without traceable source

## Artifacts in .agent-workspace

```
.agent-workspace/git-research/
├── video1.en.srt   (Edward Thomson NDC 2025)
├── video2.en.srt   (15ish git commands)
├── video3.en.srt   (10 Little-Known Features)
├── video4.en.srt   (So You Think You Know Git Pt2)
├── video5.en.srt   (Scott Chacon FOSDEM 2024)
├── video6.en.srt   (Why everyone hates submodules)
└── video*-unique.txt (deduplicated text extracts for videos 1,2,4,5)
```

## Next Steps for Continuation

- **Update skill** when git 2.55+ releases: fetch new RelNotes, update VERSION_FEATURE_MAP
- **Populate LESSONS_LEARNED.md**: use the skill in real tasks, record patterns that prove useful
- **Promote validated lessons**: after 3+ real-world validations, move from LESSONS_LEARNED to SKILL.md
- **Prune stale content**: if any section proves unused across multiple sessions, remove it
- **Verify against local git**: skill assumes git 2.54 — local version is 2.54.0 (verified)

## Gotchas for Future Sessions

- SRT subtitle files are very verbose (auto-generated captions, triple-repeated lines)
- Subagent `explore` type struggled to read large SRT files — better to extract unique lines first with `rg -v | sort -u`
- `glab api` needs URL-encoded path: `git-scm%2Fgit` for the git project
- `sources` is not a valid frontmatter field in AgentSkills spec — moved to references/SOURCES.md
- SKILL.md must be < 500 lines per spec — moved detailed content to references/DETAILED_PATTERNS.md
