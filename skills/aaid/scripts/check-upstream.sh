#!/usr/bin/env bash
# check-upstream.sh — compare the aaid skill's pinned upstream snapshot
# (assets/upstream/) against the repository tip via `gh`.
#
# THREAT MODEL (binding, closure-gate iter-3):
#   IN scope: a concurrent SAME-USER local process able to create/rename/
#     modify files and directories anywhere user write access exists,
#     INCLUDING rename/swap attacks on the skill root itself; upstream-
#     controlled transport responses and content bytes; careless local
#     cleanup (e.g. a stale lock or leftover staging from a killed run).
#   OUT of scope (documented, not defended here): hostile direct editing of
#     the checker script or of the provenance records themselves (manifest/
#     SOURCE bytes) — whoever can edit those already has arbitrary-code-
#     execution power over this skill; a compromised or sysroot-swapped gh
#     binary; the operator's invocation environment (PATH, env vars).
#
# Modes (hardened per adversarial review; closure-gate semantics):
#   check-only (no args): verdict "UNCHANGED" or "CHANGED" on stdout, exit 0;
#     never writes anything under the skill root, never locks. The verdict
#     baseline is the human-integrated pin: the SOURCE.md check-status
#     Integrated pin when SOURCE exists, otherwise the manifest
#     integrated_commit. A manifest WITHOUT integrated_commit and without
#     SOURCE.md is an ERROR — ABSENCE OF PROVENANCE NEVER AUTHENTICATES
#     (the legacy first-run resolved_commit default is REMOVED; genuine
#     first-run vendoring REQUIRES the new-schema manifest, which the
#     shipped assets/upstream/MANIFEST.json carries). If
#     references/SOURCE.md contains a check-status BEGIN marker, the block
#     must be COMPLETE (BEGIN, Integrated-pin line, END) or it is an ERROR;
#     a SOURCE.md that is itself a symlink (or has a symlinked ancestor)
#     is tampered provenance — ERROR. Fetched-only state can never yield
#     UNCHANGED, regardless of directory presence.
#   --update: authorized refresh. Takes an exclusive lock
#     (.cache/update.lock via O_EXCL; another/stale lock is an ERROR with the
#     lock age and manual-removal instructions, never auto-removed), fetches
#     every manifest path at tip into a PER-INVOCATION staging dir
#     (.cache/staging-<pid>-<timestamp>), validates the fetched bytes against
#     the remote's own size/blob-sha metadata, and only then cuts over:
#     raw manifest-path files first, MANIFEST.json second, the checker block
#     in references/SOURCE.md last — every live write AND every staging
#     write is a temp file + atomic rename anchored on validated directory
#     fds (never in-place truncate, never a plain write through a planted
#     symlink). Emits `UPDATED <tip-sha>`, exit 0. On ANY failure after
#     staging is complete (during cutover), staging is RETAINED as the
#     recovery copy and noted in the ERROR line; fetch-phase failures still
#     clean this run's staging only (foreign staging dirs are never
#     touched). Adapted files (SKILL.md, references/) outside the block, and
#     assets/upstream/README.md, are never touched; the integrated pin (and
#     the manifest integrated_commit) is never advanced by a fetch — only
#     synced when a subsequent authorized update finds the SOURCE block pin
#     already equal to the previously fetched resolved commit (a
#     human-integrated state). Check-only never locks.
#   "ERROR: ..." and nonzero exit on transport/parse/validation failure.
#
# Boundary discipline (closure-gate): the skill root is pinned ONCE at
# startup as a DIRECTORY FD (final-component nofollow, fstat-backed
# identity), re-verified before EVERY write; ALL containment checks and ALL
# writes are dirfd-relative (no string re-resolution of the base anywhere).
# Every trusted read (manifest, SOURCE.md) opens its file O_NOFOLLOW and
# fstats the SAME fd before reading, requiring S_ISREG — a symlinked record
# is tampered provenance and a FIFO/device refusal is fast (no unbounded
# read through a FIFO). LOCAL SNAPSHOT reads are a pinned contract exception:
# they FOLLOW a final-component symlink (replace-not-follow semantics at the
# write side), are SIZE-CAPPED at the manifest-declared bytes + 64KB slack
# (sanitized ERROR beyond — /dev/zero redirection cannot drive an unbounded
# read), and intermediate components are walked nofollow by the dirfd walk.
#
# Transport bounds (closure-gate): every gh call is bounded END-TO-END —
# a checker-enforced wall-clock deadline (AAID_CHECK_TIMEOUT, default 30s,
# clamped to <=600s, non-finite values rejected) applied while streaming
# BOTH stdout and stderr (select over both fds so stderr can never fill
# its pipe), a RAW stdout cap (kill + reject beyond 4MB, read incrementally
# so nothing oversized is ever buffered), a stderr cap, and a deadline-
# bounded post-EOF wait (gh closing stdout then blocking is killed and
# reported, not waited on forever).
#
# Residual (approved wording, binding): pre-open parent/root pivots do not
# redirect fd-anchored writes (writes land in the pinned inode tree —
# verify_boundary / verify_cache_identity before every write detect a
# persistent pathname swap). Cleanup protection is identity-verified —
# nofollow walks throughout. Two substitution outcomes are deliberately
# distinct, stated precisely: (1) a substituted STAGING TEMP is a
# WRITE-path condition — verdict-fatal fail()/ERROR ("staging temp was
# substituted mid-write", inode mismatch at replace time); only (2) the
# CLEANUP mismatches (substituted staged dir, substituted child) skip
# that cleanup with ONE sanitized WARNING and spare the foreign tree.
# Child identity is verified at enumeration→open (scandir stat vs fstat
# of the opened directory fd), BEFORE recursion; the child
# rmdir(name, dir_fd=parent) acts on the already-verified name with no
# fresh comparison. Three documented windows are
# accepted/design behavior, stated explicitly:
#   (a) post-open relocation of an already-opened descriptor between the
#       final identity check and the anchored operation — THE approved
#       residual (not closable in userspace);
#   (b) content planted inside the checker-created staging directory
#       BEFORE enumeration is deleted with the staging tree — the staging
#       dir is checker-owned space with an unpredictable name;
#   (c) the final top-name rmdir can at most remove an EMPTY replacement
#       directory (rmdir never recurses; a populated substitute fails the
#       rmdir → refuse + warn).
# The ONLY accepted residual outside these design windows is the same-user
# rename/relocation of already-opened descriptors: it grants no capability
# the same-user attacker does not already hold.
#
# Environment: AAID_SKILL_ROOT is honored ONLY when AAID_FAKE_ROOT is also
# set (test-harness marker; adversarial finding: an env-controlled boundary
# must not be reachable in production) — otherwise the root is derived
# strictly from the script's own location.
#
# Untrusted remote data discipline: everything `gh` returns is
# DATA. The embedded python parser below never eval/source/executes remote
# content, only passes decoded bytes through base64/JSON/sha plumbing.
# Remote tip metadata is a single 16–64 alphanumeric-character token or the
# run is rejected;
# manifest paths are canonicalized ONCE at load and only the canonical
# form is ever read or written; reserved local policy paths (README.md,
# MANIFEST.json at upstream root) are rejected.
set -u

