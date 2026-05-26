# MIGRATION_ROLLBACK_PLAN

## Rules

- back up before applying migrations
- do not apply to production without approval
- define rollback or down-migration path
- test on staging or copy-of-data first
- review destructive operations
- use expand-and-contract for zero-downtime changes when needed
- run smoke tests after migration
