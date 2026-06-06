from __future__ import annotations

from .utils import load_json, print_output, repo_root, repo_version


def payload() -> dict[str, object]:
    root = repo_root()
    data = load_json(root / '.vcp' / 'control-scorecard.example.json')
    data['version'] = repo_version(root)
    data['note'] = 'Local heuristic scorecard only; not a certification or guarantee.'
    return data


def run(json_mode: bool = False) -> int:
    print_output(payload(), json_mode)
    return 0
