"""Tests for sync-index.py — validators, parsing, search, indexing.

Tests cover all pure functions: validators, frontmatter parsing,
search scoring, name lookup, tag filtering, and scan logic.
"""

from __future__ import annotations

import importlib
import json
import unicodedata
from pathlib import Path

import pytest
import yaml

sync_index = importlib.import_module("sync-index")


def _write_skill(tmp_path: Path, name: str, description: str, **extra: object) -> Path:
    skill_dir = tmp_path / name
    skill_dir.mkdir(parents=True, exist_ok=True)
    fm = {"name": name, "description": description, **extra}
    body = extra.pop("_body", "Instructions go here.")
    content = f"---\n{yaml.dump(fm, default_flow_style=False)}---\n\n{body}\n"
    (skill_dir / "SKILL.md").write_text(content, encoding="utf-8")
    return skill_dir


class TestParseFrontmatter:
    def test_valid_frontmatter(self, tmp_path: Path):
        p = tmp_path / "SKILL.md"
        p.write_text("---\nname: foo\ndescription: bar\n---\nBody\n")
        result = sync_index.parse_frontmatter(p)
        assert result == {"name": "foo", "description": "bar"}

    def test_no_frontmatter(self, tmp_path: Path):
        p = tmp_path / "SKILL.md"
        p.write_text("Just regular text\n")
        assert sync_index.parse_frontmatter(p) is None

    def test_unclosed_frontmatter(self, tmp_path: Path):
        p = tmp_path / "SKILL.md"
        p.write_text("---\nname: foo\n")
        assert sync_index.parse_frontmatter(p) is None

    def test_invalid_yaml(self, tmp_path: Path):
        p = tmp_path / "SKILL.md"
        p.write_text("---\n: [invalid\n---\n")
        assert sync_index.parse_frontmatter(p) is None

    def test_non_dict_frontmatter(self, tmp_path: Path):
        p = tmp_path / "SKILL.md"
        p.write_text("---\n- item1\n- item2\n---\n")
        assert sync_index.parse_frontmatter(p) is None

    def test_empty_frontmatter(self, tmp_path: Path):
        p = tmp_path / "SKILL.md"
        p.write_text("---\n---\nBody\n")
        assert sync_index.parse_frontmatter(p) is None


class TestValidateName:
    def test_valid_name(self):
        assert sync_index.validate_name("my-skill") == []

    def test_valid_name_with_numbers(self):
        assert sync_index.validate_name("skill-v2") == []

    def test_empty_string(self):
        errors = sync_index.validate_name("")
        assert any("non-empty" in e for e in errors)

    def test_not_a_string(self):
        errors = sync_index.validate_name(123)  # type: ignore[arg-type]
        assert any("non-empty" in e for e in errors)

    def test_uppercase_rejected(self):
        errors = sync_index.validate_name("MySkill")
        assert any("lowercase" in e for e in errors)

    def test_starts_with_hyphen(self):
        errors = sync_index.validate_name("-skill")
        assert any("hyphen" in e for e in errors)

    def test_ends_with_hyphen(self):
        errors = sync_index.validate_name("skill-")
        assert any("hyphen" in e for e in errors)

    def test_consecutive_hyphens(self):
        errors = sync_index.validate_name("my--skill")
        assert any("consecutive" in e for e in errors)

    def test_spaces_rejected(self):
        errors = sync_index.validate_name("my skill")
        assert any("invalid characters" in e for e in errors)

    def test_underscores_rejected(self):
        errors = sync_index.validate_name("my_skill")
        assert any("invalid characters" in e for e in errors)

    def test_exceeds_max_length(self):
        name = "a" * (sync_index.MAX_NAME_LENGTH + 1)
        errors = sync_index.validate_name(name)
        assert any("exceeds" in e for e in errors)

    def test_dir_name_mismatch(self):
        errors = sync_index.validate_name("foo", dir_name="bar")
        assert any("must match" in e for e in errors)

    def test_dir_name_match(self):
        assert sync_index.validate_name("foo", dir_name="foo") == []

    def test_unicode_normalization(self):
        name = "skill\ufb01x"
        normalized = unicodedata.normalize("NFKC", name)
        errors = sync_index.validate_name(name)
        has_issue = any("invalid characters" in e for e in errors) or "skillfix" in normalized
        assert has_issue or normalized == name


