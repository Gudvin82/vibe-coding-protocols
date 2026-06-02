from __future__ import annotations

import contextlib
import io
import json
import os
import platform
import shutil
import sys
from pathlib import Path
from typing import Any

from . import benchmark as benchmark_cmd
from . import manifest as manifest_cmd
from .utils import (
    dump_json,
    load_json,
    manifest_path,
    manifest_paths,
    methodology_version,
    repo_root,
    repo_version,
    run_command,
)

VERSION_EXCLUSIONS = {
    "templates/README.md",
    "templates/LEGAL_CHECKLIST.md",
    "templates/PAYMENT_FISCALIZATION_CHECKLIST.md",
    "templates/PROMPTS.md",
    "templates/SCALABILITY_BACKLOG.md",
    "templates/SECURITY_SCANNER_REPORT.md",
}

FAST_REQUIRED_FILES = [
    "VERSION",
    "METHODOLOGY_VERSION",
    "README.md",
    "README_ru.md",
    "AI_EVALUATION_GUIDE.md",
    "START_HERE.md",
    "AI_INTAKE.md",
    "ROADMAP.md",
    ".vcp/README.md",
    "docs/cli.md",
    "docs/install.md",
    "docs/glossary.md",
    "docs/scoring.md",
    "docs/npm-publishing-checklist.md",
    "docs/public-proof-roadmap.md",
    "docs/windows.md",
    "docs/npm.md",
    "docs/init.md",
    "docs/geo-ai-visibility.md",
    "docs/page-templates.md",
    "docs/protocol-index.md",
    "docs/adoption-packs.md",
    "docs/adoption-packs.quickstart.md",
    "docs/project-backlog.md",
    "docs/release-v0.5.6.md",
    "docs/production-observability.md",
    "docs/automation-guidance.md",
    "docs/tooling-roadmap.md",
    "docs/known-limitations.md",
    "docs/measured-impact.md",
    "PROJECT_BACKLOG.md",
    "protocols/integrations/README.md",
    "protocols/integrations/third-party-api-intake.md",
    "protocols/public-growth/README.md",
    "protocols/public-growth/public-growth-playbook.md",
    "protocols/public-growth/seo-geo-ai-visibility.md",
    "protocols/public-growth/page-template-system.md",
    "protocols/public-growth/public-growth-risk-control.md",
    "protocols/operations/README.md",
    "protocols/operations/production-error-capture.md",
    "protocols/operations/daily-error-triage.md",
    "commands/third-party-api-intake.md",
    "commands/prod-log-monitor.md",
    "commands/daily-error-triage.md",
    "commands/backlog-update.md",
    "templates/prompts/third-party-api-intake.md",
    "templates/prompts/evaluate-vcp-repository.md",
    "templates/prompts/evaluate-vcp-for-my-repo.md",
    "templates/prompts/prod-log-monitor.md",
    "templates/prompts/daily-error-triage.md",
    "templates/prompts/backlog-update.md",
    "templates/prompts/public-growth-audit.md",
    "templates/reports/third-party-api-intake-report.md",
    "templates/reports/vcp-repository-evaluation-report.md",
    "templates/reports/production-error-capture-report.md",
    "templates/reports/daily-error-triage-report.md",
    "templates/reports/error-inbox-entry.md",
    "templates/reports/backlog-update-report.md",
    "templates/reports/public-growth-audit-report.md",
    "templates/reports/ai-visibility-monitoring-report.md",
    "templates/THIRD_PARTY_REGISTRY.md",
    "templates/PROJECT_BACKLOG.md",
    "templates/public-growth/page-brief.md",
    "templates/public-growth/service-page-template.md",
    "templates/public-growth/article-template.md",
    "templates/public-growth/case-study-template.md",
    "templates/public-growth/faq-page-template.md",
    "templates/public-growth/comparison-page-template.md",
    "templates/public-growth/alternatives-page-template.md",
    "templates/public-growth/homepage-template.md",
    "templates/public-growth/public-growth-checklist.md",
    "templates/public-growth/ai-visibility-queries.md",
    "templates/public-growth/schema/README.md",
    "templates/public-growth/schema/organization.jsonld",
    "templates/public-growth/schema/person.jsonld",
    "templates/public-growth/schema/service.jsonld",
    "templates/public-growth/schema/article.jsonld",
    "templates/public-growth/schema/faqpage.jsonld",
    "templates/public-growth/schema/breadcrumb-list.jsonld",
    "templates/public-growth/schema/software-application.jsonld",
    "templates/public-growth/schema/video-object.jsonld",
    "templates/runtime/error-inbox/.gitkeep",
    "examples/public-growth/README.md",
    "examples/public-growth/public-growth-audit.example.md",
    "examples/public-growth/ai-visibility-monitoring.example.md",
    "examples/public-growth/page-brief.example.md",
    "examples/public-growth/service-page.example.md",
    "examples/public-growth/faq-schema.example.md",
    "examples/backlog/README.md",
    "examples/backlog/add-idea.example.md",
    "examples/backlog/move-doing.example.md",
    "examples/backlog/done-with-review.example.md",
    "examples/backlog/archive-not-taken.example.md",
    "examples/backlog/architecture-impact.example.md",
    "examples/backlog/prod-error-to-backlog.example.md",
    "templates/examples/THIRD_PARTY_REGISTRY.filled.example.md",
    "scripts/check-newlines.py",
    "scripts/validate-links.sh",
    "scripts/check-version-consistency.sh",
    "bin/vcp",
    "bin/vcp.cmd",
    "bin/vcp.ps1",
    "bin/vcp-node.js",
    "package.json",
    "setup.py",
    "benchmarks/ai-adoption/scenarios/production-error-capture.json",
    "benchmarks/ai-adoption/scenarios/project-backlog-update.json",
    "benchmarks/ai-adoption/scenarios/backlog-add-idea.json",
    "benchmarks/ai-adoption/scenarios/backlog-move-done-with-review.json",
    "benchmarks/ai-adoption/scenarios/backlog-archive-not-taken.json",
    "benchmarks/ai-adoption/scenarios/backlog-architecture-impact.json",
    "benchmarks/ai-adoption/scenarios/third-party-api-intake.json",
    "benchmarks/ai-adoption/scenarios/repository-evaluation-full.json",
    "benchmarks/ai-adoption/scenarios/repository-evaluation-shallow.json",
    "benchmarks/ai-adoption/scenarios/public-growth-audit.json",
    "benchmarks/ai-adoption/scenarios/geo-ai-visibility.json",
    "benchmarks/ai-adoption/scenarios/page-template-selection.json",
    "benchmarks/ai-adoption/scenarios/glossary-inspection.json",
    "case-studies/README.md",
    "case-studies/sanitized/README.md",
    "case-studies/sanitized/measured-impact-template.md",
    "examples/operations/README.md",
]

