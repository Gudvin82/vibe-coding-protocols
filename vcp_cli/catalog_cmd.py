from __future__ import annotations

from pathlib import Path
from typing import Any

from .utils import load_json, print_output, repo_root

ALLOWED_STATUSES = {"shipped", "optional", "experimental", "roadmap-only", "not-shipped"}


def catalog_path(root: Path | None = None) -> Path:
    return repo_root(root) / ".vcp" / "control-catalog.json"


def _load_catalog(root: Path | None = None) -> dict[str, Any]:
    path = catalog_path(root)
    data = load_json(path)
    if not isinstance(data, dict) or not isinstance(data.get("entries"), list):
        raise ValueError("Control catalog must be a JSON object with an entries list.")
    return data


def list_payload(root: Path | None = None) -> dict[str, Any]:
    data = _load_catalog(root)
    entries = data.get("entries", [])
    return {
        "ok": True,
        "version": data.get("version"),
        "count": len(entries),
        "statuses": data.get("statuses", []),
        "entries": entries,
        "note": "Read-only local catalog. No install, mutation, or network execution occurs.",
    }


def explain_payload(entry_id: str, root: Path | None = None) -> dict[str, Any]:
    data = _load_catalog(root)
    entries = data.get("entries", [])
    for entry in entries:
        if entry.get("id") == entry_id:
            return {
                "ok": True,
                "version": data.get("version"),
                "entry": entry,
                "note": "Control catalog entries describe local VCP surfaces and boundaries only.",
            }
    raise ValueError(f"Unknown control catalog id: {entry_id}")


def validate(root: Path | None = None) -> list[str]:
    root = repo_root(root)
    data = _load_catalog(root)
    problems: list[str] = []
    statuses = set(data.get("statuses", []))
    if statuses != ALLOWED_STATUSES:
        problems.append("control-catalog statuses must be shipped, optional, experimental, roadmap-only, and not-shipped")
    seen: set[str] = set()
    for entry in data.get("entries", []):
        entry_id = entry.get("id")
        if not entry_id or not isinstance(entry_id, str):
            problems.append("catalog entry missing id")
            continue
        if entry_id in seen:
            problems.append(f"duplicate catalog entry id: {entry_id}")
        seen.add(entry_id)
        if entry.get("status") not in ALLOWED_STATUSES:
            problems.append(f"{entry_id} has invalid status {entry.get('status')!r}")
        for key in ("title", "category", "summary", "when_to_use", "not_for", "docs", "docs_ru"):
            if not entry.get(key):
                problems.append(f"{entry_id} missing {key}")
        for rel in entry.get("primary_files", []):
            if not (root / rel).exists():
                problems.append(f"{entry_id} missing primary file: {rel}")
        for rel in (entry.get("docs"), entry.get("docs_ru")):
            if rel and not (root / rel).exists():
                problems.append(f"{entry_id} missing doc surface: {rel}")
    return problems


def run_list(json_mode: bool = False) -> int:
    try:
        payload = list_payload()
    except Exception as exc:  # noqa: BLE001
        print_output({"ok": False, "error": str(exc)}, json_mode)
        return 1
    print_output(payload, json_mode)
    return 0


def run_explain(entry_id: str, json_mode: bool = False) -> int:
    try:
        payload = explain_payload(entry_id)
    except Exception as exc:  # noqa: BLE001
        print_output({"ok": False, "id": entry_id, "error": str(exc)}, json_mode)
        return 1
    print_output(payload, json_mode)
    return 0
