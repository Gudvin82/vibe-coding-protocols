#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
issues: list[str] = []

integrations = json.loads((ROOT / '.vcp' / 'integrations.json').read_text(encoding='utf-8'))
packs = json.loads((ROOT / '.vcp' / 'integration-packs.json').read_text(encoding='utf-8'))

status_by_id = {item['id']: item.get('status') for item in integrations.get('items', [])}
pack_status_by_id = {item['id']: item.get('status') for item in packs.get('items', [])}

checks = [
    ('docs/roadmap/vscode-extension.md', ['does not ship a VS Code extension', 'roadmap'], ['shipped extension', 'marketplace listing is live']),
    ('docs/dashboard.md', ['local dashboard artifact', 'not a hosted dashboard'], ['hosted dashboard is shipped']),
    ('docs/distribution.md', ['does not claim public PyPI or public npm publication'], ['published to PyPI', 'published to npm']),
    ('docs/pypi-publishing.md', ['does not claim a public PyPI release'], ['public PyPI release is live']),
    ('docs/plugins/README.md', ['not a plugin marketplace'], ['plugin marketplace is shipped']),
    ('README.md', ['not a hosted platform', 'not an official IDE extension'], ['hosted platform is live', 'official IDE extension shipped']),
    ('README_ru.md', ['hosted platform', 'VS Code extension'], ['official IDE extension shipped']),
]

for rel, required, forbidden in checks:
    text = (ROOT / rel).read_text(encoding='utf-8')
    for needle in required:
        if needle not in text:
            issues.append(f'{rel}: missing required boundary -> {needle}')
    for needle in forbidden:
        if needle in text:
            issues.append(f'{rel}: forbidden shipped claim -> {needle}')

if status_by_id.get('vs-code-extension') not in {None, 'roadmap', 'not-shipped'}:
    issues.append(f".vcp/integrations.json: vscode-extension status is {status_by_id.get('vs-code-extension')!r}, expected roadmap/not-shipped")
if status_by_id.get('hosted-dashboard') not in {None, 'roadmap', 'not-shipped'}:
    issues.append(f".vcp/integrations.json: dashboard-hosting status is {status_by_id.get('hosted-dashboard')!r}, expected roadmap/not-shipped")
if pack_status_by_id.get('future-ide-pack') not in {'roadmap', 'not-shipped'}:
    issues.append(f".vcp/integration-packs.json: future-ide-pack status is {pack_status_by_id.get('future-ide-pack')!r}, expected roadmap/not-shipped")
if pack_status_by_id.get('pypi-readiness-pack') not in {'experimental', 'local-template', 'shipped'}:
    issues.append(f".vcp/integration-packs.json: pypi-readiness-pack unexpected status {pack_status_by_id.get('pypi-readiness-pack')!r}")

if issues:
    print('Roadmap overclaim check failed:')
    for issue in issues:
        print(f'- {issue}')
    sys.exit(1)

print('Roadmap overclaim check passed.')