FAST_REQUIRED_DIRS = [
    "vcp_cli",
    ".vcp/manifests",
    "protocols/integrations",
    "protocols/public-growth",
    "protocols/operations",
    "templates/reports",
    "templates/prompts",
    "templates/runtime/error-inbox",
    "templates/public-growth",
    "templates/public-growth/schema",
    "examples/integrations",
    "examples/public-growth",
    "examples/operations",
    "examples/backlog",
    "benchmarks/ai-adoption/scenarios",
]

STALE_VERSIONS = [
    "v0.1.11",
    "v0.2.0",
    "v0.2.1",
    "v0.2.2",
    "v0.3.0",
    "v0.4.0",
    "v0.4.1",
    "v0.4.2",
    "v0.4.3",
    "v0.4.4",
    "v0.5.0",
    "v0.5.1",
    "v0.5.2",
    "v0.5.3",
    "v0.5.4",
    "v0.5.5",
]

ENTRY_FILES_FOR_STALE_SCAN = [
    "README.md",
    "README_ru.md",
    "docs/versioning.md",
    "PROJECT_MAP.md",
    "package.json",
    "pyproject.toml",
]

CORE_SMOKE_COMMANDS = [
    ["--help"],
    ["version", "--json"],
    ["evaluate", "--json"],
    ["evaluate", "--print-prompt"],
    ["init", "--print-prompt"],
    ["route", "--profile", "production", "--json"],
    ["route", "--profile", "operations", "--json"],
    ["route", "--profile", "third-party-api", "--json"],
    ["route", "--profile", "public-growth", "--json"],
    ["adopt", "--pack", "third-party-api", "--dry-run", "--json"],
    ["adopt", "--pack", "public-growth", "--dry-run", "--json"],
    ["backlog", "validate", "--json"],
    ["backlog", "list", "--json"],
    ["backlog", "report", "--json"],
    ["backlog", "add", "--title", "Synthetic dry-run test item", "--type", "idea", "--priority", "P3", "--source", "manual", "--dry-run", "--json"],
    ["backlog", "move", "--id", "VCP-001", "--status", "doing", "--dry-run", "--json"],
    ["backlog", "done", "--id", "VCP-001", "--validation", "tests green", "--review", "accepted", "--dry-run", "--json"],
    ["backlog", "archive", "--id", "VCP-002", "--reason", "Synthetic archive path", "--dry-run", "--json"],
    ["backlog", "template"],
]


def current_python() -> str:
    return sys.executable or "python3"


def has_bash() -> bool:
    return shutil.which("bash") is not None


