from __future__ import annotations

from pathlib import Path

from .utils import print_output, repo_root, runtime_path_exists

CHECKS = {
    "fail_closed_doc": "docs/safety/fail-closed.md",
    "plugin_safety_doc": "docs/plugins/plugin-safety.md",
    "dashboard_doc": "docs/dashboard.md",
    "adoption_packs_doc": "docs/adoption-packs.md",
    "pr_gate_doc": "docs/pr-gate.md",
}


def payload(root: Path | None = None) -> dict[str, object]:
    root = repo_root(root)
    checks = {key: runtime_path_exists(root, rel) for key, rel in CHECKS.items()}
    status = "pass" if all(checks.values()) else "warn"
    return {
        "ok": True,
        "status": status,
        "checks": checks,
        "default_policy": {
            "read_only": "allowed",
            "report_only": "allowed",
            "local_write": "explicit output path required",
            "project_write": "human confirmation required",
            "execute": "explicit interactive/command gate required",
            "network": "disabled unless explicitly documented",
            "credentialed": "not supported by default",
            "destructive": "disabled by default",
        },
        "note": "This is a static local safety summary, not a sandbox or security certification.",
    }


def run_check(json_mode: bool = False) -> int:
    print_output(payload(), json_mode)
    return 0
