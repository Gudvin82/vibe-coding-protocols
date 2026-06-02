from __future__ import annotations

from pathlib import Path

from .utils import print_output, repo_root

REQUIRED_SECTIONS = [
    "# Project Backlog",
    "## Rules",
    "## TODO",
    "## DOING",
    "## DONE",
    "## ARCHIVED / NOT TAKEN",
]

REQUIRED_TABLE_MARKERS = [
    "| ID | Priority | Type | Title | Route | Source | Created | Updated | Notes |",
    "| ID | Priority | Type | Title | Route | Source | Started | Updated | Validation |",
    "| ID | Priority | Type | Title | Route | Source | Done | Validation | Review |",
    "| ID | Priority | Type | Title | Source | Reason | Archived |",
]


def backlog_path(root: Path | None = None) -> Path:
    base = repo_root(root)
    return base / "PROJECT_BACKLOG.md"


TEMPLATE_PATH = Path("templates/PROJECT_BACKLOG.md")


def validate(json_mode: bool = False) -> int:
    root = repo_root()
    path = backlog_path(root)
    errors: list[str] = []
    if not path.exists():
        errors.append("PROJECT_BACKLOG.md is missing.")
        payload = {"ok": False, "path": str(path), "errors": errors}
        print_output(payload, json_mode)
        return 1

    text = path.read_text(encoding="utf-8")
    for marker in REQUIRED_SECTIONS:
        if marker not in text:
            errors.append(f"Missing section: {marker}")
    for marker in REQUIRED_TABLE_MARKERS:
        if marker not in text:
            errors.append(f"Missing table header: {marker}")

    payload = {
        "ok": not errors,
        "path": str(path),
        "errors": errors,
        "required_sections": REQUIRED_SECTIONS,
    }
    print_output(payload, json_mode)
    return 0 if not errors else 1


def template() -> int:
    root = repo_root()
    path = root / TEMPLATE_PATH
    print(path.read_text(encoding="utf-8").rstrip())
    return 0
