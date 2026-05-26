# AGENTS for Cursor

Use this variant when Cursor Composer or similar editor-driven AI is in charge.

## Focus
- propose the changed-files plan first;
- keep file references explicit;
- prefer smaller diffs over broad rewrites;
- stop for dependency, auth, migration and workflow changes.

## Cursor-specific notes
- ask Composer for a compact evidence map before broad edits;
- keep implementation scoped to the named files;
- run validation after each meaningful slice;
- document deferred follow-up in `AUDIT_BACKLOG.md`.
