<!-- vcp-version: v0.8.4 -->

<!-- vcp-version: v0.8.2 -->
<!-- methodology-version: v1.4 -->
# Evaluate Spec Artifacts

Review the available spec artifacts and decide whether they are good enough to drive AI implementation.

Check for:

- clear goal;
- clear target user;
- explicit non-goals;
- testable acceptance criteria;
- constraints;
- risk level;
- data, privacy, or security impact;
- third-party dependencies;
- architecture impact;
- migration or rollback implications;
- validation plan;
- release or PR gate;
- visible open questions.

Return one of:

- `pass`
- `warn`
- `block`