# Resolve skill root: script's ../.. — AAID_SKILL_ROOT is honored ONLY in
# the test harness (AAID_FAKE_ROOT must also be set; see threat model).
_here="$(cd "$(dirname "$0")" && pwd)"
if [ -n "${AAID_SKILL_ROOT:-}" ] && [ -n "${AAID_FAKE_ROOT:-}" ]; then
    SKILL_ROOT="$AAID_SKILL_ROOT"
else
    SKILL_ROOT="$_here/.."
fi
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

if ! command -v python3 >/dev/null 2>&1; then
    # Preflight here too: the embedded program below needs python3, and a
    # missing interpreter would otherwise surface as a raw exit 127 outside
    # the sanitized ERROR channel (gate 6.2 nit 5).
    echo "ERROR: python3 not found on PATH (the embedded checker program requires python3)" >&2
    exit 1
fi

if ! python3 -c 'import sys; raise SystemExit(0 if sys.version_info >= (3, 11) else 1)' >/dev/null 2>&1; then
    # Supported-interpreter policy (binding): CPython >= 3.11 (3.10 is
    # EOL). Fail sanitized BEFORE the update runs — a version mismatch
    # must never surface as a raw traceback and a wedged update.lock
    # mid-cutover. No fallback path.
    echo "ERROR: python3 >= 3.11 is required (supported interpreter policy: CPython >= 3.11; 3.10 is EOL); stock macOS /usr/bin/python3 (3.9) is not supported" >&2
    exit 1
fi

# All logic in one embedded python program (clean top-level indentation,
# quoted heredoc delimiter so no shell expansion reaches remote-derived or
# fixture-derived text). gh is spawned via subprocess; JSON is parsed, never
# interpolated into shell or python code.
python3 - "$SKILL_ROOT" "$UPDATE_MODE" <<'PYEOF'
import base64
import errno
import hashlib
import json
import math
import os
import re
import select
import stat
import subprocess
import sys
import time
from pathlib import Path

NOFOLLOW = getattr(os, "O_NOFOLLOW", 0)
NONBLOCK = getattr(os, "O_NONBLOCK", 0)

root_arg = sys.argv[1]
update_mode = sys.argv[2] == "1"

# Relative names/tuples (containment anchors their dirfds, never strings):
cache_name = ".cache"
lock_name = "update.lock"

# Display-only strings derived from the pinned root (error messages);
# containment and IO NEVER traverse these.
root_str = None

# Module-level run ownership state (fd identity anchors):
root_fd = None           # pinned skill-root dirfd, opened once
manifest_rel = ("assets", "upstream", "MANIFEST.json")
source_rel = ("references", "SOURCE.md")
cache_fd = None          # .cache dirfd once created
staging_name = None      # staging dir NAME (relative to .cache dirfd)
staging_fd = None        # staging dirfd once created
lock_fd = None           # this run's own update.lock fd, once held
retain_staging = False   # True once staging holds a COMPLETE fetched snapshot

# Transport deadline (gate 6.3 low): checker-enforced; override for slow or
# air-gapped hosts via AAID_CHECK_TIMEOUT (seconds). Parsed/validated in
# main() (fail() must exist first); a non-finite or non-positive value is
# an ERROR, values above TRANSPORT_MAX_S are clamped (a huge value must not
# silently disable the deadline).
TRANSPORT_DEFAULT_S = 30.0
TRANSPORT_MAX_S = 600.0
GH_TIMEOUT = TRANSPORT_DEFAULT_S
# RAW stdout cap + decoded payload cap + stderr cap: raw stdout is read
# incrementally and the run is killed once it exceeds MAX_RAW_BYTES —
# whitespace/base64 padding inflation cannot escape the bound because the
# cap applies BEFORE any JSON parse or decode. Separately a successfully
# decoded payload above MAX_PAYLOAD_BYTES is rejected before any use.
MAX_PAYLOAD_BYTES = 2 * 1024 * 1024
MAX_RAW_BYTES = 4 * 1024 * 1024
MAX_ERR_BYTES = 1 * 1024 * 1024

BEGIN = re.compile(r"<!-- BEGIN CHECK-STATUS.*?-->\n?", re.S)
END = re.compile(r"<!-- END CHECK-STATUS -->")


def sanitize(reason):
    """Failure reasons are output — sanitize to ONE printable line.
    Control characters (incl. newlines, ESC/ANSI) are removed, whitespace
    runs collapsed, and the line capped, so server-influenced stderr from gh
    can never spoof a verdict line or inject escapes into the verdict channel."""
    text = "".join(ch if ch.isprintable() else " " for ch in reason)
    return " ".join(text.split())[:300]


def release_lock():
    """Release + unlink this run's own lock GUARDED by inode identity: the
    held fd's (dev, ino) must match a fresh nofollow stat via the held
    .cache dirfd — a pivoted .cache must never cause the unlink of a
    foreign/external lock file (adversarial medium)."""
    global lock_fd
    if lock_fd is None:
        return
    try:
        try:
            fst = os.fstat(lock_fd)
            pst = os.stat(lock_name, dir_fd=cache_fd, follow_symlinks=False)
            if (fst.st_dev, fst.st_ino) == (pst.st_dev, pst.st_ino):
                os.unlink(lock_name, dir_fd=cache_fd)
        except OSError:
            pass
    finally:
        try:
            os.close(lock_fd)
        except OSError:
            pass
        lock_fd = None


class _RefuseCleanup(Exception):
    """A manipulated entry inside the staging dir (e.g. a symlinked
    SUB-directory) — cleanup refuses rather than following/deleting
    anything it cannot prove is checker-owned."""
    pass


def identity_matches(a, b):
    """(st_dev, st_ino) equality — two stat results name the SAME file."""
    return (a.st_dev, a.st_ino) == (b.st_dev, b.st_ino)


