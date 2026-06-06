from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from .integrations_cmd import ALLOWED_STATUSES as INTEGRATION_STATUSES, list_payload, packs_payload
from .utils import dump_json, load_json, print_output, repo_root, repo_version, run_command


SCRIPT_CHECKS = [
    ("version-surfaces", ["python3", "scripts/check-public-version-surfaces.py"], "Public version surfaces agree with the current repository package."),
    ("readme-parity", ["python3", "scripts/check-readme-parity.py"], "README.md and README_ru.md expose the same current-release and route signals."),
    ("russian-docs-parity", ["python3", "scripts/check-russian-docs-parity.py"], "Russian docs index and release surfaces are present and synchronized."),
    ("roadmap-overclaim", ["python3", "scripts/check-roadmap-overclaim.py"], "Roadmap-only surfaces are not described as shipped."),
    ("evaluator-pack", ["python3", "scripts/check-evaluator-pack.py"], "Evaluator shortcut, anti-misread surfaces, token-budget levels, machine-readable evaluator pack, and evaluation-receipt rules are synchronized."),
]


DOC_EXPECTATIONS = {
    "README.md": ["EVALUATE_THIS_REPO.md", "docs/killer-workflow.md", "docs/comparisons.md", "docs/product-model.md", "docs/benchmark-report.md", "docs/trust-check.md", "docs/ai-tooling.md", "docs/proof-snapshot.md", "docs/evaluator-architecture-map.md", "docs/evaluation-receipt.md", "docs/public-proof-demo.md", "docs/community-and-adoption-status.md", "docs_ru/README.md"],
    "README_ru.md": ["EVALUATE_THIS_REPO.md", "docs_ru/killer-workflow.md", "docs_ru/comparisons.md", "docs_ru/product-model.md", "docs_ru/benchmark-report.md", "docs_ru/trust-check.md", "docs_ru/ai-tooling.md", "docs_ru/proof-snapshot.md", "docs_ru/evaluation-receipt.md", "docs_ru/public-proof-demo.md", "docs_ru/community-and-adoption-status.md"],
}


def _text(root: Path, rel: str) -> str:
    return (root / rel).read_text(encoding="utf-8")


def _status_rank(value: str) -> int:
    return {"pass": 0, "warn": 1, "fail": 2}[value]


def _script_check(root: Path, check_id: str, command: list[str], summary: str) -> dict[str, Any]:
    try:
        result = run_command(command, root)
        status = "pass" if result.returncode == 0 else "fail"
        details = result.stdout.strip() or result.stderr.strip() or "no output"
    except OSError as exc:
        status = "fail"
        details = f"command could not start: {exc}"
    return {
        "id": check_id,
        "status": status,
        "summary": summary,
        "details": details,
        "command": " ".join(command),
    }


def _readme_link_check(root: Path) -> dict[str, Any]:
    missing: list[str] = []
    for rel, needles in DOC_EXPECTATIONS.items():
        text = _text(root, rel)
        for needle in needles:
            if needle not in text:
                missing.append(f"{rel} missing {needle}")
    status = "pass" if not missing else "fail"
    return {
        "id": "landing-page-links",
        "status": status,
        "summary": "Landing-page README surfaces link to killer workflow, comparisons, product model, benchmark report, trust check, and AI tooling docs.",
        "details": missing or ["README and README_ru include the expected landing-page links."],
    }


def _workflow_sync_check(root: Path) -> dict[str, Any]:
    workflow = load_json(root / ".vcp" / "workflows" / "mvp-to-launch.json")
    workflow_id = workflow.get("id")
    docs_to_scan = [
        "README.md",
        "README_ru.md",
        "docs/killer-workflow.md",
        "docs/local-platform-flow.md",
        "docs/mvp-to-launch-path.md",
        "docs/workflows.md",
    ]
    missing = [rel for rel in docs_to_scan if workflow_id not in _text(root, rel)]
    status = "pass" if not missing else "warn"
    return {
        "id": "workflow-doc-sync",
        "status": status,
        "summary": "Canonical workflow ids are discoverable from the main docs.",
        "details": [f"{workflow_id} missing from {rel}" for rel in missing] or [f"Workflow id {workflow_id} is referenced by all key docs."],
    }


