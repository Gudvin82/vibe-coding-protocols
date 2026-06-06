# Agent Instruction Templates

VCP ships copyable agent instruction templates for local use.

Available templates:
- `templates/agents/CLAUDE.md`
- `templates/agents/CODEX.md`
- `templates/agents/CURSOR_RULES.md`
- `templates/agents/AGENTS.md`

## Cost-aware model routing

These templates now separate:
- fast/cheap discovery work;
- strong/reasoning mutation work.

They do not claim automatic model switching, provider API automation, or official IDE integrations.

Optional command surface:

```bash
python3 -m vcp_cli agents template --agent codex --json
```

These templates are deterministic local files, not remote policies.
