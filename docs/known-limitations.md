# Known Limitations

## Improved in v0.5.3

- VCP now has an explicit operations feedback loop for read-only production observation and daily triage.
- `PROJECT_BACKLOG.md` now exists as a separate working kanban next to `AUDIT_BACKLOG.md`.
- The local CLI now validates backlog structure and can print a backlog template.
- Benchmarks and manifests now cover operations and backlog workflows.

## Still limited

- legacy Bash script parity on native Windows is not complete;
- VCP does not automatically review vendor terms or legal compatibility;
- VCP does not auto-connect or test external APIs;
- VCP does not provide real API monitoring integration;
- the operations route is documentation-first, not a live observability product;
- authenticated GitHub Release creation still depends on external auth tooling;
- npm distribution is local-wrapper-only until a real published package exists.
