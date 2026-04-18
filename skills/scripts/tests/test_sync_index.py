"""Tests for sync-index.py — sync, validate, tag_index, search, lookup, staleness."""

from __future__ import annotations

import importlib
import importlib.util
import json
import sys
import textwrap
from pathlib import Path
from unittest.mock import patch

import pytest
import yaml

_SCRIPTS_DIR = Path(__file__).resolve().parent.parent
_sync_index_path = _SCRIPTS_DIR / "sync-index.py"

if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

_spec = importlib.util.spec_from_file_location("sync_index", _sync_index_path)
sync_index = importlib.util.module_from_spec(_spec)  # type: ignore[attr-defined]
_spec.loader.exec_module(sync_index)  # type: ignore[union-attr]

SKILLS_DIR = _SCRIPTS_DIR.parent


@pytest.fixture
def tmp_skill_tree(tmp_path: Path) -> Path:
    """Create a minimal skill tree for testing."""
    skills = tmp_path / "skills"
    skills.mkdir()

    (skills / "foo-bar" / "references").mkdir(parents=True)
    (skills / "foo-bar" / "SKILL.md").write_text(
        textwrap.dedent("""\
        ---
        name: foo-bar
        description: A test skill for foo bar operations.
        tags:
          - testing
          - foo
        triggers:
          - foo bar
          - test foo
        license: MIT
        metadata:
          author: test
          version: "1.0"
        ---
        # Foo Bar

        Test instructions.
        """),
        encoding="utf-8",
    )

    (skills / "baz-qux").mkdir()
    (skills / "baz-qux" / "SKILL.md").write_text(
        textwrap.dedent("""\
        ---
        name: baz-qux
        description: A test skill for baz qux operations.
        tags:
          - testing
          - qux
        ---
        # Baz Qux

        More test instructions.
        """),
        encoding="utf-8",
    )

    lock = {"foo-bar": {"source": "https://example.com/repo", "ref": "main", "installed_at": "2026-01-01"}}
    (skills / "skills-lock.json").write_text(json.dumps({"skills": lock}), encoding="utf-8")

    return skills


@pytest.fixture
def patched_skills_dir(tmp_skill_tree: Path):
    """Patch SKILLS_DIR to use tmp tree."""
    with (
        patch.object(sync_index, "SKILLS_DIR", tmp_skill_tree),
        patch.object(sync_index, "INDEX_PATH", tmp_skill_tree / "SKILL_INDEX.yaml"),
        patch.object(sync_index, "LOCK_PATH", tmp_skill_tree / "skills-lock.json"),
    ):
        yield tmp_skill_tree


class TestDiscovery:
    def test_discovers_flat_skill_dirs(self, patched_skills_dir: Path):
        dirs = sync_index._discover_skill_dirs()
        names = {d.name for d in dirs}
        assert names == {"foo-bar", "baz-qux"}

    def test_ignores_hidden_dirs(self, patched_skills_dir: Path):
        hidden = patched_skills_dir / ".hidden-skill"
        hidden.mkdir()
        (hidden / "SKILL.md").write_text("---\nname: hidden\n---\nbody", encoding="utf-8")
        dirs = sync_index._discover_skill_dirs()
        names = {d.name for d in dirs}
        assert "hidden" not in names

    def test_ignores_scripts_dir(self, patched_skills_dir: Path):
        scripts = patched_skills_dir / "scripts"
        scripts.mkdir()
        (scripts / "SKILL.md").write_text("---\nname: scripts\n---\nbody", encoding="utf-8")
        dirs = sync_index._discover_skill_dirs()
        names = {d.name for d in dirs}
        assert "scripts" not in names


