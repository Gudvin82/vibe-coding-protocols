# Adaptive Rigor Modes

<!-- vcp-version: v0.9.1 -->
<!-- methodology-version: v1.4 -->

Adaptive rigor позволяет right-size VCP под ситуацию.

Режимы: `fast`, `standard`, `controlled`, `brownfield`, `launch`, `deep-hardening`.

- `fast`: для tiny changes и quick triage, обычно nano profile.
- `standard`: режим по умолчанию, нужен change intent и basic proof.
- `controlled`: важные изменения, нужны charter, intent, work package, gate и proof.
- `brownfield`: existing repo с неясным состоянием, нужен classify и control catalog.
- `launch`: demo/release/customer exposure, нужны PR Gate, trust-check, benchmark, launch decision.
- `deep-hardening`: high-risk/safety/security, нужен full profile и human approval.