def has_git() -> bool:
    return shutil.which("git") is not None


def current_shell() -> str:
    return os.environ.get("SHELL") or os.environ.get("ComSpec") or "unknown"


def os_name() -> str:
    return platform.system()


def windows_path_mode() -> bool:
    return os.name == "nt" or platform.system().lower().startswith("windows")


def powershell_first_supported(root: Path) -> bool:
    return (root / "bin/vcp.ps1").exists() and (root / "vcp_cli/cli.py").exists()


def full_bash_checks_available(root: Path) -> bool:
    return has_bash() and (root / "scripts/check-toolkit.sh").exists() and (root / "scripts/vibe-check.sh").exists()


def _ok_result(name: str, runner: str, stdout: str = "", note: str = "") -> dict[str, Any]:
    return {
        "name": name,
        "status": "PASS",
        "runner": runner,
        "stdout": stdout.strip(),
        "note": note,
    }


def _fail_result(name: str, runner: str, errors: list[str] | None = None, stdout: str = "", stderr: str = "", note: str = "") -> dict[str, Any]:
    return {
        "name": name,
        "status": "FAIL",
        "runner": runner,
        "errors": errors or [],
        "stdout": stdout.strip(),
        "stderr": stderr.strip(),
        "note": note,
    }


def _skip_result(name: str, runner: str, reason: str) -> dict[str, Any]:
    return {
        "name": name,
        "status": "SKIP",
        "runner": runner,
        "reason": reason,
    }


def validate_required_files(root: Path) -> dict[str, Any]:
    missing: list[str] = []
    for rel in FAST_REQUIRED_FILES:
        if not (root / rel).exists():
            missing.append(rel)
    for _, path in manifest_paths(root).items():
        if not path.exists():
            missing.append(str(path.relative_to(root)))
    for rel in FAST_REQUIRED_DIRS:
        if not (root / rel).is_dir():
            missing.append(f"{rel}/")
    if missing:
        return _fail_result("required-files", "python", errors=missing)
    return _ok_result("required-files", "python", note="Core cross-platform CLI, manifests, npm wrapper, public-growth, operations, backlog, and API intake files are present.")


def validate_version_consistency(root: Path) -> dict[str, Any]:
    repo_ver = repo_version(root)
    method_ver = methodology_version(root)
    problems: list[str] = []
    vcp_manifest = manifest_path(root, "vcp")

    checks = [
        (root / "README.md", f"repo-{repo_ver}", "README badge"),
        (root / "README.md", repo_ver, "README repository package"),
        (root / "README_ru.md", repo_ver, "README_ru repository package"),
        (root / "CHANGELOG.md", repo_ver, "CHANGELOG entry"),
        (root / "docs/versioning.md", f"Repository package `{repo_ver}`", "docs/versioning repo version"),
        (root / "docs/versioning.md", f"Web methodology `{method_ver}`", "docs/versioning methodology version"),
        (root / f"docs/release-{repo_ver}.md", repo_ver, "release notes title"),
        (vcp_manifest, f'"package_version": "{repo_ver}"', "vcp manifest package version"),
        (vcp_manifest, f'"methodology_version": "{method_ver}"', "vcp manifest methodology version"),
        (root / "package.json", f'"version": "{repo_ver.removeprefix("v")}"', "package.json version"),
        (root / "pyproject.toml", f'version = "{repo_ver.removeprefix("v")}"', "pyproject.toml version"),
        (root / "vcp_cli/__init__.py", f'__version__ = "{repo_ver.removeprefix("v")}"', "vcp_cli version"),
    ]
    for path, needle, label in checks:
        if not path.exists():
            problems.append(f"Missing file: {path.relative_to(root)}")
            continue
        if needle not in path.read_text(encoding="utf-8"):
            problems.append(f"Version mismatch in {path.relative_to(root)}: missing {label} -> {needle}")

    for path in sorted((root / "templates").rglob("*.md")):
        rel = path.relative_to(root).as_posix()
        if rel in VERSION_EXCLUSIONS or rel.endswith("_ru.md"):
            continue
        text = path.read_text(encoding="utf-8")
        if f"<!-- vcp-version: {repo_ver} -->" not in text:
            problems.append(f"Template marker missing in {rel}: <!-- vcp-version: {repo_ver} -->")
        if f"<!-- methodology-version: {method_ver} -->" not in text:
            problems.append(f"Methodology marker missing in {rel}: <!-- methodology-version: {method_ver} -->")

    for rel in ENTRY_FILES_FOR_STALE_SCAN:
        path = root / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for stale in STALE_VERSIONS:
            if stale == repo_ver:
                continue
            if stale in text:
                problems.append(f"Stale version marker in {rel}: {stale}")

    if problems:
        return _fail_result("version-consistency", "python", errors=problems)
    return _ok_result("version-consistency", "python", note=f"Repository package {repo_ver} and methodology {method_ver} are aligned.")


