# Plugin Contract Draft

This is a draft contract for local VCP plugin metadata.
It is not yet a stable official plugin API.

## Goals

The draft contract exists so plugins can be described consistently before any marketplace or execution engine exists.

## Draft metadata fields

- `id`
- `name`
- `version`
- `vcp_compatibility`
- `capabilities`
- `execution`
- `trust_level`
- `entrypoint`
- `outputs`
- `network`
- `writes`

Example:

```json
{
  "id": "example-readiness-check",
  "name": "Example Readiness Check",
  "version": "0.1.0",
  "vcp_compatibility": ">=0.8.2",
  "capabilities": ["check", "report"],
  "execution": "read-only",
  "trust_level": "local-reviewed",
  "entrypoint": "python -m example_plugin",
  "outputs": ["json"],
  "network": false,
  "writes": false
}
```

## Important limits

This draft does not promise:
- stable API compatibility;
- plugin installation;
- remote discovery;
- execution orchestration;
- official plugin review.
