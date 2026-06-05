import subprocess


def test_benchmark_run():
    result = subprocess.run(["python3", "-m", "vcp_cli", "benchmark", "run"], text=True, capture_output=True, check=False)
    assert result.returncode == 0
