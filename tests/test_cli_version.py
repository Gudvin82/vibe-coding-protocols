import json
import subprocess


def test_cli_version_json():
    result = subprocess.run(["python3", "-m", "vcp_cli", "version", "--json"], text=True, capture_output=True, check=False)
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["repository_package"] == "v0.7.1"
    assert payload["legacy_methodology_reference"] == "v1.4"
