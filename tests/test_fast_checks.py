from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

from vcp_cli import fast_checks


def test_run_python_script_uses_runpy_for_non_py_extensions(monkeypatch, tmp_path: Path) -> None:
    captured: dict[str, object] = {}
    monkeypatch.setattr(fast_checks, "current_python", lambda: "py.exe")

    def fake_run_command(command: list[str], cwd: Path, capture: bool = True) -> SimpleNamespace:
        captured["command"] = command
        captured["cwd"] = cwd
        return SimpleNamespace(returncode=0, stdout="ok\n", stderr="")

    monkeypatch.setattr(fast_checks, "run_command", fake_run_command)

    result = fast_checks.run_python_script(tmp_path, "scripts/validate-links.sh")

    assert result["status"] == "PASS"
    command = captured["command"]
    assert command[:3] == ["py.exe", "-3", "-c"]
    assert "runpy.run_path" in command[3]
    assert "sys.argv=[path, *sys.argv[2:]]" in command[3]
    assert command[4] == str((tmp_path / "scripts/validate-links.sh").resolve())
    assert captured["cwd"] == tmp_path


def test_validate_cli_smoke_uses_windows_py_launcher_for_module_calls(monkeypatch, tmp_path: Path) -> None:
    commands: list[list[str]] = []
    monkeypatch.setattr(fast_checks, "current_python", lambda: "py.exe")
    monkeypatch.setattr(fast_checks, "CORE_SMOKE_COMMANDS", [["version", "--json"]])

    def fake_run_command(command: list[str], cwd: Path, capture: bool = True) -> SimpleNamespace:
        commands.append(command)
        return SimpleNamespace(returncode=0, stdout='{"version": "v0.5.9"}\n', stderr="")

    monkeypatch.setattr(fast_checks, "run_command", fake_run_command)

    result = fast_checks.validate_cli_smoke(tmp_path)

    assert result["status"] == "PASS"
    assert commands == [["py.exe", "-3", "-m", "vcp_cli", "version", "--json"]]
