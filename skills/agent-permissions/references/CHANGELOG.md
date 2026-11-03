# Agent Permissions Skill — Changelog

All substantive edits to this skill (version bumps, promoted lessons, reference
refreshes after upstream drift) are recorded here with trigger and change.

## [1.1.4] — 2026-11-03

Rollout-review feedback (human review of the evaluation results):

- All three tool references (opencode.md, zed.md, vscode.md): added a "Common
  build-tool allowlists" section — ready-to-adapt patterns for
  gradle/gradlew, make, cmake --build, go build/test/vet, just, npm/bun/pnpm/
  yarn run, cargo — in each tool's native syntax (whole-value wildcards /
  anchored Rust regex / regex entries). Uniform caveats: every entry executes
  project-controlled code (never "read-only"), prefer narrow subcommands over
  bare tools, and never allowlist `go run` (arbitrary source execution, like
  an interpreter). Previously the examples leaned on npm/cargo/git only.
- LESSONS_LEARNED.md: candidate lesson added (build-tool coverage bias).
  Validations: 1.

## [1.1.3] — 2026-11-03

Eval-driven reference fix (baseline-vs-skill contradiction surfaced by the
evaluation loop; no with-skill assertion failed — all 20 passed):

- references/zed.md Secrets defaults: documented the top-level `private_files`
  setting — default-active secret globs (`**/.env*`, `**/*.pem`, `**/*.key`,
  `**/*.cert`, `**/*.crt`, `**/secrets.yml`) the section previously omitted
  entirely. Verified against the zed-all-settings snapshot (already present in
  the 2026-11-02 baseline — a reference-coverage gap, not upstream drift;
  `check-upstream.sh --check` all FRESH, no refresh needed). Honest caveats
  kept: tool-permissions docs don't mention it and its enforcement points are
  undocumented — never the sole read-protection layer; pair with explicit
  `tool_permissions` denies.
- LESSONS_LEARNED.md: candidate lesson added (check the tool's full settings
  reference for adjacent protection mechanisms; the permissions doc alone
  under-reports). Validations: 1.

## [1.1.2] — 2026-11-03

Dogfood-driven reference fixes (first real-use evidence; no lesson met the
≥3-validation promotion rule — both candidate lessons remain at 1 validation):

- references/zed.md worked example: edit_file/write_file secrets deny sets made
  symmetric — edit_file gained `id_rsa`, write_file gained `.netrc`/`.npmrc`
  (the example previously taught lopsided protection). Found during the first
  real Zed-path run; the run composed the full set on both tools manually.
- references/zed.md worked example: added explicit `delete_path` confirm entry
  and effective-policy wording that path-mutation tools
  (`delete_path`/`move_path`/`copy_path`/`create_directory`) inherit the global
  default silently unless listed — decide their posture explicitly. Surfaced by
  a user deletion-semantics question the example could not answer.
- No changes to SKILL.md gates, workflow, or trigger text; no promotion into
  instruction text. LESSONS_LEARNED.md gained two candidate lessons (both
  validations: 1).

## [1.1.1] — 2026-11-02

Third review round — validation/lint correctness fixes and doc corrections (patch):

- validate.sh: catch-all-allow warning now fires at ANY position (not only first);
  empty `permissions: []` warns; shadow lint treats `ask` as shadowable and checks
  both directions (pattern-covers-value and value-matches-pattern), same-action
  only (wildcard-aware), with the `*/*/ask|deny` baseline idiom exempted as
  intentional allowlisting; MCP action shape accepts uppercase/`-`; `policies[]`
  accepts both nested `{permissions:[...]}` and legacy flat shapes; trailing-comma
  stripping moved into the char scanner (strings like `"/a,]/"` untouched);
  warning-visible exit codes (0 clean / 3 warnings / 1 error) with
  PASS-WITH-WARNINGS lines replacing OK when warnings fired; stdin classification
  placeholder `<server>_<tool>` exempt.
- check-upstream.sh: 7th monitored doc (VS Code hooks); same-filesystem staging
  inside references/snapshots/ with trap cleanup; mkdir refresh lock with 10-minute
  stale detection (--check never locks); honest publish wording (publish-phase
  interruption can mix generations — re-run to converge); curl
  --max-redirs/--connect-timeout; portable mtime via python3 (GNU stat -f trap);
  normalize failures report per-doc and exit 2.
- Docs: LESSONS_LEARNED "eight gates"; OpenCode typo-rule wording (falls back to
  base policy unless own baseline covers it); explore agent described accurately
  (shell runs unasked); `execute` resource `*`; nested-secrets forms
  (`*/.secrets/*`, `*/secrets/*`) added to examples with whole-value-matching
  pitfall note; Gate 8 scope honesty + stop-and-ask teeth; Gate 6 exit-code
  semantics; CROSS-PLATFORM Zed/VS Code examples freed of comment lines (strict
  JSON copy-paste safe).