class TestValidation:
    def test_valid_skill_passes(self, patched_skills_dir: Path):
        skill_dir = patched_skills_dir / "foo-bar"
        errors = sync_index.validate_skill(skill_dir)
        assert errors == []

    def test_missing_skill_md_fails(self, patched_skills_dir: Path):
        empty = patched_skills_dir / "empty-skill"
        empty.mkdir()
        errors = sync_index.validate_skill(empty)
        assert any("Missing required file" in e for e in errors)

    def test_name_dir_mismatch_fails(self, patched_skills_dir: Path):
        bad = patched_skills_dir / "wrong-name"
        bad.mkdir()
        (bad / "SKILL.md").write_text(
            "---\nname: different-name\ndescription: test\n---\nbody", encoding="utf-8"
        )
        errors = sync_index.validate_skill(bad)
        assert any("must match" in e for e in errors)

    def test_missing_description_fails(self, patched_skills_dir: Path):
        bad = patched_skills_dir / "no-desc"
        bad.mkdir()
        (bad / "SKILL.md").write_text("---\nname: no-desc\n---\nbody", encoding="utf-8")
        errors = sync_index.validate_skill(bad)
        assert any("description" in e.lower() for e in errors)

    def test_empty_body_warns(self, patched_skills_dir: Path):
        bad = patched_skills_dir / "empty-body"
        bad.mkdir()
        (bad / "SKILL.md").write_text(
            "---\nname: empty-body\ndescription: test\n---\n", encoding="utf-8"
        )
        errors = sync_index.validate_skill(bad)
        assert any("empty" in e.lower() for e in errors)

    def test_unknown_fields_flagged(self, patched_skills_dir: Path):
        bad = patched_skills_dir / "unknown-fields"
        bad.mkdir()
        (bad / "SKILL.md").write_text(
            "---\nname: unknown-fields\ndescription: test\nbogus_field: true\n---\nbody",
            encoding="utf-8",
        )
        errors = sync_index.validate_skill(bad)
        assert any("Unknown fields" in e for e in errors)

    def test_uppercase_name_fails(self, patched_skills_dir: Path):
        bad = patched_skills_dir / "UPPER"
        bad.mkdir()
        (bad / "SKILL.md").write_text(
            "---\nname: UPPER\ndescription: test\n---\nbody", encoding="utf-8"
        )
        errors = sync_index.validate_skill(bad)
        assert any("lowercase" in e.lower() for e in errors)

    def test_double_hyphen_name_fails(self, patched_skills_dir: Path):
        bad = patched_skills_dir / "bad--name"
        bad.mkdir()
        (bad / "SKILL.md").write_text(
            "---\nname: bad--name\ndescription: test\n---\nbody", encoding="utf-8"
        )
        errors = sync_index.validate_skill(bad)
        assert any("consecutive" in e.lower() for e in errors)


class TestSync:
    def test_sync_generates_index(self, patched_skills_dir: Path):
        entries = sync_index.scan_skills()
        sync_index.write_index(entries)
        index_path = patched_skills_dir / "SKILL_INDEX.yaml"
        assert index_path.exists()
        data = yaml.safe_load(index_path.read_text(encoding="utf-8"))
        names = {e["name"] for e in data["skills"]}
        assert names == {"foo-bar", "baz-qux"}

    def test_sync_includes_tag_index(self, patched_skills_dir: Path):
        entries = sync_index.scan_skills()
        sync_index.write_index(entries)
        index_path = patched_skills_dir / "SKILL_INDEX.yaml"
        data = yaml.safe_load(index_path.read_text(encoding="utf-8"))
        tag_index = data.get("tag_index", {})
        assert "testing" in tag_index
        assert set(tag_index["testing"]) == {"foo-bar", "baz-qux"}
        assert "foo" in tag_index
        assert tag_index["foo"] == ["foo-bar"]

    def test_sync_flat_paths(self, patched_skills_dir: Path):
        entries = sync_index.scan_skills()
        for entry in entries:
            assert "/" not in entry["path"], f"Path should be flat: {entry['path']}"

    def test_sync_merges_lock_data(self, patched_skills_dir: Path):
        entries = sync_index.scan_skills()
        foo = next(e for e in entries if e["name"] == "foo-bar")
        assert "source" in foo
        assert foo["source"]["source"] == "https://example.com/repo"

    def test_sync_preserves_triggers(self, patched_skills_dir: Path):
        entries = sync_index.scan_skills()
        foo = next(e for e in entries if e["name"] == "foo-bar")
        assert "triggers" in foo
        assert "foo bar" in foo["triggers"]


