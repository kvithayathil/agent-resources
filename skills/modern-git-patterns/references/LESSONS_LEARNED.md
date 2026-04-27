# Lessons Learned

Evolving log of patterns and anti-patterns discovered during real-world use.
Agent: append new entries here with date and context. Promote to SKILL.md after
3+ validations.

## Template

```
### [YYYY-MM-DD] Brief Title
- **Context**: What task/situation prompted this
- **Discovery**: What was learned
- **Evidence**: How it was verified
```

## Entries

### [2026-04-26] Config-based hooks fail in bare+worktree repos
- **Context**: Migrated votecatcher from standard repo to bare+worktree. Tried git 2.54 config-based hooks (`hook.<name>.event = pre-commit`, `hook.<name>.command = "cd backend && ruff check --fix"`).
- **Discovery**: Config-based hooks execute from bare repo common directory (no working tree). Path-relative commands like `cd backend && ruff check` fail because the bare repo has no `backend/` directory. Pre-commit framework correctly resolves worktree working directory.
- **Evidence**: Hand-tested config-based hooks from bare repo — all path-relative commands failed. Reverted to pre-commit framework.
- **Docs**: [githooks(5)](https://git-scm.com/docs/githooks#_description) — *"Before Git invokes a hook, it changes its working directory to either $GIT_DIR in a bare repository or the root of the working tree in a non-bare repository."*
- **Implication**: Config-based hooks work for global/personal hooks with absolute paths, but not for project hooks requiring worktree-relative paths in bare+worktree setups.

### [2026-04-26] Worktrees from bare repos inherit core.bare=true
- **Context**: `git worktree add main/ main` from a bare repo.
- **Discovery**: New worktrees inherit `core.bare=true` from the bare repo config. Every git operation in the worktree fails with "fatal: this operation must be run in a work tree". Must explicitly set `git config --worktree core.bare false` per worktree.
- **Evidence**: `git status` in new worktree immediately after creation — failed. Required `extensions.worktreeconfig=true` plus explicit per-worktree override.
- **Docs**: [git-worktree CONFIGURATION FILE](https://git-scm.com/docs/git-worktree#_configuration_file) — *"If the config variables core.bare or core.worktree are present in the common config file... they will be applied to the main worktree only."* [git-config extensions.worktreeConfig](https://git-scm.com/docs/git-config#Documentation/git-config.txt-extensionseasierworktreeConfig) — *"If core.bare is true, then it must be moved from $GIT_COMMON_DIR/config to $GIT_COMMON_DIR/config.worktree."*
- **Implication**: `git worktree add` should handle this but doesn't (at least through 2.54.0).

### [2026-04-26] git clone --bare drops fetch refspecs
- **Context**: `git clone --bare` to create bare repo from existing repo.
- **Discovery**: Bare clone doesn't set `remote.origin.fetch` refspec. `git fetch` creates no remote tracking branches until refspec is manually added: `git config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"`.
- **Evidence**: `git branch -r` returned empty after clone+fetch until refspec was configured.
- **Docs**: [git-clone --bare](https://git-scm.com/docs/git-clone#Documentation/git-clone.txt---bare) — *"When this option is used, neither remote-tracking branches nor the related configuration variables are created."*

### [2026-04-26] git check-ignore skips staged files without --no-index
- **Context**: Pre-commit hook using `git check-ignore` to block internal directories from being committed.
- **Discovery**: `git check-ignore` skips files already in the index (staged). The hook's purpose is to check staged files, so it was a silent no-op. Fix: `git check-ignore --no-index` matches purely on path patterns without index lookup.
- **Evidence**: Hook passed despite blocked files being staged. After adding `--no-index`, files were correctly rejected.
- **Docs**: [git-check-ignore DESCRIPTION](https://git-scm.com/docs/git-check-ignore#_description) — *"By default, tracked files are not shown at all since they are not subject to exclude rules; but see --no-index."*
- **Bonus**: `--no-index` also avoids symlink resolution errors for symlinked dirs in worktrees (`.agents/`, `.crosslink/` etc.).
