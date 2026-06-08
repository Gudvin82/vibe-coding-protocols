import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRENT = (ROOT / "VERSION").read_text(encoding="utf-8").strip()


def test_cli_version_json():
    result = subprocess.run(["python3", "-m", "vcp_cli", "version", "--json"], text=True, capture_output=True, check=False)
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["repository_package"] == CURRENT
    assert payload["legacy_methodology_reference"] == "v1.4"
