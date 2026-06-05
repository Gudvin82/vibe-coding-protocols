import json
import subprocess


def test_index_validate_json():
    result = subprocess.run(["python3", "-m", "vcp_cli", "index", "validate", "--json"], text=True, capture_output=True, check=False)
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["ok"] is True


def test_cards_show():
    result = subprocess.run(["python3", "-m", "vcp_cli", "cards", "show", "production-hardening", "--json"], text=True, capture_output=True, check=False)
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["id"] == "production-hardening"
