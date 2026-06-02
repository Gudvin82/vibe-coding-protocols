from __future__ import annotations

from pathlib import Path

from .utils import load_json, manifest_path, print_output, repo_root


def scenario_paths() -> list[Path]:
    return sorted((repo_root() / "benchmarks/ai-adoption/scenarios").glob("*.json"))


def list_scenarios() -> int:
    for path in scenario_paths():
        print(path.stem)
    return 0


def _manifest_ids(group: str) -> set[str]:
    items = load_json(manifest_path(repo_root(), group)).get("items", [])
    return {item.get("id") for item in items}


def run(scenario: str | None = None, json_mode: bool = False) -> int:
    root = repo_root()
    route_ids = _manifest_ids("protocols")
    pack_ids = _manifest_ids("adoption-packs")
    selected = [p for p in scenario_paths() if scenario in {None, p.stem}]
    results = []
    errors = []
    for path in selected:
        data = load_json(path)
        scenario_errors = []
        expected_route = data.get("expected_route")
        expected_pack = data.get("expected_adoption_pack")
        if expected_route and expected_route not in route_ids:
            scenario_errors.append(f"Unknown route: {data.get('expected_route')}")
        if expected_pack and expected_pack not in pack_ids:
            scenario_errors.append(f"Unknown pack: {data.get('expected_adoption_pack')}")
        for rel in data.get("required_files_to_inspect", []):
            if not (root / rel).exists():
                scenario_errors.append(f"Missing required file: {rel}")
        results.append(
            {
                "scenario": data.get("scenario_id"),
                "ok": not scenario_errors,
                "errors": scenario_errors,
                "expected_warnings": data.get("expected_warnings", []),
            }
        )
        errors.extend(scenario_errors)
    payload = {"ok": not errors, "results": results}
    if json_mode:
        print_output(payload, True)
    else:
        for result in results:
            print(f"{result['scenario']}: {'PASS' if result['ok'] else 'FAIL'}")
            for error in result["errors"]:
                print(f"- {error}")
    return 0 if not errors else 1
