import json
import subprocess


def test_cli_route_production_json():
    result = subprocess.run(["python3", "-m", "vcp_cli", "route", "--profile", "production", "--json"], text=True, capture_output=True, check=False)
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["selected_route"] == "Hardening Full"
    assert payload["adoption_pack"] == "production"
