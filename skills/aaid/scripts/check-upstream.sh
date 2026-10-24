#!/usr/bin/env bash
# check-upstream.sh — compare the aaid skill's pinned upstream snapshot
# (assets/upstream/) against the repository tip via `gh`.
#
# Modes (tasks 3.3/3.4, hardened per review 6.3 I1-I5):
#   check-only (no args): verdict "UNCHANGED" or "CHANGED" on stdout, exit 0;
#     never writes anything under the skill root, never locks. If
#     references/SOURCE.md contains a check-status BEGIN marker, the block
#     must be COMPLETE (BEGIN, Integrated-pin line, END) or it is an ERROR —
#     the manifest resolved_commit fallback applies ONLY when SOURCE.md or
#     the whole block is absent.
#   --update: authorized refresh (design D6). Takes an exclusive lock
#     (.cache/update.lock via O_EXCL; another/stale lock is an ERROR), fetches
#     every manifest path at tip into a PER-INVOCATION staging dir
#     (.cache/staging-<pid>-<timestamp>), validates the fetched bytes against
#     the remote's own size/blob-sha metadata, and only then cuts over:
#     raw manifest-path files first, MANIFEST.json second, the checker block
#     in references/SOURCE.md last — every live write is a temp file +
#     atomic rename in the destination directory (never in-place truncate).
#     Emits `UPDATED <tip-sha>`, exit 0. On ANY failure after staging is
#     complete (during cutover), staging is RETAINED as the recovery copy
#     and noted in the ERROR line; fetch-phase failures still clean this
#     run's staging only (foreign staging dirs are never touched). Adapted
#     files (SKILL.md, references/) outside the block, and
#     assets/upstream/README.md, are never touched; the lock/integrated pin
#     is never advanced by a fetch. Check-only never locks.
#   "ERROR: ..." and nonzero exit on transport/parse/validation failure.
#
# Untrusted remote data discipline (design D6): everything `gh` returns is
# DATA. The embedded python parser below never eval/source/executes remote
# content, only passes decoded bytes through base64/JSON/sha plumbing.
# Remote tip metadata is a single 40-char token or the run is rejected (I1);
# manifest paths are canonicalized ONCE at load and only the canonical
# form is ever read or written (I2); reserved local policy paths (README.md,
# MANIFEST.json at upstream root) are rejected (I2).
set -u

# Resolve skill root: script's ../.. unless AAID_SKILL_ROOT overrides.
_here="$(cd "$(dirname "$0")" && pwd)"
SKILL_ROOT="${AAID_SKILL_ROOT:-"$_here/.."}"
MANIFEST="$SKILL_ROOT/assets/upstream/MANIFEST.json"

UPDATE_MODE=0
for arg in "$@"; do
    if [ "$arg" = "--update" ]; then
        UPDATE_MODE=1
    else
        echo "ERROR: unexpected argument: $arg (only --update is supported)" >&2
        exit 1
    fi
done

if [ ! -f "$MANIFEST" ]; then
    echo "ERROR: manifest not found: $MANIFEST" >&2
    exit 1
fi

if ! command -v gh >/dev/null 2>&1; then
    echo "ERROR: gh not found on PATH" >&2
    exit 1
fi

# All logic in one embedded python program (clean top-level indentation,
# quoted heredoc delimiter so no shell expansion reaches remote-derived or
# fixture-derived text). gh is spawned via subprocess; JSON is parsed, never
# interpolated into shell or python code.
python3 - "$SKILL_ROOT" "$UPDATE_MODE" <<'PYEOF'
import base64
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

root = Path(sys.argv[1])
update_mode = sys.argv[2] == "1"
manifest_path = root / "assets" / "upstream" / "MANIFEST.json"
source_path = root / "references" / "SOURCE.md"
# Per-invocation staging (I4): created lazily, exactly one per run, removed
# by this run only; shared fixed-name staging would let concurrent runs
# delete or interleave each other's staged files.
cache_dir = root / ".cache"
lock_path = cache_dir / "update.lock"

