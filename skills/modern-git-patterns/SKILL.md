---
name: modern-git-patterns
description: >
  Use when working with git commands, planning git workflows, advising on git best practices,
  or needing version-aware git guidance. Provides modern patterns, commands, and approaches
  for git 2.50+. Covers history rewriting, maintenance, sparse operations, config-based hooks,
  signing, blame techniques, partial clone, and workflow patterns. Triggers on: git, rebase,
  merge, branch, commit, blame, diff, bisect, worktree, stash, submodule, hook, maintenance,
  sparse-checkout, partial clone, signing, force push, reflog, cherry-pick.
tags:
  - git
  - version-control
  - patterns
  - workflow
  - devops
license: Apache-2.0
metadata:
  author: kvithayathil
  version: "1.0.0"
  living: "true"
  self-learning: "true"
  self-updating: "true"
  update-policy: "evolve-on-evidence"
  last-reviewed: "2026-04-21"
  min-git-version: "2.50.0"
  verified-git-version: "2.54.0"
---

# Modern Git Patterns, Commands & Approaches

Version-aware git guidance grounded in evidence from git 2.50–2.54 release notes,
expert talks, and real-world practice.

## Version Detection

Before advising on any git command, check the available version:

```bash
git --version
```

If version < 2.50, note that many patterns below are unavailable or behave differently.
Feature availability annotations use `[2.XX+]` to indicate minimum git version.

## Section Index

