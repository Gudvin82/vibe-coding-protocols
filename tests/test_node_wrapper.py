import subprocess


def test_node_wrapper_version():
    result = subprocess.run(["node", "bin/vcp-node.js", "version"], text=True, capture_output=True, check=False)
    assert result.returncode == 0
    assert "Repository package: v0.5.6" in result.stdout
