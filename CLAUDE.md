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
