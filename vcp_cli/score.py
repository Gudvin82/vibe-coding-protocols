from __future__ import annotations

from .utils import manifest_paths, print_output, repo_root, relative_to_root


def manifest_relpaths() -> list[str]:
    root = repo_root()
    return [relative_to_root(root, path) for path in manifest_paths(root).values()]


CATEGORY_RULES = [
    ("AI Intake readiness", ["AI_INTAKE.md", "docs/target-project-classifier.md"]),
    ("Route classifier", ["docs/protocol-index.md", "docs/route-map.md"]),
    ("Adoption packs", ["docs/adoption-packs.md", ".vcp/manifests/adoption-packs.manifest.json"]),
    ("Third-party API intake / registry", ["protocols/integrations/third-party-api-intake.md", "templates/THIRD_PARTY_REGISTRY.md", "templates/reports/third-party-api-intake-report.md"]),
    ("Post-task review gate", ["protocols/review/post-task-code-review.md", "commands/loop-code-review.md"]),
    ("Protocol index", ["docs/protocol-index.md"]),
    ("Manifests", manifest_relpaths()),
    ("CLI status", ["docs/cli.md", "docs/windows.md", "docs/npm.md", "docs/init.md", "vcp_cli/cli.py", "bin/vcp-node.js"]),
    ("Validation scripts", ["scripts/check-newlines.py", "scripts/check-toolkit.sh", "scripts/validate-links.sh"]),
    ("Markdown readability", ["docs/markdown-style.md"]),
    ("Security posture docs", ["docs/security-methodology-scope.md", "docs/security-tooling-landscape.md"]),
    ("Public-site readiness", ["docs/public-site-readiness.md", "docs/seo-ai-crawler-readiness.md"]),
    ("Examples and benchmarks", ["benchmarks/ai-adoption/README.md", "examples/integrations/README.md", "docs/measured-impact.md"]),
    ("Release discipline", ["docs/release-checklist.md", "docs/release-v0.5.2.md"]),
    ("Community readiness", ["docs/community-feedback.md", "CONTRIBUTING.md"]),
]

WARNINGS = [
    "Historical API_KEY marker warning may still appear in git history.",
    "Historical SECRET marker warning may still appear in git history.",
    "Public root AGENTS.md remains intentionally visible.",
    "Public root PROJECT_MAP.md remains intentionally visible.",
    "Readability warnings remain for docs/migration/README.md and templates/ARCHITECTURE_SOURCE_OF_TRUTH.md.",
]


def run(json_mode: bool = False) -> int:
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
        ],
    }
    if json_mode:
        print_output(payload, True)
    else:
        print(f"Score: {payload['score']}/100")
        for category in categories:
            print(f"- {category['name']}: {category['status']}")
        if payload["warnings"]:
            print("Warnings:")
            for warning in payload["warnings"]:
                print(f"- {warning}")
    return 0
