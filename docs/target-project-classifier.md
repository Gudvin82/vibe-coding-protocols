# Target Project Classifier

Use this matrix before choosing a VCP route.

## Route matrix

| Target project signal | Route |
|---|---|
| No code yet or idea stage | Starter Protocol |
| New MVP being prepared | Starter Protocol |
| Existing AI-generated project before staging | Hardening Light or Standard |
| Existing production project | Hardening Full |
| Users, payments, personal data or compliance | Hardening Full + Security Review Scope |
| Legal, security or financial claims | Hardening Full + Architecture Source of Truth |
| Shared engine powering multiple products | Shared Engine or Multi-product Adoption Pack |
| Works but risky to change | Maintenance Refactoring |
| Frontend styling drift or component ownership problems | UI Component Ownership |
| Public website, docs, SEO or AI crawler readiness | Public Site Readiness |
| New behavior or product decision | Product task or Extended Protocol |
| Broad architecture change | Extended Protocol |

## Severity defaults

- Production plus user data defaults to Full Hardening.
- Payments or personal data default to Full Hardening.
- Shared engine work should include `PROJECT_MAP.md`, `ARCHITECTURE_SOURCE_OF_TRUTH.md` and release gates.
- Security-sensitive change belongs in Hardening or Extended, not routine maintenance.
- If no validation path exists, stop or narrow scope.

## Synthetic examples

### 1. New SaaS MVP with no production users

- Classification: new MVP
- Route: Starter Protocol
- Optional additions: Lite adoption path, Architecture Map

### 2. Existing marketing website

- Classification: existing public site
- Route: Public Site Readiness
- Optional additions: Maintenance Refactoring if content/code is messy

### 3. Existing production app with payments

- Classification: existing production + payments
- Route: Full Hardening + Security Review Scope
- Optional additions: Architecture Source of Truth, release gates

### 4. Two products on one shared engine

- Classification: shared engine and multi-product production risk
- Route: Shared Engine or Multi-product Adoption Pack + Full Hardening
- Optional additions: Maintenance Refactoring for safe cleanup after mapping

### 5. Working app with messy code

- Classification: maintainability problem
- Route: Maintenance Refactoring
- Stop condition: escalate if public contracts or auth/payment behavior must change

### 6. Frontend pages with hardcoded styling

- Classification: UI ownership problem
- Route: UI Component Ownership
- Stop condition: escalate if redesigning the whole design system

## Route choice notes

- Starter is for new work, not for already risky production systems.
- Maintenance Refactoring is a safe, narrow route for behavior-preserving cleanup.
- UI Component Ownership is a focused frontend route, not a full redesign track.
- Hardening is the default for production readiness, security posture and sensitive change.
