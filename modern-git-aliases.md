---
title: "Modern Git Aliases: 2.50+ Feature Shortcuts"
tags: ["git", "aliases", "config", "reference"]
sources: []
contributors: ["Jm2A"]
created: 2026-04-21
updated: 2026-04-21
---

Modern git aliases derived from features in git 2.50–2.54. All assume git 2.54+.

## Recommended Aliases

```gitconfig
[alias]
    # Modern commands (2.51+ stable)
    sw = switch
    rs = restore
    swc = switch -c
    sw- = switch -

    # Safety
    pf = push --force-with-lease
    undo = reset --soft HEAD~1
    redo = reset --hard HEAD@{1}
    recover = "!f() { git branch recovered \"$1\"; snip }; snip f"

    # Investigation (2.52–2.54)
    blame-move = blame -C -w
    blame-func = "!f() { git blame -C -w -L :\"$1\" \"$2\"; snip }; snip f"
    trace = "!f() { git log -L :\"$1\":\"$2\"; snip }; snip f"
    who = last-modified
    pick = "!f() { git log -S \"$1\" --oneline; snip }; snip f"
    pickre = "!f() { git log -G \"$1\" --oneline; snip }; snip f"

    # Diff improvements
    wdiff = diff --word-diff
    hdiff = diff --diff-algorithm=histogram
    rdiff = "!f() { git range-diff \"$1\" \"$2\"; snip }; snip f"

    # Stash (2.51–2.52)
    stashall = stash push -u -m
    stashstaged = stash push -S

    # History rewriting (2.54+)
    reword = history reword
    split = history split

    # Maintenance (2.50+, geometric default 2.54+)
    maint = maintenance run

    # General
    br = branch --sort=-committerdate
    st = status --short --branch
    lg = log --oneline --graph --decorate -20
    last = log -1 HEAD --stat
    visual = log --oneline --graph --all --decorate
    unstage = restore --staged
    contributors = shortlog --summary --numbered
```

## What Changed vs Traditional Aliases

| Old | Issue | New | Why |
|-----|-------|-----|-----|
| `co = checkout` | `switch` is the modern command (2.51+) | `sw = switch` | Separates branch switching from file restoration |
| `unstage = reset HEAD --` | `restore --staged` is the dedicated command | `unstage = restore --staged` | Clearer intent, no HEAD pointer manipulation |
| `wip = !git add -A && snip git commit -m WIP` | Adds everything blindly | Removed | Risky; snip use explicit `git add -p` instead |
| (missing) | `--force-with-lease` too long to type | `pf = push --force-with-lease` | Safe force push should be the default |
| (missing) | `git blame -C -w` is a common combo | `blame-move = blame -C -w` | Detects code movement, ignores whitespace |
| (missing) | `git log -L :func:file` hard to remember syntax | `trace` shell alias | Traces function history across renames |
| (missing) | `git history reword` new in 2.54 | `reword = history reword` | Reword without touching working tree |
| (missing) | `--word-diff` and histogram diff | `wdiff`, `hdiff` | Better diff output on demand |

## When to Use

- `pf` instead of `push --force` — always. No performance difference. `--force-with-lease` rejects if remote has commits you haven't fetched.
- `trace` when investigating when a function changed and how.
- `pick` when searching for commits that added/removed a specific string.
- `blame-move` instead of bare `blame` on any file with refactored code.
- `wdiff` for prose/config review where line-level diffs are noisy.
- `reword` instead of `rebase -i` when you only need to fix a commit message.
- `maint` when repo feels slow (though `git maintenance start` handles this automatically).

## Prerequisites

```bash
# Enable these once for aliases to work optimally:
git config --global push.autoSetupRemote true   # makes swc + push seamless
git config --global branch.sort -committerdate  # br alias benefits
git config --global stash.index true             # 2.52+ stash preserves index
git config --global diff.algorithm histogram     # hdiff becomes the default
git maintenance start                            # maint alias less needed
```

## Sources

- git 2.50–2.54 Release Notes: https://gitlab.com/git-scm/git/-/blob/HEAD/Documentation/RelNotes/
- git-switch docs: https://git-scm.com/docs/git-switch
- git-restore docs: https://git-scm.com/docs/git-restore
- git-hook docs: https://git-scm.com/docs/git-hook
- Skill reference: skills/modern-git-patterns/references/DETAILED_PATTERNS.md
- Skill quick ref: skills/modern-git-patterns/references/COMMAND_QUICK_REFERENCE.md

Last verified: 2026-04-21 against git 2.54.0.
