#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PYTHON = sys.executable


def run(*args: str) -> str:
    proc = subprocess.run([PYTHON, '-m', 'vcp_cli', *args], cwd=ROOT, text=True, capture_output=True, check=False)
    if proc.returncode != 0:
        raise SystemExit(f"Command failed: {' '.join(args)}\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}")
    return proc.stdout


def run_npm(*args: str) -> str:
    proc = subprocess.run(['npm', 'run', 'vcp', '--', *args], cwd=ROOT, text=True, capture_output=True, check=False)
    if proc.returncode != 0:
        raise SystemExit(f"npm wrapper failed: {' '.join(args)}\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}")
    return proc.stdout


def main() -> int:
    doctor = json.loads(run('doctor', '--json'))
    assert 'powershell_first_mode_supported' in doctor
    assert '.vcp/manifests' in doctor['manifest_directory']
    check = json.loads(run('check', '--fast', '--json'))
    assert check['ok'] is True
    evaluate = json.loads(run('evaluate', '--json'))
    assert evaluate['evaluation_guide_present'] is True
    assert evaluate['progressive_disclosure_present'] is True
    route = json.loads(run('route', '--profile', 'third-party-api', '--json'))
    assert route['adoption_pack'] == 'third-party-api'
    public_growth_route = json.loads(run('route', '--profile', 'public-growth', '--json'))
    assert public_growth_route['adoption_pack'] == 'public-growth'
    spec_first_route = json.loads(run('route', '--profile', 'spec-first', '--json'))
    assert spec_first_route['adoption_pack'] == 'spec-first'
    adopt = json.loads(run('adopt', '--pack', 'third-party-api', '--dry-run', '--json'))
    assert adopt['pack'] == 'third-party-api'
    public_growth_adopt = json.loads(run('adopt', '--pack', 'public-growth', '--dry-run', '--json'))
    assert public_growth_adopt['pack'] == 'public-growth'
    spec_first_adopt = json.loads(run('adopt', '--pack', 'spec-first', '--dry-run', '--json'))
    assert spec_first_adopt['pack'] == 'spec-first'
    manifest = json.loads(run('manifest', 'validate', '--json'))
    assert manifest['ok'] is True
    index_validate = json.loads(run('index', 'validate', '--json'))
    assert index_validate['ok'] is True
    index_show = json.loads(run('index', 'show', '--json'))
    assert index_show['version'] == 'v0.6.0'
    index_search = json.loads(run('index', 'search', 'production', '--json'))
    assert index_search['query'] == 'production'
    cards_list = json.loads(run('cards', 'list', '--json'))
    assert cards_list['total'] > 0
    cards_recommended = json.loads(run('cards', 'list', '--recommended', '--json'))
    assert 'items' in cards_recommended
    cards_maturity = json.loads(run('cards', 'list', '--maturity', 'stable', '--json'))
    assert 'items' in cards_maturity
    cards_platform = json.loads(run('cards', 'list', '--platform', 'codex-cli', '--json'))
    assert 'items' in cards_platform
    cards_validate = json.loads(run('cards', 'validate', '--json'))
    assert cards_validate['ok'] is True
    card_show = json.loads(run('cards', 'show', 'production-hardening', '--json'))
    assert card_show['id'] == 'production-hardening'
    spec_validate = json.loads(run('spec', 'validate', '--json'))
    assert 'spec_files' in spec_validate
    assert '# Product Requirements Document' in run('spec', 'template', 'prd')
    spec_summary = json.loads(run('spec', 'summary', '--json'))
    assert 'recommended_flow' in spec_summary
    spec_depth = json.loads(run('spec', 'depth', '--task', 'copy-only docs fix', '--json'))
    assert spec_depth['recommended_spec_depth'] == 'no-spec'
    spec_skip = json.loads(run('spec', 'skip-check', '--task', 'copy-only docs fix', '--json'))
    assert spec_skip['safe_to_skip_spec'] is True
    spec_questions = json.loads(run('spec', 'questions', '--idea', 'build a customer portal', '--json'))
    assert spec_questions['one_question_at_a_time'] is True
    spec_retrofit = json.loads(run('spec', 'retrofit', '--scope', 'auth', '--dry-run', '--json'))
    assert spec_retrofit['writes_source_code'] is False
    spec_freshness = json.loads(run('spec', 'freshness', '--json'))
    assert 'summary' in spec_freshness
    preset_list = json.loads(run('preset', 'list', '--json'))
    assert preset_list['total'] == 5
    preset_show = json.loads(run('preset', 'show', 'solo-founder', '--json'))
    assert preset_show['id'] == 'solo-founder'
    preset_validate = json.loads(run('preset', 'validate', '--json'))
    assert preset_validate['ok'] is True
    platform_cards = json.loads(run('cards', 'list', '--type', 'platform', '--json'))
    assert platform_cards['total'] == 27
    workflow_list = json.loads(run('workflow', 'list', '--json'))
    assert workflow_list['total'] > 0
    workflow_validate = json.loads(run('workflow', 'validate', '--json'))
    assert workflow_validate['ok'] is True
    workflow_show = json.loads(run('workflow', 'show', 'production-hardening', '--json'))
    assert workflow_show['id'] == 'production-hardening'
    workflow_search = json.loads(run('workflow', 'search', 'hardening', '--json'))
    assert workflow_search['query'] == 'hardening'
    diagnose = json.loads(run('diagnose', '--json'))
    assert 'difference_from_doctor' in diagnose
    diagnose_production = json.loads(run('diagnose', '--profile', 'production', '--json'))
    assert diagnose_production['profile'] == 'production'
    benchmark = json.loads(run('benchmark', 'run', '--scenario', 'third-party-api-intake', '--json'))
    assert benchmark['ok'] is True
    score = json.loads(run('score', '--json'))
    assert any(item['name'] == 'Spec lane' for item in score['categories'])
    backlog_list = json.loads(run('backlog', 'list', '--json'))
    assert backlog_list['ok'] is True
    backlog_report = json.loads(run('backlog', 'report', '--json'))
    assert backlog_report['ok'] is True
    backlog_add = json.loads(run('backlog', 'add', '--title', 'Synthetic backlog test item', '--type', 'idea', '--priority', 'P3', '--source', 'manual', '--dry-run', '--json'))
    assert backlog_add['write_result']['dry_run'] is True
    backlog_move = json.loads(run('backlog', 'move', '--id', 'VCP-001', '--status', 'doing', '--dry-run', '--json'))
    assert backlog_move['write_result']['dry_run'] is True
    backlog_done = json.loads(run('backlog', 'done', '--id', 'VCP-001', '--validation', 'tests green', '--review', 'accepted', '--dry-run', '--json'))
    assert backlog_done['write_result']['dry_run'] is True
    backlog_archive = json.loads(run('backlog', 'archive', '--id', 'VCP-002', '--reason', 'Synthetic archive path', '--dry-run', '--json'))
    assert backlog_archive['write_result']['dry_run'] is True
    prompt = run('init', '--print-prompt')
    assert 'Read START_HERE.md first.' in prompt
    eval_prompt = run('evaluate', '--print-prompt')
    assert 'Do not judge from README alone.' in eval_prompt
    npm_doctor = run_npm('doctor')
    assert 'Repository package:' in npm_doctor
    npm_evaluate = run_npm('evaluate')
    assert 'Evaluation guide present:' in npm_evaluate
    npm_index = run_npm('index', 'validate')
    assert 'Index validation passed.' in npm_index
    npm_workflow = run_npm('workflow', 'validate')
    assert 'Workflow validation passed.' in npm_workflow
    print('Windows parity CLI smoke passed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
