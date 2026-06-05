# Spec-driven Development

`vcp-version: v0.5.9`

This lane turns a fuzzy idea into a scoped, reviewable feature before implementation starts.

Use this lane when:
- a founder or PM has an idea but no PRD yet;
- a feature request is non-trivial and still ambiguous;
- AI-assisted delivery is likely to drift without acceptance criteria;
- the team wants task breakdown before coding.

Do not use this lane when:
- the change is a one-line typo fix;
- the work is purely mechanical formatting;
- a production incident needs immediate containment;
- the user explicitly wants exploration only.

Core principle:

> No implementation before the product intent, acceptance criteria, risks, dependencies and validation plan are clear enough for the chosen scope.

Suggested flow:
1. Product brief or founder note
2. PRD draft
3. Clarifying questions
4. Feature spec
5. Acceptance criteria
6. Tasks and backlog linkage
7. Spec review
8. Implementation
9. Post-task review

Connected artifacts:
- `PROJECT_BACKLOG.md`
- `PROJECT_MAP.md`
- `templates/ARCHITECTURE_SOURCE_OF_TRUTH.md`
- `protocols/review/post-task-code-review.md`
