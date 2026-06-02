from pathlib import Path

from vcp_cli.utils import manifest_paths, repo_root


def test_manifests_live_under_vcp_dir():
    root = repo_root(Path(__file__).resolve())
    paths = manifest_paths(root)
    assert all(path.exists() for path in paths.values())
    assert all('.vcp/manifests/' in str(path).replace('\\', '/') for path in paths.values())
