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
from .utils import git_status_short, manifest_paths, print_output, repo_root, repo_version, relative_to_root, runtime_path_exists

CORE_FILES = [
    "AI_EVALUATION_GUIDE.md",
    "AGENTS.md",
    "AI_INTAKE.md",
    "START_HERE.md",
    "llms.txt",
    "llms-full.txt",
    "ai.txt",
    "CITATION.cff",
    "ADOPTERS.md",
    "docs/protocol-index.md",
    "docs/adoption-packs.md",
    "docs/adoption-packs.quickstart.md",
    "docs/scoring.md",
    "docs/install.md",
    "docs/glossary.md",
    ".vcp/index.json",
    ".vcp/catalog.json",
    ".vcp/cards/README.md",
    ".vcp/presets/README.md",
    ".vcp/workflows/README.md",
    ".vcp/diagnostics/README.md",
    "schemas/vcp-card.schema.json",
    "schemas/vcp-preset.schema.json",
    "schemas/vcp-workflow.schema.json",
    "schemas/vcp-event.schema.json",
    "docs/adaptive-spec-depth.md",
    "docs/spec-escape-hatch.md",
    "docs/question-engine.md",
    "docs/spec-retrofit.md",
    "docs/spec-freshness.md",
    "docs/packs-and-presets.md",
    "docs/integrations/spec-kit-bridge.md",
    "docs/progressive-disclosure.md",
    "docs/vcp-cards.md",
    "docs/vcp-mappings.md",
    "docs/platforms/README.md",
    "docs/platforms/claude-code.md",
    "docs/platforms/codex-cli.md",
    "docs/platforms/cursor.md",
    "docs/platforms/windsurf.md",
    "docs/platforms/github-copilot.md",
    "docs/platforms/gemini-cli.md",
    "docs/platforms/jetbrains-junie.md",
    "docs/geo-ai-visibility.md",
    "docs/page-templates.md",
    "docs/faq.md",
    "docs/comparison.md",
    "docs/anti-patterns.md",
    "docs/quickstart-walkthrough.md",
    "docs/demo-script.md",
    "docs/workflows.md",
    "docs/diagnostics.md",
    "docs/catalog.md",
    "docs/event-schema.md",
    "docs/npm-publishing-checklist.md",
    "docs/public-proof-roadmap.md",
    "docs/project-backlog.md",
    "docs/production-observability.md",
    "docs/automation-guidance.md",
    "docs/npm.md",
    "docs/init.md",
    "PROJECT_BACKLOG.md",
    "protocols/review/post-task-code-review.md",
    "protocols/integrations/third-party-api-intake.md",
    "protocols/operations/production-error-capture.md",
    "protocols/operations/daily-error-triage.md",
    "protocols/public-growth/public-growth-playbook.md",
    "protocols/public-growth/seo-geo-ai-visibility.md",
    "protocols/spec-driven/README.md",
    "protocols/spec-driven/adaptive-spec-depth.md",
    "protocols/spec-driven/product-brief-to-prd.md",
    "protocols/spec-driven/feature-spec.md",
    "protocols/spec-driven/question-engine.md",
    "protocols/spec-driven/spec-escape-hatch.md",
    "protocols/spec-driven/spec-freshness.md",
    "protocols/spec-driven/spec-retrofit.md",
    "protocols/spec-driven/spec-review.md",
    "protocols/spec-driven/spec-to-tasks.md",
    "protocols/spec-driven/spec-change-control.md",
    "templates/THIRD_PARTY_REGISTRY.md",
    "templates/PROJECT_BACKLOG.md",
    "templates/specs/PRD.md",
    "templates/specs/FEATURE_SPEC.md",
    "templates/specs/ACCEPTANCE_CRITERIA.md",
    "templates/specs/OBSERVED_SPEC.md",
    "templates/specs/SPEC_GAPS.md",
    "templates/specs/TASKS.md",
    "templates/specs/SPEC_REVIEW.md",
    "templates/specs/SPEC_CHANGELOG.md",
    "templates/reports/spec-depth-decision-report.md",
    "templates/reports/spec-freshness-report.md",
    "templates/reports/spec-questions-report.md",
    "templates/reports/spec-retrofit-report.md",
    "templates/reports/spec-skip-check-report.md",
    "templates/reports/spec-to-backlog-report.md",
    "templates/reports/error-inbox-entry.md",
    "templates/reports/diagnostic-report.md",
    "templates/reports/vcp-event-entry.md",
    "templates/public-growth/public-growth-checklist.md",
    "docs/public-site-readiness.md",
    "case-studies/sanitized/vcp-retrofit-public-growth/README.md",
    "scripts/check-newlines.py",
    "scripts/validate-links.sh",
    "scripts/check-toolkit.sh",
    ".github/workflows/vibe-check.yml",
]


