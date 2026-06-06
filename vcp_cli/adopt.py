from __future__ import annotations

import difflib
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .utils import load_json, manifest_path, print_output, runtime_root

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
    "templates/ARCHITECTURE_MAP.md": "ARCHITECTURE_MAP.md",
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
    "templates/specs/ACCEPTANCE_CRITERIA.md": "ACCEPTANCE_CRITERIA.md",
    "templates/specs/TASKS.md": "TASKS.md",
    "templates/specs/SPEC_REVIEW.md": "SPEC_REVIEW.md",
    "templates/specs/SPEC_CHANGELOG.md": "SPEC_CHANGELOG.md",
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


def load_pack(pack_id: str, root: Path | None = None) -> dict[str, Any]:
    data = load_json(manifest_path(runtime_root(root), "adoption-packs"))
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
    root = runtime_root(root)
    pack_data = load_pack(pack, root)
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
    root = runtime_root(root)
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


def _safe_apply_entries(pack_data: dict[str, Any]) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    for rel in pack_data.get("safe_apply_files", []):
        destination = _copy_destination(rel)
        if destination:
            entries.append({"source": rel, "destination": destination})
    if entries:
        return entries
    files_to_copy, _, _ = _build_copy_map(pack_data)
    return files_to_copy


def _target_log_path(target: Path, log_path: str | None) -> Path:
    return Path(log_path).resolve() if log_path else target / "vcp-adopt-log.md"


def _log_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# VCP Adopt Apply Log",
        "",
        f"- Timestamp: `{payload['timestamp']}`",
        f"- Repository package: `{payload['repository_package_version']}`",
        f"- Pack: `{payload['selected_pack']}`",
        f"- Target: `{payload['target']}`",
        f"- Dry run: `{str(payload['dry_run']).lower()}`",
        "",
        "## Copied",
    ]
    lines += [f"- `{item}`" for item in payload["copied"]] or ["- none"]
    lines += ["", "## Skipped"]
    lines += [f"- `{item}`" for item in payload["skipped"]] or ["- none"]
    lines += ["", "## Conflicts"]
    lines += [f"- `{item}`" for item in payload["conflicts"]] or ["- none"]
    lines += ["", "## Manual next steps"]
    lines += [f"- {item}" for item in payload["manual_next_steps"]] or ["- none"]
    lines += ["", "## Rollback guidance", "- Remove copied files listed above if you decide not to keep the pack.", "- Re-run with `--dry-run --json` before any repeated apply."]
    return "\n".join(lines) + "\n"


def apply_payload(
    pack: str,
    *,
    target: str | None,
    confirm: bool,
    dry_run: bool = False,
    create_target: bool = False,
    log_path: str | None = None,
    force: bool = False,
    root: Path | None = None,
) -> tuple[int, dict[str, Any]]:
    runtime = runtime_root(root)
    timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    if force:
        return 1, {
            "ok": False,
            "status": "blocked",
            "error": "--force is intentionally not implemented in v0.8.6 because overwrite safety is not yet strong enough.",
        }
    if not target:
        return 1, {"ok": False, "status": "blocked", "error": "--target is required for adopt apply."}
    if not confirm and not dry_run:
        return 1, {"ok": False, "status": "blocked", "error": "--confirm is required unless --dry-run is used."}

    target_path = Path(target).expanduser().resolve()
    if not target_path.exists():
        if create_target:
            if not dry_run:
                target_path.mkdir(parents=True, exist_ok=True)
        else:
            return 1, {
                "ok": False,
                "status": "blocked",
                "error": f"Target path does not exist: {target_path}. Use --create-target if you want VCP to create it.",
            }

    pack_data = load_pack(pack, runtime)
    entries = _safe_apply_entries(pack_data)
    copied: list[str] = []
    skipped: list[str] = []
    conflicts: list[str] = []

    for entry in entries:
        source = runtime / entry["source"]
        destination = target_path / entry["destination"]
        rel_destination = destination.relative_to(target_path).as_posix() if destination.is_relative_to(target_path) else str(destination)
        if not source.exists():
            skipped.append(f"{entry['source']} -> {rel_destination} (missing source)")
            continue
        if destination.exists():
            conflicts.append(f"{entry['source']} -> {rel_destination}")
            continue
        copied.append(rel_destination)
        if dry_run:
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")

    payload = {
        "ok": True,
        "status": "dry_run" if dry_run else "applied",
        "selected_pack": pack_data["id"],
        "repository_package_version": (runtime / "VERSION").read_text(encoding="utf-8").strip(),
        "target": str(target_path),
        "dry_run": dry_run,
        "timestamp": timestamp,
        "copied": copied,
        "skipped": skipped,
        "conflicts": conflicts,
        "manual_next_steps": [
            pack_data.get("next_safe_step", "Review the adopted files before using them."),
            "Run the pack validation commands manually after you review copied files.",
            "Resolve conflicts manually; existing files were not overwritten.",
        ],
        "validation_commands": pack_data.get("validation_commands", []),
        "review_gate_requirement": pack_data.get("review_gate_requirement"),
        "log_path": str(_target_log_path(target_path, log_path)),
    }
    if not dry_run:
        log_target = _target_log_path(target_path, log_path)
        log_target.parent.mkdir(parents=True, exist_ok=True)
        log_target.write_text(_log_markdown(payload), encoding="utf-8")
        payload["log_written"] = str(log_target)
    else:
        payload["log_written"] = None
    return 0, payload


def run_apply(
    pack: str,
    *,
    target: str | None,
    confirm: bool,
    dry_run: bool = False,
    create_target: bool = False,
    log_path: str | None = None,
    force: bool = False,
    json_mode: bool = False,
) -> int:
    code, payload = apply_payload(
        pack,
        target=target,
        confirm=confirm,
        dry_run=dry_run,
        create_target=create_target,
        log_path=log_path,
        force=force,
    )
    if json_mode:
        print_output(payload, True)
        return code
    if code != 0:
        print(payload["error"])
        return code
    print(f"Pack: {payload['selected_pack']}")
    print(f"Target: {payload['target']}")
    print(f"Status: {payload['status']}")
    print(f"Copied: {len(payload['copied'])}")
    print(f"Skipped: {len(payload['skipped'])}")
    print(f"Conflicts: {len(payload['conflicts'])}")
    if payload["log_written"]:
        print(f"Log: {payload['log_written']}")
    return code


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
        print("adopt --apply is replaced by `vcp adopt apply --pack ... --target ... --confirm`.")
        return 1
    return run_plan(pack, json_mode=json_mode, output=output, copy_list=copy_list, patch=patch)
