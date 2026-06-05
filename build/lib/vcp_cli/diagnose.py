from __future__ import annotations

from pathlib import Path
from typing import Any

from .utils import load_json, methodology_version, print_output, repo_root, repo_version


def layers_path(root: Path | None = None) -> Path:
    return repo_root(root) / ".vcp" / "diagnostics" / "layers.json"


def _release_doc_for_current_version(root: Path) -> Path:
    return root / f"docs/release-{repo_version(root)}.md"


def _layer_result(root: Path, layer: dict[str, Any]) -> dict[str, Any]:
    required = layer.get("required_files", [])
    missing = [rel for rel in required if not (root / rel).exists()]
    result = "OK"
    likely_reason = ""
    evidence: list[str] = []
    if layer["id"] == "repository-state":
        import subprocess
        status = subprocess.run(["git", "status", "--short"], cwd=root, text=True, capture_output=True, check=False)
        dirty = bool(status.stdout.strip())
        result = "WARN" if dirty else "OK"
        likely_reason = "Uncommitted changes present." if dirty else "Repository is clean."
        evidence.append("git status --short")
    elif layer["id"] == "vcp-version":
        version_value = repo_version(root)
        version_ok = version_value.startswith("v") and len(version_value) > 2
        methodology_ok = methodology_version(root) == "v1.4"
        init_ok = (root / "vcp_cli/__init__.py").read_text(encoding="utf-8").find(version_value.removeprefix("v")) != -1 if (root / "vcp_cli/__init__.py").exists() else False
        if not (version_ok and methodology_ok and init_ok):
            result = "FAIL"
            likely_reason = "Version surfaces are not aligned."
        evidence.extend([f"VERSION={version_value}", f"METHODOLOGY_VERSION={methodology_version(root)}"])
    elif layer["id"] == "release-readiness":
        if missing:
            result = "MISSING"
            likely_reason = "Release checklist is missing."
        elif not _release_doc_for_current_version(root).exists():
            result = "WARN"
            likely_reason = "Current release notes are missing for this package version."
            evidence.append(str(_release_doc_for_current_version(root).relative_to(root)))
        else:
            evidence.append(str(_release_doc_for_current_version(root).relative_to(root)))
    else:
        if missing:
            result = "MISSING"
            likely_reason = "Required layer artifacts are missing."
    if not likely_reason:
        likely_reason = "All required layer artifacts are present."
    return {
        "layer": layer["name"],
        "check": layer.get("check", ""),
        "result": result,
        "evidence": evidence + missing,
        "likely_reason": likely_reason,
        "next_action": layer.get("next_action", ""),
        "tags": layer.get("tags", []),
    }


def run(profile: str | None = None, json_mode: bool = False) -> int:
    root = repo_root()
    layers = load_json(layers_path(root))
    results = [_layer_result(root, layer) for layer in layers]
    if profile:
        for item in results:
            tags = set(item.get("tags", []))
            item["profile_relevant"] = profile in tags or "all" in tags
    ok = all(item["result"] in {"OK", "WARN"} for item in results)
    payload = {
        "ok": ok,
        "repository_package_version": repo_version(root),
        "legacy_methodology_reference": methodology_version(root),
        "version_semantics_warning": f"Use Vibe Coding Protocols {repo_version(root)} when naming the current GitHub release.",
        "profile": profile,
        "summary": {
            "ok": sum(1 for item in results if item["result"] == "OK"),
            "warn": sum(1 for item in results if item["result"] == "WARN"),
            "missing": sum(1 for item in results if item["result"] == "MISSING"),
            "fail": sum(1 for item in results if item["result"] == "FAIL"),
        },
        "layers": results,
        "difference_from_doctor": "doctor checks toolkit environment; diagnose checks project/process readiness by layer.",
    }
    print_output(payload, json_mode)
    return 0 if ok else 1
