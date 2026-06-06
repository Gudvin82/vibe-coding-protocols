from __future__ import annotations

from pathlib import Path

from .utils import print_output, repo_root

TEMPLATES = {
    "claude": "templates/agents/CLAUDE.md",
    "codex": "templates/agents/CODEX.md",
    "copilot": "templates/agents/COPILOT_INSTRUCTIONS.md",
    "cursor": "templates/agents/CURSOR_RULES.md",
    "agents": "templates/agents/AGENTS.md",
}


def template_payload(agent: str, root: Path | None = None) -> dict[str, object]:
    root = repo_root(root)
    if agent not in TEMPLATES:
        return {"ok": False, "error": f"Unknown agent template: {agent}", "available": sorted(TEMPLATES)}
    path = root / TEMPLATES[agent]
    return {"ok": True, "agent": agent, "path": str(path), "content": path.read_text(encoding='utf-8')}


def run_template(agent: str, output: str | None = None, confirm: bool = False, json_mode: bool = False) -> int:
    payload = template_payload(agent)
    if not payload["ok"]:
        print_output(payload, json_mode)
        return 1
    if output:
        target = Path(output)
        if not target.is_absolute():
            target = (Path.cwd() / target).resolve()
        if target.exists() and not confirm:
            print_output({"ok": False, "error": "Target exists. Re-run with --confirm to overwrite.", "target": str(target)}, json_mode)
            return 1
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(payload["content"], encoding="utf-8")
        payload = {k: v for k, v in payload.items() if k != "content"}
        payload["written"] = str(target)
    print_output(payload, json_mode)
    return 0
