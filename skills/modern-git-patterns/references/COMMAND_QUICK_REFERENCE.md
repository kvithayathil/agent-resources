# Command Quick Reference

One-liner commands for common modern git operations. Assumes git 2.54+.

## Daily Workflow

```bash
git switch -c feature/branch        # create and switch to new branch
git switch -                         # switch back to previous branch
git restore --staged <file>          # unstage file
git restore <file>                   # discard working tree changes
git add -p <file>                    # interactive staging
git commit -v                        # commit with diff shown in editor
git push -u origin HEAD              # push and set upstream
```

## Safety

```bash
git push --force-with-lease          # safe force push
git reflog --date=relative           # see what you did recently
git reset --soft HEAD~1              # undo last commit, keep changes staged
git reset --mixed HEAD~1             # undo last commit, keep changes unstaged
git stash push -u -m "description"   # stash everything including untracked
```

## Investigation

```bash
git blame -C -w -L :func file.c      # blame function, detect moves, ignore ws
git log -L :func:file.c              # trace function history
git log -S "search_term" --oneline   # find commits adding/removing string
git log --all --oneline --graph      # visual branch overview
git log --follow -p -- path          # follow file renames with patch
git last-modified <path>             # [2.52+] last commit touching path
git range-diff A..B C..D            # compare two versions of a branch
```

## Large Repo Performance

```bash
git maintenance start                # one-time: set up background maintenance
git commit-graph write --reachable --changed-paths
git config core.fsmonitor true
git config core.untrackedCache true
git sparse-checkout init --cone
git sparse-checkout set dir1 dir2
```

## History Rewriting

```bash
git history reword HEAD~3            # [2.54+] reword a commit
git history split HEAD~2             # [2.54+] split a commit
git rebase -i --autostash HEAD~5     # interactive rebase with autostash
git commit --amend --no-edit         # amend without changing message
```

## Config

```bash
git config --global user.signingKey ~/.ssh/id_ed25519.pub
git config --global gpg.format ssh
git config --global commit.gpgSign true
git config --global rerere.enabled true
git config --global push.autoSetupRemote true
git config --global init.defaultBranch main
git config --global core.fsmonitor true
git config --global branch.sort -committerdate
git config --global column.ui auto
```

## Cleanup

```bash
git maintenance run                  # [2.54+] geometric repack by default
git gc --aggressive                  # traditional full GC (use maintenance instead)
git reflog expire --expire=now --all
git gc --prune=now
```
