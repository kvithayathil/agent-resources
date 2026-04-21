# Version Feature Map

Features available by git version. Check `git --version` before using.

## Git 2.50

| Feature | Command/Config |
|---------|---------------|
| Incremental multi-pack index | `git multi-pack-index` |
| Reflog batch expire | `git maintenance` task |
| Machine-parsable rev-list | `git rev-list --format=nul` |
| Best-effort batch ref updates | internal |
| Bundle-URI optimized clone | server-side |
| `.ini` userdiff driver | automatic |

## Git 2.51

| Feature | Command/Config |
|---------|---------------|
| Stash import/export | `git stash export/import` |
| `--compact-summary` for merge/pull | `git merge --compact-summary` |
| Reftable backend maturation | Git 3.0 default announced |
| `git switch`/`git restore` stable | no longer experimental |
| `git for-each-ref --start-after` | pagination support |
| Lift changed-path filter for multi-path | `git log` with multiple paths |
| `netrc` credential helper improvements | textual service names |

## Git 2.52

| Feature | Command/Config |
|---------|---------------|
| `git last-modified` | new command |
| `git refs list` | front-end for `for-each-ref` |
| `git repo` | new subcommand family |
| `git repo structure` | inspect repo characteristics |
| `git maintenance` geometric strategy | `maintenance.strategy = geometric` |
| Sparse-checkout clean | `git sparse-checkout clean` |
| Sparse index | `index.sparse = true` |
| `commitGraph.changedPaths` config | default changed-paths |
| `core.commentChar=auto` deprecated | will be removed |
| Git 3.0: `main` default branch | announced |
| `stash.index` config | `stash pop/apply` with `--index` behavior |
| `--signed-commits` for fast-import | `git fast-import --signed-commits` |
| Optional path config values | `:(optional)` prefix |

## Git 2.53

| Feature | Command/Config |
|---------|---------------|
| `git maintenance is-needed` | check if maintenance needed |
| `git replay` ref updates | atomic by default |
| `git blame --diff-algorithm` | choose diff algo for blame |
| `git repo info --all` | show all repo info |
| Incomplete-line whitespace error | new error class |
| Data model manual | `git help gitformat` |

## Git 2.54

| Feature | Command/Config |
|---------|---------------|
| `git history` (experimental) | `git history reword/split` |
| Config-based hooks | `hook.<name>.event/command` |
| Geometric repack default | `git maintenance run` default strategy |
| `git add -p` hunk status display | shows accepted/skipped state |
| `git add -p --no-auto-advance` | stay on file after all hunks decided |
| `git replay --revert` | revert mode for replay |
| `git replay` drop empty commits | automatic during replay |
| `git rebase --trailer` | add trailers during rebase |
| `git status` compare branches | `status.compareBranches` config |
| Non-ASCII aliases | `[alias "hämta"]` syntax |
| HTTP 429 retry | `http.retryAfter`, `http.maxRetries` |
| `git log -L` with pickaxe | compatible with `-S`, `-G` |
| Expired GPG key = good signature | correct display |
| Histogram diff quality fix | better compaction phase |
| `git backfill` with pathspec/range | scoped blob download |
| `git rev-list --maximal-only` | show only non-reachable commits |
| `git config list` official | replaces `git config -l` |
| `git hook list` | show configured hooks |
| `git repo info --keys` | list known info keys |
| `git history split` | interactive commit splitting |
| Reference-transaction hook pre-lock | `preparing` phase trigger |
| `git apply` improved error messages | file name + line number |
| `git format-patch --commit-list-format` | simpler cover letter format |
