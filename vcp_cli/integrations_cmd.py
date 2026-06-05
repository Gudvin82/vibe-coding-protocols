from __future__ import annotations

from pathlib import Path
from typing import Any

from .utils import load_json, print_output, repo_root

ALLOWED_STATUSES = {"shipped", "local-template", "experimental", "roadmap", "not-shipped"}


def registry_path(root: Path | None = None) -> Path:
    return repo_root(root) / ".vcp" / "integrations.json"


def _load_registry(root: Path | None = None) -> dict[str, Any]:
    path = registry_path(root)
    if not path.exists():
        raise FileNotFoundError(path)
    data = load_json(path)
    if not isinstance(data, dict) or not isinstance(data.get("items"), list):
        raise ValueError("Integration registry must be a JSON object with an items list.")
    return data


def integration_packs_path(root: Path | None = None) -> Path:
    return repo_root(root) / ".vcp" / "integration-packs.json"


def _load_integration_packs(root: Path | None = None) -> dict[str, Any]:
    path = integration_packs_path(root)
    if not path.exists():
        raise FileNotFoundError(path)
    data = load_json(path)
    if not isinstance(data, dict) or not isinstance(data.get("items"), list):
        raise ValueError("Integration packs registry must be a JSON object with an items list.")
    return data


def _counts(items: list[dict[str, Any]]) -> dict[str, int]:
    counts = {status: 0 for status in sorted(ALLOWED_STATUSES)}
    for item in items:
        status = item.get("status")
        if status in counts:
            counts[status] += 1
    return counts


def list_payload(status: str | None = None, root: Path | None = None) -> dict[str, Any]:
    if status and status not in ALLOWED_STATUSES:
        raise ValueError(f"Unknown integration status: {status}")
    data = _load_registry(root)
    items = data.get("items", [])
    filtered = [item for item in items if status is None or item.get("status") == status]
    return {
        "ok": True,
        "version": data.get("version"),
        "status_filter": status,
        "counts": _counts(items),
        "count": len(filtered),
        "items": filtered,
        "note": "Read-only local registry. No install, registry sync, or network execution occurs.",
    }


def packs_payload(status: str | None = None, root: Path | None = None) -> dict[str, Any]:
    if status and status not in ALLOWED_STATUSES:
        raise ValueError(f"Unknown integration status: {status}")
    data = _load_integration_packs(root)
    items = data.get("items", [])
    filtered = [item for item in items if status is None or item.get("status") == status]
    return {
        "ok": True,
        "version": data.get("version"),
        "status_filter": status,
        "counts": _counts(items),
        "count": len(filtered),
        "items": filtered,
        "note": "Integration packs are local, documented setup bundles. They are not official third-party integrations or marketplace installs.",
    }


def run_list(status: str | None = None, json_mode: bool = False) -> int:
    try:
        payload = list_payload(status=status)
    except Exception as exc:  # noqa: BLE001
        payload = {
            "ok": False,
            "status_filter": status,
            "allowed_statuses": sorted(ALLOWED_STATUSES),
            "error": str(exc),
        }
        print_output(payload, json_mode)
        return 1
    print_output(payload, json_mode)
    return 0


def run_packs(status: str | None = None, json_mode: bool = False) -> int:
    try:
        payload = packs_payload(status=status)
    except Exception as exc:  # noqa: BLE001
        payload = {
            "ok": False,
            "status_filter": status,
            "allowed_statuses": sorted(ALLOWED_STATUSES),
            "error": str(exc),
        }
        print_output(payload, json_mode)
        return 1
    print_output(payload, json_mode)
    return 0
