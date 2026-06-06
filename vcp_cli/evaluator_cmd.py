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
    }


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
    return problems


def run_pack(json_mode: bool = False) -> int:
    data = payload()
    print_output(data, json_mode)
    if json_mode:
        return 0
    print("Evaluator pack loaded.")
    return 0
