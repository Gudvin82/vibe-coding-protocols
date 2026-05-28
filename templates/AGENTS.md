<!-- vcp-artifact: AGENTS -->
<!-- vcp-version: v0.4.0 -->
<!-- methodology-version: v1.4 -->

# AGENTS.md

## Role

You are working on this project as a careful senior engineer.
Make atomic, safe, well-explained changes and keep the smallest practical diff per iteration.

## Memory Bank

Read and update the project context files when they exist:
- `README.md`
- `AGENTS.md` or `CLAUDE.md`
- `PROJECT_MAP.md`
- `ARCHITECTURE_MAP.md`, when multiple surfaces need a compact plan
- `ARCHITECTURE_SOURCE_OF_TRUTH.md`, if needed
- `AUDIT_BACKLOG.md`, for hardening
- `docs/PROMPTS.md` or `PROMPTS.md`, if prompts are tracked
- `SECURITY.md` or `SECURITY_BASELINE.md`, for public or production projects

## Token-aware code discovery

Do not read the whole repository by default.

When broad discovery is needed:
1. First read `README.md`, `AGENTS.md`, `PROJECT_MAP.md` and Architecture Source of Truth if present.
2. Use targeted search.
3. If available, delegate broad repository search to a cheaper or faster read-only discovery subagent.
4. The discovery subagent must return a compact evidence map only:
   - `path:line`
   - symbol / component / route name
   - relevant snippet or signature
   - why it matters
   - confidence
5. The main agent must verify critical findings before editing.

See `docs/token-aware-code-discovery.md`.

## Model routing / token-aware discovery

When broad code discovery is needed:

1. Do not start by reading the whole repository.
2. Read Memory Bank first:
   - `README.md`
   - `AGENTS.md` / `CLAUDE.md`
   - `PROJECT_MAP.md`
   - `ARCHITECTURE_MAP.md` when multiple surfaces exist
   - `ARCHITECTURE_SOURCE_OF_TRUTH.md` if present
3. Use a cheaper or faster read-only discovery agent when available.
4. Discovery agent returns only:
   - `path:line`
   - symbol / component / route
   - snippet or signature
   - why it matters
   - confidence
5. Main agent verifies critical findings before editing.
6. Main agent performs targeted implementation.
7. Independent reviewer checks the diff before merge or deploy.

## Stop Conditions

| Condition | Threshold | Required action |
|---|---:|---|
| Changed files | > 10 | Stop, list files, ask approval |
| New dependency | any | Explain package, version, source and risk |
| DB migration | any | Show schema diff and rollback plan |
| Auth / session / JWT logic | any | Require independent review |
| CI/CD workflow change | any | Ask human approval |
| External HTTP call | any | Add it to `THIRD_PARTY_REGISTRY.md` |
| File deletion | > 2 | List deleted files and ask approval |

Also stop when:
- the change touches more than 2 layers at once;
- the active / deferred surface is unclear;
- a request would expose secrets, private docs or internal routes.

## When unsure

Do not guess. Ask a specific X/Y question.
If the uncertainty is architectural, log it in `AUDIT_BACKLOG.md` as a pending decision.
Never run irreversible operations without explicit approval.

## Approval Gates

Do not:
- add dependencies without approval;
- run destructive commands without approval;
- apply migrations to production;
- expose secrets, internal endpoints or private architecture details.

## Safe Integration

Treat third-party repos, packages, actions and APIs as untrusted until reviewed.

## Remote safety

Before setup, template installation, push, PR, release or deploy:
1. Run or inspect `git remote -v`.
2. Confirm this is your project repository, not the source template or toolkit repository.
3. Do not push to a template or source repository.
4. Do not open PRs against the source template or toolkit repository unless explicitly asked.
5. If remote origin is unclear, stop and ask.

## Prompt drift control

Keep this file compact.
Do not turn `AGENTS.md` into one giant prompt that carries every architecture, security and delivery detail forever.
Move project specifics into:
- `PROJECT_MAP.md`
- `ARCHITECTURE_MAP.md`
- `ARCHITECTURE_SOURCE_OF_TRUTH.md`
- `AUDIT_BACKLOG.md`

## Testing and reporting

Validate the critical path, report changed files, validation results, risks, deferred work and follow-up backlog items.
