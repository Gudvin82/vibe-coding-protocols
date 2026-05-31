from __future__ import annotations

from .fast_checks import repo_root, run_fast_checks, run_full_bash_checks, summarize_results
from .utils import print_output


def run(fast: bool = False, full: bool = False, no_audit: bool = False, json_mode: bool = False) -> int:
    root = repo_root()
    mode = "full" if full else "fast"
    results = run_fast_checks(root)
    if full:
        results.extend(run_full_bash_checks(root, include_audit=not no_audit))
    ok, passed, failed, skipped = summarize_results(results)
    payload = {
        "ok": ok,
        "mode": mode,
        "checks": results,
        "summary": {
            "passed": passed,
            "failed": failed,
            "skipped": skipped,
        },
        "notes": [
            "Fast mode is Python-native and intended to work on PowerShell without Bash.",
            "Full mode may call legacy Bash scripts when Bash is available.",
        ],
    }
    if json_mode:
        print_output(payload, True)
    else:
        print(f"Mode: {mode}")
        for item in results:
            print(f"[{item.get('status')}] {item.get('name')} ({item.get('runner')})")
            if item.get("reason"):
                print(item["reason"])
            if item.get("note"):
                print(item["note"])
            if item.get("stdout"):
                print(item["stdout"])
            for error in item.get("errors", []):
                print(f"- {error}")
            if item.get("stderr"):
                print(item["stderr"])
        print(f"Summary: {passed} passed, {failed} failed, {skipped} skipped")
    return 0 if ok else 1
