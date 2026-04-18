---
title: "Modern Git Reference: Commands, Patterns & Approaches (2.50+)"
tags: ["git", "reference", "commands", "patterns", "version-aware"]
sources: []
contributors: ["Jm2A"]
created: 2026-04-21
updated: 2026-04-21
---

# Modern Git Reference: Commands, Patterns & Approaches (2.50+)

Version-aware git reference grounded in git 2.50–2.54 release notes, GitHub Blog highlights, and expert talks. Check `git --version` before using version-specific features.

## History Rewriting

### git history (experimental) [2.54+]
- `git history reword <commit>` — reword commit message without touching working tree/index. Works in bare repos.
- `git history split <commit>` — split a commit into two via hunk selection (add -p style). Creates new parent commit with selected hunks.
- Limitations: No merge commits. Refuses operations that would cause conflicts.
- Built on `git replay` machinery.

### git replay (experimental) [2.53+]
- `git replay --onto <new-base> <upstream>..<branch>` — replay without touching working tree
- `git replay --revert <range>` — revert mode [2.54+]
- Atomic ref updates by default [2.53+] (no longer prints update-ref to stdout)
- Drops commits that become empty during replay [2.54+]
- Supports replaying to root commit [2.54+]

### git rebase --trailer [2.54+]
- `git rebase --trailer "Reviewed-by: Name <email>"` — append trailer to every rebased commit

## Safety Patterns

### --force-with-lease
Always prefer over `--force`. Checks remote ref hasn't changed since last fetch. Safer force push.

### reflog
- `git reflog --date=relative` — view HEAD movement history
- `git reflog --pretty=format:'%h %gd %gs %ci'` — custom format
- `git branch recovered <reflog-hash>` — recover lost commits
- Entirely local, not shared with remotes

### rerere (Reuse Recorded Resolution)
- `git config --global rerere.enabled true` — record and reuse merge conflict resolutions
- Valuable for repeated rebasing of long-running branches

## Maintenance & Performance

### git maintenance [2.50+, geometric default 2.54+]
- `git maintenance start` — one-time setup, registers cron/launchd jobs
- `git maintenance run` — manual run (geometric strategy default in 2.54+)
- `git maintenance is-needed` [2.53+] — check if maintenance needed
- Hourly: incremental repack (geometric), commit-graph, loose object collection, prefetch
- Daily: more aggressive repack
- Geometric strategy combines packs incrementally (avoids full GC)

### commit-graph
- `git commit-graph write --reachable --changed-paths`
- Speeds up log, branch --contains, traversal-heavy ops
- `commitGraph.changedPaths` config [2.52+]

### core.fsmonitor [2.50+]
- `git config core.fsmonitor true && git config core.untrackedCache true`
- Uses OS file watcher instead of scanning every file
- Critical for repos with 100K+ files (status: seconds → milliseconds)

### Multi-Pack Indexes
- `git multi-pack-index write`
- Incremental MIDX with compaction [2.54+]
- Geometric repacking now default in maintenance [2.54+]

### Prefetching [2.50+]
- Maintenance prefetches remote refs hourly in background
- Subsequent `git fetch` nearly instant

## Sparse & Partial Operations

### sparse-checkout
- `git clone --filter=blob:none --sparse <url>` then `git sparse-checkout init --cone`
- `git sparse-checkout set dir1 dir2` — add directories
- `git sparse-checkout clean` [2.52+] — prune files outside sparse paths
- `git config index.sparse true` — sparse index for better performance
- Use `--cone` mode for best performance

### partial clone
- `git clone --filter=blob:none <url>` — no blobs (downloaded on demand)
- `git clone --filter=blob:limit=1m <url>` — filter blobs > 1MB
- `git clone --filter=tree:0 <url>` — no trees either [2.50+]

### git backfill (experimental) [2.54+]
- `git backfill -- '*.c'` — download missing blobs for specific paths
- `git backfill main~100..main` — scope to specific range

## Config-Based Hooks [2.54+]

```gitconfig
[hook "linter"]
    event = pre-commit
    command = ~/bin/linter --cpp20
[hook "no-leaks"]
    event = pre-commit
    command = ~/bin/leak-detector
```

- `git hook list pre-commit` — show configured hooks (with source: global/local)
- `hook.<name>.enabled = false` — disable without removing
- Multiple hooks per event, run in config order
- Traditional `.git/hooks/` scripts still work, run last
- Can be defined in ~/.gitconfig (global), /etc/gitconfig (system), or per-repo

## Signing & Verification

### SSH Signing [2.34+]
```gitconfig
[user]
    signingKey = ~/.ssh/id_ed25519.pub
[gpg]
    format = ssh
[commit]
    gpgSign = true
```
Upload SSH public key to GitHub/GitLab for verification.

### Expired Key Handling [2.54+]
Signatures from since-expired GPG keys shown as good signatures (not alarming red).

## Blame & History Investigation

