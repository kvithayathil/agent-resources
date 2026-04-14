---
title: Enhancement Proposal Template
status: reference
created: 2026-04-14
updated: 2026-04-14
applies-to:
  - enhancements
---

# Enhancement Proposal Specification

## Purpose

Every enhancement in `docs/enhancements/` follows this spec. It ensures proposals are structured, traceable, and decision-ready.

## File Naming

- Lowercase, hyphenated, descriptive: `self-learning-hooks.md`
- One enhancement per file
- Never rename after creation (breaks index references)

## Required Frontmatter

Every enhancement **must** include this YAML frontmatter:

```yaml
---
title: Short Descriptive Title
status: proposed
created: YYYY-MM-DD
updated: YYYY-MM-DD
applies-to:
  - skill-or-component-name
---
```

### Fields

| Field | Required | Description |
|-------|----------|-------------|
| `title` | Yes | Human-readable title. Keep under 80 chars. |
| `status` | Yes | Current lifecycle state. See Status Lifecycle below. |
| `created` | Yes | Date first created. Never changes. |
| `updated` | Yes | Date of last substantive edit. Update on every change. |
| `applies-to` | Yes | List of skills, components, or systems affected. |
| `supersedes` | No | Filename of enhancement this replaces (if any). |
| `depends-on` | No | List of enhancement filenames this depends on. |
| `assignee` | No | Person or agent responsible. |

### Status Lifecycle

```
proposed → investigating → accepted → implementing → complete
                 ↓              ↓
              rejected       deferred
                              ↓
                       superseded-by:<name>
```

| Status | Meaning | Entry Criteria |
|--------|---------|---------------|
| `proposed` | Initial idea, needs discussion | File created with all required sections |
| `investigating` | Researching feasibility | Someone actively researching |
| `accepted` | Approved for implementation | Decision recorded in the proposal |
| `implementing` | Currently being built | Work has started |
| `complete` | Done and in use | All checklist items checked |
| `rejected` | Decided against | Rationale documented |
| `deferred` | Good idea, not now | Reason and revisit date noted |
| `superseded-by` | Replaced by newer proposal | New enhancement filename noted |

Status may move forward, backward, or to terminal states at any time.

## Required Sections

Every enhancement **must** contain these sections in this order:

### 1. Problem

What is the pain point or gap? Why does this matter?

- State the problem concretely
- Include evidence if available (e.g., "Failed 3 times in production")
- One paragraph minimum

### 2. Proposed Solution

What are you proposing and how does it work?

- Describe the approach
- Explain why this approach over alternatives
- Include diagrams, tables, or code as needed

### 3. Alternatives Considered

What other approaches were evaluated and why were they not chosen?

- List at least one alternative
- State why it was inferior or inappropriate
- Even a brief "Considered X but rejected because Y" suffices

### 4. Impact

Who and what does this affect?

- Skills modified
- Breaking changes
- Dependencies introduced
- Affected agents or workflows

### 5. Implementation Plan

Step-by-step plan to build it.

- Ordered list of tasks
- Each task should be independently verifiable
- Include a checklist that can be marked off

### 6. Success Criteria

How do we know this enhancement worked?

- Measurable or observable outcomes
- At least 3 criteria

### 7. Open Questions

What is still undecided? What needs input?

- List unresolved questions
- Mark which ones block implementation vs. are nice-to-resolve
- Acceptable to have "None" if fully specified

## Optional Sections

Add any of these when relevant:

| Section | When to Include |
|---------|----------------|
| Security Considerations | If the change affects auth, data handling, or attack surface |
| Performance Impact | If the change adds runtime overhead |
| Migration Guide | If existing skills need to be updated |
| References | External links, research, related enhancements |
| Appendix | Supplementary data that would clutter the main body |

## Formatting Rules

- Use ATX headings (`##`)
- Code blocks must specify language
- Tables for structured comparisons
- Diagrams in Mermaid or ASCII
- Keep total length under 300 lines; move detail to appendices

## Index Maintenance

The `README.md` index must be updated when:

- A new enhancement is created (add row)
- Status changes (update status column and `updated` date)
- An enhancement is superseded (note in both entries)

## Validation Checklist

Before considering any enhancement proposal valid:

- [ ] All required frontmatter fields present
- [ ] Status matches a valid lifecycle value
- [ ] All 7 required sections present and non-empty
- [ ] Index table updated
- [ ] `applies-to` references real skills/components
- [ ] No orphaned references (all links resolve)
