# CLAUDE.md

Start here.

1. Read `README.md` first.
2. Ask what stage the project is in.
3. Use `protocols/ai-project-starter-protocol.md` if the project is new.
4. Use `protocols/ai-project-hardening-protocol.md` if code already exists.
5. Do not write code before the route is confirmed.
6. Use the Memory Bank: `README.md`, `AGENTS.md`, `PROJECT_MAP.md`, `ARCHITECTURE.md`, `AUDIT_BACKLOG.md`.
7. Respect Stop Conditions and approval gates.
8. Do not run destructive commands.
9. Do not access or expose secrets.
10. Use independent diff review before important merge or deploy decisions.

## Read-only discovery subagent

For large repositories, use a read-only subagent to map relevant files before editing.

The subagent should not modify files. It should return an evidence map only:
- `path:line`
- symbol / route / component
- relevant snippet or signature
- why it matters

## Model routing / token-aware discovery

When broad code discovery is needed:
1. read Memory Bank first;
2. use a cheaper or faster read-only discovery agent when available;
3. return only an evidence map with `path:line`, symbol, snippet, why it matters and confidence;
4. let the main implementation pass verify critical findings before editing;
5. run a separate review pass before important merge or deploy decisions.

If Claude Code model routing is available:
- use Haiku or a cheaper or faster model for read-only discovery;
- use the main model for planning and implementation;
- use a separate review pass for independent diff review.