def delete_contents_fd(dir_fd, what):
    """Delete the CONTENTS of the directory identified by dir_fd — an
    already-validated fd. The top NAME is never resolved again (fd-anchored
    deletion cannot be redirected by a top-name swap). Each child is
    IDENTITY-VERIFIED between enumeration and action: (dev, ino) from the
    scandir DirEntry stat (follow_symlinks=False) must equal the dev/ino of
    the descriptor/stat taken at action time — directory children: the
    opened dirfd's fstat; file children: a fresh nofollow stat of the name.
    A mismatch is a PRE-OPEN substitution (the enumerated inode was
    replaced under the same name — in-model) → _RefuseCleanup →
    remove_staging skips the cleanup with ONE sanitized WARNING and spares
    the foreign tree.

    Documented windows (accepted/design behavior, stated explicitly):
    (a) POST-OPEN relocation of an opened descriptor between the final
        identity check and the anchored operation is THE approved residual
        (not closable in userspace);
    (b) CONTENT planted inside the checker-created staging directory
        BEFORE enumeration is deleted with the staging tree — the staging
        dir is checker-owned space with an unpredictable name;
    (c) the final top-name rmdir can at most remove an EMPTY replacement
        directory — rmdir never recurses; a populated substitute makes the
        rmdir fail (ENOOTEMPTY) → refuse + warn.

    Exception style (docs match code): a MISSING entry (ENOENT between
    enumeration and action) is SKIPPED and traversal continues; any other
    unexpected OSError rides up to remove_staging's OSError arm — the
    cleanup is skipped and a warning is emitted (same terminate-and-warn
    outcome). Because a termination can arrive after earlier successful
    deletions, the remaining tree may be PARTIALLY deleted (stated
    honestly)."""
    with os.scandir(dir_fd) as it:
        for entry in it:
            name = entry.name
            if entry.is_symlink():
                # A link the checker cannot prove is checker-owned (a planted
                # pivot could point anywhere): REFUSE the whole cleanup —
                # never follow, never judge the target (the name itself is
                # left in place; remove_staging warns + spares).
                raise _RefuseCleanup(f"symlinked entry in staging: {name}")
            try:
                enumerated = entry.stat(follow_symlinks=False)
            except FileNotFoundError:
                continue  # raced away between iterations: skipped
            if entry.is_dir(follow_symlinks=False):
                try:
                    sub = open_dir_at(dir_fd, name, what)
                except Missing:
                    continue  # missing between enumeration and open: skipped
                opened = os.fstat(sub)
                if not identity_matches(enumerated, opened):
                    try:
                        os.close(sub)
                    except OSError:
                        pass
                    raise _RefuseCleanup(
                        f"directory child substituted between enumeration "
                        f"and open: {name} (dev/ino mismatch)"
                    )
                # Recurse on the identity-verified fd itself.
                try:
                    delete_contents_fd(sub, what)
                finally:
                    try:
                        os.close(sub)
                    except OSError:
                        pass
                try:
                    os.rmdir(name, dir_fd=dir_fd)
                except FileNotFoundError:
                    continue  # raced: skipped
            else:
                try:
                    named = os.stat(name, dir_fd=dir_fd, follow_symlinks=False)
                except FileNotFoundError:
                    continue  # missing between enumeration and stat: skipped
                if not identity_matches(enumerated, named):
                    raise _RefuseCleanup(
                        f"file child substituted: {name} (dev/ino mismatch)"
                    )
                try:
                    os.unlink(name, dir_fd=dir_fd)
                except FileNotFoundError:
                    continue  # raced: skipped


def remove_staging():
    """Remove THIS run's staging dir entirely dirfd-relative:
    delete_contents_fd on the HELD staging fd (the top name is never
    resolved for the contents), then — only after a FINAL identity re-stat
    of the staging name via the held .cache dirfd (inode == held staging
    fd) — os.rmdir the top name dir_fd-relative. Each staging child is
    identity-verified between enumeration and action (dev/ino) — a
    pre-open substitution at ANY point (identity snapshot, child
    substitution, final re-stat) skips the cleanup with ONE sanitized
    WARNING and spares the foreign tree; the populated-substitute case
    also fails the top rmdir (ENOTEMPTY → refuse + warn). Because a
    refusal can land after earlier successful deletions, the tree may be
    PARTIALLY deleted at that point (stated honestly)."""
    global staging_name, staging_fd
    if staging_name is None:
        return
    cleanup_done = False
    if cache_fd is not None and staging_fd is not None:
        try:
            held = os.fstat(staging_fd)
            nam = os.stat(staging_name, dir_fd=cache_fd, follow_symlinks=False)
            identity_ok = (nam.st_dev, nam.st_ino) == (held.st_dev, held.st_ino)
        except FileNotFoundError:
            identity_ok, held = True, None  # already gone
        except OSError:
            identity_ok, held = False, None  # warn-skip below
        if identity_ok:
            try:
                delete_contents_fd(staging_fd, "staging cleanup")
                if held is not None:
                    final = os.stat(staging_name, dir_fd=cache_fd, follow_symlinks=False)
                    if (final.st_dev, final.st_ino) != (held.st_dev, held.st_ino):
                        raise _RefuseCleanup("final identity re-stat mismatch")
                os.rmdir(staging_name, dir_fd=cache_fd)
                cleanup_done = True
            except _RefuseCleanup as refusal:
                print(
                    "WARNING: " + sanitize(
                        "staging cleanup skipped (" + str(refusal) + " —"
                        " manipulated layout); staging remains under"
                        " .cache/" + staging_name
                    ),
                    file=sys.stderr,
                )
            except OSError as exc:
                print(
                    "WARNING: " + sanitize(
                        "staging cleanup skipped (mid-run deletion failure: "
                        + str(exc) + "); staging may remain under"
                        " .cache/" + staging_name
                    ),
                    file=sys.stderr,
                )
        else:
            print(
                "WARNING: staging cleanup skipped (inode mismatch: the "
                f"staging name was substituted mid-run); staging remains "
                f"under .cache/{staging_name}",
                file=sys.stderr,
            )
    if staging_fd is not None:
        try:
            os.close(staging_fd)
        except OSError:
            pass
    staging_name = None
    staging_fd = None


def fail(reason):
    # Cleanup is strictly this run's own state: only the staging dir THIS
    # run created (dirfd-relative, never through a swapped pathname) and
    # only the lock fd THIS run holds (inode-verified unlink). A failing
    # check-only run owns neither. NOTE: fetch-phase failures clean the
    # staging copy; cutover failures RETAIN it (retain_staging).
    if not retain_staging:
        remove_staging()
    release_lock()
    message = str(reason)
    if retain_staging and staging_name is not None:
        # The staging copy is the recovery snapshot; point at it, sanitized
        # together with the reason.
        message += " staging retained at .cache/" + staging_name
    # Unified ERROR channel: stderr (shell pre-checks use stderr too);
    # verdict lines (UNCHANGED/CHANGED/UPDATED) stay on stdout.
    print(f"ERROR: {sanitize(message)}", file=sys.stderr)
    sys.exit(1)


def reap(proc, timeout=5.0):
    try:
        proc.wait(timeout=timeout)
    except (subprocess.TimeoutExpired, OSError):
        pass


def verify_boundary(what):
    """Identity-check the pinned root before acting on it: fstat the held
    dirfd vs a fresh stat of the pinned PATHNAME (st_dev/st_ino). A root
    rename + symlink swap to a matching external tree is a mismatch →
    ERROR. Containment itself never re-resolves strings; this check is
    identity-only, and the residual race between it and the actual write is
    documented as such (no dirfd-relative write can anchor the root's OWN
    parent)."""
    if root_fd is None:
        return
    try:
        fresh = os.stat(root_str)
    except OSError as exc:
        fail(f"{what}: the pinned skill root is no longer reachable: {exc}")
    held = os.fstat(root_fd)
    if (fresh.st_dev, fresh.st_ino) != (held.st_dev, held.st_ino):
        fail(
            f"{what}: the pinned skill root was renamed or swapped mid-run "
            "(path/identity mismatch) — manipulated local layout"
        )


def verify_cache_identity(what):
    """Identity-check the pinned .cache: fstat the held dirfd vs a fresh
    NOFOLLOW stat of the .cache NAME via the held root dirfd. A persisted
    rename + symlink swap of .cache is a mismatch → ERROR (no foreign
    dir's contents are ever written or unlinked through the swap)."""
    if cache_fd is None:
        return
    try:
        nam = os.stat(cache_name, dir_fd=root_fd, follow_symlinks=False)
    except OSError as exc:
        fail(f"{what}: the pinned .cache is no longer reachable: {exc}")
    held = os.fstat(cache_fd)
    if (nam.st_dev, nam.st_ino) != (held.st_dev, held.st_ino):
        fail(
            f"{what}: the pinned .cache was renamed or swapped mid-run "
            "(path/identity mismatch) — manipulated local layout"
        )


