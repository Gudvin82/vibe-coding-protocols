from __future__ import annotations

from pathlib import Path
from typing import Any

from .utils import load_json, print_output, repo_root

REQUIRED_FIELDS = [
    "id",
    "name",
    "default_spec_depth",
    "recommended_routes",
    "required_gates",
    "notes",
]
VALID_SPEC_DEPTHS = {"no-spec", "spec-lite", "full-spec", "governed-spec"}


def presets_root(root: Path | None = None) -> Path:
    return repo_root(root) / ".vcp" / "presets"


def preset_paths(root: Path | None = None) -> list[Path]:
    return sorted(presets_root(root).glob("*.json"))


def load_presets(root: Path | None = None) -> list[dict[str, Any]]:
    root = repo_root(root)
    items = []
    for path in preset_paths(root):
        data = load_json(path)
        data["__path"] = str(path.relative_to(root))
        items.append(data)
    return items


def list_presets(json_mode: bool = False) -> int:
    items = load_presets()
    payload = {
        "total": len(items),
        "items": [
            {
                "id": item["id"],
                "name": item["name"],
                "default_spec_depth": item["default_spec_depth"],
                "path": item["__path"],
            }
            for item in items
        ],
    }
    print_output(payload, json_mode)
    return 0


def show_preset(preset_id: str, json_mode: bool = False) -> int:
    matches = [item for item in load_presets() if item.get("id") == preset_id]
    if not matches:
        print(f"Preset not found: {preset_id}")
        return 1
    print_output(matches[0], json_mode)
    return 0


def validate_presets(json_mode: bool = False) -> int:
    root = repo_root()
    errors: list[str] = []
    items = load_presets(root)
    for item in items:
        for field in REQUIRED_FIELDS:
            if field not in item:
                errors.append(f"Missing field {field} in {item['__path']}")
        if item.get("default_spec_depth") not in VALID_SPEC_DEPTHS:
            errors.append(f"Invalid default_spec_depth in {item['__path']}: {item.get('default_spec_depth')}")
        for key in ["recommended_routes", "required_gates"]:
            if key in item and not isinstance(item[key], list):
                errors.append(f"{key} must be a list in {item['__path']}")
        for key in ["public_growth_options", "risk_defaults", "terminology_overrides"]:
            if key in item and not isinstance(item[key], (list, dict)):
                errors.append(f"{key} must be a list or object in {item['__path']}")
    payload = {"ok": not errors, "count": len(items), "errors": errors}
    if json_mode:
        print_output(payload, True)
    else:
        if errors:
            for error in errors:
                print(error)
        else:
            print(f"Preset validation passed. ({len(items)} presets)")
    return 0 if not errors else 1
