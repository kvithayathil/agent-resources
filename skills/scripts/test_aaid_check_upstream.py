"""RED test for skills/aaid/scripts/check-upstream.sh — check-only UNCHANGED.

Fixture-driven failing test for the
unchanged/check-only behavior. Mock transport via a fake `gh` on PATH; no
live network, no live writes.

Contract the tests define for GREEN:
- Script path: skills/aaid/scripts/check-upstream.sh, run with `bash`.
- Default invocation with no arguments is check-only; it never writes
  anything under the skill root.
- Skill root resolution: the script's own ../../ by default, overridable
  via env AAID_SKILL_ROOT (the tests point it at a disposable fixture).
- Transport: `gh` resolved via PATH. Expected calls (per the provenance policy and
  the verified API facts in source-manifest.md):
    gh api --method GET "repos/<repo>/commits/<default_branch>"
    gh api --method GET "repos/<repo>/contents/<path>" -f ref=<sha>
  with base64 responses {"content": ..., "encoding": "base64", ...}.
- Manifest: $AAID_SKILL_ROOT/assets/upstream/MANIFEST.json with keys
  repository, default_branch, resolved_commit, generated,
  files[{path, bytes, sha256, git_blob_sha}] (matching the real snapshot
  schema in skills/aaid/assets/upstream/MANIFEST.json).
- Verdict: exit 0 with exactly one status line on stdout.
  - "UNCHANGED" when every manifest path is byte-identical at the current
    tip compared to the pinned commit (pin == tip in this fixture) and
    local snapshot files match the manifest hashes.
  - "CHANGED" when any path differs at the tip (exit 0).
  - "ERROR: <short reason>" and nonzero exit on transport/parse/validation
    failure — NOT tested here.
- --update: authorized refresh — staged fetch of all
  manifest paths at tip, atomic cutover of the raw files + MANIFEST.json,
  and refresh of the checker-maintained check-status block in
  references/SOURCE.md; integrated pin and adapted files untouched.
"""

from __future__ import annotations

import base64
import datetime
import hashlib
import json
import os
import shutil
import subprocess
import time
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
CHECKER = REPO_ROOT / "skills" / "aaid" / "scripts" / "check-upstream.sh"
# Absolute bash: needed when a test sandboxes PATH to a fixture-only dir.
BASH = shutil.which("bash") or "/bin/bash"

PIN = "pin0000000000000000000000000000000000000001"
REPO = "example/ex"
BRANCH = "main"

# Manifest path -> raw upstream content mirrored into the fixture snapshot.
UPSTREAM_FILES = {
    "docs/guide.md": b"alpha line\n",
    "rules/rule.mdc": b"beta line\n",
}


def _git_blob_sha(data: bytes) -> str:
    """git blob SHA = sha1 of "blob <len>\\0<data>" (same as git hash-object)."""
    return hashlib.sha1(b"blob %d\x00%s" % (len(data), data)).hexdigest()


def _make_fake_gh(bin_dir: Path, fixture_upstream: Path) -> None:
    """Fake `gh` handling the two API calls the checker must make; anything
    else exits 1. Contents responses are served for any ref by default; the
    test selects tip divergence via the AAID_FAKE_TIP_SHA and
    AAID_FAKE_TIP_OVERRIDES env vars (path -> base64 remap when the ref is
    not the pin)."""
    gh = bin_dir / "gh"
    gh.write_text(
        "#!/usr/bin/env python3\n"
        "import base64, hashlib, json, os, sys\n"
        "\n"
        'pin = os.environ["AAID_FAKE_PIN"]\n'
        'root = os.environ["AAID_FAKE_ROOT"]\n'
        'overrides = json.loads(os.environ.get("AAID_FAKE_TIP_OVERRIDES", "{}"))\n'
        'pin_overrides = json.loads(os.environ.get("AAID_FAKE_PIN_OVERRIDES", "{}"))\n'
        "args = sys.argv[1:]\n"
        "\n"
        'if any("repos/example/ex/commits/main" in a for a in args):\n'
        '    print(json.dumps({"sha": os.environ.get("AAID_FAKE_TIP_SHA", pin), "commit": {"committer": {"date": "2026-01-01T00:00:00Z"}}}))\n'
        "    sys.exit(0)\n"
        "\n"
        "path = None\n"
        "ref = None\n"
        "for a in args:\n"
        '    if "repos/example/ex/contents/" in a:\n'
        '        path = a.split("repos/example/ex/contents/", 1)[1]\n'
        '    elif a.startswith("ref="):\n'
        "        ref = a[4:]\n"
        "if path is None:\n"
        "    sys.exit(1)\n"
        "try:\n"
        "    if ref == pin:\n"
        '        data = base64.b64decode(pin_overrides[path]) if path in pin_overrides else open(os.path.join(root, path), "rb").read()\n'
        "    elif path in overrides:\n"
        "        data = base64.b64decode(overrides[path])\n"
        "    else:\n"
        '        data = open(os.path.join(root, path), "rb").read()\n'
        "except OSError as e:\n"
        '    sys.stderr.write("gh: Not Found (HTTP 404)\\n")\n'
        "    sys.exit(1)\n"
        "print(json.dumps({\n"
        '    "content": base64.b64encode(data).decode(),\n'
        '    "encoding": "base64",\n'
        '    "size": len(data),\n'
        '    "sha": hashlib.sha1(b"blob %d\\0" % len(data) + data).hexdigest(),\n'
        "}))\n"
    )
    gh.chmod(0o755)


def _snapshot(root: Path) -> dict[str, str]:
    """Byte-level snapshot of every file under root, for write-mutation check."""
    return {
        str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted(root.rglob("*"))
        if p.is_file()
    }


