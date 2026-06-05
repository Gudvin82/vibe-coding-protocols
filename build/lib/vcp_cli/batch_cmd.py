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
        return {"ok": False, "error": "No targets provided.", "results": []}
    results: list[dict[str, Any]] = []
    summary = {"passed": 0, "warn": 0, "failed": 0, "not_run": 0}
    for raw in collected:
        target = Path(raw)
        if not target.is_absolute():
            target = (Path.cwd() / target).resolve()
        if not target.exists():
            item = {"target": str(target), "status": "failed", "error": "Target does not exist."}
            summary["failed"] += 1
            results.append(item)
            if fail_fast:
                break
            continue
        try:
            payload = evaluate_cmd.evaluate_payload(target)
            item = {
                "target": str(target),
                "status": "passed",
                "repository_package": payload.get("repository_package_version"),
                "benchmark_count": payload.get("benchmark_count"),
                "command_count": payload.get("command_count"),
            }
            summary["passed"] += 1
        except Exception as exc:  # noqa: BLE001
            item = {"target": str(target), "status": "failed", "error": str(exc)}
            summary["failed"] += 1
            if fail_fast:
                results.append(item)
                break
        results.append(item)
    return {
        "ok": summary["failed"] == 0,
        "mode": "batch-evaluate",
        "results": results,
        "summary": summary,
        "note": "Batch mode is local-only and non-mutating. It does not use network calls or background execution.",
    }


def run_evaluate(targets: list[str] | None = None, targets_file: str | None = None, fail_fast: bool = False, json_mode: bool = False) -> int:
    payload = evaluate_payload(targets, targets_file, fail_fast=fail_fast)
    print_output(payload, json_mode)
    return 0 if payload.get("ok") else 1
