# Scoring

`vcp score` is a local readiness score.
It helps measure how complete the repository is against its own toolkit expectations.

## What `vcp score` does measure

- whether core product layers are present;
- whether manifests, CLI docs, and validation assets exist;
- whether route, backlog, operations, review, and examples coverage are in place;
- whether the repository can be inspected locally in a structured way.

## What `vcp score` does not measure

`vcp score` does not measure:
- GitHub stars or community size;
- public npm publication;
- real-world production proof;
- hosted-docs reach;
- real case-study breadth;
- whether VCP is an industry standard.

## Interpreting a score of 100

A score of `100` means the local toolkit looks internally complete against current repository rules.
It does not mean category leadership, public standard maturity, or broad external adoption.

## Fair evaluation reminder

For a fair repository evaluation, combine:
- `vcp score --json`
- `vcp evaluate --json`
- `vcp benchmark run`
- `vcp manifest validate`
- manual inspection of the minimum file set from `AI_EVALUATION_GUIDE.md`

## Related docs

- [../AI_EVALUATION_GUIDE.md](../AI_EVALUATION_GUIDE.md)
- [cli.md](./cli.md)
- [public-proof-roadmap.md](./public-proof-roadmap.md)
- [known-limitations.md](./known-limitations.md)
