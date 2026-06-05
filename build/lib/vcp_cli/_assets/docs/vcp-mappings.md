# VCP Mappings

This document explains how VCP cards map routes and concepts to practical delivery dimensions.

## Mapping dimensions

### SDLC phase
- idea
- planning
- implementation
- review
- hardening
- release
- operations
- growth

### Project state
- new
- existing MVP
- production
- regulated
- public site
- shared engine

### AI failure mode
- README-only evaluation
- no product brief
- no architecture memory
- no stop conditions
- no review gate
- no validation
- backlog only in chat
- unsafe external API
- public growth without baseline
- production logs ignored

### Artifact
- `PROJECT_MAP.md`
- `ARCHITECTURE_SOURCE_OF_TRUTH.md`
- `PROJECT_BACKLOG.md`
- `AUDIT_BACKLOG.md`
- `THIRD_PARTY_REGISTRY.md`
- review reports

### Risk category
- security
- architecture drift
- delivery chaos
- operations
- privacy/data
- public visibility
- compliance/legal
- maintainability

## Route mapping table

| Route | SDLC phase | Project state | Common failure modes | Primary artifacts | Risk categories |
|---|---|---|---|---|---|
| Starter | idea, planning | new | no product brief | `PROJECT_MAP.md`, starter files | delivery chaos |
| Production Hardening | hardening, release | existing MVP, production, regulated, shared engine | no review gate, no validation, no architecture memory | `AUDIT_BACKLOG.md`, security review scope, architecture docs | security, privacy/data, architecture drift |
| Maintenance Refactoring | implementation, review | existing MVP, production | no validation, architecture drift | refactoring report, `PROJECT_BACKLOG.md` | maintainability, delivery chaos |
| UI Component Ownership | implementation, review | existing MVP, public site | UI drift, no ownership | UI report | maintainability, public visibility |
| Post-Task Code Review | review, release | existing MVP, production | no review gate | code review report | delivery chaos, security |
| Production Error Capture | operations | production | production logs ignored | capture report, backlog | operations, security |
| Daily Error Triage | operations | production | backlog only in chat | triage report, `PROJECT_BACKLOG.md` | operations, delivery chaos |
| Third-party API Intake | planning, implementation, review | existing MVP, production, regulated | unsafe external API | `THIRD_PARTY_REGISTRY.md`, intake report | security, privacy/data, compliance/legal |
| Public Site Readiness | release, growth | public site | public growth without baseline | trust pages, `llms.txt` | public visibility |
| Public Growth | growth | public site, production | README-only evaluation, public growth without baseline | page brief, AI visibility report | public visibility, delivery chaos |
| Repository Evaluation | planning, review | any | README-only evaluation | evaluation guide, index, cards | delivery chaos |

Related:
- [vcp-cards.md](./vcp-cards.md)
- [progressive-disclosure.md](./progressive-disclosure.md)
