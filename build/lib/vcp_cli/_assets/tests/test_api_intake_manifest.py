from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_api_intake_manifest_entries_exist() -> None:
    proc = subprocess.run([sys.executable, '-m', 'vcp_cli', 'manifest', 'validate', '--json'], cwd=ROOT, text=True, capture_output=True, check=False)
    assert proc.returncode == 0, proc.stderr
    payload = json.loads(proc.stdout)
    assert payload['ok'] is True
