from __future__ import annotations

import difflib
from pathlib import Path
from typing import Any

from .utils import load_json, manifest_path, print_output, repo_root

PACK_ALIASES = {
    "spec-foundation": "spec-first",
}

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

SAFE_TEMPLATE_TARGETS = {
    "templates/AGENTS.md": "AGENTS.md",
    "templates/PROJECT_MAP.md": "PROJECT_MAP.md",
    "templates/PROJECT_BACKLOG.md": "PROJECT_BACKLOG.md",
    "templates/ARCHITECTURE_SOURCE_OF_TRUTH.md": "ARCHITECTURE_SOURCE_OF_TRUTH.md",
    "templates/AUDIT_BACKLOG.md": "AUDIT_BACKLOG.md",
    "templates/SECURITY_BASELINE.md": "SECURITY_BASELINE.md",
    "templates/SECURITY_OPERATIONS_BASELINE.md": "SECURITY_OPERATIONS_BASELINE.md",
    "templates/THIRD_PARTY_REGISTRY.md": "THIRD_PARTY_REGISTRY.md",
    "templates/INCIDENT_RECOVERY_RUNBOOK.md": "INCIDENT_RECOVERY_RUNBOOK.md",
    "templates/specs/PRODUCT_BRIEF.md": "PRODUCT_BRIEF.md",
    "templates/specs/PRD.md": "PRD.md",
    "templates/specs/FEATURE_SPEC.md": "FEATURE_SPEC.md",
    "templates/specs/SPEC_TO_BACKLOG.md": "SPEC_TO_BACKLOG.md",
    "templates/specs/OBSERVED_SPEC.md": "OBSERVED_SPEC.md",
    "templates/specs/SPEC_GAPS.md": "SPEC_GAPS.md",
}

TRACK_BY_PACK = {
    "new-project": "New Project Track",
    "spec-first": "New Project Track",
    "existing-mvp": "Existing Project Track",
    "brownfield-rescue": "Existing Project Track",
    "production": "Existing Project Track",
    "regulated": "Existing Project Track",
    "shared-engine": "Existing Project Track",
    "public-growth": "Existing Project Track",
    "public-site": "Existing Project Track",
    "maintenance": "Existing Project Track",
    "third-party-api": "Existing Project Track",
    "backlog": "Existing Project Track",
    "operations": "Existing Project Track",
    "post-task-review": "Existing Project Track",
    "ui-ownership": "Existing Project Track",
}

TIER_BY_PACK = {
    "new-project": "Lite",
    "spec-first": "Lite",
    "existing-mvp": "Lite",
    "maintenance": "Lite",
    "backlog": "Team",
    "brownfield-rescue": "Team",
    "ui-ownership": "Team",
    "third-party-api": "Team",
    "operations": "Team",
    "public-site": "Team",
    "public-growth": "Team",
    "production": "Governed",
    "regulated": "Governed",
    "shared-engine": "Governed",
    "post-task-review": "Governed",
}


def _canonical_pack_id(pack_id: str) -> str:
    return PACK_ALIASES.get(pack_id, pack_id)


def load_pack(pack_id: str) -> dict[str, Any]:
    data = load_json(manifest_path(repo_root(), "adoption-packs"))
    canonical = _canonical_pack_id(pack_id)
    for item in data.get("items", []):
        if item.get("id") == canonical:
            return item
    raise KeyError(pack_id)


def _copy_destination(source: str) -> str | None:
    if source in SAFE_TEMPLATE_TARGETS:
        return SAFE_TEMPLATE_TARGETS[source]
    if source.startswith("templates/public-growth/"):
        return source.removeprefix("templates/")
    if source.startswith("templates/reports/"):
        return None
    return None


def _build_copy_map(pack_data: dict[str, Any]) -> tuple[list[dict[str, str]], list[str], list[str]]:
    files_to_copy: list[dict[str, str]] = []
    files_to_review: list[str] = []
    files_not_to_copy: list[str] = []

    for group_name in ("recommended_files", "optional_files"):
        for rel in pack_data.get(group_name, []):
            destination = _copy_destination(rel)
            if destination:
                files_to_copy.append({"source": rel, "destination": destination})
            else:
                files_to_review.append(rel)

    for rel in pack_data.get("merge_only_files", []):
        if rel not in files_to_review:
            files_to_review.append(rel)

    for rel in pack_data.get("skip_files", []):
        if rel not in files_not_to_copy:
            files_not_to_copy.append(rel)

    for rel in PROTECTED_FILES:
        if rel not in files_not_to_copy:
            files_not_to_copy.append(rel)

    return files_to_copy, sorted(set(files_to_review)), sorted(set(files_not_to_copy))


