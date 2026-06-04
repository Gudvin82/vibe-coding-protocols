import subprocess
from pathlib import Path


def test_node_wrapper_version():
    result = subprocess.run(["node", "bin/vcp-node.js", "version"], text=True, capture_output=True, check=False)
    assert result.returncode == 0
    expected_version = Path("VERSION").read_text(encoding="utf-8").strip()
    assert f"Repository package: {expected_version}" in result.stdout
