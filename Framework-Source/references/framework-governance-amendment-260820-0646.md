# Project Source Framework Governance Amendment — 1.1.1

```yaml
framework_document_id: "FRAMEWORK-001"
previous_project_source_framework_version: "1.1.0"
project_source_framework_version: "1.1.1"
project_source_schema_version: "1.0.0"
approved_at: "2026-08-20T06:46:00+07:00"
approval_basis: "Explicit user approval in the 2026-08-20 ProjectFramework canonicalization and upgrade conversation"
compatibility_intent: "Backward-compatible governance clarification/fix"
```

## Binding Amendment

This amendment clarifies the existing Current Truth, canonical object home, archive, Manifest, readiness, and export invariants. It does not introduce a new mandatory document type or machine schema structure.

1. **Active canonical registries are materialized current projections, not delta chains.** A current authoritative object record must contain enough semantic payload to determine what is true now, or link to an active/current canonical Detail Document containing that payload.
2. **Current Stable IDs resolve without archived revisions.** Every Stable ID referenced from the Active/Current Project Source must resolve to a current authoritative record within the Current Reconstructable Snapshot.
3. **Archive is Historical Truth, not a Current Truth runtime dependency.** Archived revisions may explain historical rationale/evolution, but they must not be required to determine current semantics.
4. **CURRENT export and Current Reconstructable Snapshot preserve interpretability.** They must include current canonical records plus any active/current Detail Documents required to interpret referenced current Stable IDs. Omitted archive content must not be necessary to know current truth.
5. **Referential validation fails on archive-dependent current semantics.** If a current Stable ID requires archive traversal to determine its current authoritative meaning, Project Source integrity/readiness fails for the affected scope; that scope is not operationally ready until repaired.

## Observed Case

The ambiguity was observed when later active `04-Decision Log` / `05-Requirements` revisions used entries such as:

```text
DEC-005 — retain previous status
REQ-008 — retain previous status
REQ-017 — retain previous status
```

while the complete Decision/Requirement semantics existed only in archived r002. Preservation of r002 makes history reconstructable, but it does not make r003 a self-contained Current Reconstructable Snapshot. Under Framework 1.1.1, the active `DEC-*` and `REQ-*` records must materialize their current semantics or link to active/current canonical Detail Documents that do so.

The invariant is general to current-state-bearing canonical object homes; `DEC-*` and `REQ-*` are the concrete observed case, not the only applicable object types.

## Prohibited Current-Payload Shortcuts

The following wording is not sufficient as the authoritative current payload when the actual semantics would otherwise exist only in archive:

```text
retain previous status
unchanged from rNNN
see archived revision
```

Such language may appear as historical/change commentary only when current semantics remain directly resolvable from the current snapshot.

## Compatibility and Migration

Project Source Framework version changes from `1.1.0` to `1.1.1`; Project Source Schema remains `1.0.0`. This is intended as a backward-compatible governance clarification/fix. Existing Projects remain pinned to their approved Framework/Schema versions and do not auto-upgrade. Applying 1.1.1 to an existing Project requires the normal governed `MIG-*` assessment, approval, validation, promotion, supersede, archive, and postflight flow.

## Non-Goals

This amendment does **not** add or authorize an executable Stable-ID resolver, CLI, validator, migration engine, automation service, or other software enforcement. Those remain separate future scope requiring explicit user approval.

## Precedence

For materialized-current-state, archive-independence, Stable-ID resolvability, Manifest/CURRENT completeness, and affected readiness, this 1.1.1 amendment is the latest binding Framework clarification. The 2026-08-14 amendment remains preserved as historical approved governance and continues to apply where not superseded or clarified here.
