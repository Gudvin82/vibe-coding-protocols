from __future__ import annotations

from pathlib import Path

from .utils import MANIFEST_SCHEMA_VERSION, git_head, methodology_version, print_output, repo_root, repo_version


def get_version_info(start: Path | None = None) -> dict[str, object]:
    root = repo_root(start)
    return {
        "name": "Vibe Coding Protocols",
        "repository_package": repo_version(root),
        "methodology": methodology_version(root),
        "manifest_schema": MANIFEST_SCHEMA_VERSION,
        "git_commit": git_head(root),
        "repo_root": str(root),
        "running_from_repo_root": root == Path.cwd().resolve(),
    }


def run(json_mode: bool = False) -> int:
    data = get_version_info()
    if json_mode:
        print_output(data, True)
    else:
        print("Vibe Coding Protocols")
        print(f"Repository package: {data['repository_package']}")
        print(f"Methodology: {data['methodology']}")
        print(f"Manifest schema: {data['manifest_schema']}")
        print(f"Git commit: {data['git_commit'] or 'unknown'}")
        print(f"Repo root: {'yes' if data['running_from_repo_root'] else 'no'}")
    return 0
