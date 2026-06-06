
#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / '.vcp' / 'proof-counts.json').read_text(encoding='utf-8'))
issues: list[str] = []

evaluator = json.loads((ROOT / '.vcp' / 'evaluator-pack.json').read_text(encoding='utf-8'))
expected = data['counts']
proof = evaluator.get('proof_numbers', {})
mapping = {
    'benchmark_scenarios': expected['benchmark_scenarios'],
    'cards': expected['cards'],
    'cli_commands_in_manifest': expected['cli_commands_in_manifest'],
    'tests': expected['tests'],
    'report_templates': expected['report_templates'],
    'visual_diagrams': expected['visual_diagrams'],
    'agent_kits': expected['agent_kits'],
}
for key, value in mapping.items():
    if proof.get(key) != value:
        issues.append(f'evaluator pack proof number mismatch for {key}: {proof.get(key)!r} != {value!r}')

for rel in ['README.md', 'README_ru.md', 'docs/proof-snapshot.md', 'docs_ru/proof-snapshot.md', 'EVALUATE_THIS_REPO.md', 'REPO_CAPABILITIES_INDEX.md']:
    text = (ROOT / rel).read_text(encoding='utf-8')
    if '.vcp/proof-counts.json' not in text:
        issues.append(f'{rel} missing canonical proof-counts link')

if issues:
    print('Proof counts check failed:')
    for issue in issues:
        print(f'- {issue}')
    sys.exit(1)
print('Proof counts check passed.')
