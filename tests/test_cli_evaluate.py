import json
import subprocess
from pathlib import Path


def test_cli_evaluate_json():
    result = subprocess.run(["python3", "-m", "vcp_cli", "evaluate", "--json"], text=True, capture_output=True, check=False)
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    expected_version = Path("VERSION").read_text(encoding="utf-8").strip()
    assert payload["repository_package"] == expected_version
    assert payload["evaluation_guide_present"] is True
    assert payload["operations_workflow_present"] is True


def test_cli_evaluate_prompt():
    result = subprocess.run(["python3", "-m", "vcp_cli", "evaluate", "--print-prompt"], text=True, capture_output=True, check=False)
    assert result.returncode == 0
    assert "Do not judge from README alone." in result.stdout
