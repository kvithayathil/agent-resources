# AAID (Augmented AI Development) skill

Attribution and rights record for this skill. This file is the authority referenced by
the `license` field of `SKILL.md` frontmatter.

## Upstream

- **Title**: AAID (Augmented AI Development) skill (this file's subject; local skill name `aaid`)
- **Upstream repository**: https://github.com/dawid-dahl-umain/augmented-ai-development
- **Source paths consumed** (12 paths): see `openspec/changes/add-aaid-skill/evidence/source-manifest.md`
  — guide `docs/aidd-workflow.md`, rules `rules/aaid/aaid-development-rules.mdc`,
  `aaid-workflow-diagram.mermaid`, appendices A/B/D/E, the two plugin SKILL.md entrypoints,
  `plugins/aaid-tdd/.claude-plugin/plugin.json`, `plugins/aaid-bdd/.claude-plugin/plugin.json`,
  and `.claude-plugin/marketplace.json`.
- **Pinned commit**: `54b4e5f0600f0d49131b74ffcb686876582ee20c` (tree
  `b0da7f19f18fb012df34ba43611a99482dbbc7ef`), fingerprint-verified against the complete
  repo tree (`truncated: false`).

## Upstream license declaration (verbatim, from the manifests)

The manifests file `plugins/aaid-tdd/.claude-plugin/plugin.json` (identically the
`plugins/aaid-bdd/.claude-plugin/plugin.json` manifest and the
`.claude-plugin/marketplace.json` entries) declare:

```json
{
  "name": "aaid-tdd",
  ...
  "author": {
    "name": "Dawid Dahl"
  },
  "repository": "https://github.com/dawid-dahl-umain/augmented-ai-development",
  "license": "MIT"
}
```

Marketplace declaration excerpt (`.claude-plugin/marketplace.json`): root owner
`"name": "Dawid Dahl"`, and for plugins aaid-tdd (1.1.2), aaid-bdd (1.0.7), implan
(1.4.1), testing (1.1.3), code-quality (1.2.0), each carries
`"license": "MIT"` with author Dawid Dahl.

Recorded verbatim above with filenames as source; treat as the upstream's own
self-declaration (see its limits immediately below).

## No LICENSE file exists upstream

**Explicit statement:** the upstream repository ships **no LICENSE file anywhere** —
verified against the complete repository tree at pinned commit
`54b4e5f0600f0d49131b74ffcb686876582ee20c` on 2026-10-24 (recursive tree scan,
`truncated: false`). The manifest `license: MIT` string is therefore **not an
authoritative copyright or permission notice**: it is an unverified metadata
declaration.

That declaration was accepted as the attribution basis **by explicit USER DECISION
2026-10-23 (recorded in design.md D7)**, with the risk of proceeding without an
authoritative notice explicitly accepted. No maintainer contact was made, and none is
required under the recorded decision. **No copyright years or holders are invented
here** — the only holder named is the author the upstream itself declares (Dawid Dahl)
and third parties the upstream text itself credits (below).

## Third-party credits found in the upstream text (verified against local pinned copies)

Citations are file + line in the committed snapshot at `assets/upstream/`; quote
forms taken directly from those files:

- `docs/aidd-workflow.md:425` — "Test Ordering with ZOMBIES: Whichever approach you
  choose, order your tests following **James Grenning's ZOMBIES heuristic**." Also
  `docs/aidd-workflow.md:1257` and
  `rules/aaid/aaid-development-rules.mdc:195` — "Order tests following the ZOMBIES
  progression (James Grenning)."
- `appendices/appendix-a/docs/aaid-acceptance-testing-workflow.md:756` —
  "Credit goes to **Dave Farley** for creating the original **Params and DslContext**
  implementations."
- `appendices/appendix-a/docs/aaid-acceptance-testing-workflow.md:55` — "This guide
  combines **Dave Farley's Four-Layer Model** for acceptance testing…" and
  `appendices/appendix-e/dependencies-and-mocking.md:177` — "`AAID` structures these
  tests using **Dave Farley's Four-Layer Model** (Executable Specs, DSL, Protocol
  Drivers, SUT)."
- `docs/aidd-workflow.md:94-105` — "Built on Proven Foundations" list crediting Kent
  Beck (TDD cycles), Dave Farley (Continuous Delivery and four-layer acceptance
  testing), Robert C. Martin (Three Laws of TDD), Daniel Terhorst-North (BDD),
  Gojko Adzic (Specification by Example), Aslak Hellesøy (BDD/Gherkin), Eric Evans
  (DDD and Ubiquitous Language), and Martin Fowler (refactoring, evolutionary design,
  DSLs).

## Local additions vs upstream-derived content

- **Local additions** (original to this hub; not derived from the upstream): the
  human-gated hard-gate/stop wording as adapted, the conversational state summary, the
  maintenance/freshness/self-improvement protocols, LESSONS_LEARNED/CHANGELOG/SOURCE/
  ATTRIBUTION files, route determination, and the Quality System's own formatting and
  edge-classification guidance.
- **Upstream-derived** (adapted from the pinned paths, with D4 divergence where
  recorded): phase structure and gate concepts, ZOMBIES guidance, dependency/mocking
  boundaries, and the four-layer acceptance model.
- The frontmatter `license` string simplifies to "MIT" with a pointer to this file;
  the pointer (not the tag) is the authoritative detailed record. Where in doubt, read this
  file; where this file conflicts with a binding decision, raise a proposed amendment
  (SELF-IMPROVEMENT.md §7).
