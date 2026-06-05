# PR Gate

PR Gate is a local approval model plus a GitHub Actions template surface.

See also:
- [docs/pr-gate-approval-model.md](./pr-gate-approval-model.md)
- [docs/launch-decision-checklist.md](./launch-decision-checklist.md)
- `ci-examples/github-actions/vcp-pr-gate.yml`

## PR Gate before launch

Use PR Gate before launch when an AI-generated MVP is crossing from demoable to user-facing.

Typical flow:
- review changed files;
- explain PR Gate status;
- compare warn vs block conditions;
- require human review for risky surfaces;
- feed the result into the launch decision checklist.

## Examples

Warn:
- docs drift;
- missing dashboard artifact refresh;
- incomplete proof write-up.

Block:
- unresolved launch blockers;
- unsafe architecture drift;
- missing review for payment/auth/data-critical changes;
- AI-generated MVP changes that are still unreviewed but being treated as ready to ship.

## Boundaries

PR Gate does not claim:
- official GitHub Marketplace Action status;
- automatic merge control unless your copied workflow enforces it;
- security certification;
- production readiness certification.
