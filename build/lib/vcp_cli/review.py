from __future__ import annotations

from .utils import git_status_short, print_output, repo_root, run_command

PROMPT_PATH = "templates/prompts/loop-code-review.md"
REPORT_PATH = "templates/reports/code-review-report.md"
COMMAND_PATH = "commands/loop-code-review.md"
PROTOCOL_PATH = "protocols/review/post-task-code-review.md"


def _status_payload() -> dict:
    root = repo_root()
    return {
        "git_status_short": git_status_short(root),
        "prompt_path": PROMPT_PATH,
        "report_template_path": REPORT_PATH,
        "command_path": COMMAND_PATH,
        "protocol_path": PROTOCOL_PATH,
        "independence_rule": "Reviewer must be independent and read-only.",
    }


def plan(json_mode: bool = False) -> int:
    payload = {
        **_status_payload(),
        "next_step": "Inspect active git changes, collect validation output, then request independent review.",
    }
    if json_mode:
        print_output(payload, True)
    else:
        print("Post-task review plan")
        print(f"Prompt: {PROMPT_PATH}")
        print(f"Report: {REPORT_PATH}")
        print(f"Command doc: {COMMAND_PATH}")
        print("Reviewer rule: independent and read-only")
        print(f"Git status: {payload['git_status_short'] or 'clean'}")
    return 0


def prompt() -> int:
    print((repo_root() / PROMPT_PATH).read_text(encoding="utf-8"))
    return 0


def report_template() -> int:
    print((repo_root() / REPORT_PATH).read_text(encoding="utf-8"))
    return 0


def status(json_mode: bool = False) -> int:
    payload = _status_payload()
    if json_mode:
        print_output(payload, True)
    else:
        print(f"Git status: {payload['git_status_short'] or 'clean'}")
        print(f"Prompt path: {PROMPT_PATH}")
        print(f"Report path: {REPORT_PATH}")
        print(payload['independence_rule'])
    return 0
