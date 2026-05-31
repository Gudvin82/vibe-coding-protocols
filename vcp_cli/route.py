from __future__ import annotations

from .utils import print_output

ROUTES = {
    "new-project": {
        "selected_route": "Starter Protocol",
        "adoption_pack": "new-project",
        "confidence": "High",
        "required_files_to_inspect": ["START_HERE.md", "protocols/ai-project-starter-protocol.md", "templates/AGENTS.md"],
        "first_safe_action": "Create or refine Product Brief and PROJECT_MAP before implementation.",
        "stop_conditions": ["Existing production code already exists", "Sensitive production behavior is already live"],
        "validation_commands": ["bash scripts/vibe-check.sh --starter"],
        "post_task_review_gate": "Recommended for meaningful code changes before merge.",
    },
    "existing-mvp": {
        "selected_route": "Hardening Light or Standard",
        "adoption_pack": "existing-mvp",
        "confidence": "High",
        "required_files_to_inspect": ["AI_INTAKE.md", "docs/adoption-packs.md", "protocols/ai-project-hardening-protocol.md"],
        "first_safe_action": "Map risk areas and third-party dependencies before new feature work.",
        "stop_conditions": ["Users or payments already exist", "No validation path exists"],
        "validation_commands": ["bash scripts/vibe-check.sh --hardening"],
        "post_task_review_gate": "Run for meaningful changes before merge.",
    },
    "production": {
        "selected_route": "Full Hardening",
        "adoption_pack": "production",
        "confidence": "High",
        "required_files_to_inspect": ["AI_INTAKE.md", "docs/adoption-packs.md", "templates/reports/security-review-scope.md", "protocols/review/post-task-code-review.md"],
        "first_safe_action": "Confirm production risk map, security scope and release gate before code changes.",
        "stop_conditions": ["Auth, payments or personal data changed without explicit scope", "No validation path exists"],
        "validation_commands": ["bash scripts/vibe-check.sh --audit --json", "python3 -m vcp_cli review plan --json"],
        "post_task_review_gate": "Required before merge, release or deploy.",
    },
    "regulated": {
        "selected_route": "Full Hardening + Security Review Scope",
        "adoption_pack": "regulated",
        "confidence": "High",
        "required_files_to_inspect": ["templates/reports/security-review-scope.md", "protocols/review/post-task-code-review.md", "docs/security-methodology-scope.md"],
        "first_safe_action": "Lock review scope and escalation path before modifying sensitive flows.",
        "stop_conditions": ["Human review is unavailable", "Sensitive data or payments are touched without validation"],
        "validation_commands": ["bash scripts/vibe-check.sh --audit --json", "python3 -m vcp_cli review plan --json"],
        "post_task_review_gate": "Required with independent review plus validation.",
    },
    "shared-engine": {
        "selected_route": "Full Hardening + Shared Engine / Multi-product",
        "adoption_pack": "shared-engine",
        "confidence": "High",
        "required_files_to_inspect": ["AI_INTAKE.md", "PROJECT_MAP.md", "templates/ARCHITECTURE_SOURCE_OF_TRUTH.md", "protocols/review/post-task-code-review.md"],
        "first_safe_action": "Create or update PROJECT_MAP and Architecture Source of Truth before changing shared engine code.",
        "stop_conditions": ["Cross-product regression risk is unvalidated", "One product path is missing from validation"],
        "validation_commands": ["bash scripts/vibe-check.sh --audit --json", "python3 -m vcp_cli benchmark run --scenario shared-engine-production"],
        "post_task_review_gate": "Required before the next feature, merge or release.",
    },
    "maintenance": {
        "selected_route": "Maintenance Refactoring",
        "adoption_pack": "maintenance",
        "confidence": "High",
        "required_files_to_inspect": ["protocols/maintenance/care-refactoring.md", "templates/reports/refactoring-report.md", "protocols/review/post-task-code-review.md"],
        "first_safe_action": "Choose one small behavior-preserving refactor scope.",
        "stop_conditions": ["Public contract change is required", "No characterization or validation path exists"],
        "validation_commands": ["python3 -m vcp_cli review plan --json"],
        "post_task_review_gate": "Required after the refactoring slice.",
    },
    "ui-ownership": {
        "selected_route": "UI Component Ownership",
        "adoption_pack": "ui-ownership",
        "confidence": "High",
        "required_files_to_inspect": ["protocols/maintenance/ui-refactoring.md", "templates/reports/ui-refactoring-report.md", "protocols/review/post-task-code-review.md"],
        "first_safe_action": "Choose one visual ownership slice and preserve behavior.",
        "stop_conditions": ["You are redesigning the whole system", "Accessibility behavior is changing without validation"],
        "validation_commands": ["python3 -m vcp_cli review plan --json"],
        "post_task_review_gate": "Required after meaningful UI extraction or ownership cleanup.",
    },
    "public-site": {
        "selected_route": "Public Site Readiness",
        "adoption_pack": "public-site",
        "confidence": "High",
        "required_files_to_inspect": ["docs/public-site-readiness.md", "docs/seo-ai-crawler-readiness.md", "llms.txt"],
        "first_safe_action": "Check canonical docs, trust links and publishing checklist before shipping site changes.",
        "stop_conditions": ["Visible content and structured data diverge", "No publish-safe validation path exists"],
        "validation_commands": ["python3 scripts/check-newlines.py", "python3 scripts/validate-links.sh"],
        "post_task_review_gate": "Use lighter review for meaningful docs or config changes.",
    },
    "post-task-review": {
        "selected_route": "Post-Task Code Review",
        "adoption_pack": "post-task-review",
        "confidence": "High",
        "required_files_to_inspect": ["protocols/review/post-task-code-review.md", "commands/loop-code-review.md", "templates/reports/code-review-report.md"],
        "first_safe_action": "Inspect active git changes and collect validation output before requesting independent review.",
        "stop_conditions": ["Validation is red", "Independent reviewer path is unavailable for sensitive changes"],
        "validation_commands": ["python3 -m vcp_cli review plan --json", "python3 -m vcp_cli check --fast"],
        "post_task_review_gate": "This route is the gate itself.",
    },
}


def run(profile: str, json_mode: bool = False) -> int:
    if profile not in ROUTES:
        print(f"Unknown profile: {profile}", flush=True)
        return 1
    data = {"profile": profile, **ROUTES[profile]}
    if json_mode:
        print_output(data, True)
    else:
        print(f"Profile: {profile}")
        print(f"Route: {data['selected_route']}")
        print(f"Adoption pack: {data['adoption_pack']}")
        print(f"Confidence: {data['confidence']}")
        print(f"First action: {data['first_safe_action']}")
        print(f"Review gate: {data['post_task_review_gate']}")
    return 0
