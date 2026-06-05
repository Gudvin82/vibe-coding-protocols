# PR Gate Approval Model

PR Gate is an approval model, not only a workflow file.

## States

- `pass`: core evidence is present and no material blocker is open.
- `warn`: the change can move forward only if the team consciously accepts visible gaps.
- `block`: do not merge or release until the mismatch is fixed.
- `needs-human-review`: automation is insufficient for the final decision.
- `not-applicable`: the gate does not apply to this slice.

## Examples

- AI-generated changes without tests: `warn` or `block` depending on scope.
- Public release docs mismatch: `block`.
- Missing proof layer on a risky external claim: `warn`.
- Destructive apply without confirmation: `block`.
- Roadmap overclaim presented as shipped: `block`.
- Unrun tests claimed as passed: `block`.

## Command surface

```bash
python3 -m vcp_cli pr-gate explain --json
```

## Boundaries

- not a GitHub Marketplace Action;
- not a policy engine;
- not a security certification.
