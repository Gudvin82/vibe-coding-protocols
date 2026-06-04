from __future__ import annotations

from pathlib import Path
from typing import Any

from . import backlog as backlog_cmd
from . import release_check as release_check_cmd
from .utils import load_json, manifest_paths, methodology_version, print_output, repo_root, repo_version, runtime_path_exists


def _count_items(path: Path) -> int:
    data = load_json(path)
    return len(data.get("items", [])) if isinstance(data, dict) else 0


def _backlog_summary(root: Path) -> dict[str, Any]:
    path = root / "PROJECT_BACKLOG.md"
    if not path.exists():
        return {"present": False, "status_counts": {}, "priority_counts": {}, "total": 0}
    doc = backlog_cmd.load_document(root)
    status_counts: dict[str, int] = {}
    priority_counts: dict[str, int] = {}
    for item in doc.items:
        status_counts[item.status] = status_counts.get(item.status, 0) + 1
        priority_counts[item.priority] = priority_counts.get(item.priority, 0) + 1
    return {
        "present": True,
        "status_counts": status_counts,
        "priority_counts": priority_counts,
        "total": len(doc.items),
    }


def _integration_status_counts(root: Path) -> dict[str, int]:
    path = root / ".vcp" / "integrations.json"
    if not path.exists():
        return {}
    data = load_json(path)
    counts: dict[str, int] = {}
    for item in data.get("items", []):
        status = item.get("status", "unknown")
        counts[status] = counts.get(status, 0) + 1
    return counts


def payload(root: Path | None = None) -> dict[str, Any]:
    root = repo_root(root)
    manifests = manifest_paths(root)
    cards_dir = root / ".vcp" / "cards"
    release = release_check_cmd.payload(root)
    return {
        "repository_package_version": repo_version(root),
        "methodology_version": methodology_version(root),
        "cards_count": sum(1 for path in cards_dir.rglob("*.json") if path.is_file()),
        "benchmark_scenario_count": _count_items(manifests["benchmarks"]),
        "report_template_count": _count_items(manifests["reports"]),
        "command_count": _count_items(manifests["commands"]),
        "release_readiness": {
            "status": release["status"],
            "missing": release["missing"],
        },
        "audit_backlog": _backlog_summary(root),
        "integration_status_counts": _integration_status_counts(root),
        "signals": {
            "dashboard_doc_present": runtime_path_exists(root, "docs/dashboard.md"),
            "metrics_board_doc_present": runtime_path_exists(root, "docs/metrics-board.md"),
            "audit_backlog_visualization_doc_present": runtime_path_exists(root, "docs/audit-backlog-visualization.md"),
            "integration_registry_present": runtime_path_exists(root, ".vcp/integrations.json"),
        },
        "limits": [
            "Metrics are local readiness signals, not objective truth.",
            "No production readiness guarantee.",
            "No SEO/GEO ranking or AI citation guarantee.",
        ],
    }


def run_board(json_mode: bool = False) -> int:
    data = payload()
    if json_mode:
        print_output(data, True)
    else:
        print("Metrics Board")
        print(f"Repository package: {data['repository_package_version']}")
        print(f"Methodology version: {data['methodology_version']}")
        print(f"Cards: {data['cards_count']}")
        print(f"Benchmarks: {data['benchmark_scenario_count']}")
        print(f"Commands: {data['command_count']}")
        print(f"Release readiness: {data['release_readiness']['status']}")
    return 0
