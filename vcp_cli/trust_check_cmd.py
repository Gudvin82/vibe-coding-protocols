from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from .catalog_cmd import validate as validate_catalog
from .agent_kits_cmd import validate_registry as validate_agent_kits_registry
from .change_cmd import validate_change_intent_data
from .charter_cmd import validate_charter_data
from .integrations_cmd import ALLOWED_STATUSES as INTEGRATION_STATUSES, list_payload, packs_payload
from .profiles_cmd import validate as validate_profiles
from .utils import dump_json, load_json, print_output, repo_root, repo_version, run_command


SCRIPT_CHECKS = [
    ("version-surfaces", ["python3", "scripts/check-public-version-surfaces.py"], "Public version surfaces agree with the current repository package."),
    ("readme-parity", ["python3", "scripts/check-readme-parity.py"], "README.md and README_ru.md expose the same current-release and route signals."),
    ("russian-docs-parity", ["python3", "scripts/check-russian-docs-parity.py"], "Russian docs index and release surfaces are present and synchronized."),
    ("roadmap-overclaim", ["python3", "scripts/check-roadmap-overclaim.py"], "Roadmap-only surfaces are not described as shipped."),
    ("evaluator-pack", ["python3", "scripts/check-evaluator-pack.py"], "Evaluator shortcut, anti-misread surfaces, token-budget levels, machine-readable evaluator pack, and evaluation-receipt rules are synchronized."),
]


