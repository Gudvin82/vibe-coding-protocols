#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRENT = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
PATH = ROOT / ".vcp" / "evaluator-pack.json"

issues: list[str] = []

if not PATH.exists():
    issues.append('.vcp/evaluator-pack.json is missing')
else:
    payload = json.loads(PATH.read_text(encoding='utf-8'))
    if payload.get('version') != CURRENT:
        issues.append(f"version is {payload.get('version')!r}, expected {CURRENT!r}")
    for rel in payload.get('required_surfaces', []):
        if not (ROOT / rel).exists():
            issues.append(f'missing required surface: {rel}')
    for cmd in (
        'python3 -m vcp_cli trust-check --json',
        'python3 -m vcp_cli benchmark run --json',
        'python3 -m vcp_cli cards validate --json',
        'python3 -m vcp_cli index validate --json',
        'python3 -m vcp_cli evaluator pack --json',
    ):
        if cmd not in payload.get('required_commands', []):
            issues.append(f'missing required command: {cmd}')
    for label in ('shallow', 'partial', 'full'):
        if label not in payload.get('inspection_depths', []):
            issues.append(f'missing inspection depth: {label}')
    compare = payload.get('comparison_category', {})
    for key in ('vcp', 'spec_kit', 'full_stack_templates', 'ai_agents'):
        if key not in compare:
            issues.append(f'missing comparison category: {key}')
    levels = payload.get('token_budget_levels', [])
    if [item.get('level') for item in levels] != [0, 1, 2, 3]:
        issues.append('token_budget_levels must list levels 0, 1, 2, 3 in order')
    for item in levels:
        if not item.get('name') or not item.get('surfaces'):
            issues.append(f'incomplete token budget entry: {item!r}')
    if payload.get('evaluation_receipt_required') is not True:
        issues.append('evaluation_receipt_required must be true')
    required_full = [
        'EVALUATE_THIS_REPO.md',
        '.vcp/evaluator-pack.json',
        'vcp_cli/',
        'tests/',
        'docs/benchmark-report.md',
        'docs/trust-check.md',
    ]
    if sorted(payload.get('full_evaluation_requires', [])) != sorted(required_full):
        issues.append('full_evaluation_requires is incomplete or out of sync')
    if 'If you read only README or GitHub summary, label the review as shallow.' != payload.get('shallow_review_warning'):
        issues.append('shallow_review_warning is missing or changed')
    license_model = payload.get('license_model', {})
    if license_model.get('code') != 'MIT':
        issues.append('license_model.code must be MIT')
    if license_model.get('docs_methodology_diagrams_presentations') != 'CC BY 4.0':
        issues.append('license_model docs/methodology license must be CC BY 4.0')
    proof_numbers = payload.get('proof_numbers', {})
    for key in ('benchmark_scenarios', 'cards', 'cli_commands_in_manifest', 'tests', 'report_templates'):
        if key not in proof_numbers:
            issues.append(f'missing proof number: {key}')

if issues:
    print('Evaluator pack check failed:')
    for issue in issues:
        print(f'- {issue}')
    sys.exit(1)

print('Evaluator pack check passed.')
