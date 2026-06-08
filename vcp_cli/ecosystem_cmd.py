from __future__ import annotations

from .utils import load_json, print_output, repo_root, repo_version


def watchlist_payload() -> dict[str, object]:
    root = repo_root()
    data = load_json(root / '.vcp' / 'ai-ecosystem-watchlist.json')
    return {
        'ok': True,
        'version': repo_version(root),
        'count': len(data.get('items', [])),
        'items': data.get('items', []),
        'note': 'Governance watchlist only. VCP does not ship or host these external tools.',
    }


def scout_payload() -> dict[str, object]:
    root = repo_root()
    data = load_json(root / '.vcp' / 'ecosystem-scouting-workflow.json')
    return {
        'ok': True,
        'version': repo_version(root),
        'steps': data.get('steps', []),
        'references': data.get('references', []),
        'note': 'Workflow only. No automated crawling, ranking, or vendor scanning occurs.',
    }


def run_watchlist(json_mode: bool = False) -> int:
    print_output(watchlist_payload(), json_mode)
    return 0


def run_scout(json_mode: bool = False) -> int:
    print_output(scout_payload(), json_mode)
    return 0
