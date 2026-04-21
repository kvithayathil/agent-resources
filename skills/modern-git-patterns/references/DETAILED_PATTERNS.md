# Detailed Patterns

Expanded patterns from SKILL.md. Moved here to keep main skill under 500 lines.

## Diff & Merge Patterns

### Word Diff

```bash
git diff --word-diff
git diff --word-diff-regex='[a-zA-Z_]+'
```

### Histogram Diff Algorithm

```bash
git diff --diff-algorithm=histogram
git config diff.algorithm histogram
```

Histogram fix [2.54+]: Compaction phase no longer produces visually redundant output.

### `git range-diff`

```bash
git range-diff <old-base>..<old-tip> <new-base>..<new-tip>
```

### Merge Conflict Patterns

```bash
git config --global rerere.enabled true
git merge --abort
git merge-base <branch1> <branch2>
```

## Worktree & Multi-Branch

```bash
git worktree add ../feature-branch feature
git worktree list
git worktree remove ../feature-branch
```

Best practice: Short-lived workspaces at the same level as main repo.

## Stash Patterns

```bash
git stash push --keep-index
git stash push -u           # include untracked files
git stash push -S           # include staged changes only
git config stash.index true # [2.52+] makes pop/apply behave like --index
git stash export            # [2.51+] interchange format
git stash import            # [2.51+] import stash entries
```

## Submodules & Alternatives

```bash
git clone --recursive <url>
git submodule update --init --recursive
git config --global submodule.recurse true
git config --global diff.submodule log
```

Consider alternatives when dependencies are language-specific packages, you need
monorepo-style development, or team finds submodule workflow confusing.

| Approach | Best For |
|----------|----------|
| Package managers | Language-specific dependencies |
| `git subtree` | Embedding external repos with history |
| Sparse checkout + monorepo | Large shared codebases |
| Partial clone | Large repos where you need only parts |

## Status & Comparison

### `status.compareBranches` [2.54+]

```gitconfig
[status]
    compareBranches = @{upstream} @{push}
```

Useful in triangular workflows (fetch from one remote, push to another).

### Column UI

```bash
git config --global branch.sort -committerdate
git config --global column.ui auto
git branch --column
```

## Alias & Config Patterns

### `includeIf` for Conditional Config

```gitconfig
[includeIf "gitdir:~/work/"]
    path = ~/work/.gitconfig
[includeIf "gitdir:~/oss/"]
    path = ~/.gitconfig-oss
```

### Non-ASCII Aliases [2.54+]

```gitconfig
[alias "hämta"]
    command = fetch
```

### Useful Aliases

```gitconfig
[alias]
    co = checkout
    br = branch --sort=-committerdate
    st = status --short --branch
    lg = log --oneline --graph --decorate -20
    unstage = reset HEAD --
    last = log -1 HEAD --stat
    visual = log --oneline --graph --all --decorate
    amended = commit --amend --no-edit
    wip = !git add -A && git commit -m 'WIP'
    untracked = ls-files --others --exclude-standard
    contributors = shortlog --summary --numbered
```

## Bisect & Debugging

### `git bisect`

```bash
git bisect start
git bisect bad
git bisect good <commit-or-tag>
# Test midpoint, then:
git bisect good  # if it works
git bisect bad   # if it's broken
git bisect reset
# Automated:
git bisect start HEAD <known-good>
git bisect run ./test-script.sh
```

### `git fsck`

```bash
git fsck --full
```

## HTTP & Remote Patterns

### HTTP 429 Retry [2.54+]

```gitconfig
[http]
    retryAfter = 5
    maxRetries = 3
    maxRetryTime = 60
```

### Bundle URIs [2.50+]

Optimized initial clone using pre-built bundle files.

## Config-Based Hooks vs `pre-commit` Framework

