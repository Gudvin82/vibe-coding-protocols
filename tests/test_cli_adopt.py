import json
import subprocess


def test_cli_adopt_production_json():
    result = subprocess.run(["python3", "-m", "vcp_cli", "adopt", "--pack", "production", "--dry-run", "--json"], text=True, capture_output=True, check=False)
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["pack"] == "production"
    assert "AGENTS.md" in payload["protected_files"]


def test_cli_adopt_public_growth_json():
    result = subprocess.run(["python3", "-m", "vcp_cli", "adopt", "--pack", "public-growth", "--dry-run", "--json"], text=True, capture_output=True, check=False)
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["pack"] == "public-growth"
    assert "SECURITY.md" in payload["files_to_skip"]
