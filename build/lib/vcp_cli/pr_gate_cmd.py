from __future__ import annotations

from .utils import print_output


def payload() -> dict[str, object]:
    return {
        "ok": True,
        "states": {
            "pass": "Core evidence is present and no material blocker is open.",
            "warn": "Merge may continue only if the team consciously accepts visible gaps.",
            "block": "Do not merge or release until the mismatch or unsafe condition is resolved.",
            "needs-human-review": "Automation output is insufficient for final approval.",
            "not-applicable": "The gate does not apply to this change slice.",
        },
        "examples": [
            {"case": "AI generated changes without tests", "recommended_state": "warn"},
            {"case": "Public release docs mismatch", "recommended_state": "block"},
            {"case": "Missing proof layer on internal-only refactor", "recommended_state": "warn"},
            {"case": "Destructive apply without confirmation", "recommended_state": "block"},
            {"case": "Roadmap overclaim in shipped docs", "recommended_state": "block"},
            {"case": "Unrun tests claimed as passed", "recommended_state": "block"},
        ],
        "note": "PR Gate is an approval model and workflow template, not a GitHub Marketplace action or policy engine.",
    }


def run_explain(json_mode: bool = False) -> int:
    print_output(payload(), json_mode)
    return 0
