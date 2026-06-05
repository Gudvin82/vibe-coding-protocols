# Metrics to Track

Track these if you want to evaluate whether the workflow is helping.
Do not present them as guaranteed outcomes.

Use [`templates/METRICS_BOARD.md`](../templates/METRICS_BOARD.md) if you want a small place to record them.

## Time to first safe slice

Measure:
- time from idea to Product Brief;
- time from Product Brief to first reviewable slice;
- time from first slice to first hardening pass.

## Number of files changed per AI task

Track:
- median files changed;
- large-diff outliers;
- tasks that trigger stop conditions because scope grew too wide.

## Number of stop-condition triggers

Track:
- changes touching too many files;
- new dependency additions;
- auth, session or payment changes;
- migration-related pauses;
- CI/CD approval stops.

## Findings in AUDIT_BACKLOG

Track:
- number of open findings;
- severity distribution;
- recurring finding categories;
- time from finding to resolution.

## Secrets found before deploy

Track:
- suspicious secret-like patterns found locally;
- real secret leaks prevented before merge or deploy;
- git-history secret rotation follow-ups.

## Failed AI attempts avoided

Track:
- entries in `docs/PROMPTS.md` or prompt logs marked as rejected;
- repeated failure modes that stop recurring after documentation;
- routes avoided because a smaller safe step was chosen instead.

## Rollback events

Track:
- how often rollback was needed;
- whether rollback notes existed beforehand;
- whether rollback succeeded cleanly.

## Review findings

Track:
- number of independent review findings per change;
- which categories are caught by review versus by tests;
- whether repeated issues suggest stale AGENTS or PROJECT_MAP guidance.

## Time from idea to Product Brief

Track:
- how long it takes to turn a vague idea into a usable Product Brief;
- which inputs are usually missing at the beginning;
- whether `START_HERE.md` reduces routing confusion.

## Notes

Metrics require real project data.
They do not prove that the toolkit automatically improves delivery,
security or velocity.
