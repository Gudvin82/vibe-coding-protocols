# Hardening Thresholds

These thresholds are practical gates, not guarantees.

| Metric | Light | Standard | Full / Production |
|---|---:|---:|---:|
| Open blockers | 0 | 0 | 0 |
| Real secrets | 0 | 0 | 0 |
| Critical dependency findings | documented | 0 or accepted risk | 0 or accepted risk |
| Gitleaks real findings | 0 | 0 | 0 |
| Tests run | smoke | core flows | critical + regression |
| AUDIT_BACKLOG | created | prioritized | owners + due dates |
| Accepted risks | optional | documented | documented + owner |
| Architecture docs | minimal | updated | source of truth updated |
| Rollback plan | optional | required for risky changes | required |

## MVP gate

Use this when the project is still small but already needs a clean merge/deploy decision.

- no unresolved blockers;
- no real secrets in repo or screenshots;
- a smoke test for the main path has been run;
- `AUDIT_BACKLOG.md` exists if AI-generated code already exists;
- accepted risks are explicit, not hidden in chat history.

## Production gate

Use this when the project is public, client-facing, paid, or handles users, auth, personal data or money.

- zero unresolved blockers;
- zero real secrets;
- dependency findings triaged with explicit accepted-risk logic;
- critical flows tested;
- rollback plan exists for risky changes;
- architecture and security operations docs are updated;
- recurring checks have owners and evidence.

## Do not deploy if

- a real secret is still present;
- merge/deploy blockers are still open;
- the rollback path is unknown for a risky change;
- the system handles auth, payments or personal data and no hardening pass has been done;
- accepted risks are undocumented or ownerless.
