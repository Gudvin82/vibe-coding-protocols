from __future__ import annotations

import platform
import sys
from pathlib import Path

from .fast_checks import (
    current_shell,
    full_bash_checks_available,
    has_bash,
    has_git,
    powershell_first_supported,
    run_fast_checks,
    summarize_results,
    validate_required_files,
    windows_path_mode,
)
from .utils import git_status_short, manifest_paths, print_output, repo_root, repo_version

CORE_FILES = [
    "AI_INTAKE.md",
    "START_HERE.md",
    "docs/protocol-index.md",
    "docs/adoption-packs.md",
    "protocols/review/post-task-code-review.md",
    "protocols/integrations/third-party-api-intake.md",
    "templates/THIRD_PARTY_REGISTRY.md",
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
    for _, path in manifest_paths(root).items():
        checks.append({"item": path.name, "status": "PASS" if path.exists() else "FAIL"})

    required_files_result = validate_required_files(root)
    checks.append({"item": "required-files", "status": required_files_result["status"]})

    warnings = [
        "Public root AGENTS.md is intentionally visible and must stay sanitized.",
        "Public root PROJECT_MAP.md is intentionally visible and must stay sanitized.",
        "Historical API_KEY marker warning may still appear in git history checks.",
        "Historical SECRET marker warning may still appear in git history checks.",
    ]

    fast_results = run_fast_checks(root)
    ok, passed, failed, skipped = summarize_results(fast_results)

    payload = {
        "repository_package": repo_version(root),
        "worktree_clean": git_status_short(root) == "",
        "os": platform.system(),
        "python_version": sys.version.split()[0],
        "shell_environment": current_shell(),
        "bash_available": has_bash(),
        "git_available": has_git(),
        "repo_root_detected": str(root),
        "running_from_repo_root": root == Path.cwd().resolve(),
        "windows_path_mode": windows_path_mode(),
        "powershell_first_mode_supported": powershell_first_supported(root),
        "full_bash_checks_available": full_bash_checks_available(root),
        "third_party_registry_template_exists": (root / "templates/THIRD_PARTY_REGISTRY.md").exists(),
        "third_party_api_intake_protocol_exists": (root / "protocols/integrations/third-party-api-intake.md").exists(),
        "checks": checks,
        "fast_check_summary": {
            "ok": ok,
            "passed": passed,
            "failed": failed,
            "skipped": skipped,
        },
        "warnings": warnings,
        "manifests_present": all(path.exists() for path in manifest_paths(root).values()),
    }
    if json_mode:
        print_output(payload, True)
    else:
        print(f"Repository package: {payload['repository_package']}")
        print(f"Worktree clean: {'yes' if payload['worktree_clean'] else 'no'}")
        print(f"OS: {payload['os']}")
        print(f"Python: {payload['python_version']}")
        print(f"Shell: {payload['shell_environment']}")
        print(f"Bash available: {'yes' if payload['bash_available'] else 'no'}")
        print(f"Git available: {'yes' if payload['git_available'] else 'no'}")
        print(f"Windows path mode: {'yes' if payload['windows_path_mode'] else 'no'}")
        print(f"PowerShell-first mode supported: {'yes' if payload['powershell_first_mode_supported'] else 'no'}")
        print(f"Full Bash checks available: {'yes' if payload['full_bash_checks_available'] else 'no'}")
        print(f"THIRD_PARTY_REGISTRY template: {'yes' if payload['third_party_registry_template_exists'] else 'no'}")
        print(f"Third-party API intake protocol: {'yes' if payload['third_party_api_intake_protocol_exists'] else 'no'}")
        for item in checks:
            print(f"{item['status']}: {item['item']}")
        if warnings:
            print("Warnings:")
            for warning in warnings:
                print(f"- {warning}")
    return 0 if all(item['status'] == 'PASS' for item in checks) else 1