class TestTagIndex:
    def test_tag_index_sorted_by_tag(self, tmp_path: Path):
        entries = [
            {"name": "c", "tags": ["beta"]},
            {"name": "a", "tags": ["alpha"]},
            {"name": "b", "tags": ["alpha", "beta"]},
        ]
        result = sync_index._build_tag_index(entries)
        assert list(result.keys()) == ["alpha", "beta"]
        assert result["alpha"] == ["a", "b"]
        assert result["beta"] == ["b", "c"]

    def test_tag_index_empty_skills(self):
        assert sync_index._build_tag_index([]) == {}

    def test_tag_index_case_insensitive(self):
        entries = [{"name": "x", "tags": ["Foo", "foo"]}]
        result = sync_index._build_tag_index(entries)
        assert "foo" in result
        assert result["foo"] == ["x"]


class TestSearch:
    def test_search_by_trigger(self, patched_skills_dir: Path):
        entries = sync_index.scan_skills()
        results = sync_index.search_skills("foo bar", entries)
        assert len(results) > 0
        assert results[0]["name"] == "foo-bar"

    def test_search_by_tag(self, patched_skills_dir: Path):
        entries = sync_index.scan_skills()
        results = sync_index.search_skills("qux", entries)
        assert len(results) > 0
        assert results[0]["name"] == "baz-qux"

    def test_search_no_results(self, patched_skills_dir: Path):
        entries = sync_index.scan_skills()
        results = sync_index.search_skills("zzzzz-nonexistent", entries)
        assert results == []


class TestLookup:
    def test_lookup_existing(self, patched_skills_dir: Path):
        entries = sync_index.scan_skills()
        result = sync_index.find_by_name("foo-bar", entries)
        assert result is not None
        assert result["name"] == "foo-bar"

    def test_lookup_missing(self, patched_skills_dir: Path):
        entries = sync_index.scan_skills()
        assert sync_index.find_by_name("nonexistent", entries) is None

    def test_lookup_case_insensitive(self, patched_skills_dir: Path):
        entries = sync_index.scan_skills()
        assert sync_index.find_by_name("FOO-BAR", entries) is not None


class TestTagFilter:
    def test_filter_by_tag(self, patched_skills_dir: Path):
        entries = sync_index.scan_skills()
        results = sync_index.filter_by_tag("foo", entries)
        assert len(results) == 1
        assert results[0]["name"] == "foo-bar"

    def test_filter_no_match(self, patched_skills_dir: Path):
        entries = sync_index.scan_skills()
        assert sync_index.filter_by_tag("nonexistent", entries) == []


class TestStaleness:
    def test_stale_skill_detected(self, patched_skills_dir: Path):
        entries = sync_index.scan_skills()
        warnings = sync_index.check_staleness(entries, stale_days=30)
        assert any("foo-bar" in w for w in warnings)

    def test_fresh_skill_no_warning(self, patched_skills_dir: Path):
        entries = sync_index.scan_skills()
        warnings = sync_index.check_staleness(entries, stale_days=9999)
        assert warnings == []


class TestRealSkills:
    """Validate the actual skills in the repo."""

    def test_real_validate_all(self):
        results = sync_index.validate_all_skills()
        for name, errors in results.items():
            assert errors == [], f"Validation failed for {name}: {errors}"

    def test_real_sync_and_tag_index(self):
        entries = sync_index.scan_skills()
        tag_index = sync_index._build_tag_index(entries)
        assert len(tag_index) > 0
        assert "security" in tag_index
        assert "verification" in tag_index

    def test_real_all_paths_flat(self):
        entries = sync_index.scan_skills()
        for entry in entries:
            parts = entry["path"].split("/")
            if parts[0] == "android":
                continue  # android group is an accepted prefix
            assert len(parts) == 1, f"Non-android skill has nested path: {entry['path']}"

    def test_real_names_match_dirs(self):
        for skill_dir in sync_index._discover_skill_dirs():
            fm = sync_index.parse_frontmatter(skill_dir / "SKILL.md")
            assert fm is not None, f"No frontmatter in {skill_dir}"
            assert fm["name"] == skill_dir.name, f"Name/dir mismatch: {fm['name']} vs {skill_dir.name}"
