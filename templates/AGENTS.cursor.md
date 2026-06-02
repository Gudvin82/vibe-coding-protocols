<!-- vcp-artifact: AGENTS_CURSOR -->
<!-- vcp-version: v0.5.2 -->
<!-- methodology-version: v1.4 -->

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

## Model routing / token-aware discovery

When broad code discovery is needed:
1. read Memory Bank first;
2. do targeted search before broad search;
3. if Cursor can simulate model routing, use a lighter read-only discovery pass first;
4. require an evidence map with `path:line`, symbol, snippet, why it matters and confidence;
5. keep the main implementation step focused on the touched files only;
6. run an independent review pass before merge or deploy.

## Remote safety

Before setup, template installation, push, PR, release or deploy:
- inspect `git remote -v`;
- confirm this is your project repository, not the source toolkit repository;
- do not push to the source toolkit repository by mistake;
- stop and ask when remote origin is unclear.
