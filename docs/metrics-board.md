# Metrics Board

The metrics board is a conservative local summary surface.

Use:

```bash
python3 -m vcp_cli metrics board --json
```

Current local signals include:
- card count;
- benchmark scenario count;
- report template count;
- command count;
- release-readiness status;
- audit backlog counts;
- integration status counts.

These metrics are useful for demos, local review, and repository inspection.
They are not objective truth and not a production readiness guarantee.
