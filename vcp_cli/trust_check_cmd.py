from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from .catalog_cmd import validate as validate_catalog
from .agent_kits_cmd import validate_registry as validate_agent_kits_registry
from .utils import load_json, print_output, repo_root, repo_version, run_command

SCRIPT_CHECKS = [
    ("version-surfaces", ["python3", "scripts/check-public-version-surfaces.py"], "Public version surfaces agree with the current repository package."),
    ("readme-parity", ["python3", "scripts/check-readme-parity.py"], "README.md and README_ru.md expose the same current-release and route signals."),
    ("russian-docs-parity", ["python3", "scripts/check-russian-docs-parity.py"], "Russian docs index and release surfaces are present and synchronized."),
    ("roadmap-overclaim", ["python3", "scripts/check-roadmap-overclaim.py"], "Roadmap-only surfaces are not described as shipped."),
    ("evaluator-pack", ["python3", "scripts/check-evaluator-pack.py"], "Evaluator shortcut, token-budget layers, and machine-readable evaluator pack are synchronized."),
    ("proof-counts-script", ["python3", "scripts/check-proof-counts.py"], "Canonical proof counts and public proof surfaces stay synchronized."),
]


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


def _bundle_check(root: Path, check_id: str, summary: str, required: list[str], *, needles: dict[str, list[str]] | None = None) -> dict[str, Any]:
    problems = [f"missing {rel}" for rel in required if not (root / rel).exists()]
    if not problems and needles:
        for rel, rel_needles in needles.items():
            text = _text(root, rel)
            for needle in rel_needles:
                if needle not in text:
                    problems.append(f"{rel} missing {needle}")
    return {
        "id": check_id,
        "status": "pass" if not problems else "fail",
        "summary": summary,
        "details": problems or [summary],
    }


def _proof_counts_check(root: Path) -> dict[str, Any]:
    required = [
        ".vcp/proof-counts.json",
        "docs/proof-counts.md",
        "docs_ru/proof-counts.md",
        "docs/proof-snapshot.md",
        "docs_ru/proof-snapshot.md",
    ]
    problems = [f"missing {rel}" for rel in required if not (root / rel).exists()]
    if not problems:
        payload = load_json(root / ".vcp" / "proof-counts.json")
        if payload.get("version") != repo_version(root):
            problems.append("proof counts version mismatch")
        if "canonical counted snapshot" not in payload.get("canonical_policy", ""):
            problems.append("proof counts canonical policy missing")
        for rel in ("README.md", "README_ru.md", "docs/proof-snapshot.md", "docs_ru/proof-snapshot.md"):
            if ".vcp/proof-counts.json" not in _text(root, rel):
                problems.append(f"{rel} missing canonical proof-counts link")
    return {
        "id": "proof-counts",
        "status": "pass" if not problems else "fail",
        "summary": "Canonical proof count snapshot exists and public proof surfaces point to it.",
        "details": problems or ["Proof count synchronization is present."],
    }


def _evaluator_surface_check(root: Path) -> dict[str, Any]:
    required = [
        "EVALUATE_THIS_REPO.md",
        ".vcp/evaluator-pack.json",
        "docs/benchmark-report.md",
        "docs/trust-check.md",
        "docs/current-limitations.md",
        "docs/route-recommender.md",
        "docs/control-scorecard.md",
        "docs/evidence-bundle.md",
        "docs/pr-readiness.md",
        "docs/integrations/proof-matrix.md",
        "docs/agent-model-routing.md",
        "docs/evaluator-token-budget.md",
        "docs/visuals.md",
    ]
    missing = [f"missing {rel}" for rel in required if not (root / rel).exists()]
    return {
        "id": "evaluator-surfaces",
        "status": "pass" if not missing else "fail",
        "summary": "Evaluator shortcut, token-budget docs, route/proof surfaces, and machine-readable evaluator pack exist.",
        "details": missing or ["Evaluator-proof surfaces are present."],
    }


