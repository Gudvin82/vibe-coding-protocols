# INCIDENT_RECOVERY_RUNBOOK.md

## Scenario

Choose the incident type:
- AI broke working code
- secrets leak
- migration failed
- payment webhook issue
- scanner found critical finding

## Immediate actions
- stop broad changes
- capture `git status`
- list changed files
- capture failing command / error
- decide whether approval is needed before rollback

## Rollback notes
- use rollback path that matches the incident
- do not delete user work blindly
- do not use destructive commands without approval

## Approval required
- production rollback
- migration rollback with real data
- secret rotation
- changes affecting payment/auth/admin flows

## Post-incident
- add note to `AUDIT_BACKLOG.md`
- add follow-up to architecture or security docs
- record what validation was run after recovery
