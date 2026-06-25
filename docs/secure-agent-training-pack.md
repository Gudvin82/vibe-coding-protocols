# Secure Agent Training Pack

Repository package: `v0.9.5`

This pack is a lightweight onboarding layer for safer AI-assisted contribution.
It is not a game engine and not a security certification.

## Purpose

Use it to train contributors and reviewers to stop unsafe AI behavior before it
turns into drift, overclaim, risky release behavior, or unsafe repository-wide
changes.

## Covered scenarios

1. AI wants to change auth code without review.
2. Agent adds dependency without license/security review.
3. AI writes public claim without evidence.
4. Multi-agent reviews conflict.
5. Secret appears in prompt/code.
6. PR is prepared without tests/trust-check.
7. Agent tries broad rewrite outside scope.
8. AI marks release as production-ready without evidence.
9. Agent modifies CI/release files without approval.
10. AI suggests dangerous shell command.

## Required outputs

Each exercise should end with:
- a VCP response path;
- a required artifact;
- a required check;
- a stop condition;
- a reflection question.

## Best place in rollout

- VCP-Audit: use as a reviewer calibration pack.
- VCP-Pilot: use before agent kits and PR Gate become mandatory.
- VCP-Scale: use as recurring team enablement material.

## Related surfaces

- [Team Enablement Pack](./team-enablement-pack.md)
- [PR Readiness](./pr-readiness.md)
- [GitHub-native Control Checklist](./github-native-control-checklist.md)
- [Current Limitations](./current-limitations.md)
