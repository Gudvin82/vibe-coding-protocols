#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
CURRENT = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()
required = [
    'README_ru.md',
    'docs_ru/README.md',
    'docs_ru/install.md',
    'docs_ru/10-minute-adoption-path.md',
    'docs_ru/mvp-to-launch-path.md',
    'docs_ru/local-platform-flow.md',
    'docs_ru/dashboard.md',
    'docs_ru/integration-packs.md',
    'docs_ru/pr-gate.md',
    'docs_ru/comparisons.md',
    'docs_ru/product-model.md',
    'docs_ru/killer-workflow.md',
    'docs_ru/anti-misread-guide.md',
    'docs_ru/evaluator-architecture-map.md',
    'docs_ru/proof-snapshot.md',
    'docs_ru/external-evaluation.md',
    'docs_ru/public-surfaces.md',
    'docs_ru/demo-artifacts.md',
    'docs_ru/benchmark-report.md',
    'docs_ru/trust-check.md',
    'docs_ru/ai-tooling.md',
    'docs_ru/integration-setup.md',
    'docs_ru/agent-kits.md',
    'docs_ru/agent-model-routing.md',
    'docs_ru/evaluator-token-budget.md',
    'docs_ru/visuals.md',
    'docs_ru/visual-spec.md',
    'docs_ru/control-catalog.md',
    'docs_ru/change-intent.md',
    'docs_ru/starter-template-adoption.md',
    'docs_ru/agent-rule-profiles.md',
    'docs_ru/project-control-charter.md',
    'docs_ru/ecosystem-map.md',
    'docs_ru/agent-rule-provenance.md',
    'docs_ru/ai-augmented-solo-squad-path.md',
    'docs_ru/current-limitations.md',
    'docs_ru/proof-counts.md',
    'docs_ru/route-recommender.md',
    'docs_ru/guided-adoption-modes.md',
    'docs_ru/control-scorecard.md',
    'docs_ru/evidence-bundle.md',
    'docs_ru/release-decision-matrix.md',
    'docs_ru/anti-chaos-recovery-kit.md',
    'docs_ru/pr-readiness.md',
    'docs_ru/github-pr-gate.md',
    'docs_ru/integration-proof-matrix.md',
    'docs_ru/ai-tool-mode-packs.md',
    'docs_ru/evaluation-status-badges.md',
    'docs_ru/ai-ecosystem-watchlist.md',
    'docs_ru/model-tool-governance.md',
    'docs_ru/secure-agent-training-pack.md',
    'docs_ru/github-native-control-checklist.md',
    'docs_ru/ai-stack-adoption-checklist.md',
    'docs_ru/team-enablement-pack.md',
    'docs_ru/ecosystem-scouting-workflow.md',
    'docs_ru/release-v0.9.5.md',
]
issues = []
for rel in required:
    path = ROOT / rel
    if not path.exists() or not path.read_text(encoding='utf-8').strip():
        issues.append(f'missing or empty {rel}')
        continue
    text = path.read_text(encoding='utf-8')
    if rel in {'README_ru.md', 'docs_ru/README.md', 'docs_ru/release-v0.9.5.md', 'docs_ru/benchmark-report.md', 'docs_ru/trust-check.md'} and CURRENT not in text:
        issues.append(f'{rel} missing current version {CURRENT}')
    if rel == 'docs_ru/README.md':
        for needle in (
            'Если вы даёте VCP своему ИИ-агенту',
            'Как не дать ИИ неправильно оценить VCP',
            'AGENTS.md',
            'AI_EVALUATION_GUIDE.md',
            'EVALUATE_THIS_REPO.md',
            'llms.txt',
            '.vcp/index.json',
            '.vcp/catalog.json',
            '.vcp/manifests/',
            '.vcp/cards/',
            '.vcp/workflows/',
            'docs/benchmark-report.md',
            'docs/trust-check.md',
            'shallow',
            'partial',
            'full',
            'английских docs',
            'agent-model-routing.md',
            'evaluator-token-budget.md',
            'control-catalog.md',
            'change-intent.md',
            'starter-template-adoption.md',
            'agent-rule-profiles.md',
            'project-control-charter.md',
            'ecosystem-map.md',
            'ai-augmented-solo-squad-path.md',
            'docs_ru/current-limitations.md',
            'docs_ru/route-recommender.md',
            'docs_ru/evidence-bundle.md',
            'docs_ru/pr-readiness.md',
            'AI ecosystem governance в VCP',
            'docs_ru/ai-ecosystem-watchlist.md',
            'docs_ru/model-tool-governance.md',
            'docs_ru/secure-agent-training-pack.md',
            'docs_ru/github-native-control-checklist.md',
            'docs_ru/ai-stack-adoption-checklist.md',
            'docs_ru/team-enablement-pack.md',
            'docs_ru/ecosystem-scouting-workflow.md',
        ):
            if needle not in text:
                issues.append(f'docs_ru/README.md missing required guidance: {needle}')
    if rel == 'docs_ru/current-limitations.md':
        for needle in (
            'VCP специально остаётся local-first.',
            'Это не SaaS, не hosted dashboard, не marketplace и не official IDE extension.',
            'VCP не создаёт PR автоматически, не делает auto-merge и не является',
            'VCP даёт local artifacts, CLI checks, agent kits, PR Gate, proof',
        ):
            if needle not in text:
                issues.append(f'docs_ru/current-limitations.md missing required phrase: {needle}')
    if rel == 'docs_ru/route-recommender.md':
        for needle in ('быстрый MVP', 'новый проект', 'текущий проект', 'raw AI MVP', 'release decision', 'brownfield rescue', 'client rollout', 'AI chaos recovery', 'deep hardening'):
            if needle not in text:
                issues.append(f'docs_ru/route-recommender.md missing scenario: {needle}')
    if rel == 'docs_ru/evidence-bundle.md':
        for needle in ('ревьюеру', 'техлиду', 'клиенту', 'внешнему evaluator', 'AI-агенту', 'команде перед PR/release'):
            if needle not in text:
                issues.append(f'docs_ru/evidence-bundle.md missing audience: {needle}')
    if rel == 'docs_ru/pr-readiness.md':
        if 'PR Readiness не создаёт PR автоматически.' not in text:
            issues.append('docs_ru/pr-readiness.md missing no-auto-PR guard')
    if rel == 'docs_ru/integration-proof-matrix.md':
        for needle in ('Integration Proof Matrix не означает official integrations.', 'Claude Code', 'Codex', 'Cursor', 'GitHub Copilot', 'GitHub Actions'):
            if needle not in text:
                issues.append(f'docs_ru/integration-proof-matrix.md missing: {needle}')
    if rel == 'docs_ru/evaluation-status-badges.md':
        for needle in ('честные внутренние status labels', 'не сертификаты и не гарантии', 'не означают production safety, compliance или launch success'):
            if needle not in text:
                issues.append(f'docs_ru/evaluation-status-badges.md missing: {needle}')
if issues:
    print('Russian docs parity check failed:')
    for issue in issues:
        print(f'- {issue}')
    sys.exit(1)
print('Russian docs parity check passed.')
