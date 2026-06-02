from __future__ import annotations

from .utils import print_output

ROUTES = {
    "new-project": {
        "selected_route": "Starter Protocol",
        "manifest_route_id": "starter",
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
        "manifest_route_id": "hardening-light",
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
        "manifest_route_id": "hardening-full",
        "adoption_pack": "production",
        "confidence": "High",
        "required_files_to_inspect": ["AI_INTAKE.md", "docs/adoption-packs.md", "templates/reports/security-review-scope.md", "protocols/review/post-task-code-review.md"],
        "first_safe_action": "Confirm production risk map, security scope and release gate before code changes.",
        "stop_conditions": ["Auth, payments or personal data changed without explicit scope", "No validation path exists"],
        "validation_commands": ["python3 -m vcp_cli check --fast --json", "python3 -m vcp_cli review plan --json"],
        "post_task_review_gate": "Required before merge, release or deploy.",
    },
    "regulated": {
        "selected_route": "Full Hardening + Security Review Scope",
        "manifest_route_id": "hardening-full",
        "adoption_pack": "regulated",
        "confidence": "High",
        "required_files_to_inspect": ["templates/reports/security-review-scope.md", "protocols/review/post-task-code-review.md", "docs/security-methodology-scope.md", "templates/THIRD_PARTY_REGISTRY.md"],
        "first_safe_action": "Lock review scope, data path and escalation path before modifying sensitive flows.",
        "stop_conditions": ["Human review is unavailable", "Sensitive data or payments are touched without validation"],
        "validation_commands": ["python3 -m vcp_cli check --fast --json", "python3 -m vcp_cli review plan --json"],
        "post_task_review_gate": "Required with independent review plus validation.",
    },
    "shared-engine": {
        "selected_route": "Full Hardening + Shared Engine / Multi-product",
        "manifest_route_id": "hardening-full",
        "adoption_pack": "shared-engine",
        "confidence": "High",
        "required_files_to_inspect": ["AI_INTAKE.md", "PROJECT_MAP.md", "templates/ARCHITECTURE_SOURCE_OF_TRUTH.md", "templates/THIRD_PARTY_REGISTRY.md", "protocols/review/post-task-code-review.md"],
        "first_safe_action": "Create or update PROJECT_MAP and Architecture Source of Truth before changing shared engine code.",
        "stop_conditions": ["Cross-product regression risk is unvalidated", "One product path is missing from validation"],
        "validation_commands": ["python3 -m vcp_cli check --fast --json", "python3 -m vcp_cli benchmark run --scenario shared-engine-production"],
        "post_task_review_gate": "Required before the next feature, merge or release.",
    },
    "maintenance": {
        "selected_route": "Maintenance Refactoring",
        "manifest_route_id": "maintenance-refactoring",
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
        "manifest_route_id": "ui-ownership",
        "adoption_pack": "ui-ownership",
        "confidence": "High",
        "required_files_to_inspect": ["protocols/maintenance/ui-refactoring.md", "templates/reports/ui-refactoring-report.md", "protocols/review/post-task-code-review.md"],
        "first_safe_action": "Choose one visual ownership slice and preserve behavior.",
        "stop_conditions": ["You are redesigning the whole system", "Accessibility behavior is changing without validation"],
        "validation_commands": ["python3 -m vcp_cli review plan --json"],
        "post_task_review_gate": "Required after meaningful UI extraction or ownership cleanup.",
    },
    "third-party-api": {
        "selected_route": "Third-party API Intake / Integrations",
        "manifest_route_id": "third-party-api-intake",
        "adoption_pack": "third-party-api",
        "confidence": "High",
        "required_files_to_inspect": [
            "protocols/integrations/third-party-api-intake.md",
            "templates/THIRD_PARTY_REGISTRY.md",
            "templates/reports/third-party-api-intake-report.md",
            "commands/third-party-api-intake.md",
        ],
        "first_safe_action": "Classify the API, owner, auth, data flow, terms and fallback before writing integration code.",
        "stop_conditions": [
            "API key or token would be committed to code",
            "Terms, data handling or fallback are still unknown",
        ],
        "validation_commands": ["python3 -m vcp_cli check --fast --json", "python3 -m vcp_cli review plan --json"],
        "post_task_review_gate": "Required before production integration merge or release.",
    },
    "public-site": {
        "selected_route": "Public Site Readiness",
        "manifest_route_id": "public-site-readiness",
        "adoption_pack": "public-site",
        "confidence": "High",
        "required_files_to_inspect": ["docs/public-site-readiness.md", "docs/seo-ai-crawler-readiness.md", "llms.txt"],
        "first_safe_action": "Check canonical docs, trust links and publishing checklist before shipping site changes.",
        "stop_conditions": ["Visible content and structured data diverge", "No publish-safe validation path exists"],
        "validation_commands": ["python3 scripts/check-newlines.py", "python3 scripts/validate-links.sh"],
        "post_task_review_gate": "Use lighter review for meaningful docs or config changes.",
    },
    "operations": {
        "selected_route": "Operations Feedback Loop",
        "manifest_route_id": "production-error-capture",
        "adoption_pack": "operations",
        "confidence": "High",
        "required_files_to_inspect": [
            "protocols/operations/production-error-capture.md",
            "protocols/operations/daily-error-triage.md",
            "docs/production-observability.md",
            "PROJECT_BACKLOG.md",
        ],
        "first_safe_action": "Discover the documented authorized production log path before monitoring anything.",
        "stop_conditions": [
            "No documented log path exists",
            "The task would require fixing or changing production state",
        ],
        "validation_commands": ["python3 -m vcp_cli doctor", "python3 -m vcp_cli backlog validate"],
        "post_task_review_gate": "Review is required only after a separate follow-up code change starts.",
    },
    "backlog": {
        "selected_route": "Project Backlog Update",
        "manifest_route_id": "project-backlog-workflow",
        "adoption_pack": "backlog",
        "confidence": "High",
        "required_files_to_inspect": [
            "PROJECT_BACKLOG.md",
            "docs/project-backlog.md",
            "commands/backlog-update.md",
            "templates/reports/backlog-update-report.md",
        ],
        "first_safe_action": "Add or update the backlog item before implementation starts.",
        "stop_conditions": [
            "Architecture impact is cross-layer or production-critical and no doc update is possible",
            "The request would silently bypass backlog state tracking",
        ],
        "validation_commands": ["python3 -m vcp_cli backlog validate", "python3 -m vcp_cli review plan --json"],
        "post_task_review_gate": "Required once the backlog item turns into meaningful code changes.",
    },
    "post-task-review": {
        "selected_route": "Post-Task Code Review",
        "manifest_route_id": "post-task-code-review",
        "adoption_pack": "post-task-review",
        "confidence": "High",
        "required_files_to_inspect": ["protocols/review/post-task-code-review.md", "commands/loop-code-review.md", "templates/reports/code-review-report.md"],
        "first_safe_action": "Inspect active git changes and collect validation output before requesting independent review.",
        "stop_conditions": ["Validation is red", "Independent reviewer path is unavailable for sensitive changes"],
        "validation_commands": ["python3 -m vcp_cli review plan --json", "python3 -m vcp_cli check --fast --json"],
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
