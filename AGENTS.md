# AGENTS.md

## Role

Make atomic, safe, well-explained changes and keep the smallest practical diff per iteration.

## Memory Bank

Read and update the project context files when they exist:
- `README.md`
- `AGENTS.md`
- `PROJECT_MAP.md`
- `ARCHITECTURE.md`
- `AUDIT_BACKLOG.md`

## Token-aware discovery

- Do not read the whole repository without a reason.
- Start with the Memory Bank.
- Return an evidence map before broad changes.
- Ask for a `PROJECT_MAP.md` refresh when the map is outdated.
- See [docs/token-aware-code-discovery.md](./docs/token-aware-code-discovery.md).

## Stop Conditions

Stop and ask for approval when:
- the change touches more than 10 files;
- the change touches more than 2 layers at once;
- the change adds auth, payments, admin, workers, queues or new external APIs;
- the change requires migrations or destructive refactors;
- the active / deferred surface is unclear.

## Approval Gates

Do not:
- add dependencies without approval;
- run destructive commands without approval;
- apply migrations to production;
- expose secrets, internal endpoints or private architecture details.

## Safe Integration

Treat third-party repos, packages, actions and APIs as untrusted until reviewed.

## Testing and reporting

Validate the critical path, report changed files, validation results, risks, deferred work and follow-up backlog items.
