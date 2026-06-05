from __future__ import annotations

from pathlib import Path
from typing import Any

from .utils import dump_json, load_json, print_output, repo_root

REQUIRED_TOP_LEVEL = {
    "version": str,
    "project": dict,
    "decisions": list,
    "risks": list,
    "blockers": list,
    "proof_history": list,
}


def example_path(root: Path | None = None) -> Path:
    return repo_root(root) / ".vcp" / "project-memory.example.json"


def _validate_payload(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for field, expected in REQUIRED_TOP_LEVEL.items():
        if field not in data:
            errors.append(f"Missing field: {field}")
        elif not isinstance(data[field], expected):
            errors.append(f"Field {field} must be {expected.__name__}")
    project = data.get("project")
    if isinstance(project, dict):
        for field in ("name", "track", "methodology"):
            if field not in project:
                errors.append(f"project missing field: {field}")
    return errors


def validate_payload(path_str: str, root: Path | None = None) -> dict[str, Any]:
    root = repo_root(root)
    path = Path(path_str)
    if not path.is_absolute():
        path = (Path.cwd() / path).resolve()
    data = load_json(path)
    errors = _validate_payload(data)
    return {
        "ok": not errors,
        "path": str(path),
        "errors": errors,
        "project": data.get("project", {}),
        "decision_count": len(data.get("decisions", [])) if isinstance(data.get("decisions"), list) else None,
    }


def show_payload(path_str: str | None = None, root: Path | None = None) -> dict[str, Any]:
    path = Path(path_str).resolve() if path_str else example_path(root)
    data = load_json(path)
    return {
        "ok": True,
        "path": str(path),
        "memory": data,
        "note": "Project memory is explicit, local, file-based, and project-scoped. It is not personal assistant memory.",
    }


def init_payload(target: str, root: Path | None = None) -> dict[str, Any]:
    source = example_path(root)
    target_path = Path(target)
    if not target_path.is_absolute():
        target_path = (Path.cwd() / target_path).resolve()
    if target_path.exists():
        return {"ok": False, "error": "Target already exists.", "target": str(target_path)}
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return {"ok": True, "target": str(target_path), "source": str(source)}


def run_validate(path: str, json_mode: bool = False) -> int:
    payload = validate_payload(path)
    print_output(payload, json_mode)
    return 0 if payload["ok"] else 1


def run_show(path: str | None = None, json_mode: bool = False) -> int:
    print_output(show_payload(path), json_mode)
    return 0


def run_init(target: str, json_mode: bool = False) -> int:
    payload = init_payload(target)
    print_output(payload, json_mode)
    return 0 if payload["ok"] else 1