def run_python_script(root: Path, relative_script: str) -> dict[str, Any]:
    proc = run_command([current_python(), relative_script], root)
    name = Path(relative_script).name
    if proc.returncode != 0:
        return _fail_result(name, "python", stdout=proc.stdout, stderr=proc.stderr)
    return _ok_result(name, "python", stdout=proc.stdout)


def validate_manifest_in_process() -> dict[str, Any]:
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        rc = manifest_cmd.validate_manifests(json_mode=True)
    raw = buffer.getvalue().strip()
    payload = json.loads(raw) if raw else {"ok": rc == 0, "errors": []}
    if rc != 0 or not payload.get("ok", False):
        return _fail_result("manifest-validation", "python", errors=payload.get("errors", []), stdout=raw)
    return _ok_result("manifest-validation", "python", stdout=raw)


def validate_benchmarks_in_process() -> dict[str, Any]:
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        rc = benchmark_cmd.run(None, True)
    raw = buffer.getvalue().strip()
    payload = json.loads(raw) if raw else {"ok": rc == 0, "results": []}
    errors = []
    for item in payload.get("results", []):
        if not item.get("ok", False):
            errors.extend(item.get("errors", []))
    if rc != 0 or errors:
        return _fail_result("benchmark-validation", "python", errors=errors, stdout=raw)
    return _ok_result("benchmark-validation", "python", stdout=raw)


def validate_cli_smoke(root: Path) -> dict[str, Any]:
    failures: list[str] = []
    outputs: list[str] = []
    for command in CORE_SMOKE_COMMANDS:
        proc = run_command([current_python(), "-m", "vcp_cli", *command], root)
        label = " ".join(command)
        outputs.append(f"$ vcp {label}\n{(proc.stdout or proc.stderr).strip()}")
        if proc.returncode != 0:
            failures.append(label)
    if failures:
        return _fail_result("cli-smoke", "python", errors=failures, stdout="\n\n".join(outputs))
    return _ok_result("cli-smoke", "python", stdout="\n\n".join(outputs))


def run_fast_checks(root: Path) -> list[dict[str, Any]]:
    return [
        validate_required_files(root),
        validate_version_consistency(root),
        run_python_script(root, "scripts/check-newlines.py"),
        run_python_script(root, "scripts/validate-links.sh"),
        validate_manifest_in_process(),
        validate_benchmarks_in_process(),
        validate_cli_smoke(root),
    ]


def run_full_bash_checks(root: Path, include_audit: bool = True) -> list[dict[str, Any]]:
    if not has_bash():
        return [
            _skip_result("legacy-toolkit", "bash", "bash not available; use Git Bash, WSL or MSYS2 for full legacy script parity."),
            _skip_result("legacy-audit", "bash", "bash not available; fast Python CLI path still works cross-platform.") if include_audit else _skip_result("legacy-audit", "bash", "audit not requested"),
        ]

    results: list[dict[str, Any]] = []
    toolkit = run_command(["bash", "scripts/check-toolkit.sh"], root)
    if toolkit.returncode != 0:
        results.append(_fail_result("legacy-toolkit", "bash", stdout=toolkit.stdout, stderr=toolkit.stderr))
    else:
        results.append(_ok_result("legacy-toolkit", "bash", stdout=toolkit.stdout))

    if include_audit:
        audit = run_command(["bash", "scripts/vibe-check.sh", "--audit", "--json"], root)
        if audit.returncode != 0:
            results.append(_fail_result("legacy-audit", "bash", stdout=audit.stdout, stderr=audit.stderr))
        else:
            results.append(_ok_result("legacy-audit", "bash", stdout=audit.stdout))
    return results


def summarize_results(results: list[dict[str, Any]]) -> tuple[bool, int, int, int]:
    passed = sum(1 for item in results if item["status"] == "PASS")
    failed = sum(1 for item in results if item["status"] == "FAIL")
    skipped = sum(1 for item in results if item["status"] == "SKIP")
    return failed == 0, passed, failed, skipped


def render_results(results: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    for item in results:
        lines.append(f"[{item['status']}] {item['name']} ({item['runner']})")
        if item.get("note"):
            lines.append(f"  note: {item['note']}")
        if item.get("reason"):
            lines.append(f"  reason: {item['reason']}")
        if item.get("errors"):
            for error in item["errors"]:
                lines.append(f"  - {error}")
        if item.get("stdout"):
            lines.append(item["stdout"])
        if item.get("stderr"):
            lines.append(item["stderr"])
    return "\n".join(lines)
