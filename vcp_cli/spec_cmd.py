from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any

from .utils import print_output, repo_root

TEMPLATES = {
    "prd": ("templates/specs/PRD.md", "PRD.md"),
    "feature": ("templates/specs/FEATURE_SPEC.md", "FEATURE_SPEC.md"),
    "tasks": ("templates/specs/TASKS.md", "TASKS.md"),
}

SPEC_FILES = {
    "PRD.md": ["# Product Requirements Document", "## Problem statement", "## Validation plan"],
    "FEATURE_SPEC.md": ["# Feature Spec", "## User flow", "## Validation plan"],
    "ACCEPTANCE_CRITERIA.md": ["# Acceptance Criteria", "## Acceptance criteria"],
    "TASKS.md": ["# Tasks", "## Task breakdown", "## Validation tasks"],
    "SPEC_REVIEW.md": ["# Spec Review", "## Review scope", "## Decision"],
    "SPEC_CHANGELOG.md": ["# Spec Changelog", "## Change log"],
}

NO_SPEC_KEYWORDS = {
    "typo", "copy", "copy-only", "spelling", "rename local variable", "variable rename",
    "formatting", "whitespace", "docs fix", "readme fix", "copy edit", "css tweak",
    "non-behavioral", "metadata update", "comment", "label", "heading",
}
FULL_SPEC_KEYWORDS = {
    "auth", "session", "oauth", "login", "token", "payment", "billing", "webhook",
    "database", "db", "persistence", "storage", "migration", "external api", "sdk",
    "integration", "user data", "personal data", "permissions", "rbac", "cron", "queue",
}
GOVERNED_KEYWORDS = {
    "regulated", "compliance", "production-critical", "shared engine", "shared-engine",
    "billing", "payment", "permissions", "migration", "public release", "legal", "gdpr",
    "pci", "sox", "hipaa",
}
QUESTION_BANK: list[dict[str, Any]] = [
    {
        "id": "persona",
        "question": "Who is the primary user or operator for this change?",
        "why": "Clarifies whether this is an internal tool, customer-facing feature, or ops change.",
        "options": ["Internal team (Recommended)", "External customer", "Operations/support", "Other / not sure"],
    },
    {
        "id": "problem",
        "question": "What problem should this change solve first?",
        "why": "Prevents implementation before the core problem is explicit.",
        "options": ["Fix broken behavior (Recommended)", "Improve workflow speed", "Reduce manual work", "Other / not sure"],
    },
    {
        "id": "success",
        "question": "How will we know this change worked?",
        "why": "Forces a minimum validation target.",
        "options": ["Passing validation/tests (Recommended)", "User-visible outcome", "Operational metric", "Other / not sure"],
    },
    {
        "id": "data",
        "question": "Does this touch user data, persistence, or external systems?",
        "why": "This is the main fork between spec-lite and full/governed spec.",
        "options": ["No (Recommended)", "Yes, external API", "Yes, database or user data", "Other / not sure"],
    },
    {
        "id": "constraints",
        "question": "Are there constraints that could change the route?",
        "why": "Captures deadlines, release pressure, compliance, and environment constraints.",
        "options": ["No major constraints (Recommended)", "Production deadline", "Compliance/security rules", "Other / not sure"],
    },
    {
        "id": "rollout",
        "question": "Does this need staged rollout or release coordination?",
        "why": "Helps detect governed-spec or hardening needs.",
        "options": ["No (Recommended)", "Yes, production rollout", "Yes, customer communication", "Other / not sure"],
    },
]


def _target_path(root: Path, default_name: str, output: str | None) -> Path:
    return (root / output).resolve() if output else (root / default_name)


def _backup_if_needed(path: Path) -> str | None:
    if not path.exists():
        return None
    stamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    backup = path.with_name(f"{path.name}.bak-{stamp}")
    backup.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
    return str(backup)


def _source_text(task: str | None = None, from_path: str | None = None) -> str:
    if task:
        return task.strip()
    if from_path:
        path = (repo_root() / from_path).resolve()
        if not path.exists():
            raise FileNotFoundError(f"Source file not found: {from_path}")
        return path.read_text(encoding="utf-8")
    raise ValueError("Provide --task/--idea or --from")


