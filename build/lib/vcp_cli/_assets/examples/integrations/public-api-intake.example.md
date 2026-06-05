# Public API Intake Example

> Synthetic example. Not a real project claim.

## Bad behavior

An agent receives a request for live weather hints in a dashboard and immediately writes integration code, adds a placeholder API key constant and assumes the free tier is fine for production.

## Correct VCP behavior

1. Run Third-party API Intake before implementation.
2. Classify the provider as a public weather-style API dependency.
3. Review auth model, data sent, quota, caching rules, attribution and fallback behavior.
4. Update `THIRD_PARTY_REGISTRY` with owner, environment, criticality and review status.
5. Add mocks and timeout handling before implementation.
6. Run Post-Task Code Review after the narrow implementation slice.

## Expected warning signals

- Do not add API keys to code.
- Do not assume public or free means production-safe.
- Do not ship without fallback or graceful degradation.
- Do not skip terms and data review.
