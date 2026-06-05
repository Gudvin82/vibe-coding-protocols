import json
import subprocess


def test_review_plan_json():
    result = subprocess.run(["python3", "-m", "vcp_cli", "review", "plan", "--json"], text=True, capture_output=True, check=False)
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["prompt_path"] == "templates/prompts/loop-code-review.md"
