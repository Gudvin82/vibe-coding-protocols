from __future__ import annotations

import contextlib
import io
import json
import os
import platform
import re
import shutil
import sys
from pathlib import Path
from typing import Any

from . import benchmark as benchmark_cmd
from . import manifest as manifest_cmd
from .utils import (
    dump_json,
    load_json,
    methodology_version,
    read_trimmed,
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
    "START_HERE.md",
    "AI_INTAKE.md",
    "docs/cli.md",
    "docs/windows.md",
    "docs/protocol-index.md",
    "docs/adoption-packs.md",
    "docs/tooling-roadmap.md",
    "docs/known-limitations.md",
    "protocols/integrations/README.md",
    "protocols/integrations/third-party-api-intake.md",
    "commands/third-party-api-intake.md",
    "templates/prompts/third-party-api-intake.md",
    "templates/reports/third-party-api-intake-report.md",
    "templates/THIRD_PARTY_REGISTRY.md",
    "templates/examples/THIRD_PARTY_REGISTRY.filled.example.md",
    "scripts/check-newlines.py",
    "scripts/validate-links.sh",
    "scripts/check-version-consistency.sh",
    "vcp.manifest.json",
    "protocols.manifest.json",
    "adoption-packs.manifest.json",
    "commands.manifest.json",
    "reports.manifest.json",
    "benchmarks.manifest.json",
    "benchmarks/ai-adoption/scenarios/third-party-api-intake.json",
    "bin/vcp",
    "bin/vcp.cmd",
    "bin/vcp.ps1",
]

FAST_REQUIRED_DIRS = [
    "vcp_cli",
    "protocols/integrations",
    "templates/reports",
    "templates/prompts",
    "examples/integrations",
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
    ["route", "--profile", "production", "--json"],
    ["route", "--profile", "third-party-api", "--json"],
    ["adopt", "--pack", "third-party-api", "--dry-run", "--json"],
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
    for rel in FAST_REQUIRED_DIRS:
        if not (root / rel).is_dir():
            missing.append(f"{rel}/")
    if missing:
        return _fail_result("required-files", "python", errors=missing)
    return _ok_result("required-files", "python", note="Core cross-platform CLI and API intake files are present.")


def validate_version_consistency(root: Path) -> dict[str, Any]:
    repo_ver = repo_version(root)
    method_ver = methodology_version(root)
    problems: list[str] = []

    checks = [
        (root / "README.md", f"repo-{repo_ver}", "README badge"),
        (root / "README.md", repo_ver, "README repository package"),
        (root / "README_ru.md", repo_ver, "README_ru repository package"),
        (root / "CHANGELOG.md", repo_ver, "CHANGELOG entry"),
        (root / "docs/versioning.md", f"Repository package `{repo_ver}`", "docs/versioning repo version"),
        (root / "docs/versioning.md", f"Web methodology `{method_ver}`", "docs/versioning methodology version"),
        (root / f"docs/release-{repo_ver}.md", repo_ver, "release notes title"),
        (root / "vcp.manifest.json", f'"package_version": "{repo_ver}"', "vcp manifest package version"),
        (root / "vcp.manifest.json", f'"methodology_version": "{method_ver}"', "vcp manifest methodology version"),
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
    passed = sum(1 for item in results if item.get("status") == "PASS")
    failed = sum(1 for item in results if item.get("status") == "FAIL")
    skipped = sum(1 for item in results if item.get("status") == "SKIP")
    return failed == 0, passed, failed, skipped
