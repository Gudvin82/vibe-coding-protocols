#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRENT = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
CURRENT_NO_V = CURRENT.removeprefix("v")
METHODOLOGY = (ROOT / "METHODOLOGY_VERSION").read_text(encoding="utf-8").strip()

issues: list[str] = []
allowed_historical_hits: list[str] = []


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def require_contains(path: str, needle: str, label: str) -> None:
    text = read(path)
    if needle not in text:
        issues.append(f"{path}: missing {label} -> {needle}")


def require_exact(path: str, expected: str, label: str) -> None:
    actual = read(path).strip()
    if actual != expected:
        issues.append(f"{path}: {label} is {actual!r}, expected {expected!r}")


def require_json_value(path: str, key: str, expected: str) -> None:
    payload = json.loads(read(path))
    actual = payload.get(key)
    if actual != expected:
        issues.append(f"{path}: {key} is {actual!r}, expected {expected!r}")


def scan_cards() -> None:
    for card in sorted((ROOT / ".vcp/cards").rglob("*.json")):
        payload = json.loads(card.read_text(encoding="utf-8"))
        if payload.get("version") != CURRENT:
            issues.append(f"{card.relative_to(ROOT)}: version is {payload.get('version')!r}, expected {CURRENT!r}")


def latest_release_title() -> None:
    path = ROOT / f"docs/release-{CURRENT}.md"
    if not path.exists():
        issues.append(f"{path.relative_to(ROOT)}: missing current release notes")
        return
    first = path.read_text(encoding="utf-8").splitlines()[0].strip()
    expected = f"# Vibe Coding Protocols {CURRENT}"
    if not first.startswith(expected):
        issues.append(f"{path.relative_to(ROOT)}: first heading {first!r} does not start with {expected!r}")


def latest_changelog_heading() -> None:
    changelog = read("CHANGELOG.md")
    match = re.search(r"^##\s+(v\d+\.\d+\.\d+)\b", changelog, re.MULTILINE)
    if not match:
        issues.append("CHANGELOG.md: could not find a version heading")
        return
    if match.group(1) != CURRENT:
        issues.append(f"CHANGELOG.md: latest heading is {match.group(1)!r}, expected {CURRENT!r}")


def scan_stale_versions() -> None:
    stale_versions = sorted(
        {
            m.group(0)
            for path in [ROOT / "CHANGELOG.md", ROOT / "docs/releases/README.md"]
            for m in re.finditer(r"v\d+\.\d+\.\d+", path.read_text(encoding="utf-8"))
            if m.group(0) != CURRENT
        }
    )
    current_files = [
        "README.md",
        "README_ru.md",
        "VERSION",
        "docs/versioning.md",
        "package.json",
        "pyproject.toml",
        "CITATION.cff",
        "llms.txt",
        "llms-full.txt",
        "PROJECT_MAP.md",
        "AGENTS.md",
        ".vcp/index.json",
        ".vcp/catalog.json",
        "vcp_cli/__init__.py",
        f"docs/release-{CURRENT}.md",
    ]
    current_files += [str(p.relative_to(ROOT)) for p in sorted((ROOT / ".vcp/manifests").glob("*.json"))]

    for rel in current_files:
        text = read(rel)
        for stale in stale_versions:
            if stale in text:
                issues.append(f"{rel}: stale current-surface version {stale!r} found")

    historical_allowed = [
        "CHANGELOG.md",
        "docs/releases/README.md",
        "docs/migration/README.md",
    ]
    for rel in historical_allowed:
        text = read(rel)
        hits = sorted({m.group(0) for m in re.finditer(r"v\d+\.\d+\.\d+", text) if m.group(0) != CURRENT})
        if hits:
            allowed_historical_hits.append(f"{rel}: allowed historical references -> {', '.join(hits)}")


require_exact("VERSION", CURRENT, "repository version")
require_contains("README.md", f"repo-{CURRENT}", "README badge")
require_contains("README.md", f"Repository package: `{CURRENT}`", "README package marker")
require_contains("README_ru.md", f"Repository package: `{CURRENT}`", "README_ru package marker")
require_contains("docs/versioning.md", f"Repository package `{CURRENT}`", "docs/versioning package marker")
require_contains("docs/versioning.md", f"Web methodology `{METHODOLOGY}`", "docs/versioning methodology marker")
require_contains("llms.txt", CURRENT, "llms current version")
require_contains("llms-full.txt", CURRENT, "llms-full current version")
require_contains("CITATION.cff", f'version: "{CURRENT}"', "citation version")
require_contains("package.json", f'"version": "{CURRENT_NO_V}"', "package.json version")
require_contains("pyproject.toml", f'version = "{CURRENT_NO_V}"', "pyproject version")
require_contains("vcp_cli/__init__.py", f'__version__ = "{CURRENT_NO_V}"', "CLI version")
require_json_value(".vcp/index.json", "version", CURRENT)
require_json_value(".vcp/catalog.json", "version", CURRENT)
require_json_value(".vcp/manifests/vcp.manifest.json", "package_version", CURRENT)
require_json_value(".vcp/manifests/vcp.manifest.json", "methodology_version", METHODOLOGY)
latest_release_title()
latest_changelog_heading()
scan_cards()
scan_stale_versions()

if issues:
    print(f"Public version surface check failed for {CURRENT}:")
    for item in issues:
        print(f"- {item}")
    if allowed_historical_hits:
        print("Allowed historical references:")
        for item in allowed_historical_hits:
            print(f"- {item}")
    sys.exit(1)

print(f"Public version surface check passed for {CURRENT}.")
if allowed_historical_hits:
    print("Allowed historical references:")
    for item in allowed_historical_hits:
        print(f"- {item}")