class TestValidateDescription:
    def test_valid_description(self):
        assert sync_index.validate_description("A useful skill") == []

    def test_empty_string(self):
        errors = sync_index.validate_description("")
        assert any("non-empty" in e for e in errors)

    def test_not_a_string(self):
        errors = sync_index.validate_description(None)  # type: ignore[arg-type]
        assert any("non-empty" in e for e in errors)

    def test_whitespace_only(self):
        errors = sync_index.validate_description("   ")
        assert any("non-empty" in e for e in errors)

    def test_exceeds_max_length(self):
        desc = "x" * (sync_index.MAX_DESCRIPTION_LENGTH + 1)
        errors = sync_index.validate_description(desc)
        assert any("exceeds" in e for e in errors)

    def test_at_max_length_ok(self):
        desc = "x" * sync_index.MAX_DESCRIPTION_LENGTH
        assert sync_index.validate_description(desc) == []


class TestValidateCompatibility:
    def test_valid(self):
        assert sync_index.validate_compatibility(">=3.12") == []

    def test_not_string(self):
        errors = sync_index.validate_compatibility(["3.12"])  # type: ignore[arg-type]
        assert any("must be a string" in e for e in errors)

    def test_exceeds_length(self):
        val = "x" * (sync_index.MAX_COMPATIBILITY_LENGTH + 1)
        errors = sync_index.validate_compatibility(val)
        assert any("exceeds" in e for e in errors)


class TestValidateMetadata:
    def test_valid(self):
        assert sync_index.validate_metadata({"version": "1.0", "author": "test"}) == []

    def test_not_dict(self):
        errors = sync_index.validate_metadata("bad")  # type: ignore[arg-type]
        assert any("must be a mapping" in e for e in errors)

    def test_non_string_value(self):
        errors = sync_index.validate_metadata({"version": 1})
        assert any("must be strings" in e for e in errors)

    def test_nested_list_value(self):
        errors = sync_index.validate_metadata({"tags": ["a", "b"]})
        assert any("must be strings" in e for e in errors)


class TestValidateSource:
    def test_valid_full(self):
        src = {"repo": "https://github.com/org/repo", "ref": "main"}
        assert sync_index.validate_source(src) == []

    def test_missing_repo(self):
        errors = sync_index.validate_source({"ref": "main"})
        assert any("repo is required" in e for e in errors)

    def test_empty_repo(self):
        errors = sync_index.validate_source({"repo": ""})
        assert any("repo is required" in e for e in errors)

    def test_not_dict(self):
        errors = sync_index.validate_source("bad")  # type: ignore[arg-type]
        assert any("must be a mapping" in e for e in errors)

    def test_non_string_fields(self):
        errors = sync_index.validate_source({"repo": "url", "ref": 123})
        assert any("must be a string" in e for e in errors)


class TestValidateTriggers:
    def test_valid(self):
        assert sync_index.validate_triggers(["deploy", "release"]) == []

    def test_not_list(self):
        errors = sync_index.validate_triggers("deploy")  # type: ignore[arg-type]
        assert any("must be a list" in e for e in errors)

    def test_empty_list(self):
        errors = sync_index.validate_triggers([])
        assert any("not be empty" in e for e in errors)

    def test_non_string_item(self):
        errors = sync_index.validate_triggers(["ok", 42])
        assert any("must be a string" in e for e in errors)


class TestValidateTags:
    def test_valid(self):
        assert sync_index.validate_tags(["security", "testing"]) == []

    def test_not_list(self):
        errors = sync_index.validate_tags("security")  # type: ignore[arg-type]
        assert any("must be a list" in e for e in errors)

    def test_empty_list(self):
        errors = sync_index.validate_tags([])
        assert any("not be empty" in e for e in errors)

    def test_non_string_item(self):
        errors = sync_index.validate_tags(["ok", None])  # type: ignore[list-item]
        assert any("must be a string" in e for e in errors)


