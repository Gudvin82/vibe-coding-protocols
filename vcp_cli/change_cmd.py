from __future__ import annotations

from pathlib import Path
from typing import Any

from .utils import load_json, print_output, repo_root, repo_version

ALLOWED_STAGES = {"new", "existing", "mvp-to-launch", "release-prep", "hotfix"}
ALLOWED_RISKS = {"low", "medium", "high", "critical"}


def example_path(root: Path | None = None) -> Path:
    return repo_root(root) / ".vcp" / "change-intent.example.json"


def example_payload(root: Path | None = None) -> dict[str, Any]:
    return load_json(example_path(root))


def validate_change_intent_data(data: dict[str, Any], root: Path | None = None) -> list[str]:
    root = repo_root(root)
    problems: list[str] = []
    required = {
        "version", "change_id", "intent", "reason", "project_stage", "affected_surfaces",
        "risk_level", "requires_human_approval", "recommended_vcp_path", "required_checks",
        "rollback_plan", "not_in_scope",
    }
    missing = sorted(required - set(data.keys()))
    for key in missing:
        problems.append(f"missing field: {key}")
    if data.get("version") != repo_version(root):
        problems.append("change-intent version does not match VERSION")
    if data.get("project_stage") not in ALLOWED_STAGES:
        problems.append("project_stage must be new, existing, mvp-to-launch, release-prep, or hotfix")
    if data.get("risk_level") not in ALLOWED_RISKS:
        problems.append("risk_level must be low, medium, high, or critical")
    if not isinstance(data.get("requires_human_approval"), bool):
        problems.append("requires_human_approval must be boolean")
    for key in ("affected_surfaces", "required_checks", "not_in_scope"):
        if not isinstance(data.get(key), list) or not data.get(key):
            problems.append(f"{key} must be a non-empty list")
    for key in ("change_id", "intent", "reason", "recommended_vcp_path", "rollback_plan"):
        if not isinstance(data.get(key), str) or not data.get(key).strip():
            problems.append(f"{key} must be a non-empty string")
    return problems


def run_intent(json_mode: bool = False) -> int:
    print_output(example_payload(), json_mode)
    return 0


def run_validate(path: str, json_mode: bool = False) -> int:
    data = load_json(Path(path))
    problems = validate_change_intent_data(data)
    payload = {"ok": not problems, "errors": problems, "path": path}
    print_output(payload, json_mode)
    return 0 if not problems else 1
