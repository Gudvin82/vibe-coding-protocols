# Agent Instruction Templates

VCP ships copyable agent instruction templates for local use.

Available templates:
- `templates/agents/CLAUDE.md`
- `templates/agents/CODEX.md`
- `templates/agents/CURSOR_RULES.md`
- `templates/agents/AGENTS.md`

Optional command surface:

```bash
python3 -m vcp_cli agents template --agent codex --json
```

These templates are deterministic local files, not remote policies.
