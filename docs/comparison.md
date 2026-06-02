# Comparison

VCP should be compared by purpose, not by hype.
It complements several adjacent tools and conventions.
It does not replace all of them.

## Capability comparison

| Capability | VCP | `.cursorrules` only | Copilot Instructions | Conventional Commits | Generic prompt pack | Issue tracker | Security scanner |
|---|---|---|---|---|---|---|---|
| Multi-AI support | Yes | Partial | Partial | No | Partial | N/A | N/A |
| Route classification | Yes | No | No | No | Rarely | No | No |
| Adoption packs | Yes | No | No | No | Rarely | No | No |
| Project memory | Yes | Partial | Partial | No | Partial | Partial | No |
| Architecture Source of Truth | Supported | No | No | No | Rarely | No | No |
| Hardening workflow | Yes | No | No | No | Rarely | No | No |
| Post-task review gate | Yes | No | No | No | Rarely | No | No |
| Backlog discipline | Yes | No | No | No | No | Yes | No |
| Production error capture | Yes | No | No | No | No | No | No |
| Third-party API intake | Yes | No | No | No | Rarely | No | No |
| Public Growth / GEO | Yes | No | No | No | Rarely | No | No |
| CLI | Yes | No | No | No | Rarely | No | Yes |
| Manifests | Yes | No | No | No | Rarely | No | No |
| Benchmarks | Yes | No | No | No | Rarely | No | Partial |
| Reports/templates | Yes | Rarely | Rarely | No | Partial | Partial | Partial |
| Security scanning | No, different purpose | No | No | No | No | No | Yes |
| Replaces human review | No | No | No | No | No | No | No |

## Notes by category

### `.cursorrules` or a single IDE rules file

Different purpose. A rules file can shape one assistant’s local behavior, but it usually does not provide route classification, manifests, benchmarks, backlog discipline, or operations workflow.

### GitHub Copilot Instructions

Different purpose. Copilot Instructions guide one assistant surface; VCP adds repository-wide workflow structure across adoption, validation, review, and public-growth work.

### Conventional Commits

Different purpose. Conventional Commits standardize commit messages, while VCP focuses on upstream delivery discipline before and after changes are made.

### Generic prompt packs

Prompt packs can be useful, but they often stop at prompting. VCP tries to add repeatable routing, scoped adoption, manifests, benchmarks, and review/report artifacts.

### Product starter templates

Starter templates help bootstrap code. VCP is more about controlling AI-assisted delivery across the project lifecycle.

### Security scanners

Different purpose. Scanners inspect for specific technical findings. VCP does not pretend to replace scanning, testing, or human security review.

### Issue trackers like Jira or Linear

Different purpose. Issue trackers remain useful for teams. VCP’s local backlog is a lightweight workflow layer, not a claim that external trackers are unnecessary.

## Conclusion

VCP complements these tools.
It is not trying to replace IDE instructions, scanners, issue trackers, or commit conventions.
It is most useful when AI-assisted delivery needs route discipline, scoped adoption, validation, review gates, and honest public-growth structure.
