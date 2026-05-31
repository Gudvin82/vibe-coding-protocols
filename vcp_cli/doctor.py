from __future__ import annotations

from .utils import git_status_short, load_json, manifest_paths, print_output, repo_root, repo_version, run_command

CORE_FILES = [
    "AI_INTAKE.md",
    "START_HERE.md",
    "docs/protocol-index.md",
    "docs/adoption-packs.md",
    "protocols/review/post-task-code-review.md",
    "docs/public-site-readiness.md",
    "scripts/check-newlines.py",
    "scripts/validate-links.sh",
    "scripts/check-toolkit.sh",
    ".github/workflows/vibe-check.yml",
]


def run(json_mode: bool = False) -> int:
    root = repo_root()
    checks = []
    for rel in CORE_FILES:
        checks.append({"item": rel, "status": "PASS" if (root / rel).exists() else "FAIL"})
    for name, path in manifest_paths(root).items():
        checks.append({"item": path.name, "status": "PASS" if path.exists() else "FAIL"})
    version_ok = run_command(["bash", "scripts/check-version-consistency.sh"], root).returncode == 0
    checks.append({"item": "version-consistency", "status": "PASS" if version_ok else "FAIL"})
    warnings = [
        "Public root AGENTS.md is intentionally visible and must stay sanitized.",
        "Public root PROJECT_MAP.md is intentionally visible and must stay sanitized.",
        "Historical API_KEY marker warning may still appear in git history checks.",
        "Historical SECRET marker warning may still appear in git history checks.",
    ]
    payload = {
        "repository_package": repo_version(root),
        "worktree_clean": git_status_short(root) == "",
        "checks": checks,
        "warnings": warnings,
        "manifests_present": all(path.exists() for path in manifest_paths(root).values()),
    }
    if json_mode:
        print_output(payload, True)
    else:
        print(f"Repository package: {payload['repository_package']}")
        print(f"Worktree clean: {'yes' if payload['worktree_clean'] else 'no'}")
        for item in checks:
            print(f"{item['status']}: {item['item']}")
        if warnings:
            print("Warnings:")
            for warning in warnings:
                print(f"- {warning}")
    return 0 if all(item['status'] == 'PASS' for item in checks) else 1