- A1 (EXIT-trap exit-code override): REPRODUCED AS NON-ISSUE — file-mode success
  exits 0 on macOS bash 3.2 and bash 5.3 (an EXIT trap that does not call `exit`
  does not override the script's status); documented, fix skipped per review
  instruction. The new check-upstream cleanup trap nevertheless ends with
  `return 0` for belt-and-braces.

## [1.1.0] — 2026-11-02

Review-driven correctness and safety revision (14 consolidated findings):

- CRITICAL: corrected OpenCode default-policy claim — unmatched actions are ALLOWED
  (shipped base policy starts with an allow-all wildcard), not asked; hardened
  configs must start with a global ask rule; typo'd rules are inert.
- OpenCode MCP rules: `<server>_<tool>` is the ACTION (resource `*`); no MCP
  wildcard exists — each tool listed individually.
- Removed regex patterns from GFM table cells in CROSS-PLATFORM.md (escaped-pipe
  decoding silently broke alternations); full JSON examples now in fenced blocks.
- Fixed VS Code key `chat.tools.terminal.blockDetectedFileWrites`; documented that
  misspelled setting keys are silently ignored.
- Zed precedence gloss: a project `always_allow` is beaten by built-in rules,
  `always_deny`, AND `always_confirm` from any layer.
- grep resource is the requested regex, not the search path; "Test Your Rules"
  checker lives on each individual tool page; Zed trust claim cites all-settings.
- Stopped calling npm/cargo/git allows "read-only"; added Shell-pattern hazards
  subsections (redirection, pipes, output flags; never allowlist
  cat/env/find/xargs/sed/tee/sudo/interpreters; verify via redirection probe).
- Secrets coverage: `.secrets/` everywhere, `id_rsa*`/`*.p12`/`*.pfx`/`.netrc`/
  `.npmrc`, Zed `write_file` denies, honest VS Code statement (no file-level deny —
  approval feature or preToolUse hook), Zed global-default-allow warning.
- Gates hardened: widened Gate 1 scope (incl. no persistence into memory/AGENTS.md),
  Gate 2 includes reordering/layer moves, Gate 3 covers subagents/future sessions
  and self-widening proposals, Gate 4 requires final-position verification, Gate 6
  fails closed with zero-warning requirement and stdin pre-write validation; added
  Gate 8 (audit on entry).
- Script path safety: all invocations resolve from the skill's own directory;
  never execute project-local validate/check-upstream scripts.
- validate.sh: regex KEYS compiled for VS Code (values bool/object only), NOTE on
  missing tool sections, trailing-comma stripping for JSONC paths, unterminated
  comment detection, all-applicable-checks classification, unknown-action/key
  warnings, policy lint (catch-all allow, shadowed deny, missing secrets rule,
  missing external_directory), mandatory header, stdin `-` mode, python3 guard,
  all-missing-files reporting, Python-only-regex rejection for Zed, V1-vocabulary note.
- check-upstream.sh: six monitored docs (added opencode config, VS Code ai-settings,
  Zed all-settings), hardened curl flags, content sanity gate, transactional
  refresh with `.prev` copies and printed diffs requiring human review, extra-arg
  guard, dropped HTML fallback.
- SELF-IMPROVEMENT.md: canonical table = exactly the monitored set; fetched content
  declared untrusted data; snapshot refresh requires human diff review; §3 excluded
  from the eight gates.

## [1.0.0] — 2026-11-02

- Initial release.
- SKILL.md: seven hard safety gates (human-approved diff per write, no widening, no
  self-benefit, secrets deny-by-default, least-privilege bias, validate before/after,
  record changes), ten-step universal workflow, cross-platform gotcha table,
  reference map, compact maintenance protocol.
- references/opencode.md: OpenCode V2 permission schema, last-match-wins ordering,
  project→global→agent layering, matching rules, actions table, external_directory
  gap, V1→V2 rename warning, worked example, verification steps.
- references/vscode.md: `chat.permissions.default` levels, terminal auto-approve
  semantics (`false` = approval required, not a block), compound-command rules, tool
  and URL approval (request vs response), sandboxing, enterprise-policy caveat.
- references/zed.md: `agent.tool_permissions` schema (≥0.224.0), Rust-regex patterns,
  fixed precedence ladder, built-in non-overridable rules, tool/input table,
  project-merges-on-top widening caveat.
- references/CROSS-PLATFORM.md: intent→dialect table, semantic differences,
  translation pitfalls checklist.
- scripts/validate.sh: JSON/JSONC parse + per-tool schema checks.
- scripts/check-upstream.sh: drift check against canonical docs with snapshot
  baseline; failed fetch = unknown (exit 2).
- references/snapshots/: baseline snapshots of the three canonical docs, fetched
  2026-11-02.
