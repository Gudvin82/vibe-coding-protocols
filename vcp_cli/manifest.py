from __future__ import annotations

from pathlib import Path
from typing import Any

from .utils import dump_json, load_json, manifest_paths, print_output, repo_root

GROUP_KEYS = {
    "routes": "routes",
    "packs": "packs",
    "commands": "commands",
    "reports": "reports",
    "benchmarks": "benchmarks",
}


def show_manifest(name: str | None = None) -> dict[str, Any]:
    root = repo_root()
    paths = manifest_paths(root)
    if name:
        return {name: load_json(paths[name])}
    return {key: load_json(path) for key, path in paths.items()}


def validate_manifests(json_mode: bool = False) -> int:
    root = repo_root()
    paths = manifest_paths(root)
    errors: list[str] = []
    details: dict[str, Any] = {}
    protocol_ids: set[str] = set()
    pack_ids: set[str] = set()
    command_ids: set[str] = set()
    report_ids: set[str] = set()

    try:
        protocol_ids = {item.get("id") for item in load_json(paths["protocols"]).get("items", [])}
        pack_ids = {item.get("id") for item in load_json(paths["adoption-packs"]).get("items", [])}
        command_ids = {item.get("id") for item in load_json(paths["commands"]).get("items", [])}
        report_ids = {item.get("id") for item in load_json(paths["reports"]).get("items", [])}
    except Exception as exc:  # noqa: BLE001
        errors.append(f"Manifest pre-load failed: {exc}")

    for key, path in paths.items():
        try:
            data = load_json(path)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"Invalid JSON in {path.name}: {exc}")
            continue
        details[key] = {"path": str(path), "status": "ok"}
        for item in data.get("items", []):
            file_path = item.get("file")
            if file_path and not (root / file_path).exists():
                errors.append(f"Missing file for {key}:{item.get('id')}: {file_path}")
            for linked in item.get("related_docs", []):
                if not (root / linked).exists():
                    errors.append(f"Missing related doc for {key}:{item.get('id')}: {linked}")
            for template in item.get("report_template", []) if isinstance(item.get("report_template"), list) else []:
                if not (root / template).exists():
                    errors.append(f"Missing report template for {key}:{item.get('id')}: {template}")
            if key == "adoption-packs":
                for field in ["recommended_files", "optional_files", "merge_only_files"]:
                    for rel in item.get(field, []):
                        if rel.endswith((".md", ".json", ".sh", ".py", ".txt")) and not (root / rel).exists():
                            errors.append(f"Missing pack path for {item.get('id')}:{field}: {rel}")
            if key == "benchmarks":
                scenario_file = item.get("scenario_file")
                if scenario_file and not (root / scenario_file).exists():
                    errors.append(f"Missing benchmark scenario for {item.get('id')}: {scenario_file}")
                if item.get("expected_route") not in protocol_ids:
                    errors.append(f"Unknown expected route in benchmarks:{item.get('id')}: {item.get('expected_route')}")
                if item.get("expected_pack") not in pack_ids:
                    errors.append(f"Unknown expected pack in benchmarks:{item.get('id')}: {item.get('expected_pack')}")
            if key == "commands" and item.get("id") not in command_ids:
                errors.append(f"Command manifest lost id for item in {path.name}")
            if key == "reports" and item.get("id") not in report_ids:
                errors.append(f"Report manifest lost id for item in {path.name}")
        for top_key in ["entrypoints", "core_docs", "validation_scripts", "safety_boundaries"]:
            for rel in data.get(top_key, []):
                if rel.endswith(('.md', '.json', '.sh', '.py', '.yml', '.yaml', '.txt')) and not (root / rel).exists():
                    errors.append(f"Missing manifest path in {path.name}: {rel}")
    payload = {
        "ok": not errors,
        "errors": errors,
        "manifests": details,
    }
    if json_mode:
        print_output(payload, True)
    else:
        if errors:
            for error in errors:
                print(error)
        else:
            print("Manifest validation passed.")
    return 0 if not errors else 1


def list_group(group: str) -> int:
    root = repo_root()
    lookup = {
        "routes": root / "protocols.manifest.json",
        "packs": root / "adoption-packs.manifest.json",
        "commands": root / "commands.manifest.json",
        "reports": root / "reports.manifest.json",
        "benchmarks": root / "benchmarks.manifest.json",
    }
    data = load_json(lookup[group])
    print(dump_json(data.get("items", [])))
    return 0
