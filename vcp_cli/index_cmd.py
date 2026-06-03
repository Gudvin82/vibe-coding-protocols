from __future__ import annotations

from pathlib import Path
from typing import Any

from . import cards as cards_cmd
from .utils import dump_json, load_json, print_output, repo_root


def index_path(root: Path | None = None) -> Path:
    return repo_root(root) / '.vcp' / 'index.json'


def show(json_mode: bool = False) -> int:
    data = load_json(index_path())
    if json_mode:
        print_output(data, True)
    else:
        summary = {
            'name': data.get('name'),
            'version': data.get('version'),
            'methodology_version': data.get('methodology_version'),
            'entrypoints': data.get('entrypoints', []),
            'cards_root': data.get('cards', {}).get('root'),
            'recommended_ai_flow': data.get('recommended_ai_flow', []),
        }
        print(dump_json(summary))
    return 0


def validate(json_mode: bool = False) -> int:
    root = repo_root()
    path = index_path(root)
    errors: list[str] = []
    if not path.exists():
        errors.append('.vcp/index.json does not exist')
        payload = {'ok': False, 'errors': errors}
        print_output(payload, json_mode)
        return 1
    data = load_json(path)
    for key in ['name', 'version', 'methodology_version', 'schema_version', 'entrypoints', 'cards', 'manifests', 'benchmarks', 'recommended_ai_flow', 'not']:
        if key not in data:
            errors.append(f'Missing key in .vcp/index.json: {key}')
    for rel in data.get('entrypoints', []):
        if not (root / rel).exists():
            errors.append(f'Missing entrypoint: {rel}')
    cards = data.get('cards', {}) if isinstance(data.get('cards'), dict) else {}
    for rel in cards.values():
        if not (root / rel).exists():
            errors.append(f'Missing cards path: {rel}')
    manifests_rel = data.get('manifests')
    if isinstance(manifests_rel, str) and not (root / manifests_rel).exists():
        errors.append(f'Missing manifests directory: {manifests_rel}')
    bench_rel = data.get('benchmarks')
    if isinstance(bench_rel, str) and not (root / bench_rel).exists():
        errors.append(f'Missing benchmarks directory: {bench_rel}')
    for rel in data.get('docs', []):
        if not (root / rel).exists():
            errors.append(f'Missing doc from index: {rel}')
    _, card_errors = cards_cmd.collect_card_validation(root)
    payload = {'ok': not errors and not card_errors, 'errors': errors + card_errors, 'index_path': str(path.relative_to(root))}
    if json_mode:
        print_output(payload, True)
    else:
        if errors:
            for error in errors:
                print(error)
        else:
            print('Index validation passed.')
    return 0 if not errors and not card_errors else 1


def search(query: str, json_mode: bool = False) -> int:
    return cards_cmd.search_cards(query, json_mode)
