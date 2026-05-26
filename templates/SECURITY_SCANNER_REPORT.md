# Security Scanner Report

Практический шаблон отчета после запуска Trivy, OSV-Scanner, Gitleaks и смежных проверок.

## Project

- Name:
- Repository:
- Branch / commit:
- Audit mode:
- Auditor:
- Date:

## Commands

```bash
trivy fs --scanners vuln,secret,misconfig,license --severity HIGH,CRITICAL .
osv-scanner scan source -r .
gitleaks detect --source . --redact
```

## Environment

- OS / runtime:
- Package managers detected:
- Lockfiles detected:
- Docker / image scan used:
- Server / rootfs scan used:

## Files and targets scanned

- Filesystem:
- Lockfiles:
- CI workflows:
- Docker images:
- Rootfs / server paths:
- Git history:

## Summary

- Critical vulnerabilities:
- High vulnerabilities:
- Secrets found:
- Misconfigurations:
- License issues:
- False positives / noise:
- Needs manual review:

## Top risks

1. 
2. 
3. 

## Triage

| Finding ID | Type | Severity | Location | Why it matters | Action | Status |
|---|---|---|---|---|---|---|
| SCAN-001 | Secret | Critical |  |  | Rotate / remove / verify history | Open |
| SCAN-002 | Vulnerability | High |  |  | Update package / document exception | Open |
| SCAN-003 | Misconfiguration | High |  |  | Fix config / add CI check | Open |

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

- Rotate:
- Update:
- Remove / replace:
- Add CI check:
- Add alert:
- Add documented exception:

## CI / future checks

- Secret scan on PR:
- Dependency scan on PR:
- Weekly scan:
- Alert on critical finding:
- Block merge rule:

## Final note

Сканеры дают evidence, но не заменяют triage, ручную проверку и приоритетный план исправлений.