class Missing(Exception):
    """A required path component does not exist (yet)."""


def open_dir_at(base_fd, name, what):
    """Open ONE component as a DIRECTORY, O_NOFOLLOW, dir_fd-relative to
    base_fd. Missing → Missing; symlink/non-dir (ELOOP/ENOTDIR) → ERROR
    naming the manipulation. The canonical-path policy guarantees no
    component ever legitimately needs to traverse a symlink."""
    try:
        return os.open(name, os.O_RDONLY | os.O_DIRECTORY | NOFOLLOW, dir_fd=base_fd)
    except FileNotFoundError:
        raise Missing(name)
    except OSError as exc:
        if exc.errno in (errno.ELOOP, errno.ENOTDIR):
            fail(
                f"{what} is a symlink or not a directory (manipulated local "
                f"layout): {name} — remove the link and restore the real directory"
            )
        fail(f"{what} cannot be opened as a directory ({name}): {exc}")


def walk_dirs(rel_parts, base_fd, what, create=False):
    """Walk the directory chain rel_parts below base_fd, EVERY component
    opened O_NOFOLLOW|O_DIRECTORY dir_fd-relative (no string resolution of
    the base anywhere). With create=True, missing components are mkdir'd
    dir_fd-relative and REVALIDATED immediately after creation — a symlink
    planted in the creation gap is an ERROR, not a traversal. Closes every
    intermediate fd it opened; the base_fd is borrowed (never closed). The
    FINAL fd is owned by the caller (close it when done) — for an EMPTY
    rel_parts chain the base fd itself would be borrowed, so a dup() is
    returned instead: walk_dirs NEVER returns a borrowed fd, and callers
    may close the result unconditionally."""
    if not rel_parts:
        return os.dup(base_fd)
    fd = base_fd
    for i, part in enumerate(rel_parts):
        if part in ("", ".", "..") or os.sep in part:
            fail(
                f"{what} would escape its boundary via a non-canonical "
                f"component: {part!r}"
            )
        try:
            nxt = open_dir_at(fd, part, what)
        except Missing:
            if not create:
                raise
            try:
                os.mkdir(part, dir_fd=fd)
            except OSError as exc:
                fail(f"{what}: cannot create directory {part}: {exc}")
            # Revalidate the created level: a symlink planted in the
            # mkdir→open gap must ERROR, never be traversed.
            nxt = open_dir_at(fd, part, what)
        if i > 0:
            os.close(fd)
        fd = nxt
    return fd


def read_regular_at_fd(dir_fd, name, what, require_regular=True, max_bytes=None):
    """Open a FILE O_NOFOLLOW|O_NONBLOCK relative to dir_fd, fstat the SAME
    fd, require S_ISREG (a symlinked record is tampered provenance; a FIFO/
    device is refused fast — no unbounded read through a FIFO), then read
    from the SAME fd: the fstat-on-open closes the lstat→read swap window.
    With max_bytes set (local snapshot reads: manifest-declared bytes + a
    64KB slack), the read is chunked and the instant the bound is exceeded
    the run fails sanitized — an entry redirected to /dev/zero (or any
    oversized/redirected target) cannot trigger an unbounded read.
    require_regular=False (LOCAL SNAPSHOT reads only) follows the final
    component's symlink — the CONTENT is then hash-checked against the
    manifest, so redirection can never smuggle bytes into a verdict.
    Returns bytes; raises Missing when absent."""
    try:
        # O_NOFOLLOW (provenance/manifest reads only): a symlinked record is
        # tampered provenance. Local-snapshot reads (require_regular=False)
        # follow the final component — the CONTENT is then hash-checked
        # against the manifest, so redirection cannot smuggle bytes.
        file_flags = os.O_RDONLY | NONBLOCK
        if require_regular:
            file_flags |= NOFOLLOW
        fd = os.open(name, file_flags, dir_fd=dir_fd)
    except FileNotFoundError:
        raise Missing(name)
    except OSError as exc:
        if exc.errno in (errno.ELOOP, errno.ENOTDIR):
            fail(
                f"tampered provenance: {what} is a symlink (a provenance "
                f"record must be a regular file inside its boundary): {name}"
            )
        fail(f"{what} cannot be opened ({name}): {exc}")
    try:
        st = os.fstat(fd)
    except OSError as exc:
        try:
            os.close(fd)
        except OSError:
            pass
        fail(f"{what} cannot be fstat'ed ({name}): {exc}")
    if require_regular and not stat.S_ISREG(st.st_mode):
        try:
            os.close(fd)
        except OSError:
            pass
        fail(
            f"{what} is not a regular file (symlink/FIFO/device — refusing "
            f"an unbounded read): {name}"
        )
    try:
        if max_bytes is None:
            with os.fdopen(fd, "rb") as fh:
                return fh.read()
        # Size-capped chunked read (F3): /dev/zero-style redirection cannot
        # drive an unbounded read.
        chunks = []
        total = 0
        with os.fdopen(fd, "rb") as fh:
            while True:
                chunk = fh.read(65536)
                if not chunk:
                    break
                total += len(chunk)
                if total > max_bytes:
                    fail(
                        f"{what} exceeds its declared size cap ({max_bytes} "
                        f"bytes) — refusing an unbounded read: {name}"
                    )
                chunks.append(chunk)
        return b"".join(chunks)
    except OSError as exc:
        fail(f"{what} cannot be read ({name}): {exc}")


def split_path(rel):
    """('a/b/c.txt') -> (('a','b'), 'c.txt') — canonical manifest-derived
    path only."""
    parts = tuple(Path(rel).parts)
    return parts[:-1], parts[-1]


def read_provenance():
    """Read references/SOURCE.md through the pinned dirfd walk. Returns
    None when the references directory or the SOURCE.md record does not
    exist (the caller decides what absent provenance means); fails on a
    broken/blocked references path, a SYMLINKED record, or a non-regular
    record (FIFO/device)."""
    try:
        ref_fd = walk_dirs(source_rel[:1], root_fd, "provenance path")
    except Missing:
        return None
    try:
        try:
            return read_regular_at_fd(ref_fd, source_rel[1], "provenance record").decode("utf-8")
        except Missing:
            return None
    finally:
        try:
            os.close(ref_fd)
        except OSError:
            pass


def load_manifest():
    """Manifest bytes via the pinned dirfd walk (O_NOFOLLOW + fstat S_ISREG
    on the SAME fd), parsed as JSON; remote-independent local policy."""
    up_fd = walk_dirs(manifest_rel[:2], root_fd, "manifest path")
    try:
        try:
            raw = read_regular_at_fd(up_fd, manifest_rel[2], "manifest file")
        except Missing:
            fail("manifest not found under assets/upstream/: " + manifest_rel[2])
    finally:
        try:
            os.close(up_fd)
        except OSError:
            pass
    try:
        return json.loads(raw)
    except ValueError:
        fail("invalid manifest JSON in assets/upstream/MANIFEST.json")