class TestValidateSkill:
    def test_valid_skill(self, tmp_path: Path):
        d = _write_skill(tmp_path, "my-skill", "A skill")
        assert sync_index.validate_skill(d) == []

    def test_missing_dir(self, tmp_path: Path):
        errors = sync_index.validate_skill(tmp_path / "nonexistent")
        assert any("does not exist" in e for e in errors)

    def test_file_not_dir(self, tmp_path: Path):
        f = tmp_path / "not-a-dir"
        f.write_text("data")
        errors = sync_index.validate_skill(f)
        assert any("Not a directory" in e for e in errors)

    def test_missing_skill_md(self, tmp_path: Path):
        d = tmp_path / "empty-skill"
        d.mkdir()
        errors = sync_index.validate_skill(d)
        assert any("Missing required" in e for e in errors)

    def test_lowercase_skill_md_warns(self, tmp_path: Path):
        d = tmp_path / "my-skill"
        d.mkdir()
        fm = {"name": "my-skill", "description": "desc"}
        content = f"---\n{yaml.dump(fm, default_flow_style=False)}---\n\nBody\n"
        (d / "skill.md").write_text(content)
        skill_upper = d / "SKILL.md"
        if skill_upper.exists() and skill_upper.samefile(d / "skill.md"):
            pytest.skip("case-insensitive filesystem (SKILL.md == skill.md)")
        errors = sync_index.validate_skill(d)
        assert any("uppercase" in e for e in errors)

    def test_no_frontmatter(self, tmp_path: Path):
        d = tmp_path / "my-skill"
        d.mkdir()
        (d / "SKILL.md").write_text("No frontmatter here")
        errors = sync_index.validate_skill(d)
        assert any("frontmatter" in e for e in errors)

    def test_unknown_fields(self, tmp_path: Path):
        d = _write_skill(tmp_path, "my-skill", "desc", foobar="bad")
        errors = sync_index.validate_skill(d)
        assert any("Unknown fields" in e for e in errors)

    def test_missing_name(self, tmp_path: Path):
        d = tmp_path / "myskill"
        d.mkdir()
        content = "---\ndescription: desc\n---\n\nBody\n"
        (d / "SKILL.md").write_text(content)
        errors = sync_index.validate_skill(d)
        assert any("Missing required field: name" in e for e in errors)

    def test_missing_description(self, tmp_path: Path):
        d = tmp_path / "myskill"
        d.mkdir()
        content = "---\nname: myskill\n---\n\nBody\n"
        (d / "SKILL.md").write_text(content)
        errors = sync_index.validate_skill(d)
        assert any("Missing required field: description" in e for e in errors)

    def test_empty_body(self, tmp_path: Path):
        d = _write_skill(tmp_path, "my-skill", "desc", _body="")
        errors = sync_index.validate_skill(d)
        assert any("body is empty" in e for e in errors)

    def test_too_long_file(self, tmp_path: Path):
        d = tmp_path / "my-skill"
        d.mkdir()
        lines = ["---", "name: my-skill", "description: desc", "---", ""]
        lines.extend(f"line {i}" for i in range(600))
        (d / "SKILL.md").write_text("\n".join(lines))
        errors = sync_index.validate_skill(d)
        assert any("spec recommends" in e for e in errors)


class TestTokenize:
    def test_simple(self):
        assert sync_index._tokenize("hello world") == {"hello", "world"}

    def test_mixed_case(self):
        assert sync_index._tokenize("Hello World") == {"hello", "world"}

    def test_with_punctuation(self):
        assert sync_index._tokenize("hello, world! test-case") == {"hello", "world", "test", "case"}

    def test_empty(self):
        assert sync_index._tokenize("") == set()

    def test_numbers(self):
        assert sync_index._tokenize("python3 web") == {"python3", "web"}


