<!-- vcp-artifact: SECURITY_OPERATIONS_BASELINE -->
<!-- vcp-version: v0.5.5 -->
<!-- methodology-version: v1.4 -->

# Security Operations Baseline

## Ownership

- Security owner: [FILL IN: person or role]
- Backup owner: [FILL IN: person or role]
- Incident owner: [FILL IN: person or role]
- Dependency owner: [FILL IN: person or role]

## Recurring checks

| Check | Cadence | Owner | Evidence location | Last run | Next run |
|---|---|---|---|---|---|
| Secret scan | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| Dependency scan | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| Public exposure check | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| Open ports/service inventory | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| Security headers check | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| Backup/restore drill | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| Admin access review | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| Third-party registry review | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| Logs/retention review | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |
| Accepted risks review | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

## Suggested recurring checks

- Secret scan
- Dependency scan
- Public exposure check
- Open ports/service inventory
- Security headers check
- Backup/restore drill
- Admin access review
- Third-party registry review
- Logs/retention review
- Accepted risks review

## Patch and update policy

- Critical patch SLA: [FILL IN]
- High patch SLA: [FILL IN]
- Dependency update cadence: [FILL IN]
- Emergency dependency patch path: [FILL IN]
- Rollback owner: [FILL IN]

## Alerts

- What alerts exist: [FILL IN]
- Where alerts go: [FILL IN]
- Who responds: [FILL IN]
- Escalation path: [FILL IN]

## Evidence

- Scanner reports: [FILL IN]
- Screenshots: [FILL IN]
- CI logs: [FILL IN]
- Manual review notes: [FILL IN]

Example:
- Secret scan cadence: weekly
- Evidence location: docs/security/weekly-secret-scan.md