def _classify_spec_depth(text: str) -> dict[str, Any]:
    lowered = text.lower().strip()
    matched_governed = sorted({kw for kw in GOVERNED_KEYWORDS if kw in lowered})
    matched_full = sorted({kw for kw in FULL_SPEC_KEYWORDS if kw in lowered})
    matched_no_spec = sorted({kw for kw in NO_SPEC_KEYWORDS if kw in lowered})

    if matched_governed:
        depth = "governed-spec"
        reason = "production-critical, regulated, billing, permission, migration, or comparable release-risk signals were detected"
        required_artifacts = [
            "PRD.md",
            "FEATURE_SPEC.md",
            "ACCEPTANCE_CRITERIA.md",
            "TASKS.md",
            "SPEC_REVIEW.md",
            "PROJECT_BACKLOG.md",
            "architecture update",
            "release gate evidence",
        ]
        required_validation = [
            "architecture impact check",
            "validation plan",
            "post-task review",
            "release gate",
        ]
        stop_conditions = [
            "scope still unclear for production-critical work",
            "compliance or data boundaries still unknown",
            "release path has no validation evidence",
        ]
    elif matched_full:
        depth = "full-spec"
        reason = "cross-layer, persistence, auth, external API, or user-data signals were detected"
        required_artifacts = [
            "FEATURE_SPEC.md",
            "ACCEPTANCE_CRITERIA.md",
            "TASKS.md",
            "PROJECT_BACKLOG.md",
            "architecture impact note",
        ]
        required_validation = [
            "validation plan",
            "review gate",
        ]
        stop_conditions = [
            "external dependency is still unclassified",
            "data flow is still unknown",
            "behavior changes without validation path",
        ]
    elif matched_no_spec and len(lowered) < 180:
        depth = "no-spec"
        reason = "the task looks mechanical, local, and non-behavioral"
        required_artifacts = [
            "backlog note or short work note",
            "validation command",
        ]
        required_validation = [
            "relevant local validation",
        ]
        stop_conditions = [
            "behavior actually changes",
            "new external dependency or persistence appears",
        ]
    else:
        depth = "spec-lite"
        reason = "the task looks like a normal feature or flow change without strong governed/full-spec signals"
        required_artifacts = [
            "one-page feature brief",
            "ACCEPTANCE_CRITERIA.md",
            "validation plan",
            "PROJECT_BACKLOG.md",
        ]
        required_validation = [
            "validation plan",
            "backlog linkage",
        ]
        stop_conditions = [
            "cross-layer risk appears during clarification",
            "auth, payments, persistence, or external API scope expands",
        ]

    return {
        "recommended_spec_depth": depth,
        "reason": reason,
        "matched_signals": {
            "no_spec": matched_no_spec,
            "full_spec": matched_full,
            "governed_spec": matched_governed,
        },
        "required_artifacts": required_artifacts,
        "required_validation": required_validation,
        "stop_conditions": stop_conditions,
        "note": "Heuristic helper only. It does not guarantee perfect classification.",
    }


def template(kind: str, write: bool = False, output: str | None = None, json_mode: bool = False) -> int:
    root = repo_root()
    template_rel, default_name = TEMPLATES[kind]
    source = root / template_rel
    text = source.read_text(encoding="utf-8")
    if not write:
        if json_mode:
            print_output({"kind": kind, "template": template_rel, "write": False, "default_output": default_name, "content": text}, True)
        else:
            print(text.rstrip())
        return 0
    target = _target_path(root, default_name, output)
    backup = _backup_if_needed(target)
    target.write_text(text, encoding="utf-8")
    payload = {
        "kind": kind,
        "template": template_rel,
        "write": True,
        "target": str(target.relative_to(root)),
        "backup": backup,
    }
    print_output(payload, json_mode)
    return 0


def _inspect_spec_file(root: Path, rel: str) -> dict[str, Any]:
    path = root / rel
    if not path.exists():
        return {"file": rel, "status": "MISSING", "missing_sections": [], "evidence": "file not present"}
    text = path.read_text(encoding="utf-8")
    missing = [section for section in SPEC_FILES[rel] if section not in text]
    return {
        "file": rel,
        "status": "OK" if not missing else "WARN",
        "missing_sections": missing,
        "evidence": "present",
    }


