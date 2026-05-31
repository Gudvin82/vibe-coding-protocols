import json
import subprocess


def test_score_json():
    result = subprocess.run(["python3", "-m", "vcp_cli", "score", "--json"], text=True, capture_output=True, check=False)
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert "categories" in payload
