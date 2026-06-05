from __future__ import annotations

from pathlib import Path
from typing import Any

from .utils import load_json, print_output, repo_root

REQUIRED_FIELDS = {
    "run_id": str,
    "version": str,
    "created_at": str,
    "command": str,
    "status": str,
    "steps": list,
    "artifacts": list,
    "warnings": list,
    "errors": list,
}


def runs_dir(root: Path | None = None) -> Path:
    return repo_root(root) / ".vcp" / "runs"


def validate_payload(path_str: str, root: Path | None = None) -> dict[str, Any]:
    path = Path(path_str)
    if not path.is_absolute():
        path = (Path.cwd() / path).resolve()
    data = load_json(path)
    errors: list[str] = []
    for field, expected in REQUIRED_FIELDS.items():
        if field not in data:
            errors.append(f"Missing field: {field}")
        elif not isinstance(data[field], expected):
            errors.append(f"Field {field} must be {expected.__name__}")
    return {
        "ok": not errors,
        "path": str(path),
        "errors": errors,
        "run_id": data.get("run_id"),
        "step_count": len(data.get("steps", [])) if isinstance(data.get("steps"), list) else None,
    }


def list_payload(root: Path | None = None) -> dict[str, Any]:
    base = runs_dir(root)
    items: list[dict[str, Any]] = []
    for path in sorted(base.glob("*.json")) if base.exists() else []:
        data = load_json(path)
        items.append({
            "run_id": data.get("run_id"),
            "status": data.get("status"),
            "path": str(path.relative_to(repo_root(root))),
            "command": data.get("command"),
        })
    return {"ok": True, "count": len(items), "items": items}


def show_payload(run_id: str, root: Path | None = None) -> dict[str, Any]:
    for path in sorted(runs_dir(root).glob("*.json")):
        data = load_json(path)
        if data.get("run_id") == run_id:
            return {"ok": True, "path": str(path), "run": data}
    return {"ok": False, "error": f"Run not found: {run_id}"}


def run_list(json_mode: bool = False) -> int:
    print_output(list_payload(), json_mode)
    return 0


def run_show(run_id: str, json_mode: bool = False) -> int:
    payload = show_payload(run_id)
    print_output(payload, json_mode)
    return 0 if payload["ok"] else 1


def run_validate(path: str, json_mode: bool = False) -> int:
    payload = validate_payload(path)
    print_output(payload, json_mode)
    return 0 if payload["ok"] else 1
