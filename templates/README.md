# Templates

This is the `Artifact Pack` — working markdown templates you can copy into a project.

Included themes:
- Memory Bank and agent rules;
- architecture and project mapping;
- audit backlog and scanner reporting;
- third-party registry;
- security operations baseline.

AI / IDE variants:
- Root [`../AGENTS.md`](../AGENTS.md) configures this repository itself.
- Root [`../CLAUDE.md`](../CLAUDE.md) configures Claude Code for this repository.
- Copy-ready project template: [`AGENTS.md`](./AGENTS.md)
- Claude variant: [`AGENTS.claude.md`](./AGENTS.claude.md)
- Cursor variant: [`AGENTS.cursor.md`](./AGENTS.cursor.md)
- Windsurf variant: [`AGENTS.windsurf.md`](./AGENTS.windsurf.md)

## Which agent file should I copy?

- Root `AGENTS.md` configures this repository.
- Root `CLAUDE.md` configures Claude Code for this repository.
- Use `templates/AGENTS.md` as the generic copy-ready agent template for your project.
- Use `templates/AGENTS.claude.md` if you want Claude Code-specific rules.
- Use `templates/AGENTS.cursor.md` or `templates/AGENTS.windsurf.md` for Cursor or Windsurf-specific workflows.

Core memory files across the toolkit:
- `README.md`
- `AGENTS.md` or `CLAUDE.md`
- `PROJECT_MAP.md`
- `ARCHITECTURE_SOURCE_OF_TRUTH.md`, if needed
- `AUDIT_BACKLOG.md`, for hardening
- `docs/PROMPTS.md` or `PROMPTS.md`, if prompts are tracked
- `SECURITY.md` or `SECURITY_BASELINE.md`, for public or production projects

Recommended companions:
- [`../docs/template-style-guide.md`](../docs/template-style-guide.md)
- [`../docs/hardening-thresholds.md`](../docs/hardening-thresholds.md)
- [`../docs/scanner-integration.md`](../docs/scanner-integration.md)
- [`../docs/migration/README.md`](../docs/migration/README.md)

Important:
- these are public templates;
- these are not real private project docs;
- real `AGENTS.md`, `PROJECT_MAP.md`, `ARCHITECTURE.md`, incident docs and internal runbooks often contain sensitive details and should stay private / sanitized / encrypted.
