# Audit Backlog Dedup and Staleness

Inside the MVP-to-Launch Path, the audit backlog acts as the visible risk backlog between initial surface scan and human launch decision.

Audit findings should be managed as backlog items with deduplication and staleness tracking.

Example file:
- `.vcp/audit-backlog.example.json`

Statuses:
- `active`
- `resolved`
- `stale`
- `superseded`
- `accepted-risk`

Fingerprints help prevent duplicate findings from being treated as new evidence.
