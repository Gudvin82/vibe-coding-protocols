from __future__ import annotations

import json
from pathlib import Path

from .utils import repo_root, run_command

CHECKS = {
    "newline": ["python3", "scripts/check-newlines.py"],
    "links": ["python3", "scripts/validate-links.sh"],
    "version": ["bash", "scripts/check-version-consistency.sh"],
    "toolkit": ["bash", "scripts/check-toolkit.sh"],
    "audit": ["bash", "scripts/vibe-check.sh", "--audit", "--json"],
}


def run(fast: bool = False, full: bool = False, no_audit: bool = False, json_mode: bool = False) -> int:
    root = repo_root()
    selected = ["newline", "links", "version"] if fast else ["newline", "links", "version", "toolkit"]
    if full and "toolkit" not in selected:
        selected.append("toolkit")
    if not no_audit:
        selected.append("audit")
    results = []
    rc = 0
    for name in selected:
        proc = run_command(CHECKS[name], root)
        results.append({
            "name": name,
            "returncode": proc.returncode,
            "stdout": proc.stdout.strip(),
            "stderr": proc.stderr.strip(),
        })
        if proc.returncode != 0:
            rc = proc.returncode
    payload = {"ok": rc == 0, "checks": results}
    if json_mode:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        for item in results:
            print(f"[{item['returncode']}] {item['name']}")
            if item['stdout']:
                print(item['stdout'])
            if item['stderr']:
                print(item['stderr'])
    return rc
