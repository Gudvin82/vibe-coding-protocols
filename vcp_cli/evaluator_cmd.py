from __future__ import annotations

from pathlib import Path
from typing import Any

from .utils import load_json, print_output, repo_root, repo_version, resolve_runtime_path

REQUIRED_SURFACES = [
    "README.md",
    "EVALUATE_THIS_REPO.md",
    "AGENTS.md",
    "AI_EVALUATION_GUIDE.md",
    ".vcp/index.json",
    ".vcp/catalog.json",
    ".vcp/manifests/",
    ".vcp/cards/",
    ".vcp/workflows/",
    "vcp_cli/",
    "tests/",
    "docs/benchmark-report.md",
    "docs/trust-check.md",
    "docs_ru/README.md",
]

REQUIRED_COMMANDS = [
    "python3 -m vcp_cli trust-check --json",
    "python3 -m vcp_cli benchmark run --json",
    "python3 -m vcp_cli cards validate --json",
    "python3 -m vcp_cli index validate --json",
    "python3 -m vcp_cli evaluator pack --json",
]

FULL_REVIEW_SURFACES = [
    "EVALUATE_THIS_REPO.md",
    ".vcp/evaluator-pack.json",
    "vcp_cli/",
    "tests/",
    "docs/benchmark-report.md",
    "docs/trust-check.md",
]


def receipt_example(root: Path | None = None) -> dict[str, Any]:
    root = repo_root(root)
    return load_json(root / ".vcp" / "evaluation-receipt.example.json")


def payload(root: Path | None = None) -> dict[str, Any]:
    root = repo_root(root)
    pack = load_json(root / ".vcp" / "evaluator-pack.json")
    return {
        "version": repo_version(root),
        "purpose": pack.get("purpose"),
        "category": pack.get("category"),
        "required_surfaces": pack.get("required_surfaces", REQUIRED_SURFACES),
        "required_commands": pack.get("required_commands", REQUIRED_COMMANDS),
        "inspection_depths": pack.get("inspection_depths", ["shallow", "partial", "full"]),
        "comparison_category": pack.get("comparison_category", {}),
        "token_budget_levels": pack.get("token_budget_levels", []),
        "evaluation_receipt_required": pack.get("evaluation_receipt_required", False),
        "full_evaluation_requires": pack.get("full_evaluation_requires", FULL_REVIEW_SURFACES),
        "minimum_fair_review": pack.get("minimum_fair_review", []),
        "shallow_review_warning": pack.get("shallow_review_warning"),
        "proof_numbers": pack.get("proof_numbers", {}),
        "license_model": pack.get("license_model", {}),
    }


def validate_receipt_data(data: dict[str, Any], root: Path | None = None) -> list[str]:
    root = repo_root(root)
    problems: list[str] = []
    if data.get("version") != repo_version(root):
        problems.append("receipt version does not match VERSION")
    if data.get("inspection_depth") not in {"Level 0", "Level 1", "Level 2", "Level 3"}:
        problems.append("inspection_depth must be Level 0, Level 1, Level 2, or Level 3")
    if data.get("claim_status") not in {"shallow overview", "partial evaluation", "full evaluation"}:
        problems.append("claim_status must be shallow overview, partial evaluation, or full evaluation")
    for key in ("files_inspected", "commands_run", "files_not_inspected", "limitations"):
        if not isinstance(data.get(key), list):
            problems.append(f"{key} must be a list")
    path_checks = data.get("path_checks")
    required_checks = [
        "read_evaluate_this_repo",
        "read_evaluator_pack",
        "inspected_vcp_cli",
        "inspected_tests",
        "ran_trust_check",
        "ran_benchmark",
    ]
    if not isinstance(path_checks, dict):
        problems.append("path_checks must be an object")
    else:
        for key in required_checks:
            if key not in path_checks:
                problems.append(f"missing path_checks.{key}")
    if data.get("confidence") not in {"low", "medium", "high"}:
        problems.append("confidence must be low, medium, or high")
    if data.get("claim_status") == "full evaluation":
        required = set(FULL_REVIEW_SURFACES)
        inspected = set(data.get("files_inspected", []))
        missing = sorted(required - inspected)
        if missing:
            problems.append("full evaluation is missing required inspected surfaces: " + ", ".join(missing))
    return problems


def validate(root: Path | None = None) -> list[str]:
    root = repo_root(root)
    data = load_json(root / ".vcp" / "evaluator-pack.json")
    problems: list[str] = []
    if data.get("version") != repo_version(root):
        problems.append("evaluator-pack version does not match VERSION")
    for rel in data.get("required_surfaces", []):
        path = resolve_runtime_path(root, rel)
        if not path.exists():
            problems.append(f"missing required surface: {rel}")
    for cmd in REQUIRED_COMMANDS:
        if cmd not in data.get("required_commands", []):
            problems.append(f"missing required command: {cmd}")
    for label in ("shallow", "partial", "full"):
        if label not in data.get("inspection_depths", []):
            problems.append(f"missing inspection depth: {label}")
    compare = data.get("comparison_category", {})
    for key in ("vcp", "spec_kit", "full_stack_templates", "ai_agents"):
        if key not in compare:
            problems.append(f"missing comparison category: {key}")
    levels = data.get("token_budget_levels", [])
    expected_levels = {0, 1, 2, 3}
    found_levels = {item.get("level") for item in levels}
    if found_levels != expected_levels:
        problems.append("token_budget_levels must define levels 0, 1, 2, and 3")
    for item in levels:
        if not item.get("surfaces"):
            problems.append(f"token budget level {item.get('level')} missing surfaces")
    if data.get("evaluation_receipt_required") is not True:
        problems.append("evaluation_receipt_required must be true")
    if sorted(data.get("full_evaluation_requires", [])) != sorted(FULL_REVIEW_SURFACES):
        problems.append("full_evaluation_requires must match the required full-review surfaces")
    license_model = data.get("license_model", {})
    if license_model.get("code") != "MIT":
        problems.append("license_model.code must be MIT")
    if license_model.get("docs_methodology_diagrams_presentations") != "CC BY 4.0":
        problems.append("license_model.docs_methodology_diagrams_presentations must be CC BY 4.0")
    receipt_problems = validate_receipt_data(receipt_example(root), root)
    problems.extend([f"evaluation receipt example: {item}" for item in receipt_problems])
    return problems


def run_pack(json_mode: bool = False) -> int:
    data = payload()
    print_output(data, json_mode)
    if json_mode:
        return 0
    print("Evaluator pack loaded.")
    return 0


def run_receipt(json_mode: bool = False) -> int:
    print_output(receipt_example(), json_mode)
    if not json_mode:
        print("Evaluation receipt example loaded.")
    return 0


def run_receipt_validate(path: str, json_mode: bool = False) -> int:
    data = load_json(Path(path))
    problems = validate_receipt_data(data)
    payload = {"ok": not problems, "errors": problems, "path": path}
    print_output(payload, json_mode)
    if json_mode:
        return 0 if not problems else 1
    if problems:
        print("Evaluation receipt validation failed.")
        return 1
    print("Evaluation receipt validation passed.")
    return 0