| Section | Focus |
|---------|-------|
| [History Rewriting](#history-rewriting) | reword, split, replay, rebase |
| [Safety Patterns](#safety-patterns) | force-with-lease, reflog, rerere |
| [Maintenance & Performance](#maintenance--performance) | geometric repack, commit-graph, fsmonitor |
| [Sparse & Partial Operations](#sparse--partial-operations) | sparse-checkout, partial clone, backfill |
| [Config-Based Hooks](#config-based-hooks) | declarative hooks in gitconfig |
| [Signing & Verification](#signing--verification) | SSH signing, expired key handling |
| [Blame & History Investigation](#blame--history-investigation) | blame -C, -L, --diff-algorithm, log -L |
| [Diff & Merge Patterns](#diff--merge-patterns) | word-diff, histogram, rerere, merge-conflict recording |
| [Worktree & Multi-Branch](#worktree--multi-branch) | worktree, virtual branches |
| [Stash Patterns](#stash-patterns) | stash --index, import/export |
| [Submodules & Alternatives](#submodules--alternatives) | submodule, subtree, package managers |
| [Status & Comparison](#status--comparison) | status.compareBranches, column UI |
| [Alias & Config Patterns](#alias--config-patterns) | includeIf, non-ASCII aliases, column.ui |
| [Bisect & Debugging](#bisect--debugging) | binary search for regressions |
| [HTTP & Remote Patterns](#http--remote-patterns) | 429 retry, prefetch, bundle URIs |
| [Deprecation Warnings (Git 3.0)](#deprecation-warnings-git-30) | upcoming breaking changes |

---

## History Rewriting

### `git history` (experimental) [2.54+]

Targeted history rewriting without the complexity of interactive rebase.

**Reword a commit message** without touching working tree or index:

```bash
git history reword <commit>
```

**Split a commit** into two by selecting hunks (uses `add -p` style interface):

```bash
git history split <commit>
```

Limitations: No merge commit support. Refuses operations that would cause conflicts.
Works in bare repositories. Built on `git replay` machinery.

### `git replay` (experimental) [2.53+]

Replay commits onto a new base without touching working tree. Safer than rebase for
scripting.

```bash
# Replay range onto new base
git replay --onto <new-base> <upstream>..<branch>

# Revert mode [2.54+]
git replay --revert <upstream>..<branch>

# Now performs atomic ref updates by default [2.53+]
# (instead of printing update-ref commands to stdout)

# Drop commits that become empty during replay [2.54+]
```

Can replay down to root commit [2.54+].

### `git rebase` with trailers [2.54+]

```bash
git rebase --trailer "Reviewed-by: A U Thor <author@example.com>"
```

Appends a trailer to every rebased commit via `interpret-trailers` machinery.

---

## Safety Patterns

### `--force-with-lease`

**Always prefer** `--force-with-lease` over `--force`. Checks that remote ref hasn't
changed since your last fetch before force-pushing.

```bash
git push --force-with-lease
```

If someone else pushed to the same branch, the push is rejected. Much safer than
blind `--force`. Works by comparing your local remote-tracking ref with the actual
remote ref.

### Reflog: Your Safety Net

Reflog records every HEAD movement (commit, checkout, merge, reset, rebase).
Entirely local — not shared with remotes.

```bash
# View reflog with dates
git reflog --date=relative

# Pretty format
git reflog --pretty=format:'%h %gd %gs %ci'

# Recover a "lost" commit
git checkout <reflog-hash>
# or create a branch from it
git branch recovered-work <reflog-hash>
```

### `git rerere` (Reuse Recorded Resolution)

Records how you resolved merge conflicts. When the same conflict appears again,
automatically applies the previous resolution.

```bash
git config --global rerere.enabled true
```

Especially valuable when rebasing long-running feature branches repeatedly.

---

## Maintenance & Performance

### `git maintenance` [2.50+, geometric default 2.54+]

Automated repository maintenance. **Geometric strategy** is now default [2.54+].

```bash
# One-time setup: registers cron jobs for hourly/daily/weekly maintenance
git maintenance start

# Check if maintenance is needed [2.53+]
git maintenance is-needed

# Manual run (uses geometric strategy by default in 2.54+)
git maintenance run
```

What it does (hourly):
- Incremental repacking (geometric strategy — avoids full GC)
- Commit graph generation
- Loose object collection
- Prefetching remote refs

What it does (daily):
- More aggressive repacking

### Commit Graph

Dramatically speeds up `git log`, `git branch --contains`, and other traversal-heavy
operations by pre-computing a reachability graph.

```bash
# Write commit graph
git commit-graph write --reachable --changed-paths

# Enabled by default in maintenance [2.52+]
# commitGraph.changedPaths config [2.52+]
```

### `core.fsmonitor` [2.50+]

Uses OS file system watcher instead of scanning every file. Critical for large repos.

```bash
git config core.fsmonitor true
git config core.untrackedCache true
```

Reduces `git status` from seconds to milliseconds on repos with 100K+ files.

### Multi-Pack Indexes & Geometric Repacking

```bash
# Write multi-pack index
git multi-pack-index write

# Geometric repack (now default in maintenance) [2.54+]
# Combines packs incrementally to form geometric progression by object count
# Avoids expensive all-into-one repacks
```

Incremental MIDX with compaction support [2.54+].

### Prefetching [2.50+]

Maintenance prefetches remote refs hourly in background. Makes subsequent
`git fetch` nearly instant since data is already local.

---

## Sparse & Partial Operations

### Sparse Checkout

Work with only a subset of files in a monorepo.

```bash
# Clone with no files checked out
git clone --filter=blob:none --sparse <url>
cd repo

# Initialize sparse checkout
git sparse-checkout init --cone

# Add directories to working tree
git sparse-checkout set src/core src/utils

# Clean untracked files outside sparse paths [2.52+]
git sparse-checkout clean

# Sparse index for even better performance [2.52+]
git config index.sparse true
```

Use `--cone` mode for best performance. Pattern mode is slower.

### Partial Clone

Clone without blob data. Downloads blobs on demand.

```bash
# Filter blobs entirely
git clone --filter=blob:none <url>

# Filter blobs larger than 1MB
git clone --filter=blob:limit=1m

# Filter trees (no directory structure) [2.50+]
git clone --filter=tree:0 <url>
```

### `git backfill` (experimental) [2.54+]

Download missing blobs in a partial clone, scoped to specific paths or ranges.

```bash
# Backfill specific paths
git backfill -- '*.c'

# Backfill specific range
git backfill main~100..main
```

---

## Config-Based Hooks [2.54+]

Define hooks in gitconfig instead of scripts in `.git/hooks/`. Supports multiple
hooks per event, centralized configuration, and per-repository overrides.

```gitconfig
[hook "linter"]
    event = pre-commit
    command = ~/bin/linter --cpp20

[hook "no-leaks"]
    event = pre-commit
    command = ~/bin/leak-detector

# Disable a hook without removing it
[hook "linter"]
    enabled = false
```

```bash
# List configured hooks
git hook list pre-commit
# Output:
# global    linter    ~/bin/linter --cpp20
# local     no-leaks  ~/bin/leak-detector
```

Traditional hooks in `$GIT_DIR/hooks` still work and run last. Config-based hooks
can be defined in `~/.gitconfig` (global), `/etc/gitconfig` (system), or per-repo config.

---

## Signing & Verification

### SSH Signing (no GPG required) [2.34+]

Sign commits with SSH keys instead of GPG. Many developers already have SSH keys.

```gitconfig
[user]
    signingKey = ~/.ssh/id_ed25519.pub
[gpg]
    format = ssh
[commit]
    gpgSign = true
```

Upload SSH public key to GitHub/GitLab for verification. GitHub shows "Verified" badge.

### Expired Key Handling [2.54+]

Signatures made with since-expired GPG keys are now correctly shown as **good signatures**
(not alarming red). A signature remains valid even after the signing key expires.

### Signed Pushes

```bash
git config receive.certNonceseed <secret>
```

Servers can verify that pushes were made by authorized users.

---

## Blame & History Investigation

### `git blame` Advanced Options

```bash
git blame -C <file>                        # detect code movement from other files
git blame -C -C <file>                     # detect code copied from other files
git blame -w <file>                        # ignore whitespace changes
git blame -L 100,150 <file>                # blame specific line range
git blame -L :function_name <file>         # blame a function by name
git blame --diff-algorithm=histogram <file> # [2.53+] choose diff algo for blame
```

`--diff-algorithm` can produce meaningfully different blame output. `histogram` often
produces better results for refactored code.

### `git log -L` (Line-Level History) [2.54+ enhanced]

```bash
git log -L :function_name:file.c           # trace a function's history
git log -L :func:file.c -S term --oneline  # [2.54+] now compatible with pickaxe
```

Previously, `-S`, `-G`, `--word-diff`, and `--color-moved` were silently ignored with `-L`.

### `git log` Pickaxe

```bash
git log -S "string" --oneline              # find commits adding/removing a string
git log -G "pattern" --oneline             # find commits matching regex in diff
git log -S "term" -- path/to/file          # filter by file
```

### Other Investigation Tools

- **`git last-modified`** [2.52+]: Closest ancestor commit that touched each path
- **`git rev-list --maximal-only`** [2.54+]: Only commits not reachable by others

---

## Diff & Merge Patterns

- **Word diff**: `git diff --word-diff` for word-level differences
- **Histogram algorithm**: `git diff --diff-algorithm=histogram` (often cleaner; fix in 2.54+)
- **range-diff**: `git range-diff A..B C..D` to compare two versions of a branch
- **rerere**: `git config rerere.enabled true` to record and reuse merge conflict resolutions

## Worktree & Multi-Branch

```bash
git worktree add ../feature-branch feature   # work on multiple branches simultaneously
git worktree list
git worktree remove ../feature-branch        # clean up when done
```

### Bare Repo + Worktree Gotchas

When using a bare repo as shared root with worktrees, two pitfalls require manual fixes:

1. **Worktrees inherit `core.bare=true`** — every git operation fails until you set
   `git config --worktree core.bare false` per worktree. Requires `extensions.worktreeconfig=true`.
   ([git-worktree CONFIGURATION FILE](https://git-scm.com/docs/git-worktree#_configuration_file),
   [git-config extensions.worktreeConfig](https://git-scm.com/docs/git-config#Documentation/git-config.txt-extensionseasierworktreeConfig))

2. **Config-based hooks run from `$GIT_DIR`** (bare repo, no working tree) — path-relative
   commands fail. Use `pre-commit` framework for project hooks instead.
   ([githooks(5)](https://git-scm.com/docs/githooks#_description),
   [DETAILED_PATTERNS — Bare Repo + Worktree Architecture](references/DETAILED_PATTERNS.md))

See [references/DETAILED_PATTERNS.md](references/DETAILED_PATTERNS.md) for full setup walkthrough.

## Stash Patterns

```bash
git stash push -u -m "description"           # stash including untracked
git config stash.index true                   # [2.52+] preserve index on pop
git stash export / git stash import           # [2.51+] interchange format
```

## Submodules & Alternatives

```bash
git clone --recursive <url>                   # clone with submodules
git config --global submodule.recurse true    # auto-update on branch switch
```

Prefer package managers (npm/pip/cargo), `git subtree`, or sparse checkout when possible.

## Status, Alias & Config

- **status.compareBranches** [2.54+]: Compare against `@{upstream}` and `@{push}` simultaneously
- **column.ui auto**: Display branch lists in columns; `branch.sort -committerdate`
- **includeIf**: Conditional config per directory (`[includeIf "gitdir:~/work/"]`)
- **Non-ASCII aliases** [2.54+]: `[alias "hämta"] command = fetch`

## Bisect & Debugging

```bash
git bisect start && git bisect bad && git bisect good <known-good>
git bisect run ./test-script.sh               # automated binary search
git fsck --full                               # repository integrity check
```

## HTTP & Remote Patterns

- **HTTP 429 retry** [2.54+]: `http.retryAfter`, `http.maxRetries` — handles rate limiting
- **Bundle URIs** [2.50+]: Pre-built bundles for faster initial clones
- **Prefetching**: Maintenance fetches remote data hourly in background

## Deprecation Warnings (Git 3.0)

Default branch → `main`, reftable default, SHA-256 default, symlink symrefs removed,
`core.commentChar=auto` removed, `git whatchanged` removed.

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Using `--force` instead of `--force-with-lease` | Use `--force-with-lease` for safe force pushes |
| Not running `git maintenance start` | One command gives hours of faster git operations |
| Ignoring reflog after bad reset | `git reflog` to find and recover lost commits |
| Full clone of enormous repos | Use `--filter=blob:none` or `--filter=tree:0` |
| Not setting up commit-graph | `git commit-graph write --reachable --changed-paths` |
| Blaming without `-C` for moved code | `git blame -C` detects code movement across files |
| Using `git checkout` for everything | `git switch` (branches) and `git restore` (files) [2.51+: no longer experimental] |
| Editing `.git/hooks/` scripts manually | Use config-based hooks [2.54+] |
| Not signing commits | Use SSH signing (easier than GPG) [2.34+] |
| Forgetting `git submodule update` | Set `submodule.recurse true` |
| Running `git gc` manually | Use `git maintenance run` instead (geometric by default) |

## Gotchas

- `git blame -C` is expensive on large repos but essential for accurate attribution of moved code.
- Partial clone with `--filter=blob:none` still downloads all commits and trees. Use `--filter=tree:0`
  to skip trees too, but some operations will require fetching missing data.
- `git maintenance start` adds cron jobs. On macOS, this uses `launchd`. On Linux, `cron` or `systemd` timers.
- Config-based hooks [2.54+] run in config file order. Traditional hook scripts run last.
- `git switch` and `git restore` were declared no longer experimental in 2.51. Prefer them over
  the overloaded `git checkout`.
- Expired GPG keys still produce valid signatures. Git 2.54 correctly shows these as good, not invalid.
- `git log -L` now works with `-S` and `-G` (pickaxe) as of 2.54. Before that, these options were silently ignored.
- Worktrees created from bare repos inherit `core.bare=true` — must manually set `core.bare false` per worktree. ([git-worktree docs](https://git-scm.com/docs/git-worktree#_configuration_file))
- Config-based hooks [2.54+] run from `$GIT_DIR` in bare repos, not the worktree root. Path-relative commands fail. Use `pre-commit` framework for project hooks. ([githooks docs](https://git-scm.com/docs/githooks#_description))
- `git clone --bare` doesn't create `remote.origin.fetch` refspec. Run `git config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"` after clone. ([git-clone --bare docs](https://git-scm.com/docs/git-clone#Documentation/git-clone.txt---bare))
- `git check-ignore` skips files in the index (staged). Use `--no-index` for pre-commit hooks that validate staged files. Also avoids symlink resolution errors in worktrees. ([git-check-ignore docs](https://git-scm.com/docs/git-check-ignore#_description))

## References

- [references/VERSION_FEATURE_MAP.md](references/VERSION_FEATURE_MAP.md) — Feature availability by git version
- [references/DETAILED_PATTERNS.md](references/DETAILED_PATTERNS.md) — Expanded patterns for diff, merge, worktree, stash, submodules, aliases, bisect, HTTP
- [references/COMMAND_QUICK_REFERENCE.md](references/COMMAND_QUICK_REFERENCE.md) — One-liner command reference
- [references/SOURCES.md](references/SOURCES.md) — Full source bibliography
- [references/LESSONS_LEARNED.md](references/LESSONS_LEARNED.md) — Evolving log of patterns from real-world use
- [references/CHANGELOG.md](references/CHANGELOG.md) — History of skill updates
