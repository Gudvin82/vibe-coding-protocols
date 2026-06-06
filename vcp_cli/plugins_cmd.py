from __future__ import annotations

from pathlib import Path
from typing import Any

from .utils import load_json, print_output, repo_root

REQUIRED_FIELDS = {
    "id",
    "name",
    "version",
    "vcp_compatibility",
    "capabilities",
    "execution",
    "trust_level",
    "entrypoint",
    "outputs",
    "network",
    "writes",
}

ALLOWED_EXECUTION = {"read-only", "write-capable"}
PLUGIN_EXAMPLES_DIR = Path("examples/plugins")


def _plugin_dir(root: Path) -> Path:
    return root / PLUGIN_EXAMPLES_DIR


def list_payload(root: Path | None = None) -> dict[str, Any]:
    root = repo_root(root)
    items: list[dict[str, Any]] = []
    for path in sorted(_plugin_dir(root).glob("*.plugin.json")):
        data = load_json(path)
        items.append({
            "path": str(path.relative_to(root)),
            "id": data.get("id"),
            "name": data.get("name"),
            "execution": data.get("execution"),
            "trust_level": data.get("trust_level"),
            "network": data.get("network"),
            "writes": data.get("writes"),
        })
    return {
        "ok": True,
        "kind": "local-plugin-scaffold",
        "note": "This is a local metadata scaffold, not a plugin marketplace or execution engine.",
        "items": items,
    }


def validate_payload(plugin_path: str, root: Path | None = None) -> dict[str, Any]:
    root = repo_root(root)
    path = Path(plugin_path)
    if not path.is_absolute():
        path = (Path.cwd() / path).resolve()
    data = load_json(path)
    missing = sorted(REQUIRED_FIELDS - set(data.keys()))
    warnings: list[str] = []
    errors: list[str] = []
    if missing:
        errors.append(f"Missing required fields: {', '.join(missing)}")
    if data.get("execution") not in ALLOWED_EXECUTION:
        errors.append("execution must be read-only or write-capable")
    capabilities = data.get("capabilities")
    if not isinstance(capabilities, list) or not capabilities:
        errors.append("capabilities must be a non-empty list")
    outputs = data.get("outputs")
    if not isinstance(outputs, list) or not outputs:
        errors.append("outputs must be a non-empty list")
    if data.get("network") is True:
        warnings.append("Plugin requests network access. Treat it as higher-risk and review manually.")
    if data.get("writes") is True:
        warnings.append("Plugin declares write capability. Do not auto-execute it.")
    if data.get("execution") == "write-capable":
        warnings.append("Write-capable plugins are scaffold-only in v0.8.8 and must remain opt-in.")
    return {
        "ok": not errors,
        "path": str(path),
        "plugin": data,
        "errors": errors,
        "warnings": warnings,
        "execution_occurs": False,
        "note": "Validation inspects metadata only. It never executes plugin code.",
    }


def run_list(json_mode: bool = False) -> int:
    print_output(list_payload(), json_mode)
    return 0


def run_validate(plugin_path: str, json_mode: bool = False) -> int:
    payload = validate_payload(plugin_path)
    print_output(payload, json_mode)
    return 0 if payload["ok"] else 1
