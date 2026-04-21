---
title: "Modern Git Patterns, Commands & Approaches Research"
tags: ["git", "patterns", "research", "commands", "handover", "session"]
sources: []
contributors: ["Jm2A"]
created: 2026-04-21
updated: 2026-04-21
---

# Handover: Modern Git Patterns Skill Authoring

**Date**: 2026-04-21
**Status**: Complete
**Agent**: glm-5.1 via opencode

## Summary

Researched modern git patterns from 6 expert talks, 5 release notes, and GitHub Blog highlights. Synthesized into a version-aware agent skill at `skills/modern-git-patterns/`. All quality gates pass.

## Created Items

| Item | Location | Description |
|------|----------|-------------|
| Agent skill | `skills/modern-git-patterns/SKILL.md` | 489-line self-learning skill (git 2.50+) |
| Version map | `skills/modern-git-patterns/references/VERSION_FEATURE_MAP.md` | Features by git version |
| Detailed patterns | `skills/modern-git-patterns/references/DETAILED_PATTERNS.md` | Expanded diff, merge, worktree, stash, etc. |
| Quick reference | `skills/modern-git-patterns/references/COMMAND_QUICK_REFERENCE.md` | One-liner commands |
| Sources | `skills/modern-git-patterns/references/SOURCES.md` | Full bibliography |
| Lessons log | `skills/modern-git-patterns/references/LESSONS_LEARNED.md` | Empty — populated via use |
| Changelog | `skills/modern-git-patterns/references/CHANGELOG.md` | v1.0.0 entry |
| Knowledge page | `crosslink:modern-git-reference` | Full research reference document |

## Research Artifacts

| File | Location | Source |
|------|----------|--------|
| video1.en.srt | `.agent-workspace/git-research/` | Edward Thomson — NDC London 2025 |
| video2.en.srt | `.agent-workspace/git-research/` | "you only need 15ish git commands" |
| video3.en.srt | `.agent-workspace/git-research/` | "10 Little-Known Features You'll Love" |
| video4.en.srt | `.agent-workspace/git-research/` | "So You Think You Know Git Part 2" — DevWorld 2024 |
| video5.en.srt | `.agent-workspace/git-research/` | Scott Chacon — FOSDEM 2024 |
| video6.en.srt | `.agent-workspace/git-research/` | "Why everyone hates git submodules" |
| video*-unique.txt | `.agent-workspace/git-research/` | Deduplicated text extracts |

## Sources Consulted

**Primary evidence** (version claims grounded here):
- Git 2.50.0–2.54.0 Release Notes — `glab api` from gitlab.com/git-scm/git
- GitHub Blog "Highlights from Git 2.54" — https://github.blog/open-source/git/highlights-from-git-2-54/

**Pattern/workflow guidance**:
- Edward Thomson, NDC London 2025 (video)
- "you only need 15ish git commands" (video)
- "10 Little-Known Features You'll Love" (video)
- "So You Think You Know Git Part 2", DevWorld 2024 (video)
- Scott Chacon, FOSDEM 2024 (video)
- "Why everyone hates git submodules" (video)

## Verification

- VDD/VSDD applied: every feature claim annotated with `[2.XX+]` from release notes
- `just check`: all 26 skills valid, all lint/type/dead-code/duplication/security gates pass
- Local git version verified: 2.54.0
- Skill registered in SKILL_INDEX.yaml via `just sync`

## Gotchas for Continuation

- SRT files are verbose — extract unique lines with `rg -v '^\d+$|^[0-9]{2}:[0-9]{2}.*-->' file | rg -v '^\s*$' | sort -u`
- `glab api` needs URL-encoded paths (`git-scm%2Fgit`)
- AgentSkills spec: no `sources` in frontmatter, SKILL.md < 500 lines
- Subagent `explore` struggled with large SRT files — preprocess first

## Next Steps

1. Update when git 2.55+ releases (fetch RelNotes, update VERSION_FEATURE_MAP)
2. Populate LESSONS_LEARNED.md through real-world use
3. Promote validated lessons to SKILL.md after 3+ confirmations
4. Prune unused sections