def runtime_error_inbox_gitignored(root: Path) -> bool:
    gitignore = root / ".gitignore"
    if not gitignore.exists():
        return False
    text = gitignore.read_text(encoding="utf-8")
    return ".vcp/runtime/" in text and ".vcp/runtime/error-inbox/" in text


def runtime_backups_gitignored(root: Path) -> bool:
    gitignore = root / ".gitignore"
    if not gitignore.exists():
        return False
    text = gitignore.read_text(encoding="utf-8")
    return ".vcp/runtime/backups/" in text


def run(json_mode: bool = False) -> int:
    root = repo_root()
    checks = []
    for rel in CORE_FILES:
        checks.append({"item": rel, "status": "PASS" if runtime_path_exists(root, rel) else "FAIL"})
    for _, path in manifest_paths(root).items():
        checks.append({"item": relative_to_root(root, path), "status": "PASS" if path.exists() else "FAIL"})

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
        "third_party_registry_template_exists": runtime_path_exists(root, "templates/THIRD_PARTY_REGISTRY.md"),
        "third_party_api_intake_protocol_exists": runtime_path_exists(root, "protocols/integrations/third-party-api-intake.md"),
        "operations_protocol_exists": runtime_path_exists(root, "protocols/operations/production-error-capture.md"),
        "public_growth_protocol_exists": runtime_path_exists(root, "protocols/public-growth/public-growth-playbook.md"),
        "public_growth_templates_exist": runtime_path_exists(root, "templates/public-growth/public-growth-checklist.md"),
        "adaptive_spec_layer_exists": all(
            runtime_path_exists(root, rel)
            for rel in [
                "docs/adaptive-spec-depth.md",
                "docs/spec-escape-hatch.md",
                "docs/question-engine.md",
                "docs/spec-retrofit.md",
                "docs/spec-freshness.md",
                "protocols/spec-driven/adaptive-spec-depth.md",
                "protocols/spec-driven/spec-escape-hatch.md",
                "protocols/spec-driven/question-engine.md",
                "protocols/spec-driven/spec-retrofit.md",
                "protocols/spec-driven/spec-freshness.md",
            ]
        ),
        "preset_layer_exists": all(
            runtime_path_exists(root, rel)
            for rel in [
                "docs/packs-and-presets.md",
                ".vcp/presets/README.md",
                "schemas/vcp-preset.schema.json",
            ]
        ),
        "platform_doc_count": len(list((root / "docs" / "platforms").glob("*.md"))) if (root / "docs" / "platforms").exists() else 0,
        "platform_card_count": len(list((root / ".vcp" / "cards" / "platforms").glob("*.json"))) if (root / ".vcp" / "cards" / "platforms").exists() else 0,
        "project_backlog_exists": (root / "PROJECT_BACKLOG.md").exists(),
        "runtime_error_inbox_gitignored": runtime_error_inbox_gitignored(root),
        "runtime_backups_gitignored": runtime_backups_gitignored(root),
        "manifest_directory": str((root / ".vcp" / "manifests").resolve()),
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
        print(f"Manifest directory: {payload['manifest_directory']}")
        print(f"THIRD_PARTY_REGISTRY template: {'yes' if payload['third_party_registry_template_exists'] else 'no'}")
        print(f"Third-party API intake protocol: {'yes' if payload['third_party_api_intake_protocol_exists'] else 'no'}")
        print(f"Operations protocol: {'yes' if payload['operations_protocol_exists'] else 'no'}")
        print(f"Public growth protocol: {'yes' if payload['public_growth_protocol_exists'] else 'no'}")
        print(f"Public growth templates: {'yes' if payload['public_growth_templates_exist'] else 'no'}")
        print(f"Adaptive spec layer: {'yes' if payload['adaptive_spec_layer_exists'] else 'no'}")
        print(f"Preset layer: {'yes' if payload['preset_layer_exists'] else 'no'}")
        print(f"Platform docs: {payload['platform_doc_count']}")
        print(f"Platform cards: {payload['platform_card_count']}")
        print(f"PROJECT_BACKLOG.md: {'yes' if payload['project_backlog_exists'] else 'no'}")
        print(f"Runtime error inbox gitignored: {'yes' if payload['runtime_error_inbox_gitignored'] else 'no'}")
        print(f"Runtime backups gitignored: {'yes' if payload['runtime_backups_gitignored'] else 'no'}")
        for item in checks:
            print(f"{item['status']}: {item['item']}")
        if warnings:
            print("Warnings:")
            for warning in warnings:
                print(f"- {warning}")
    return 0 if all(item['status'] == 'PASS' for item in checks) else 1