def _agent_kits_check(root: Path) -> dict[str, Any]:
    problems = []
    for rel in [
        "docs/integrations/setup-playbook.md",
        "docs_ru/integration-setup.md",
        "docs/integrations/agent-kits.md",
        "docs_ru/agent-kits.md",
        ".vcp/agent-kits.json",
        "templates/agents/COPILOT_INSTRUCTIONS.md",
        "ci-examples/github-actions/vcp-pr-gate.yml",
    ]:
        if not (root / rel).exists():
            problems.append(f"missing {rel}")
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
        if "official plugin" in rel:
            continue
        if (
            "not official plugin" not in text
            and "not official plugins" not in text
            and "Это не official plugins" not in text
            and "не official plugin" not in text
        ):
            problems.append(f"{rel} must state the not-official-plugin boundary")
    return {
        "id": "agent-kits",
        "status": "pass" if not problems else "fail",
        "summary": "Copy-ready AI tool agent kits, setup docs, safe export registry, and no-overclaim boundaries exist.",
        "details": problems or ["Agent kit docs, templates, registry, and boundaries are present and valid."],
    }


def _client_adoption_rollout_check(root: Path) -> dict[str, Any]:
    return _bundle_check(
        root,
        "client-adoption-rollout",
        "Client/team adoption playbook, rollout offers, and delivery surfaces exist.",
        [
            "START_HERE.md",
            "docs/client-adoption-playbook.md",
            "docs/consulting-offers.md",
            "docs/client-discovery.md",
            "docs/technical-intake-workshop.md",
            "docs/track-selection-for-clients.md",
            "docs/customer-repo-scaffold.md",
            "docs/executive-reporting.md",
            "docs_ru/client-adoption-playbook.md",
            "docs_ru/consulting-offers.md",
            "docs_ru/client-discovery.md",
            "docs_ru/technical-intake-workshop.md",
            "docs_ru/track-selection-for-clients.md",
            "docs_ru/customer-repo-scaffold.md",
            "docs_ru/executive-reporting.md",
        ],
        needles={
            "START_HERE.md": ["I do not know which VCP path to choose", "I need to prepare a PR", "AI already created chaos in my repo"],
            "docs/client-adoption-playbook.md": ["Definition of success", "8-step flow", "docs/integrations/agent-kits.md"],
        },
    )


def _control_catalog_check(root: Path) -> dict[str, Any]:
    problems = validate_catalog(root)
    return {
        "id": "control-catalog",
        "status": "pass" if not problems else "fail",
        "summary": "Control catalog docs and machine-readable catalog exist and catalog entries validate.",
        "details": problems or ["Control catalog surfaces are present and valid."],
    }


def _ecosystem_governance_check(root: Path) -> dict[str, Any]:
    return _bundle_check(
        root,
        "ecosystem-governance",
        "AI ecosystem watchlist, model/tool governance, stack adoption, training, and scouting workflow surfaces exist.",
        [
            "docs/ai-ecosystem-watchlist.md",
            "docs_ru/ai-ecosystem-watchlist.md",
            ".vcp/ai-ecosystem-watchlist.json",
            "docs/model-tool-governance.md",
            "docs_ru/model-tool-governance.md",
            "schemas/model-tool-dependency.schema.json",
            ".vcp/model-tool-dependencies.example.json",
            "templates/reports/model-tool-dependency-review.md",
            "docs/secure-agent-training-pack.md",
            "docs_ru/secure-agent-training-pack.md",
            "templates/training/secure-agent-exercises.md",
            ".vcp/secure-agent-training-pack.json",
            "docs/github-native-control-checklist.md",
            "docs_ru/github-native-control-checklist.md",
            "templates/reports/github-native-control-checklist.md",
            ".vcp/github-native-control-checklist.example.json",
            "docs/ai-stack-adoption-checklist.md",
            "docs_ru/ai-stack-adoption-checklist.md",
            "templates/reports/ai-stack-adoption-checklist.md",
            ".vcp/ai-stack-adoption-checklist.example.json",
            "docs/team-enablement-pack.md",
            "docs_ru/team-enablement-pack.md",
            "templates/training/team-enablement-plan.md",
            ".vcp/team-enablement-pack.json",
            "docs/ecosystem-scouting-workflow.md",
            "docs_ru/ecosystem-scouting-workflow.md",
            "templates/reports/ecosystem-scouting-note.md",
            ".vcp/ecosystem-scouting-workflow.json",
        ],
        needles={
            "README.md": [
                "AI Ecosystem Watchlist",
                "Model / Tool Dependency Governance",
                "VCP does not ship external models/tools",
            ],
            "README_ru.md": [
                "AI Ecosystem Watchlist",
                "Model / Tool Dependency Governance",
                "VCP не поставляет внешние модели/tools",
            ],
            "START_HERE.md": [
                "I want to evaluate an AI tool/model/stack before adopting it",
                "I want to train my team for safer AI coding",
            ],
            "docs_ru/README.md": [
                "AI ecosystem governance в VCP",
            ],
        },
    )


