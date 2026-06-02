from __future__ import annotations

from pathlib import Path

from .utils import load_json, manifest_path, print_output, repo_root

PROTECTED_FILES = [
    "AGENTS.md",
    "CLAUDE.md",
    "PROJECT_MAP.md",
    "SECURITY.md",
    ".env",
    "package.json",
    "pyproject.toml",
    ".github/workflows",
]


def load_pack(pack_id: str) -> dict:
    data = load_json(manifest_path(repo_root(), "adoption-packs"))
    for item in data.get("items", []):
        if item.get("id") == pack_id:
            return item
    raise KeyError(pack_id)


def to_markdown(plan: dict) -> str:
    lines = [f"# Adoption Dry Run: {plan['name']}", "", "## Files to copy"]
    lines += [f"- `{item}`" for item in plan["files_to_copy"]]
    lines += ["", "## Files to merge manually"]
    lines += [f"- `{item}`" for item in plan["files_to_merge_manually"]]
    lines += ["", "## Files to skip"]
    lines += [f"- `{item}`" for item in plan["files_to_skip"]]
    lines += ["", "## Protected files"]
    lines += [f"- `{item}`" for item in plan["protected_files"]]
    lines += ["", f"Review gate: {plan['review_gate_requirement']}"]
    lines += ["", f"Suggested commit message: {plan['suggested_commit_message']}"]
    return "\n".join(lines) + "\n"


def run(pack: str, dry_run: bool = True, json_mode: bool = False, output: str | None = None, apply: bool = False, yes: bool = False) -> int:
    if apply and not yes:
        print("Refusing apply without --yes.")
        return 1
    if apply:
        print("Apply mode is intentionally not implemented in v0.5.2. Use --dry-run and merge manually.")
        return 1
    pack_data = load_pack(pack)
    plan = {
        "pack": pack_data["id"],
        "name": pack_data["name"],
        "dry_run": dry_run,
        "files_to_copy": pack_data.get("recommended_files", []),
        "files_to_merge_manually": pack_data.get("merge_only_files", []),
        "files_to_skip": pack_data.get("skip_files", []),
        "protected_files": PROTECTED_FILES,
        "stop_conditions": pack_data.get("skip_conditions", []),
        "review_gate_requirement": pack_data.get("review_gate_requirement"),
        "validation_commands": pack_data.get("validation_commands", []),
        "suggested_commit_message": f"Adopt VCP {pack_data['name']}",
        "next_safe_step": pack_data.get("next_safe_step"),
    }
    if output:
        Path(output).write_text(to_markdown(plan), encoding="utf-8")
    if json_mode:
        print_output(plan, True)
    else:
        print(to_markdown(plan).rstrip())
    return 0