def plan_payload(pack: str, root: Path | None = None) -> dict[str, Any]:
    root = repo_root(root)
    pack_data = load_pack(pack)
    files_to_copy, files_to_review, files_not_to_copy = _build_copy_map(pack_data)
    canonical_pack = pack_data["id"]
    expected_reports = pack_data.get("expected_report_template", [])
    manual_steps = [
        pack_data.get("next_safe_step", "Review the pack before moving files."),
        "Read docs/protocol-pack-security.md before applying external or high-trust packs.",
        "Run validation commands only after you decide which files to adopt manually.",
    ]
    return {
        "selected_pack": canonical_pack,
        "pack_alias_requested": pack,
        "pack_name": pack_data["name"],
        "target_track": TRACK_BY_PACK.get(canonical_pack, "Existing Project Track"),
        "target_tier": TIER_BY_PACK.get(canonical_pack, "Lite"),
        "files_to_copy": files_to_copy,
        "files_to_review": files_to_review,
        "files_not_to_copy": files_not_to_copy,
        "commands_to_run": pack_data.get("validation_commands", []),
        "expected_reports": expected_reports,
        "stop_conditions": pack_data.get("skip_conditions", []),
        "manual_steps": manual_steps,
        "safety_notes": [
            "This command is non-destructive and does not write into your project by default.",
            "Patch output is preview-only unless you explicitly choose an output file.",
            "Protected files and CI paths always require manual review.",
        ],
        "review_gate_requirement": pack_data.get("review_gate_requirement"),
        "protected_files": PROTECTED_FILES,
        "writes_by_default": False,
    }


def _copy_list_text(plan: dict[str, Any]) -> str:
    lines = []
    for item in plan["files_to_copy"]:
        lines.append(f"Copy {item['source']} -> {item['destination']}")
    for rel in plan["files_to_review"]:
        lines.append(f"Review {rel} before applying manually.")
    for rel in plan["files_not_to_copy"]:
        lines.append(f"Do not copy {rel} automatically.")
    return "\n".join(lines) + "\n"


def _patch_preview(plan: dict[str, Any], root: Path | None = None) -> str:
    root = repo_root(root)
    chunks: list[str] = []
    for item in plan["files_to_copy"]:
        source = root / item["source"]
        if not source.exists():
            continue
        destination = item["destination"]
        content = source.read_text(encoding="utf-8").splitlines(keepends=True)
        diff = difflib.unified_diff(
            [],
            content,
            fromfile="/dev/null",
            tofile=destination,
        )
        chunks.append("".join(diff))
    if not chunks:
        return "# No copyable template files were selected for patch preview.\n"
    return "\n".join(chunks)


def to_markdown(plan: dict[str, Any]) -> str:
    lines = [f"# Adoption Plan: {plan['pack_name']}", "", "## Files to copy"]
    lines += [f"- `{item['source']}` -> `{item['destination']}`" for item in plan["files_to_copy"]] or ["- none"]
    lines += ["", "## Files to review"]
    lines += [f"- `{item}`" for item in plan["files_to_review"]] or ["- none"]
    lines += ["", "## Files not to copy"]
    lines += [f"- `{item}`" for item in plan["files_not_to_copy"]] or ["- none"]
    lines += ["", "## Commands to run"]
    lines += [f"- `{item}`" for item in plan["commands_to_run"]] or ["- none"]
    lines += ["", "## Stop conditions"]
    lines += [f"- {item}" for item in plan["stop_conditions"]] or ["- none"]
    lines += ["", "## Safety notes"]
    lines += [f"- {item}" for item in plan["safety_notes"]]
    return "\n".join(lines) + "\n"


def run_plan(
    pack: str,
    *,
    json_mode: bool = False,
    output: str | None = None,
    copy_list: bool = False,
    patch: bool = False,
) -> int:
    plan = plan_payload(pack)
    if copy_list:
        text = _copy_list_text(plan)
    elif patch:
        text = _patch_preview(plan)
    elif json_mode:
        print_output(plan, True)
        return 0
    else:
        text = to_markdown(plan)

    if output:
        Path(output).write_text(text, encoding="utf-8")
    print(text.rstrip())
    return 0


def run(
    pack: str,
    dry_run: bool = True,
    json_mode: bool = False,
    output: str | None = None,
    apply: bool = False,
    yes: bool = False,
    *,
    copy_list: bool = False,
    patch: bool = False,
) -> int:
    del dry_run, yes
    if apply:
        print("adopt --apply remains intentionally disabled. Use `vcp adopt plan` for safe copy-list or patch previews.")
        return 1
    return run_plan(pack, json_mode=json_mode, output=output, copy_list=copy_list, patch=patch)
