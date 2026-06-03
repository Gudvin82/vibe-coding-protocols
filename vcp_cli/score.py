from __future__ import annotations

from datetime import date

from .utils import manifest_paths, print_output, repo_root, relative_to_root


def manifest_relpaths() -> list[str]:
    root = repo_root()
    return [relative_to_root(root, path) for path in manifest_paths(root).values()]


CATEGORY_RULES = [
    (
        "Repository evaluation guidance",
        [
            "AI_EVALUATION_GUIDE.md",
            "templates/prompts/evaluate-vcp-repository.md",
            "templates/reports/vcp-repository-evaluation-report.md",
        ],
    ),
    (
        "LLM citation and AI-agent entry",
        ["AGENTS.md", "llms.txt", "llms-full.txt", "ai.txt", "CITATION.cff", "ADOPTERS.md"],
    ),
    (
        "Foundation and trust docs",
        [
            "README.md",
            "README_ru.md",
            "docs/product-delivery-lifecycle.md",
            "docs/flagship-workflows.md",
            "docs/review-diff.md",
            "docs/score-badge.md",
            "docs/github-action.md",
            "docs/case-study-guidelines.md",
        ],
    ),
    (
        "Progressive disclosure and cards",
        [
            ".vcp/index.json",
            ".vcp/cards/README.md",
            "schemas/vcp-card.schema.json",
            "docs/progressive-disclosure.md",
            "docs/vcp-cards.md",
            "docs/vcp-mappings.md",
            "docs/platforms/README.md",
            "vcp_cli/index_cmd.py",
            "vcp_cli/cards.py",
        ],
    ),
    (
        "Spec lane",
        [
            "protocols/spec-driven/README.md",
            "protocols/spec-driven/product-brief-to-prd.md",
            "protocols/spec-driven/feature-spec.md",
            "protocols/spec-driven/spec-review.md",
            "protocols/spec-driven/spec-to-tasks.md",
            "protocols/spec-driven/spec-change-control.md",
            "templates/specs/PRD.md",
            "templates/specs/FEATURE_SPEC.md",
            "templates/specs/ACCEPTANCE_CRITERIA.md",
            "templates/specs/TASKS.md",
            "templates/specs/SPEC_REVIEW.md",
            "commands/spec-intake.md",
            "commands/spec-review.md",
            "commands/spec-to-tasks.md",
            "vcp_cli/spec_cmd.py",
        ],
    ),
    (
        "Adaptive spec depth and presets",
        [
            "docs/adaptive-spec-depth.md",
            "docs/spec-escape-hatch.md",
            "docs/question-engine.md",
            "docs/spec-retrofit.md",
            "docs/spec-freshness.md",
            "docs/packs-and-presets.md",
            "protocols/spec-driven/adaptive-spec-depth.md",
            "protocols/spec-driven/spec-escape-hatch.md",
            "protocols/spec-driven/question-engine.md",
            "protocols/spec-driven/spec-retrofit.md",
            "protocols/spec-driven/spec-freshness.md",
            ".vcp/presets/README.md",
            "schemas/vcp-preset.schema.json",
            "vcp_cli/preset_cmd.py",
        ],
    ),
    (
        "Workflow layer",
        ["docs/workflows.md", ".vcp/workflows/README.md", "schemas/vcp-workflow.schema.json", "vcp_cli/workflow_cmd.py"],
    ),
    (
        "Diagnostics layer",
        ["docs/diagnostics.md", ".vcp/diagnostics/README.md", ".vcp/diagnostics/layers.json", "templates/reports/diagnostic-report.md", "vcp_cli/diagnose.py"],
    ),
    ("Catalog UX", ["docs/catalog.md", ".vcp/catalog.json", "docs/vcp-cards.md", "vcp_cli/cards.py"]),
    (
        "AI platform coverage",
        [
            "docs/platforms/README.md",
            "docs/platforms/claude-code.md",
            "docs/platforms/codex-cli.md",
            "docs/platforms/aider.md",
            ".vcp/cards/platforms/claude-code.json",
            ".vcp/cards/platforms/codex-cli.json",
            ".vcp/cards/platforms/ollama-local-coding.json",
            "benchmarks/ai-adoption/scenarios/platform-25-plus-coverage.json",
        ],
    ),
    ("Event schema", ["docs/event-schema.md", "schemas/vcp-event.schema.json", "templates/reports/vcp-event-entry.md"]),
    ("AI Intake readiness", ["AI_INTAKE.md", "docs/target-project-classifier.md"]),
    ("Route classifier", ["docs/protocol-index.md", "docs/route-map.md"]),
    ("Adoption packs", ["docs/adoption-packs.md", ".vcp/manifests/adoption-packs.manifest.json"]),
    ("Third-party API intake / registry", ["protocols/integrations/third-party-api-intake.md", "templates/THIRD_PARTY_REGISTRY.md", "templates/reports/third-party-api-intake-report.md"]),
    ("Operations feedback loop", ["protocols/operations/production-error-capture.md", "protocols/operations/daily-error-triage.md", "docs/production-observability.md", "docs/automation-guidance.md"]),
    ("Post-task review gate", ["protocols/review/post-task-code-review.md", "commands/loop-code-review.md"]),
    ("Project Backlog", ["PROJECT_BACKLOG.md", "templates/PROJECT_BACKLOG.md", "docs/project-backlog.md", "commands/backlog-update.md", "vcp_cli/backlog.py", "examples/backlog/README.md", "protocols/operations/daily-error-triage.md", "protocols/review/post-task-code-review.md"]),
    ("Public growth and AI visibility", ["protocols/public-growth/public-growth-playbook.md", "protocols/public-growth/seo-geo-ai-visibility.md", "docs/geo-ai-visibility.md", "docs/page-templates.md", "templates/public-growth/public-growth-checklist.md", "examples/public-growth/README.md"]),
    ("Protocol index", ["docs/protocol-index.md"]),
    ("Manifests", manifest_relpaths()),
    ("CLI status", ["docs/cli.md", "docs/windows.md", "docs/npm.md", "docs/install.md", "docs/init.md", "vcp_cli/cli.py", "bin/vcp-node.js"]),
    ("Evaluation surfaces", ["docs/scoring.md", "docs/public-proof-roadmap.md", "docs/faq.md", "docs/comparison.md", "docs/anti-patterns.md", "docs/quickstart-walkthrough.md", "docs/demo-script.md", "case-studies/README.md", "vcp_cli/evaluate.py"]),
    ("Installation and terminology docs", ["docs/install.md", "docs/glossary.md"]),
    ("Validation scripts", ["scripts/check-newlines.py", "scripts/check-toolkit.sh", "scripts/validate-links.sh"]),
    ("Markdown readability", ["docs/markdown-style.md"]),
    ("Security posture docs", ["docs/security-methodology-scope.md", "docs/security-tooling-landscape.md"]),
    ("Public-site readiness", ["docs/public-site-readiness.md", "docs/seo-ai-crawler-readiness.md"]),
    ("Examples and benchmarks", ["benchmarks/ai-adoption/README.md", "examples/integrations/README.md", "docs/measured-impact.md"]),
    ("Release discipline", ["docs/release-checklist.md", "docs/release-v0.6.1.md", "ci-examples/github-actions/vcp-check.yml"]),
    ("Community readiness", ["docs/community-feedback.md", "CONTRIBUTING.md"]),
]

