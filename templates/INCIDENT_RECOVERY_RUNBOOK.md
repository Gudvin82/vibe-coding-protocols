<!-- vcp-version: v0.8.8 -->
<!-- methodology-version: v1.4 -->
<!-- vcp-version: v0.8.4 -->

<!-- vcp-version: v0.8.2 -->

<!-- vcp-artifact: INCIDENT_RECOVERY_RUNBOOK -->
<!-- vcp-version: v0.8.2 -->

# INCIDENT_RECOVERY_RUNBOOK.md

Use this runbook when the project is already under stress and the team
needs a small, practical recovery path.

## General principles

- Stop broad changes.
- Preserve evidence before cleanup.
- Prefer rollback over blind forward-fixing when the blast radius is unclear.
- Do not run destructive commands without approval.
- Record the incident in `AUDIT_BACKLOG.md` after stabilization.

## Scenario 1. AI broke production behavior

### Immediate actions
- Stop new AI-generated changes.
- Capture the failing route, command or user flow.
- Save `git status`, `git diff` and recent deploy metadata.
- Confirm whether this is a code regression, config issue or data issue.

### What to stop
- automatic deploys;
- feature work on the affected path;
- unrelated refactors.

### What to preserve
- error logs;
- failing requests and timestamps;
- deploy ID or commit SHA;
- user reports and screenshots if available.

### Rollback
- Roll back to the last known-good commit or deployment if recovery is not obvious.
- If rollback is risky, isolate the broken feature behind a flag, route or config gate.

### Evidence
- failing tests or runtime errors;
- touched files;
- impacted user flow;
- validation run after rollback or fix.

### Who to notify
- owner of the affected feature;
- release owner;
- support or ops if users are impacted.

### Follow-up
- add a regression test if practical;
- update `PROJECT_MAP.md` or architecture docs if the incident exposed stale memory;
- record accepted risk if a partial fix ships first.

## Scenario 2. Secret leaked

### Immediate actions
- Treat the secret as compromised.
- Stop using the exposed credential.
- Check whether the leak is in the working tree, logs, screenshots or git history.

### What to stop
- further sharing of the affected branch or logs;
- deploys that still rely on the compromised credential;
- any public paste of the leaked value.

### What to preserve
- affected file paths;
- approximate exposure window;
- commit SHA or log location;
- which system used the secret.

### Rollback
- Remove the secret from current files.
- Rotate and revoke the old credential.
- If the leak is in git history, do not assume deleting the file is enough.

### Evidence
- where the secret appeared;
- whether it reached git history;
- whether rotation and revocation completed;
- whether replacement config was verified.

### Who to notify
- secret owner;
- platform or infra owner;
- security owner if one exists.

### Follow-up
- add `.env.example` or placeholder cleanup if needed;
- run secret scanning again;
- document rotation status in backlog or security notes.

## Scenario 3. Migration failed

### Immediate actions
- Stop further schema changes.
- Capture the migration name, command and error.
- Confirm whether partial schema changes were applied.

### What to stop
- automatic deploy continuation;
- follow-up migrations;
- data writes to unstable paths if possible.

### What to preserve
- schema diff;
- migration logs;
- backup status;
- row counts or affected entities if known.

### Rollback
- Use the prepared rollback or down migration if it is safe.
- If no rollback exists, restore from the approved recovery path.
- Avoid improvising destructive SQL under pressure.

### Evidence
- what changed in schema;
- whether data was mutated;
- whether rollback succeeded;
- post-recovery smoke test results.

### Who to notify
- database owner;
- release owner;
- affected product owner if the incident is user-visible.

### Follow-up
- require rollback notes for future risky migrations;
- improve staging or copy-of-data migration checks;
- add the failure mode to `AUDIT_BACKLOG.md`.

## Scenario 4. Payment or webhook incident

### Immediate actions
- Pause automatic retries only if they amplify damage.
- Capture provider event IDs, timestamps and affected user/account IDs.
- Confirm whether the issue is duplicate processing, failed callback or auth/config breakage.

### What to stop
- risky replays without idempotency review;
- manual compensation without evidence;
- unrelated payment changes.

### What to preserve
- webhook payload IDs;
- provider dashboard evidence;
- internal processing logs;
- idempotency keys or missing-key evidence.

### Rollback
- Disable the broken integration path if needed.
- Reconcile from provider-side truth before replaying events.
- Use manual compensation only with a logged decision.

### Evidence
- duplicate or missing events;
- affected payments or orders;
- whether callbacks were authenticated;
- whether replay succeeded after fix.

### Who to notify
- payments owner;
- support if users are impacted;
- finance or operations if money movement is involved.

### Follow-up
- add idempotency coverage if missing;
- add replay-safe tests;
- document provider-side and app-side responsibilities.

## Post-incident checklist

- [ ] System stabilized or rolled back
- [ ] Evidence preserved
- [ ] Owners notified
- [ ] `AUDIT_BACKLOG.md` updated
- [ ] Architecture or security docs updated if needed
- [ ] Follow-up validation run completed