def validate(json_mode: bool = False) -> int:
    root = repo_root()
    results = [_inspect_spec_file(root, rel) for rel in SPEC_FILES]
    ok = all(item["status"] in {"OK", "MISSING"} for item in results)
    payload = {
        "ok": ok,
        "spec_files": results,
        "templates_present": {kind: (root / template_rel).exists() for kind, (template_rel, _) in TEMPLATES.items()},
    }
    if json_mode:
        print_output(payload, True)
    else:
        for item in results:
            print(f"{item['file']}: {item['status']}")
            for section in item["missing_sections"]:
                print(f"- missing section: {section}")
    return 0 if ok else 1


def review(json_mode: bool = False) -> int:
    root = repo_root()
    items = [_inspect_spec_file(root, rel) for rel in SPEC_FILES]
    gaps = []
    for item in items:
        if item["status"] == "WARN":
            gaps.append(f"{item['file']} missing: {', '.join(item['missing_sections'])}")
        if item["status"] == "MISSING" and item["file"] in {"PRD.md", "FEATURE_SPEC.md", "ACCEPTANCE_CRITERIA.md", "TASKS.md"}:
            gaps.append(f"{item['file']} is missing for non-trivial spec-first work.")
    payload = {
        "ok": not gaps,
        "decision": "approved" if not gaps else "blocked pending spec gaps",
        "gaps": gaps,
        "next_action": "Clarify missing spec sections before implementation." if gaps else "Spec lane is ready for implementation planning.",
    }
    print_output(payload, json_mode)
    return 0 if not gaps else 1


def summary(json_mode: bool = False) -> int:
    root = repo_root()
    results = [_inspect_spec_file(root, rel) for rel in SPEC_FILES]
    present = [item["file"] for item in results if item["status"] != "MISSING"]
    payload = {
        "ok": True,
        "present": present,
        "missing": [item["file"] for item in results if item["status"] == "MISSING"],
        "warnings": [item for item in results if item["status"] == "WARN"],
        "recommended_flow": ["PRD.md", "FEATURE_SPEC.md", "ACCEPTANCE_CRITERIA.md", "TASKS.md", "SPEC_REVIEW.md"],
    }
    print_output(payload, json_mode)
    return 0


def depth(task: str | None = None, from_path: str | None = None, json_mode: bool = False) -> int:
    text = _source_text(task=task, from_path=from_path)
    payload = _classify_spec_depth(text)
    payload["source"] = {"task": task, "from": from_path}
    if json_mode:
        print_output(payload, True)
    else:
        print(f"Recommended spec depth: {payload['recommended_spec_depth']}")
        print(f"Reason: {payload['reason']}")
        print("Required artifacts:")
        for item in payload["required_artifacts"]:
            print(f"- {item}")
        print("Required validation:")
        for item in payload["required_validation"]:
            print(f"- {item}")
        print("Stop conditions:")
        for item in payload["stop_conditions"]:
            print(f"- {item}")
        print(payload["note"])
    return 0


def skip_check(task: str | None = None, reason: str | None = None, json_mode: bool = False) -> int:
    text = task or reason
    if not text:
        raise ValueError("Provide --task or --reason")
    depth_payload = _classify_spec_depth(text)
    depth_name = depth_payload["recommended_spec_depth"]
    if depth_name == "no-spec":
        status = "can_skip"
        safe = True
        explanation = "Spec can be skipped, but validation still remains required."
    elif depth_name == "spec-lite":
        status = "spec_lite_required"
        safe = False
        explanation = "A lightweight feature brief and acceptance criteria are still recommended."
    elif depth_name == "full-spec":
        status = "full_spec_required"
        safe = False
        explanation = "Risk signals are too high to skip specification safely."
    else:
        status = "governed_spec_required"
        safe = False
        explanation = "This scope is too sensitive for a spec skip path."
    payload = {
        "status": status,
        "safe_to_skip_spec": safe,
        "explanation": explanation,
        "required_validation": depth_payload["required_validation"],
        "stop_conditions": depth_payload["stop_conditions"],
        "note": "Skipping spec never means skipping validation or review when behavior changes.",
    }
    print_output(payload, json_mode)
    return 0


