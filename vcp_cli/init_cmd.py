from __future__ import annotations

from pathlib import Path

from .utils import print_output, repo_root

TARGET_NOTES = {
    "generic": "Use this when you just need a neutral onboarding prompt.",
    "claude": "Good for Claude Code or Claude chat workflows that respect repository files.",
    "codex": "Good for Codex / Codex desktop / terminal-agent workflows.",
    "cursor": "Good for Cursor chat or agent mode. Slash commands remain documentation conventions unless supported natively.",
    "windsurf": "Good for Windsurf chat or agent mode. Keep rule files and prompts aligned with local project docs.",
    "copilot": "Good for GitHub Copilot chat and repository instruction flows.",
}

TARGET_PROMPTS = {
    "generic": "Read START_HERE.md first. Choose the correct route for this project. Do not read the entire repository unless needed. Report the selected route, files needed, and files intentionally skipped. Preserve user changes. Run validation before final report.",
    "claude": "Read START_HERE.md first. Choose the correct route for this project. Use AI_INTAKE.md before recommending any file copy. Do not read the whole repo unless needed. Report the selected route, inspected files, skipped files, and required validation before final output.",
    "codex": "Read START_HERE.md first. Choose the correct route for this project. Use AI_INTAKE.md before recommending any file copy. Do not read the whole repo unless needed. Report the selected route, inspected files, skipped files, and validation plan before code changes.",
    "cursor": "Read START_HERE.md first. Choose the correct route for this project. Use AI_INTAKE.md before recommending any file copy. Keep the scope narrow, preserve user changes, and report inspected files, skipped files, and validation before final output.",
    "windsurf": "Read START_HERE.md first. Choose the correct route for this project. Use AI_INTAKE.md before recommending any file copy. Keep the scope narrow, preserve user changes, and report inspected files, skipped files, and validation before final output.",
    "copilot": "Read START_HERE.md first. Choose the correct route for this project. Use AI_INTAKE.md before recommending any file copy. Do not assume Starter if the repo already exists. Report selected route, inspected files, skipped files, and validation before code changes.",
}


def _guide(target: str, include_prompt: bool) -> str:
    root = repo_root()
    prompt_path = root / "templates/prompts/evaluate-vcp-for-my-repo.md"
    lines = [
        "# VCP Init",
        "",
        "VCP init is guidance-only in v0.5.8.",
        "It does not modify files by default.",
        "",
        f"Target: {target}",
        TARGET_NOTES[target],
        "",
        "## Recommended first steps",
        "1. Read `AI_INTAKE.md` before deciding what to copy.",
        "2. Run `vcp route --profile production` or another profile that matches the repo.",
        "3. Run `vcp adopt --pack production --dry-run` or another pack in dry-run mode.",
        "4. Merge only the relevant files manually. Do not copy everything blindly.",
        "5. Run validation before accepting AI-generated changes.",
        "",
        "## Useful commands",
        "```bash",
        "python3 -m vcp_cli doctor",
        "python3 -m vcp_cli route --profile production",
        "python3 -m vcp_cli adopt --pack production --dry-run",
        "```",
        "",
        f"Prompt template path: {prompt_path.relative_to(root)}",
    ]
    if include_prompt:
        lines += [
            "",
            "## Copy-paste prompt",
            "```text",
            TARGET_PROMPTS[target],
            "```",
        ]
    lines += [
        "",
        "## Safety reminder",
        "- Do not overwrite local `AGENTS.md`, `PROJECT_MAP.md`, `SECURITY.md` or CI files blindly.",
        "- Do not treat public or free third-party APIs as production-safe without intake.",
        "- Use the review gate before merge or release when the route requires it.",
    ]
    return "\n".join(lines) + "\n"


def run(target: str = "generic", print_prompt: bool = False, json_mode: bool = False, apply: bool = False) -> int:
    if apply:
        print("`vcp init --apply` is not implemented in v0.5.8. Init is guidance-only.")
        return 1
    if target not in TARGET_PROMPTS:
        print(f"Unknown init target: {target}")
        return 1
    if print_prompt:
        print(TARGET_PROMPTS[target])
        return 0
    payload = {
        "target": target,
        "guidance_only": True,
        "prompt_template": "templates/prompts/evaluate-vcp-for-my-repo.md",
        "recommended_commands": [
            "python3 -m vcp_cli doctor",
            "python3 -m vcp_cli route --profile production",
            "python3 -m vcp_cli adopt --pack production --dry-run",
        ],
        "warnings": [
            "Do not copy everything blindly.",
            "Do not overwrite project-specific AGENTS.md, PROJECT_MAP.md, SECURITY.md or CI files blindly.",
        ],
    }
    if json_mode:
        print_output(payload, True)
    else:
        print(_guide(target, include_prompt=True).rstrip())
    return 0
