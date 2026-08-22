# UAAC 5.0 Adoption Guide

Status: **NON-NORMATIVE GUIDE**

## Required record

`governance/UAAC-ADOPTION.yaml` contains exactly two required sections:

```yaml
project:
  id: project-a
  boundary: .
constitution:
  id: UAAC-001
  version: "5.0.0"
  local_locator: vendor/uaac/v5.0.0/UAAC-v5.0-CONSTITUTION.md
  immutable_identity: project-release-object:uaac-5.0.0-r1
```

The required fields are `project.id`, `project.boundary`, `constitution.id`, `constitution.version`, `constitution.local_locator`, and `constitution.immutable_identity`.

The local locator is the normal operating route. The immutable identity is established at install or migration using a mechanism appropriate to the source system, such as an immutable object ID, Git identity, content digest, signed revision, or equivalent. No particular mechanism and no repeated runtime hashing are universally required.

## Optional real routes

Omit every unused section. Do not emit an empty list or placeholder object.

```yaml
project_rules:
  - locator: governance/PROJECT-RULES.md

canonical_sources:
  - role: product_definition
    locator: project-docs/PRD.md
  - role: current_state
    locator: project-docs/CURRENT-STATE.md

continuation:
  locator: project-docs/CURRENT-STATE.md

profiles:
  - id: high-assurance
    locator: vendor/uaac/v5.0.0/profiles/high-assurance/PROFILE.md
```

Project rules are optional because Projects differ. Reuse an existing actual rules source; create `governance/PROJECT-RULES.md` only when real Project-specific rules will be written.

Profiles are active only when explicitly listed under applicable Project authority. Their presence in the vendored release does not activate them.

## Forbidden adoption content

The adoption record is not a status store or runtime control plane. It excludes lifecycle status, epochs, receipts, claim tokens, boot modes, mutable runtime state, validation results, adapter or capability graphs, registries, and tool configuration.

## Bounded reading

The Project router uses adoption to find real sources. For each task, identify a bounded set of materially required laws, rules, and canonical sources, then obtain sufficient complete coverage of each selected source. Search, relevance, retrieval, and summaries may route reading; they do not prove complete coverage.
