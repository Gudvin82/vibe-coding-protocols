from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

MANIFEST_SCHEMA_VERSION = "v1"
REPO_NAME = "vibe-coding-protocols"
MANIFEST_FILENAMES = {
    "vcp": "vcp.manifest.json",
    "protocols": "protocols.manifest.json",
    "adoption-packs": "adoption-packs.manifest.json",
    "commands": "commands.manifest.json",
    "reports": "reports.manifest.json",
    "benchmarks": "benchmarks.manifest.json",
}


def repo_root(start: Path | None = None) -> Path:
    cwd = (start or Path.cwd()).resolve()
    for base in [cwd, *cwd.parents, Path(__file__).resolve().parents[1]]:
        if (base / "VERSION").is_file() and (base / "METHODOLOGY_VERSION").is_file():
            return base
    return Path(__file__).resolve().parents[1]


def read_trimmed(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def repo_version(root: Path | None = None) -> str:
    return read_trimmed(repo_root(root) / "VERSION")


def methodology_version(root: Path | None = None) -> str:
    return read_trimmed(repo_root(root) / "METHODOLOGY_VERSION")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(data: Any) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False)


def print_output(data: Any, json_mode: bool) -> None:
    if json_mode:
        print(dump_json(data))
    elif isinstance(data, str):
        print(data)
    else:
        print(dump_json(data))


def run_command(command: list[str], cwd: Path, capture: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=cwd,
        text=True,
        capture_output=capture,
        check=False,
    )


def git_head(root: Path) -> str | None:
    result = run_command(["git", "rev-parse", "HEAD"], root)
    if result.returncode == 0:
        return result.stdout.strip()
    return None


def git_status_short(root: Path) -> str:
    result = run_command(["git", "status", "--short"], root)
    return result.stdout.strip() if result.returncode == 0 else ""


def manifest_dir(root: Path) -> Path:
    preferred = root / ".vcp" / "manifests"
    if preferred.is_dir():
        return preferred
    return root


def manifest_path(root: Path, name: str) -> Path:
    filename = MANIFEST_FILENAMES[name]
    preferred = root / ".vcp" / "manifests" / filename
    if preferred.exists():
        return preferred
    legacy = root / filename
    return legacy if legacy.exists() else preferred


def manifest_paths(root: Path) -> dict[str, Path]:
    return {key: manifest_path(root, key) for key in MANIFEST_FILENAMES}


def relative_to_root(root: Path, path: Path) -> str:
    return str(path.relative_to(root))


def ensure_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def eprint(*args: object) -> None:
    print(*args, file=sys.stderr)