def _integration_proof_check(root: Path) -> dict[str, Any]:
    required = [
        "docs/integrations/proof-matrix.md",
        "docs_ru/integration-proof-matrix.md",
        ".vcp/integration-proof-matrix.json",
    ]
    problems = [f"missing {rel}" for rel in required if not (root / rel).exists()]
    if not problems:
        matrix = load_json(root / ".vcp" / "integration-proof-matrix.json")
        ids = {item.get("id") for item in matrix.get("items", [])}
        if ids != {"claude", "codex", "cursor", "copilot", "github-actions"}:
            problems.append("integration proof matrix must include claude/codex/cursor/copilot/github-actions")
    return {
        "id": "integration-proof-matrix",
        "status": "pass" if not problems else "fail",
        "summary": "Integration proof matrix exists and covers all five shipped copy-ready kits.",
        "details": problems or ["Integration proof matrix is present and complete."],
    }


def _visual_layer_check(root: Path) -> dict[str, Any]:
    required = [
        "docs/visuals.md",
        "docs_ru/visuals.md",
        "assets/diagrams/vcp-route-selector.svg",
        "assets/diagrams/vcp-evidence-bundle.svg",
        "assets/diagrams/vcp-pr-readiness-flow.svg",
        "assets/diagrams/vcp-release-decision-matrix.svg",
        "assets/diagrams/vcp-anti-chaos-recovery.svg",
    ]
    return _bundle_check(
        root,
        "visual-proof-layer",
        "Visual proof layer exists and ships SVG diagrams for route, evidence, PR flow, release, and recovery.",
        required,
    )


def _release_doc_check(root: Path) -> dict[str, Any]:
    current = repo_version(root)
    required = [f"docs/release-{current}.md", f"docs_ru/release-{current}.md"]
    return _bundle_check(root, "release-docs", "English and Russian release notes exist for the current package version.", required)


def _current_limitations_check(root: Path) -> dict[str, Any]:
    return _bundle_check(
        root,
        "current-limitations",
        "Current limitations exist in English and Russian and keep local-first boundaries explicit.",
        ["docs/current-limitations.md", "docs_ru/current-limitations.md", "docs/scope-boundary.md", "docs_ru/scope-boundary.md"],
        needles={
            "docs/current-limitations.md": ["local-first", "not SaaS", "no public PyPI/npm publication yet"],
            "docs_ru/current-limitations.md": ["VCP специально остаётся local-first.", "Это не SaaS", "VCP не создаёт PR автоматически"],
        },
    )


def _route_recommender_check(root: Path) -> dict[str, Any]:
    return _bundle_check(
        root,
        "route-recommender",
        "Route recommender docs, JSON, schema, and example exist for common project scenarios.",
        [
            "docs/route-recommender.md",
            "docs_ru/route-recommender.md",
            ".vcp/route-recommender.json",
            "schemas/route-recommendation.schema.json",
            ".vcp/route-recommendation.example.json",
        ],
    )


def _guided_modes_check(root: Path) -> dict[str, Any]:
    return _bundle_check(
        root,
        "guided-adoption-modes",
        "Guided adoption modes exist for 5-minute, 30-minute, half-day, and full-audit onboarding.",
        ["docs/guided-adoption-modes.md", "docs_ru/guided-adoption-modes.md", ".vcp/guided-adoption-modes.json"],
    )


def _scorecard_check(root: Path) -> dict[str, Any]:
    return _bundle_check(
        root,
        "control-scorecard",
        "Control scorecard docs, template, schema, and example exist as a local heuristic readiness view.",
        [
            "docs/control-scorecard.md",
            "docs_ru/control-scorecard.md",
            "templates/reports/control-scorecard.md",
            "schemas/control-scorecard.schema.json",
            ".vcp/control-scorecard.example.json",
        ],
    )