DOC_EXPECTATIONS = {
    "README.md": [
        "EVALUATE_THIS_REPO.md",
        "PUBLIC_EVALUATION_KIT.md",
        "docs/killer-workflow.md",
        "docs/comparisons.md",
        "docs/product-model.md",
        "docs/benchmark-report.md",
        "docs/trust-check.md",
        "docs/ai-tooling.md",
        "docs/proof-snapshot.md",
        "docs/evaluator-architecture-map.md",
        "docs/evaluation-receipt.md",
        "docs/public-proof-demo.md",
        "docs/community-and-adoption-status.md",
        "docs/control-catalog.md",
        "docs/change-intent.md",
        "docs/starter-template-adoption.md",
        "docs/agent-rule-profiles.md",
        "docs/project-control-charter.md",
        "docs/ecosystem-map.md",
        "docs/ai-augmented-solo-squad-path.md",
        "docs/control-spine.md",
        "docs/first-time-adoption.md",
        "docs/flagship-demo.md",
        "docs_ru/README.md",
    ],
    "README_ru.md": [
        "EVALUATE_THIS_REPO.md",
        "PUBLIC_EVALUATION_KIT.md",
        "docs_ru/killer-workflow.md",
        "docs_ru/comparisons.md",
        "docs_ru/product-model.md",
        "docs_ru/benchmark-report.md",
        "docs_ru/trust-check.md",
        "docs_ru/ai-tooling.md",
        "docs_ru/proof-snapshot.md",
        "docs_ru/evaluation-receipt.md",
        "docs_ru/public-proof-demo.md",
        "docs_ru/community-and-adoption-status.md",
        "docs/control-catalog.md",
        "docs/change-intent.md",
        "docs/starter-template-adoption.md",
        "docs/agent-rule-profiles.md",
        "docs/project-control-charter.md",
        "docs/ecosystem-map.md",
        "docs/ai-augmented-solo-squad-path.md",
        "docs/control-spine.md",
        "docs/first-time-adoption.md",
        "docs/flagship-demo.md",
    ],
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


def _control_catalog_check(root: Path) -> dict[str, Any]:
    problems = validate_catalog(root)
    return {
        "id": "control-catalog",
        "status": "pass" if not problems else "fail",
        "summary": "Control catalog docs and machine-readable catalog exist and catalog entries validate.",
        "details": problems or ["Control catalog surfaces are present and valid."],
    }


def _change_intent_check(root: Path) -> dict[str, Any]:
    required = [
        "docs/change-intent.md",
        "docs_ru/change-intent.md",
        "templates/reports/change-intent.md",
        "schemas/change-intent.schema.json",
        ".vcp/change-intent.example.json",
    ]
    missing = [rel for rel in required if not (root / rel).exists()]
    problems = [f"missing {rel}" for rel in missing]
    if not missing:
        problems.extend(validate_change_intent_data(load_json(root / ".vcp" / "change-intent.example.json"), root))
    return {
        "id": "change-intent",
        "status": "pass" if not problems else "fail",
        "summary": "Change-intent docs, schema, template, and example exist and validate.",
        "details": problems or ["Change-intent surfaces are present and valid."],
    }


def _starter_adoption_matrix_check(root: Path) -> dict[str, Any]:
    required = ["docs/starter-template-adoption.md", "docs_ru/starter-template-adoption.md", ".vcp/starter-adoption-matrix.json"]
    problems = [f"missing {rel}" for rel in required if not (root / rel).exists()]
    if not problems:
        payload = load_json(root / ".vcp" / "starter-adoption-matrix.json")
        if payload.get("official_integrations_claimed") is not False:
            problems.append("starter-adoption-matrix must not claim official integrations")
        if len(payload.get("items", [])) < 10:
            problems.append("starter-adoption-matrix must contain at least 10 starter categories")
    return {
        "id": "starter-adoption-matrix",
        "status": "pass" if not problems else "fail",
        "summary": "Starter adoption matrix exists and positions VCP as a complementary control layer.",
        "details": problems or ["Starter adoption matrix surfaces are present and valid."],
    }


def _agent_rule_profiles_check(root: Path) -> dict[str, Any]:
    problems = validate_profiles(root)
    return {
        "id": "agent-rule-profiles",
        "status": "pass" if not problems else "fail",
        "summary": "Nano, mini, and full agent rule profiles exist and stay constraint-first.",
        "details": problems or ["Agent rule profiles are present and valid."],
    }


def _project_control_charter_check(root: Path) -> dict[str, Any]:
    required = [
        "docs/project-control-charter.md",
        "docs_ru/project-control-charter.md",
        "templates/project-control-charter.md",
        "schemas/project-control-charter.schema.json",
        ".vcp/project-control-charter.example.json",
    ]
    problems = [f"missing {rel}" for rel in required if not (root / rel).exists()]
    if not problems:
        problems.extend(validate_charter_data(load_json(root / ".vcp" / "project-control-charter.example.json"), root))
    return {
        "id": "project-control-charter",
        "status": "pass" if not problems else "fail",
        "summary": "Project control charter docs, template, schema, and example exist and validate.",
        "details": problems or ["Project control charter surfaces are present and valid."],
    }


def _ecosystem_map_check(root: Path) -> dict[str, Any]:
    required = ["docs/ecosystem-map.md", "docs_ru/ecosystem-map.md"]
    problems = [f"missing {rel}" for rel in required if not (root / rel).exists()]
    if not problems:
        text = _text(root, "docs/ecosystem-map.md")
        for needle in (
            "Spec Kit",
            "OpenSpec-like tools",
            "Full-stack templates",
            "VCP complements adjacent tools and does not replace them.",
        ):
            if needle not in text:
                problems.append(f"docs/ecosystem-map.md missing {needle}")
    return {
        "id": "ecosystem-map",
        "status": "pass" if not problems else "fail",
        "summary": "Ecosystem map exists and keeps comparison boundaries respectful.",
        "details": problems or ["Ecosystem map surfaces are present and valid."],
    }


def _rule_provenance_check(root: Path) -> dict[str, Any]:
    required = ["docs/agent-rule-provenance.md", "docs_ru/agent-rule-provenance.md", ".vcp/agent-rule-provenance.json"]
    problems = [f"missing {rel}" for rel in required if not (root / rel).exists()]
    if not problems:
        payload = load_json(root / ".vcp" / "agent-rule-provenance.json")
        profile_ids = {item.get("id") for item in load_json(root / ".vcp" / "agent-rule-profiles.json").get("items", [])}
        provenance_ids = {item.get("id") for item in payload.get("items", [])}
        if profile_ids != provenance_ids:
            problems.append("rule provenance ids must match agent-rule-profiles ids")
        for item in payload.get("items", []):
            if item.get("status") not in {"shipped", "optional", "experimental", "roadmap-only", "not-shipped"}:
                problems.append(f"invalid provenance status for {item.get('id')}: {item.get('status')!r}")
    return {
        "id": "agent-rule-provenance",
        "status": "pass" if not problems else "fail",
        "summary": "Rule provenance exists, lists shipped profiles, and uses valid statuses.",
        "details": problems or ["Rule provenance surfaces are present and valid."],
    }


def _solo_squad_check(root: Path) -> dict[str, Any]:
    required = [
        "docs/ai-augmented-solo-squad-path.md",
        "docs_ru/ai-augmented-solo-squad-path.md",
        ".vcp/workflows/ai-augmented-solo-squad.json",
        "templates/reports/solo-squad-control-plan.md",
    ]
    problems = [f"missing {rel}" for rel in required if not (root / rel).exists()]
    if not problems:
        text = _text(root, "docs/ai-augmented-solo-squad-path.md")
        if "human-led" not in text:
            problems.append("docs/ai-augmented-solo-squad-path.md must say human-led")
        if "does not claim autonomous orchestration" not in text:
            problems.append("docs/ai-augmented-solo-squad-path.md must reject autonomous orchestration overclaim")
    return {
        "id": "ai-augmented-solo-squad-path",
        "status": "pass" if not problems else "fail",
        "summary": "Solo/squad path exists and stays explicitly human-led.",
        "details": problems or ["Solo/squad path surfaces are present and valid."],
    }


def _agent_kits_check(root: Path) -> dict[str, Any]:
    required = [
        "docs/integrations/setup-playbook.md",
        "docs_ru/integration-setup.md",
        "docs/integrations/agent-kits.md",
        "docs_ru/agent-kits.md",
        ".vcp/agent-kits.json",
        "templates/agents/COPILOT_INSTRUCTIONS.md",
        "ci-examples/github-actions/vcp-pr-gate.yml",
    ]
    problems = [f"missing {rel}" for rel in required if not (root / rel).exists()]
    for kit_id in ("claude", "codex", "cursor", "copilot", "github-actions"):
        kit_dir = root / "templates" / "agent-kits" / kit_id
        if not kit_dir.exists():
            problems.append(f"missing kit folder templates/agent-kits/{kit_id}")
            continue
        if not (kit_dir / "README.md").exists():
            problems.append(f"missing kit README for {kit_id}")
    if not problems:
        problems.extend(validate_agent_kits_registry(root))
    for rel in (
        "docs/integrations/agent-kits.md",
        "docs/integrations/setup-playbook.md",
        "docs_ru/agent-kits.md",
        "docs_ru/integration-setup.md",
        "README.md",
        "README_ru.md",
    ):
        text = _text(root, rel)
        if "not official plugin" not in text and "not official plugins" not in text and "не official plugin" not in text and "Это не official plugins" not in text:
            problems.append(f"{rel} must state the not-official-plugin boundary")
    return {
        "id": "agent-kits",
        "status": "pass" if not problems else "fail",
        "summary": "Copy-ready AI tool agent kits, setup docs, safe export registry, and no-overclaim boundaries exist.",
        "details": problems or ["Agent kit docs, templates, registry, and boundaries are present and valid."],
    }


def _v091_surface_check(root: Path) -> dict[str, Any]:
    required = [
        "PUBLIC_EVALUATION_KIT.md",
        "docs/product-spine.md",
        "docs/control-spine.md",
        "docs/first-time-adoption.md",
        "docs/adaptive-rigor-modes.md",
        "docs/tiny-vcp-pipeline.md",
        "docs/flagship-demo.md",
        "docs/portable-control-pack.md",
        "docs/surface-priority-model.md",
        "docs/work-package-lifecycle.md",
        "docs/review-accept-merge.md",
        "docs/mission-retrospective.md",
        "docs/delivery-graph.md",
        "docs/public-evaluation-kit.md",
        "docs/scope-boundary.md",
        "docs_ru/product-spine.md",
        "docs_ru/control-spine.md",
        "docs_ru/first-time-adoption.md",
        "docs_ru/adaptive-rigor-modes.md",
        "docs_ru/tiny-vcp-pipeline.md",
        "docs_ru/flagship-demo.md",
        "docs_ru/portable-control-pack.md",
        "docs_ru/surface-priority-model.md",
        "docs_ru/work-package-lifecycle.md",
        "docs_ru/review-accept-merge.md",
        "docs_ru/mission-retrospective.md",
        "docs_ru/delivery-graph.md",
        "docs_ru/public-evaluation-kit.md",
        "docs_ru/scope-boundary.md",
        "site/README.md",
        "examples/flagship-demo/README.md",
        "templates/control-pack/README.md",
        ".vcp/control-spine.json",
        ".vcp/rigor-modes.json",
        ".vcp/surface-priority-model.json",
        ".vcp/work-packages/example.json",
        ".vcp/review-accept-merge.example.json",
        ".vcp/delivery-graph.example.json",
    ]
    missing = [rel for rel in required if not (root / rel).exists()]
    status = "pass" if not missing else "fail"
    return {
        "id": "v091-product-spine",
        "status": status,
        "summary": "v0.9.1 product spine, first-time adoption, portable control, and flagship demo surfaces exist.",
        "details": [f"missing {rel}" for rel in missing] or ["v0.9.1 product-spine surfaces are present."],
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
    checks.append(_control_catalog_check(root))
    checks.append(_change_intent_check(root))
    checks.append(_starter_adoption_matrix_check(root))
    checks.append(_agent_rule_profiles_check(root))
    checks.append(_project_control_charter_check(root))
    checks.append(_ecosystem_map_check(root))
    checks.append(_rule_provenance_check(root))
    checks.append(_solo_squad_check(root))
    checks.append(_agent_kits_check(root))
    checks.append(_v091_surface_check(root))
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
