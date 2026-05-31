from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*args: str) -> dict:
    proc = subprocess.run([sys.executable, '-m', 'vcp_cli', *args], cwd=ROOT, text=True, capture_output=True, check=False)
    assert proc.returncode == 0, proc.stderr
    return json.loads(proc.stdout)


def test_fast_check_is_python_native() -> None:
    payload = run('check', '--fast', '--json')
    assert payload['ok'] is True
    assert payload['mode'] == 'fast'


def test_third_party_api_route_exists() -> None:
    payload = run('route', '--profile', 'third-party-api', '--json')
    assert payload['manifest_route_id'] == 'third-party-api-intake'
    assert payload['adoption_pack'] == 'third-party-api'