### git blame advanced
- `git blame -C` — detect code movement from other files
- `git blame -C -C` — detect code copied from other files
- `git blame -w` — ignore whitespace
- `git blame -L 100,150` — specific line range
- `git blame -L :func_name` — blame a function
- `git blame --diff-algorithm=histogram` [2.53+] — choose diff algo

### git log -L [2.54+ enhanced]
- `git log -L :func:file.c` — trace function history
- Now compatible with `-S`, `-G` (pickaxe), `--word-diff`, `--color-moved` [2.54+]

### git log pickaxe
- `git log -S "string" --oneline` — find commits adding/removing string
- `git log -G "pattern" --oneline` — find commits matching regex in diff

### Other tools
- `git last-modified <path>` [2.52+] — closest ancestor commit touching path
- `git rev-list --maximal-only` [2.54+] — only commits not reachable by others

## Diff & Merge

- `git diff --word-diff` — word-level differences
- `git diff --diff-algorithm=histogram` — often cleaner diffs
- `git range-diff A..B C..D` — compare two versions of a branch
- `git config diff.algorithm histogram` — set as default
- Histogram fix [2.54+]: compaction no longer produces redundant output
- `git config rerere.enabled true` — record/reuse merge conflict resolutions

## Worktree

- `git worktree add ../feature-branch feature` — work on multiple branches simultaneously
- `git worktree list` / `git worktree remove ../feature-branch`
- Best practice: short-lived workspaces, same level as main repo

## Stash

- `git stash push -u -m "desc"` — include untracked files
- `git stash push -S` — staged changes only
- `git config stash.index true` [2.52+] — pop/apply preserves index
- `git stash export / import` [2.51+] — interchange format

## Submodules

- `git clone --recursive <url>` — clone with submodules
- `git submodule update --init --recursive` — update after branch switch
- `git config --global submodule.recurse true` — auto-update
- Prefer package managers, git subtree, or sparse checkout when possible

## Status & Config

- `status.compareBranches = @{upstream} @{push}` [2.54+] — compare against multiple refs
- `branch.sort -committerdate` — sort branches by recent commit
- `column.ui auto` — display lists in columns
- `includeIf` — conditional config per directory
- Non-ASCII aliases [2.54+]: `[alias "hämta"] command = fetch`

## Bisect

- `git bisect start && git bisect bad && git bisect good <known-good>`
- `git bisect run ./test-script.sh` — automated binary search
- `git fsck --full` — repository integrity check

## HTTP & Remote

- HTTP 429 retry [2.54+]: `http.retryAfter`, `http.maxRetries`, `http.maxRetryTime`
- Bundle URIs [2.50+] — pre-built bundles for faster clones
- Prefetching — maintenance fetches remote data hourly

## Git 3.0 Breaking Changes

- Default branch: `main` (not `master`)
- Reftable default for new repos
- SHA-256 default hash
- Symlink symrefs removed
- `core.commentChar=auto` removed
- `git whatchanged` removed (use `git log --raw`)

## Key git switch / restore [2.51+: stable]

- `git switch` — switch branches (replaces `git checkout <branch>`)
- `git restore` — restore working tree files (replaces `git checkout -- <file>`)
- Both declared no longer experimental in 2.51

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| `--force` instead of `--force-with-lease` | Use `--force-with-lease` |
| Not running `git maintenance start` | One command for faster git |
| Ignoring reflog after bad reset | `git reflog` to recover |
| Full clone of huge repos | `--filter=blob:none` or `--filter=tree:0` |
| No commit-graph | `git commit-graph write --reachable --changed-paths` |
| `git blame` without `-C` on moved code | `git blame -C` detects moves |
| Using `git checkout` for everything | `git switch` + `git restore` [2.51+] |
| Manual hook scripts | Config-based hooks [2.54+] |
| Not signing commits | SSH signing [2.34+] |
| Forgetting submodule update | `submodule.recurse true` |
| Manual `git gc` | `git maintenance run` (geometric default) |

## Sources

- Git 2.50–2.54 Release Notes: https://gitlab.com/git-scm/git/-/blob/HEAD/Documentation/RelNotes/
- GitHub Blog "Highlights from Git 2.54": https://github.blog/open-source/git/highlights-from-git-2-54/
- Edward Thomson, "You Don't Know Git", NDC London 2025: https://youtu.be/DZI0Zl-1JqQ
- "you only need 15ish git commands": https://youtu.be/y6meVhckYmQ
- "Level Up Your Git Game: 10 Little-Known Features": https://www.youtube.com/watch?v=bVnsBnnW3Tw
- "So You Think You Know Git Part 2", DevWorld 2024: https://www.youtube.com/watch?v=Md44rcw13k4
- Scott Chacon, "So You Think You Know Git", FOSDEM 2024: https://www.youtube.com/watch?v=aolI_Rz0ZqY
- "Why everyone hates git submodules": https://www.youtube.com/watch?v=JESI498HSMA
