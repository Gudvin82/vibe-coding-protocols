from __future__ import annotations

from pathlib import Path
from typing import Any

from .utils import load_json, print_output, repo_root, repo_version


def example_path(root: Path | None = None) -> Path:
    return repo_root(root) / ".vcp" / "project-control-charter.example.json"


def validate_charter_data(data: dict[str, Any], root: Path | None = None) -> list[str]:
    root = repo_root(root)
    problems: list[str] = []
    required = {
        "version", "project_name", "source_of_truth", "agent_permissions", "human_approval_required",
        "required_checks", "release_gates", "docs_and_proof_rules", "risk_levels",
        "rollback_expectations", "roadmap_boundaries",
    }
    missing = sorted(required - set(data.keys()))
    for key in missing:
        problems.append(f"missing field: {key}")
    if data.get("version") != repo_version(root):
        problems.append("project-control-charter version does not match VERSION")
    for key in ("source_of_truth", "human_approval_required", "required_checks", "release_gates", "docs_and_proof_rules", "risk_levels", "roadmap_boundaries"):
        if not isinstance(data.get(key), list) or not data.get(key):
            problems.append(f"{key} must be a non-empty list")
    if not isinstance(data.get("agent_permissions"), dict) or not data.get("agent_permissions"):
        problems.append("agent_permissions must be a non-empty object")
    for key in ("project_name", "rollback_expectations"):
        if not isinstance(data.get(key), str) or not data.get(key).strip():
            problems.append(f"{key} must be a non-empty string")
    return problems


def run_validate(path: str, json_mode: bool = False) -> int:
    data = load_json(Path(path))
    problems = validate_charter_data(data)
    payload = {"ok": not problems, "errors": problems, "path": path}
    print_output(payload, json_mode)
    return 0 if not problems else 1
