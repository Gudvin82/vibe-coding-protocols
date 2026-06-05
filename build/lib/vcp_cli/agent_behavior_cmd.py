from __future__ import annotations

from pathlib import Path

from .utils import print_output

CHECKS = {
    "no_overclaim": "did not overclaim shipped capabilities",
    "no_unrun_tests_claimed": "did not claim unrun tests as passed",
    "version_sync": "kept version surfaces in sync",
    "minimal_diff": "avoided broad unrelated rewrites",
}


def payload(report: str) -> dict[str, object]:
    path = Path(report)
    if not path.is_absolute():
        path = (Path.cwd() / path).resolve()
    if not path.exists():
        return {"ok": False, "error": f"Report not found: {path}"}
    text = path.read_text(encoding="utf-8").lower()
    warnings: list[str] = []
    if "tests passed" in text and "not run" not in text and "failed" not in text:
        warnings.append("Report claims tests passed. Confirm those tests were actually run.")
    if "hosted dashboard" in text or "plugin marketplace" in text:
        warnings.append("Report may blur shipped and roadmap-only surfaces.")
    if "broad rewrite" in text:
        warnings.append("Report references broad rewrite risk. Confirm the diff stayed reviewable.")
    status = "pass" if not warnings else "warn"
    return {
        "ok": True,
        "status": status,
        "checks": CHECKS,
        "warnings": warnings,
        "limitations": [
            "Heuristic text-only check.",
            "No LLM call.",
            "No code execution or network access.",
        ],
    }


def run_check(report: str, json_mode: bool = False) -> int:
    data = payload(report)
    print_output(data, json_mode)
    return 0 if data.get("ok") else 1