def questions(idea: str | None = None, from_path: str | None = None, json_mode: bool = False) -> int:
    text = _source_text(task=idea, from_path=from_path).lower()
    selected: list[dict[str, Any]] = []
    for item in QUESTION_BANK:
        if item["id"] in {"persona", "problem", "success"}:
            selected.append(item)
            continue
        if item["id"] == "data" and any(kw in text for kw in ["api", "database", "auth", "payment", "data", "webhook", "integration"]):
            selected.append(item)
        elif item["id"] == "constraints" and any(kw in text for kw in ["production", "deadline", "compliance", "security", "migration"]):
            selected.append(item)
        elif item["id"] == "rollout" and any(kw in text for kw in ["release", "rollout", "production", "launch", "public"]):
            selected.append(item)
    if len(selected) < 5:
        for item in QUESTION_BANK:
            if item not in selected:
                selected.append(item)
            if len(selected) >= 5:
                break
    payload = {
        "ok": True,
        "source": {"idea": idea, "from": from_path},
        "mode": "template-driven",
        "one_question_at_a_time": True,
        "questions": selected[:6],
        "guidance": [
            "Ask one question at a time.",
            "Use multiple-choice options first.",
            "Keep Other / not sure available.",
            "Stop when enough information exists.",
        ],
        "note": "This helper is static/template-driven. It does not call external AI APIs.",
    }
    print_output(payload, json_mode)
    return 0


def retrofit(scope: str, dry_run: bool = False, json_mode: bool = False) -> int:
    root = repo_root()
    doc_candidates = [
        rel for rel in ["README.md", "PROJECT_MAP.md", "AI_INTAKE.md", "docs/protocol-index.md", "templates/ARCHITECTURE_SOURCE_OF_TRUTH.md"]
        if (root / rel).exists()
    ]
    payload = {
        "ok": True,
        "scope": scope,
        "dry_run": dry_run,
        "mode": "guidance-only",
        "writes_source_code": False,
        "steps": [
            "Inspect available project docs.",
            "Inspect project map / architecture memory if present.",
            "Capture observed behavior for the scoped area.",
            "Write OBSERVED_SPEC.md.",
            "Write SPEC_GAPS.md.",
            "Propose acceptance criteria and backlog follow-up.",
            "Do not rewrite code in this lane.",
        ],
        "suggested_artifacts": [
            "templates/specs/OBSERVED_SPEC.md",
            "templates/specs/SPEC_GAPS.md",
            "templates/reports/spec-retrofit-report.md",
        ],
        "suggested_inputs": doc_candidates,
        "limitations": [
            "This release provides guidance/templates, not automatic code scanning.",
            "It may inspect docs only when repository context is limited.",
        ],
    }
    print_output(payload, json_mode)
    return 0