class TestSearchScore:
    def _entry(self, **kw: object) -> dict:
        return {"name": "test", "description": "a test skill", **kw}

    def test_name_match_highest(self):
        q = {"deploy"}
        score = sync_index._search_score(q, self._entry(name="deploy-skill"))
        assert score > 0

    def test_trigger_match(self):
        q = {"deploy"}
        score = sync_index._search_score(q, self._entry(triggers=["deploy", "release"]))
        assert score > 0

    def test_tag_match(self):
        q = {"security"}
        score = sync_index._search_score(q, self._entry(tags=["security", "testing"]))
        assert score > 0

    def test_description_match_lowest(self):
        q = {"pipeline"}
        score = sync_index._search_score(q, self._entry(description="pipeline tool"))
        assert score > 0

    def test_no_match_zero(self):
        q = {"nonexistent"}
        score = sync_index._search_score(q, self._entry())
        assert score == 0.0

    def test_name_weights_higher_than_desc(self):
        q = {"search"}
        name_score = sync_index._search_score(q, self._entry(name="search-tool"))
        desc_score = sync_index._search_score(q, self._entry(description="search utility"))
        assert name_score > desc_score

    def test_trigger_substring_match(self):
        q = {"deploy"}
        score = sync_index._search_score(q, self._entry(triggers=["auto-deploy"]))
        assert score > 0

    def test_coverage_bonus(self):
        q = {"deploy", "fast"}
        entry = self._entry(name="deploy-fast", description="deploy fast")
        score = sync_index._search_score(q, entry)
        assert score > 0


class TestSearchSkills:
    def _skills(self) -> list[dict]:
        return [
            {"name": "deploy", "description": "deploy things", "triggers": ["deploy", "release"], "tags": []},
            {"name": "security", "description": "security scanner", "triggers": ["scan"], "tags": ["security"]},
            {"name": "testing", "description": "test runner", "triggers": ["test"], "tags": ["testing"]},
        ]

    def test_finds_matching(self):
        results = sync_index.search_skills("deploy", self._skills())
        assert len(results) >= 1
        assert results[0]["name"] == "deploy"

    def test_empty_query_returns_top(self):
        results = sync_index.search_skills("", self._skills(), top=2)
        assert len(results) == 2

    def test_no_match_returns_empty(self):
        results = sync_index.search_skills("nonexistent-xyz", self._skills())
        assert results == []

    def test_scores_rounded(self):
        results = sync_index.search_skills("deploy", self._skills())
        for r in results:
            assert r["score"] == round(r["score"], 2)

    def test_top_limit(self):
        results = sync_index.search_skills("e", self._skills(), top=1)
        assert len(results) <= 1


class TestFindByName:
    def _skills(self) -> list[dict]:
        return [
            {"name": "deploy", "description": "deploy things"},
            {"name": "security-scan", "description": "scanner"},
        ]

    def test_found(self):
        assert sync_index.find_by_name("deploy", self._skills()) is not None

    def test_case_insensitive(self):
        assert sync_index.find_by_name("Deploy", self._skills()) is not None

    def test_not_found(self):
        assert sync_index.find_by_name("nonexistent", self._skills()) is None


class TestFilterByTag:
    def _skills(self) -> list[dict]:
        return [
            {"name": "a", "description": "a", "tags": ["security", "testing"]},
            {"name": "b", "description": "b", "tags": ["deploy"]},
        ]

    def test_found(self):
        results = sync_index.filter_by_tag("security", self._skills())
        assert len(results) == 1
        assert results[0]["name"] == "a"

    def test_case_insensitive(self):
        results = sync_index.filter_by_tag("SECURITY", self._skills())
        assert len(results) == 1

    def test_no_match(self):
        results = sync_index.filter_by_tag("nonexistent", self._skills())
        assert results == []

    def test_no_tags_field(self):
        skills = [{"name": "c", "description": "c"}]
        assert sync_index.filter_by_tag("anything", skills) == []


