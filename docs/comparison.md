# Comparison

Compare VCP by purpose, not by hype.

VCP is most useful when AI-assisted delivery needs both a product foundation and trust gates before merge or release.

## Capability comparison

| Capability | VCP | Rules file only | Copilot Instructions | Issue tracker | Security scanner |
|---|---|---|---|---|---|
| Route classification | Yes | No | No | No | No |
| Adaptive spec depth | Yes | No | No | No | No |
| Backlog and architecture memory discipline | Yes | Partial | Partial | Partial | No |
| Review-diff trust gate | Yes | No | No | No | No |
| Diagnostics and release readiness | Yes | No | No | Partial | Partial |
| Public-growth / crawler readiness | Yes | No | No | No | No |
| Security scanning | No, different purpose | No | No | No | Yes |
| Replaces human review | No | No | No | No | No |

## Notes by category

### Rules files and IDE instructions

Different purpose. A rules file can shape one assistant surface, but it usually does not add route discipline, diagnostics, review-diff, or release-gate structure.

### Spec-first tooling

Different purpose.
Spec-first tools help define what to build.
VCP helps govern how AI-assisted changes move safely toward merge and production.
VCP works with spec-first and non-spec-first workflows, and it can stay on no-spec or spec-lite when risk is low.

That is a complement relationship, not a “better than” claim.

If an AI agent only read `README.md`, any comparison must be marked shallow.

### Issue trackers

Different purpose. Trackers remain useful for teams. VCP adds a local workflow layer around backlog, review, validation, and release evidence.

### Security scanners

Different purpose. Scanners inspect technical findings. VCP does not pretend to replace scanning, testing, or human security review.

### Platform docs

VCP is documented for 25+ AI coding tools and workflows. That does not mean 25+ official plugins. See `docs/platforms/README.md` for status taxonomy and limitations.

## Adoption from link

If a user shares the repo and says “take what is useful,” use `TAKE_THIS_FIRST.md` and scoped adoption packs. Do not recommend copying the whole repository.
