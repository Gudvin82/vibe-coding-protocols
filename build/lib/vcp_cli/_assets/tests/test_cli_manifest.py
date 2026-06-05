import subprocess


def test_manifest_validate():
    result = subprocess.run(["python3", "-m", "vcp_cli", "manifest", "validate"], text=True, capture_output=True, check=False)
    assert result.returncode == 0
