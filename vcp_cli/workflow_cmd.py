from __future__ import annotations

from pathlib import Path
from typing import Any

from .utils import load_json, print_output, runtime_root, repo_version

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
    return runtime_root(root) / ".vcp" / "workflows"


def workflow_paths(root: Path | None = None) -> list[Path]:
    return sorted(workflows_root(root).glob("*.json"))


def load_workflows(root: Path | None = None) -> list[dict[str, Any]]:
    root = runtime_root(root)
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
    root = runtime_root()
    errors: list[str] = []
    workflows = load_workflows(root)
    current_version = repo_version(root)
    for workflow in workflows:
        for field in REQUIRED_FIELDS:
            if field not in workflow:
                errors.append(f"Missing field {field} in {workflow['__path']}")
        if workflow.get("version") != current_version:
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


def workflow_plan_payload(workflow_id: str | None = None, root: Path | None = None) -> dict[str, Any]:
    root = runtime_root(root)
    workflows = load_workflows(root)
    selected = workflows
    if workflow_id:
        selected = [item for item in workflows if item.get("id") == workflow_id]
        if not selected:
            return {
                "ok": False,
                "requested_workflow": workflow_id,
                "error": f"Workflow not found: {workflow_id}",
                "note": "Workflow JSON files are planning artifacts, not an execution engine.",
            }

    plans = []
    for workflow in selected:
        plans.append(
            {
                "id": workflow["id"],
                "name": workflow["name"],
                "route": workflow["route"],
                "trigger": workflow["trigger"],
                "steps": workflow.get("steps", []),
                "validation": workflow.get("validation", []),
                "stop_conditions": workflow.get("stop_conditions", []),
            }
        )

    return {
        "ok": True,
        "requested_workflow": workflow_id,
        "plans": plans,
        "note": "Workflow JSON files are machine-readable planning/governance artifacts. They do not execute external actions.",
    }


SAFE_WORKFLOW_ACTIONS = {"route", "review", "plan", "artifact"}


def workflow_run_payload(
    workflow_id: str,
    *,
    interactive: bool,
    dry_run: bool = False,
    root: Path | None = None,
) -> dict[str, Any]:
    payload = workflow_plan_payload(workflow_id, root=root)
    if not payload.get("ok"):
        return payload
    if not interactive:
        return {
            "ok": False,
            "requested_workflow": workflow_id,
            "error": "workflow run requires --interactive. Use workflow plan for the default non-executing view.",
            "note": "Workflow JSON remains planning/governance metadata, not a hidden automation engine.",
        }

    plan = payload["plans"][0]
    step_results = []
    for step in plan.get("steps", []):
        action = step.get("action", "unknown")
        command = step.get("command")
        step_results.append(
            {
                "id": step.get("id"),
                "name": step.get("name"),
                "action": action,
                "safe_action": action in SAFE_WORKFLOW_ACTIONS,
                "command": command,
                "executed": False,
                "status": "planned" if action in SAFE_WORKFLOW_ACTIONS else "blocked",
                "reason": (
                    "Interactive workflow run in v0.8.0 is a safe preview surface and does not execute external actions."
                    if action in SAFE_WORKFLOW_ACTIONS
                    else "Action is outside the safe preview allowlist."
                ),
            }
        )

    return {
        "ok": True,
        "requested_workflow": workflow_id,
        "interactive": True,
        "dry_run": dry_run,
        "plan": plan,
        "steps": step_results,
        "note": "workflow run is an interactive safe runner/planner. In v0.8.0 it previews only safe local VCP steps and never deploys, publishes, modifies files, or accesses secrets.",
    }


def plan_workflow(workflow_id: str | None = None, json_mode: bool = False) -> int:
    payload = workflow_plan_payload(workflow_id)
    if json_mode:
        print_output(payload, True)
        return 0 if payload.get("ok") else 1
    if not payload.get("ok"):
        print(payload["error"])
        return 1
    for plan in payload["plans"]:
        print(f"{plan['name']} ({plan['id']})")
        print(f"Route: {plan['route']}")
        print(f"Trigger: {plan['trigger']}")
        print("Steps:")
        for step in plan["steps"]:
            print(f"- {step.get('name')} [{step.get('action')}]")
        print("Validation:")
        for item in plan["validation"]:
            print(f"- {item}")
        print()
    print(payload["note"])
    return 0


def run_workflow(workflow_id: str, *, interactive: bool, dry_run: bool = False, json_mode: bool = False) -> int:
    payload = workflow_run_payload(workflow_id, interactive=interactive, dry_run=dry_run)
    if json_mode:
        print_output(payload, True)
        return 0 if payload.get("ok") else 1
    if not payload.get("ok"):
        print(payload["error"])
        return 1
    print(f"{payload['plan']['name']} ({payload['plan']['id']})")
    print(f"Interactive: {'yes' if payload['interactive'] else 'no'}")
    print(f"Dry run: {'yes' if payload['dry_run'] else 'no'}")
    print("Steps:")
    for step in payload["steps"]:
        print(f"- {step['name']} [{step['action']}] -> {step['status']}")
        if step.get("command"):
            print(f"  Command: {step['command']}")
        print(f"  Reason: {step['reason']}")
    print(payload["note"])
    return 0
