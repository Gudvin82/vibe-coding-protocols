from __future__ import annotations

from pathlib import Path

from .utils import print_output, repo_root


def payload(root: Path | None = None) -> dict[str, object]:
    root = repo_root(root)
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
        "distribution_doc": (root / "docs/distribution.md").exists(),
        "adoption_tiers_doc": (root / "docs/adoption-tiers.md").exists(),
        "proof_pack_doc": (root / "docs/proof-pack.md").exists(),
        "project_backlog": (root / "PROJECT_BACKLOG.md").exists(),
        "project_map": (root / "PROJECT_MAP.md").exists(),
    }
    missing = [name for name, present in checks.items() if not present]
    status = "pass"
    if missing:
        status = "block" if len(missing) >= 3 else "warn"
    return {
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


def run(json_mode: bool = False) -> int:
    data = payload()
    print_output(data, json_mode)
    return 0 if data["status"] != "block" else 1
