from __future__ import annotations

from pathlib import Path
from typing import Any
import shutil

from .utils import load_json, print_output, repo_root

ALLOWED_STATUSES = {"shipped", "optional", "manual", "roadmap-only"}
REQUIRED_IDS = {"claude", "codex", "cursor", "copilot", "github-actions"}
REQUIRED_FIELDS = {
    "id",
    "title",
    "target",
    "status",
    "summary",
    "files",
    "default_output",
    "safe_write_rules",
    "commands",
    "docs",
    "docs_ru",
    "not_official_plugin",
    "roadmap_boundary",
}


def registry_path(root: Path | None = None) -> Path:
    return repo_root(root) / ".vcp" / "agent-kits.json"


def _load_registry(root: Path | None = None) -> dict[str, Any]:
    path = registry_path(root)
    if not path.exists():
        raise FileNotFoundError(path)
    data = load_json(path)
    if not isinstance(data, dict) or not isinstance(data.get("items"), list):
        raise ValueError("Agent kit registry must be a JSON object with an items list.")
    return data


def validate_registry(root: Path | None = None) -> list[str]:
    root = repo_root(root)
    data = _load_registry(root)
    problems: list[str] = []
    seen: set[str] = set()
    for item in data.get("items", []):
        missing = sorted(REQUIRED_FIELDS - set(item))
        if missing:
            problems.append(f"kit {item.get('id', '?')} missing fields: {', '.join(missing)}")
        kit_id = item.get("id")
        if kit_id in seen:
            problems.append(f"duplicate kit id: {kit_id}")
        seen.add(kit_id)
        if item.get("status") not in ALLOWED_STATUSES:
            problems.append(f"kit {kit_id} has invalid status {item.get('status')!r}")
        for file_item in item.get("files", []):
            source = file_item.get("source")
            if not source or not (root / source).exists():
                problems.append(f"kit {kit_id} missing source file: {source}")
            if "recommended_destination" not in file_item:
                problems.append(f"kit {kit_id} file missing recommended_destination: {source}")
        for rel in (item.get("docs"), item.get("docs_ru")):
            if not rel or not (root / rel).exists():
                problems.append(f"kit {kit_id} missing docs surface: {rel}")
        kit_dir = root / "templates" / "agent-kits" / str(kit_id)
        if not kit_dir.exists():
            problems.append(f"kit {kit_id} directory missing: {kit_dir.relative_to(root)}")
        elif not (kit_dir / "README.md").exists():
            problems.append(f"kit {kit_id} missing README.md")
    missing_ids = sorted(REQUIRED_IDS - seen)
    if missing_ids:
        problems.append("missing required kit ids: " + ", ".join(missing_ids))
    return problems


def _find_item(target: str, root: Path | None = None) -> tuple[dict[str, Any], Path]:
    root = repo_root(root)
    data = _load_registry(root)
    for item in data.get("items", []):
        if item.get("id") == target:
            return item, root
    raise KeyError(target)


def _kit_dir(root: Path, kit_id: str) -> Path:
    return root / "templates" / "agent-kits" / kit_id


def kit_payload(target: str, root: Path | None = None) -> dict[str, Any]:
    try:
        item, root = _find_item(target, root)
    except KeyError:
        return {"ok": False, "error": f"Unknown agent kit target: {target}", "available": sorted(REQUIRED_IDS)}
    return {
        "ok": True,
        "target": item["id"],
        "title": item["title"],
        "status": item["status"],
        "summary": item["summary"],
        "not_official_plugin": item["not_official_plugin"],
        "files": item["files"],
        "default_output": item["default_output"],
        "safe_write_rules": item["safe_write_rules"],
        "commands": item["commands"],
        "docs": item["docs"],
        "docs_ru": item["docs_ru"],
        "roadmap_boundary": item["roadmap_boundary"],
        "kit_source_dir": str(_kit_dir(root, item["id"]))
    }


def _iter_kit_files(base: Path) -> list[Path]:
    return sorted(path for path in base.rglob("*") if path.is_file())


def run_kit(
    target: str,
    output: str | None = None,
    confirm: bool = False,
    force: bool = False,
    dry_run: bool = False,
    json_mode: bool = False,
) -> int:
    payload = kit_payload(target)
    if not payload.get("ok"):
        print_output(payload, json_mode)
        return 1
    if not output:
        print_output(payload, json_mode)
        return 0
    if not confirm:
        print_output({
            "ok": False,
            "target": target,
            "error": "Write mode requires --confirm.",
            "safe_write_rules": payload["safe_write_rules"],
        }, json_mode)
        return 1

    root = repo_root()
    source_dir = Path(payload["kit_source_dir"])
    target_dir = Path(output)
    if not target_dir.is_absolute():
        target_dir = (Path.cwd() / target_dir).resolve()

    planned: list[dict[str, Any]] = []
    existing: list[str] = []
    for source_path in _iter_kit_files(source_dir):
        rel = source_path.relative_to(source_dir)
        destination = target_dir / rel
        planned.append({
            "source": str(source_path.relative_to(root)),
            "destination": str(destination),
            "relative_path": str(rel),
        })
        if destination.exists():
            existing.append(str(destination))

    if existing and not force:
        print_output({
            "ok": False,
            "target": target,
            "error": "Refusing to overwrite existing files without --force.",
            "existing_files": existing,
            "safe_write_rules": payload["safe_write_rules"],
        }, json_mode)
        return 1

    result = dict(payload)
    result["output"] = str(target_dir)
    result["planned_writes"] = planned
    result["dry_run"] = dry_run

    if dry_run:
        print_output(result, json_mode)
        return 0

    target_dir.mkdir(parents=True, exist_ok=True)
    for source_path in _iter_kit_files(source_dir):
        rel = source_path.relative_to(source_dir)
        destination = target_dir / rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, destination)

    result["written"] = [item["destination"] for item in planned]
    print_output(result, json_mode)
    return 0