BEGIN = re.compile(r"<!-- BEGIN CHECK-STATUS.*?-->\n?", re.S)
END = re.compile(r"<!-- END CHECK-STATUS -->")

# Module-level run ownership state (I3/I4):
staging = None          # this run's own staging dir, once created
lock_fd = None          # this run's own update.lock descriptor, once held
retain_staging = False  # True once staging holds a COMPLETE fetched snapshot


def sanitize(reason):
    """D6: failure reasons are output — sanitize to ONE printable line.
    Control characters (incl. newlines, ESC/ANSI) are removed, whitespace
    runs collapsed, and the line capped, so server-influenced stderr from gh
    can never spoof a verdict line or inject escapes into the verdict channel."""
    text = "".join(ch if ch.isprintable() else " " for ch in reason)
    return " ".join(text.split())[:300]


def fail(reason):
    # Cleanup is strictly this run's own state (I4): only the staging dir
    # THIS run created, only the lock THIS run holds. A failing check-only
    # run owns neither, so it can never remove an updater's staging.
    if staging is not None and staging.is_dir() and not retain_staging:
        shutil.rmtree(staging, ignore_errors=True)
    if lock_fd is not None:
        try:
            os.close(lock_fd)
        except OSError:
            pass
        try:
            os.unlink(lock_path)
        except OSError:
            pass
    message = str(reason)
    if retain_staging and staging is not None:
        # The staging copy is the recovery snapshot; point at it, sanitized
        # together with the reason (I3).
        try:
            rel = staging.relative_to(root)
        except ValueError:
            rel = staging
        message += " staging retained at " + str(rel)
    # Unified ERROR channel: stderr (shell pre-checks use stderr too);
    # verdict lines (UNCHANGED/CHANGED/UPDATED) stay on stdout.
    print(f"ERROR: {sanitize(message)}", file=sys.stderr)
    sys.exit(1)


def fresh(date, tip):
    """Check-status lines emitted by an authorized refresh (D6):
    machine-updatable block contents, integrated pin preserved separately."""
    # NOTE: date/is None-safe; tip is the validated fetched commit, never the pin.
    return (f"- Last successful check: {date}\n"
            f"- Fetched commit: `{tip}`\n")


def atomic_write(dest, data):
    """Cutover discipline (I3 + round-2 blocker 2): every live-file write
    replaces the whole file via a UNIQUE UNPREDICTABLE temp file created
    with O_CREAT|O_EXCL (and O_NOFOLLOW where available, so a planted
    symlink at the temp path cannot redirect the write) in the SAME
    directory, written through the exclusive fd, then os.replace()'d onto
    the destination. No in-place truncation, no predictable/hard-linkable
    temp name; fsync is intentionally skipped (no power-loss durability
    claim). os.replace replaces the dest ENTRY itself and does NOT follow a
    destination symlink: a symlinked dest ends as a regular file and the
    symlink's target keeps its old bytes."""
    dest = Path(dest)
    if dest.exists() and not os.access(dest, os.W_OK):
        raise PermissionError(f"write destination is not writable: {dest}")
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0)
    for _ in range(8):
        # Random hex suffix: unpredictable, unguessable temp name.
        tmp = dest.parent / f".{dest.name}.tmp-{os.getpid()}-{os.urandom(8).hex()}"
        try:
            fd = os.open(tmp, flags, 0o600)
        except FileExistsError:
            continue
        break
    else:
        raise OSError("could not create a unique temp file next to " + str(dest))
    tmp_bytes = tmp
    try:
        with os.fdopen(fd, "wb") as fh:
            fh.write(data)
        os.replace(tmp_bytes, dest)
    finally:
        if tmp_bytes.exists():
            try:
                tmp_bytes.unlink()
            except OSError:
                pass