def _integration_status_check(root: Path) -> dict[str, Any]:
    problems: list[str] = []
    for payload, label in ((list_payload(root=root), ".vcp/integrations.json"), (packs_payload(root=root), ".vcp/integration-packs.json")):
        for item in payload["items"]:
            status = item.get("status")
            if status not in INTEGRATION_STATUSES:
                problems.append(f"{label}: {item.get('id')} has invalid status {status!r}")
    status = "pass" if not problems else "fail"
    return {
        "id": "integration-status-validity",
        "status": status,
        "summary": "Integration and integration-pack registries use only declared statuses.",
        "details": problems or ["All integration statuses are valid."],
    }


def _benchmark_report_check(root: Path) -> dict[str, Any]:
    current = repo_version(root)
    report = _text(root, "docs/benchmark-report.md")
    details: list[str] = []
    if current not in report:
        details.append(f"docs/benchmark-report.md missing {current}")
    if "python3 -m vcp_cli benchmark run --json" not in report:
        details.append("docs/benchmark-report.md missing reproduction command")
    status = "pass" if not details else "fail"
    return {
        "id": "benchmark-report",
        "status": status,
        "summary": "Public benchmark report exists, names the current release, and explains how to reproduce it.",
        "details": details or ["Benchmark report references the current version and reproduction command."],
    }


def _evaluator_surface_check(root: Path) -> dict[str, Any]:
    required = [
        "EVALUATE_THIS_REPO.md",
        "docs/anti-misread-guide.md",
        "docs_ru/anti-misread-guide.md",
        "docs/evaluator-architecture-map.md",
        "docs_ru/evaluator-architecture-map.md",
        "docs/proof-snapshot.md",
        "docs_ru/proof-snapshot.md",
        "templates/reports/external-evaluation.md",
        ".vcp/evaluator-pack.json",
        "docs/agent-model-routing.md",
        "docs_ru/agent-model-routing.md",
        "docs/evaluator-token-budget.md",
        "docs_ru/evaluator-token-budget.md",
        "docs/visuals.md",
        "docs_ru/visuals.md",
        "docs/evaluation-receipt.md",
        "docs_ru/evaluation-receipt.md",
        "templates/reports/evaluation-receipt.md",
        "schemas/evaluation-receipt.schema.json",
        ".vcp/evaluation-receipt.example.json",
        "docs/public-proof-demo.md",
        "docs_ru/public-proof-demo.md",
        "docs/community-and-adoption-status.md",
        "docs_ru/community-and-adoption-status.md",
        "docs/license.md",
        "docs_ru/license.md",
        "assets/presentations/README.md",
        "docs/presentations.md",
        "docs_ru/presentations.md",
    ]
    missing = [rel for rel in required if not (root / rel).exists()]
    status = "pass" if not missing else "fail"
    return {
        "id": "evaluator-surfaces",
        "status": status,
        "summary": "Evaluator shortcut, anti-misread docs, proof snapshot, architecture map, token-budget docs, and machine-readable evaluator pack exist.",
        "details": [f"missing {rel}" for rel in missing] or ["Evaluator-proof surfaces are present."],
    }


def _proof_strip_check(root: Path) -> dict[str, Any]:
    required_snippets = [
        "benchmark scenarios:",
        "cards:",
        "CLI commands in manifest:",
        "tests:",
        "report templates:",
        "trust-check: yes",
        "evaluator pack: yes",
    ]
    missing: list[str] = []
    for rel in ("README.md", "README_ru.md", "docs/proof-snapshot.md", "docs_ru/proof-snapshot.md"):
        text = _text(root, rel)
        for snippet in required_snippets:
            if snippet not in text:
                missing.append(f"{rel} missing proof-strip snippet: {snippet}")
    status = "pass" if not missing else "fail"
    return {
        "id": "proof-strip",
        "status": status,
        "summary": "Public proof numbers strip is visible in README and proof snapshot surfaces.",
        "details": missing or ["Proof strip is visible on README and proof snapshot surfaces."],
    }


def _license_model_check(root: Path) -> dict[str, Any]:
    missing = [rel for rel in ("LICENSE", "LICENSE-CODE-MIT", "LICENSE-DOCS-CC-BY-4.0", "NOTICE", "docs/license.md", "docs_ru/license.md") if not (root / rel).exists()]
    status = "pass" if not missing else "fail"
    return {
        "id": "license-model",
        "status": status,
        "summary": "Dual-license model for code versus docs/methodology is documented.",
        "details": [f"missing {rel}" for rel in missing] or ["Dual-license surfaces are present."],
    }


def _community_adoption_check(root: Path) -> dict[str, Any]:
    required = ["docs/community-and-adoption-status.md", "docs_ru/community-and-adoption-status.md"]
    missing = [rel for rel in required if not (root / rel).exists()]
    status = "pass" if not missing else "fail"
    return {
        "id": "community-adoption",
        "status": status,
        "summary": "Community/adoption status docs exist and make social-proof limits explicit.",
        "details": [f"missing {rel}" for rel in missing] or ["Community/adoption status docs are present."],
    }


