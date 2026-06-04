from __future__ import annotations

from pathlib import Path

from .utils import print_output, repo_root


def run(json_mode: bool = False) -> int:
    root = repo_root()
    checks = {
        "version": (root / "VERSION").exists(),
        "readme": (root / "README.md").exists(),
        "readme_ru": (root / "README_ru.md").exists(),
        "versioning": (root / "docs/versioning.md").exists(),
        "release_notes": any((root / "docs").glob("release-v*.md")),
        "public_version_check": (root / "scripts/check-public-version-surfaces.py").exists(),
        "readme_parity_check": (root / "scripts/check-readme-parity.py").exists(),
        "pr_gate_doc": (root / "docs/pr-gate.md").exists(),
        "release_readiness_doc": (root / "docs/release-readiness.md").exists(),
        "architecture_drift_doc": (root / "docs/architecture-drift.md").exists(),
        "project_backlog": (root / "PROJECT_BACKLOG.md").exists(),
        "project_map": (root / "PROJECT_MAP.md").exists(),
    }
    missing = [name for name, present in checks.items() if not present]
    status = "pass"
    if missing:
        status = "block" if len(missing) >= 3 else "warn"
    payload = {
        "ok": status != "block",
        "status": status,
        "checked": checks,
        "missing": missing,
        "required_validation": [
            "python3 scripts/check-public-version-surfaces.py",
            "python3 scripts/check-readme-parity.py",
            "bash scripts/check-version-consistency.sh",
            "python3 -m vcp_cli cards validate",
            "python3 -m vcp_cli index validate",
        ],
        "next_action": (
            "Release readiness surface is present. Run full validation before tagging."
            if status == "pass"
            else "Restore the missing release-control files before tagging."
        ),
        "note": "Release Check is a lightweight repository surface check. It does not replace full validation or clean-clone verification.",
    }
    print_output(payload, json_mode)
    return 0 if status != "block" else 1