def pin_boundary():
    """Boundary pinning (iteration-3 Fix 2): the skill root is pinned as a
    DIRECTORY FD (os.open O_NOFOLLOW|O_DIRECTORY from the script's own
    location) — an fd is an identity anchor, not a pathname. Pre-open
    parent/root pivots do not redirect fd-anchored writes (writes land in
    the pinned inode tree — verify_boundary detects a persistent root
    pathname swap before EVERY write); pathname DISPLAY and re-invocation
    are environment-owned (root_str is a display-only canonical string,
    error messages only). The ONLY accepted residual (the header's approved
    wording): post-verification same-user rename/relocation of already-
    opened descriptors between the final identity check and the anchored
    operation — not closable in userspace."""
    global root_fd, root_str, cache_fd, staging_name, staging_fd
    given_abs = os.path.abspath(root_arg)
    try:
        st = os.lstat(given_abs)
    except FileNotFoundError:
        fail(f"skill root boundary does not exist: {given_abs}")
    except OSError as exc:
        fail(f"cannot lstat skill root boundary {given_abs}: {exc}")
    if stat.S_ISLNK(st.st_mode):
        fail(
            "skill root boundary itself is a symlink: " + given_abs
            + " — manipulated local layout"
        )
    try:
        root_fd = os.open(given_abs, os.O_RDONLY | os.O_DIRECTORY | NOFOLLOW)
    except OSError as exc:
        if exc.errno in (errno.ELOOP, errno.ENOTDIR):
            fail(f"skill root boundary is a symlink or not a directory: {given_abs}")
        fail(f"cannot open skill root boundary ({given_abs}): {exc}")
    if not stat.S_ISDIR(os.fstat(root_fd).st_mode):
        fail(f"skill root boundary is not a directory: {given_abs}")
    # Display-only canonical string.
    root_str = os.path.realpath(given_abs)



def guarded_write(rel_parts, name, data, base_fd, what):
    """THE write discipline for every destination (live or staging):
    1. verify the pinned root's and .cache's path/identity before the walk
       (persistent rename/swap → ERROR);
    2. validate every ancestor dirfd-relative, O_NOFOLLOW, creating missing
       levels (and revalidating after creation);
    3. write via a UNIQUE UNPREDICTABLE temp file created
       O_CREAT|O_EXCL|O_NOFOLLOW inside the DESTINATION dirfd, written
       through the exclusive fd;
    4. verify the temp's inode identity (dev/ino) against a fresh nofollow
       stat via the destination dirfd — a temp substituted mid-write is a
       manipulated layout → ERROR;
    5. os.replace onto the destination name anchored on
       src_dir_fd/dst_dir_fd (entry replacement: a planted symlink at the
       dest ends replaced, never followed through — its target keeps its
       old bytes).
    No in-place truncation; fsync is intentionally skipped (no power-loss
    durability claim)."""
    walk_fd = None
    if root_fd is not None:
        verify_boundary(what)
    if cache_fd is not None:
        verify_cache_identity(what)
    try:
        walk_fd = walk_dirs(rel_parts, base_fd, what, create=True)
        # Destination writability parity (pre-iteration-3 behavior): a
        # read-only existing entry must fail the run, not be silently
        # replaced (os.replace ignores the file's own write bit; this
        # check restores the explicit failure).
        try:
            entry_st = os.stat(name, dir_fd=walk_fd)
        except FileNotFoundError:
            entry_st = None
        if entry_st is not None and not (entry_st.st_mode & stat.S_IWUSR):
            fail(f"{what}: destination entry is read-only: {name}")
        f_flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | NOFOLLOW
        for _ in range(8):
            tmp_name = f".{name}.tmp-{os.getpid()}-{os.urandom(8).hex()}"
            try:
                tmp_fd = os.open(tmp_name, f_flags, 0o600, dir_fd=walk_fd)
            except FileExistsError:
                continue
            break
        else:
            raise OSError(f"could not create a unique temp file next to {name}")
        try:
            wrote_ino = None
            with os.fdopen(tmp_fd, "wb") as fh:
                fh.write(data)
                wrote_ino = (os.fstat(fh.fileno()).st_dev,
                             os.fstat(fh.fileno()).st_ino)
            # Substitution guard (accepted-residual boundary: closing the
            # window to inode identity at replace time).
            anchor = os.stat(tmp_name, dir_fd=walk_fd, follow_symlinks=False)
            if (anchor.st_dev, anchor.st_ino) != wrote_ino:
                fail(f"{what}: staging temp was substituted mid-write "
                     "(inode mismatch) — manipulated local layout")
            os.replace(tmp_name, name, src_dir_fd=walk_fd, dst_dir_fd=walk_fd)
        except OSError as exc:
            fail(f"{what}: write to {name} failed: {exc}")
        finally:
            try:
                os.unlink(tmp_name, dir_fd=walk_fd)
            except OSError:
                pass
    finally:
        if walk_fd is not None and walk_fd is not base_fd:
            try:
                os.close(walk_fd)
            except OSError:
                pass


def transport_deadline():
    """Validate AAID_CHECK_TIMEOUT: finite, positive; clamp to
    TRANSPORT_MAX_S — an absent/huge/non-finite value must never silently
    disable the checker-enforced deadline."""
    raw = os.environ.get("AAID_CHECK_TIMEOUT", "")
    if raw.strip() == "":
        return TRANSPORT_DEFAULT_S
    try:
        val = float(raw)
    except ValueError:
        fail(f"invalid AAID_CHECK_TIMEOUT (not a number): {raw!r}")
    if not math.isfinite(val) or val <= 0:
        fail(f"AAID_CHECK_TIMEOUT must be a finite positive number, got {raw!r}")
    return min(val, TRANSPORT_MAX_S)


def fresh(date, tip):
    """Check-status lines emitted by an authorized refresh:
    machine-updatable block contents, integrated pin preserved separately."""
    # NOTE: date is None-safe; tip is the validated fetched commit, never the pin.
    return (f"- Last successful check: {date}\n"
            f"- Fetched commit: `{tip}`\n")


def extract_source_pin(src_text, allow_blockless):
    """Validate the check-status block and return its Integrated pin token
    (opaque; the checker resolves it via gh). A marker trace without a
    WELL-FORMED block is a runtime-produced corruption state and must fail
    loudly in EVERY mode — silently falling back would report a false
    UNCHANGED after an interrupted cutover. When the file carries no block
    and no marker substring at all: legacy semantics (pre-block snapshots) —
    returns None if allow_blockless, else ERROR."""
    trace = any(
        "begin check-status" in line.casefold() for line in src_text.splitlines()
    )
    b = BEGIN.search(src_text)
    if trace and not b:
        fail("malformed check-status block (truncated BEGIN marker) in references/SOURCE.md")
    if not b:
        if allow_blockless:
            return None
        fail(
            "missing provenance: references/SOURCE.md has no check-status"
            " block — restore the check-status block or re-record the"
            " integrated pin after human review; the manifest pin alone"
            " can never establish an integrated baseline"
        )
    e = END.search(src_text, b.end())
    if not e:
        fail("malformed check-status block (no END marker) in references/SOURCE.md")
    block = src_text[b.end():e.start()]
    line = re.search(r"- Integrated pin: `([^`\n]+)`", block)
    if not line:
        fail("malformed check-status block (no Integrated pin line) in references/SOURCE.md")
    # The pin token is opaque here (checker resolves it via gh); anything
    # backquoted on the first Integrated pin line counts.
    return line.group(1)


