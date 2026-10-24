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
    line removed, (b) truncated block with no END marker — check-only must
    ERROR 'malformed check-status block', never silently fall back to the
    manifest resolved_commit (which would read pin==tip and report a false
    UNCHANGED after an interrupted cutover). Pinned contract change
    disclosed: both corrupt states previously degraded to UNCHANGED.
    (c) ENTIRELY ABSENT SOURCE.md keeps old fallback semantics: pin==tip
    fixture yields UNCHANGED (guard-rails fixture equivalent)."""
    root, upstream, source, env = _i5_fixture(tmp_path, mutation)
    before = _snapshot(root)
    result = _run(root, env)

    if mutation == "absent_source":
        assert result.returncode == 0, f"stderr:\n{result.stderr}"
        assert result.stdout.strip() == "UNCHANGED", result.stdout
    else:
        assert result.returncode != 0 and result.stdout == "", (
            f"{mutation}: stdout {result.stdout!r} stderr {result.stderr!r}"
        )
        assert "ERROR: malformed check-status block" in result.stderr, result.stderr
    assert _snapshot(root) == before, "run modified the fixture root"


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
    these docstrings) do NOT trip it; a SOURCE.md with no marker substring
    and no block keeps old absent-block semantics: UNCHANGED in the
    pin==tip fixture."""
    root, upstream, source, bin_dir, env = _harden_fixture(tmp_path)
    source.write_text("# Source provenance — fixture\n\nNo block here yet.\n")
    r1 = _run(root, env)
    assert r1.returncode == 0 and r1.stdout.strip() == "UNCHANGED", r1.stdout

    # ...and the marker substring must look like a marker attempt ON ITS
    # OWN line? No — substring-in-line is the contract: any line containing
    # BEGIN CHECK-STATUS (even mid-line prose quoting the token) counts as
    # a trace and yields ERROR once strict validation cannot complete.
    source.write_text("# Provenance\n\nSomeone wrote BEGIN CHECK-STATUS inside a sentence.\n")
    r2 = _run(root, env)
    assert r2.returncode != 0, r2.stdout
    assert "malformed check-status block" in r2.stderr, r2.stderr