def _presentation_destination_check(root: Path) -> dict[str, Any]:
    required = ["assets/presentations/README.md", "docs/presentations.md", "docs_ru/presentations.md"]
    missing = [rel for rel in required if not (root / rel).exists()]
    status = "pass" if not missing else "fail"
    return {
        "id": "presentations-destination",
        "status": status,
        "summary": "Presentations destination is prepared without claiming the files already ship.",
        "details": [f"missing {rel}" for rel in missing] or ["Presentations destination docs are present."],
    }


def _public_proof_demo_check(root: Path) -> dict[str, Any]:
    required = [
        "examples/public-proof/README.md",
        "examples/public-proof/before-raw-ai-mvp.md",
        "examples/public-proof/after-vcp-launch-control-package.md",
        "examples/public-proof/route-example.json",
        "examples/public-proof/risk-backlog-example.json",
        "examples/public-proof/pr-gate-example.json",
        "examples/public-proof/metrics-board-example.json",
        "examples/public-proof/launch-decision-example.md",
        "examples/public-proof/trust-check-example.json",
    ]
    missing = [rel for rel in required if not (root / rel).exists()]
    status = "pass" if not missing else "fail"
    return {
        "id": "public-proof-demo",
        "status": status,
        "summary": "Public proof demo exists as a quick before/after artifact pack.",
        "details": [f"missing {rel}" for rel in missing] or ["Public proof demo assets are present."],
    }


def _changelog_hygiene_check(root: Path) -> dict[str, Any]:
    current = repo_version(root)
    text = _text(root, "CHANGELOG.md")
    lines = [line for line in text.splitlines() if line.strip()]
    details: list[str] = []
    if not lines or lines[0].strip() != "# Changelog":
        details.append("first non-empty line must be '# Changelog'")
    match = re.search(r"^##\s+(v\d+\.\d+\.\d+)\b", text, re.MULTILINE)
    if not match:
        details.append("missing release heading")
    elif match.group(1) != current:
        details.append(f"latest release heading is {match.group(1)!r}, expected {current!r}")
    status = "pass" if not details else "fail"
    return {
        "id": "changelog-hygiene",
        "status": status,
        "summary": "CHANGELOG starts with a heading and lists the current release first.",
        "details": details or [f"CHANGELOG begins with '# Changelog' and lists {current} first."],
    }


def _release_doc_check(root: Path) -> dict[str, Any]:
    current = repo_version(root)
    expected = [root / "docs" / f"release-{current}.md", root / "docs_ru" / f"release-{current}.md"]
    missing = [str(path.relative_to(root)) for path in expected if not path.exists()]
    status = "pass" if not missing else "fail"
    return {
        "id": "release-docs",
        "status": status,
        "summary": "English and Russian release notes exist for the current package version.",
        "details": missing or [f"Release docs exist for {current}."],
    }


def payload(root: Path | None = None) -> dict[str, Any]:
    root = repo_root(root)
    current = repo_version(root)
    checks: list[dict[str, Any]] = []

    for check_id, command, summary in SCRIPT_CHECKS:
        checks.append(_script_check(root, check_id, command, summary))
    checks.append(_readme_link_check(root))
    checks.append(_workflow_sync_check(root))
    checks.append(_integration_status_check(root))
    checks.append(_benchmark_report_check(root))
    checks.append(_evaluator_surface_check(root))
    checks.append(_proof_strip_check(root))
    checks.append(_license_model_check(root))
    checks.append(_public_proof_demo_check(root))
    checks.append(_community_adoption_check(root))
    checks.append(_presentation_destination_check(root))
    checks.append(_changelog_hygiene_check(root))
    checks.append(_release_doc_check(root))

    worst = max((item["status"] for item in checks), key=_status_rank, default="pass")
    summary = {
        "pass": sum(1 for item in checks if item["status"] == "pass"),
        "warn": sum(1 for item in checks if item["status"] == "warn"),
        "fail": sum(1 for item in checks if item["status"] == "fail"),
    }
    return {
        "status": worst,
        "version": current,
        "checks": checks,
        "summary": summary,
        "note": "Trust Check is a repository trust and consistency audit. It does not certify production safety.",
    }


def run(json_mode: bool = False) -> int:
    data = payload()
    print_output(data, json_mode)
    return 0 if data["status"] != "fail" else 1
