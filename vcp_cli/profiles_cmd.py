from __future__ import annotations

from pathlib import Path
from typing import Any

from .utils import load_json, print_output, repo_root

ALLOWED_STATUSES = {"shipped", "optional", "experimental", "roadmap-only", "not-shipped"}


def profiles_path(root: Path | None = None) -> Path:
    return repo_root(root) / ".vcp" / "agent-rule-profiles.json"


def _load_profiles(root: Path | None = None) -> dict[str, Any]:
    path = profiles_path(root)
    data = load_json(path)
    if not isinstance(data, dict) or not isinstance(data.get("items"), list):
        raise ValueError("Agent rule profiles must be a JSON object with an items list.")
    return data


def list_payload(root: Path | None = None) -> dict[str, Any]:
    data = _load_profiles(root)
    items = data.get("items", [])
    return {
        "ok": True,
        "version": data.get("version"),
        "count": len(items),
        "items": items,
        "note": "Profiles are local instruction surfaces. No provider automation or hidden routing occurs.",
    }


def show_payload(profile_id: str, root: Path | None = None) -> dict[str, Any]:
    data = _load_profiles(root)
    for item in data.get("items", []):
        if item.get("id") == profile_id:
            file_rel = item.get("file")
            text = (repo_root(root) / file_rel).read_text(encoding="utf-8") if file_rel else ""
            return {
                "ok": True,
                "version": data.get("version"),
                "profile": item,
                "text": text,
                "note": "Profiles are constraint-first local instruction templates.",
            }
    raise ValueError(f"Unknown profile id: {profile_id}")


def validate(root: Path | None = None) -> list[str]:
    root = repo_root(root)
    data = _load_profiles(root)
    problems: list[str] = []
    expected = ["nano", "mini", "full"]
    found = [item.get("id") for item in data.get("items", [])]
    if found != expected:
        problems.append("agent-rule-profiles must list nano, mini, full in order")
    for item in data.get("items", []):
        profile_id = item.get("id")
        if item.get("status") not in ALLOWED_STATUSES:
            problems.append(f"{profile_id} has invalid status {item.get('status')!r}")
        for rel in (item.get("file"), item.get("file_ru")):
            if not rel or not (root / rel).exists():
                problems.append(f"{profile_id} missing profile file: {rel}")
                continue
            text = (root / rel).read_text(encoding="utf-8")
            for needle in (
                "Do not edit before inspection.",
                "Do not claim tests passed unless run.",
                "Do not broaden scope.",
                "Do not treat roadmap as shipped.",
                "Do not skip trust-check for release-sensitive changes.",
            ):
                if needle not in text:
                    problems.append(f"{rel} missing constraint: {needle}")
    return problems


def run_list(json_mode: bool = False) -> int:
    try:
        payload = list_payload()
    except Exception as exc:  # noqa: BLE001
        print_output({"ok": False, "error": str(exc)}, json_mode)
        return 1
    print_output(payload, json_mode)
    return 0


def run_show(profile_id: str, json_mode: bool = False) -> int:
    try:
        payload = show_payload(profile_id)
    except Exception as exc:  # noqa: BLE001
        print_output({"ok": False, "id": profile_id, "error": str(exc)}, json_mode)
        return 1
    print_output(payload, json_mode)
    return 0
