from __future__ import annotations

from typing import Any

from .utils import dump_json, load_json, manifest_path, manifest_paths, print_output, repo_root

REQUIRED_API_INTAKE_PROTOCOL_ID = "third-party-api-intake"
REQUIRED_API_INTAKE_COMMAND_ID = "third-party-api-intake"
REQUIRED_API_INTAKE_REPORT_ID = "third-party-api-intake-report"
REQUIRED_API_INTAKE_PACK_ID = "third-party-api"
REQUIRED_API_INTAKE_BENCHMARK_ID = "third-party-api-intake"


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
    benchmark_ids: set[str] = set()

    try:
        protocol_ids = {item.get("id") for item in load_json(paths["protocols"]).get("items", [])}
        pack_ids = {item.get("id") for item in load_json(paths["adoption-packs"]).get("items", [])}
        command_ids = {item.get("id") for item in load_json(paths["commands"]).get("items", [])}
        report_ids = {item.get("id") for item in load_json(paths["reports"]).get("items", [])}
        benchmark_ids = {item.get("id") for item in load_json(paths["benchmarks"]).get("items", [])}
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
            report_template = item.get("report_template")
            if isinstance(report_template, list):
                for template in report_template:
                    if not (root / template).exists():
                        errors.append(f"Missing report template for {key}:{item.get('id')}: {template}")
            elif isinstance(report_template, str) and report_template and not (root / report_template).exists():
                errors.append(f"Missing report template for {key}:{item.get('id')}: {report_template}")
            if key == "adoption-packs":
                for field in ["recommended_files", "optional_files", "merge_only_files"]:
                    for rel in item.get(field, []):
                        if rel.endswith((".md", ".json", ".sh", ".py", ".txt", ".ps1", ".cmd", ".yml", ".yaml")) and not (root / rel).exists():
                            errors.append(f"Missing pack path for {item.get('id')}:{field}: {rel}")
            if key == "benchmarks":
                scenario_file = item.get("scenario_file")
                if scenario_file and not (root / scenario_file).exists():
                    errors.append(f"Missing benchmark scenario for {item.get('id')}: {scenario_file}")
                if item.get("expected_route") not in protocol_ids:
                    errors.append(f"Unknown expected route in benchmarks:{item.get('id')}: {item.get('expected_route')}")
                if item.get("expected_pack") not in pack_ids:
                    errors.append(f"Unknown expected pack in benchmarks:{item.get('id')}: {item.get('expected_pack')}")
        for top_key in ["entrypoints", "core_docs", "validation_scripts", "safety_boundaries", "route_docs", "known_limitations"]:
            for rel in data.get(top_key, []):
                if rel.endswith((".md", ".json", ".sh", ".py", ".yml", ".yaml", ".txt", ".ps1", ".cmd")) and not (root / rel).exists():
                    errors.append(f"Missing manifest path in {path.name}: {rel}")

    if REQUIRED_API_INTAKE_PROTOCOL_ID not in protocol_ids:
        errors.append("Missing required protocol manifest entry: third-party-api-intake")
    if REQUIRED_API_INTAKE_COMMAND_ID not in command_ids:
        errors.append("Missing required command manifest entry: third-party-api-intake")
    if REQUIRED_API_INTAKE_REPORT_ID not in report_ids:
        errors.append("Missing required report manifest entry: third-party-api-intake-report")
    if REQUIRED_API_INTAKE_PACK_ID not in pack_ids:
        errors.append("Missing required adoption pack manifest entry: third-party-api")
    if REQUIRED_API_INTAKE_BENCHMARK_ID not in benchmark_ids:
        errors.append("Missing required benchmark manifest entry: third-party-api-intake")

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
        "routes": manifest_path(root, "protocols"),
        "packs": manifest_path(root, "adoption-packs"),
        "commands": manifest_path(root, "commands"),
        "reports": manifest_path(root, "reports"),
        "benchmarks": manifest_path(root, "benchmarks"),
    }
    data = load_json(lookup[group])
    print(dump_json(data.get("items", [])))
    return 0
