# Boundary Linting Status

## Current status

VCP does not currently ship a mature AST or interface boundary linter.
Current checks are still lightweight and repository-facing.

## Current checks can catch

- missing structure;
- broken local markdown links;
- version drift;
- newline-poor docs;
- basic toolkit consistency.

## Current checks cannot catch

- architecture boundary violations;
- business logic leaking across layers;
- UI component ownership violations;
- security correctness;
- dependency safety;
- whether a refactor is worth doing.

## Future boundary linter ideas

Possible future work:
- route-specific rule packs;
- import boundary checks;
- public API surface checks;
- UI ownership checks;
- report schema validation;
- CI annotations.

## CI and pre-commit plan

Current CI should keep running the existing checks.
Local hook installation can be done through `scripts/install-hooks.sh`.
Do not claim boundary linting is enforced until it actually exists.
