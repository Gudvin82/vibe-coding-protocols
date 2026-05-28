from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


def locate_script() -> Path | None:
    cwd = Path.cwd().resolve()
    for base in (cwd, Path(__file__).resolve().parents[1]):
        candidate = base / "scripts" / "vibe-check.sh"
        if candidate.exists():
            return candidate
    for parent in cwd.parents:
        candidate = parent / "scripts" / "vibe-check.sh"
        if candidate.exists():
            return candidate
    return None


def main() -> int:
    if shutil.which("bash") is None:
        print("bash was not found. Use Git Bash, WSL or another Bash-capable environment.", file=sys.stderr)
        return 1

    script = locate_script()
    if script is None:
        print(
            "Could not locate scripts/vibe-check.sh. Use this wrapper inside a VCP-enabled repository or clone the toolkit first.",
            file=sys.stderr,
        )
        return 1

    args = sys.argv[1:] or ["doctor"]
    normalized = [f"--{arg}" if not arg.startswith("-") else arg for arg in args]
    result = subprocess.run(["bash", str(script), *normalized], cwd=Path.cwd())
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
