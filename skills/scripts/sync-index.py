#!/usr/bin/env python3
"""Skill index manager — sync, search, validate.

Reads SKILL.md frontmatter from all skill directories, merges provenance
from skills-lock.json, and generates SKILL_INDEX.yaml.

Commands:
    sync                           Regenerate SKILL_INDEX.yaml
    validate [skill...]            Validate skill(s) against spec + extensions
    search <query>                 Fuzzy search by task description
    lookup <name>                  Exact lookup by name
    tag <tag>                      Filter by tag
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

import yaml

SKILLS_DIR = Path(__file__).resolve().parent.parent
INDEX_PATH = SKILLS_DIR / "SKILL_INDEX.yaml"
LOCK_PATH = SKILLS_DIR / "skills-lock.json"
EXCLUDED_DIRS = {".templates", ".git", "scripts"}

SPEC_FIELDS = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
EXTENSION_FIELDS = {"triggers", "tags", "source"}
ALL_ALLOWED_FIELDS = SPEC_FIELDS | EXTENSION_FIELDS

MAX_NAME_LENGTH = 64
MAX_DESCRIPTION_LENGTH = 1024
MAX_COMPATIBILITY_LENGTH = 500


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------


def parse_frontmatter(skill_md: Path) -> dict | None:
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.find("---", 3)
    if end == -1:
        return None
    try:
        fm = yaml.safe_load(text[3:end])
    except yaml.YAMLError:
        return None
    return fm if isinstance(fm, dict) else None


def load_lock() -> dict:
    if not LOCK_PATH.exists():
        return {}
    try:
        data = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
        return data.get("skills", {}) if isinstance(data, dict) else {}
    except (json.JSONDecodeError, OSError):
        return {}


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------


def validate_name(name: str, dir_name: str | None = None) -> list[str]:
    errors: list[str] = []
    if not isinstance(name, str) or not name.strip():
        errors.append("Field 'name' must be a non-empty string")
        return errors

    normalized = unicodedata.normalize("NFKC", name.strip())
    if len(normalized) > MAX_NAME_LENGTH:
        errors.append(f"Name exceeds {MAX_NAME_LENGTH} chars ({len(normalized)})")
    if normalized != normalized.lower():
        errors.append(f"Name '{normalized}' must be lowercase")
    if normalized.startswith("-") or normalized.endswith("-"):
        errors.append("Name cannot start or end with a hyphen")
    if "--" in normalized:
        errors.append("Name cannot contain consecutive hyphens")
    if not all(c.isalnum() or c == "-" for c in normalized):
        errors.append(f"Name '{normalized}' contains invalid characters (only a-z, 0-9, hyphens)")

    if dir_name is not None:
        norm_dir = unicodedata.normalize("NFKC", dir_name)
        if norm_dir != normalized:
            errors.append(f"Directory '{dir_name}' must match name '{normalized}'")

    return errors


def validate_description(desc) -> list[str]:
    errors: list[str] = []
    if not isinstance(desc, str) or not desc.strip():
        errors.append("Field 'description' must be a non-empty string")
        return errors
    if len(desc) > MAX_DESCRIPTION_LENGTH:
        errors.append(f"Description exceeds {MAX_DESCRIPTION_LENGTH} chars ({len(desc)})")
    return errors


def validate_compatibility(val) -> list[str]:
    errors: list[str] = []
    if not isinstance(val, str):
        errors.append("Field 'compatibility' must be a string")
        return errors
    if len(val) > MAX_COMPATIBILITY_LENGTH:
        errors.append(f"Compatibility exceeds {MAX_COMPATIBILITY_LENGTH} chars ({len(val)})")
    return errors


def validate_metadata(val) -> list[str]:
    errors: list[str] = []
    if not isinstance(val, dict):
        errors.append("Field 'metadata' must be a mapping")
    else:
        for k, v in val.items():
            if not isinstance(v, str):
                errors.append(f"metadata.{k}: values must be strings, got {type(v).__name__}")
    return errors


def validate_source(val) -> list[str]:
    errors: list[str] = []
    if not isinstance(val, dict):
        errors.append("Field 'source' must be a mapping")
        return errors
    if "repo" not in val or not val["repo"]:
        errors.append("source.repo is required when source is present")
    errors.extend(
        f"source.{field} must be a string"
        for field in ("repo", "ref", "path", "commit", "fetched_at")
        if field in val and not isinstance(val[field], str)
    )
    return errors


def validate_triggers(val) -> list[str]:
    errors: list[str] = []
    if not isinstance(val, list):
        errors.append("Field 'triggers' must be a list of strings")
    elif len(val) == 0:
        errors.append("Field 'triggers' should not be empty if present")
    else:
        for i, item in enumerate(val):
            if not isinstance(item, str):
                errors.append(f"triggers[{i}]: must be a string, got {type(item).__name__}")
    return errors


def validate_tags(val) -> list[str]:
    errors: list[str] = []
    if not isinstance(val, list):
        errors.append("Field 'tags' must be a list of strings")
    elif len(val) == 0:
        errors.append("Field 'tags' should not be empty if present")
    else:
        for i, item in enumerate(val):
            if not isinstance(item, str):
                errors.append(f"tags[{i}]: must be a string, got {type(item).__name__}")
    return errors


def validate_skill(skill_dir: Path) -> list[str]:
    """Validate a single skill directory. Returns list of errors (empty = valid)."""
    errors: list[str] = []

    if not skill_dir.exists():
        return [f"Path does not exist: {skill_dir}"]
    if not skill_dir.is_dir():
        return [f"Not a directory: {skill_dir}"]

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        alt = skill_dir / "skill.md"
        if alt.exists():
            errors.append("SKILL.md should be uppercase (found skill.md)")
            skill_md = alt
        else:
            return ["Missing required file: SKILL.md"]

    fm = parse_frontmatter(skill_md)
    if fm is None:
        return ["SKILL.md has no valid YAML frontmatter"]

    # Unknown fields
    unknown = set(fm.keys()) - ALL_ALLOWED_FIELDS
    if unknown:
        errors.append(f"Unknown fields: {', '.join(sorted(unknown))}")

    # Required fields
    if "name" not in fm:
        errors.append("Missing required field: name")
    else:
        errors.extend(validate_name(fm["name"], skill_dir.name))

    if "description" not in fm:
        errors.append("Missing required field: description")
    else:
        errors.extend(validate_description(fm["description"]))

    # Optional spec fields
    if "compatibility" in fm:
        errors.extend(validate_compatibility(fm["compatibility"]))
    if "metadata" in fm:
        errors.extend(validate_metadata(fm["metadata"]))

    # Extension fields
    if "source" in fm:
        errors.extend(validate_source(fm["source"]))
    if "triggers" in fm:
        errors.extend(validate_triggers(fm["triggers"]))
    if "tags" in fm:
        errors.extend(validate_tags(fm["tags"]))

    # Body should exist (not just frontmatter)
    text = skill_md.read_text(encoding="utf-8")
    end = text.find("---", 3)
    if end != -1:
        body = text[end + 3 :].strip()
        if not body:
            errors.append("SKILL.md body is empty — skill should contain instructions")

    # File size sanity (spec recommends < 500 lines)
    line_count = text.count("\n") + 1
    if line_count > 500:
        errors.append(f"SKILL.md is {line_count} lines (spec recommends < 500)")

    return errors


def validate_all_skills(skill_dirs: list[Path] | None = None) -> dict[str, list[str]]:
    """Validate specified skills or all skills. Returns {name: [errors]}."""
    if skill_dirs is None:
        skill_dirs = [
            child
            for child in sorted(SKILLS_DIR.iterdir())
            if child.is_dir() and not child.name.startswith(".") and child.name not in EXCLUDED_DIRS
        ]
    results: dict[str, list[str]] = {}
    for d in skill_dirs:
        results[d.name] = validate_skill(d)
    return results


# ---------------------------------------------------------------------------
# Token estimation
# ---------------------------------------------------------------------------

_encoder = None


def _get_encoder():
    global _encoder
    if _encoder is None:
        import tiktoken

        _encoder = tiktoken.get_encoding("cl100k_base")
    return _encoder


def estimate_tokens(skill_md: Path) -> int:
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return len(_get_encoder().encode(text))
    end = text.find("---", 3)
    if end == -1:
        return len(_get_encoder().encode(text))
    body = text[end + 3 :].strip()
    if not body:
        return 0
    return len(_get_encoder().encode(body))


# ---------------------------------------------------------------------------
# Scanning & indexing
# ---------------------------------------------------------------------------


def scan_skills() -> list[dict]:
    lock_data = load_lock()
    entries: list[dict] = []
    for child in sorted(SKILLS_DIR.iterdir()):
        if not child.is_dir() or child.name.startswith(".") or child.name in EXCLUDED_DIRS:
            continue
        skill_md = child / "SKILL.md"
        if not skill_md.exists():
            print(f"WARNING: {child.name}/ has no SKILL.md, skipping", file=sys.stderr)
            continue
        fm = parse_frontmatter(skill_md)
        if fm is None:
            print(f"WARNING: {child.name}/SKILL.md invalid frontmatter, skipping", file=sys.stderr)
            continue
        if not fm.get("name"):
            print(f"WARNING: {child.name}/SKILL.md missing 'name', skipping", file=sys.stderr)
            continue
        if not fm.get("description"):
            print(f"WARNING: {child.name}/SKILL.md missing 'description', skipping", file=sys.stderr)
            continue
        if fm["name"] != child.name:
            print(f"WARNING: {child.name}/ name mismatch — '{fm['name']}' vs dir '{child.name}'", file=sys.stderr)

        entry: dict = {"name": fm["name"], "description": fm["description"], "path": child.name}
        for field in ("triggers", "tags"):
            if field in fm:
                entry[field] = fm[field]
        for field in ("license", "compatibility", "metadata", "allowed-tools"):
            if field in fm:
                entry[field] = fm[field]
        if isinstance(fm.get("metadata"), dict) and "version" in fm["metadata"]:
            entry["version"] = fm["metadata"]["version"]

        entry["token_estimate"] = estimate_tokens(skill_md)

        lock_entry = lock_data.get(fm["name"], {})
        if lock_entry:
            source: dict = {}
            for k in ("source", "ref", "source_type", "provider", "installed_at", "updated_at"):
                if k in lock_entry:
                    source[k] = lock_entry[k]
            if source:
                entry["source"] = source
        elif isinstance(fm.get("source"), dict) and fm["source"].get("repo"):
            entry["source"] = {
                "repo": fm["source"]["repo"],
                "ref": fm["source"].get("ref", ""),
                "path": fm["source"].get("path", ""),
            }

        entries.append(entry)
    return entries


def load_index() -> list[dict]:
    if not INDEX_PATH.exists():
        return []
    with open(INDEX_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data.get("skills", []) if isinstance(data, dict) else []


def write_index(entries: list[dict]) -> None:
    header = (
        "# Agent Skills Index (auto-generated)\n"
        "# Do not edit manually — run: python scripts/sync-index.py sync\n"
        "#     or via wrapper: ./scripts/skill-manager sync\n"
        "#\n"
        "# Source of truth: SKILL.md frontmatter + skills-lock.json\n"
    )
    doc = yaml.dump({"skills": entries}, default_flow_style=False, sort_keys=False, width=200, allow_unicode=True)
    INDEX_PATH.write_text(header + "\n" + doc + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# Search
# ---------------------------------------------------------------------------


def _tokenize(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def _search_score(query_tokens: set[str], entry: dict) -> float:
    score = 0.0
    name_tokens = _tokenize(entry.get("name", ""))
    desc_tokens = _tokenize(entry.get("description", ""))
    trigger_tokens = {t.lower() for t in entry.get("triggers", [])}
    tag_tokens = {t.lower() for t in entry.get("tags", [])}

    if query_tokens & name_tokens:
        score += len(query_tokens & name_tokens) * 3.0
    if query_tokens & trigger_tokens:
        score += len(query_tokens & trigger_tokens) * 2.0
    if query_tokens & tag_tokens:
        score += len(query_tokens & tag_tokens) * 2.0
    if query_tokens & desc_tokens:
        score += len(query_tokens & desc_tokens) * 1.0

    query_str = " ".join(query_tokens)
    for trigger in entry.get("triggers", []):
        t = trigger.lower()
        if query_str in t or t in query_str:
            score += 2.5
    for tag in entry.get("tags", []):
        t = tag.lower()
        if query_str in t or t in query_str:
            score += 1.5

    all_tokens = name_tokens | desc_tokens | trigger_tokens | tag_tokens
    coverage = len(query_tokens & all_tokens) / max(len(query_tokens), 1)
    score += coverage * 1.0
    return score


def search_skills(query: str, skills: list[dict], top: int = 10) -> list[dict]:
    query_tokens = _tokenize(query)
    if not query_tokens:
        return skills[:top]
    scored = [(entry, _search_score(query_tokens, entry)) for entry in skills]
    scored.sort(key=lambda x: x[1], reverse=True)
    return [{"score": round(s, 2), **entry} for entry, s in scored if s > 0][:top]


def find_by_name(name: str, skills: list[dict]) -> dict | None:
    name_lower = name.lower()
    for entry in skills:
        if entry["name"].lower() == name_lower:
            return entry
    return None


def filter_by_tag(tag: str, skills: list[dict]) -> list[dict]:
    tag_lower = tag.lower()
    return [e for e in skills if tag_lower in [t.lower() for t in e.get("tags", [])]]


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------


def cmd_sync(args: argparse.Namespace) -> None:
    entries = scan_skills()
    write_index(entries)
    if not getattr(args, "quiet", False):
        print(f"Indexed {len(entries)} skill(s) -> {INDEX_PATH.relative_to(SKILLS_DIR.parent)}")


def cmd_validate(args: argparse.Namespace) -> None:
    if args.skills:
        dirs = [SKILLS_DIR / s for s in args.skills]
        for d in dirs:
            if not d.exists():
                print(f"ERROR: {d} does not exist", file=sys.stderr)
                sys.exit(1)
    else:
        dirs = None

    results = validate_all_skills(dirs)
    total_errors = 0
    for name, errors in sorted(results.items()):
        if errors:
            total_errors += len(errors)
            print(f"FAIL {name}/")
            for e in errors:
                print(f"  - {e}")
        else:
            print(f"  OK {name}/")

    print()
    if total_errors:
        print(f"{total_errors} error(s) in {sum(1 for e in results.values() if e)} skill(s)")
        sys.exit(1)
    else:
        print(f"All {len(results)} skill(s) valid")


def cmd_search(args: argparse.Namespace) -> None:
    skills = load_index() or scan_skills()
    results = search_skills(args.query, skills, top=args.top)
    if not results:
        print("No matching skills found.")
        sys.exit(1)
    if args.format == "json":
        print(json.dumps(results, indent=2))
    else:
        for r in results:
            tags = ", ".join(r.get("tags", []))
            triggers = ", ".join(r.get("triggers", []))
            print(f"[{r['score']}] {r['name']}")
            print(f"    {r['description']}")
            if tags:
                print(f"    tags: {tags}")
            if triggers:
                print(f"    triggers: {triggers}")
            print()


def cmd_lookup(args: argparse.Namespace) -> None:
    skills = load_index() or scan_skills()
    result = find_by_name(args.name, skills)
    if not result:
        print(f"Skill '{args.name}' not found.")
        sys.exit(1)
    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        print(yaml.dump(result, default_flow_style=False, sort_keys=False))


def cmd_tag(args: argparse.Namespace) -> None:
    skills = load_index() or scan_skills()
    results = filter_by_tag(args.tag, skills)
    if not results:
        print(f"No skills found with tag '{args.tag}'.")
        sys.exit(1)
    if args.format == "json":
        print(json.dumps(results, indent=2))
    else:
        for r in results:
            print(f"  {r['name']}: {r['description']}")


def cmd_tokens(args: argparse.Namespace) -> None:
    skills = load_index() or scan_skills()
    if args.format == "json":
        print(json.dumps(skills, indent=2))
    else:
        total = 0
        rows = []
        for s in sorted(skills, key=lambda x: x.get("token_estimate", 0), reverse=True):
            est = s.get("token_estimate", 0)
            total += est
            rows.append((s["name"], est))
        for name, est in rows:
            print(f"  {name}: ~{est:,} tokens")
        print(f"\n  Total: ~{total:,} tokens across {len(skills)} skill(s)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Skill index manager")
    sub = parser.add_subparsers(dest="command")

    sync_p = sub.add_parser("sync", help="Regenerate SKILL_INDEX.yaml")
    sync_p.add_argument("--quiet", "-q", action="store_true")

    val_p = sub.add_parser("validate", help="Validate skill(s) against spec")
    val_p.add_argument("skills", nargs="*", help="Specific skill dirs to validate (default: all)")

    s = sub.add_parser("search", help="Fuzzy search by task description")
    s.add_argument("query", help="Task description or keywords")
    s.add_argument("--top", type=int, default=10)
    s.add_argument("--format", choices=["text", "json"], default="text")

    lookup_p = sub.add_parser("lookup", help="Exact lookup by name")
    lookup_p.add_argument("name", help="Skill name")
    lookup_p.add_argument("--format", choices=["text", "json"], default="text")

    t = sub.add_parser("tag", help="Filter by tag")
    t.add_argument("tag", help="Tag to filter by")
    t.add_argument("--format", choices=["text", "json"], default="text")

    tok = sub.add_parser("tokens", help="Show token estimates for all skills")
    tok.add_argument("--format", choices=["text", "json"], default="text")

    args = parser.parse_args()
    match args.command:
        case "sync" | None:
            cmd_sync(args)
        case "validate":
            cmd_validate(args)
        case "search":
            cmd_search(args)
        case "lookup":
            cmd_lookup(args)
        case "tag":
            cmd_tag(args)
        case "tokens":
            cmd_tokens(args)
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
