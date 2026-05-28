# Mirror Sync

GitHub is the canonical source for VCP.
Mirrors are optional distribution channels.

## Manual sync

The safest starting point is manual mirror sync after a GitHub release or tagged update.

## Future automation

A future GitHub Action could push to mirrors, but that would require:
- mirror credentials;
- clearly scoped permissions;
- failure handling;
- stale-mirror detection.

## Risks

- stale mirror content;
- missing release notes;
- security issues opened against an outdated mirror;
- users treating a lagging mirror as canonical.

## Rule

If a mirror lags, GitHub still wins.
Always link back to the canonical GitHub repository.
