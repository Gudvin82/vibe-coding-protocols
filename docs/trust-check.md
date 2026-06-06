# Trust Check

Repository package: `v0.8.6`

Use the trust check when you want a local, read-only repository consistency audit.

## Command

```bash
python3 -m vcp_cli trust-check --json
```

Installed CLI form:

```bash
vcp trust-check --json
```

## What it checks

- version surface consistency;
- README / README_ru parity;
- Russian docs parity;
- roadmap-only overclaim contradictions;
- workflow/docs sync;
- integration status validity;
- benchmark report presence;
- changelog hygiene;
- release note presence.

## What it does not prove

Trust Check does not prove:
- production safety;
- launch success;
- security certification;
- hosted platform readiness.

It is a repository trust and consistency check.
