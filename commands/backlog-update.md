# /backlog-update

Use this command when a user gives a new idea, task, request, follow-up, deferred item, or architecture-affecting change.

## Return

- backlog item ID;
- current state (`TODO`, `DOING`, `DONE`, or `ARCHIVED / NOT TAKEN`);
- why the state changed;
- linked docs that must be updated;
- architecture impact level;
- validation or review expected next.

## Rules

1. Add or update a `PROJECT_BACKLOG.md` item before implementation starts.
2. Do not silently lose tasks in chat history.
3. Move accepted active work into `DOING`.
4. Move completed validated work into `DONE`.
5. Move rejected or deferred work into `ARCHIVED / NOT TAKEN` with reason.
6. If architecture impact is not `none`, update `PROJECT_MAP.md` and related architecture docs in the same task or create a follow-up backlog item.
7. If the task is also a security or hardening risk, update `AUDIT_BACKLOG.md` too.
8. If third-party APIs or dependencies are involved, update `THIRD_PARTY_REGISTRY.md` too.