WARNINGS = [
    "Historical API_KEY marker warning may still appear in git history.",
    "Historical SECRET marker warning may still appear in git history.",
    "Public root AGENTS.md remains intentionally visible.",
    "Public root PROJECT_MAP.md remains intentionally visible.",
    "Readability warnings remain for docs/migration/README.md and templates/ARCHITECTURE_SOURCE_OF_TRUTH.md.",
]


def _score_status(score: int) -> tuple[str, str]:
    if score >= 90:
        return "pass", "brightgreen"
    if score >= 75:
        return "warn", "yellow"
    return "fail", "red"


def _build_payload() -> dict[str, object]:
    root = repo_root()
    categories = []
    score = 0
    per_category = 100 / len(CATEGORY_RULES)
    for name, files in CATEGORY_RULES:
        missing = [rel for rel in files if not (root / rel).exists()]
        status = "PASS" if not missing else "FAIL"
        if status == "PASS":
            score += per_category
        categories.append({"name": name, "status": status, "missing": missing})
    payload = {
        "score": round(score),
        "categories": categories,
        "warnings": WARNINGS,
        "next_recommended_improvements": [
            "Reduce remaining markdown readability warnings.",
            "Add authenticated GitHub Release publishing when tooling is available.",
            "Keep Python CLI, npm wrapper and manifest validation in CI.",
            "Add real external proof layers before claiming public-standard maturity.",
        ],
    }
    status, color = _score_status(payload["score"])
    payload["status"] = status
    payload["badge"] = f"https://img.shields.io/badge/VCP_score-{payload['score']}%2F100-{color}"
    payload["checked_at"] = str(date.today())
    return payload


def run(json_mode: bool = False, badge_mode: str | None = None) -> int:
    payload = _build_payload()
    if json_mode:
        print_output(payload, True)
    elif badge_mode == "json":
        print_output(
            {
                "score": payload["score"],
                "status": payload["status"],
                "badge": payload["badge"],
                "checked_at": payload["checked_at"],
                "note": "Local readiness score only; not a security certification.",
            },
            True,
        )
    elif badge_mode == "markdown":
        print(f"![VCP Score]({payload['badge']})")
    elif badge_mode == "text":
        print(f"**VCP Score:** {payload['score']}/100")
        print(f"**Status:** {payload['status']}")
        print(f"**Last checked:** {payload['checked_at']}")
        print(f"**Badge:** {payload['badge']}")
        print("This is a local readiness signal, not a security certification.")
    else:
        print(f"Score: {payload['score']}/100")
        for category in payload["categories"]:
            print(f"- {category['name']}: {category['status']}")
        if payload["warnings"]:
            print("Warnings:")
            for warning in payload["warnings"]:
                print(f"- {warning}")
    return 0
