from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

MANIFEST_SCHEMA_VERSION = "v1"
REPO_NAME = "vibe-coding-protocols"
PROJECT_ROOT_MARKERS = (
    ".git",
    "pyproject.toml",
    "package.json",
    "requirements.txt",
    "go.mod",
    "Cargo.toml",
    "Gemfile",
    "composer.json",
)
MANIFEST_FILENAMES = {
    "vcp": "vcp.manifest.json",
    "protocols": "protocols.manifest.json",
    "adoption-packs": "adoption-packs.manifest.json",
    "commands": "commands.manifest.json",
    "reports": "reports.manifest.json",
    "benchmarks": "benchmarks.manifest.json",
}


def _candidate_paths(start: Path | None = None) -> list[Path]:
    cwd = (start or Path.cwd()).resolve()
    return [cwd, *cwd.parents]


def is_vcp_runtime_root(path: Path) -> bool:
    return (path / "VERSION").is_file() and (path / "METHODOLOGY_VERSION").is_file()


def source_root() -> Path:
    return Path(__file__).resolve().parents[1]


def bundled_root() -> Path:
    return Path(__file__).resolve().parent / "_assets"


def find_vcp_repo_root(start: Path | None = None) -> Path | None:
    for base in [*_candidate_paths(start), source_root()]:
        if is_vcp_runtime_root(base):
            return base
    return None


def runtime_root(start: Path | None = None) -> Path:
    detected = find_vcp_repo_root(start)
    if detected is not None:
        return detected
    bundle = bundled_root()
    if is_vcp_runtime_root(bundle):
        return bundle
    raise FileNotFoundError(
        "VCP runtime assets were not found. Run inside a VCP repository checkout or reinstall the package so bundled assets are included."
    )


def repo_root(start: Path | None = None) -> Path:
    return runtime_root(start)


def project_root(start: Path | None = None) -> Path:
    cwd = (start or Path.cwd()).resolve()
    for base in _candidate_paths(cwd):
        if any((base / marker).exists() for marker in PROJECT_ROOT_MARKERS):
            return base
    return cwd


def resolve_runtime_path(root: Path, rel: str) -> Path:
    candidate = root / rel
    if candidate.exists():
        return candidate
    source_candidate = source_root() / rel
    return source_candidate if source_candidate.exists() else candidate


def runtime_path_exists(root: Path, rel: str) -> bool:
    return resolve_runtime_path(root, rel).exists()


def read_trimmed(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def repo_version(root: Path | None = None) -> str:
    return read_trimmed(runtime_root(root) / "VERSION")


def methodology_version(root: Path | None = None) -> str:
    return read_trimmed(runtime_root(root) / "METHODOLOGY_VERSION")


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
