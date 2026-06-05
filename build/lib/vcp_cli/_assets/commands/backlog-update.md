# /backlog-update

Use this command when a user gives a new idea, task, request, follow-up, deferred item, or architecture-affecting change.

## Return

- backlog item ID;
- current state (`TODO`, `DOING`, `DONE`, or `ARCHIVED / NOT TAKEN`);
- why the state changed;
- linked docs that must be updated;
- architecture impact level;
- validation or review expected next.

## ID convention

- Default VCP IDs use `VCP-001`, `VCP-002`, `VCP-003`.
- Copied projects may choose prefixes such as `PROJECT-001` or `APP-001`.
- Keep IDs stable and unique.
- Do not renumber existing items.
- If duplicates are merged, keep the oldest ID and mention merged IDs in notes.

## Workflow

1. Capture the idea, task, request, or follow-up.
2. Check the backlog for duplicates first.
3. Add or update the backlog item.
4. Decide the route.
5. Decide architecture impact.
6. If the task is accepted for work, move it to `DOING`.
7. When done, attach validation and review evidence.
8. Move it to `DONE`.
9. If rejected or deferred, move it to `ARCHIVED / NOT TAKEN` with reason.
10. If architecture changed, update architecture docs or create a follow-up backlog item.

## Rules

1. Add or update a `PROJECT_BACKLOG.md` item before implementation starts.
2. Do not silently lose tasks in chat history.
3. Move accepted active work into `DOING`.
4. Move completed validated work into `DONE`.
5. Move rejected or deferred work into `ARCHIVED / NOT TAKEN` with reason.
6. If architecture impact is not `none`, update `PROJECT_MAP.md` and related architecture docs in the same task or create a follow-up backlog item.
7. If the task is also a security or hardening risk, update `AUDIT_BACKLOG.md` too.
8. If third-party APIs or dependencies are involved, update `THIRD_PARTY_REGISTRY.md` too.
9. If the task came from production error triage, link the error inbox entry.
10. If the task came from review findings, link the review report or finding note.
