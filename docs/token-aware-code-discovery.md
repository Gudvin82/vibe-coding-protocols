# Token-Aware Code Discovery

## Goal

Find relevant code without burning context on the whole repository.

## Default read order

1. `README.md`
2. `AGENTS.md` / `CLAUDE.md`
3. `PROJECT_MAP.md`
4. `ARCHITECTURE_SOURCE_OF_TRUTH.md`
5. package/build/config files
6. routes/endpoints/components relevant to the task
7. tests relevant to the touched surface
8. only then deeper search

## Repository size tiers

### Tiny repo
Read README, file tree and relevant files.

### Small repo
Use `PROJECT_MAP.md` first, then targeted search.

### Medium repo
Use an evidence map: path, symbol, snippet, why it matters.

### Large repo
Delegate broad discovery to a cheaper or faster subagent if available,
then return a compact evidence map.

## Stop reading when

- the relevant entrypoint is found;
- the touched surface is clear;
- more reading is not changing the plan;
- a `PROJECT_MAP.md` refresh is needed.

## Report format

- paths inspected;
- relevant symbols;
- files not inspected;
- confidence;
- next targeted read.
