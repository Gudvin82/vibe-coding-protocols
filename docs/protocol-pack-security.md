# Protocol Pack Security

VCP packs should be inspectable before they are adopted.
This page defines the trust model for adoption packs, protocol packs, command packs, and future external packs.

## Trust levels

- `core`
- `local`
- `workspace`
- `external`
- `experimental`
- `deprecated`

## Pack source

Each pack should state:
- source;
- owner;
- version;
- trust level;
- intended use;
- required files;
- commands if any;
- whether it modifies code, docs, CI, settings, or workflows.

## External pack rules

External packs:
- must not be applied blindly;
- must not require secrets in docs or prompts;
- must not modify CI or release gates without review;
- must not add network calls without an explicit note;
- must not weaken VCP safety boundaries;
- must go through PR Gate or `review-diff` before merge.

## Pack mutation rules

If a pack changes:
- run cards, index, and manifests validation;
- update version metadata;
- update report templates if needed;
- add a changelog note;
- review source and scope.

## CLI-friendly checklist

- identify source and owner;
- classify trust level;
- list touched files;
- note code, docs, CI, settings, and workflow impact;
- validate cards, index, manifests, and benchmarks;
- pass through review before merge.