class TestLoadLock:
    def test_missing_file(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        monkeypatch.setattr(sync_index, "LOCK_PATH", tmp_path / "nope.json")
        assert sync_index.load_lock() == {}

    def test_invalid_json(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        lock = tmp_path / "skills-lock.json"
        lock.write_text("not json")
        monkeypatch.setattr(sync_index, "LOCK_PATH", lock)
        assert sync_index.load_lock() == {}

    def test_valid_lock(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        lock = tmp_path / "skills-lock.json"
        lock.write_text(json.dumps({"skills": {"my-skill": {"source": "git"}}}))
        monkeypatch.setattr(sync_index, "LOCK_PATH", lock)
        result = sync_index.load_lock()
        assert "my-skill" in result

    def test_non_dict_top_level(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        lock = tmp_path / "skills-lock.json"
        lock.write_text(json.dumps([1, 2, 3]))
        monkeypatch.setattr(sync_index, "LOCK_PATH", lock)
        assert sync_index.load_lock() == {}


class TestScanSkills:
    def test_scans_valid_skills(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        monkeypatch.setattr(sync_index, "SKILLS_DIR", tmp_path)
        _write_skill(tmp_path, "alpha", "Alpha skill")
        _write_skill(tmp_path, "beta", "Beta skill")
        entries = sync_index.scan_skills()
        names = [e["name"] for e in entries]
        assert "alpha" in names
        assert "beta" in names

    def test_skips_excluded_dirs(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        monkeypatch.setattr(sync_index, "SKILLS_DIR", tmp_path)
        _write_skill(tmp_path, "good", "Good skill")
        hidden = tmp_path / ".hidden"
        hidden.mkdir()
        (hidden / "SKILL.md").write_text("---\nname: hidden\n---\nBody")
        entries = sync_index.scan_skills()
        assert all(e["name"] != "hidden" for e in entries)

    def test_skips_no_skill_md(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        monkeypatch.setattr(sync_index, "SKILLS_DIR", tmp_path)
        empty = tmp_path / "empty"
        empty.mkdir()
        entries = sync_index.scan_skills()
        assert all(e["name"] != "empty" for e in entries)

    def test_includes_triggers(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        monkeypatch.setattr(sync_index, "SKILLS_DIR", tmp_path)
        _write_skill(tmp_path, "my-skill", "desc", triggers=["deploy"])
        entries = sync_index.scan_skills()
        assert entries[0]["triggers"] == ["deploy"]

    def test_source_from_frontmatter(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        monkeypatch.setattr(sync_index, "SKILLS_DIR", tmp_path)
        monkeypatch.setattr(sync_index, "LOCK_PATH", tmp_path / "nope.json")
        _write_skill(
            tmp_path,
            "my-skill",
            "desc",
            source={"repo": "https://github.com/org/repo"},
        )
        entries = sync_index.scan_skills()
        assert entries[0]["source"]["repo"] == "https://github.com/org/repo"


class TestLoadIndex:
    def test_missing_file(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        monkeypatch.setattr(sync_index, "INDEX_PATH", tmp_path / "nope.yaml")
        assert sync_index.load_index() == []

    def test_valid_index(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        idx = tmp_path / "SKILL_INDEX.yaml"
        data = {"skills": [{"name": "test", "description": "desc"}]}
        idx.write_text(yaml.dump(data))
        monkeypatch.setattr(sync_index, "INDEX_PATH", idx)
        result = sync_index.load_index()
        assert len(result) == 1

    def test_non_dict_yaml(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        idx = tmp_path / "SKILL_INDEX.yaml"
        idx.write_text("- item1\n- item2\n")
        monkeypatch.setattr(sync_index, "INDEX_PATH", idx)
        assert sync_index.load_index() == []


class TestWriteIndex:
    def test_writes_header(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        idx = tmp_path / "SKILL_INDEX.yaml"
        monkeypatch.setattr(sync_index, "INDEX_PATH", idx)
        sync_index.write_index([{"name": "test", "description": "desc"}])
        content = idx.read_text()
        assert "auto-generated" in content
        assert "test" in content

    def test_roundtrip(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        idx = tmp_path / "SKILL_INDEX.yaml"
        monkeypatch.setattr(sync_index, "INDEX_PATH", idx)
        entries = [{"name": "alpha", "description": "Alpha skill"}, {"name": "beta", "description": "Beta skill"}]
        sync_index.write_index(entries)
        loaded = sync_index.load_index()
        assert len(loaded) == 2
        assert loaded[0]["name"] == "alpha"


class TestValidateAllSkills:
    def test_valid_skill(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        d = _write_skill(tmp_path, "my-skill", "desc")
        results = sync_index.validate_all_skills([d])
        assert results["my-skill"] == []

    def test_invalid_skill(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        d = tmp_path / "bad-skill"
        d.mkdir()
        (d / "SKILL.md").write_text("No frontmatter")
        results = sync_index.validate_all_skills([d])
        assert len(results["bad-skill"]) > 0
