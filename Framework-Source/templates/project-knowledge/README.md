# Project Knowledge Starter

This directory is the maintained Framework starter source for an optional consuming-Project `Project-Knowledge/` layer. It is not an active Project Knowledge instance and is never Project authority.

```text
Project Knowledge ≠ Project Authority
Derived synthesis ≠ Evidence ≠ Governed Project truth
```

## Layout

```text
Project-Knowledge/
├── README.md
├── index.md
├── log.md
└── pages/
```

Materialize this layer only when useful and approved after active `FRAMEWORK-001` resolves. Absence is valid. Brownfield Projects never auto-adopt it.

## Page contract

Maintained pages use `knowledge_page_id`, exact `knowledge_state`, timestamps, `source_refs`, optional `related_project_source_refs`, `related_knowledge`, and `review_trigger`. Exact states are:

```text
CURRENT | REVIEW_DUE | STALE | CONTRADICTED | SUPERSEDED | RETIRED
```

State is maintenance/navigation status, not truth certainty. Material synthesis requires reconstructable provenance. Raw/source material remains source-native by default; retained copies gain no authority from location.

## Operations

- `ingest` — compare a source with existing Knowledge; update pages/cross-links/index; append one material log entry; surface contradictions/promotion candidates.
- `query-file` — file reusable synthesis using the same provenance/index/log rules.
- `lint` — advisory checks for stale/review-due pages, contradictions, broken/orphan links, weak provenance, superseded sources, and unreviewed governance candidates.
- `maintain` — explicit page/index/log housekeeping without changing Project authority.

## Promotion and integration

Knowledge→Governance promotion identifies the existing canonical Project Source home, verifies evidence, obtains applicable authority, mutates only that owner, then links the governed result back to Knowledge. No automatic promotion is permitted.

`[Meeting]` output remains advisory before filing. `EVD-*` remains evidence, not Knowledge. TASK-026 disclosure applies independently before external use. Knowledge cross-links are not `REL-*`; Project Graph stays canonical in `92`. OpenViking keeps `PROJECT_SOURCE_AUTHORITY` separate from `PROJECT_KNOWLEDGE_ADVISORY`, remains `DERIVED_ONLY` / rebuildable, and never promotes content by retrieval rank.

Actual secret values are forbidden. This starter creates no wiki engine, vector database, UI, watcher, crawler, auto-ingest daemon, embedding pipeline, MCP wiki service, validator/CLI, scheduler, or runtime automation.