def test_check_only_unchanged(tmp_path: Path) -> None:
    """Check-only over an unchanged fixture reports UNCHANGED, exit 0,
    and modifies nothing under the skill root."""
    root = tmp_path / "skill-root"
    upstream = root / "assets" / "upstream"
    upstream.mkdir(parents=True)

    files: list[dict[str, object]] = []
    for path, data in UPSTREAM_FILES.items():
        (upstream / path).parent.mkdir(parents=True)
        (upstream / path).write_bytes(data)
        files.append(
            {
                "path": path,
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
                "git_blob_sha": _git_blob_sha(data),
            }
        )

    manifest = {
        "repository": REPO,
        "default_branch": BRANCH,
        "resolved_commit": PIN,
        "integrated_commit": PIN,  # vendored: the snapshot IS the integrated state
        "generated": "2026-10-24",
        "files": files,
    }
    (upstream / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")

    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    _make_fake_gh(bin_dir, upstream)

    before = _snapshot(root)
    env = dict(os.environ)
    env["PATH"] = str(bin_dir) + os.pathsep + env["PATH"]
    env["AAID_SKILL_ROOT"] = str(root)
    env["AAID_FAKE_PIN"] = PIN
    env["AAID_FAKE_ROOT"] = str(upstream)

    result = subprocess.run(
        ["bash", str(CHECKER)],
        capture_output=True,
        text=True,
        env=env,
        timeout=120,
    )

    after = _snapshot(root)

    assert result.returncode == 0, f"expected exit 0, got {result.returncode}; stderr:\n{result.stderr}"
    assert result.stdout.strip() == "UNCHANGED", f"stdout was {result.stdout!r}, stderr {result.stderr!r}"
    assert after == before, "check-only run modified files under the skill root"


CHECK_STATUS_BLOCK = """\
<!-- BEGIN CHECK-STATUS: checker-maintained — rewrite only via an authorized
     `check-upstream.sh --update` run (design D6); lines inside this block are
     data consumed by the checker's freshness report. -->
- Last successful check: pending (no authorized refresh run yet)
- Fetched commit: none
- Integrated pin: `{pin}` (reviewed/integrated content only; never advanced by a fetch)
<!-- END CHECK-STATUS -->
"""


def test_update_refreshes_snapshot_and_metadata(tmp_path: Path) -> None:
    """Authorized `--update` over a changed fixture: staged fetch of every
    manifest path at tip, validated as a complete snapshot, then atomic
    replacement of the raw files + regenerated MANIFEST.json + refreshed
    SOURCE.md check-status block (design D6: fetched snapshot vs integrated
    pin stay distinguishable — the integrated pin is never advanced).
    Adapted sentinels, assets/upstream/README.md, the lock file, and
    everything else under the skill root stay byte-identical; no staging
    residue remains."""
    root = tmp_path / "skill-root"
    upstream = root / "assets" / "upstream"
    upstream.mkdir(parents=True)
    (root / "references").mkdir(exist_ok=True)

    tip = "tip0000000000000000000000000000000000000002"
    tip_data = dict(UPSTREAM_FILES)
    tip_data["docs/guide.md"] = b"alpha line changed\n"

    files: list[dict[str, object]] = []
    for path, data in UPSTREAM_FILES.items():
        (upstream / path).parent.mkdir(parents=True)
        (upstream / path).write_bytes(data)
        files.append(
            {
                "path": path,
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
                "git_blob_sha": _git_blob_sha(data),
            }
        )

    manifest = {
        "repository": REPO,
        "default_branch": BRANCH,
        "resolved_commit": PIN,
        "generated": "2026-10-24",
        "files": files,
    }
    (upstream / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")

    readme = "upstream README policy file — local, never fetched\n".encode()
    (upstream / "README.md").write_bytes(readme)

    sentinels = {
        "references/SKILL.md": b"adapted skill content sentinel\n",
        "references/LESSONS_LEARNED.md": b"adapted lessons sentinel\n",
    }
    for rel, data in sentinels.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)

    lock = b'{"locks": {"aaid": {"integrated_pin": "' + PIN.encode() + b'"}}}\n'
    (root / "skills-lock.json").write_bytes(lock)

    source = root / "references" / "SOURCE.md"
    source.write_text(f"# Source provenance — fixture\n\n{CHECK_STATUS_BLOCK.format(pin=PIN)}")

    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    _make_fake_gh(bin_dir, upstream)
    env = dict(os.environ)
    env["PATH"] = str(bin_dir) + os.pathsep + env["PATH"]
    env["AAID_SKILL_ROOT"] = str(root)
    env["AAID_FAKE_PIN"] = PIN
    env["AAID_FAKE_ROOT"] = str(upstream)
    env["AAID_FAKE_TIP_SHA"] = tip
    env["AAID_FAKE_TIP_OVERRIDES"] = json.dumps({"docs/guide.md": base64.b64encode(tip_data["docs/guide.md"]).decode()})

    before = _snapshot(root)
    allowed = {
        "assets/upstream/MANIFEST.json",
        "assets/upstream/docs/guide.md",
        "references/SOURCE.md",
    }
    result = subprocess.run(
        ["bash", str(CHECKER), "--update"],
        capture_output=True,
        text=True,
        env=env,
        timeout=120,
    )
    after = _snapshot(root)

    assert result.returncode == 0, f"expected exit 0, got {result.returncode}; stderr:\n{result.stderr}"
    assert result.stdout.strip() == f"UPDATED {tip}", f"stdout was {result.stdout!r}, stderr {result.stderr!r}"

    # 2. raw manifest-path files hold tip content; manifest regenerated.
    assert (upstream / "docs/guide.md").read_bytes() == tip_data["docs/guide.md"]
    assert (upstream / "rules/rule.mdc").read_bytes() == UPSTREAM_FILES["rules/rule.mdc"]
    new_manifest = json.loads((upstream / "MANIFEST.json").read_text())
    assert new_manifest["repository"] == REPO and new_manifest["default_branch"] == BRANCH
    assert new_manifest["resolved_commit"] == tip
    by_path = {e["path"]: e for e in new_manifest["files"]}
    for path, data in tip_data.items():
        entry = by_path[path]
        assert entry["bytes"] == len(data)
        assert entry["sha256"] == hashlib.sha256(data).hexdigest()
        assert entry["git_blob_sha"] == _git_blob_sha(data)

    # 3. SOURCE.md check-status block refreshed, integrated pin untouched.
    src = source.read_text()
    assert "Last successful check: pending" not in src
    assert f"Fetched commit: `{tip}`" in src
    assert f"`{PIN}`" in src  # integrated pin line unchanged

    # 4+5. everything else byte-identical (covers sentinels, README.md, lock,
    # and proves no staging residue under .cache/ survived the run).
    unexpected = {k: v for k, v in after.items() if k not in allowed}
    expected_kept = {k: v for k, v in before.items() if k not in allowed}
    assert unexpected == expected_kept, (
        f"files outside the update scope changed or missing:\n"
        f"gone: {sorted(set(expected_kept) - set(unexpected))}\n"
        f"new/altered: {sorted(set(unexpected) - set(expected_kept))}"
    )


def test_check_only_idempotent(tmp_path: Path) -> None:
    """Idempotence (per the maintenance spec): after one authorized --update
    over a successfully-integrated fixture (tip content == pinned content,
    tip sha == pin), repeated check-only runs report UNCHANGED with exit 0 and
    leave the fixture root byte-identical — no writes, no `.cache` residue.
    The fixture's check-status block carries a 3-LINE Integrated pin entry;
    the --update pass must preserve the COMPLETE entry so the two check-only
    runs see a stable file."""
    root = tmp_path / "skill-root"
    upstream = root / "assets" / "upstream"
    upstream.mkdir(parents=True)
    (root / "references").mkdir(exist_ok=True)

    files: list[dict[str, object]] = []
    for path, data in UPSTREAM_FILES.items():
        (upstream / path).parent.mkdir(parents=True, exist_ok=True)
        (upstream / path).write_bytes(data)
        files.append(
            {
                "path": path,
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
                "git_blob_sha": _git_blob_sha(data),
            }
        )

    manifest = {
        "repository": REPO,
        "default_branch": BRANCH,
        "resolved_commit": PIN,
        "generated": "2026-10-24",
        "files": files,
    }
    (upstream / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")

    pin_entry = (
        f"- Integrated pin: `{PIN}`\n"
        "  (tree `b0da7f19f18fb012df34ba43611a99482dbbc7ef`, commit author date\n"
        "  `2026-08-30T19:51:46Z`) — the reviewed/integrated content only; never\n"
        "  advanced by a fetch.\n"
    )
    block = (
        "<!-- BEGIN CHECK-STATUS: checker-maintained — rewrite only via an authorized\n"
        "     `check-upstream.sh --update` run (design D6); lines inside this block are\n"
        "     data consumed by the checker's freshness report. -->\n"
        "- Last successful check: pending (no authorized refresh run yet)\n"
        "- Fetched commit: none\n" + pin_entry + "<!-- END CHECK-STATUS -->\n"
    )
    source = root / "references" / "SOURCE.md"
    source.write_text(f"# Source provenance — fixture\n\n{block}")

    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    _make_fake_gh(bin_dir, upstream)
    env = dict(os.environ)
    env["PATH"] = str(bin_dir) + os.pathsep + env["PATH"]
    env["AAID_SKILL_ROOT"] = str(root)
    env["AAID_FAKE_PIN"] = PIN
    env["AAID_FAKE_ROOT"] = str(upstream)
    env["AAID_FAKE_TIP_SHA"] = PIN
    env["AAID_FAKE_TIP_OVERRIDES"] = "{}"

    def run(args: list[str]) -> subprocess.CompletedProcess:
        return subprocess.run(
            ["bash", str(CHECKER), *args],
            capture_output=True,
            text=True,
            env=env,
            timeout=120,
        )

    # One authorized refresh settles the fixture into the integrated state.
    first = run(["--update"])
    assert first.returncode == 0, f"stderr:\n{first.stderr}"
    assert first.stdout.strip() == f"UPDATED {PIN}", first.stdout

    # The COMPLETE 3-line Integrated pin entry survives the rewrite verbatim.
    src = source.read_text()
    for line in pin_entry.rstrip("\n").split("\n"):
        assert line in src, f"pin entry line lost: {line!r}\nblock now:\n{src}"

    # Repeated check-only runs: UNCHANGED, no writes, no residue — state after
    # run 1 must equal state after run 2 (and the settled post-update state).
    before = _snapshot(root)
    for i, r in enumerate((run([]), run([])), 1):
        assert r.returncode == 0, f"run {i}: stderr:\n{r.stderr}"
        assert r.stdout.strip() == "UNCHANGED", f"run {i}: {r.stdout!r}"
        assert _snapshot(root) == before, f"run {i} modified the fixture root"
    assert not list((root / ".cache").glob("staging-*")) if (root / ".cache").is_dir() else True, (
        "staging residue after run 2"
    )


def test_unreviewed_fetched_state_flags_changed(tmp_path: Path) -> None:
    """Post-update state WITHOUT running --update in the test: the manifest
    resolves to TIP2 and the local snapshot is coherent at TIP2 (single
    commit for the whole snapshot — D6), but the SOURCE block's integrated
    pin is still PIN1. Check-only must keep flagging the unreviewed fetched
    content as CHANGED (D6: the lock/integrated pin represents reviewed
    content only; a fetched-but-unreviewed refresh is never 'UNCHANGED') —
    NOT upgrade to UNCHANGED merely because the manifest was advanced by the
    last fetch."""
    pin1 = PIN
    tip2 = "tip200000000000000000000000000000000000002"
    pin1_files = dict(UPSTREAM_FILES)
    tip2_files = {"docs/guide.md": b"alpha line changed\n", "rules/rule.mdc": UPSTREAM_FILES["rules/rule.mdc"]}

    root = tmp_path / "skill-root"
    upstream = root / "assets" / "upstream"
    upstream.mkdir(parents=True)
    (root / "references").mkdir(exist_ok=True)

    files: list[dict[str, object]] = []
    for path, data in tip2_files.items():
        (upstream / path).parent.mkdir(parents=True, exist_ok=True)
        (upstream / path).write_bytes(data)
        files.append(
            {
                "path": path,
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
                "git_blob_sha": _git_blob_sha(data),
            }
        )

    # Fixture coherence (the state the checker validates): one snapshot
    # commit across all files — every entry hashes the TIP2 content and the
    # manifest's resolved_commit is that one commit.
    manifest = {
        "repository": REPO,
        "default_branch": BRANCH,
        "resolved_commit": tip2,
        "generated": "2026-10-24",
        "files": files,
    }
    for e in files:
        data = tip2_files[e["path"]]
        assert e["bytes"] == len(data)
        assert e["sha256"] == hashlib.sha256(data).hexdigest()
        assert e["git_blob_sha"] == _git_blob_sha(data)
    (upstream / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")

    pin_entry = (
        f"- Integrated pin: `{pin1}`\n"
        "  (tree `b0da7f19f18fb012df34ba43611a99482dbbc7ef`, commit author date\n"
        "  `2026-08-30T19:51:46Z`) — the reviewed/integrated content only; never\n"
        "  advanced by a fetch.\n"
    )
    source = root / "references" / "SOURCE.md"
    source.write_text(
        "# Source provenance — fixture\n\n"
        "<!-- BEGIN CHECK-STATUS: checker-maintained — rewrite only via an authorized\n"
        "     `check-upstream.sh --update` run (design D6); lines inside this block are\n"
        "     data consumed by the checker's freshness report. -->\n"
        "- Last successful check: " + datetime.date.today().isoformat() + "\n"
        f"- Fetched commit: `{tip2}`\n" + pin_entry + "<!-- END CHECK-STATUS -->\n"
    )

    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    _make_fake_gh(bin_dir, upstream)
    env = dict(os.environ)
    env["PATH"] = str(bin_dir) + os.pathsep + env["PATH"]
    env["AAID_SKILL_ROOT"] = str(root)
    env["AAID_FAKE_PIN"] = pin1
    env["AAID_FAKE_ROOT"] = str(upstream)
    env["AAID_FAKE_TIP_SHA"] = tip2
    # gh serves TIP2 content at the tip ref (identical to the local snapshot)
    # and PIN1 content at the PIN1 ref (one path differs).
    env["AAID_FAKE_TIP_OVERRIDES"] = "{}"
    env["AAID_FAKE_PIN_OVERRIDES"] = json.dumps(
        {"docs/guide.md": base64.b64encode(pin1_files["docs/guide.md"]).decode()}
    )

    before = _snapshot(root)
    result = subprocess.run(
        ["bash", str(CHECKER)],
        capture_output=True,
        text=True,
        env=env,
        timeout=120,
    )
    after = _snapshot(root)

    assert result.returncode == 0, f"expected exit 0, got {result.returncode}; stderr:\n{result.stderr}"
    assert result.stdout.strip() == "CHANGED", (
        f"unreviewed fetched content must stay flagged; stdout was {result.stdout!r}, stderr {result.stderr!r}"
    )
    assert after == before, "check-only run modified files under the skill root"


def test_update_preserves_adapted_skill_and_lessons(tmp_path: Path) -> None:
    """--update over a realistic adapted skill root refreshes only the raw
    snapshot + MANIFEST.json + SOURCE's checker block, and byte-preserves the
    adapted intellectual property: SKILL.md, LESSONS_LEARNED.md (lesson entry
    verbatim), CHANGELOG.md, PHASES.md, and assets/upstream/README.md (D6:
    never replaces adapted SKILL.md/references; preserves lessons and the
    protected README policy file)."""
    tip = "tip0000000000000000000000000000000000000002"
    tip_files = {"docs/guide.md": b"alpha line changed\n", "rules/rule.mdc": UPSTREAM_FILES["rules/rule.mdc"]}

    root = tmp_path / "skill-root"
    upstream = root / "assets" / "upstream"
    upstream.mkdir(parents=True)
    (root / "references").mkdir()

    files: list[dict[str, object]] = []
    for path, data in UPSTREAM_FILES.items():
        (upstream / path).parent.mkdir(parents=True, exist_ok=True)
        (upstream / path).write_bytes(data)
        files.append(
            {
                "path": path,
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
                "git_blob_sha": _git_blob_sha(data),
            }
        )
    manifest = {
        "repository": REPO,
        "default_branch": BRANCH,
        "resolved_commit": PIN,
        "generated": "2026-10-24",
        "files": files,
    }
    (upstream / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")
    readme = "README = protected local upstream-mirror policy file\n".encode()
    (upstream / "README.md").write_bytes(readme)

    docs = {}  # rel -> content, all adapted IP that must survive verbatim
    docs["references/SKILL.md"] = (
        "---\n"
        "name: aaid\n"
        "description: Augmented AI Development methodology, adapted\n"
        "metadata:\n"
        "  source: upstream (modified)\n"
        "  version: 1.0.0\n"
        "---\n"
        "\n"
        "# AAID\n"
        "\n"
        "Use when driving spec-driven development for testing-heavy work.\n"
        "\n"
        "## Phases\n"
        "\n"
        "1. Baseline: derive acceptance tests from requirements.\n"
        "2. Design: decompose into workflows and data contracts.\n"
        "3. Execute: one workflow at a time with validation gates.\n"
        "4. Review: human sign-off before advancing.\n"
        "\n"
        "## Adaptations relative to upstream\n"
        "\n"
        "- Four-layer framing kept; the recorded divergence decisions applied.\n"
        "- Checks fail closed; fetches staged; pins never self-advance.\n"
        "\n"
        "## References\n"
        "\n"
        "- See references/ATDD.md for the acceptance-testing workflow.\n"
        "- See references/PHASES.md for phase gates.\n"
    )
    docs["references/LESSONS_LEARNED.md"] = (
        "# Lessons learned\n"
        "\n"
        "## Format\n"
        "\n"
        "Each entry: Context / Lesson / Validations count / Evidence.\n"
        "\n"
        "## Entries\n"
        "\n"
        "### 2026-10-24 — heredoc discipline\n"
        "\n"
        "- **Context**: checker scripts embed python programs.\n"
        "- **Lesson**: use a quoted heredoc delimiter so no shell expansion\n"
        "  reaches remote-derived text.\n"
        "- **Validations**: 1\n"
        "- **Evidence**: fixture paths with spaces round-trip fine.\n"
    )
    docs["references/CHANGELOG.md"] = "# Changelog\n\n## 1.0.0\n\n- Adapted from upstream at pin.\n"
    docs["references/PHASES.md"] = (
        "# Phases\n\n"
        + "".join(f"## Phase {i}\nGate: sign-off {i}.\n\n" for i in range(1, 12))
        + "## Review\nHuman sign-off closes every phase.\n"
    )
    for rel, content in docs.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(content.encode())

    pin_entry = (
        f"- Integrated pin: `{PIN}`\n"
        "  (tree `b0da7f19f18fb012df34ba43611a99482dbbc7ef`, commit author date\n"
        "  `2026-08-30T19:51:46Z`) — the reviewed/integrated content only; never\n"
        "  advanced by a fetch.\n"
    )
    source = root / "references" / "SOURCE.md"
    source.write_text(
        "# Source provenance — fixture\n\n"
        "<!-- BEGIN CHECK-STATUS: checker-maintained — rewrite only via an authorized\n"
        "     `check-upstream.sh --update` run (design D6); lines inside this block are\n"
        "     data consumed by the checker's freshness report. -->\n"
        "- Last successful check: pending (no authorized refresh run yet)\n"
        "- Fetched commit: none\n" + pin_entry + "<!-- END CHECK-STATUS -->\n"
    )

    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    _make_fake_gh(bin_dir, upstream)
    env = dict(os.environ)
    env["PATH"] = str(bin_dir) + os.pathsep + env["PATH"]
    env["AAID_SKILL_ROOT"] = str(root)
    env["AAID_FAKE_PIN"] = PIN
    env["AAID_FAKE_ROOT"] = str(upstream)
    env["AAID_FAKE_TIP_SHA"] = tip
    env["AAID_FAKE_TIP_OVERRIDES"] = json.dumps(
        {"docs/guide.md": base64.b64encode(tip_files["docs/guide.md"]).decode()}
    )

    before = _snapshot(root)
    allowed = {
        "assets/upstream/MANIFEST.json",
        "assets/upstream/docs/guide.md",
        "references/SOURCE.md",
    }
    result = subprocess.run(
        ["bash", str(CHECKER), "--update"],
        capture_output=True,
        text=True,
        env=env,
        timeout=120,
    )
    after = _snapshot(root)

    assert result.returncode == 0, f"expected exit 0, got {result.returncode}; stderr:\n{result.stderr}"
    assert result.stdout.strip() == f"UPDATED {tip}", f"stdout {result.stdout!r}"

    # Raw snapshot + manifest regenerated at tip.
    assert (upstream / "docs/guide.md").read_bytes() == tip_files["docs/guide.md"]
    new_manifest = json.loads((upstream / "MANIFEST.json").read_text())
    assert new_manifest["resolved_commit"] == tip
    by_path = {e["path"]: e for e in new_manifest["files"]}
    for path, data in tip_files.items():
        assert by_path[path]["sha256"] == hashlib.sha256(data).hexdigest()

    # Adapted IP byte-identical — including the whole multi-line pin entry.
    for rel, content in docs.items():
        assert (root / rel).read_bytes() == content.encode(), f"{rel} modified"
    assert (upstream / "README.md").read_bytes() == readme, "README modified"
    src = source.read_text()
    assert all(line in src for line in pin_entry.rstrip("\n").split("\n")), src

    # Full-root diff is EXACTLY the allowed set (no other writes anywhere).
    gone = set(before) - set(after)
    added = set(after) - set(before)
    # changed over the UNION of keys (review nit: before-keys-or-after-keys
    # only would let a stray new/deleted file escape the diff).
    changed_paths = {k for k in set(before) | set(after) if before.get(k) != after.get(k)}
    assert changed_paths == allowed - gone, (
        f"changed: {sorted(changed_paths)} gone: {sorted(gone)} added: {sorted(added)}"
    )


def test_check_only_changed(tmp_path: Path) -> None:
    """Check-only over a fixture whose tip differs from the pin at one path
    reports CHANGED, exit 0 (a successful check, not a command failure),
    and modifies nothing under the skill root (design D6)."""
    root = tmp_path / "skill-root"
    upstream = root / "assets" / "upstream"
    upstream.mkdir(parents=True)

    files: list[dict[str, object]] = []
    for path, data in UPSTREAM_FILES.items():
        (upstream / path).parent.mkdir(parents=True)
        (upstream / path).write_bytes(data)
        files.append(
            {
                "path": path,
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
                "git_blob_sha": _git_blob_sha(data),
            }
        )

    manifest = {
        "repository": REPO,
        "default_branch": BRANCH,
        "resolved_commit": PIN,
        "integrated_commit": PIN,  # vendored: the snapshot IS the integrated state
        "generated": "2026-10-24",
        "files": files,
    }
    (upstream / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")

    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    tip = "tip0000000000000000000000000000000000000002"
    changed = {"docs/guide.md": b"alpha line changed\n"}
    _make_fake_gh(bin_dir, upstream)

    before = _snapshot(root)
    env = dict(os.environ)
    env["PATH"] = str(bin_dir) + os.pathsep + env["PATH"]
    env["AAID_SKILL_ROOT"] = str(root)
    env["AAID_FAKE_PIN"] = PIN
    env["AAID_FAKE_ROOT"] = str(upstream)
    env["AAID_FAKE_TIP_SHA"] = tip
    env["AAID_FAKE_TIP_OVERRIDES"] = json.dumps({p: base64.b64encode(d).decode() for p, d in changed.items()})

    result = subprocess.run(
        ["bash", str(CHECKER)],
        capture_output=True,
        text=True,
        env=env,
        timeout=120,
    )

    after = _snapshot(root)

    assert result.returncode == 0, f"expected exit 0, got {result.returncode}; stderr:\n{result.stderr}"
    assert result.stdout.strip() == "CHANGED", f"stdout was {result.stdout!r}, stderr {result.stderr!r}"
    assert after == before, "check-only run modified files under the skill root"


TRANSPORT_FAILURES = {
    "network_500": (1, "gh: HTTP 500 (network)"),
    "auth_exit4": (4, "gh: authentication required"),
    "rate_limited_403": (1, "gh: HTTP 403, x-ratelimit-remaining: 0 (rate limit)"),
}


def _make_failing_gh(bin_dir: Path, exit_code: int, message: str) -> None:
    """Fake `gh` that always fails the way gh does: same exit code, message on
    stderr, nothing on stdout (transport/auth/rate-limit shipping failure)."""
    gh = bin_dir / "gh"
    gh.write_text(
        f"#!/usr/bin/env python3\nimport sys\nsys.stderr.write({message!r} + chr(10))\nsys.exit({exit_code})\n"
    )
    gh.chmod(0o755)


def _failure_fixture(tmp_path: Path) -> tuple[Path, Path, Path, dict[str, str]]:
    """Base fixture root in last-good state: 2-path snapshot + MANIFEST.json
    + protected README.md + references/SOURCE.md with a settled check-status
    block. Returns (root, upstream, source, env)."""
    root = tmp_path / "skill-root"
    upstream = root / "assets" / "upstream"
    upstream.mkdir(parents=True)
    (root / "references").mkdir(exist_ok=True)

    files: list[dict[str, object]] = []
    for path, data in UPSTREAM_FILES.items():
        (upstream / path).parent.mkdir(parents=True, exist_ok=True)
        (upstream / path).write_bytes(data)
        files.append(
            {
                "path": path,
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
                "git_blob_sha": _git_blob_sha(data),
            }
        )
    (upstream / "MANIFEST.json").write_text(
        json.dumps(
            {
                "repository": REPO,
                "default_branch": BRANCH,
                "resolved_commit": PIN,
                "generated": "2026-10-24",
                "files": files,
            },
            indent=2,
        )
        + "\n"
    )
    source = root / "references" / "SOURCE.md"
    source.write_text(
        "# Source provenance — fixture\n\n"
        "<!-- BEGIN CHECK-STATUS: checker-maintained -->\n"
        "- Last successful check: 2026-10-23\n"
        f"- Fetched commit: `{PIN}`\n"
        f"- Integrated pin: `{PIN}`\n"
        "<!-- END CHECK-STATUS -->\n"
    )
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    env = dict(os.environ)
    env["PATH"] = str(bin_dir) + os.pathsep + env["PATH"]
    env["AAID_SKILL_ROOT"] = str(root)
    env["AAID_FAKE_PIN"] = PIN
    env["AAID_FAKE_ROOT"] = str(upstream)
    return root, upstream, source, env


@pytest.mark.parametrize("variant", list(TRANSPORT_FAILURES), ids=list(TRANSPORT_FAILURES))
def test_transport_failures_error(tmp_path: Path, variant: str) -> None:
    """Network / authentication / rate-limit failures (design D6, spec aaid-
    maintenance): the checker reports ERROR, exits nonzero, retains the last
    good data and metadata (no false-freshness write, no block rewrite), and
    leaves no staging residue."""
    root, upstream, source, env = _failure_fixture(tmp_path)
    exit_code, message = TRANSPORT_FAILURES[variant]
    _make_failing_gh(tmp_path / "bin", exit_code, message)

    before = _snapshot(root)
    result = subprocess.run(
        ["bash", str(CHECKER)],
        capture_output=True,
        text=True,
        env=env,
        timeout=120,
    )
    after = _snapshot(root)

    assert result.returncode != 0, f"{variant}: transport failure must exit nonzero; stdout {result.stdout!r}"
    out = result.stderr.strip()
    assert out.startswith("ERROR:"), f"{variant}: no ERROR verdict line; got {out!r}"
    # No false freshness: the settled check-status block survives verbatim.
    assert "Last successful check: 2026-10-23" in source.read_text()
    assert after == before, f"{variant}: run modified the fixture root"
    assert not list((root / ".cache").glob("staging-*")) if (root / ".cache").is_dir() else True, "staging residue"


def test_transport_failure_update_preserves_last_good_state(tmp_path: Path) -> None:
    """One --update run under an authentication failure: nonzero ERROR, raw
    files + MANIFEST.json + SOURCE.md block all byte-identical (last good
    snapshot retained, staging cleaned, no false freshness)."""
    root, upstream, source, env = _failure_fixture(tmp_path)
    _make_failing_gh(tmp_path / "bin", 4, "gh: authentication required")

    before = _snapshot(root)
    result = subprocess.run(
        ["bash", str(CHECKER), "--update"],
        capture_output=True,
        text=True,
        env=env,
        timeout=120,
    )
    after = _snapshot(root)

    assert result.returncode != 0, f"stdout {result.stdout!r}"
    out = result.stderr.strip()
    assert out.startswith("ERROR:"), f"no ERROR verdict line; got {out!r}"
    assert after == before, "--update under failure modified the fixture root"
    assert not list((root / ".cache").glob("staging-*")) if (root / ".cache").is_dir() else True, "staging residue"


MALFORMED_SHAPES = {
    "garbage_not_json": {"stdout": "not-json-garbage\n"},
    "encoding_none": {"stdout": json.dumps({"encoding": "none"}) + "\n"},
    "content_missing": {"stdout": json.dumps({"encoding": "base64", "size": 5}) + "\n"},
    "content_empty": {
        "stdout": json.dumps(
            {"encoding": "base64", "content": "", "size": 5, "sha": hashlib.sha1(b"blob 0\x00").hexdigest()}
        )
        + "\n"
    },
    "sha_none": {
        "stdout": json.dumps(
            {
                "encoding": "base64",
                "content": base64.b64encode(UPSTREAM_FILES["docs/guide.md"]).decode(),
                "size": len(UPSTREAM_FILES["docs/guide.md"]),
                "sha": None,
            }
        )
        + "\n"
    },
}


def _make_malformed_gh(bin_dir: Path, shape: dict[str, str]) -> None:
    """Fake `gh` answering the commits call correctly (tip = pin) but the
    FIRST contents call with an API-returned malformed/mis-declared shape."""
    gh = bin_dir / "gh"
    gh.write_text(
        "#!/usr/bin/env python3\n"
        "import json, os, sys\n"
        "args = sys.argv[1:]\n"
        'if any("commits/main" in a for a in args):\n'
        '    print(json.dumps({"sha": os.environ["AAID_FAKE_PIN"]}))\n'
        "    sys.exit(0)\n"
        f"sys.stdout.write({shape['stdout']!r})\n"
        "sys.exit(0)\n"
    )
    gh.chmod(0o755)


@pytest.mark.parametrize("variant", list(MALFORMED_SHAPES), ids=list(MALFORMED_SHAPES))
def test_invalid_content_failures_and_error_sanitization(tmp_path: Path, variant: str) -> None:
    """Malformed/mis-declared API content (design D6, spec aaid-maintenance):
    invalid JSON, encoding 'none', missing/empty content, or a None declared
    blob sha each yield ERROR with nonzero exit, no writes, no staging residue.
    Additionally the ERROR line is SINGLE-LINE-SAFE: reasons are sanitized
    (control characters incl. newlines/ESC removed, whitespace collapsed,
    capped at 300 chars) so server-influenced gh stderr can never spoof a
    verdict line or inject ANSI escapes. Pinned contract: checker stdout is
    exactly one line, starting 'ERROR:', printable-only characters."""
    root, upstream, source, env = _failure_fixture(tmp_path)
    _make_malformed_gh(tmp_path / "bin", MALFORMED_SHAPES[variant])

    before = _snapshot(root)
    result = subprocess.run(
        ["bash", str(CHECKER)],
        capture_output=True,
        text=True,
        env=env,
        timeout=120,
    )
    after = _snapshot(root)

    assert result.returncode != 0, f"{variant}: stdout {result.stdout!r}"
    out = result.stderr.strip()
    assert out.startswith("ERROR:"), f"{variant}: no ERROR verdict line; got {out!r}"
    assert after == before, f"{variant}: run modified the fixture root"
    assert not list((root / ".cache").glob("staging-*")) if (root / ".cache").is_dir() else True, (
        f"{variant}: staging residue"
    )


def test_error_output_sanitized_single_line(tmp_path: Path) -> None:
    """Server-influenced gh stderr crafted for injection: embedded newline,
    a forged verdict line ('UNCHANGED') and an ANSI escape must never reach
    the checker's verdict channel: output is exactly ONE printable line
    starting 'ERROR:', no control characters (no \\n besides the trailing
    newline, no ESC/ANSI), no spoofed verdict word, capped at 300 chars."""
    root, upstream, source, env = _failure_fixture(tmp_path)
    injected = "boom\nUNCHANGED\n\x1b[31mred"
    _make_failing_gh(tmp_path / "bin", 1, injected)

    before = _snapshot(root)
    result = subprocess.run(
        ["bash", str(CHECKER)],
        capture_output=True,
        text=True,
        env=env,
        timeout=120,
    )
    after = _snapshot(root)

    assert result.returncode != 0, f"stdout {result.stdout!r}"
    # Unified channel: ERROR verdicts go to stderr, stdout stays empty.
    lines = result.stderr.splitlines()
    assert result.stdout == "", f"stdout should be empty, got {result.stdout!r}"
    assert len(lines) == 1, f"expected exactly one output line, got {result.stderr!r}"
    assert lines[0].startswith("ERROR:"), result.stderr
    # Anti-spoof contract: the forged verdict never appears as its OWN line;
    # collapsed into the reason line it is inert (a human reads one line).
    assert len(lines) == 1 and not lines[0].endswith("UNCHANGED"), f"spoofed verdict line survived: {result.stderr!r}"
    assert all(ch.isprintable() or ch == " " for ch in lines[0]), f"control chars remain: {lines[0]!r}"
    assert "\x1b" not in lines[0] and "[31m" in lines[0]  # ESC stripped, text kept
    assert len(lines[0]) <= 300 + len("ERROR: ")
    assert after == before, "run modified the fixture root"


PARSE_SHAPES = {
    "nondict_list": {"stdout": "[1, 2]\n"},
    "nondict_string": {"stdout": '"just a string"\n'},
    "nondict_number": {"stdout": "123\n"},
}


@pytest.mark.parametrize(
    "variant",
    list(PARSE_SHAPES) + ["manifest_corrupt", "raw_file_missing"],
    ids=list(PARSE_SHAPES) + ["manifest_corrupt", "raw_file_missing"],
)
def test_parse_and_local_input_errors_report_error(tmp_path: Path, variant: str) -> None:
    """Non-dict JSON from gh and corrupt/absent local inputs must surface as
    ONE sanitized `ERROR:` line on stderr with nonzero exit — never a raw
    traceback ('Traceback (most recent call last)' must not appear) and never
    a partial write (zero writes, fixture byte-identical)."""
    root, upstream, source, env = _failure_fixture(tmp_path)
    if variant in PARSE_SHAPES:
        _make_malformed_gh(tmp_path / "bin", PARSE_SHAPES[variant])
    else:
        # Local-input defects run with a healthy tip mock (tip == pin) so the
        # error provably comes from local state, never from the transport,
        # and no system gh / live network is ever consulted.
        _make_fake_gh(tmp_path / "bin", upstream)
    if variant == "manifest_corrupt":
        (upstream / "MANIFEST.json").write_text("{not json at all\n")
    elif variant == "raw_file_missing":
        (upstream / "docs/guide.md").unlink()

    before = _snapshot(root)
    result = subprocess.run(
        ["bash", str(CHECKER)],
        capture_output=True,
        text=True,
        env=env,
        timeout=120,
    )
    after = _snapshot(root)

    assert result.returncode != 0, f"{variant}: stdout {result.stdout!r}"
    assert result.stdout == "", f"{variant}: stdout not empty: {result.stdout!r}"
    err = result.stderr.strip()
    assert err.startswith("ERROR:"), f"{variant}: no ERROR verdict line; got {err[:200]!r}"
    assert "Traceback (most recent call last)" not in result.stderr, f"{variant}: raw traceback escaped to stderr"
    assert after == before, f"{variant}: run modified the fixture root"
    assert not list((root / ".cache").glob("staging-*")) if (root / ".cache").is_dir() else True, (
        f"{variant}: staging residue"
    )


def test_interrupted_update_preserves_last_good_state(tmp_path: Path) -> None:
    """--update where the fetch succeeds for the FIRST path (staging dir gets
    created, a partial fetch lands) then fails with HTTP 500 on the second
    path: nonzero + ERROR on stderr, the ENTIRE last-good fixture root stays
    byte-identical, every piece of staging residue is removed, and the
    settled SOURCE.md block is untouched (no false freshness)."""
    root, upstream, source, env = _failure_fixture(tmp_path)

    bin_dir = Path(env["PATH"].split(os.pathsep, 1)[0])
    gh = bin_dir / "gh"
    gh.write_text(
        "#!/usr/bin/env python3\n"
        "import base64, hashlib, json, os, sys\n"
        "args = sys.argv[1:]\n"
        'if any("commits/main" in a for a in args):\n'
        '    print(json.dumps({"sha": os.environ["AAID_FAKE_TIP"]}))\n'
        "    sys.exit(0)\n"
        "path = None\n"
        "for a in args:\n"
        '    if "contents/" in a:\n'
        '        path = a.split("contents/", 1)[1]\n'
        'if path == "docs/guide.md":\n'
        '    data = open(os.path.join(os.environ["AAID_FAKE_ROOT"], path), "rb").read()\n'
        "    print(json.dumps({\n"
        '        "content": base64.b64encode(data).decode(),\n'
        '        "encoding": "base64",\n'
        '        "size": len(data),\n'
        '        "sha": hashlib.sha1(b"blob %d\\0" % len(data) + data).hexdigest(),\n'
        "    }))\n"
        "    sys.exit(0)\n"
        'sys.stderr.write("gh: HTTP 500 (network)\\n")\n'
        "sys.exit(1)\n"
    )
    gh.chmod(0o755)
    env["AAID_FAKE_TIP"] = "tip0000000000000000000000000000000000000002"
    env["AAID_FAKE_ROOT"] = str(upstream)
    env["AAID_FAKE_PIN_OVERRIDES"] = "{}"
    env["AAID_FAKE_TIP_OVERRIDES"] = "{}"

    before = _snapshot(root)
    result = subprocess.run(
        ["bash", str(CHECKER), "--update"],
        capture_output=True,
        text=True,
        env=env,
        timeout=120,
    )
    after = _snapshot(root)

    assert result.returncode != 0, f"stdout {result.stdout!r}"
    assert result.stdout == "", f"stdout not empty: {result.stdout!r}"
    err = result.stderr.strip()
    assert err.startswith("ERROR:"), f"no ERROR verdict line; got {err[:200]!r}"
    assert "Traceback (most recent call last)" not in result.stderr
    assert after == before, "interrupted --update modified the last-good fixture root"
    assert not list((root / ".cache").glob("staging-*")) if (root / ".cache").is_dir() else True, (
        "staging residue after interrupted update"
    )
    assert "Last successful check: 2026-10-23" in source.read_text()


MISSING_VARIANTS = ("no_gh_binary", "manifest_file_absent", "upstream_dir_absent", "source_absent_update")


@pytest.mark.parametrize("variant", MISSING_VARIANTS, ids=MISSING_VARIANTS)
def test_missing_tools_and_assets(tmp_path: Path, variant: str) -> None:
    """Missing tools/assets (design D6, spec aaid-maintenance): (i) gh not on
    PATH, (ii) MANIFEST.json file absent, (iii) whole assets/upstream dir
    absent — each surfaces as ONE sanitized single `ERROR:` line on stderr,
    nonzero exit, NO raw traceback, zero writes. (iv) references/SOURCE.md
    entirely absent during `--update` must produce a SPECIFIC reason naming
    SOURCE.md (not a bare 'unexpected FileNotFoundError') — with the hygiene
    contract shared: nonzero, stdout empty, no Traceback, zero writes, no
    staging residue."""

    root, upstream, source, env = _failure_fixture(tmp_path)
    _make_fake_gh(tmp_path / "bin", upstream)  # healthy tip mock in every variant
    if variant == "no_gh_binary":
        # Hardening fix: the PATH is SANDBOXED to
        # an empty bin dir ONLY — the system PATH is not kept, so on a
        # gh-equipped host the pre-check verifiably fires and the checker can
        # never reach the real gh. The actual emitted reason is pinned below.
        # Minimal CONTAINED bin: only what the script itself needs
        # (dirname, pwd builtin, python3) — gh is absent everywhere.
        minbin = tmp_path / "no_gh_bin"
        minbin.mkdir(exist_ok=True)
        (minbin / "dirname").symlink_to("/usr/bin/dirname")
        (minbin / "python3").symlink_to(str(shutil.which("python3")))
        env["PATH"] = str(minbin)
    elif variant == "manifest_file_absent":
        (upstream / "MANIFEST.json").unlink()
    elif variant == "upstream_dir_absent":
        shutil.rmtree(upstream)
    env["AAID_FAKE_TIP_SHA"] = PIN
    env["AAID_FAKE_TIP_OVERRIDES"] = "{}"
    env["AAID_FAKE_PIN_OVERRIDES"] = "{}"

    args = ["--update"] if variant == "source_absent_update" else []
    if variant == "source_absent_update":
        (root / "references" / "SOURCE.md").unlink()
    before = _snapshot(root)
    result = subprocess.run(
        [BASH, str(CHECKER), *args],
        capture_output=True,
        text=True,
        env=env,
        timeout=120,
    )
    after = _snapshot(root)

    assert result.returncode != 0, f"{variant}: stdout {result.stdout!r}"
    assert result.stdout == "", f"{variant}: stdout not empty: {result.stdout!r}"
    err = result.stderr.strip()
    assert err.startswith("ERROR:"), f"{variant}: no ERROR verdict line; got {err[:200]!r}"
    if variant == "no_gh_binary":
        # Pinned pre-check reason (the honest contract: the shell-level
        # pre-check message shape, not the generic python router).
        assert err == "ERROR: gh not found on PATH", f"unexpected reason: {err!r}"
    assert "Traceback (most recent call last)" not in result.stderr, f"{variant}: raw traceback escaped to stderr"
    if variant == "source_absent_update":
        # Pinned specific-reason contract: names SOURCE.md AND is not the
        # generic routed 'unexpected <Type>' formulation (the identity path
        # inside the message cannot stand in for a domain-specific reason).
        assert "SOURCE.md" in err and "unexpected " not in err, (
            f"{variant}: reason must be SOURCE-specific; got {err!r}"
        )
    assert after == before, f"{variant}: run modified the fixture root"
    assert not list((root / ".cache").glob("staging-*")) if (root / ".cache").is_dir() else True, (
        f"{variant}: staging residue"
    )


def test_paths_with_spaces_end_to_end(tmp_path: Path) -> None:
    """Everything end to end under deliberate spaces (regardless of host):
    skill root `... skill root with spaces/`, manifest path entries with
    spaces (docs/guide notes.md, rules/rule set.mdc), fake gh's bin dir under
    `.../fake bin with space/`. Check-only over pin==tip reports UNCHANGED,
    exit 0, zero writes; --update over a divergent tip refreshes the raw
    snapshot + MANIFEST.json + SOURCE block and byte-keeps adapted files.
    All quoting must survive end to end (env PATH, staging paths, cutover)."""
    base = tmp_path / "aaid skill dir"
    root = base / "skill root with spaces"
    upstream = root / "assets" / "upstream"
    (upstream / "docs").mkdir(parents=True)
    (upstream / "rules").mkdir(parents=True)
    (root / "references").mkdir()

    raw_files = {"docs/guide notes.md": b"alpha line\n", "rules/rule set.mdc": b"beta line\n"}
    files: list[dict[str, object]] = []
    for path, data in raw_files.items():
        (upstream / path).write_bytes(data)
        files.append(
            {
                "path": path,
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
                "git_blob_sha": _git_blob_sha(data),
            }
        )
    manifest = {
        "repository": REPO,
        "default_branch": BRANCH,
        "resolved_commit": PIN,
        "generated": "2026-10-24",
        "files": files,
    }
    (upstream / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")
    adapted = "references/SKILL.md"
    sentinel = b"adapted ip sentinel stays untouched\n"
    (root / adapted).write_bytes(sentinel)

    pin_entry = f"- Integrated pin: `{PIN}` (reviewed/integrated content only; never advanced by a fetch)\n"
    source = root / "references" / "SOURCE.md"
    source.write_text(
        "# Source provenance — fixture\n\n"
        "<!-- BEGIN CHECK-STATUS: checker-maintained -->\n"
        "- Last successful check: pending\n"
        "- Fetched commit: none\n" + pin_entry + "<!-- END CHECK-STATUS -->\n"
    )

    bin_dir = tmp_path / "fake bin with space"
    bin_dir.mkdir()
    _make_fake_gh(bin_dir, upstream)
    env = dict(os.environ)
    env["PATH"] = str(bin_dir) + os.pathsep + env["PATH"]
    env["AAID_SKILL_ROOT"] = str(root)
    env["AAID_FAKE_PIN"] = PIN
    env["AAID_FAKE_ROOT"] = str(upstream)

    tip = "tip0000000000000000000000000000000000000002"

    # --- mode 1: check-only, pin == tip (content and sha) -> UNCHANGED ---
    env["AAID_FAKE_TIP_SHA"] = PIN
    env["AAID_FAKE_TIP_OVERRIDES"] = "{}"
    env["AAID_FAKE_PIN_OVERRIDES"] = "{}"
    before1 = _snapshot(root)
    r1 = subprocess.run(["bash", str(CHECKER)], capture_output=True, text=True, env=env, timeout=120)
    assert r1.returncode == 0, f"check-only stderr:\n{r1.stderr}"
    assert r1.stdout.strip() == "UNCHANGED", r1.stdout
    assert _snapshot(root) == before1, "check-only modified the spaced fixture root"

    # --- mode 2: --update, tip differs (sha and one path's content) ---
    # The fixture stays in its last good (PIN1) state on disk; the tip content
    # is served ONLY by the mock (validated decode ladder covers it).
    tip_notes = {"docs/guide notes.md": b"alpha line changed\n", "rules/rule set.mdc": raw_files["rules/rule set.mdc"]}
    env["AAID_FAKE_TIP_SHA"] = tip
    env["AAID_FAKE_TIP_OVERRIDES"] = json.dumps(
        {"docs/guide notes.md": base64.b64encode(tip_notes["docs/guide notes.md"]).decode()}
    )
    before2 = _snapshot(root)
    # NOTE (gate 6.2 nit 7): the fake gh here is invoked with an argv path
    # containing spaces, so this end-to-end pass proves the checker's own
    # quoting only. REAL `gh api` URL-encoding of spaces in contents paths is
    # UNVERIFIED by these fixtures (latent; no consumed path has spaces).
    allowed = {
        "assets/upstream/MANIFEST.json",
        "assets/upstream/docs/guide notes.md",
        "references/SOURCE.md",
    }
    r2 = subprocess.run(["bash", str(CHECKER), "--update"], capture_output=True, text=True, env=env, timeout=120)
    after2 = _snapshot(root)
    assert r2.returncode == 0, f"--update stderr:\n{r2.stderr}"
    assert r2.stdout.strip() == f"UPDATED {tip}", r2.stdout
    assert (upstream / "docs/guide notes.md").read_bytes() == tip_notes["docs/guide notes.md"]
    new_manifest = json.loads((upstream / "MANIFEST.json").read_text())
    assert new_manifest["resolved_commit"] == tip
    by_path = {e["path"]: e for e in new_manifest["files"]}
    for path, data in tip_notes.items():
        assert by_path[path]["sha256"] == hashlib.sha256(data).hexdigest()
    src = source.read_text()
    assert "Last successful check: pending" not in src
    assert f"Fetched commit: `{tip}`" in src
    assert pin_entry.rstrip("\n") in src
    assert (root / adapted).read_bytes() == sentinel, "adapted file modified"
    residue = list((root / ".cache").glob("staging-*")) if (root / ".cache").is_dir() else []
    assert not residue, "staging residue under spaces"
    # Full-root diff is EXACTLY the allowed set (no other writes anywhere).
    gone = set(before2) - set(after2)
    added = set(after2) - set(before2)
    # Union iteration so a stray NEW file (after-only key) cannot escape the diff.
    changed = {k for k in set(before2) | set(after2) if before2.get(k) != after2.get(k)}
    assert changed == allowed - added and not gone, (
        f"gone: {sorted(gone)} added: {sorted(added)} changed: {sorted(changed)}"
    )


# ---------------------------------------------------------------------------
# Unsafe manifest paths + malicious upstream content (
# "unsafe paths" discipline; upstream content is bytes-only data).
# ---------------------------------------------------------------------------

UNSAFE_PATHS = {
    "relative_escape": "../../../outside probe.md",
    "absolute_escape": "/abs/evil.md",
}

EVIL_BYTES = b"evil doc bytes\n"


def _unsafe_path_fixture(tmp_path: Path, unsafe_path: str) -> tuple[Path, Path, Path, dict[str, str]]:
    """Fixture root in last-good state with a TAMPERED local MANIFEST.json:
    the two legitimate snapshot entries are intact and self-consistent, and
    one extra entry carries the unsafe path with self-consistent hashes of
    EVIL_BYTES. Any escaping path resolution lands OUTSIDE the skill root —
    under tmp_path — which the probe assertions observe whole-tree."""
    base = tmp_path
    root = base / "skill-root"
    upstream = root / "assets" / "upstream"
    upstream.mkdir(parents=True)
    (root / "references").mkdir(exist_ok=True)

    files: list[dict[str, object]] = []
    for path, data in UPSTREAM_FILES.items():
        (upstream / path).parent.mkdir(parents=True, exist_ok=True)
        (upstream / path).write_bytes(data)
        files.append(
            {
                "path": path,
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
                "git_blob_sha": _git_blob_sha(data),
            }
        )
    files.append(
        {
            "path": unsafe_path,
            "bytes": len(EVIL_BYTES),
            "sha256": hashlib.sha256(EVIL_BYTES).hexdigest(),
            "git_blob_sha": _git_blob_sha(EVIL_BYTES),
        }
    )
    manifest = {
        "repository": REPO,
        "default_branch": BRANCH,
        "resolved_commit": PIN,
        "generated": "2026-01-31",
        "files": files,
    }
    (upstream / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")

    source = root / "references" / "SOURCE.md"
    source.write_text(
        "# Source provenance — fixture\n\n"
        "<!-- BEGIN CHECK-STATUS: checker-maintained -->\n"
        "- Last successful check: 2026-10-23\n"
        f"- Fetched commit: `{PIN}`\n"
        f"- Integrated pin: `{PIN}`\n"
        "<!-- END CHECK-STATUS -->\n"
    )
    bin_dir = base / "bin"
    bin_dir.mkdir()
    _make_fake_gh(bin_dir, upstream)
    env = dict(os.environ)
    env["PATH"] = str(bin_dir) + os.pathsep + env["PATH"]
    env["AAID_SKILL_ROOT"] = str(root)
    env["AAID_FAKE_PIN"] = PIN
    env["AAID_FAKE_ROOT"] = str(upstream)
    env["AAID_FAKE_TIP_SHA"] = PIN
    env["AAID_FAKE_TIP_OVERRIDES"] = "{}"
    env["AAID_FAKE_PIN_OVERRIDES"] = "{}"
    return base, root, upstream, source, env


@pytest.mark.parametrize("variant", list(UNSAFE_PATHS), ids=list(UNSAFE_PATHS))
def test_unsafe_manifest_paths_rejected(tmp_path: Path, variant: str) -> None:
    """The provenance policy's unsafe-path rule: a TAMPERED local manifest whose file-entry
    path escapes the snapshot dir (relative `../..` escape or an absolute
    path) must be rejected at LOAD time — before any read or write ever uses
    the path. Both modes (check-only AND --update) must exit nonzero with a
    single sanitized `ERROR:` line naming the unsafe path, and NOTHING may
    be written outside the skill root: a probe file at the escape's resolve
    target (variant a) and the whole tmp tree outside skill-root/ stay
    byte-untouched; the last-good fixture root stays byte-identical."""
    base, root, upstream, source, env = _unsafe_path_fixture(tmp_path, UNSAFE_PATHS[variant])
    # Probe: the exact file the relative variant resolves to, OUTSIDE the
    # skill root, present with matching bytes so every stage of a pre-fix run
    # could proceed (reads via the join-escape, fetch, staging write, cutover).
    probe = base / "outside probe.md"
    probe.write_bytes(EVIL_BYTES)

    # Whole-tmp probe: every byte outside the skill root must stay identical
    # across BOTH runs (relative-escape and absolute-escape writes all land
    # somewhere under base/skill-root/../ — i.e. under base, not root).
    def outside() -> dict[str, str]:
        return {k: v for k, v in _snapshot(base).items() if not k.startswith("skill-root")}

    expected = outside()  # bin/gh + probe file; nothing else may ever appear

    for args in ([], ["--update"]):
        mode = "check-only" if not args else "--update"
        before_root = _snapshot(root)
        result = subprocess.run(
            ["bash", str(CHECKER), *args],
            capture_output=True,
            text=True,
            env=env,
            timeout=120,
        )

        assert result.returncode != 0, (
            f"{variant}/{mode}: unsafe manifest path must be rejected; "
            f"stdout {result.stdout!r} stderr {result.stderr!r}"
        )
        assert result.stdout == "", f"{variant}/{mode}: stdout not empty: {result.stdout!r}"
        lines = result.stderr.splitlines()
        assert len(lines) == 1, f"{variant}/{mode}: stderr not one line: {result.stderr!r}"
        assert lines[0].startswith("ERROR:"), f"{variant}/{mode}: got {lines[0]!r}"
        assert all(ch.isprintable() or ch == " " for ch in lines[0]), (
            f"{variant}/{mode}: control chars in reason: {lines[0]!r}"
        )
        assert "unsafe manifest path" in lines[0], (
            f"{variant}/{mode}: reason must be path-containment specific: {lines[0]!r}"
        )
        assert UNSAFE_PATHS[variant] in lines[0], f"{variant}/{mode}: reason must name the unsafe path: {lines[0]!r}"
        assert "Traceback (most recent call last)" not in result.stderr
        # Zero writes: probe file untouched, the PROBE DIR (an 'outside' dir
        # sibling of the probe file) never created/appears, nothing anywhere
        # outside the skill root changed, and last-good bytes inside too.
        assert probe.read_bytes() == EVIL_BYTES, f"{variant}/{mode}: probe file written"
        assert not (base / "outside").exists(), f"{variant}/{mode}: outside dir appeared"
        assert outside() == expected, (
            f"{variant}/{mode}: writes escaped the skill root: {set(outside()) - set(expected)}"
        )
        assert _snapshot(root) == before_root, f"{variant}/{mode}: root modified despite rejection"
        assert not list((root / ".cache").glob("staging-*")) if (root / ".cache").is_dir() else True, (
            f"{variant}/{mode}: staging residue"
        )
    # The settled SOURCE block is never rewritten by a rejected run.
    assert "Last successful check: 2026-10-23" in source.read_text()


MALICIOUS_PAYLOAD = (
    b"alpha line\n"
    b"$(touch 'malicious marker one')\n"
    b"`touch 'malicious marker two'`\n"
    b"; rm -rf 'everywhere'\n"
    b"\x1b[31mCHANGED \x1b[0m UNCHANGED\n"
    b'import os; __import__("os").system("touch \'malicious marker three\'")\n'
)


def test_malicious_upstream_content_is_inert(tmp_path: Path) -> None:
    """Characterization of the bytes-only data discipline (design D6): fake gh
    serves tip == pin payloads whose bytes contain shell substitution,
    command separators, ANSI escapes with forged verdict words, and python
    exec code — and the manifest EXPECTS exactly those bytes (hashes match).
    Check-only must report UNCHANGED and --update must refresh normally;
    the payload must round-trip byte-for-byte (never interpreted), no
    'malicious marker*' file may appear anywhere in the tmp tree, adapted
    files stay intact, and only the legitimately updatable set is written."""
    root = tmp_path / "skill-root"
    upstream = root / "assets" / "upstream"
    upstream.mkdir(parents=True)
    (root / "references").mkdir(exist_ok=True)

    files: list[dict[str, object]] = []
    raw_files = {"docs/guide.md": MALICIOUS_PAYLOAD, "rules/rule.mdc": MALICIOUS_PAYLOAD}
    for path, data in raw_files.items():
        (upstream / path).parent.mkdir(parents=True, exist_ok=True)
        (upstream / path).write_bytes(data)
        files.append(
            {
                "path": path,
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
                "git_blob_sha": _git_blob_sha(data),
            }
        )
    manifest = {
        "repository": REPO,
        "default_branch": BRANCH,
        "resolved_commit": PIN,
        "generated": "2026-01-31",
        "files": files,
    }
    (upstream / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")

    adapted = root / "references" / "SKILL.md"
    adapted.write_bytes(b"adapted ip sentinel stays untouched\n")
    source = root / "references" / "SOURCE.md"
    source.write_text(
        "# Source provenance — fixture\n\n"
        "<!-- BEGIN CHECK-STATUS: checker-maintained -->\n"
        "- Last successful check: 2026-10-23\n"
        f"- Fetched commit: `{PIN}`\n"
        f"- Integrated pin: `{PIN}`\n"
        "<!-- END CHECK-STATUS -->\n"
    )
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    _make_fake_gh(bin_dir, upstream)  # serves the malicious bytes at pin AND tip
    env = dict(os.environ)
    env["PATH"] = str(bin_dir) + os.pathsep + env["PATH"]
    env["AAID_SKILL_ROOT"] = str(root)
    env["AAID_FAKE_PIN"] = PIN
    env["AAID_FAKE_ROOT"] = str(upstream)
    env["AAID_FAKE_TIP_SHA"] = PIN
    env["AAID_FAKE_TIP_OVERRIDES"] = "{}"
    env["AAID_FAKE_PIN_OVERRIDES"] = "{}"

    def outside() -> dict[str, str]:
        return {
            k: v for k, v in _snapshot(tmp_path).items() if not k.startswith("skill-root")
        }  # markdown-in-heredoc guard: fixture root is 'skill-root', tmp base

    before_out = outside()

    # Mode 1: check-only, pin == tip -> UNCHANGED, zero writes, bytes inert.
    r1 = subprocess.run(["bash", str(CHECKER)], capture_output=True, text=True, env=env, timeout=120)
    assert r1.returncode == 0, f"check-only stderr:\n{r1.stderr}"
    assert r1.stdout.strip() == "UNCHANGED", f"check-only stdout: {r1.stdout!r}"

    # Mode 2: authorized --update -> normal refresh verdict, bytes-only cutover.
    allowed = {
        "assets/upstream/MANIFEST.json",
        "references/SOURCE.md",
    }
    before2 = _snapshot(root)
    r2 = subprocess.run(["bash", str(CHECKER), "--update"], capture_output=True, text=True, env=env, timeout=120)
    assert r2.returncode == 0, f"--update stderr:\n{r2.stderr}"
    assert r2.stdout.strip() == f"UPDATED {PIN}", f"--update stdout: {r2.stdout!r}"

    # Payload round-trips byte-for-byte in BOTH files (never re-interpreted),
    # including control bytes and the ANSI-escape spoof attempt.
    for path, data in raw_files.items():
        assert (upstream / path).read_bytes() == data, f"{path} bytes altered"
    new_manifest = json.loads((upstream / "MANIFEST.json").read_text())
    assert new_manifest["resolved_commit"] == PIN
    for e in new_manifest["files"]:
        data = raw_files[e["path"]]
        assert e["sha256"] == hashlib.sha256(data).hexdigest()
        assert e["git_blob_sha"] == _git_blob_sha(data)

    # Adapted files intact; no staging residue.
    assert adapted.read_bytes() == b"adapted ip sentinel stays untouched\n"
    src_after = source.read_text()
    assert "Last successful check:" in src_after  # refresh still happened
    assert "Last successful check: pending" not in src_after
    assert f"Fetched commit: `{PIN}`" in src_after
    residue = list((root / ".cache").glob("staging-*")) if (root / ".cache").is_dir() else []
    assert not residue, "staging residue"

    # No 'malicious marker*' creation anywhere (shell/code payloads inert).
    for bad in tmp_path.rglob("*malicious marker*"):
        raise AssertionError(f"payload executed?: {bad}")
    for f2 in list(tmp_path.rglob("marker")) + list(tmp_path.rglob("everywhere")):
        raise AssertionError(f"payload executed?: {f2}")
    assert outside() == before_out, f"malicious run wrote outside the skill root: {set(outside()) - set(before_out)}"
    # Whole-root diff is exactly the allowed update set.
    after2 = _snapshot(root)
    gone = set(before2) - set(after2)
    added = set(after2) - set(before2)
    changed = {k for k in set(before2) | set(after2) if before2.get(k) != after2.get(k)}
    assert changed == allowed - gone, f"changed: {sorted(changed)} gone: {sorted(gone)} added: {sorted(added)}"


# ---------------------------------------------------------------------------
# Real-run regression pins. The first real upstream run exposed
# three bugs no fixture caught because tests always set AAID_SKILL_ROOT and
# use bare owner/repo manifests. This test pins the fixed behavior post-hoc
# (DISCLOSED: CHARACTERIZATION pins, fixes already applied before the test).
# ---------------------------------------------------------------------------

# Real-world manifest shape: full clone-style URL, not bare owner/repo.
URL_REPO = "https://github.com/dawid-dahl-umain/augmented-ai-development"
NORMALIZED_REPO = "dawid-dahl-umain/augmented-ai-development"

# Long enough that its base64 (120 chars) must wrap at GitHub's 60-char lines.
GUIDE_BYTES = b"alpha line\n" * 8


def _make_real_shape_gh(bin_dir: Path, fixture_upstream: Path) -> None:
    """Fake `gh` for the real-world-shape regression pins. Serves ONLY the
    normalized repo path (repos/dawid-dahl-umain/augmented-ai-development/...);
    invocations for any other endpoint exit 1. Every invocation is logged to
    AAID_FAKE_LOG so the test can assert the checker's gh api paths are the
    NORMALIZED repo. Base64 content is newline-wrapped every 60 chars the
    way the real GitHub contents API serves it."""
    gh = bin_dir / "gh"
    gh.write_text(
        "#!/usr/bin/env python3\n"
        "import base64, hashlib, json, os, sys\n"
        "log = open(os.environ['AAID_FAKE_LOG'], 'a')\n"
        "log.write('CALL ' + ' '.join(sys.argv[1:]) + '\\n')\n"
        "log.close()\n"
        "pin = os.environ['AAID_FAKE_PIN']\n"
        "root = os.environ['AAID_FAKE_ROOT']\n"
        'repo = "repos/dawid-dahl-umain/augmented-ai-development/"\n'
        "args = sys.argv[1:]\n"
        "if any(a.startswith(repo + 'commits/') for a in args):\n"
        "    print(json.dumps({'sha': pin, 'commit': {}}))\n"
        "    sys.exit(0)\n"
        "path = None\n"
        "ref = None\n"
        "for a in args:\n"
        "    if a.startswith(repo + 'contents/'):\n"
        "        path = a[len(repo + 'contents/'):]\n"
        "    elif a.startswith('ref='):\n"
        "        ref = a[4:]\n"
        "if path is None or ref != pin:\n"
        "    sys.exit(1)\n"
        "data = open(os.path.join(root, path), 'rb').read()\n"
        "b64 = base64.b64encode(data).decode()\n"
        "wrapped = '\\n'.join(b64[i:i+60] for i in range(0, len(b64), 60))\n"
        "print(json.dumps({\n"
        "    'content': wrapped,\n"
        "    'encoding': 'base64',\n"
        "    'size': len(data),\n"
        "    'sha': hashlib.sha1(b'blob %d\\0' % len(data) + data).hexdigest(),\n"
        "}))\n"
    )
    gh.chmod(0o755)


def _real_shape_fixture(tmp_path: Path) -> tuple[Path, Path, Path, dict[str, str]]:
    """Skill-root fixture shaped like the REAL repository: manifest
    `repository` is the full https URL, snapshot content long enough to wrap,
    SOURCE.md check-status block present, integrated pin == tip -> UNCHANGED."""
    root = tmp_path / "skill-root"
    upstream = root / "assets" / "upstream"
    upstream.mkdir(parents=True)
    (root / "references").mkdir()

    raw_files = {"docs/guide.md": GUIDE_BYTES, "rules/rule.mdc": b"beta line\n"}
    files: list[dict[str, object]] = []
    for path, data in raw_files.items():
        (upstream / path).parent.mkdir(parents=True, exist_ok=True)
        (upstream / path).write_bytes(data)
        files.append(
            {
                "path": path,
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
                "git_blob_sha": _git_blob_sha(data),
            }
        )
    manifest = {
        "repository": URL_REPO,
        "default_branch": BRANCH,
        "resolved_commit": PIN,
        "generated": "2026-01-31",
        "files": files,
    }
    (upstream / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")
    (upstream / "README.md").write_bytes(b"protected readme\n")

    source = root / "references" / "SOURCE.md"
    source.write_text(
        "# Source provenance — fixture\n\n"
        "<!-- BEGIN CHECK-STATUS: checker-maintained -->\n"
        "- Last successful check: 2026-10-23\n"
        f"- Fetched commit: `{PIN}`\n"
        f"- Integrated pin: `{PIN}`\n"
        "<!-- END CHECK-STATUS -->\n"
    )

    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    _make_real_shape_gh(bin_dir, upstream)
    log = tmp_path / "gh_calls.log"
    log.write_text("")

    env = dict(os.environ)
    env["PATH"] = str(bin_dir) + os.pathsep + env["PATH"]
    env["AAID_SKILL_ROOT"] = str(root)
    env["AAID_FAKE_PIN"] = PIN
    env["AAID_FAKE_ROOT"] = str(upstream)
    env["AAID_FAKE_LOG"] = str(log)
    return root, bin_dir, log, env


REAL_SHAPES = {
    "url_repository": "manifest repository is a full https URL",
    "newline_base64": "fake gh serves GitHub-style 60-char newline-wrapped base64",
    "default_root": "run with no AAID_SKILL_ROOT; checker copied into root/scripts resolves its own ../",
}


@pytest.mark.parametrize("shape", list(REAL_SHAPES), ids=list(REAL_SHAPES))
def test_real_world_shape_regressions(tmp_path: Path, shape: str) -> None:
    """CHARACTERIZATION (post-hoc pins of the real-run fixes). Check-only
    over a pin==tip fixture shaped like the real repository must report
    UNCHANGED, exit 0, and write nothing. (a) a URL-form manifest repository
    is normalized for gh api (every logged call hits
    repos/dawid-dahl-umain/augmented-ai-development/ and none carries the raw
    URL); (b) GitHub-style newline-wrapped base64 decodes correctly; (c) with
    NO AAID_SKILL_ROOT, the checker copied into <root>/scripts/ resolves its
    own location (default `$_here/..`) to the fixture root."""
    root, bin_dir, log, env = _real_shape_fixture(tmp_path)
    checker = CHECKER
    if shape == "default_root":
        scripts_dir = root / "scripts"
        scripts_dir.mkdir()
        checker = scripts_dir / "check-upstream.sh"
        shutil.copyfile(CHECKER, checker)
        # Sandboxed PATH: the checker must find gh AND (via its shebang-spawned
        # python3) resolve python3 + dirname inside the contained bin only.
        env["PATH"] = str(bin_dir)
        env.pop("AAID_SKILL_ROOT", None)
        assert shutil.which("python3"), "host python3 required for symlink"
        (bin_dir / "python3").symlink_to(shutil.which("python3"))
        (bin_dir / "dirname").symlink_to(shutil.which("dirname"))

    before = _snapshot(root)
    result = subprocess.run([BASH, str(checker)], capture_output=True, text=True, env=env, timeout=120)

    assert result.returncode == 0, f"{shape}: stderr:\n{result.stderr}"
    assert result.stdout.strip() == "UNCHANGED", f"{shape}: stdout {result.stdout!r}"

    calls = log.read_text().splitlines()
    repo_calls = [c for c in calls if "repos/" in c]
    assert repo_calls, f"{shape}: no gh api calls logged"
    for call in repo_calls:
        # (a) normalized owner/repo path, never the raw URL form.
        assert "repos/dawid-dahl-umain/augmented-ai-development/" in call, (
            f"{shape}: unnormalized gh api call: {call!r}"
        )
        assert "https://" not in call and "http://" not in call, f"{shape}: raw URL reached gh api: {call!r}"
    joined = "\n".join(repo_calls)
    assert f"repos/{NORMALIZED_REPO}/commits/main" in joined, f"{shape}: no tip call: {joined!r}"
    for path in ("docs/guide.md", "rules/rule.mdc"):
        assert f"repos/{NORMALIZED_REPO}/contents/{path}" in joined, f"{shape}: contents call missing for {path}"

    # Zero writes: check-only leaves the whole fixture root byte-identical.
    assert _snapshot(root) == before, f"{shape}: root written during check-only"
    assert not (root / ".cache").exists(), f"{shape}: .cache residue"


# ---------------------------------------------------------------------------
# Adversarial-hardening regression tests.
# Each test names the finding it pins. Behavior-preserving for the 33 legacy
# semantics except where disclosed in the hardening review.
# ---------------------------------------------------------------------------


def _harden_fixture(tmp_path: Path) -> tuple[Path, Path, Path, Path, dict[str, str]]:
    """Last-good fixture root (like _failure_fixture) + healthy fake gh with
    the tip/override env pre-set. Returns (root, upstream, source, bin_dir,
    env). Tests mutate `gh` or the fixture afterwards."""
    root, upstream, source, env = _failure_fixture(tmp_path)
    bin_dir = tmp_path / "bin"
    _make_fake_gh(bin_dir, upstream)
    env["AAID_FAKE_TIP_SHA"] = PIN
    env["AAID_FAKE_TIP_OVERRIDES"] = "{}"
    env["AAID_FAKE_PIN_OVERRIDES"] = "{}"
    return root, upstream, source, bin_dir, env


def _run(root: Path, env: dict[str, str], *args: str) -> subprocess.CompletedProcess:
    return subprocess.run([BASH, str(CHECKER), *args], capture_output=True, text=True, env=env, timeout=120)


# --- malicious remote tip metadata must never reach output --------------


def _make_tip_sha_gh(bin_dir: Path, upstream: Path, tip_sha: str) -> None:
    """Fake `gh` answering the commits call with an ATTACKER-CONTROLLED sha and
    healthy base64 contents responses (pin == local bytes)."""
    gh = bin_dir / "gh"
    gh.write_text(
        "#!/usr/bin/env python3\n"
        "import base64, hashlib, json, os, sys\n"
        f"tip_sha = {tip_sha!r}\n"
        "args = sys.argv[1:]\n"
        'if any("repos/example/ex/commits/main" in a for a in args):\n'
        '    print(json.dumps({"sha": tip_sha}))\n'
        "    sys.exit(0)\n"
        "path = None\n"
        "ref = None\n"
        "for a in args:\n"
        '    if "repos/example/ex/contents/" in a:\n'
        '        path = a.split("repos/example/ex/contents/", 1)[1]\n'
        '    elif a.startswith("ref="):\n'
        "        ref = a[4:]\n"
        "data = open(os.path.join(os.environ['AAID_FAKE_ROOT'], path), 'rb').read()\n"
        "print(json.dumps({\n"
        "    'content': base64.b64encode(data).decode(),\n"
        "    'encoding': 'base64',\n"
        "    'size': len(data),\n"
        "    'sha': hashlib.sha1(b'blob %d\\0' % len(data) + data).hexdigest(),\n"
        "}))\n"
    )
    gh.chmod(0o755)


def test_i1_malicious_tip_metadata_rejected_on_success_paths(tmp_path: Path) -> None:
    """(check-only): remote tip metadata containing a newline, a forged
    verdict line and an ANSI escape — served on an otherwise HEALTHY transport
    path — must yield ERROR, never a verdict line, and no writes (SOURCE.md
    block untouched, no .cache residue). Pinned contract change disclosed:
    such metadata previously produced a verdict; now it is an ERROR."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    malicious_tip = "tip\nUNCHANGED\n\x1b[31m"
    _make_tip_sha_gh(bin_dir, upstream, malicious_tip)

    before = _snapshot(root)
    result = _run(root, env)

    assert result.returncode != 0, f"stdout {result.stdout!r}"
    # No forged verdict: the only stdout is nothing at all.
    assert result.stdout == "", f"stdout: {result.stdout!r}"
    lines = result.stderr.splitlines()
    assert len(lines) == 1, f"stderr not single-line: {result.stderr!r}"
    assert lines[0].startswith("ERROR:"), result.stderr
    assert not lines[0].endswith("UNCHANGED"), f"spoof survived: {lines[0]!r}"
    assert "\x1b" not in lines[0], f"ANSI escape reached output: {lines[0]!r}"
    assert _snapshot(root) == before, "run wrote to the fixture root"
    assert source.read_text().count("Integrated pin") == 1, "SOURCE block rewritten"
    assert not (root / ".cache").exists(), "check-only created .cache residue"


def test_i1_malicious_tip_metadata_update_rejected(tmp_path: Path) -> None:
    """(--update): the same malicious tip sha must fail BEFORE any
    staging/cutover: ERROR, last-good root byte-identical, no staging, and the
    lock removed (a failed run cannot wedge .cache/update.lock)."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    _make_tip_sha_gh(bin_dir, upstream, "tip\nUPDATED\n")
    before = _snapshot(root)
    result = _run(root, env, "--update")
    assert result.returncode != 0 and result.stdout == ""
    assert "ERROR:" in result.stderr
    assert "UPDATED" not in result.stdout and result.stdout == ""
    assert _snapshot(root) == before, "failed --update wrote to the fixture root"
    assert not (root / ".cache" / "update.lock").exists(), "lock wedged by failed run"


# --- manifest path canonicalization; staging never aliases the live tree ---

ALIAS_PATH = "../../assets/upstream/docs/guide.md"


def _alias_fixture(tmp_path: Path):
    """Fixture where the manifest carries ONLY the alias spelling of
    docs/guide.md (self-consistent hashes of its real local bytes — the alias
    resolves INSIDE upstream, so pre-analysis containment passes it) plus the
    normal rules entry. Returns (root, upstream, source, bin_dir, env) with
    the tip divergent for docs/guide.md and a SECOND-path failure (rules ->
    HTTP 500) to exercise the staged-fetch-failure path."""
    root = tmp_path / "skill-root"
    upstream = root / "assets" / "upstream"
    (upstream / "docs").mkdir(parents=True)
    (upstream / "rules").mkdir(parents=True)
    (root / "references").mkdir()
    guidetip = b"alpha line changed\n"
    raw = {"docs/guide.md": b"alpha line\n", "rules/rule.mdc": b"beta line\n"}
    files = []
    for path, data in raw.items():
        (upstream / path).write_bytes(data)
        entry = {
            "path": path,
            "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
            "git_blob_sha": _git_blob_sha(data),
        }
        if path == "docs/guide.md":
            entry["path"] = ALIAS_PATH
        files.append(entry)
    (upstream / "MANIFEST.json").write_text(
        json.dumps(
            {
                "repository": REPO,
                "default_branch": BRANCH,
                "resolved_commit": PIN,
                "generated": "2026-01-31",
                "files": files,
            },
            indent=2,
        )
        + "\n"
    )
    source = root / "references" / "SOURCE.md"
    source.write_text(
        "# Source provenance — fixture\n\n"
        "<!-- BEGIN CHECK-STATUS: checker-maintained -->\n"
        "- Last successful check: 2026-10-23\n"
        f"- Fetched commit: `{PIN}`\n"
        f"- Integrated pin: `{PIN}`\n"
        "<!-- END CHECK-STATUS -->\n"
    )
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    gh = bin_dir / "gh"
    gh.write_text(
        "#!/usr/bin/env python3\n"
        "import base64, hashlib, json, os, sys\n"
        "args = sys.argv[1:]\n"
        'if any("repos/example/ex/commits/main" in a for a in args):\n'
        '    print(json.dumps({"sha": os.environ["AAID_FAKE_TIP_SHA"]}))\n'
        "    sys.exit(0)\n"
        "path = None\n"
        "for a in args:\n"
        '    if "repos/example/ex/contents/" in a:\n'
        '        path = a.split("repos/example/ex/contents/", 1)[1]\n'
        'if path == "rules/rule.mdc" and os.environ.get("AAID_FAIL_ON_RULES") == "1":\n'
        '    sys.stderr.write("gh: HTTP 500 (network)\\n")\n'
        "    sys.exit(1)\n"
        'if path == "docs/guide.md" and os.environ.get("AAID_TIP_GUIDE_B64") and os.environ["AAID_FAKE_TIP_SHA"] != os.environ["AAID_FAKE_PIN"]:\n'
        '    data = base64.b64decode(os.environ["AAID_TIP_GUIDE_B64"])\n'
        "else:\n"
        '    data = open(os.path.join(os.environ["AAID_FAKE_ROOT"], path), "rb").read()\n'
        "print(json.dumps({\n"
        "    'content': base64.b64encode(data).decode(),\n"
        "    'encoding': 'base64',\n"
        "    'size': len(data),\n"
        "    'sha': hashlib.sha1(b'blob %d\\0' % len(data) + data).hexdigest(),\n"
        "}))\n"
    )
    gh.chmod(0o755)
    env = dict(os.environ)
    env["PATH"] = str(bin_dir) + os.pathsep + env["PATH"]
    env["AAID_SKILL_ROOT"] = str(root)
    env["AAID_FAKE_PIN"] = PIN
    env["AAID_FAKE_ROOT"] = str(upstream)
    env["AAID_FAKE_TIP_SHA"] = PIN
    env["AAID_TIP_GUIDE_B64"] = base64.b64encode(guidetip).decode()
    env["AAID_FAIL_ON_RULES"] = "0"
    return root, upstream, source, bin_dir, env


def test_i2_alias_escape_cannot_reach_live_tree(tmp_path: Path) -> None:
    """(staged-fetch failure): manifest entry
    `../../assets/upstream/docs/guide.md` (self-consistent hashes, resolves
    inside upstream) with a SECOND-path fetch failure. The staging write for
    the alias path must land inside the PER-INVOCATION staging dir only — the
    live docs/guide.md bytes must be identical after the run, staging is
    cleaned (fetch-phase pinned semantics), nothing appears outside the root.
    Pre-fix behavior would have written the live file via the alias."""
    root, upstream, source, bin_dir, env = _alias_fixture(tmp_path)
    env["AAID_FAIL_ON_RULES"] = "1"
    env["AAID_FAKE_TIP_SHA"] = "tip0000000000000000000000000000000000000002"
    before = _snapshot(root)
    result = _run(root, env, "--update")

    assert result.returncode != 0 and result.stdout == ""
    assert "ERROR:" in result.stderr.splitlines()[0], result.stderr
    assert not list((root / ".cache").glob("staging-*")) if (root / ".cache").is_dir() else True, (
        "staging residue (fetch phase)"
    )
    live = root / "assets" / "upstream" / "docs/guide.md"
    assert live.read_bytes() == b"alpha line\n", "ALIAS PATH REACHED THE LIVE TREE"
    assert (upstream / "rules/rule.mdc").read_bytes() == b"beta line\n"
    assert _snapshot(root) == before, "run modified the last-good fixture root"

    # Check-only over the same alias manifest must also behave (fetch by
    # CANONICAL path); restore the healthy transport for this leg.
    env["AAID_FAIL_ON_RULES"] = "0"
    r2 = _run(root, env)
    assert r2.returncode == 0, f"check-only stderr:\n{r2.stderr}"
    assert r2.stdout.strip() == "UNCHANGED", r2.stdout
    assert live.read_bytes() == b"alpha line\n", "check-only wrote the live tree"


def test_i2_alias_canonical_form_used_end_to_end(tmp_path: Path) -> None:
    """(successful --update): with the same alias manifest and a clean
    tip, the update succeeds with `UPDATED`; the cutover writes the LIVE file
    via its canonical path; the regenerated manifest stores CANONICAL paths
    (the alias spelling is gone); no staging residue; the tmp tree outside
    skill-root is untouched (no accidental root-level ../writes)."""
    root, upstream, source, bin_dir, env = _alias_fixture(tmp_path)
    tip = "tip0000000000000000000000000000000000000002"
    env["AAID_FAKE_TIP_SHA"] = tip
    outside_before = {k: v for k, v in _snapshot(tmp_path).items() if not k.startswith("skill-root")}
    before = _snapshot(root)
    result = _run(root, env, "--update")

    assert result.returncode == 0, f"--update stderr:\n{result.stderr}"
    assert result.stdout.strip() == f"UPDATED {tip}", result.stdout
    assert (upstream / "docs/guide.md").read_bytes() == b"alpha line changed\n"
    new_manifest = json.loads((upstream / "MANIFEST.json").read_text())
    assert {e["path"] for e in new_manifest["files"]} == {
        "docs/guide.md",
        "rules/rule.mdc",  # canonical, alias spelling gone
    }
    assert new_manifest["resolved_commit"] == tip
    assert not list((root / ".cache").glob("staging-*")) if (root / ".cache").is_dir() else True, "staging residue"
    allowed = {
        "assets/upstream/MANIFEST.json",
        "assets/upstream/docs/guide.md",
        "references/SOURCE.md",
    }
    changed = {k for k in set(before) | set(_snapshot(root)) if before.get(k) != _snapshot(root).get(k)}
    assert changed == allowed, f"changed: {sorted(changed)}"
    outside_after = {k: v for k, v in _snapshot(tmp_path).items() if not k.startswith("skill-root")}
    assert outside_after == outside_before, "write escaped the skill root"


@pytest.mark.parametrize("reserved", ["README.md", "MANIFEST.json"])
def test_i2_reserved_policy_paths_rejected(tmp_path: Path, reserved: str) -> None:
    """(reserved paths): a tampered manifest entry whose CANONICAL
    path is a local policy file at the upstream root (README.md or
    MANIFEST.json itself) must be rejected in BOTH modes — never staged,
    fetched, or cutover-written over the local policy bytes."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    manifest = json.loads((upstream / "MANIFEST.json").read_text())
    data = EVIL_BYTES
    readme = b"reserved local policy readme sentinel\n"
    (upstream / "README.md").write_bytes(readme)
    manifest["files"].append(
        {
            "path": reserved,
            "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
            "git_blob_sha": _git_blob_sha(data),
        }
    )
    (upstream / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")
    for args in ([], ["--update"]):
        mode = "check-only" if not args else "--update"
        readme = (upstream / "README.md").read_bytes()
        result = _run(root, env, *args)
        assert result.returncode != 0, f"{mode}: stdout {result.stdout!r}"
        assert result.stdout == "", f"{mode}: stdout {result.stdout!r}"
        assert "ERROR:" in result.stderr, result.stderr
        assert "reserved" in result.stderr, f"{mode}: reason not reserved-specific: {result.stderr!r}"
        assert (upstream / "README.md").read_bytes() == readme, f"{mode}: README overwritten"
        if reserved == "MANIFEST.json":
            assert json.loads((upstream / "MANIFEST.json").read_text())["resolved_commit"] == PIN, (
                f"{mode}: MANIFEST clobbered"
            )


# --- detectable interruption + retained staging on cutover failure ---


def test_i3_mid_cutover_state_is_detectable_error(tmp_path: Path) -> None:
    """(corruption detectability): simulate death between cutover
    steps — raw files advanced to tip bytes while MANIFEST.json keeps the
    old pin hashes. The next check-only run must report ERROR (local
    snapshot mismatch), NEVER UNCHANGED, with no writes."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    tip_guide = b"alpha line changed\n"
    (upstream / "docs/guide.md").write_bytes(tip_guide)  # mid-cutover state
    env["AAID_FAKE_TIP_SHA"] = "tip0000000000000000000000000000000000000002"
    before = _snapshot(root)
    result = _run(root, env)

    assert result.returncode != 0 and result.stdout == ""
    assert "ERROR:" in result.stderr.splitlines()[0], result.stderr
    assert "local snapshot mismatch" in result.stderr, result.stderr
    assert _snapshot(root) == before, "the erroring run modified the fixture root"


def test_i3_cutover_failure_retains_complete_staging(tmp_path: Path) -> None:
    """(cutover failure): SOURCE.md made read-only during --update so
    the final write fails. Must yield ERROR (staging retained noted in the
    reason), NOT delete staging: the per-invocation staging dir must still
    hold the COMPLETE fetched tip snapshot (raw files + MANIFEST.json). The
    live manifest + raw files ARE advanced (write order raw -> MANIFEST ->
    SOURCE; the run failed on the LAST write), while the SOURCE block keeps
    its old state — the detectable window-(iii) partial state.
    Pinned contract change disclosed: previously the failed run deleted the
    only complete fetched copy."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    tip = "tip0000000000000000000000000000000000000002"
    guide_tip = b"alpha line changed\n"
    env["AAID_FAKE_TIP_SHA"] = tip
    env["AAID_FAKE_TIP_OVERRIDES"] = json.dumps({"docs/guide.md": base64.b64encode(guide_tip).decode()})
    source.chmod(0o444)
    try:
        result = _run(root, env, "--update")
    finally:
        source.chmod(0o644)

    assert result.returncode != 0 and result.stdout == ""
    err = result.stderr.strip()
    assert err.startswith("ERROR:"), err
    assert "staging retained" in err, f"cutover failure without retention note: {err!r}"
    # staging still exists, uniquely this run's, holding the complete set
    staging_dirs = list((root / ".cache").glob("staging-*") if (root / ".cache").is_dir() else [])
    assert len(staging_dirs) == 1, f"expected the retained staging dir: {staging_dirs}"
    staging = staging_dirs[0]
    assert (staging / "docs/guide.md").read_bytes() == guide_tip
    assert (staging / "rules/rule.mdc").read_bytes() == UPSTREAM_FILES["rules/rule.mdc"]
    staged_manifest = json.loads((staging / "MANIFEST.json").read_text())
    assert staged_manifest["resolved_commit"] == tip
    # Write order raw -> MANIFEST -> SOURCE: the run failed on the LAST
    # cutover write, so raw files + manifest hold tip bytes but SOURCE keeps
    # the old block (the detectable mismatch state), staging intact.
    assert (upstream / "docs/guide.md").read_bytes() == guide_tip
    assert json.loads((upstream / "MANIFEST.json").read_text())["resolved_commit"] == tip
    assert f"- Fetched commit: `{PIN}`" in source.read_text(), "SOURCE rewritten despite failure"
    assert not (root / ".cache" / "update.lock").exists(), "lock wedged after failed cutover"


# --- per-invocation staging + exclusive update lock ------------------


def test_i4_third_lock_blocks_update(tmp_path: Path) -> None:
    """(lock): a pre-existing .cache/update.lock (another updater or
    a stale lock) must make --update ERROR 'another update...' without
    staging anything or taking over the state file directory."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    lock_dir = root / ".cache"
    lock_dir.mkdir()
    (lock_dir / "update.lock").write_bytes(b"owner: other\n")
    before = _snapshot(root)
    result = _run(root, env, "--update")

    assert result.returncode != 0 and result.stdout == ""
    assert "ERROR:" in result.stderr, result.stderr
    assert "another update" in result.stderr, result.stderr
    assert (lock_dir / "update.lock").exists(), "foreign/own lock deleted by non-holder"
    assert not list(lock_dir.glob("staging-*")), "staging created despite lock"
    assert _snapshot(root) == before, "locked run modified the fixture root"


def test_i4_failing_check_only_spares_foreign_staging(tmp_path: Path) -> None:
    """(shared-staging cleanup): pre-create a FOREIGN staging dir (a
    concurrent updater's) with a sentinel, then run a FAILING check-only. It
    owns no staging: the sentinel dir must survive intact byte-for-byte."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    foreign = root / ".cache" / "staging-99999-9999999999999"
    foreign.mkdir(parents=True)
    sentinel = foreign / "docs"
    sentinel.mkdir()
    (sentinel / "guide.md").write_bytes(b"foreign staged bytes\n")
    _make_failing_gh(bin_dir, 1, "gh: HTTP 500 (network)")

    result = _run(root, env)
    assert result.returncode != 0 and result.stdout == ""
    assert "ERROR:" in result.stderr, result.stderr
    assert foreign.is_dir(), "failing check-only removed a foreign staging dir"
    assert (sentinel / "guide.md").read_bytes() == b"foreign staged bytes\n", "sentinel disturbed"


# --- check-only validates the check-status block ---------------------

BLOCK_AFFIX = "<!-- BEGIN CHECK-STATUS: checker-maintained -->\n- Last successful check: 2026-10-23\n-Fetched commit\n"


def _i5_fixture(tmp_path: Path, mutation: str):
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    if mutation == "pin_removed":
        source.write_text(
            "# Source provenance — fixture\n\n"
            "<!-- BEGIN CHECK-STATUS: checker-maintained -->\n"
            "- Last successful check: 2026-10-23\n"
            f"- Fetched commit: `{PIN}`\n"
            "<!-- END CHECK-STATUS -->\n"
        )
    elif mutation == "end_removed":
        source.write_text(
            "# Source provenance — fixture\n\n"
            "<!-- BEGIN CHECK-STATUS: checker-maintained -->\n"
            "- Last successful check: 2026-10-23\n"
            f"- Fetched commit: `{PIN}`\n"
            f"- Integrated pin: `{PIN}`\n"
        )
    elif mutation == "absent_source":
        source.unlink()
    return root, upstream, source, env


I5_MUTATIONS = ("pin_removed", "end_removed", "absent_source")


@pytest.mark.parametrize("mutation", I5_MUTATIONS, ids=I5_MUTATIONS)
def test_i5_corrupted_block_fallback_contract(tmp_path: Path, mutation: str) -> None:
    """(corrupt check-status block): (a) SOURCE block with BEGIN marker but the Integrated-pin
    line removed, (b) truncated block with no END marker, (c) ENTIRELY ABSENT
    SOURCE.md — check-only must ERROR 'missing provenance'/'malformed
    check-status block', never silently fall back to the manifest
    resolved_commit (which would read pin==tip and report a false UNCHANGED
    after an interrupted cutover, laundering fetched-but-unreviewed content
    as integrated — closure-gate 6.3 finding 1). Pinned contract change
    disclosed: absent SOURCE.md previously degraded to UNCHANGED; all three
    corruption states now fail closed. Only a genuine first-run fixture
    WITHOUT any provenance residue (no references/ dir, no .cache/) keeps the
    manifest-pin fallback (pinned by test_check_only_unchanged)."""
    root, upstream, source, env = _i5_fixture(tmp_path, mutation)
    before = _snapshot(root)
    result = _run(root, env)

    if mutation == "absent_source":
        assert result.returncode != 0 and result.stdout == "", f"stdout {result.stdout!r} stderr {result.stderr!r}"
        assert "provenance record missing" in result.stderr, result.stderr
        assert "integrated pin after human review" in result.stderr, result.stderr
    else:
        assert result.returncode != 0 and result.stdout == "", (
            f"{mutation}: stdout {result.stdout!r} stderr {result.stderr!r}"
        )
        assert "ERROR: malformed check-status block" in result.stderr, result.stderr
    assert _snapshot(root) == before, "run modified the fixture root"


def test_absent_source_after_fetched_not_laundered(tmp_path: Path) -> None:
    """(closure-gate 6.3 finding 1, direct scenario): a refresh FETCHED changed
    content (manifest advanced to tip2, local snapshot coherent at tip2,
    SOURCE block still pin1) and THEN references/SOURCE.md was removed.
    Check-only must ERROR — never UNCHANGED. The pre-fix checker fell back to
    the manifest resolved_commit (== tip2) and reported the fetched state as
    UNCHANGED (tip-vs-itself), laundering unreviewed content as integrated."""
    pin1 = PIN
    tip2 = "tip200000000000000000000000000000000000000002"
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    # Advance the fixture to the fetched-but-unreviewed state WITHOUT running
    # --update: tip2 bytes on disk, manifest resolved at tip2, OLD pin in a
    # valid block — then remove the provenance record entirely.
    tip2_files = {"docs/guide.md": b"alpha line changed\n", "rules/rule.mdc": UPSTREAM_FILES["rules/rule.mdc"]}
    manifest = json.loads((upstream / "MANIFEST.json").read_text())
    manifest["resolved_commit"] = tip2
    manifest["files"] = [
        {
            "path": path,
            "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
            "git_blob_sha": _git_blob_sha(data),
        }
        for path, data in tip2_files.items()
    ]
    (upstream / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")
    (upstream / "docs/guide.md").write_bytes(tip2_files["docs/guide.md"])
    source.write_text(
        "# Source provenance — fixture\n\n"
        "<!-- BEGIN CHECK-STATUS: checker-maintained -->\n"
        "- Last successful check: " + datetime.date.today().isoformat() + "\n"
        f"- Fetched commit: `{tip2}`\n"
        f"- Integrated pin: `{pin1}`\n"
        "<!-- END CHECK-STATUS -->\n"
    )
    env["AAID_FAKE_TIP_SHA"] = tip2
    # gh serves tip2 content at the tip ref; pre-removal, tip-vs-pin1 was
    # CHANGED (pin override), so the fixture was genuinely unreviewed.
    env["AAID_FAKE_PIN_OVERRIDES"] = json.dumps(
        {"docs/guide.md": base64.b64encode(UPSTREAM_FILES["docs/guide.md"]).decode()}
    )
    source.unlink()  # the laundering precondition: provenance file removed

    before = _snapshot(root)
    result = _run(root, env)

    assert result.returncode != 0 and result.stdout == "", (
        f"launched state must NOT report a verdict: stdout {result.stdout!r} stderr {result.stderr!r}"
    )
    assert result.stdout.strip() != "UNCHANGED", "fetched state laundered as UNCHANGED"
    assert "provenance record missing" in result.stderr, result.stderr
    assert "re-record the integrated pin after human review" in result.stderr, result.stderr
    assert _snapshot(root) == before, "the erroring run modified the fixture root"


# ---------------------------------------------------------------------------
# Adversarial-hardening round 2: re-review fixes.
# ---------------------------------------------------------------------------

RESERVED_SPELLINGS = ("readme.md", "Manifest.json", "Readme.MD")


@pytest.mark.parametrize("spelling", RESERVED_SPELLINGS, ids=RESERVED_SPELLINGS)
def test_reserved_root_case_insensitive(tmp_path: Path, spelling: str) -> None:
    """(reserved paths, root-level casefold): root-level reserved paths are rejected
    CASE-INSENSITIVELY — a tampered manifest entry spelled `readme.md`,
    `Manifest.json` or `Readme.MD` addresses the local README.md /
    MANIFEST.json at the upstream root on case-insensitive filesystems
    (macOS) and must be an ERROR in BOTH modes, never fetched or staged.
    CHOICE (documented in the checker): the reserved concern is overwriting
    local POLICY at the upstream ROOT, so only root-level casefolded
    collisions are rejected — a nested `docs/readme.md` stays allowed
    (pinned by test_nested_readme_allowed)."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    readme_bytes = b"reserved policy readme bytes\n"
    (upstream / "README.md").write_bytes(readme_bytes)
    manifest = json.loads((upstream / "MANIFEST.json").read_text())
    manifest["files"].append(
        {
            "path": spelling,
            "bytes": len(EVIL_BYTES),
            "sha256": hashlib.sha256(EVIL_BYTES).hexdigest(),
            "git_blob_sha": _git_blob_sha(EVIL_BYTES),
        }
    )
    (upstream / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")

    for args in ([], ["--update"]):
        mode = "check-only" if not args else "--update"
        result = _run(root, env, *args)
        assert result.returncode != 0, f"{mode}: stdout {result.stdout!r}"
        assert result.stdout == "", f"{mode}: stdout {result.stdout!r}"
        assert "ERROR:" in result.stderr, result.stderr
        assert "reserved" in result.stderr, f"{mode}: reason: {result.stderr!r}"
        assert (upstream / "README.md").read_bytes() == readme_bytes, (
            f"{mode}: README overwritten via casefolded spelling"
        )


def test_nested_readme_allowed(tmp_path: Path) -> None:
    """(deliberate choice): a NESTED upstream asset
    `docs/readme.md` (self-consistent hashes, served by the fake transport)
    is NOT reserved — only upstream-root policy files are — so check-only
    still reports UNCHANGED and --update refreshes it normally."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    nested = {"docs/readme.md": b"nested upstream readme\n"}
    manifest = json.loads((upstream / "MANIFEST.json").read_text())
    for path, data in nested.items():
        (upstream / path).write_bytes(data)
        manifest["files"].append(
            {
                "path": path,
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
                "git_blob_sha": _git_blob_sha(data),
            }
        )
    (upstream / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")

    r1 = _run(root, env)
    assert r1.returncode == 0 and r1.stdout.strip() == "UNCHANGED", r1.stderr
    tip = "tip0000000000000000000000000000000000000002"
    env["AAID_FAKE_TIP_SHA"] = tip
    env["AAID_FAKE_TIP_OVERRIDES"] = json.dumps(
        {"docs/readme.md": base64.b64encode(b"nested upstream readme changed\n").decode()}
    )
    r2 = _run(root, env, "--update")
    assert r2.returncode == 0 and r2.stdout.strip() == f"UPDATED {tip}", r2.stderr
    assert (upstream / "docs/readme.md").read_bytes() == b"nested upstream readme changed\n"


def test_dest_symlink_is_replaced_not_followed(tmp_path: Path) -> None:
    """(destination symlink): a SYMLINK planted at a live destination
    path must not redirect the cutover write: --update ends with the dest as
    a REGULAR file holding the tip bytes, and the symlink's TARGET keeps its
    old bytes untouched (os.replace replaces the entry, not the target)."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    tip = "tip0000000000000000000000000000000000000002"
    guide_tip = b"alpha line changed\n"
    env["AAID_FAKE_TIP_SHA"] = tip
    env["AAID_FAKE_TIP_OVERRIDES"] = json.dumps({"docs/guide.md": base64.b64encode(guide_tip).decode()})
    # Victim: a live dest path swapped to a symlink pointing at an unrelated
    # target outside the authorized tree. The target holds the PIN bytes so
    # the local-snapshot validation passes (reads follow the symlink); the
    # cutover must then replace the LINK ITSELF with regular tip bytes and
    # leave the target holding the OLD (pin) bytes verbatim.
    victim_target = tmp_path / "OFF-TREE-VICTIM.md"
    victim_target.write_bytes(UPSTREAM_FILES["docs/guide.md"])
    live = root / "assets" / "upstream" / "docs/guide.md"
    live.unlink()
    live.symlink_to(victim_target)

    result = _run(root, env, "--update")
    assert result.returncode == 0, f"--update stderr:\n{result.stderr}"
    assert result.stdout.strip() == f"UPDATED {tip}", result.stdout
    assert not live.is_symlink(), "dest stayed a symlink after cutover"
    assert live.is_file() and live.read_bytes() == guide_tip, "dest content wrong"
    assert victim_target.read_bytes() == UPSTREAM_FILES["docs/guide.md"], "symlink target was written through"


def test_no_symlinks_in_upstream_after_update(tmp_path: Path) -> None:
    """(symlink check): after a normal --update, EVERY file under
    assets/upstream is a REGULAR file (no symlink anywhere in the snapshot
    — a planted temp-path symlink cannot survive as a live entry), staged
    bytes hash correctly, and a pre-planted symlink forest OUTSIDE the
    authorized write set is untouched by the run."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    tip = "tip0000000000000000000000000000000000000002"
    guide_tip = b"alpha line changed\n"
    env["AAID_FAKE_TIP_SHA"] = tip
    env["AAID_FAKE_TIP_OVERRIDES"] = json.dumps({"docs/guide.md": base64.b64encode(guide_tip).decode()})
    # Pre-planted symlink forest OUTSIDE the write set (siblings of the
    # snapshot, plus an unrelated name next to MANIFEST.json): if the
    # checker ever adopted/followed planted links these would be altered.
    forest = {}
    for name in ("sibling.md", "docs-mirror.md"):
        tgt = tmp_path / f"TARGET-{name}"
        tgt.write_bytes(b"forest target bytes\n")
        link = tmp_path / f"FOREST-{name}"  # outside skill-root entirely
        link.symlink_to(tgt)
        forest[link] = tgt

    before = _snapshot(root)
    result = _run(root, env, "--update")
    assert result.returncode == 0, f"--update stderr:\n{result.stderr}"

    for entry in json.loads((upstream / "MANIFEST.json").read_text())["files"]:
        p = upstream / entry["path"]
        assert not p.is_symlink(), f"live snapshot entry became a symlink: {entry['path']}"
        assert p.is_file(), f"missing after update: {entry['path']}"
        assert hashlib.sha256(p.read_bytes()).hexdigest() == entry["sha256"]
    for link, tgt in forest.items():
        assert link.is_symlink() and link.resolve() == tgt.resolve()
        assert tgt.read_bytes() == b"forest target bytes\n", "symlink forest altered"
    assert (before["assets/upstream/rules/rule.mdc"]) == _snapshot(root)["assets/upstream/rules/rule.mdc"]
    assert not (upstream / "docs/guide.md").is_symlink()


def test_truncated_begin_marker_is_error(tmp_path: Path) -> None:
    """(truncated marker): SOURCE.md cut mid-write so its LAST line
    is a truncated `<!-- BEGIN CHECK-STATUS` (no full marker, no END, no
    pin). The strict BEGIN regex does not match it, but the loose marker
    trace discipline must fail LOUDLY: check-only reports ERROR "malformed
    check-status block", never the silent manifest resolved_commit fallback
    (which would read unreviewed pin==tip and falsely report UNCHANGED)."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    source.write_text(
        "# Source provenance — fixture\n\n"
        "<!-- BEGIN CHECK-STATUS: checker-maintained -->\n"
        "- Last successful check: 2026-10-23\n"
        f"- Fetched commit: `{PIN}`\n"
        f"- Integrated pin: `{PIN}` (reviewed content; "
        "<!-- BEGIN CHECK-STATUS"  # truncated, file ends mid-marker
    )
    before = _snapshot(root)
    result = _run(root, env)

    assert result.returncode != 0 and result.stdout == "", f"stdout {result.stdout!r} stderr {result.stderr!r}"
    assert "ERROR: malformed check-status block" in result.stderr, result.stderr
    assert _snapshot(root) == before, "the erroring run wrote to the fixture root"


def test_marker_trace_scope(tmp_path: Path) -> None:
    """(truncated-marker scope): the loose trace matches only
    lines containing 'BEGIN CHECK-STATUS'. Prose checks (like a sentence in
    these docstrings) do NOT trip it. A SOURCE.md with no marker substring
    and NO block is itself the fail-closed 'missing provenance' state (the
    integrated-pin record is absent; a manifest-pin fallback could launder a
    fetched pin: closure-gate 6.3 finding 1) — ERROR, never UNCHANGED."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    source.write_text("# Source provenance — fixture\n\nNo block here yet.\n")
    r1 = _run(root, env)
    assert r1.returncode != 0 and r1.stdout == "", f"stdout {r1.stdout!r} stderr {r1.stderr!r}"
    assert "ERROR: missing provenance" in r1.stderr, r1.stderr

    # ...and the marker substring must look like a marker attempt ON ITS
    # OWN line? No — substring-in-line is the contract: any line containing
    # BEGIN CHECK-STATUS (even mid-line prose quoting the token) counts as
    # a trace and yields ERROR once strict validation cannot complete.
    source.write_text("# Provenance\n\nSomeone wrote BEGIN CHECK-STATUS inside a sentence.\n")
    r2 = _run(root, env)
    assert r2.returncode != 0, r2.stdout
    assert "malformed check-status block" in r2.stderr, r2.stderr


# ---------------------------------------------------------------------------
# Closure-gate 6.3 fixes: ancestor-symlink bounded-write bypass (finding 2)
# and transport bounds (3), plus the direct ancestor-validator unit tests.
# ---------------------------------------------------------------------------


def test_ancestor_symlinked_references_dir_is_refused(tmp_path: Path) -> None:
    """(closure-gate 6.3 finding 2, static variant): references/ symlinked to
    a directory OUTSIDE the skill root must make --update ERROR before the
    SOURCE.md cutover write — nothing may be written through the link. The
    external directory receives no new files from the run."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    tip = "tip0000000000000000000000000000000000000002"
    env["AAID_FAKE_TIP_SHA"] = tip
    env["AAID_FAKE_TIP_OVERRIDES"] = json.dumps({"docs/guide.md": base64.b64encode(b"alpha line changed\n").decode()})
    external = tmp_path / "external-references"
    external.mkdir()
    # Valid provenance in the LINK TARGET: reads still work (so the run
    # proceeds deep into the refresh), only the WRITE must be refused.
    (external / "SOURCE.md").write_text(source.read_text())
    (root / "references").rename(tmp_path / "references-original")
    (root / "references").symlink_to(external)
    external_before = _snapshot(external)

    result = _run(root, env, "--update")

    assert result.returncode != 0 and result.stdout == "", f"stdout {result.stdout!r} stderr {result.stderr!r}"
    err = result.stderr.strip()
    assert err.startswith("ERROR:"), err
    assert "symlink" in err, f"reason must name the manipulated ancestor: {err!r}"
    assert _snapshot(external) == external_before, "external target touched by the run"


def _pivot_docs_gh(bin_dir: Path, external_docs: Path) -> None:
    """Extend the fake gh with a deterministic mid-run attacker: on the FIRST
    contents call it renames assets/upstream/docs (still a REAL plain
    directory at plan/containment time) and replaces it with a symlink to
    `external_docs`. Idempotent re-check instead of a flag env var (no dead
    scaffolding); paths derive from AAID_SKILL_ROOT, NOT AAID_FAKE_ROOT
    (which points at the upstream fixture dir)."""
    gh = bin_dir / "gh"
    original = gh.read_text()
    pivot = (
        "skill_root = os.environ['AAID_SKILL_ROOT']\n"
        "docs_dir = os.path.join(skill_root, 'assets', 'upstream', 'docs')\n"
        "if path == 'docs/guide.md' and os.path.isdir(docs_dir) and not os.path.islink(docs_dir):\n"
        "    os.rename(docs_dir, os.path.join(skill_root, 'docs-original'))\n"
        "    os.symlink(os.environ['AAID_EXTERNAL_DOCS'], docs_dir)\n"
    )
    body = original.replace("import base64", "import base64, os", 1)
    body = body.replace(
        "if path is None:\n    sys.exit(1)\n",
        "if path is None:\n    sys.exit(1)\n" + pivot,
        1,
    )
    gh.write_text(body)
    gh.chmod(0o755)


def test_mid_run_docs_pivot_is_refused_before_cutover(tmp_path: Path) -> None:
    """(closure-gate 6.3 finding 2, pivot variant — single deduped test):
    assets/upstream/docs is a REAL plain directory at plan time; a local
    attacker pivots it to an EXTERNAL symlink DURING the run (the fake gh
    rewrites the tree between fetch calls, so plan-time containment passes).
    The cutover write must ERROR pre-write on the write-time ancestor lstat,
    never `UPDATED` through the pivot, and the external guide.md must keep
    its old pin bytes (no redirected overwrite, no external writes)."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    tip = "tip0000000000000000000000000000000000000002"
    guide_tip = b"alpha line changed\n"
    env["AAID_FAKE_TIP_SHA"] = tip
    env["AAID_FAKE_TIP_OVERRIDES"] = json.dumps({"docs/guide.md": base64.b64encode(guide_tip).decode()})
    external_docs = tmp_path / "external-docs"
    external_docs.mkdir()
    external_guide = external_docs / "guide.md"
    external_guide.write_bytes(UPSTREAM_FILES["docs/guide.md"])  # pin bytes: local hash check passes
    external_before = _snapshot(external_docs)
    _pivot_docs_gh(bin_dir, external_docs)
    env["AAID_EXTERNAL_DOCS"] = str(external_docs)

    result = _run(root, env, "--update")

    assert result.returncode != 0 and result.stdout == "", f"stdout {result.stdout!r} stderr {result.stderr!r}"
    assert result.stdout.strip() != f"UPDATED {tip}", "cutover wrote through a symlinked ancestor"
    err = result.stderr.strip()
    assert err.startswith("ERROR:"), err
    # Assert INSIDE the reason text, not a bare "symlink" substring that pytest
    # tmp dirnames coincidentally contain.
    assert "is a symlink or not a directory" in err, f"reason must name the manipulated ancestor: {err!r}"
    assert "staging retained" in err, "cutover-phase refusal must retain the recovery staging"
    assert external_guide.read_bytes() == UPSTREAM_FILES["docs/guide.md"], (
        "EXTERNAL guide.md was overwritten through the ancestor symlink"
    )
    assert _snapshot(external_docs) == external_before, "external docs dir touched"


# --- transport bounds: checker-enforced deadline + payload cap -------------


def test_gh_timeout_is_error_and_releases_lock(tmp_path: Path) -> None:
    """(closure-gate 6.3 finding 3): a hung gh beyond AAID_CHECK_TIMEOUT is a
    sanitized ERROR naming the timeout, with nonzero exit; a --update run
    releases its own lock so a hung transport cannot wedge .cache/update.lock."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    gh = bin_dir / "gh"
    env["AAID_CHECK_TIMEOUT"] = "1"
    gh.write_text("#!/usr/bin/env python3\nimport time, sys\ntime.sleep(5)\n")
    gh.chmod(0o755)

    before = _snapshot(root)
    result = _run(root, env, "--update")

    assert result.returncode != 0 and result.stdout == "", f"stdout {result.stdout!r}"
    err = result.stderr.strip()
    assert err.startswith("ERROR:"), err
    assert "timed out after 1s" in err, f"no timeout reason: {err!r}"
    assert "AAID_CHECK_TIMEOUT" in err, err
    assert _snapshot(root) == before, "timed-out run modified the fixture root"
    assert not (root / ".cache" / "update.lock").exists(), "lock wedged by timed-out run"


def test_oversized_payload_rejected(tmp_path: Path) -> None:
    """(closure-gate 6.3 finding 3): a decoded contents payload above the 2MB
    checker bound is rejected with a sanitized ERROR — never buffered and
    compared (no UNCHANGED/CHANGED verdict from oversized data)."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    gh = bin_dir / "gh"
    gh.write_text(
        "#!/usr/bin/env python3\n"
        "import base64, hashlib, json, os, sys\n"
        "args = sys.argv[1:]\n"
        'if any("commits/main" in a for a in args):\n'
        '    print(json.dumps({"sha": os.environ["AAID_FAKE_PIN"]}))\n'
        "    sys.exit(0)\n"
        "data = b'x' * (2 * 1024 * 1024 + 8)\n"
        "print(json.dumps({\n"
        "    'content': base64.b64encode(data).decode(),\n"
        "    'encoding': 'base64',\n"
        "    'size': len(data),\n"
        "    'sha': hashlib.sha1(b'blob %d\\0' % len(data) + data).hexdigest(),\n"
        "}))\n"
    )
    gh.chmod(0o755)

    before = _snapshot(root)
    result = _run(root, env)

    assert result.returncode != 0 and result.stdout == "", f"stdout {result.stdout!r}"
    assert "ERROR:" in result.stderr, result.stderr
    assert "payload exceeds" in result.stderr, result.stderr
    assert _snapshot(root) == before, "run modified the fixture root"


def test_stale_lock_error_reports_age_and_manual_removal(tmp_path: Path) -> None:
    """(closure-gate 6.3 finding 3, lock UX): an existing lock ERROR reports
    the lock's age and the manual-removal instruction, and never deletes the
    lock itself (the holder may be a live updater)."""
    import time as _time

    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    lock_dir = root / ".cache"
    lock_dir.mkdir()
    lock = lock_dir / "update.lock"
    lock.write_bytes(b"owner: other\n")
    old = _time.time() - 120
    os.utime(lock, (old, old))
    before = _snapshot(root)

    result = _run(root, env, "--update")

    assert result.returncode != 0 and result.stdout == "", f"stdout {result.stdout!r}"
    err = result.stderr.strip()
    assert err.startswith("ERROR:"), err
    assert "another update in progress or stale lock" in err, err
    assert "held for 1" in err, f"lock age not reported: {err!r}"
    assert "remove .cache/update.lock manually" in err, err
    assert lock.is_file(), "non-holder deleted the lock"
    assert _snapshot(root) == before, "locked run modified the fixture root"


# --- direct unit test of the ancestor-validation function (D) --------------


def _load_checker_python(tmp_path: Path) -> dict[str, object]:
    """Extract the embedded checker python (heredoc body, truncated before
    main()) and exec it in a synthetic namespace so the dirfd walk helpers
    are unit-testable without a subprocess."""
    import re as _re
    import sys as _sys

    text = CHECKER.read_text()
    match = _re.search(r"<<'PYEOF'\n(.*?)\nPYEOF\n", text, _re.S)
    assert match, "embedded python program not found in checker"
    src = match.group(1)
    src = src[: src.index("\ndef main():")]
    env_root = tmp_path / "unit-root"
    (env_root / "assets" / "upstream").mkdir(parents=True)
    old_argv = _sys.argv
    _sys.argv = ["check-upstream.sh", str(env_root), "0"]
    try:
        namespace: dict[str, object] = {}
        exec(compile(src, "check-upstream.sh#embedded", "exec"), namespace)  # noqa: S102 - test extraction of own repo source
    finally:
        _sys.argv = old_argv
    assert "walk_dirs" in namespace, "walk_dirs not defined in extraction"
    return namespace


def test_walk_dirs_refuses_symlink_escape_and_missing(tmp_path: Path) -> None:
    """(D, dirfd API): direct unit tests of the walk helper — (a) a
    symlinked component is refused; (b) a non-canonical escape ('..') is
    refused; (c) a missing component raises Missing with create=False and
    is created-and-revalidated with create=True; (d) an ordinary in-root
    chain passes and returns an openable dirfd."""
    import os as _os
    import stat as _stat

    ns = _load_checker_python(tmp_path)
    walk_dirs = ns["walk_dirs"]
    Missing = ns["Missing"]
    root = tmp_path / "unit-root"
    external = tmp_path / "unit-external"
    external.mkdir()
    (root / "references").symlink_to(external)  # (a) symlink pivot
    root_fd = _os.open(str(root), _os.O_RDONLY | _os.O_DIRECTORY)

    with pytest.raises(SystemExit):
        walk_dirs(("references",), root_fd, "unit walk")

    (root / "references").unlink()  # (b) escape
    with pytest.raises(SystemExit):
        walk_dirs(("..",), root_fd, "unit walk")

    with pytest.raises(Missing):  # (c-i) missing, strict
        walk_dirs(("brand-new-dir",), root_fd, "unit walk")
    fd = walk_dirs(("brand-new-dir", "deeper"), root_fd, "unit walk", create=True)
    assert _stat.S_ISDIR(_os.fstat(fd).st_mode)  # (c-ii) created
    _os.close(fd)
    assert (root / "brand-new-dir" / "deeper").exists()

    fd = walk_dirs(("assets", "upstream"), root_fd, "unit walk")  # (d)
    assert _stat.S_ISDIR(_os.fstat(fd).st_mode)
    _os.close(fd)
    _os.close(root_fd)


def test_read_regular_refuses_symlink_and_fifo(tmp_path: Path) -> None:
    """(D, read-side): direct unit tests — (a) a symlinked regular record is
    refused as tampered provenance (external target untouched); (b) a FIFO
    is refused FAST (no unbounded open/read); (c) a plain file reads fine."""
    import os as _os

    ns = _load_checker_python(tmp_path)
    read_regular = ns["read_regular_at_fd"]
    root = tmp_path / "unit-root"
    root_fd = _os.open(str(root), _os.O_RDONLY | _os.O_DIRECTORY)

    (root / "regular.md").write_bytes(b"plain\n")  # (c) control leg
    assert read_regular(root_fd, "regular.md", "unit read") == b"plain\n"

    external = tmp_path / "unit-external.md"
    external.write_bytes(b"tampered bytes\n")
    (root / "linked.md").symlink_to(external)  # (a) symlinked record
    with pytest.raises(SystemExit):
        read_regular(root_fd, "linked.md", "provenance record")
    assert external.read_bytes() == b"tampered bytes\n"

    fifo = root / "fifo.md"  # (b) FIFO record
    _os.mkfifo(str(fifo))
    with pytest.raises(SystemExit):
        read_regular(root_fd, "fifo.md", "provenance record")
    _os.close(root_fd)


# ---------------------------------------------------------------------------
# Iteration-3 coverage: legacy-migration negative test; persistent root
# rename+symlink swap; symlinked root; python3 preflight; integration sync
# advancement; exact raw-cap boundary; EOF-then-stderr-hang bound;
# foreign-lock deletion refusal; FIFO SOURCE end-to-end.
# ---------------------------------------------------------------------------


def test_legacy_migration_integrated_defaults_to_source_pin(tmp_path: Path) -> None:
    """(Fix 1, HIGH): legacy manifest WITHOUT integrated_commit in the
    post-refresh state (resolved=tip2 fetched, SOURCE pin=pin1). --update
    must persist integrated_commit=pin1 (the human-integrated record),
    NEVER tip2; afterwards deleting references/ AND .cache/ must leave
    check-only reporting CHANGED (review pending), not the pre-fix-laundry
    UNCHANGED B-vs-B."""
    root, upstream, source, bin_dir, env, pin1, tip2 = _fetched_unreviewed_fixture(tmp_path, with_integrated=False)
    # Sanity: the fixture truly carries the legacy schema shape.
    legacy = json.loads((upstream / "MANIFEST.json").read_text())
    assert "integrated_commit" not in legacy
    assert legacy["resolved_commit"] == tip2

    result = _run(root, env, "--update")

    assert result.returncode == 0, f"--update stderr:\n{result.stderr}"
    assert result.stdout.strip() == f"UPDATED {tip2}", result.stdout
    new_manifest = json.loads((upstream / "MANIFEST.json").read_text())
    # The migrated integrated pin is the SOURCE record, not the fetched tip.
    assert new_manifest["integrated_commit"] == pin1, new_manifest["integrated_commit"]
    assert new_manifest["resolved_commit"] == tip2

    # Delete BOTH provenance dirs (the laundering precondition).
    source.unlink()
    shutil.rmtree(root / "references")
    if (root / ".cache").is_dir():
        shutil.rmtree(root / ".cache")

    before = _snapshot(root)
    check = _run(root, env)

    assert check.returncode == 0, f"check-only stderr:\n{check.stderr}"
    assert check.stdout.strip() == "CHANGED", (
        f"legacy migrated pin must keep flagging review pending; got {check.stdout!r}"
    )
    assert _snapshot(root) == before, "check-only run modified the fixture root"


def test_persistent_root_rename_swap_refused(tmp_path: Path) -> None:
    """(Fix 2, HIGH): the root directory is renamed and a symlink left at
    the old pathname pointing at a MATCHING EXTERNAL tree — a fake gh
    performs the swap between gh calls (deterministic mid-run pivot). The
    dirfd-pinned boundary verifies path/identity before every write: the
    run must ERROR and NOT write the external tree."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    tip = "tip0000000000000000000000000000000000000002"
    env["AAID_FAKE_TIP_SHA"] = tip
    env["AAID_FAKE_TIP_OVERRIDES"] = json.dumps({"docs/guide.md": base64.b64encode(b"alpha line changed\n").decode()})
    external_root = tmp_path / "external-matching-root"
    shutil.copytree(root, external_root, symlinks=True)
    external_before = _snapshot(external_root)
    gh = bin_dir / "gh"
    original = gh.read_text()
    pivot = (
        "new_root = os.environ['AAID_EXTERNAL_ROOT']\n"
        "old_root = os.environ['AAID_SKILL_ROOT']\n"
        "os.rename(old_root, old_root + '-renamed')\n"
        "os.symlink(new_root, old_root)\n"
    )
    body = original.replace(
        "if path is None:\n    sys.exit(1)\n",
        "if path is None:\n    sys.exit(1)\n" + pivot,
        1,
    )
    gh.write_text(body)
    gh.chmod(0o755)
    env["AAID_EXTERNAL_ROOT"] = str(external_root)

    result = _run(root, env, "--update")

    assert result.returncode != 0 and result.stdout == "", (
        f"swapped root must be refused: stdout {result.stdout!r} stderr {result.stderr!r}"
    )
    err = result.stderr.strip()
    assert err.startswith("ERROR:"), err
    assert "renamed or swapped mid-run" in err, f"reason: {err!r}"
    # Fetch-phase refusal: staging is cleaned (no retained note needed); the
    # material claim is the swap refusal + an untouched external tree.
    # The external matching tree must be byte-identical (no redirected
    # writes; note the pivot itself added the symlink inside tmp only).
    assert _snapshot(external_root) == external_before, "external root touched"


def test_symlinked_skill_root_boundary_refused(tmp_path: Path) -> None:
    """(nit 6, covered adversarially): AAID_SKILL_ROOT pointing at a SYMLINK
    (with the test-harness marker set) is refused: ERROR naming the
    boundary symlink."""
    real_root = tmp_path / "real-root"
    (real_root / "assets" / "upstream" / "docs").mkdir(parents=True)
    (real_root / "references").mkdir()
    data = UPSTREAM_FILES["docs/guide.md"]
    (real_root / "assets" / "upstream" / "docs/guide.md").write_bytes(data)
    source = real_root / "references" / "SOURCE.md"
    source.write_text(
        "# Source provenance — fixture\n\n"
        "<!-- BEGIN CHECK-STATUS: checker-maintained -->\n"
        "- Last successful check: 2026-10-23\n"
        f"- Fetched commit: `{PIN}`\n"
        f"- Integrated pin: `{PIN}`\n"
        "<!-- END CHECK-STATUS -->\n"
    )
    files = [
        {
            "path": "docs/guide.md",
            "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
            "git_blob_sha": _git_blob_sha(data),
        }
    ]
    (real_root / "assets" / "upstream" / "MANIFEST.json").write_text(
        json.dumps(
            {
                "repository": REPO,
                "default_branch": BRANCH,
                "resolved_commit": PIN,
                "generated": "2026-10-24",
                "files": files,
            },
            indent=2,
        )
        + "\n"
    )

    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    _make_fake_gh(bin_dir, real_root / "assets" / "upstream")
    env = dict(os.environ)
    env["PATH"] = str(bin_dir) + os.pathsep + env["PATH"]
    env["AAID_FAKE_ROOT"] = str(real_root / "assets" / "upstream")
    env["AAID_FAKE_PIN"] = PIN
    env["AAID_FAKE_ROOT"] = str(real_root / "assets" / "upstream")
    env["AAID_FAKE_TIP_SHA"] = PIN
    env["AAID_FAKE_TIP_OVERRIDES"] = "{}"
    env["AAID_FAKE_PIN_OVERRIDES"] = "{}"
    root_link = tmp_path / "linked-root"
    root_link.symlink_to(real_root)
    env["AAID_SKILL_ROOT"] = str(root_link)

    result = _run(root_link, env)

    assert result.returncode != 0 and result.stdout == "", (
        f"symlinked root boundary must be refused: stdout {result.stdout!r}"
    )
    assert "skill root boundary itself is a symlink" in result.stderr, result.stderr


def test_python3_preflight_message(tmp_path: Path) -> None:
    """(nit 6): a PATH-sandboxed run with gh present but python3 absent
    produces the sanitized preflight ERROR — never a raw exit 127."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    minbin = tmp_path / "no_py_bin"
    minbin.mkdir(exist_ok=True)
    (minbin / "gh").symlink_to(bin_dir / "gh")
    (minbin / "dirname").symlink_to("/usr/bin/dirname")
    env["PATH"] = str(minbin)

    result = _run(root, env)

    assert result.returncode != 0 and result.stdout == "", result.stdout
    assert result.stderr.strip() == (
        "ERROR: python3 not found on PATH (the embedded checker program requires python3)"
    ), result.stderr


def test_integration_sync_advances_integrated_pin(tmp_path: Path) -> None:
    """(nit 6): the human advances the SOURCE block pin to the previously
    fetched tip2; the NEXT authorized update syncs the manifest's
    integrated_commit pin1 -> tip2 (and resolved stays tip2)."""
    pin1 = PIN
    tip2 = "tip200000000000000000000000000000000000000002"
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    tip2_files = {
        "docs/guide.md": b"alpha line changed\n",
        "rules/rule.mdc": UPSTREAM_FILES["rules/rule.mdc"],
    }
    manifest = json.loads((upstream / "MANIFEST.json").read_text())
    manifest["resolved_commit"] = tip2
    manifest["integrated_commit"] = pin1
    manifest["files"] = [
        {"path": p, "bytes": len(d), "sha256": hashlib.sha256(d).hexdigest(), "git_blob_sha": _git_blob_sha(d)}
        for p, d in tip2_files.items()
    ]
    (upstream / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")
    (upstream / "docs/guide.md").write_bytes(tip2_files["docs/guide.md"])
    # Human integration: the SOURCE block pin now records tip2.
    source.write_text(
        "# Source provenance — fixture\n\n"
        "<!-- BEGIN CHECK-STATUS: checker-maintained -->\n"
        "- Last successful check: " + datetime.date.today().isoformat() + "\n"
        f"- Fetched commit: `{tip2}`\n"
        f"- Integrated pin: `{tip2}`\n"
        "<!-- END CHECK-STATUS -->\n"
    )
    env["AAID_FAKE_TIP_SHA"] = tip2
    env["AAID_FAKE_TIP_OVERRIDES"] = "{}"
    env["AAID_FAKE_PIN_OVERRIDES"] = json.dumps(
        {"docs/guide.md": base64.b64encode(UPSTREAM_FILES["docs/guide.md"]).decode()}
    )

    result = _run(root, env, "--update")

    assert result.returncode == 0, f"--update stderr:\n{result.stderr}"
    assert result.stdout.strip() == f"UPDATED {tip2}", result.stdout
    new_manifest = json.loads((upstream / "MANIFEST.json").read_text())
    # ADVANCEMENT: integrated pin moved pin1 -> tip2 by the sync arm.
    assert new_manifest["integrated_commit"] == tip2, new_manifest["integrated_commit"]
    assert new_manifest["resolved_commit"] == tip2


def _make_padded_gh(bin_dir: Path, upstream: Path, target_bytes: int) -> None:
    """Fake `gh` whose EVERY response (commits + contents) is padded with
    JSON-legal internal whitespace to land at EXACTLY `target_bytes` raw
    stdout bytes (used for the exact raw-cap boundary test)."""
    gh = bin_dir / "gh"
    gh.write_text(
        "#!/usr/bin/env python3\n"
        "import base64, hashlib, json, os, sys\n"
        "args = sys.argv[1:]\n"
        'target = int(os.environ.get("AAID_RAW_TARGET", "0"))\n'
        'pin = os.environ["AAID_FAKE_PIN"]\n'
        'root = os.environ["AAID_FAKE_ROOT"]\n'
        "obj = None\n"
        'if any("repos/example/ex/commits/main" in a for a in args):\n'
        '    obj = {"sha": pin}\n'
        "else:\n"
        "    path = None\n"
        "    for a in args:\n"
        '        if "repos/example/ex/contents/" in a:\n'
        '            path = a.split("repos/example/ex/contents/", 1)[1]\n'
        '    data = open(os.path.join(root, path), "rb").read()\n'
        "    obj = {\n"
        '        "content": base64.b64encode(data).decode(),\n'
        '        "encoding": "base64",\n'
        '        "size": len(data),\n'
        '        "sha": hashlib.sha1(b"blob %d\\0" % len(data) + data).hexdigest(),\n'
        "    }\n"
        "raw = json.dumps(obj)\n"
        "pad = target - len(raw)\n"
        "if pad < 0:\n"
        "    pad = 0\n"
        'sys.stdout.write(raw[:-1] + " " * pad + "}")\n'
    )
    gh.chmod(0o755)


@pytest.mark.parametrize(
    "target_bytes,expect_ok",
    [
        (4 * 1024 * 1024, True),  # exactly the raw cap: passes
        (4 * 1024 * 1024 + 1, False),  # one byte past: killed + ERROR
    ],
)
def test_raw_response_cap_exact_boundary(tmp_path: Path, target_bytes: int, expect_ok: bool) -> None:
    """(adversarial, raw-cap boundary semantics): a response of EXACTLY
    4 MiB raw stdout passes the raw cap and yields a verdict; 4 MiB + 1
    leads the run killed with the sanitized raw-cap ERROR."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    _make_padded_gh(bin_dir, upstream, target_bytes)
    env["AAID_RAW_TARGET"] = str(target_bytes)

    before = _snapshot(root)
    result = _run(root, env)

    if expect_ok:
        assert result.returncode == 0, f"stderr:\n{result.stderr}"
        assert result.stdout.strip() == "UNCHANGED", result.stdout
    else:
        assert result.returncode != 0 and result.stdout == "", result.stdout
        err = result.stderr.strip()
        assert err.startswith("ERROR:"), err
        assert "raw response exceeded" in err, f"reason: {err!r}"
    assert _snapshot(root) == before, "run modified the fixture root"


def test_post_eof_stderr_hang_is_deadline_bounded(tmp_path: Path) -> None:
    """(Fix 3): gh closes stdout then BLOCKS (sleep) on a live stderr pipe —
    the post-EOF wait is deadline-bounded: killed and reported with the
    sanitized reason, within the AAID_CHECK_TIMEOUT window."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    gh = bin_dir / "gh"
    gh.write_text(
        "#!/usr/bin/env python3\n"
        "import os, sys, time\n"
        "args = sys.argv[1:]\n"
        'if any("commits/main" in a for a in args):\n'
        '    sys.stdout.write(\'{"sha": "x" * 40}\')\n'
        "    sys.stdout.flush()\n"
        "    os.close(1)\n"  # fd-level close: sys.stdout.close() leaves the
        "    time.sleep(30)\n"  # pipe fd open on some platforms (no EOF)
        "sys.exit(0)\n"
    )
    gh.chmod(0o755)
    env["AAID_CHECK_TIMEOUT"] = "2"

    drift_start = time.time()
    result = _run(root, env)
    elapsed = time.time() - drift_start

    assert result.returncode != 0 and result.stdout == "", result.stdout
    err = result.stderr.strip()
    assert err.startswith("ERROR:"), err
    assert "did not exit after closing stdout" in err, f"reason: {err!r}"
    # Real end-to-end wall-clock bound: comfortably above the 2s deadline
    # (select granularity) but FAR below the child would block (30s).
    assert elapsed < 15, f"post-EOF hang not bounded (took {elapsed:.1f}s)"


def test_foreign_lock_deletion_refused(tmp_path: Path) -> None:
    """(adversarial medium): .cache is ALREADY a symlink pointing to an
    external directory that holds a foreign update.lock — the checker must
    ERROR at the boundary walk and never create/unlink a lock through the
    swap; the foreign lock file stays byte-identical."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    tip = "tip0000000000000000000000000000000000000002"
    env["AAID_FAKE_TIP_SHA"] = tip
    env["AAID_FAKE_TIP_OVERRIDES"] = json.dumps({"docs/guide.md": base64.b64encode(b"alpha line changed\n").decode()})
    external_cache = tmp_path / "external-cache"
    external_cache.mkdir()
    foreign_lock = external_cache / "update.lock"
    foreign_lock.write_bytes(b"owner: other-process\n")
    # The pivot replaces the fixture's .cache (created by the harden fixture?
    # no — no .cache yet) — just make .cache itself the symlink.
    (root / ".cache").symlink_to(external_cache)
    foreign_before = _snapshot(external_cache)

    result = _run(root, env, "--update")

    assert result.returncode != 0 and result.stdout == "", f"stdout {result.stdout!r} stderr {result.stderr!r}"
    err = result.stderr.strip()
    assert err.startswith("ERROR:"), err
    assert "is a symlink or not a directory" in err, f"reason: {err!r}"
    assert _snapshot(external_cache) == foreign_before, "foreign lock disturbed"


def test_fifo_source_refused_end_to_end(tmp_path: Path) -> None:
    """(Fix 2, FIFO finding): a FIFO at references/SOURCE.md blocks
    read-back with the regular-file refusal — no unbounded open/read hang."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    source.unlink()
    os.mkfifo(str(source))

    before = time.time()
    result = _run(root, env)
    elapsed = time.time() - before

    assert result.returncode != 0 and result.stdout == "", result.stdout
    err = result.stderr.strip()
    assert err.startswith("ERROR:"), err
    assert "not a regular file" in err, f"reason: {err!r}"
    assert elapsed < 15, f"FIFO refused slowly (took {elapsed:.1f}s)"


def _fetched_unreviewed_fixture(tmp_path: Path, with_integrated: bool):
    """Fixture in the post-authoritative-fetch state WITHOUT running --update:
    resolved advanced to tip2 (coherent single-snapshot manifest, tip2 bytes
    on disk), SOURCE block still pin1, and (optionally) an explicit
    integrated_commit = pin1 in the manifest. Returns the same tuple shape as
    _harden_fixture plus pin1/tip2."""
    pin1 = PIN
    tip2 = "tip200000000000000000000000000000000000000002"
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    tip2_files = {
        "docs/guide.md": b"alpha line changed\n",
        "rules/rule.mdc": UPSTREAM_FILES["rules/rule.mdc"],
    }
    manifest = json.loads((upstream / "MANIFEST.json").read_text())
    manifest["resolved_commit"] = tip2
    if with_integrated:
        manifest["integrated_commit"] = pin1
    manifest["files"] = [
        {
            "path": path,
            "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
            "git_blob_sha": _git_blob_sha(data),
        }
        for path, data in tip2_files.items()
    ]
    (upstream / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")
    (upstream / "docs/guide.md").write_bytes(tip2_files["docs/guide.md"])
    env["AAID_FAKE_TIP_SHA"] = tip2
    env["AAID_FAKE_PIN_OVERRIDES"] = json.dumps(
        {"docs/guide.md": base64.b64encode(UPSTREAM_FILES["docs/guide.md"]).decode()}
    )
    return root, upstream, source, bin_dir, env, pin1, tip2


def test_full_provenance_deletion_reports_changed(tmp_path: Path) -> None:
    """(M1-residual, binding rule): a refresh FETCHED changed content, then
    BOTH references/ and .cache/ were deleted — no residue survives, the
    residue-based first-run discriminator is fooled, and the checker takes
    the manifest fallback. That fallback must use the manifest INTEGRATED
    commit (pin1, human-integrated at vendoring), yielding CHANGED ('upstream
    moved, review pending') — NEVER UNCHANGED. The pre-fix checker fell back
    to resolved_commit (== the fetched tip) and reported tip-vs-itself as
    UNCHANGED."""
    root, upstream, source, bin_dir, env, pin1, tip2 = _fetched_unreviewed_fixture(tmp_path, with_integrated=True)
    source.unlink()
    shutil.rmtree(root / "references")
    if (root / ".cache").is_dir():
        shutil.rmtree(root / ".cache")
    assert not os.path.lexists(root / "references")
    assert not os.path.lexists(root / ".cache")

    before = _snapshot(root)
    result = _run(root, env)

    assert result.returncode == 0, f"stderr:\n{result.stderr}"
    assert result.stdout.strip() == "CHANGED", (
        f"fetched state must keep flagging review pending; stdout {result.stdout!r}, stderr {result.stderr!r}"
    )
    assert _snapshot(root) == before, "check-only run modified the fixture root"
    assert not (root / ".cache").exists(), "check-only created .cache"


def test_mid_run_cache_pivot_is_refused(tmp_path: Path) -> None:
    """(M2-residual, pinned boundary): .cache/ is a REAL plain directory at
    plan time (lock + staging already created inside it); a local attacker
    pivots it to an EXTERNAL symlink between gh calls (the fake gh rewrites
    the tree during the fetch window). Every staged write validates its
    ancestor chain against the PINNED root, so the .cache symlink is refused
    BEFORE any staging write can land inside the external directory, and the
    fail cleanup never rmtree-follows the link."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    tip = "tip0000000000000000000000000000000000000002"
    env["AAID_FAKE_TIP_SHA"] = tip
    env["AAID_FAKE_TIP_OVERRIDES"] = json.dumps({"docs/guide.md": base64.b64encode(b"alpha line changed\n").decode()})
    external_cache = tmp_path / "external-cache"
    external_cache.mkdir()
    external_before = _snapshot(external_cache)
    gh = bin_dir / "gh"
    original = gh.read_text()
    pivot = (
        "cache_now = os.path.join(os.environ['AAID_SKILL_ROOT'], '.cache')\n"
        "if path == 'docs/guide.md' and os.path.isdir(cache_now) and not os.path.islink(cache_now):\n"
        "    os.rename(cache_now, os.path.join(os.environ['AAID_SKILL_ROOT'], 'cache-original'))\n"
        "    os.symlink(os.environ['AAID_EXTERNAL_CACHE'], cache_now)\n"
    )
    body = original.replace(
        "if path is None:\n    sys.exit(1)\n",
        "if path is None:\n    sys.exit(1)\n" + pivot,
        1,
    )
    gh.write_text(body)
    gh.chmod(0o755)
    env["AAID_EXTERNAL_CACHE"] = str(external_cache)

    result = _run(root, env, "--update")

    assert result.returncode != 0 and result.stdout == "", f"stdout {result.stdout!r} stderr {result.stderr!r}"
    err = result.stderr.strip()
    assert err.startswith("ERROR:"), err
    assert "the pinned .cache was renamed or swapped mid-run" in err, f"reason: {err!r}"
    # Nothing (staged bytes, staging dirs, lock handles) may land in the
    # external dir — and fail cleanup must not rmtree through the link.
    assert _snapshot(external_cache) == external_before, "external .cache target touched"


def test_symlinked_source_is_tampered_provenance(tmp_path: Path) -> None:
    """(read-side provenance discipline): references/SOURCE.md replaced by a
    SYMLINK pointing at an external location — even one holding a VALID
    check-status block — is tampered provenance: check-only must ERROR
    naming the tamper, never trust the redirected pin."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    external_src = tmp_path / "ext-source-record.md"
    external_src.write_text(source.read_text())
    source.unlink()
    source.symlink_to(external_src)
    external_before = _snapshot(external_src)

    result = _run(root, env)

    assert result.returncode != 0 and result.stdout == "", f"stdout {result.stdout!r} stderr {result.stderr!r}"
    err = result.stderr.strip()
    assert err.startswith("ERROR:"), err
    assert "tampered provenance" in err, f"reason: {err!r}"
    assert _snapshot(external_src) == external_before, "external provenance target touched"


@pytest.mark.parametrize(
    "value,expected_msg",
    [
        ("nan", "AAID_CHECK_TIMEOUT must be a finite positive number"),
        ("inf", "AAID_CHECK_TIMEOUT must be a finite positive number"),
        ("-5", "AAID_CHECK_TIMEOUT must be a finite positive number"),
        ("not-a-number", "invalid AAID_CHECK_TIMEOUT"),
        ("999999999", None),  # clamped to the sane max; run proceeds normally
    ],
)
def test_aaid_check_timeout_value_bounds(tmp_path: Path, value: str, expected_msg: str | None) -> None:
    """(m2/L1-residual): AAID_CHECK_TIMEOUT bounds — nan/inf/negative/
    non-numeric are sanitized ERRORS (never silently disabling the
    deadline); oversized-but-finite values are CLAMPED to the sane max and
    the run proceeds normally."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    env["AAID_CHECK_TIMEOUT"] = value

    result = _run(root, env)

    if expected_msg is None:
        assert result.returncode == 0, f"stderr:\n{result.stderr}"
        assert result.stdout.strip() == "UNCHANGED", result.stdout
    else:
        assert result.returncode != 0 and result.stdout == "", result.stdout
        assert expected_msg in result.stderr, result.stderr


def test_raw_response_cap_kills_before_parse(tmp_path: Path) -> None:
    """(L1-residual, raw cap): an inflated RAW gh response (whitespace-
    padded so raw stdout > 4MB with a tiny decoded meaning) is killed at the
    raw-read bound BEFORE any JSON parse or decode: sanitized ERROR, never a
    verdict."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    gh = bin_dir / "gh"
    gh.write_text(
        "#!/usr/bin/env python3\n"
        "import json, sys\n"
        "args = sys.argv[1:]\n"
        'if any("commits/main" in a for a in args):\n'
        '    print(json.dumps({"sha": "x" * 40}))\n'
        "    sys.exit(0)\n"
        'sys.stdout.write("{" + "\\n" * (5 * 1024 * 1024))\n'
        "sys.stdout.flush()\n"
    )
    gh.chmod(0o755)

    before = _snapshot(root)
    result = _run(root, env)

    assert result.returncode != 0 and result.stdout == "", f"stdout {result.stdout!r}"
    err = result.stderr.strip()
    assert err.startswith("ERROR:"), err
    assert "raw response exceeded" in err, f"reason: {err!r}"
    assert _snapshot(root) == before, "run modified the fixture root"


def test_planted_staging_final_symlink_cannot_redirect(tmp_path: Path) -> None:
    """(staging write path): a final-component symlink planted inside the
    run's staging dir between gh calls cannot redirect a staged write: the
    guarded_write route (O_NOFOLLOW temp + os.replace entry replacement) ends
    the destination as a REGULAR file with the correct staged bytes; the
    attacker's external target keeps its old bytes; the update completes
    normally."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    tip = "tip0000000000000000000000000000000000000002"
    env["AAID_FAKE_TIP_SHA"] = tip
    env["AAID_FAKE_TIP_OVERRIDES"] = json.dumps({"docs/guide.md": base64.b64encode(b"alpha line changed\n").decode()})
    external_victim = tmp_path / "OFF-STAGING-VICTIM.mdc"
    external_victim.write_bytes(UPSTREAM_FILES["rules/rule.mdc"])
    gh = bin_dir / "gh"
    original = gh.read_text()
    plant = (
        "if path == 'docs/guide.md':\n"
        "    import glob\n"
        "    for staging_dir in glob.glob(os.path.join(os.environ['AAID_SKILL_ROOT'], '.cache', 'staging-*')):\n"
        "        rules_dir = os.path.join(staging_dir, 'rules')\n"
        "        os.makedirs(rules_dir, exist_ok=True)\n"
        "        target = os.path.join(rules_dir, 'rule.mdc')\n"
        "        if not os.path.lexists(target):\n"
        "            os.symlink(os.environ['AAID_EXTERNAL_VICTIM'], target)\n"
    )
    body = original.replace(
        "if path is None:\n    sys.exit(1)\n",
        "if path is None:\n    sys.exit(1)\n" + plant,
        1,
    )
    gh.write_text(body)
    gh.chmod(0o755)
    env["AAID_EXTERNAL_VICTIM"] = str(external_victim)

    result = _run(root, env, "--update")

    assert result.returncode == 0, f"--update stderr:\n{result.stderr}"
    assert result.stdout.strip() == f"UPDATED {tip}", result.stdout
    # The staged rules entry must be a REGULAR file with correct bytes (the
    # planted link was replaced, never followed through).
    assert not (upstream / "rules/rule.mdc").is_symlink()
    assert (upstream / "rules/rule.mdc").read_bytes() == UPSTREAM_FILES["rules/rule.mdc"]
    # The attacker's external target keeps its ORIGINAL bytes.
    assert external_victim.is_file()
    assert external_victim.read_bytes() == UPSTREAM_FILES["rules/rule.mdc"]


# ---------------------------------------------------------------------------
# Iteration-4: F1 single-ERROR-line; F2 python>=3.11 preflight; F3 snapshot
# read cap; F4 absence-of-provenance-never-authenticates; F5 top-level-file
# full update (dup-fd regression).
# ---------------------------------------------------------------------------


def test_fail_lone_path_single_error_line(tmp_path: Path) -> None:
    """(F1): a planted-symlink ANCESTOR during a staging write walk raises
    inside walk_dirs — the run's stderr must contain EXACTLY ONE ERROR line
    (pre-fix the unguarded finally raised UnboundLocalError, producing a
    second spurious ERROR and leaking the walk fd)."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    tip = "tip0000000000000000000000000000000000000002"
    env["AAID_FAKE_TIP_SHA"] = tip
    env["AAID_FAKE_TIP_OVERRIDES"] = json.dumps({"docs/guide.md": base64.b64encode(b"alpha line changed\n").decode()})
    external_docs = tmp_path / "external-docs"
    external_docs.mkdir()
    (external_docs / "guide.md").write_bytes(UPSTREAM_FILES["docs/guide.md"])
    gh = bin_dir / "gh"
    original = gh.read_text()
    pivot = (
        "if path == 'rules/rule.mdc' and ref != pin:\n"
        "    import glob\n"
        "    for staging_dir in glob.glob(os.path.join(os.environ['AAID_SKILL_ROOT'], '.cache', 'staging-*')):\n"
        "        os.rename(os.path.join(staging_dir, 'docs'), os.path.join(staging_dir, 'docs-util'))\n"
        "        os.symlink(os.environ['AAID_EXTERNAL_DOCSDIR'], os.path.join(staging_dir, 'docs'))\n"
    )
    body = original.replace(
        "if path is None:\n    sys.exit(1)\n",
        "if path is None:\n    sys.exit(1)\n" + pivot,
        1,
    )
    gh.write_text(body)
    gh.chmod(0o755)
    env["AAID_EXTERNAL_DOCSDIR"] = str(external_docs)

    result = _run(root, env, "--update")

    assert result.returncode != 0 and result.stdout == "", result.stdout
    err = result.stderr
    assert err.count("ERROR:") == 1, f"exactly one sanitized line required: {err!r}"
    assert "is a symlink or not a directory" in err, f"reason: {err!r}"
    # The Planted-docs walk must not have written through the link.
    assert (external_docs / "guide.md").read_bytes() == UPSTREAM_FILES["docs/guide.md"]


def test_python_version_floor_preflight(tmp_path: Path) -> None:
    """(F2): a python3 that fails the version check makes the shell
    preflight fire with the floor named — never a raw traceback mid-cutover."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    minbin = tmp_path / "old_py_bin"
    minbin.mkdir(exist_ok=True)
    (minbin / "gh").symlink_to(bin_dir / "gh")
    (minbin / "dirname").symlink_to("/usr/bin/dirname")
    fake_py = minbin / "python3"
    fake_py.write_text("#!/usr/bin/env sh\necho '3.9.6'\nexit 1\n")
    fake_py.chmod(0o755)
    env["PATH"] = str(minbin)

    result = _run(root, env)

    assert result.returncode != 0 and result.stdout == "", result.stdout
    err = result.stderr.strip()
    assert err.startswith("ERROR:"), err
    assert "python3 >= 3.11" in err, f"reason: {err!r}"
    assert "supported interpreter policy" in err, err


def test_snapshot_read_capped_at_declared_size(tmp_path: Path) -> None:
    """(F3): a local-snapshot entry symlinked to /dev/zero (or the REAL file
    replaced by a growing stream) is size-capped: manifest-declared bytes +
    64KB slack is the maximum read; exceeded → sanitized ERROR naming the
    cap, never an unbounded read / OOM."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    live = upstream / "docs/guide.md"
    live.unlink()
    live.symlink_to("/dev/zero")

    result = _run(root, env)

    assert result.returncode != 0 and result.stdout == "", result.stdout
    err = result.stderr.strip()
    assert err.startswith("ERROR:"), err
    assert "declared size cap" in err, f"reason: {err!r}"
    assert "/dev/zero" not in err  # sanitized reason, no device path noise


def test_legacy_manifest_no_field_after_rename_is_error(tmp_path: Path) -> None:
    """(F4 binding, negative): legacy manifest WITHOUT integrated_commit,
    resolved=tip2 (fetched-only), references/ AND .cache/ RENAMED away (not
    deleted) — absence of provenance never authenticates: ERROR fail-closed,
    NEVER UNCHANGED, regardless of residue presence."""
    root, upstream, source, bin_dir, env, pin1, tip2 = _fetched_unreviewed_fixture(tmp_path, with_integrated=False)
    # Rename (not delete) the provenance dirs away — the pre-iteration-4
    # first-run discriminator could be fooled by the disappearance.
    stash = tmp_path / "stashed-dirs"
    stash.mkdir()
    shutil.move(str(root / "references"), str(stash / "references"))
    (root / ".cache").mkdir()  # a cache dir exists, then is renamed away
    shutil.move(str(root / ".cache"), str(stash / "cache"))

    result = _run(root, env)

    assert result.returncode != 0 and result.stdout == "", result.stdout
    err = result.stderr.strip()
    assert err.startswith("ERROR:"), err
    assert "provenance record missing" in err, f"reason: {err!r}"
    assert "never authenticates" in err, err
    assert result.stdout.strip() != "UNCHANGED"


def test_top_level_file_full_update(tmp_path: Path) -> None:
    """(F5): a manifest containing a TOP-LEVEL file (path with no '/'; the
    shipped manifest has several) must complete a full --update — pins the
    caller-owned dup-fd fix (walk_dirs never returns the borrowed base)."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    tip = "tip0000000000000000000000000000000000000002"
    topdata = b"top-level diagram bytes\n"
    top_tip = b"top-level diagram bytes changed\n"
    manifest = {
        "repository": REPO,
        "default_branch": BRANCH,
        "resolved_commit": PIN,
        "integrated_commit": PIN,
        "generated": "2026-10-24",
        "files": [
            {
                "path": "diagram.mmd",
                "bytes": len(topdata),
                "sha256": hashlib.sha256(topdata).hexdigest(),
                "git_blob_sha": _git_blob_sha(topdata),
            },
        ],
    }
    (upstream / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")
    (upstream / "diagram.mmd").write_bytes(topdata)
    env["AAID_FAKE_TIP_SHA"] = tip
    env["AAID_FAKE_TIP_OVERRIDES"] = json.dumps({"diagram.mmd": base64.b64encode(top_tip).decode()})

    result = _run(root, env, "--update")

    assert result.returncode == 0, f"--update stderr:\n{result.stderr}"
    assert result.stdout.strip() == f"UPDATED {tip}", result.stdout
    assert (upstream / "diagram.mmd").read_bytes() == top_tip
    new_manifest = json.loads((upstream / "MANIFEST.json").read_text())
    assert new_manifest["resolved_commit"] == tip
    assert new_manifest["integrated_commit"] == PIN  # fetch never advances it
    residue = list((root / ".cache").glob("staging-*")) if (root / ".cache").is_dir() else []
    assert not residue, "staging residue on the top-level path"


# ---------------------------------------------------------------------------
# Iteration-5: snapshot intermediate-symlink nofollow walk (MEDIUM, pre-open
# pivot) and fd-anchored staging cleanup (HIGH, substitution-at-any-point).
# ---------------------------------------------------------------------------


def test_snapshot_intermediate_symlink_refused(tmp_path: Path) -> None:
    """(iteration-5 Fix 1): the INTERMEDIATE directory components of a
    snapshot path are walked NOFOLLOW dirfd-relative — a pre-open pivot of
    assets/upstream/docs to an EXTERNAL matching-hash tree is a sanitized
    ERROR, never UNCHANGED (the old cap test only covered the FINAL
    component)."""
    root, upstream, source, bin_dir, env, pin1, tip2 = _fetched_unreviewed_fixture(tmp_path, with_integrated=True)
    # Matching-hash external tree for docs/ (the pivot is 'invisible' to
    # the hash discipline — the content is identical — so only the
    # nofollow intermediate walk can detect it).
    pivot_target = tmp_path / "pivot-mirror"
    (pivot_target / "docs").mkdir(parents=True)
    shutil.move(str(upstream / "docs/guide.md"), str(pivot_target / "docs/guide.md"))
    shutil.move(str(upstream / "docs"), str(upstream / "docs-original"))
    (upstream / "docs").symlink_to(pivot_target / "docs")

    result = _run(root, env)

    assert result.returncode != 0 and result.stdout == "", result.stdout
    err = result.stderr.strip()
    assert err.startswith("ERROR:"), err
    assert "is a symlink or not a directory" in err, f"reason: {err!r}"
    assert result.stdout.strip() != "UNCHANGED", "pre-open pivot laundered as UNCHANGED"


def test_staging_cleanup_spared_on_preopen_substitution(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """(iteration-5 Fix 2, helper-level): with the staging NAME substituted
    (checker owned dir renamed away, a FOREIGN POPULATED dir put under the
    staging name) BEFORE cleanup, remove_staging must: (a) emit ONE
    sanitized WARNING line naming the inode mismatch, and (b) SPARE the
    foreign dir byte-for-byte. The embedded-python harness calls
    remove_staging directly with fd identity anchored via the held
    staging fd (a rename of the real staging away does not disturb it)."""
    import os as _os

    ns = _load_checker_python(tmp_path)
    remove_staging = ns["remove_staging"]
    cache = tmp_path / "cache-boundary"
    cache.mkdir()
    staged = cache / "staging-A"
    (staged / "sub").mkdir(parents=True)
    (staged / "sub" / "guide.md").write_bytes(b"staged bytes\n")
    foreign = cache / "foreign-B"
    foreign.mkdir()
    (foreign / "trackfile.md").write_bytes(b"foreign bytes\n")
    # Attacker substitution: real staging renamed away; foreign dir takes
    # its NAME. The held staging fd still points at the REAL staging dir
    # (rename does not change fd identity).
    _os.rename(str(staged), str(cache / "stashed-A"))
    _os.rename(str(foreign), str(staged))

    cache_fd = _os.open(str(cache), _os.O_RDONLY | _os.O_DIRECTORY)
    staging_fd = _os.open(str(cache / "stashed-A"), _os.O_RDONLY | _os.O_DIRECTORY)
    ns["staging_name"] = "staging-A"
    ns["staging_fd"] = staging_fd
    ns["cache_fd"] = cache_fd
    ns["retain_staging"] = False

    remove_staging()

    # Exactly ONE sanitized WARNING line, naming the inode mismatch.
    captured = capsys.readouterr().err
    warn_lines = [line for line in captured.splitlines() if line.startswith("WARNING:")]
    assert len(warn_lines) == 1, f"exactly one warning required: {captured!r}"
    assert "inode mismatch" in warn_lines[0], warn_lines[0]
    assert "substituted mid-run" in warn_lines[0], warn_lines[0]

    # Foreign dir survived byte-for-byte (now reachable under the staging-A
    # name AFTER the checker's cleanup skipped); the real dir (stashed-A)
    # also survives.
    assert (staged / "trackfile.md").read_bytes() == b"foreign bytes\n"
    assert (cache / "stashed-A" / "sub" / "guide.md").read_bytes() == b"staged bytes\n"
    _os.close(cache_fd)  # staging_fd was closed by remove_staging


def test_delete_contents_fd_recurses_and_refuses_symlink(tmp_path: Path) -> None:
    """(iteration-5 Fix 2, helper-level): delete_contents_fd deletes nested
    staged contents dirfd-relative and REFUSES a symlinked SUB-DIRECTORY
    child (raise _RefuseCleanup, target spared) — deletion never follows a
    link it cannot prove is checker-owned."""
    import os as _os

    ns = _load_checker_python(tmp_path)
    delete_contents_fd = ns["delete_contents_fd"]
    Refuse = ns["_RefuseCleanup"]
    root_dir = tmp_path / "unit-root"
    target = root_dir / "spared-target"
    (target / "inner").mkdir(parents=True)
    (target / "inner" / "file.md").write_bytes(b"precious\n")
    staging = root_dir / "staging-A"
    (staging / "docs").mkdir(parents=True)
    (staging / "docs" / "guide.md").write_bytes(b"staged\n")
    (staging / "top.md").write_bytes(b"top\n")
    (staging / "bad-link").symlink_to(target)

    staging_fd = _os.open(str(staging), _os.O_RDONLY | _os.O_DIRECTORY)
    with pytest.raises(Refuse):
        delete_contents_fd(staging_fd, "staging cleanup")
    # The foreign symlink TARGET is byte-identical (nothing followed).
    assert (target / "inner" / "file.md").read_bytes() == b"precious\n"
    # The staged REAL contents that were deleted before raise time are gone
    # as deleted (order-independent: at least the raise happened; the link
    # name itself remains — never followed, target untouched).
    assert (staging / "bad-link").is_symlink(), "planted link was removed instead of refused"
    _os.close(staging_fd)


def test_staging_cleanup_success_path_helper(tmp_path: Path) -> None:
    """(iteration-5 Fix 2, helper-level): the happy path — matching
    identity — deletes contents AND the top name dirfd-relative (no
    residue)."""
    import os as _os

    ns = _load_checker_python(tmp_path)
    remove_staging = ns["remove_staging"]
    cache = tmp_path / "cache-boundary"
    cache.mkdir()
    staging = cache / "staging-A"
    (staging / "docs").mkdir(parents=True)
    (staging / "docs" / "guide.md").write_bytes(b"staged\n")

    cache_fd = _os.open(str(cache), _os.O_RDONLY | _os.O_DIRECTORY)
    staging_fd = _os.open(str(staging), _os.O_RDONLY | _os.O_DIRECTORY)
    ns["staging_name"] = "staging-A"
    ns["staging_fd"] = staging_fd
    ns["cache_fd"] = cache_fd
    ns["retain_staging"] = False

    remove_staging()

    assert not staging.exists(), "top staging name not removed"
    residue = list(cache.iterdir())
    assert residue == [], f"residue: {[str(p) for p in residue]}"
    _os.close(cache_fd)  # staging_fd was closed by remove_staging


# ---------------------------------------------------------------------------
# Iteration-6: identity-verified enumeration→open/act in fd-anchored cleanup.
# ---------------------------------------------------------------------------


def test_identity_matches_helper(tmp_path: Path) -> None:
    """(unit): the extracted comparison helper — same dev/ino → True;
    differing dev or ino → False (differing dev also covered synthetically:
    simple namespace stat stand-ins with distinct st_dev values)."""
    import os as _os
    from types import SimpleNamespace

    ns = _load_checker_python(tmp_path)
    identity_matches = ns["identity_matches"]
    base = tmp_path / "id-root"
    (base / "a").mkdir(parents=True)
    (base / "b").mkdir(parents=True)
    (base / "f1").write_bytes(b"x\n")
    (base / "f2").write_bytes(b"y\n")
    a = _os.stat(str(base / "a"))
    b = _os.stat(str(base / "b"))
    f1 = _os.stat(str(base / "f1"))
    f2 = _os.stat(str(base / "f2"))
    assert identity_matches(a, a)
    assert identity_matches(f1, f1)
    assert not identity_matches(a, b)
    assert not identity_matches(f1, f2)
    # Synthetic cross-device leg: differing st_dev → False even when ino
    # matches (identity_matches reads only st_dev/st_ino).
    busy = SimpleNamespace(st_dev=123, st_ino=f1.st_ino)
    assert not identity_matches(f1, busy)
    assert not identity_matches(busy, f1)
    assert not identity_matches(busy, SimpleNamespace(st_dev=123, st_ino=f1.st_ino + 1))
    assert identity_matches(busy, SimpleNamespace(st_dev=123, st_ino=f1.st_ino))


def test_cleanup_child_substitution_refused(tmp_path: Path) -> None:
    """(HIGH, helper-level): the child INODE enumerated via scandir fd is
    replaced (rename-away + foreign populated dir under the SAME name)
    between enumeration and open — the identity check refuses the cleanup:
    _RefuseCleanup raised at the HELPER level only (the refusal path that
    remove_staging converts into the ONE sanitized WARNING, itself covered
    by the dedicated remove_staging substitution tests); the foreign tree
    (and the stashed real staging subtree) survive byte-for-byte. The
    interleave is modelled by patching open_dir_at in the extracted
    namespace to perform the substitution exactly between the enumeration
    stat and the real open."""
    import os as _os
    import shutil as _shutil

    ns = _load_checker_python(tmp_path)
    delete_contents_fd = ns["delete_contents_fd"]
    Refuse = ns["_RefuseCleanup"]
    real_open_dir_at = ns["open_dir_at"]
    cache = tmp_path / "cache-boundary"
    cache.mkdir()
    staging = cache / "staging-A"
    (staging / "docs").mkdir(parents=True)
    (staging / "docs" / "guide.md").write_bytes(b"staged bytes\n")
    foreign_tree = tmp_path / "foreign-tree"
    foreign_tree.mkdir()
    (foreign_tree / "trackfile.md").write_bytes(b"foreign bytes\n")
    stash_path = staging / "docs-stashed"
    foreign_dest = staging / "docs"

    def substituting_open(base_fd, name, what):
        # The attacker's between-enum-and-open move: rename the enumerated
        # child away and move a foreign populated dir into the name.
        if name == "docs":
            _os.rename(str(staging / name), str(stash_path))
            _shutil.copytree(str(foreign_tree), str(foreign_dest))
        return real_open_dir_at(base_fd, name, what)

    ns["open_dir_at"] = substituting_open

    staging_fd = _os.open(str(staging), _os.O_RDONLY | _os.O_DIRECTORY)
    with pytest.raises(Refuse):
        delete_contents_fd(staging_fd, "staging cleanup")
    _os.close(staging_fd)

    # Foreign tree content survived inside the substituted name...
    assert (foreign_dest / "trackfile.md").read_bytes() == b"foreign bytes\n"
    # ...and the REAL staged subtree (renamed away) also survives.
    assert (stash_path / "guide.md").read_bytes() == b"staged bytes\n"
