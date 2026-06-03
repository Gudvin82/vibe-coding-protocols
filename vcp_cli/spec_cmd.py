from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any

from .utils import print_output, repo_root

TEMPLATES = {
    "prd": ("templates/specs/PRD.md", "PRD.md"),
    "feature": ("templates/specs/FEATURE_SPEC.md", "FEATURE_SPEC.md"),
    "tasks": ("templates/specs/TASKS.md", "TASKS.md"),
}

SPEC_FILES = {
    "PRD.md": ["# Product Requirements Document", "## Problem statement", "## Validation plan"],
    "FEATURE_SPEC.md": ["# Feature Spec", "## User flow", "## Validation plan"],
    "ACCEPTANCE_CRITERIA.md": ["# Acceptance Criteria", "## Acceptance criteria"],
    "TASKS.md": ["# Tasks", "## Task breakdown", "## Validation tasks"],
    "SPEC_REVIEW.md": ["# Spec Review", "## Review scope", "## Decision"],
    "SPEC_CHANGELOG.md": ["# Spec Changelog", "## Change log"],
}


def _target_path(root: Path, default_name: str, output: str | None) -> Path:
    return (root / output).resolve() if output else (root / default_name)


def _backup_if_needed(path: Path) -> str | None:
    if not path.exists():
        return None
    stamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    backup = path.with_name(f"{path.name}.bak-{stamp}")
    backup.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
    return str(backup)


def template(kind: str, write: bool = False, output: str | None = None, json_mode: bool = False) -> int:
    root = repo_root()
    template_rel, default_name = TEMPLATES[kind]
    source = root / template_rel
    text = source.read_text(encoding="utf-8")
    if not write:
        if json_mode:
            print_output({"kind": kind, "template": template_rel, "write": False, "default_output": default_name, "content": text}, True)
        else:
            print(text.rstrip())
        return 0
    target = _target_path(root, default_name, output)
    backup = _backup_if_needed(target)
    target.write_text(text, encoding="utf-8")
    payload = {
        "kind": kind,
        "template": template_rel,
        "write": True,
        "target": str(target.relative_to(root)),
        "backup": backup,
    }
    print_output(payload, json_mode)
    return 0


def _inspect_spec_file(root: Path, rel: str) -> dict[str, Any]:
    path = root / rel
    if not path.exists():
        return {"file": rel, "status": "MISSING", "missing_sections": [], "evidence": "file not present"}
    text = path.read_text(encoding="utf-8")
    missing = [section for section in SPEC_FILES[rel] if section not in text]
    return {
        "file": rel,
        "status": "OK" if not missing else "WARN",
        "missing_sections": missing,
        "evidence": "present",
    }


def validate(json_mode: bool = False) -> int:
    root = repo_root()
    results = [_inspect_spec_file(root, rel) for rel in SPEC_FILES]
    ok = all(item["status"] in {"OK", "MISSING"} for item in results)
    payload = {
        "ok": ok,
        "spec_files": results,
        "templates_present": {kind: (root / template_rel).exists() for kind, (template_rel, _) in TEMPLATES.items()},
    }
    if json_mode:
        print_output(payload, True)
    else:
        for item in results:
            print(f"{item['file']}: {item['status']}")
            for section in item["missing_sections"]:
                print(f"- missing section: {section}")
    return 0 if ok else 1


def review(json_mode: bool = False) -> int:
    root = repo_root()
    items = [_inspect_spec_file(root, rel) for rel in SPEC_FILES]
    gaps = []
    for item in items:
        if item["status"] == "WARN":
            gaps.append(f"{item['file']} missing: {', '.join(item['missing_sections'])}")
        if item["status"] == "MISSING" and item["file"] in {"PRD.md", "FEATURE_SPEC.md", "ACCEPTANCE_CRITERIA.md", "TASKS.md"}:
            gaps.append(f"{item['file']} is missing for non-trivial spec-first work.")
    payload = {
        "ok": not gaps,
        "decision": "approved" if not gaps else "blocked pending spec gaps",
        "gaps": gaps,
        "next_action": "Clarify missing spec sections before implementation." if gaps else "Spec lane is ready for implementation planning.",
    }
    print_output(payload, json_mode)
    return 0 if not gaps else 1


def summary(json_mode: bool = False) -> int:
    root = repo_root()
    results = [_inspect_spec_file(root, rel) for rel in SPEC_FILES]
    present = [item["file"] for item in results if item["status"] != "MISSING"]
    payload = {
        "ok": True,
        "present": present,
        "missing": [item["file"] for item in results if item["status"] == "MISSING"],
        "warnings": [item for item in results if item["status"] == "WARN"],
        "recommended_flow": ["PRD.md", "FEATURE_SPEC.md", "ACCEPTANCE_CRITERIA.md", "TASKS.md", "SPEC_REVIEW.md"],
    }
    print_output(payload, json_mode)
    return 0
