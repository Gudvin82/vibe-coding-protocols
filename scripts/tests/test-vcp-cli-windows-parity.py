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
    assert any(item['name'] == 'Third-party API intake / registry' for item in score['categories'])
    prompt = run('init', '--print-prompt')
    assert 'Read START_HERE.md first.' in prompt
    npm_doctor = run_npm('doctor')
    assert 'Repository package:' in npm_doctor
    print('Windows parity CLI smoke passed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
