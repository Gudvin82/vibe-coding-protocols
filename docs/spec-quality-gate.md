# Spec Quality Gate

Spec Quality Gate checks whether spec artifacts are good enough to safely drive AI implementation.

It is not certification.

## Output statuses

- `pass`
- `warn`
- `block`

## Checks

- product goal is clear;
- target user is clear;
- non-goals are listed;
- acceptance criteria are testable;
- constraints are explicit;
- risk level is stated;
- data, privacy, and security impact is considered;
- third-party or API dependencies are listed;
- architecture impact is identified;
- migration or rollback need is considered;
- validation plan exists;
- release or PR gate exists;
- open questions are visible.

## Block conditions

A spec should be blocked when:

- there are no acceptance criteria;
- user, data, payment, or auth impact is unclear;
- production-critical flows would change but there is no release or rollback plan;
- external dependencies are unstated;
- privacy or security impact is unknown.

## What to do next

- `pass`: implementation can proceed with normal review discipline.
- `warn`: close visible gaps before implementation grows.
- `block`: stop and clarify spec artifacts before AI-generated implementation continues.

## Related files

- `templates/reports/spec-quality-gate-report.md`
- `templates/prompts/evaluate-spec-artifacts.md`
- `protocols/spec-driven/spec-foundation.md`
- `docs/two-track-model.md`
- `python3 -m vcp_cli spec quality-gate --json`
