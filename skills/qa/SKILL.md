---
name: qa
description: Interactive QA session where user reports bugs or issues conversationally, and the agent files GitHub issues. Explores the codebase in the background for context and domain language. Use when user wants to report bugs, do QA, file issues conversationally, or mentions "QA session".
triggers:
  - qa session
  - report bugs
  - file issues
  - qa
  - bug report
tags:
  - testing
  - qa
  - github
license: MIT
metadata:
  author: mattpocock
  version: "1.0"
source:
  repo: https://github.com/mattpocock/skills
  ref: main
  path: qa
---

# QA Session

Run an interactive QA session. The user describes problems they're encountering. You clarify, explore the codebase for context, and file GitHub issues that are durable, user-focused, and use the project's domain language.

## Instructions

### For each issue the user raises

#### 1. Listen and lightly clarify

Let the user describe the problem in their own words. Ask **at most 2-3 short clarifying questions** focused on:

- What they expected vs what actually happened
- Steps to reproduce (if not obvious)
- Whether it's consistent or intermittent

Do NOT over-interview. If the description is clear enough to file, move on.

#### 2. Explore the codebase in the background

While talking to the user, kick off an Agent (subagent_type=Explore) in the background to understand the relevant area. The goal is NOT to find a fix — it's to:

- Learn the domain language used in that area (check UBIQUITOUS_LANGUAGE.md)
- Understand what the feature is supposed to do
- Identify the user-facing behavior boundary

#### 3. Assess scope: single issue or breakdown?

Before filing, decide whether this is a **single issue** or needs to be **broken down** into multiple issues.

Break down when:

- The fix spans multiple independent areas
- There are clearly separable concerns that different people could work on in parallel
- The user describes something that has multiple distinct failure modes or symptoms

Keep as a single issue when:

- It's one behavior that's wrong in one place
- The symptoms are all caused by the same root behavior

#### 4. File the GitHub issue(s)

Create issues with `gh issue create`. Do NOT ask the user to review first — just file and share URLs.

Issues must be **durable** — they should still make sense after major refactors. Write from the user's perspective.

##### Single issue template

```markdown
## What happened

[Describe the actual behavior, in plain language]

## What I expected

[Describe the expected behavior]

## Steps to reproduce

1. [Concrete, numbered steps]
2. [Use domain terms, not internal module names]
3. [Include relevant inputs, flags, or configuration]

## Additional context

[Any extra observations — use domain language but don't cite files]
```

##### Breakdown template (multiple issues)

Create issues in dependency order (blockers first).

```markdown
## Parent issue

#<parent-issue-number> or "Reported during QA session"

## What's wrong

[Describe this specific behavior problem — just this slice]

## What I expected

[Expected behavior for this specific slice]

## Steps to reproduce

1. [Steps specific to THIS issue]

## Blocked by

- #<issue-number> or "None — can start immediately"

## Additional context

[Any extra observations relevant to this slice]
```

Rules for all issue bodies:

- **No file paths or line numbers** — these go stale
- **Use the project's domain language** (check UBIQUITOUS_LANGUAGE.md if it exists)
- **Describe behaviors, not code**
- **Reproduction steps are mandatory**
- **Keep it concise** — a developer should be able to read the issue in 30 seconds

After filing, print all issue URLs and ask: "Next issue, or are we done?"

#### 5. Continue the session

Keep going until the user says they're done. Each issue is independent — don't batch them.
