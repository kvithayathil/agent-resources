---
name: github-triage
description: Triage GitHub issues through a label-based state machine with interactive grilling sessions. Use when user wants to triage issues, review incoming bugs or feature requests, prepare issues for an AFK agent, or manage issue workflow.
triggers:
  - triage issues
  - github triage
  - review bugs
  - feature requests
  - issue workflow
  - ready for agent
tags:
  - github
  - project-management
  - workflow
license: MIT
metadata:
  author: mattpocock
  version: "1.0"
source:
  repo: https://github.com/mattpocock/skills
  ref: main
  path: github-triage
---

# GitHub Issue Triage

Triage issues in the current repo using a label-based state machine. Infer the repo from `git remote`. Use `gh` for all GitHub operations.

## Reference docs

- [AGENT-BRIEF.md](AGENT-BRIEF.md) — how to write durable agent briefs
- [OUT-OF-SCOPE.md](OUT-OF-SCOPE.md) — how the `.out-of-scope/` knowledge base works

## Labels

| Label             | Type     | Description                              |
| ----------------- | -------- | ---------------------------------------- |
| `bug`             | Category | Something is broken                      |
| `enhancement`     | Category | New feature or improvement               |
| `needs-triage`    | State    | Maintainer needs to evaluate this issue  |
| `needs-info`      | State    | Waiting on reporter for more information |
| `ready-for-agent` | State    | Fully specified, ready for AFK agent     |
| `ready-for-human` | State    | Requires human implementation            |
| `wontfix`         | State    | Will not be actioned                     |

Every issue should have exactly **one** state label and **one** category label.

## State Machine

| Current State  | Can transition to | Who triggers it        | What happens                                                                                                         |
| -------------- | ----------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `unlabeled`    | `needs-triage`    | Skill (on first look)  | Issue needs maintainer evaluation. Skill applies label after presenting recommendation.                              |
| `unlabeled`    | `ready-for-agent` | Maintainer (via skill) | Issue is already well-specified and agent-suitable. Skill writes agent brief comment, applies label.                 |
| `unlabeled`    | `ready-for-human` | Maintainer (via skill) | Issue requires human implementation. Skill writes a brief comment summarizing the task, applies label.               |
| `unlabeled`    | `wontfix`         | Maintainer (via skill) | Issue is spam, duplicate, or out of scope. Skill closes with comment (and writes `.out-of-scope/` for enhancements). |
| `needs-triage` | `needs-info`      | Maintainer (via skill) | Issue is underspecified. Skill posts triage notes capturing progress so far + questions for reporter.                |
| `needs-triage` | `ready-for-agent` | Maintainer (via skill) | Grilling session complete, agent-suitable. Skill writes agent brief comment, applies label.                          |
| `needs-triage` | `ready-for-human` | Maintainer (via skill) | Grilling session complete, needs human. Skill writes a brief comment summarizing the task, applies label.            |
| `needs-triage` | `wontfix`         | Maintainer (via skill) | Maintainer decides not to action. Skill closes with comment (and writes `.out-of-scope/` for enhancements).          |
| `needs-info`   | `needs-triage`    | Skill (detects reply)  | Reporter has replied. Skill surfaces to maintainer for re-evaluation.                                                |

## Workflow: Show What Needs Attention

When the maintainer asks for an overview, query GitHub and present a summary grouped into three buckets:

1. **Unlabeled issues** — new, no labels at all
2. **`needs-triage` issues** — maintainer needs to evaluate
3. **`needs-info` issues with new activity** — reporter has commented since last triage notes

Display counts per group. Show issues oldest first. For each issue, show: number, title, age, and a one-line summary.

Let the maintainer pick which issue to dive into.

## Workflow: Triage a Specific Issue

### Step 1: Gather context

- Read the full issue: body, all comments, all labels, who reported it, when
- If there are prior triage notes comments, parse them to understand what has already been established
- Explore the codebase to build context
- Read `.out-of-scope/*.md` files and check if this issue matches a previously rejected concept

### Step 2: Present a recommendation

Tell the maintainer:

- **Category recommendation:** bug or enhancement, with reasoning
- **State recommendation:** where this issue should go, with reasoning
- If it matches a prior out-of-scope rejection, surface that
- A brief summary of what you found in the codebase that's relevant

Then wait for the maintainer's direction.

### Step 3: Bug reproduction (bugs only)

If the issue is categorized as a bug, attempt to reproduce it:

- Read the reporter's reproduction steps (if provided)
- Explore the codebase to understand the relevant code paths
- Try to reproduce the bug: run tests, execute commands, or trace the logic
- If reproduction succeeds, report what you found — include the specific behavior and where in the code it originates
- If reproduction fails, report that too
- If the report lacks enough detail to attempt reproduction, note that

### Step 4: Grilling session (if needed)

Interview the maintainer to build a complete specification. Follow the grill-me pattern:

- Ask questions one at a time
- Provide a recommended answer for each question
- If a question can be answered by exploring the codebase, explore the codebase instead
- Resume from prior triage notes — never re-ask resolved questions

### Step 5: Apply the outcome

Before posting any comment or applying any label, show the maintainer a **preview** of exactly what will be posted and which labels will be applied/removed. Only proceed on confirmation.

Depending on the outcome:

- **ready-for-agent** — post an agent brief comment (see [AGENT-BRIEF.md](AGENT-BRIEF.md))
- **ready-for-human** — post a comment summarizing the task
- **needs-info** — post triage notes with progress so far and questions for the reporter
- **wontfix (bug)** — post a polite comment explaining why, then close
- **wontfix (enhancement)** — write to `.out-of-scope/`, post a comment linking to it, then close (see [OUT-OF-SCOPE.md](OUT-OF-SCOPE.md))

## Workflow: Quick State Override

When the maintainer explicitly tells you to move an issue to a specific state, trust their judgment and apply the label directly. Still show a confirmation. Skip the grilling session.

## Needs Info Output

```markdown
## Triage Notes

**What we've established so far:**

- point 1
- point 2

**What we still need from you (@reporter):**

- question 1
- question 2
```

## Resuming Previous Sessions

When triaging an issue that already has triage notes from a previous session:

1. Read all comments to find prior triage notes
2. Parse what was already established
3. Check if the reporter has answered any outstanding questions
4. Present the maintainer with an updated picture
5. Continue the grilling from where it stopped
