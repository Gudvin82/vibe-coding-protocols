from __future__ import annotations

from pathlib import Path
from typing import Any

from . import evaluate as evaluate_cmd
from .utils import print_output, repo_root


def _collect_targets(targets: list[str] | None = None, targets_file: str | None = None) -> list[str]:
    items = list(targets or [])
    if targets_file:
        path = Path(targets_file)
        if not path.is_absolute():
            path = (Path.cwd() / path).resolve()
        if not path.exists():
            raise FileNotFoundError(path)
        items.extend(line.strip() for line in path.read_text(encoding='utf-8').splitlines() if line.strip())
    deduped: list[str] = []
    for item in items:
        if item not in deduped:
            deduped.append(item)
    return deduped


def evaluate_payload(targets: list[str] | None = None, targets_file: str | None = None, fail_fast: bool = False) -> dict[str, Any]:
    collected = _collect_targets(targets, targets_file)
    if not collected:
        return {
            "ok": False,
            "error": "No targets provided.",
            "results": [],
            "summary": {"passed": 0, "warn": 0, "failed": 0, "not_run": 0},
            "warnings": [],
            "not_run_reasons": ["No targets were provided to batch evaluate."],
        }
    results: list[dict[str, Any]] = []
    summary = {"passed": 0, "warn": 0, "failed": 0, "not_run": 0}
    warnings: list[str] = []
    not_run_reasons: list[str] = []
    for raw in collected:
        target = Path(raw)
        if not target.is_absolute():
            target = (Path.cwd() / target).resolve()
        if not target.exists():
            item = {
                "target": str(target),
                "status": "failed",
                "error": "Target does not exist.",
                "warning": "Missing target path.",
            }
            summary["failed"] += 1
            warnings.append(f"Missing target: {target}")
            results.append(item)
            if fail_fast:
                not_run_reasons.append("Stopped after the first missing target because --fail-fast was set.")
                break
            continue
        try:
            payload = evaluate_cmd.evaluate_payload(target)
            benchmark_count = payload.get("benchmark_count")
            command_count = payload.get("command_count")
            item = {
                "target": str(target),
                "status": "passed",
                "repository_package": payload.get("repository_package_version"),
                "benchmark_count": benchmark_count,
                "command_count": command_count,
            }
            local_warnings: list[str] = []
            if benchmark_count in (None, 0):
                local_warnings.append("No benchmark coverage reported.")
            if command_count in (None, 0):
                local_warnings.append("No command coverage reported.")
            if local_warnings:
                item["warning"] = "; ".join(local_warnings)
                warnings.extend(f"{target}: {warning}" for warning in local_warnings)
                summary["warn"] += 1
            summary["passed"] += 1
        except Exception as exc:  # noqa: BLE001
            item = {
                "target": str(target),
                "status": "failed",
                "error": str(exc),
                "warning": "Target could not be evaluated.",
            }
            summary["failed"] += 1
            warnings.append(f"Evaluation failed for {target}: {exc}")
            if fail_fast:
                results.append(item)
                not_run_reasons.append("Stopped after the first evaluation failure because --fail-fast was set.")
                break
        results.append(item)
    return {
        "ok": summary["failed"] == 0,
        "mode": "batch-evaluate",
        "results": results,
        "summary": summary,
        "warnings": warnings,
        "not_run_reasons": not_run_reasons,
        "note": "Batch mode is local-only and non-mutating. It does not use network calls or background execution.",
    }


def run_evaluate(targets: list[str] | None = None, targets_file: str | None = None, fail_fast: bool = False, json_mode: bool = False) -> int:
    payload = evaluate_payload(targets, targets_file, fail_fast=fail_fast)
    print_output(payload, json_mode)
    return 0 if payload.get("ok") else 1
