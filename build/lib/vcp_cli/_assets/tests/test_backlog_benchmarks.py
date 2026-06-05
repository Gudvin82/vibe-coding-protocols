import json
import subprocess


def test_backlog_benchmark_scenarios_present():
    result = subprocess.run(["python3", "-m", "vcp_cli", "benchmark", "run", "--json"], text=True, capture_output=True, check=False)
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    names = {item["scenario"] for item in payload["results"]}
    assert "project-backlog-update" in names
    assert "production-error-capture" in names
    assert "backlog-add-idea" in names
    assert "backlog-move-done-with-review" in names
    assert "backlog-archive-not-taken" in names
    assert "backlog-architecture-impact" in names
