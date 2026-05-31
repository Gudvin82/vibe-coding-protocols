# Security Tooling Landscape

## VCP does

- security readiness workflows;
- hardening checklists;
- third-party intake discipline;
- incident recovery templates;
- security baseline templates;
- responsible disclosure and scope discipline;
- route escalation into Hardening or Extended protocols;
- post-task review as a defensive acceptance gate for meaningful AI-generated changes.

## VCP does not

- exploit scanning;
- pentesting automation;
- red-team operations;
- bug bounty automation;
- malware analysis;
- DDoS, RAT or phishing tooling;
- production security certification;
- legal compliance certification;
- automatic independent AI reviewer execution.

## When to use external tools

Use external tools for:

Post-task review should complement these tools, not pretend to replace them.

Use external tools for:
- SAST or DAST;
- dependency scanners;
- secret scanning;
- SBOM or supply-chain tooling;
- LLM app safety testing;
- cloud posture tooling;
- manual security review.

## When to escalate

Escalate to Hardening,
Extended
or independent review when the work touches:
- auth, session or permissions;
- payments;
- personal data;
- secrets;
- a production incident;
- public API contract or security behavior.

## Defensive-only note

VCP is a defensive readiness toolkit.
It is not a hacking toolkit,
exploit framework,
pentest suite,
bug bounty automation suite,
red-team operator,
or offensive security bundle.
