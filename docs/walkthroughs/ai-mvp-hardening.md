# AI MVP Hardening

This walkthrough is a fictional but realistic example of the Existing Project Track.

It is sanitized guidance, not a measured production case study.

## Initial state

An AI-generated MVP already exists and the team wants to release or merge larger changes safely.

## Symptoms

- no architecture memory;
- unclear dependencies;
- backlog exists only in chat;
- no release gate;
- no review-diff discipline.

## VCP route decision

Recommended path:

- intake -> diagnose -> hardening route -> architecture drift check -> audit backlog -> review-diff -> PR Gate -> release readiness.

## Diagnostics

Start by checking:

- repo state;
- missing memory surfaces;
- validation gaps;
- release-surface drift.

## Architecture drift check

Look for:

- new directories not reflected in project memory;
- dependency or integration changes with no registry note;
- changed public surface without release note.

## Audit backlog

Capture:

- missing validation;
- unsafe assumptions;
- undocumented integrations;
- rollout risks.

## Review-diff

Review-diff makes the current change set visible:

- impacted areas;
- risk level;
- recommended spec depth;
- artifacts to update.

## Score

Score gives a local readiness signal after checks are aligned.

It is not certification.

## PR Gate

PR Gate gives a merge decision surface:

- pass;
- warn;
- block.

## Release readiness

Before release:

- version surfaces consistent;
- memory updated;
- diagnostics clear or accepted;
- review-diff and PR Gate reviewed;
- release notes prepared.

## Limitations

- VCP does not prove the MVP is safe for production;
- it does not invent missing product ownership;
- it does not replace human release authority.
