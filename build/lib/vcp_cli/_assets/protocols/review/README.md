# Review Protocols

Post-task review is the VCP review family for active changes that are about to be accepted.

Use it after meaningful AI-generated work and before:
- the next task;
- merge;
- release;
- deploy;
- tag;
- handoff.

Why it exists:
- Hardening asks whether a project is ready for production and security risk.
- Maintenance asks whether working code can be made easier to change without behavior changes.
- Post-task review asks whether this specific set of active changes is acceptable before we move on.

This matters for AI-generated changes because useful code can still hide:
- correctness bugs;
- missing tests;
- behavioral regressions;
- public contract drift;
- security or privacy mistakes;
- UI or accessibility regressions;
- scope creep.

Use post-task review when:
- a meaningful task is done;
- the work touched production code, shared engines or public behavior;
- the next feature should not begin until the current diff is reviewed;
- you want a clear review plus validation gate before merge or release.

Do not confuse this route with hardening:
- Hardening is broader and risk-oriented.
- Post-task review is change-set oriented.

Do not confuse this route with maintenance refactoring:
- Maintenance starts from code that works but is becoming risky to extend.
- Post-task review starts from an active diff that needs acceptance.

Use this family with:
- [post-task-code-review.md](./post-task-code-review.md)
- [../../commands/loop-code-review.md](../../commands/loop-code-review.md)
- [../../templates/prompts/loop-code-review.md](../../templates/prompts/loop-code-review.md)
- [../../templates/reports/code-review-report.md](../../templates/reports/code-review-report.md)
