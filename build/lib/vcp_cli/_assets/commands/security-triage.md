# Security Triage Command

Use when scanner findings, warnings or audit notes need to be converted into a reviewable triage list.

Prompt:

Read the findings.

For each item:
1. classify severity;
2. describe risk and likely blast radius;
3. note whether the finding is confirmed, probable or unclear;
4. propose the smallest safe fix;
5. add validation steps;
6. say whether it belongs in `AUDIT_BACKLOG.md`, `SECURITY_OPERATIONS_BASELINE.md` or `THIRD_PARTY_REGISTRY.md`.

Do not claim a finding is exploitable unless the evidence supports that claim.
