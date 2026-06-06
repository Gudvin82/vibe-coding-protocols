from __future__ import annotations

from .utils import load_json, print_output, repo_root, repo_version


def payload() -> dict[str, object]:
    root = repo_root()
    data = load_json(root / '.vcp' / 'pr-readiness.example.json')
    data['version'] = repo_version(root)
    data['note'] = 'Local PR readiness only. This command does not create PRs automatically.'
    return data


def run_readiness(json_mode: bool = False) -> int:
    print_output(payload(), json_mode)
    return 0