def main():
    global staging, lock_fd, retain_staging

    if update_mode:
        # Exclusive update lock (I4); read-only-other... no-lock-check-only.
        # Simplest correct protocol: O_EXCL create; a second updater (or a
        # stale lock from a killed run) is a hard ERROR with a manual-removal
        # pointer, never a silent concurrent run.
        try:
            cache_dir.mkdir(parents=True, exist_ok=True)
        except OSError as exc:
            fail(f"cannot create update cache dir: {exc}")
        try:
            lock_fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            fail(
                "another update in progress or stale lock"
                " (remove .cache/update.lock if stale)"
            )
        except OSError as exc:
            fail(f"cannot acquire update lock: {exc}")

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except ValueError:
        # Explicit local-input reason (cheap, blocks every later check);
        # remaining unexpected failures route through main()'s caller.
        fail("invalid manifest JSON in " + str(manifest_path))

    # Path canonicalization + containment (design D6 "unsafe paths"; I2).
    # Every manifest entry's path is validated and CANONICALIZED before any
    # read or write ever uses it; ONLY the canonical in-upstream relative
    # form is stored back and used by every later operation (local snapshot
    # reads, staging writes, cutover writes, manifest regeneration). A
    # non-canonical spelling that RESOLVES inside upstream (e.g.
    # ../../assets/upstream/docs/guide.md, docs/../docs/guide.md) therefore
    # stages and cuts over at its canonical location inside the snapshot —
    # never via an alias spelling that staging would resolve elsewhere.
    # Reserved local policy paths are rejected outright.
    #(c) Reserved local policy protection (6.3 I2 + round-2 blocker 1).
    #reserved_paths names the policy files AT THE UPSTREAM ROOT. Root-level
    #collisions are rejected CASE-INSENSITIVELY (a manifest entry like
    #`readme.md` addresses the local README.md on case-insensitive
    #filesystems such as macOS default). Only ROOT-LEVEL casefolded
    #collisions are rejected: a nested `docs/readme.md` is an upstream
    #asset and stays allowed — the protection is about overwriting the
    #local policy file at the snapshot root, not about the name anywhere.
    reserved_roots = {"readme.md", "manifest.json"}
    upstream_dir = (root / "assets" / "upstream").resolve()
    canonical_entries = []
    for entry in manifest["files"]:
        raw = entry["path"]
        if not isinstance(raw, str) or not raw.strip():
            fail("unsafe manifest path (empty or non-string entry)")
        if raw != raw.strip() or raw.endswith("/"):
            fail("unsafe manifest path (unnormalized spelling): " + raw)
        p = Path(raw)
        if p.is_absolute():
            fail("unsafe manifest path (absolute): " + raw)
        # Containment resolves the PARENT directory chain (catching directory
        # symlink escapes) but does NOT follow the FINAL component: a local
        # symlink swapped in AT a live destination is a manipulated-local-
        # layout case that os.replace handles safely (it replaces the entry,
        # not the target) — resolving it here would misread the asset as an
        # escape and break the round-2 blocker-2 contract.
        parent_resolved = (upstream_dir / p.parent).resolve()
        if parent_resolved != upstream_dir and upstream_dir not in parent_resolved.parents:
            fail("unsafe manifest path (escapes assets/upstream/): " + raw)
        canonical = os.path.relpath(parent_resolved, upstream_dir)
        canonical = os.path.normpath(os.path.join(canonical, p.name))
        if canonical == ".":
            fail("unsafe manifest path (resolves to assets/upstream root): " + raw)
        if os.sep not in canonical and canonical.casefold() in reserved_roots:
            fail("unsafe manifest path (reserved local policy file): " + raw)
        # Re-verify the canonical form stays inside upstream (lexical belt).
        if os.path.normpath(os.path.join(str(upstream_dir), canonical)) != \
                os.path.normpath(os.path.join(str(parent_resolved), p.name)):
            fail("unsafe manifest path (non-canonical after normalize): " + raw)
        entry["path"] = canonical
        canonical_entries.append(entry)
    manifest["files"] = canonical_entries

    repo = manifest["repository"]
    if not isinstance(repo, str) or not repo.strip():
        fail("manifest repository missing or not a string")
    repo = repo.strip()
    # Accept a full https URL as well as bare owner/repo; normalize to the
    # bare owner/repo that `gh api` expects. Pure string plumbing on the
    # manifest's own data — no remote content involved.
    if repo.startswith(("https://", "http://")):
        tail = repo.split("://", 1)[1]
        _, _, tail = tail.partition("/")  # drop host
        repo = tail
    repo = repo.strip("/")
    if not re.match(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$", repo) or \
            repo.startswith(("/", ".")) or "/.." in repo:
        fail("unsafe manifest repository reference: " + str(repo))
    branch = manifest["default_branch"]

    def gh_json(endpoint, fields=None):
        """Run `gh api` and parse stdout as JSON. Remote JSON is data only."""
        cmd = ["gh", "api", "--method", "GET", endpoint]
        for kv in fields or []:
            cmd += ["-f", kv]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0:
            fail(f"gh api failed for {endpoint}: {proc.stderr.strip()}")
        try:
            obj = json.loads(proc.stdout)
        except ValueError:
            fail(f"gh api returned invalid JSON for {endpoint}")
        if not isinstance(obj, dict):
            # Domain-specific shape guard: non-dict documents (list/string/
            # number) would otherwise surface as AttributeError tracebacks.
            fail(f"invalid JSON shape for {endpoint}: expected object")
        return obj

    def content_bytes(path, sha):
        """Fetch one file's content bytes at a commit (base64), validated against
        the response's own size/blob-sha metadata. Remote bytes stay data only."""
        resp = gh_json(f"repos/{repo}/contents/{path}", [f"ref={sha}"])
        if resp.get("encoding") != "base64":
            fail(f"unexpected encoding for {path}")
        if not resp.get("content"):
            fail(f"missing content payload for {path}")
        try:
            # GitHub base64 payloads embed '\n' wrappers; strip all
            # whitespace before strict decode.
            payload = re.sub(r"\s+", "", resp["content"])
            data = base64.b64decode(payload, validate=True)
        except (ValueError, TypeError):
            fail(f"content payload not valid base64 for {path}")
        if resp.get("size") != len(data):
            fail(f"size mismatch from remote metadata for {path}")
        if resp.get("sha") is None:
            fail(f"API omitted the declared blob sha for {path}")
        blob_sha = hashlib.sha1(b"blob %d\x00" % len(data) + data).hexdigest()
        if resp["sha"] != blob_sha:
            fail(f"blob sha mismatch from remote metadata for {path}")
        return data

    tip_resp = gh_json(f"repos/{repo}/commits/{branch}")
    if not tip_resp.get("sha"):
        fail(f"tip commit response declared no sha for branch {branch}")
    tip = tip_resp["sha"]
    # I1: the tip sha is remote metadata that is INTERPOLATED into output
    # (verdict lines, SOURCE block). Truthiness is not enough: require a
    # strict single-token sha (16-64 alphanumeric chars — real commits are
    # exactly 40 hex) so newlines/backticks/ANSI in the response can never
    # inject provenance text or forge output lines.
    if not isinstance(tip, str) or not re.fullmatch(r"[0-9A-Za-z]{16,64}", tip):
        fail(f"tip commit response declared an invalid sha for branch {branch}")

    # Snapshot validation first: every manifest path's local bytes must match
    # the manifest hashes (both modes). Read strictly by canonical path.
    for entry in manifest["files"]:
        path = entry["path"]
        local = root / "assets" / "upstream" / path
        data = local.read_bytes()
        if len(data) != entry["bytes"] or hashlib.sha256(data).hexdigest() != entry["sha256"]:
            fail("local snapshot mismatch for " + path)

    if not update_mode:
        # Verdict baseline is the INTEGRATED pin (reviewed content, D6), read
        # from the SOURCE.md check-status block, NOT the manifest's
        # resolved_commit: after an authorized --update the manifest legitimately
        # holds fetched-but-unreviewed content, and a baseline on it would
        # wrongly report UNCHANGED. Fall back to the manifest resolved_commit
        # ONLY when SOURCE.md (or the whole BEGIN-marker block) is ABSENT
        # (older fixtures/pre-block snapshots, where manifest pin ==
        # integrated pin anyway). A source file that HAS the BEGIN marker but
        # is malformed (missing/broken END, missing Integrated-pin line) is a
        # runtime-produced corruption state (6.3 I5) and MUST fail loudly —
        # silently falling back would report a false UNCHANGED after an
        # interrupted cutover.
        src_text = None
        if source_path.is_file():
            src_text = source_path.read_text(encoding="utf-8")
        baseline = manifest["resolved_commit"]
        if src_text is not None:
            # Marker-trace discipline (6.3 I5 + round-2 blocker 3): a
            # TRUNCATED marker attempt like `<!-- BEGIN CHECK-STATUS` (file
            # cut mid-write) does not satisfy the strict BEGIN regex, but it
            # is NOT an absent block: any line containing the substring
            # "BEGIN CHECK-STATUS" counts as a marker attempt (deliberately
            # loose — prose that merely mentions checkboxes must not trip
            # this), and if the strict full-marker / END / pin validation
            # then fails, the run is an ERROR. Absent-fallback applies ONLY
            # when no such line exists anywhere.
            trace = any(
                "begin check-status" in line.casefold() for line in src_text.splitlines()
            )
            b = BEGIN.search(src_text)
            if trace and not b:
                fail("malformed check-status block (truncated BEGIN marker) in references/SOURCE.md")
            if b:
                e = END.search(src_text, b.end())
                if not e:
                    fail("malformed check-status block (no END marker) in references/SOURCE.md")
                block = src_text[b.end():e.start()]
                line = re.search(r"- Integrated pin: `([^`\n]+)`", block)
                if not line:
                    fail("malformed check-status block (no Integrated pin line) in references/SOURCE.md")
                # The pin token is opaque here (checker resolves it via gh);
                # anything backquoted on the first Integrated pin line counts.
                baseline = line.group(1)
            # No marker trace at all: SOURCE.md present but with no block and
            # no attempt at one — treat like an absent block (pre-block
            # fixture semantics).
        for entry in manifest["files"]:
            path = entry["path"]
            pinned = content_bytes(path, baseline)
            at_tip = content_bytes(path, tip)
            # data's sha256 == the manifest's is already guaranteed by the local
            # check above. UNCHANGED only when the integrated pin's content
            # matches the tip ref per path (baseline == tip makes this vacuous
            # but the fetches stay data-only, no verdict shortcut needed).
            if pinned != at_tip:
                print("CHANGED")
                sys.exit(0)
        print("UNCHANGED")
        sys.exit(0)

    # ---- authorized refresh (--update), design D6 ----
    # Stage the COMPLETE tip snapshot first; any failure before this point is
    # a fetch-phase failure: fail() removes THIS run's staging, the tracked
    # files and SOURCE.md stay untouched (pinned cleanup semantics).
    try:
        staging = cache_dir / f"staging-{os.getpid()}-{time.time_ns()}"
        staging.mkdir(parents=True)
    except OSError as exc:
        fail(f"cannot create staging dir: {exc}")

    new_files = []
    for entry in manifest["files"]:
        path = entry["path"]
        data = content_bytes(path, tip)
        # Staging writes use ONLY the canonical path (I2): by construction it
        # cannot escape this run's staging dir.
        dest = staging / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        new_files.append(
            {
                "path": path,
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
                "git_blob_sha": hashlib.sha1(b"blob %d\x00" % len(data) + data).hexdigest(),
            }
        )

    new_manifest = dict(manifest)
    new_manifest["resolved_commit"] = tip
    new_manifest["generated"] = time.strftime("%Y-%m-%d", time.gmtime())
    new_manifest["files"] = new_files
    atomic_write(
        staging / "MANIFEST.json", (json.dumps(new_manifest, indent=2) + "\n").encode()
    )
    # SOURCE.md check-status block must exist and keep the integrated pin line
    # (outside the block) untouched; the block itself is checker-maintained.
    if not source_path.is_file():
        # Specific reason for the hygiene-contract case (a missing/removed
        # SOURCE.md is a common partial state; the generic router would say
        # only "unexpected FileNotFoundError").
        fail("SOURCE.md not found for authorized refresh: " + str(source_path))
    old_text = source_path.read_text(encoding="utf-8")
    b = BEGIN.search(old_text)
    e = END.search(old_text)
    if not b or not e or not b.end() <= e.start():
        fail("SOURCE.md check-status block missing or malformed")
    old_block = old_text[b.end():e.start()]
    lines = old_block.splitlines()
    pin_start = next(
        (i for i, l in enumerate(lines) if l.startswith("- Integrated pin")), None
    )
    if pin_start is None:
        fail("check-status block has no Integrated pin line")
    # Preserve the COMPLETE Integrated pin entry (it may wrap over several
    # physical lines; the indented continuation lines belong to the entry). The
    # entry is the last entry of the block, so it runs to the block end.
    pin_entry = "\n".join(lines[pin_start:])
    new_block = fresh(time.strftime("%Y-%m-%d", time.gmtime()), tip) + pin_entry

    # Cutover (I3): temp-file + atomic-rename for EVERY live file, ordered so
    # the crash window is narrow and every partial state is detectable —
    # raw snapshot files first, MANIFEST.json second, SOURCE.md block last.
    # Crash-window table (accurate, supersedes any blanket "next check is
    # always ERROR" claim):
    #   (i)   crash before the first live replacement → prior state intact;
    #         next check UNCHANGED/CHANGED as before the refresh.
    #   (ii)  crash during raw-file replacement → old MANIFEST hashes vs new
    #         raw bytes → next check ERROR "local snapshot mismatch".
    #   (iii) crash after MANIFEST replaced, before SOURCE → coherent
    #         fetched snapshot + OLD integrated pin → next check CHANGED
    #         (not ERROR, and never UNCHANGED).
    #   (iv)  crash after SOURCE written → complete cutover; residue (if a
    #         crash skips cleanup) is staging/lock dirs, recoverable by the
    #         next run or manually.
    # No fsync / power-loss durability claim: this narrows the failure
    # window under ordinary process death, not under abrupt power loss.
    # On any HANDLED failure from here on, staging is RETAINED as the
    # recovery copy (fail() honors retain_staging and names the path).
    retain_staging = True
    for entry in new_files:
        src = staging / entry["path"]
        atomic_write(root / "assets" / "upstream" / entry["path"], src.read_bytes())
    atomic_write(manifest_path, (staging / "MANIFEST.json").read_bytes())
    atomic_write(
        source_path,
        (old_text[: b.end()] + new_block.rstrip("\n") + "\n" + old_text[e.start():]).encode("utf-8"),
    )

    shutil.rmtree(staging)
    if lock_fd is not None:
        os.close(lock_fd)
        lock_fd = None
        os.unlink(lock_path)
    print(f"UPDATED {tip}")
    sys.exit(0)


try:
    main()
except SystemExit:
    raise
except Exception as exc:  # noqa: BLE001 - D6: never escape a raw traceback
    # Route any unexpected failure (including cutover I/O failures) to the
    # sanitized ERROR verdict with nonzero exit. fail() retains staging when
    # a complete snapshot is staged and removes only this run's own state;
    # live files may be mid-cutover — see the crash-window table in the
    # cutover section for what the next check will report per window.
    fail(f"unexpected {type(exc).__name__}: {exc}")
PYEOF
