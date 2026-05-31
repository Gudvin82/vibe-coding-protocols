import subprocess


def test_cli_help():
    result = subprocess.run(["python3", "-m", "vcp_cli", "--help"], text=True, capture_output=True, check=False)
    assert result.returncode == 0