def main():
    global cache_fd, staging_name, staging_fd, lock_fd, retain_staging
    global GH_TIMEOUT

    pin_boundary()
    GH_TIMEOUT = transport_deadline()

    try:
        if update_mode:
            # Exclusive update lock (reworked: dirfd-relative). Ancestors are
            # validated against the pinned root by the dirfd walk; no
            # pathname traversal can slip a pivot in between. mkdir + the
            # O_EXCL lock open are both dirfd-relative and revalidated.
            cache_fd = walk_dirs((cache_name,), root_fd, ".cache boundary", create=True)
            try:
                lock_fd = os.open(
                    lock_name, os.O_CREAT | os.O_EXCL | os.O_WRONLY | NOFOLLOW,
                    dir_fd=cache_fd,
                )
            except FileExistsError:
                # Distinguish a TAMPERED lock (a symlink at update.lock —
                # O_NOFOLLOW|O_EXCL never opened it) from an ordinary live/
                # stale lock. Never auto-remove either: the holder may be
                # another live updater; the tamper case is a manipulated
                # layout.
                try:
                    lst = os.stat(lock_name, dir_fd=cache_fd, follow_symlinks=False)
                    if stat.S_ISLNK(lst.st_mode):
                        fail(
                            "lock path is a symlink — tampered lock"
                            " (remove .cache/update.lock manually only after"
                            " confirming no update is actually running)"
                        )
                    age = max(0, int(time.time() - lst.st_mtime))
                except OSError:
                    age = -1
                held = f"held for {age}s" if age >= 0 else "age unknown"
                fail(
                    "another update in progress or stale lock "
                    f"({held}; remove .cache/update.lock manually only if no "
                    "update is actually running)"
                )
            except OSError as exc:
                fail(f"cannot acquire update lock: {exc}")

        manifest = load_manifest()

        # Path canonicalization + containment (unsafe-path policy). Lexical
        # only — no re-resolution (the dirfd walk below enforces the real
        # containment). Every entry's path is validated and CANONICALIZED
        # before any read or write ever uses it; ONLY the canonical
        # in-upstream relative form is stored back and used by every later
        # operation. Reserved local policy paths are rejected outright.
        #(c) Reserved local policy protection.
        #reserved_paths names the policy files AT THE UPSTREAM ROOT. Root-level
        #collisions are rejected CASE-INSENSITIVELY (a manifest entry like
        #`readme.md` addresses the local README.md on case-insensitive
        #filesystems such as macOS default). Only ROOT-LEVEL casefolded
        #collisions are rejected: a nested `docs/readme.md` is an upstream
        #asset and stays allowed — the protection is about overwriting the
        #local policy file at the snapshot root, not about the name anywhere.
        reserved_roots = {"readme.md", "manifest.json"}
        upstream_lex = os.path.normpath(
            os.path.join(str(root_str or ""), "assets", "upstream")
        )
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
            # Lexical containment of the parent chain: a non-canonical
            # spelling that escapes assets/upstream/ is rejected; one that
            # resolves INSIDE upstream stages/cuts over at its canonical
            # location (the dirfd walk enforces plain directories).
            parent_lex = os.path.normpath(os.path.join(upstream_lex, str(p.parent)))
            if parent_lex != upstream_lex and \
                    not parent_lex.startswith(upstream_lex + os.sep):
                fail("unsafe manifest path (escapes assets/upstream/): " + raw)
            canonical = os.path.normpath(os.path.join(
                os.path.relpath(parent_lex, upstream_lex), p.name
            ))
            if canonical == ".":
                fail("unsafe manifest path (resolves to assets/upstream root): " + raw)
            if os.sep not in canonical and canonical.casefold() in reserved_roots:
                fail("unsafe manifest path (reserved local policy file): " + raw)
            entry["path"] = canonical
            canonical_entries.append(entry)
        manifest["files"] = canonical_entries

        repo = manifest["repository"]
        if not isinstance(repo, str) or not repo.strip():
            fail("manifest repository missing or not a string")
        repo = repo.strip()
        # Accept a full https URL as well as bare owner/repo; normalize to
        # the bare owner/repo that `gh api` expects. Pure string plumbing on
        # the manifest's own data — no remote content involved.
        if repo.startswith(("https://", "http://")):
            tail = repo.split("://", 1)[1]
            _, _, tail = tail.partition("/")  # drop host
            repo = tail
        repo = repo.strip("/")
        if not re.match(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$", repo) or \
                repo.startswith(("/", ".")) or "/.." in repo:
            fail("unsafe manifest repository reference: " + str(repo))
        branch = manifest["default_branch"]

        # Integrated-baseline resolution (iteration-4 binding, F4: absence of
        # provenance never authenticates). Priority: (1) the human-integrated
        # record — the SOURCE.md check-status pin — when SOURCE exists;
        # (2) the manifest integrated_commit when it is recorded; otherwise
        # (3) ERROR fail-closed: a legacy fetched-only manifest without the
        # field cannot be authenticated, regardless of present/absent residue
        # directories — nothing is default-merged from resolved_commit any
        # more (the pre-iteration-4 first-run resolution manufactured an
        # integrated baseline out of absent provenance). Genuine first-run
        # now REQUIRES the new-schema manifest (vendoring writes
        # integrated_commit; the shipped assets/upstream/MANIFEST.json has
        # it).
        src_text = read_provenance()
        source_pin = None
        if src_text is not None:
            source_pin = extract_source_pin(src_text, allow_blockless=False)
        if source_pin is not None:
            integrated_raw = source_pin
        else:
            integrated_raw = manifest.get("integrated_commit")
            if integrated_raw is None:
                fail(
                    "provenance record missing: references/SOURCE.md not found"
                    " — re-record the integrated pin after human review;"
                    " absence of provenance never authenticates, so no"
                    " integrated baseline can be manufactured here"
                )
        if not isinstance(integrated_raw, str) or \
                not re.fullmatch(r"[0-9A-Za-z]{16,64}", integrated_raw):
            fail("manifest integrated_commit is not a sane single commit token")
        manifest_integrated = integrated_raw

        def gh_json(endpoint, fields=None):
            """Run `gh api` and parse stdout as JSON. Remote JSON is data
            only. Transport bounds END-TO-END (iter-3): wall-clock deadline
            while streaming BOTH stdout and stderr (both fds in the select
            set — stderr can never fill its pipe mid-run), RAW stdout killed
            above MAX_RAW_BYTES before any parse/decode, stderr killed above
            MAX_ERR_BYTES, and a DEADLINE-BOUNDED post-EOF wait (a gh that
            closes stdout then blocks is killed and reported, never waited
            on forever). Timeout/cap failures release this run's own lock
            via fail()."""
            cmd = ["gh", "api", "--method", "GET", endpoint]
            for kv in fields or []:
                cmd += ["-f", kv]
            try:
                proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except OSError as exc:
                fail(f"cannot run gh for {endpoint}: {exc}")
            deadline = time.monotonic() + GH_TIMEOUT
            chunks = []
            err_bits = []
            size = 0
            esize = 0
            out_eof = False
            err_eof = False
            out_overflow = False
            err_overflow = False
            out_fd = proc.stdout.fileno()
            err_fd = proc.stderr.fileno()
            while True:
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    proc.kill()
                    reap(proc)
                    fail(
                        f"gh api timed out after {GH_TIMEOUT:g}s for {endpoint}"
                        " (AAID_CHECK_TIMEOUT)"
                    )
                watch = [fd for fd in (out_fd, err_fd)]
                ready, _, _ = select.select(watch, [], [], min(remaining, 0.5))
                if out_fd in ready:
                    chunk = os.read(out_fd, 65536)
                    if chunk:
                        size += len(chunk)
                        if size > MAX_RAW_BYTES:
                            out_overflow = True
                            break
                        chunks.append(chunk)
                    else:
                        out_eof = True
                elif err_fd in ready:
                    piece = os.read(err_fd, 65536)
                    if piece:
                        esize += len(piece)
                        if esize > MAX_ERR_BYTES:
                            err_overflow = True
                            break
                        err_bits.append(piece)
                    else:
                        err_eof = True
                if out_eof:
                    # stdout EOF: the deadline-bounded post-EOF wait owns the
                    # rest (Fix 3) — a gh that closes stdout then blocks is
                    # killed and reported, never waited on forever.
                    break
            if out_overflow:
                proc.kill()
                reap(proc)
                fail(
                    f"gh api raw response exceeded {MAX_RAW_BYTES} bytes for {endpoint}"
                    " (killed before buffering)"
                )
            if err_overflow:
                proc.kill()
                reap(proc)
                fail(
                    f"gh api stderr exceeded {MAX_ERR_BYTES} bytes for {endpoint}"
                    " (killed before buffering)"
                )
            if out_eof:
                # Deadline-bounded post-EOF wait (Fix 3): gh closing stdout
                # then blocking on a full stderr pipe is killed and
                # reported, never waited on forever.
                try:
                    proc.wait(timeout=max(0.1, deadline - time.monotonic()))
                except subprocess.TimeoutExpired:
                    proc.kill()
                    reap(proc)
                    fail(
                        f"gh api did not exit after closing stdout within the "
                        f"deadline for {endpoint} (AAID_CHECK_TIMEOUT="
                        f"{GH_TIMEOUT:g}s)"
                    )
            err_text = b"".join(err_bits).decode("utf-8", "replace").strip()
            proc.stdout.close()
            proc.stderr.close()
            if proc.returncode != 0:
                fail(f"gh api failed for {endpoint}: {err_text}")
            try:
                obj = json.loads(b"".join(chunks))
            except ValueError:
                fail(f"gh api returned invalid JSON for {endpoint}")
            if not isinstance(obj, dict):
                # Domain-specific shape guard: non-dict documents
                # (list/string/number) would otherwise surface as
                # AttributeError tracebacks.
                fail(f"invalid JSON shape for {endpoint}: expected object")
            return obj

        def content_bytes(path, sha):
            """Fetch one file's content bytes at a commit (base64), validated
            against the response's own size/blob-sha metadata. Remote bytes
            stay data only."""
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
            if len(data) > MAX_PAYLOAD_BYTES:
                # Fires AFTER the raw stream fully arrived (bounded by the
                # raw cap at read time) but before the bytes are used for
                # anything.
                fail(
                    f"decoded content payload exceeds {MAX_PAYLOAD_BYTES} bytes for {path}"
                    " (rejected before any comparison or write)"
                )
            blob_sha = hashlib.sha1(b"blob %d\x00" % len(data) + data).hexdigest()
            if resp["sha"] != blob_sha:
                fail(f"blob sha mismatch from remote metadata for {path}")
            return data

        tip_resp = gh_json(f"repos/{repo}/commits/{branch}")
        if not tip_resp.get("sha"):
            fail(f"tip commit response declared no sha for branch {branch}")
        tip = tip_resp["sha"]
        # The tip sha is remote metadata that is INTERPOLATED into output
        # (verdict lines, SOURCE block). Truthiness is not enough: require a
        # strict single-token sha (16-64 alphanumeric chars — real commits
        # are exactly 40 hex) so newlines/backticks/ANSI in the response can
        # never inject provenance text or forge output lines.
        if not isinstance(tip, str) or not re.fullmatch(r"[0-9A-Za-z]{16,64}", tip):
            fail(f"tip commit response declared an invalid sha for branch {branch}")

        # Snapshot validation first: every manifest path's local bytes must
        # match the manifest hashes (both modes). INTERMEDIATE components
        # are walked NOFOLLOW dir_fd-relative (a pre-open pivot of a nested
        # directory — e.g. assets/upstream/docs → an external matching-hash
        # tree — is a sanitized ERROR before any bytes are read); ONLY the
        # final component may be followed (the pinned read contract:
        # replace-not-follow on writes, SHA-disciplined read-through), and
        # that read is SIZE-CAPPED at the manifest-declared bytes + 64KB
        # slack; a per-entry re-walk reads the CURRENT directory state, so
        # pivots between entries are caught by the walk/regular-file checks
        # themselves.
        up_fd = walk_dirs(manifest_rel[:2], root_fd, "snapshot path")
        try:
            for entry in manifest["files"]:
                declared = entry["bytes"]
                if not isinstance(declared, int) or declared < 0:
                    fail("manifest entry bytes is not a sane integer for " + str(entry["path"]))
                snap_dirs, snap_name = split_path(entry["path"])
                snap_fd = walk_dirs(snap_dirs, up_fd, "snapshot path")
                try:
                    data = read_regular_at_fd(
                        snap_fd, snap_name, "local snapshot",
                        require_regular=False,
                        max_bytes=declared + 65536,
                    )
                except Missing:
                    fail("local snapshot file missing: " + entry["path"])
                finally:
                    try:
                        os.close(snap_fd)
                    except OSError:
                        pass
                if len(data) != declared or \
                        hashlib.sha256(data).hexdigest() != entry["sha256"]:
                    fail("local snapshot mismatch for " + entry["path"])
        finally:
            try:
                os.close(up_fd)
            except OSError:
                pass

        if not update_mode:
            # Verdict baseline: the human-integrated pin — the SOURCE block's
            # Integrated pin when present; otherwise the manifest integrated
            # commit (never the fetched resolved_commit — see the F4 block
            # above; absence of provenance never authenticates). Fetched-only
            # state never yields UNCHANGED.
            baseline = manifest_integrated
            if src_text is not None:
                pin = extract_source_pin(src_text, allow_blockless=False)
                if pin is not None:
                    baseline = pin
            for entry in manifest["files"]:
                pinned = content_bytes(entry["path"], baseline)
                at_tip = content_bytes(entry["path"], tip)
                # UNCHANGED only when the integrated pin's content matches
                # the tip ref per path (baseline == tip makes this vacuous
                # but the fetches stay data-only, no verdict shortcut
                # needed).
                if pinned != at_tip:
                    print("CHANGED")
                    sys.exit(0)
            print("UNCHANGED")
            sys.exit(0)

        # ---- authorized refresh (--update) ----
        # Stage the COMPLETE tip snapshot first; any failure before this
        # point is a fetch-phase failure: fail() removes THIS run's staging
        # (dirfd-relative), the tracked files and SOURCE.md stay untouched
        # (pinned cleanup semantics).
        verify_boundary("staging plan")
        staging_name = f"staging-{os.getpid()}-{time.time_ns()}"
        try:
            os.mkdir(staging_name, dir_fd=cache_fd)
        except OSError as exc:
            fail(f"cannot create staging dir: {exc}")
        # Revalidate the created staging dir: a symlink swapped into its
        # name between mkdir and open must ERROR, never be traversed.
        staging_fd = open_dir_at(cache_fd, staging_name, "staging dir")

        new_files = []
        for entry in manifest["files"]:
            path = entry["path"]
            data = content_bytes(path, tip)
            # Staging write discipline: full ancestor chain validated
            # dirfd-relative against the held STAGING dirfd (creation +
            # post-creation revalidation), temp+os.replace route — no plain
            # write-through-symlink anywhere.
            subdirs, fname = split_path(path)
            guarded_write(subdirs, fname, data, staging_fd, "staging write")
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
        # Preserve the integrated commit BY DEFAULT (a fetch never advances
        # it); the sync arm below may bump it when the human already
        # integrated the previously fetched resolved commit.
        new_integrated = manifest_integrated

        # SOURCE.md check-status block must exist and keep the integrated
        # pin entry (outside the block) untouched; the block is
        # checker-maintained. Re-read THROUGH the pinned dirfd walk (fresh,
        # O_NOFOLLOW, fstat S_ISREG on the same fd — no lstat→read swap
        # window).
        old_text = read_provenance()
        if old_text is None:
            # Specific reason for the hygiene-contract case (a missing/
            # removed SOURCE.md is a common partial state; the generic
            # router would say only "unexpected FileNotFoundError").
            fail("SOURCE.md not found for authorized refresh: " + "/".join(source_rel))
        old_block_pin = extract_source_pin(old_text, allow_blockless=False)
        # extract_source_pin validated the block; re-scan the (b, e) markers
        # for the surgical rewrite below (same file bytes, same regexes).
        b = BEGIN.search(old_text)
        e = END.search(old_text, b.end())
        old_block = old_text[b.end():e.start()]
        lines = old_block.splitlines()
        pin_start = next(
            (i for i, l in enumerate(lines) if l.startswith("- Integrated pin")), None
        )
        if pin_start is None:
            fail("check-status block has no Integrated pin line")
        # Preserve the COMPLETE Integrated pin entry (it may wrap over
        # several physical lines; the indented continuation lines belong to
        # the entry). The entry is the last entry of the block, so it runs
        # to the block end.
        pin_entry = "\n".join(lines[pin_start:])
        new_block = fresh(time.strftime("%Y-%m-%d", time.gmtime()), tip) + pin_entry

        # Integration sync (binding M1 rule): if the SOURCE block's pin
        # already equals the PREVIOUSLY resolved commit, a human reviewed
        # and integrated that fetched tip — this run (the next one after
        # the integration, since check-only never writes) syncs the
        # manifest integrated_commit to it; the new tip then becomes
        # fetched-but-unreviewed again. A fetch alone can never advance
        # integrated_commit.
        if old_block_pin == manifest["resolved_commit"]:
            new_integrated = manifest["resolved_commit"]
        new_manifest["integrated_commit"] = new_integrated
        guarded_write(
            (), "MANIFEST.json",
            (json.dumps(new_manifest, indent=2) + "\n").encode(),
            staging_fd, "staging manifest write",
        )

        # Cutover: temp-file + atomic-rename for EVERY live file, ordered so
        # the crash window is narrow and every partial state is detectable —
        # raw snapshot files first, MANIFEST.json second, SOURCE.md block
        # last. Crash-window table (accurate, supersedes any blanket "next
        # check is always ERROR" claim):
        #   (i)   crash before the first live replacement → prior state
        #         intact; next check UNCHANGED/CHANGED as before the
        #         refresh.
        #   (ii)  crash during raw-file replacement → old MANIFEST hashes
        #         vs new raw bytes → next check ERROR "local snapshot
        #         mismatch".
        #   (iii) crash after MANIFEST replaced, before SOURCE → coherent
        #         fetched snapshot + OLD integrated pin → next check
        #         CHANGED (not ERROR, and never UNCHANGED).
        #   (iv)  crash after SOURCE written → complete cutover; residue
        #         (if a crash skips cleanup) is staging/lock dirs,
        #         recoverable by the next run or manually.
        # No fsync / power-loss durability claim: this narrows the failure
        # window under ordinary process death, not under abrupt power loss.
        # On any HANDLED failure from here on, staging is RETAINED as the
        # recovery copy (fail() honors retain_staging and names the path).
        retain_staging = True
        assets_fd = walk_dirs(("assets",), root_fd, "cutover path")
        try:
            # Every cutover write is dirfd-anchored: `assets_fd` is opened
            # nofollow relative to the held root fd, so neither a .cache nor
            # a root pathname swap can redirect the writes.
            for entry in new_files:
                subdirs, fname = split_path(entry["path"])
                # Read the staged bytes dirfd-relative (dup fd — walk_dirs
                # NEVER returns a borrowed fd; a planted staged symlink
                # cannot be followed).
                staged_fd = walk_dirs(subdirs, staging_fd, "staged read path (caller-owned dup)")
                try:
                    staged = read_regular_at_fd(staged_fd, fname, "staged snapshot")
                except Missing:
                    fail("staged snapshot file missing: " + entry["path"])
                finally:
                    try:
                        os.close(staged_fd)
                    except OSError:
                        pass
                guarded_write(("upstream",) + subdirs, fname, staged,
                              assets_fd, "cutover write")
            try:
                staged_manifest = read_regular_at_fd(staging_fd, "MANIFEST.json", "staged manifest")
            except Missing:
                fail("staged MANIFEST.json missing")
            guarded_write(("upstream",), manifest_rel[2], staged_manifest,
                          assets_fd, "cutover manifest write")
        finally:
            try:
                os.close(assets_fd)
            except OSError:
                pass
        guarded_write(("references",), source_rel[1],
                      (old_text[: b.end()] + new_block.rstrip("\n") + "\n"
                       + old_text[e.start():]).encode("utf-8"),
                      root_fd, "cutover provenance write")

        remove_staging()
        release_lock()
        print(f"UPDATED {tip}")
        sys.exit(0)
    finally:
        # Success-path fd hygiene: close the fds this run held. (Failure
        # paths exit earlier through fail(), which releases its own.)
        for held_fd in (globals().get("staging_fd"), globals().get("cache_fd"),
                        globals().get("root_fd")):
            if held_fd is not None:
                try:
                    os.close(held_fd)
                except OSError:
                    pass


try:
    main()
except SystemExit:
    raise
except Exception as exc:  # noqa: BLE001 - never escape a raw traceback
    # Route any unexpected failure (including cutover I/O failures) to the
    # sanitized ERROR verdict with nonzero exit. fail() retains staging when
    # a complete snapshot is staged and removes only this run's own state;
    # live files may be mid-cutover — see the crash-window table in the
    # cutover section for what the next check will report per window.
    fail(f"unexpected {type(exc).__name__}: {exc}")
PYEOF