def _evidence_bundle_check(root: Path) -> dict[str, Any]:
    return _bundle_check(
        root,
        "evidence-bundle",
        "Evidence bundle docs, template, schema, and example exist as a portable proof pack.",
        [
            "docs/evidence-bundle.md",
            "docs_ru/evidence-bundle.md",
            "templates/reports/evidence-bundle.md",
            "schemas/evidence-bundle.schema.json",
            ".vcp/evidence-bundle.example.json",
        ],
    )


def _release_matrix_check(root: Path) -> dict[str, Any]:
    return _bundle_check(
        root,
        "release-decision-matrix",
        "Release decision matrix docs, template, schema, and example exist without claiming release guarantees.",
        [
            "docs/release-decision-matrix.md",
            "docs_ru/release-decision-matrix.md",
            "templates/reports/release-decision-matrix.md",
            "schemas/release-decision-matrix.schema.json",
            ".vcp/release-decision-matrix.example.json",
        ],
    )


def _anti_chaos_check(root: Path) -> dict[str, Any]:
    return _bundle_check(
        root,
        "anti-chaos-recovery-kit",
        "Anti-chaos recovery kit exists as a human-led recovery path, not an automated cleanup engine.",
        [
            "docs/anti-chaos-recovery-kit.md",
            "docs_ru/anti-chaos-recovery-kit.md",
            "templates/reports/anti-chaos-recovery-plan.md",
            ".vcp/workflows/anti-chaos-recovery.json",
        ],
    )


def _pr_readiness_check(root: Path) -> dict[str, Any]:
    return _bundle_check(
        root,
        "pr-readiness-pack",
        "PR readiness docs, templates, schema, and example exist without auto-PR or auto-merge claims.",
        [
            "docs/pr-readiness.md",
            "docs_ru/pr-readiness.md",
            "docs/integrations/github-pr-gate.md",
            "docs_ru/github-pr-gate.md",
            "templates/reports/pr-readiness-checklist.md",
            "templates/reports/pr-handoff.md",
            "templates/reports/pr-evidence-summary.md",
            "schemas/pr-readiness.schema.json",
            ".vcp/pr-readiness.example.json",
        ],
    )


def _mode_packs_check(root: Path) -> dict[str, Any]:
    return _bundle_check(
        root,
        "ai-tool-mode-packs",
        "AI tool mode packs exist for Claude Code, Codex, Cursor, and GitHub Copilot.",
        ["docs/ai-tool-mode-packs.md", "docs_ru/ai-tool-mode-packs.md", ".vcp/ai-tool-mode-packs.json"],
    )


def _evaluation_status_check(root: Path) -> dict[str, Any]:
    return _bundle_check(
        root,
        "evaluation-status-badges",
        "Evaluation status badges exist as honest labels, not certificates or guarantees.",
        ["docs/evaluation-status-badges.md", "docs_ru/evaluation-status-badges.md", ".vcp/evaluation-status-badges.json"],
    )


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
    return {
        "id": "changelog-hygiene",
        "status": "pass" if not details else "fail",
        "summary": "CHANGELOG starts with a heading and lists the current release first.",
        "details": details or [f"CHANGELOG begins with '# Changelog' and lists {current} first."],
    }


def payload(root: Path | None = None) -> dict[str, Any]:
    root = repo_root(root)
    current = repo_version(root)
    checks: list[dict[str, Any]] = []

    for check_id, command, summary in SCRIPT_CHECKS:
        checks.append(_script_check(root, check_id, command, summary))
    checks.append(_evaluator_surface_check(root))
    checks.append(_proof_counts_check(root))
    checks.append(_current_limitations_check(root))
    checks.append(_route_recommender_check(root))
    checks.append(_guided_modes_check(root))
    checks.append(_scorecard_check(root))
    checks.append(_evidence_bundle_check(root))
    checks.append(_release_matrix_check(root))
    checks.append(_anti_chaos_check(root))
    checks.append(_pr_readiness_check(root))
    checks.append(_integration_proof_check(root))
    checks.append(_mode_packs_check(root))
    checks.append(_visual_layer_check(root))
    checks.append(_evaluation_status_check(root))
    checks.append(_agent_kits_check(root))
    checks.append(_client_adoption_rollout_check(root))
    checks.append(_control_catalog_check(root))
    checks.append(_ecosystem_governance_check(root))
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
