import json
import subprocess


def test_backlog_list_json():
    result = subprocess.run(["python3", "-m", "vcp_cli", "backlog", "list", "--json"], text=True, capture_output=True, check=False)
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["ok"] is True
    assert "items" in payload


def test_backlog_report_json():
    result = subprocess.run(["python3", "-m", "vcp_cli", "backlog", "report", "--json"], text=True, capture_output=True, check=False)
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["ok"] is True
    assert "counts_by_status" in payload


def test_backlog_add_dry_run_json():
    result = subprocess.run([
        "python3", "-m", "vcp_cli", "backlog", "add",
        "--title", "Synthetic backlog test item",
        "--type", "idea",
        "--priority", "P3",
        "--source", "manual",
        "--dry-run",
        "--json",
    ], text=True, capture_output=True, check=False)
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["action"] == "add"
    assert payload["write_result"]["dry_run"] is True


def test_backlog_move_done_archive_dry_run_json():
    for args, action in [
        (["move", "--id", "VCP-001", "--status", "doing", "--dry-run", "--json"], "move"),
        (["done", "--id", "VCP-001", "--validation", "tests green", "--review", "accepted", "--dry-run", "--json"], "move"),
        (["archive", "--id", "VCP-002", "--reason", "Not in scope", "--dry-run", "--json"], "move"),
    ]:
        result = subprocess.run(["python3", "-m", "vcp_cli", "backlog", *args], text=True, capture_output=True, check=False)
        assert result.returncode == 0
        payload = json.loads(result.stdout)
        assert payload["action"] == action
        assert payload["write_result"]["dry_run"] is True
