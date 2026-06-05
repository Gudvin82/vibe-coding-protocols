# Maintenance Protocols

This is the post-MVP and existing-project lane for Vibe Coding Protocols.

Use it when a project already works,
but is becoming harder to maintain,
riskier to extend,
more duplicated,
more inconsistent
or harder to reason about.

Valid outcomes include:
- no changes needed;
- a narrow refactoring scope;
- a separate product task;
- a UI ownership cleanup slice.

## How this differs from Hardening

Use maintenance refactoring when the main problem is maintainability,
clarity,
boundaries
or safe extensibility.

Use hardening when the main problem is production readiness,
security posture,
secrets,
deploy risk
or public exposure.

Use UI refactoring when the main problem is frontend styling ownership,
component inconsistency,
or pages doing visual work that belongs inside components.

## Recommended cadence

Run this lane:
- after MVP;
- before large new feature work;
- after heavy AI-generated implementation;
- before handoff;
- after repeated difficulty modifying the same area.

## Route table

| Situation | Route |
|---|---|
| Project works but code feels risky to change | [`/care-refactoring`](../../commands/care-refactoring.md) |
| UI is inconsistent or pages contain hardcoded styling | [`/ui-refactoring`](../../commands/ui-refactoring.md) |
| Need production or security readiness | [Hardening Protocol](../ai-project-hardening-protocol.md) |
| Starting from idea | [Starter Protocol](../ai-project-starter-protocol.md) |

## Existing-user adoption path

Minimal copy set for an existing project:
- `protocols/maintenance/`
- `commands/care-refactoring.md`
- `commands/ui-refactoring.md`
- `templates/reports/refactoring-report.md`
- `templates/reports/ui-refactoring-report.md`
- `templates/examples/refactoring-report.filled.example.md`
- `templates/examples/ui-refactoring-report.filled.example.md`
- `docs/security-methodology-scope.md`
- `docs/tooling-roadmap.md`

Do not overwrite local `AGENTS.md`,
`PROJECT_MAP.md`
or `SECURITY.md` blindly.
Merge route guidance into your local project docs.

## Included protocols

- [care-refactoring.md](./care-refactoring.md)
- [ui-refactoring.md](./ui-refactoring.md)

## Filled synthetic report examples

- [../../templates/examples/refactoring-report.filled.example.md](../../templates/examples/refactoring-report.filled.example.md)
- [../../templates/examples/ui-refactoring-report.filled.example.md](../../templates/examples/ui-refactoring-report.filled.example.md)
- [../../examples/bad-to-good/maintenance-refactor-before.md](../../examples/bad-to-good/maintenance-refactor-before.md)
- [../../examples/bad-to-good/ui-ownership-before.md](../../examples/bad-to-good/ui-ownership-before.md)
