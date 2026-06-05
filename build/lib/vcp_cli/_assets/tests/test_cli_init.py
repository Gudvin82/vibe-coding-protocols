import subprocess


def test_cli_init_print_prompt():
    result = subprocess.run(["python3", "-m", "vcp_cli", "init", "--print-prompt"], text=True, capture_output=True, check=False)
    assert result.returncode == 0
    assert "Read START_HERE.md first." in result.stdout
