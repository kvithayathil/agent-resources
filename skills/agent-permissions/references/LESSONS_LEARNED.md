# Agent Permissions Lessons Learned

> Self-learning log per [SELF-IMPROVEMENT.md](SELF-IMPROVEMENT.md). Add entries only
> when real task or run evidence shows a gap, a new pattern, or a gotcha. Check this
> file before composing rules and before proposing lesson updates. Promote entries
> to SKILL.md or a reference after 3+ validations across different demonstrated
> tasks. Lessons never weaken the eight hard safety gates in SKILL.md.

## Format

```
### [YYYY-MM-DD] Brief Title
- **Context**: What task/situation triggered this
- **Lesson**: What was learned
- **Validations**: N (starts at 1; count only different demonstrated tasks)
- **Evidence**: links to real task/run evidence (privacy-redacted per SELF-IMPROVEMENT.md §2)
```

---

### [2026-11-03] Config comments about layering/precedence are unverified claims
- **Context**: OpenCode-path run auditing an existing project permission config before tightening it. The config's own header comment asserted project rules load after global rules; the tool's live documentation (opencode.ai/v2/docs/permissions/, fetched 2026-11-03) confirmed the opposite — project loads first, global/agent rules append after — making the comment's claimed overrides inert and letting the user-level `shell * → ask` baseline override every shell allow in the file.
- **Lesson**: When deriving the effective policy (workflow step 2), treat a config file's inline comments about layering/precedence as claims to verify, never as facts — a confidently wrong comment can hide that an entire rule group is dead under the user's other layers. Cross-check order semantics against the tool reference/upstream docs before reasoning about overrides, and state the verified order in any corrected comment.
- **Validations**: 1
- **Evidence**: dogfood run evidence, 2026-11-03 — see `evidence/` directory of the change that captured this lesson (audit findings, approval exchange, validator exit codes)

### [2026-11-03] Zed baselines need explicit symmetric coverage of file- and path-mutation tools
- **Context**: Zed-path run authoring a first `agent.tool_permissions` baseline in a repo with no prior agent config. The reference's worked example denies secrets asymmetrically between `edit_file` (no `id_rsa`) and `write_file` (no `.netrc`/`.npmrc`), and is silent on the path-mutation tools its own tools table lists (`delete_path`, `move_path`, `copy_path`, `create_directory`) — their posture falls to the global default without the reference saying so. The user's deletion-semantics question surfaced exactly that hole.
- **Lesson**: When composing a Zed baseline, apply the full credential deny set identically to BOTH `edit_file` and `write_file` (do not copy the example's asymmetry), and decide the posture for every path-mutation tool explicitly rather than inheriting the global default silently — state that inheritance to the user when deletion semantics come up.
- **Validations**: 1
- **Evidence**: dogfood run evidence, 2026-11-03 — see `evidence/` directory of the change that captured this lesson (cross-platform gaps section)

### [2026-11-03] Permissions docs under-report adjacent protection mechanisms
- **Context**: Evaluation-loop baseline run for a Zed secrets-tightening task proposed a top-level `private_files` glob setting the skill's reference did not mention; verification against the tool's full all-settings reference confirmed the setting is real and default-active (secret-file globs), while the tool-permissions page the reference was written from never mentions it.
- **Lesson**: When authoring or tightening protection for a tool, check the tool's FULL settings reference for adjacent protection mechanisms, not only the permissions page — default-active protections can exist outside the permission system, and omitting them understates the shipped baseline and the tightening options.
- **Validations**: 1
- **Evidence**: evaluation results evidence, 2026-11-03 — see `evidence/` directory of the change that captured this lesson (unverified-claim verification and changelog entry)

### [2026-11-03] Build-tool examples biased toward JS/Rust toolchains
- **Context**: Human review of the evaluation results for an adoption rollout noted the skill's allowlist examples and eval prompts centered on npm/bun/cargo/git, while real projects build with gradle/gradlew, make, cmake, go, just and other toolchains.
- **Lesson**: When a task is "pre-approve the project's build/test commands", offer ready-to-adapt patterns for the toolchain the project actually uses — gradle/gradlew, make, cmake --build, go build/test/vet, just, npm/bun/pnpm/yarn, cargo — not just the examples' defaults. Always carry the project-controlled-code caveat and never allowlist run-arbitrary-source forms (`go run`).
- **Validations**: 1
- **Evidence**: adoption review feedback + changelog entry, 2026-11-03 — see `evidence/` directory of the change that captured this lesson (eval-results review addendum)