Git 2.54+ introduced config-based hooks ([git-hook docs](https://git-scm.com/docs/git-hook)),
enabling declarative hook configuration in `.git/config` or `~/.gitconfig`. The `pre-commit`
framework ([pre-commit.com](https://pre-commit.com)) is a mature Python-based hook manager.
They solve overlapping but distinct problems.

### Comparison

| Aspect | git config hooks [2.54+] | `pre-commit` framework |
|--------|--------------------------|----------------------|
| **Setup** | Edit `.git/config` or `~/.gitconfig` | `.pre-commit-config.yaml` + `pre-commit install` |
| **Language** | Any executable on PATH | Any, but ecosystem is Python-centric |
| **Shared with team** | Per-repo `.git/config` (not in VCS) or committed `.gitconfig` | `.pre-commit-config.yaml` committed to repo (standard practice) |
| **Hook management** | `git hook list`, `hook.<name>.enabled = false` | `pre-commit run`, `pre-commit autoupdate` |
| **Environment isolation** | None — uses system executables as-is | Per-hook virtualenvs (automatic for 19 languages) |
| **Dependency resolution** | Manual — you manage tool versions | Automatic — pins versions from PyPI, npm, etc. |
| **Auto-update** | No built-in mechanism | `pre-commit autoupdate` bumps to latest tags |
| **Multiple hooks/event** | Yes, config parse order | Yes, YAML order |
| **Global hooks** | Native via `~/.gitconfig` | Awkward: `pre-commit init-templatedir` |
| **Skip hooks** | Edit config or `--no-verify` | `SKIP=hook-id git commit` or `--no-verify` |
| **Partial run** | No native support | `pre-commit run <hook-id>` or `--files` |
| **CI integration** | `git hook run pre-commit` | `pre-commit run --all-files` (first-class) |
| **Wrapper support** | Custom hook events via `--allow-unknown-hook-name` | N/A |
| **Version pinning** | Not available | Per-hook `rev` in YAML |

### When to Use git Config Hooks

- **Zero dependencies**: No Python, no venvs, no `pip install`. Works on any system with git 2.54+.
- **Personal/global hooks**: Linters, formatters you always want. Defined once in `~/.gitconfig`.
- **Simple commands**: `ruff check --fix`, `shellcheck`, `just lint` — single executables on PATH.
- **CI with controlled images**: Tool versions pinned in Dockerfile, no need for `pre-commit` isolation.
- **Custom wrapper events**: Tools can define their own hook events (e.g., `mytool-validate`) per the
  git-hook WRAPPERS section.

```gitconfig
[hook "ruff"]
    event = pre-commit
    command = ruff check --fix
[hook "typecheck"]
    event = pre-commit
    command = basedpyright
[hook "spelling"]
    event = commit-msg
    command = ~/bin/spellchecker
```

### When to Use `pre-commit`

- **Team projects**: `.pre-commit-config.yaml` is committed to repo — reproducible across machines.
- **Version-pinned tools**: Each hook pins `rev` (e.g., `ruff v0.8.1`), ensuring identical behavior.
- **Rich ecosystem**: Leverage `pre-commit-hooks`, language-specific repos without local install.
- **Isolated environments**: Hooks written in Node, Ruby, Rust, Go auto-isolated in venvs — no
  system pollution. pre-commit bootstraps missing language runtimes.
- **CI/CD**: `pre-commit run --all-files` is the standard CI invocation. `pre-commit.ci` offers
  hosted autofix PRs.

```yaml
repos:
- repo: https://github.com/astral-sh/ruff-pre-commit
  rev: v0.8.1
  hooks:
  - id: ruff
    args: [--fix]
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v5.0.0
  hooks:
  - id: trailing-whitespace
  - id: end-of-file-fixer
```

### Coexistence

Config-based hooks and `pre-commit` coexist — git runs config hooks in config parse order,
then traditional `.git/hooks/` scripts (where `pre-commit install` places its runner) run last.

Recommended hybrid:
1. `pre-commit` for team-shared, version-pinned hooks (committed YAML).
2. git config hooks for personal/global tooling (in `~/.gitconfig`).
3. Both run without conflict on every commit.

### Sources

- git-hook documentation: https://git-scm.com/docs/git-hook (last updated git 2.54.0, 2026-04-20)
- git githooks documentation: https://git-scm.com/docs/githooks
- Git 2.54.0 Release Notes: https://gitlab.com/git-scm/git/-/blob/HEAD/Documentation/RelNotes/2.54.0.adoc
- pre-commit framework: https://pre-commit.com (v4.5.1)
- pre-commit GitHub: https://github.com/pre-commit/pre-commit

**Last verified**: 2026-04-21 against git 2.54.0 docs and pre-commit v4.5.1 docs.

## Deprecation Warnings (Git 3.0)

| Change | Impact |
|--------|--------|
| Default branch `main` (not `master`) | `git init` creates `main` |
| Reftable default for new repos | New ref storage format |
| SHA-256 default hash | New repos use SHA-256 by default |
| Symlink symrefs removed | Refs use files/reftable only |
| `core.commentChar=auto` deprecated | Was non-functional; being removed |
| `git whatchanged` removed | Use `git log --raw` instead |
