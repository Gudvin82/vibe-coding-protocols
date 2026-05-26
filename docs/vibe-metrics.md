# Vibe metrics

These are playful but useful metrics you can track inside your own project.

No claims are made that this repository already improves them by a measurable percentage.

| Metric | What it means | Why it helps |
| --- | --- | --- |
| Time to First Working Slice | How long it takes to get the first useful vertical slice | Shows whether the workflow is practical |
| Time to First Error | How quickly the first real failure appears | Helps compare shallow generation vs safer routing |
| Vibe-to-Bug Ratio | Rough sense of how much generated code turns into bugs | Encourages evidence over vibes |
| Rework Loops Count | How many times AI re-fixes the same area | Detects loop / bad context |
| AI Diff Size | How large a typical AI change is | Shows whether changes are getting too risky |
| Validation Pass Rate | How often checks are green on the first try | Measures friction and discipline |
| Manual Approval Count | How often risky changes require explicit approval | Reveals where the project is sensitive |
| Critical Findings Before Deploy | Number of critical issues found before release | Helps compare pre-release quality |
| Accepted Risks Count | How many risks were documented and consciously accepted | Encourages explicit tradeoffs |

Use these metrics only as internal guidance, not as marketing proof.
