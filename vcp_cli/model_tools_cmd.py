from __future__ import annotations

from .utils import load_json, print_output, repo_root, repo_version


def example_payload() -> dict[str, object]:
    root = repo_root()
    data = load_json(root / '.vcp' / 'model-tool-dependencies.example.json')
    return {
        'ok': True,
        'version': repo_version(root),
        'items': data.get('items', []),
        'note': 'Example governance record only. Not legal advice or compliance certification.',
    }


def run_example(json_mode: bool = False) -> int:
    print_output(example_payload(), json_mode)
    return 0
