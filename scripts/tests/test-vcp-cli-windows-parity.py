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
    route = json.loads(run('route', '--profile', 'third-party-api', '--json'))
    assert route['adoption_pack'] == 'third-party-api'
    adopt = json.loads(run('adopt', '--pack', 'third-party-api', '--dry-run', '--json'))
    assert adopt['pack'] == 'third-party-api'
    manifest = json.loads(run('manifest', 'validate', '--json'))
    assert manifest['ok'] is True
    benchmark = json.loads(run('benchmark', 'run', '--scenario', 'third-party-api-intake', '--json'))
    assert benchmark['ok'] is True
    score = json.loads(run('score', '--json'))
    assert any(item['name'] == 'Project Backlog' for item in score['categories'])
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
    npm_doctor = run_npm('doctor')
    assert 'Repository package:' in npm_doctor
    print('Windows parity CLI smoke passed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
