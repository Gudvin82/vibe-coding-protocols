# Audit Backlog Visualization

`v0.8.2` keeps backlog visualization local.
It does not introduce a hosted board.

Current local path:
- `python3 -m vcp_cli metrics board --json`
- `python3 -m vcp_cli dashboard build --output ./vcp-dashboard --json`

The dashboard artifact and metrics board summarize:
- backlog totals;
- status counts;
- priority counts when available;
- release-readiness context.

This is intended for inspection and review, not for workflow automation guarantees.
