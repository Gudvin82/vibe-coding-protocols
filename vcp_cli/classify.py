from __future__ import annotations

from pathlib import Path
from typing import Any

from .utils import print_output, project_root

PACKAGE_MARKERS = [
    "pyproject.toml",
    "package.json",
    "requirements.txt",
    "go.mod",
    "Cargo.toml",
    "Gemfile",
    "composer.json",
]

PROJECT_MEMORY_MARKERS = [
    "AGENTS.md",
    "PROJECT_MAP.md",
    "PROJECT_BACKLOG.md",
    "ARCHITECTURE_SOURCE_OF_TRUTH.md",
]

SPEC_MARKERS = [
    "docs/spec-foundation.md",
    "docs/spec-quality-gate.md",
    "templates/specs/PRODUCT_BRIEF.md",
    "templates/specs/PRD.md",
    "templates/specs/FEATURE_SPEC.md",
]

PUBLIC_GROWTH_MARKERS = [
    "llms.txt",
    "llms-full.txt",
    "ai.txt",
    "docs/public-growth/seo-geo-ai-structure-evaluation.md",
    "docs/public-growth/README.md",
]

SENSITIVE_NAME_HINTS = (
    "auth",
    "login",
    "oauth",
    "payment",
    "billing",
    "invoice",
    "secret",
    "token",
    "security",
    "privacy",
    "personal-data",
    "gdpr",
)

CODE_DIR_HINTS = ("src", "app", "lib", "server", "client", "api", "vcp_cli")


def _scan_sensitive_paths(root: Path) -> list[str]:
    hits: list[str] = []
    for path in root.rglob("*"):
        if len(hits) >= 8:
            break
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix().lower()
        if any(part in rel for part in SENSITIVE_NAME_HINTS):
            hits.append(path.relative_to(root).as_posix())
    return sorted(set(hits))


def classify_payload(root: Path | None = None) -> dict[str, Any]:
    root = project_root(root)
    package_files = [rel for rel in PACKAGE_MARKERS if (root / rel).exists()]
    project_memory_files = [rel for rel in PROJECT_MEMORY_MARKERS if (root / rel).exists()]
    spec_files = [rel for rel in SPEC_MARKERS if (root / rel).exists()]
    public_growth_files = [rel for rel in PUBLIC_GROWTH_MARKERS if (root / rel).exists()]
    ci_files = []
    if (root / ".github/workflows").exists():
        ci_files = [p.relative_to(root).as_posix() for p in sorted((root / ".github/workflows").glob("*.yml"))]
    code_dirs = [name for name in CODE_DIR_HINTS if (root / name).exists()]
    sensitive_hits = _scan_sensitive_paths(root)

    has_existing_repo = bool(package_files or code_dirs or ci_files)
    has_spec_lane = bool(spec_files)
    has_public_growth = bool(public_growth_files)
    has_project_memory = bool(project_memory_files)
    has_sensitive_scope = bool(sensitive_hits)
    has_release_surface = (root / "CHANGELOG.md").exists() and any((root / "docs").glob("release-v*.md"))

    if not has_existing_repo and has_spec_lane:
        project_type = "idea-stage"
        track = "New Project Track"
        risk = "low"
        suggested_tier = "Lite"
        suggested_route = "spec-first"
    elif has_sensitive_scope:
        project_type = "governed-production-repo"
        track = "Existing Project Track"
        risk = "high"
        suggested_tier = "Governed"
        suggested_route = "production"
    elif has_existing_repo and (has_project_memory or has_release_surface or ci_files):
        project_type = "shared-repository"
        track = "Existing Project Track"
        risk = "medium"
        suggested_tier = "Team"
        suggested_route = "brownfield-rescue"
    elif has_existing_repo:
        project_type = "working-repository"
        track = "Existing Project Track"
        risk = "medium"
        suggested_tier = "Lite"
        suggested_route = "existing-mvp"
    else:
        project_type = "new-project-repo"
        track = "New Project Track"
        risk = "low"
        suggested_tier = "Lite"
        suggested_route = "new-project"

    if has_public_growth and suggested_tier == "Lite" and track == "Existing Project Track":
        suggested_route = "public-growth"

    limitations = [
        "Classification is repository-shape based; it does not inspect runtime traffic or hidden business constraints.",
        "Sensitive scope detection relies on visible filenames and may under-report domain risk.",
    ]

    payload = {
        "project_type": project_type,
        "track": track,
        "risk": risk,
        "suggested_tier": suggested_tier,
        "suggested_route": suggested_route,
        "confidence": "medium" if sensitive_hits else "high",
        "signals": {
            "scanned_root": root.as_posix(),
            "package_files": package_files,
            "project_memory_files": project_memory_files,
            "spec_files": spec_files,
            "public_growth_files": public_growth_files,
            "ci_files": ci_files,
            "code_dirs": code_dirs,
            "sensitive_hits": sensitive_hits,
        },
        "limitations": limitations,
    }
    return payload


def run(json_mode: bool = False) -> int:
    payload = classify_payload()
    if json_mode:
        print_output(payload, True)
    else:
        print(f"Project type: {payload['project_type']}")
        print(f"Track: {payload['track']}")
        print(f"Risk: {payload['risk']}")
        print(f"Suggested tier: {payload['suggested_tier']}")
        print(f"Suggested route: {payload['suggested_route']}")
        print(f"Confidence: {payload['confidence']}")
    return 0
