<!-- vcp-version: v0.9.4 -->
<!-- methodology-version: v1.4 -->
<!-- vcp-version: v0.8.2 -->

# Security Scanner Report

Практический шаблон отчета после запуска Trivy, OSV-Scanner, Gitleaks и смежных проверок.

## Project

- Name: [FILL IN]
- Repository: [FILL IN]
- Branch / commit: [FILL IN]
- Audit mode: [FILL IN]
- Auditor: [FILL IN]
- Date: [FILL IN]

## Commands

```bash
trivy fs --scanners vuln,secret,misconfig,license --severity HIGH,CRITICAL .
osv-scanner scan source -r .
gitleaks detect --source . --redact
```

## Environment

- OS / runtime: [FILL IN]
- Package managers detected: [FILL IN]
- Lockfiles detected: [FILL IN]
- Docker / image scan used: [FILL IN]
- Server / rootfs scan used: [FILL IN]

## Files and targets scanned

- Filesystem: [FILL IN]
- Lockfiles: [FILL IN]
- CI workflows: [FILL IN]
- Docker images: [FILL IN]
- Rootfs / server paths: [FILL IN]
- Git history: [FILL IN]

## Summary

- Critical vulnerabilities: [FILL IN]
- High vulnerabilities: [FILL IN]
- Secrets found: [FILL IN]
- Misconfigurations: [FILL IN]
- License issues: [FILL IN]
- False positives / noise: [FILL IN]
- Needs manual review: [FILL IN]

## Top risks

1. [FILL IN: top risk]
2. [FILL IN: second risk]
3. [FILL IN: third risk]

## Triage

| Finding ID | Type | Severity | Location | Why it matters | Action | Status |
|---|---|---|---|---|---|---|
| SCAN-001 | Secret | Critical | [FILL IN] | [FILL IN] | Rotate / remove / verify history | Open |
| SCAN-002 | Vulnerability | High | [FILL IN] | [FILL IN] | Update package / document exception | Open |
| SCAN-003 | Misconfiguration | High | [FILL IN] | [FILL IN] | Fix config / add CI check | Open |

## Secrets handling

- Не выводить секрет полностью.
- Указывать только masked value.
- При реальном секрете считать его скомпрометированным.
- Проверить историю git, CI, логи и внешние интеграции.

Пример маскирования:

```text
EXAMPLE_API_TOKEN=[masked-example-not-real]
EXAMPLE_DATABASE_CONNECTION=[masked-example-not-real]
```

## Required actions

- Rotate: [FILL IN]
- Update: [FILL IN]
- Remove / replace: [FILL IN]
- Add CI check: [FILL IN]
- Add alert: [FILL IN]
- Add documented exception: [FILL IN]

## CI / future checks

- Secret scan on PR: [FILL IN]
- Dependency scan on PR: [FILL IN]
- Weekly scan: [FILL IN]
- Alert on critical finding: [FILL IN]
- Block merge rule: [FILL IN]

## Final note

Сканеры дают evidence, но не заменяют triage, ручную проверку и приоритетный план исправлений.
