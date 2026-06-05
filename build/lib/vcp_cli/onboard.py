from __future__ import annotations

from typing import Any

from .classify import classify_payload
from .utils import print_output
from .version import get_version_info


def _next_commands(track: str, tier: str, route: str, guided_path: str | None) -> list[str]:
    if track == "New Project Track":
        commands = [
            "python3 -m vcp_cli spec quality-gate --json",
            "python3 -m vcp_cli spec questions --idea \"describe the product idea\" --json",
            f"python3 -m vcp_cli adopt plan --pack {route if route != 'new-project' else 'spec-foundation'} --json",
        ]
    else:
        commands = [
            "python3 -m vcp_cli diagnose --json",
            "python3 -m vcp_cli review-diff --json",
            f"python3 -m vcp_cli adopt plan --pack {route} --json",
            "python3 -m vcp_cli release-check --json",
        ]
        if guided_path == "MVP-to-Launch Path":
            commands = [
                "python3 -m vcp_cli doctor --json",
                "python3 -m vcp_cli onboard --json",
                "python3 -m vcp_cli classify --json",
                "python3 -m vcp_cli adopt plan --pack brownfield-rescue --copy-list",
                "python3 -m vcp_cli adopt plan --pack saas-ai-mvp-hardening --json",
                "python3 -m vcp_cli pr-gate explain --json",
                "python3 -m vcp_cli dashboard build --output ./vcp-dashboard --json",
            ]

    if tier == "Governed":
        commands.append("python3 -m vcp_cli score --json")
    return commands


def onboard_payload() -> dict[str, Any]:
    version_info = get_version_info()
    classification = classify_payload()
    next_commands = _next_commands(
        classification["track"],
        classification["suggested_tier"],
        classification["suggested_route"],
        classification.get("guided_path"),
    )
    return {
        "repository_package_version": version_info["repository_package_version"],
        "legacy_methodology_reference": version_info["legacy_methodology_reference"],
        "project_type": classification["project_type"],
        "recommended_track": classification["track"],
        "recommended_guided_path": classification.get("guided_path"),
        "recommended_tier": classification["suggested_tier"],
        "recommended_route": classification["suggested_route"],
        "risk": classification["risk"],
        "confidence": classification["confidence"],
        "recommended_next_commands": next_commands,
        "notes": [
            "Onboard is a guidance command. It does not change files or apply packs.",
            "Use adopt plan for copy-list or patch previews before you move any files.",
        ],
        "limitations": classification["limitations"],
    }


def run(json_mode: bool = False) -> int:
    payload = onboard_payload()
    if json_mode:
        print_output(payload, True)
    else:
        print(f"Repository package: {payload['repository_package_version']}")
        print(f"Project type: {payload['project_type']}")
        print(f"Recommended track: {payload['recommended_track']}")
        if payload.get("recommended_guided_path"):
            print(f"Recommended guided path: {payload['recommended_guided_path']}")
        print(f"Recommended tier: {payload['recommended_tier']}")
        print(f"Recommended route: {payload['recommended_route']}")
        print("Next commands:")
        for command in payload["recommended_next_commands"]:
            print(f"- {command}")
    return 0
