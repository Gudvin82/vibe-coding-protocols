# Known Limitations

## Improved in v0.5.4

- VCP now has an explicit operations feedback loop for read-only production observation and daily triage.
- `PROJECT_BACKLOG.md` now behaves like a working kanban next to `AUDIT_BACKLOG.md`.
- The local CLI now lists, adds, moves, completes, archives, and reports backlog items.
- Real backlog writes are backed up under `.vcp/runtime/backups/`.
- Benchmarks and manifests now cover the richer backlog workflow.

## Still limited

- legacy Bash script parity on native Windows is not complete;
- VCP does not automatically review vendor terms or legal compatibility;
- VCP does not auto-connect or test external APIs;
- VCP does not provide real API monitoring integration;
- the operations route is documentation-first, not a live observability product;
- authenticated GitHub Release creation still depends on external auth tooling;
- npm distribution is local-wrapper-only until a real published package exists.
