from __future__ import annotations

from pathlib import Path
from typing import Any

from .utils import load_json, print_output, repo_root

REQUIRED_FIELDS = [
    "id",
    "name",
    "trigger",
    "route",
    "steps",
    "required_artifacts",
    "outputs",
    "validation",
    "stop_conditions",
    "related_cards",
    "version",
]


def workflows_root(root: Path | None = None) -> Path:
    return repo_root(root) / ".vcp" / "workflows"


def workflow_paths(root: Path | None = None) -> list[Path]:
    return sorted(workflows_root(root).glob("*.json"))


def load_workflows(root: Path | None = None) -> list[dict[str, Any]]:
    root = repo_root(root)
    items = []
    for path in workflow_paths(root):
        data = load_json(path)
        data["__path"] = str(path.relative_to(root))
        items.append(data)
    return items


def list_workflows(json_mode: bool = False) -> int:
    items = load_workflows()
    payload = {"total": len(items), "items": [{"id": item["id"], "name": item["name"], "route": item["route"], "path": item["__path"]} for item in items]}
    print_output(payload, json_mode)
    return 0


def show_workflow(workflow_id: str, json_mode: bool = False) -> int:
    matches = [item for item in load_workflows() if item.get("id") == workflow_id]
    if not matches:
        print(f"Workflow not found: {workflow_id}")
        return 1
    print_output(matches[0], json_mode)
    return 0


def validate_workflows(json_mode: bool = False) -> int:
    root = repo_root()
    errors: list[str] = []
    workflows = load_workflows(root)
    for workflow in workflows:
        for field in REQUIRED_FIELDS:
            if field not in workflow:
                errors.append(f"Missing field {field} in {workflow['__path']}")
        if workflow.get("version") != "v0.5.9":
            errors.append(f"Workflow version mismatch in {workflow['__path']}: {workflow.get('version')}")
        steps = workflow.get("steps", [])
        if not isinstance(steps, list) or not steps:
            errors.append(f"steps must be a non-empty list in {workflow['__path']}")
        else:
            for step in steps:
                for field in ["id", "name", "action"]:
                    if field not in step:
                        errors.append(f"Step missing {field} in {workflow['__path']}")
        for rel in workflow.get("required_artifacts", []):
            if rel.endswith((".md", ".json", ".py", ".txt")) and not (root / rel).exists():
                errors.append(f"Missing workflow artifact from {workflow['__path']}: {rel}")
    payload = {"ok": not errors, "count": len(workflows), "errors": errors}
    if json_mode:
        print_output(payload, True)
    else:
        if errors:
            for error in errors:
                print(error)
        else:
            print(f"Workflow validation passed. ({len(workflows)} workflows)")
    return 0 if not errors else 1


def search_workflows(query: str, json_mode: bool = False) -> int:
    needle = query.lower()
    matches = []
    for workflow in load_workflows():
        haystack = "\n".join([
            workflow.get("id", ""),
            workflow.get("name", ""),
            workflow.get("trigger", ""),
            workflow.get("route", ""),
            *[step.get("name", "") for step in workflow.get("steps", [])],
        ]).lower()
        if needle in haystack:
            matches.append({"id": workflow["id"], "name": workflow["name"], "route": workflow["route"], "path": workflow["__path"]})
    print_output({"query": query, "count": len(matches), "results": matches}, json_mode)
    return 0