def freshness(json_mode: bool = False) -> int:
    root = repo_root()
    files = {name: root / name for name in [
        "PRD.md",
        "FEATURE_SPEC.md",
        "ACCEPTANCE_CRITERIA.md",
        "TASKS.md",
        "SPEC_REVIEW.md",
        "PROJECT_MAP.md",
        "ARCHITECTURE_SOURCE_OF_TRUTH.md",
        "THIRD_PARTY_REGISTRY.md",
        "PROJECT_BACKLOG.md",
    ]}
    observed_text = "\n".join(
        path.read_text(encoding="utf-8") for key, path in files.items() if key in {"PRD.md", "FEATURE_SPEC.md", "TASKS.md", "ACCEPTANCE_CRITERIA.md"} and path.exists()
    ).lower()
    checks: list[dict[str, Any]] = []

    def mtime(path: Path) -> float | None:
        return path.stat().st_mtime if path.exists() else None

    prd = files["PRD.md"]
    project_map = files["PROJECT_MAP.md"]
    if prd.exists() and project_map.exists():
        status = "OK" if mtime(prd) >= mtime(project_map) else "STALE"
        checks.append({"check": "PRD newer than PROJECT_MAP", "status": status, "evidence": ["PRD.md", "PROJECT_MAP.md"]})
    else:
        checks.append({"check": "PRD newer than PROJECT_MAP", "status": "UNKNOWN" if prd.exists() or project_map.exists() else "MISSING", "evidence": []})

    feature = files["FEATURE_SPEC.md"]
    architecture = files["ARCHITECTURE_SOURCE_OF_TRUTH.md"]
    if feature.exists() and architecture.exists():
        status = "OK" if mtime(feature) >= mtime(architecture) else "STALE"
        checks.append({"check": "FEATURE_SPEC newer than ARCHITECTURE_SOURCE_OF_TRUTH", "status": status, "evidence": ["FEATURE_SPEC.md", "ARCHITECTURE_SOURCE_OF_TRUTH.md"]})
    else:
        checks.append({"check": "FEATURE_SPEC newer than ARCHITECTURE_SOURCE_OF_TRUTH", "status": "UNKNOWN" if feature.exists() or architecture.exists() else "MISSING", "evidence": []})

    tasks = files["TASKS.md"]
    backlog = files["PROJECT_BACKLOG.md"]
    if tasks.exists() and backlog.exists():
        backlog_text = backlog.read_text(encoding="utf-8")
        status = "OK" if "TASKS.md" in backlog_text or "FEATURE_SPEC.md" in backlog_text or "PRD.md" in backlog_text else "WARN"
        checks.append({"check": "TASKS linked to PROJECT_BACKLOG", "status": status, "evidence": ["TASKS.md", "PROJECT_BACKLOG.md"]})
    else:
        checks.append({"check": "TASKS linked to PROJECT_BACKLOG", "status": "MISSING", "evidence": []})

    acceptance = files["ACCEPTANCE_CRITERIA.md"]
    if acceptance.exists():
        text = acceptance.read_text(encoding="utf-8").lower()
        status = "OK" if "validation" in text or "evidence" in text else "WARN"
        checks.append({"check": "Acceptance criteria include validation evidence", "status": status, "evidence": ["ACCEPTANCE_CRITERIA.md"]})
    else:
        checks.append({"check": "Acceptance criteria include validation evidence", "status": "MISSING", "evidence": []})

    registry = files["THIRD_PARTY_REGISTRY.md"]
    if any(kw in observed_text for kw in ["api", "sdk", "webhook", "integration"]) and not registry.exists():
        checks.append({"check": "External API spec has THIRD_PARTY_REGISTRY", "status": "WARN", "evidence": ["PRD.md/FEATURE_SPEC.md mention integration"]})
    elif any(kw in observed_text for kw in ["api", "sdk", "webhook", "integration"]):
        checks.append({"check": "External API spec has THIRD_PARTY_REGISTRY", "status": "OK", "evidence": ["THIRD_PARTY_REGISTRY.md"]})
    else:
        checks.append({"check": "External API spec has THIRD_PARTY_REGISTRY", "status": "UNKNOWN", "evidence": []})

    if any(kw in observed_text for kw in ["production", "payment", "billing", "regulated", "permission"]) and not files["SPEC_REVIEW.md"].exists():
        checks.append({"check": "Production-critical spec has release/review gate", "status": "WARN", "evidence": ["SPEC_REVIEW.md missing"]})
    elif any(kw in observed_text for kw in ["production", "payment", "billing", "regulated", "permission"]):
        checks.append({"check": "Production-critical spec has release/review gate", "status": "OK", "evidence": ["SPEC_REVIEW.md"]})
    else:
        checks.append({"check": "Production-critical spec has release/review gate", "status": "UNKNOWN", "evidence": []})

    if tasks.exists():
        task_text = tasks.read_text(encoding="utf-8").lower()
        done_like = any(marker in task_text for marker in ["[x]", "done", "completed"])
        review_exists = files["SPEC_REVIEW.md"].exists()
        status = "WARN" if done_like and not review_exists else "OK" if done_like and review_exists else "UNKNOWN"
        checks.append({"check": "Completed tasks have spec review evidence", "status": status, "evidence": ["TASKS.md", "SPEC_REVIEW.md"] if review_exists else ["TASKS.md"]})
    else:
        checks.append({"check": "Completed tasks have spec review evidence", "status": "MISSING", "evidence": []})

    payload = {
        "ok": True,
        "checks": checks,
        "summary": {
            "ok": sum(1 for item in checks if item["status"] == "OK"),
            "warn": sum(1 for item in checks if item["status"] == "WARN"),
            "missing": sum(1 for item in checks if item["status"] == "MISSING"),
            "stale": sum(1 for item in checks if item["status"] == "STALE"),
            "unknown": sum(1 for item in checks if item["status"] == "UNKNOWN"),
        },
        "note": "Best-effort freshness check. Missing or optional files do not hard-fail this command.",
    }
    print_output(payload, json_mode)
    return 0
