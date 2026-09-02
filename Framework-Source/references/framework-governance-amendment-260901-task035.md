# Framework Governance Amendment — TASK-035 Project Release / Publication Contract

**Framework:** 1.12.0
**Schema:** 1.0.0
**Release format:** 3
**Status:** CURRENT / SET1_INCREMENTAL
**Task:** TASK-035 — Project Release / Publication Contract

## 1. Purpose

Framework 1.12.0 defines explicit, evidence-backed publication truth without forcing every Project through one linear lifecycle.

```text
Task DONE ≠ MERGED ≠ PUSHED ≠ RELEASED ≠ ARTIFACT_PUBLISHED ≠ DEPLOYED
Implementation authority ≠ publication authority
Release evidence ≠ deployment evidence
Tag presence ≠ release truth unless the Project declares it material
```

## 2. Orthogonal publication dimensions

When material, report each dimension independently:

```text
Implementation: NOT_DONE | DONE
Integration: NOT_APPLICABLE | NOT_MERGED | MERGED
Repository Publication: NOT_APPLICABLE | NOT_PUSHED | PUSHED
Release: NOT_APPLICABLE | NOT_RELEASED | RELEASED
Artifact Publication: NOT_APPLICABLE | NOT_PUBLISHED | PUBLISHED
Deployment: NOT_APPLICABLE | NOT_DEPLOYED | DEPLOYED
```

These are reporting/lifecycle values, not Stable-ID families. `PUSHED` does not imply `MERGED`; `MERGED` does not imply formal release; `RELEASED` does not imply artifact publication or deployment.

## 3. Release Candidate identity

A material Release Candidate (RC) is bound to the minimum source-native identity needed for the Project, including repository/source identity, candidate commit/ref when Git-backed, candidate tree/content digest when material, version/release identifier, schema compatibility where applicable, verification evidence pointers, and material prerequisites/assumptions.

Exact Git SHA/tag is used only when observed/material and is never fabricated. If bound source/tree/content or a material assumption changes, prior candidate acceptance evidence is invalidated selectively under existing progressive verification rules.

## 4. Verification relationship

`RELEASE_FULL` evaluates the release candidate/distribution. It does not push, merge, tag, publish artifacts, or deploy.

`INTEGRATION_GATE` runs immediately before integration/publication actions dependent on a mutable canonical target. It re-resolves Base Freshness and prior evidence validity. Candidate or material target changes invalidate affected evidence and may require bounded/full reverification.

Exact verified transport/fast-forward may reuse still-valid candidate evidence for resulting-state confirmation; transport alone does not mandate unconditional RELEASE_FULL rerun.

## 5. Authority separation

Local implementation/commit authority never implies push. Push never implies merge. Merge never implies release/tag/artifact publication. Release approval never implies deployment. Deployment approval never implies secret disclosure or unrelated external actions. Persistent `[Goal]` includes publication only when explicitly scoped.

`commit ≠ push` remains binding.

## 6. Evidence and canonical homes

TASK-035 creates no mandatory new release Stable-ID family/semantic slot. Reuse existing homes:

- `10 Change Log` for material transitions/events;
- `13 Evidence Registry / EVD-*` for reconstructable RC, verification, publication/deployment evidence;
- `03 Current State` for current summary;
- `09 Handoff` for continuation/pending publication;
- `15 Action Registry` for execution;
- `91` for outcomes/gates/risks/change requests when applicable.

Repository-native releases/tags/package registries/deployment systems remain source-native evidence, never Project authority by themselves.

## 7. Partial publication and persistence

Multi-step publication may be partially complete. Report dimension-specific truth such as `PUSHED + NOT_MERGED`, `MERGED + NOT_RELEASED`, or `RELEASED + NOT_PUBLISHED` rather than collapsing to one success flag.

If an external publication succeeds but required durable Project reconciliation cannot be persisted, keep the observed external fact and use existing `PERSISTENCE_PENDING`; never falsely claim Project Source reconciliation.

## 8. Rollback, retraction, supersession

- **rollback** — integration/runtime/deployment is moved to a prior accepted state;
- **retraction** — a published release/artifact is declared withdrawn where supported;
- **supersession** — a newer release replaces an older one without erasing history.

Historical evidence remains. Tags/artifacts are never silently deleted/rewritten merely to make history clean. If an external platform cannot retract, record the limitation and superseding state.

## 9. Optional assurance

Immutable tags, signed commits, checksums, attestations, protected branches, release notes, and artifact signatures are optional unless the Project explicitly requires them. Missing optional assurance is never fabricated into provenance or a blocker.

## 10. GREENFIELD/Brownfield/runtime boundary

GREENFIELD declares only applicable dimensions and invents no CI/CD, registry, tag, or deployment environment. Brownfield maps existing practice without rewriting historical release truth or inventing candidate identities/approvals. TASK-035 adds no CI/CD, release bot, tag automation, package publisher, deployment automation, or remote push.
