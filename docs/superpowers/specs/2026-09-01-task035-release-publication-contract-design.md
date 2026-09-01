# TASK-035 Project Release / Publication Contract — Design

**Task:** TASK-035 — Project Release / Publication Contract
**Design state:** USER_APPROVED_SET1_DIRECTION / WRITTEN_SPEC_APPROVED_BY_GOAL
**Set 1 position:** 4 of 5
**Depends on:** TASK-034
**Target Framework:** 1.12.0
**Project Source Schema:** 1.0.0
**Release format:** 3

## 1. Purpose

ProjectFramework already preserves `commit ≠ push`, Task completion checkpoints, `RELEASE_FULL`, and `INTEGRATION_GATE`, but it lacks one standard contract for distinguishing implementation completion, integration, repository publication, release, artifact publication, and deployment.

TASK-035 defines **orthogonal publication dimensions** rather than forcing every Project through one linear lifecycle.

Core invariants:

```text
Task DONE ≠ MERGED ≠ PUSHED ≠ RELEASED ≠ ARTIFACT_PUBLISHED ≠ DEPLOYED
Implementation authority ≠ publication authority
Release evidence ≠ deployment evidence
Tag presence ≠ release truth unless the Project declares it material
```

## 2. Publication dimensions

When material, current state is represented across independent dimensions:

```text
Implementation:       NOT_DONE | DONE
Integration:          NOT_APPLICABLE | NOT_MERGED | MERGED
Repository Publication: NOT_APPLICABLE | NOT_PUSHED | PUSHED
Release:              NOT_APPLICABLE | NOT_RELEASED | RELEASED
Artifact Publication: NOT_APPLICABLE | NOT_PUBLISHED | PUBLISHED
Deployment:           NOT_APPLICABLE | NOT_DEPLOYED | DEPLOYED
```

These are lifecycle/reporting values, not new Stable-ID families. A Project MAY omit dimensions that are genuinely not applicable. `PUSHED` does not imply `MERGED`; `MERGED` does not imply a formal release; a release may exist without deployable artifacts; deployment may be intentionally separate from release publication.

## 3. Release Candidate identity

A material Release Candidate (RC) is evidence-bound to the minimum identity sufficient for the Project:

```text
source/repository identity
candidate commit/ref when Git-backed
candidate tree/content digest when material
Framework/distribution tree when releasing ProjectFramework
version/release identifier
schema/version compatibility when applicable
verification evidence pointers
captured prerequisites/assumptions
```

Exact Git SHA/tag is used when observed/material and never fabricated. Non-Git Projects use their declared source-native identity/digest.

An RC becomes invalid for prior acceptance evidence when its bound source/tree/content or material assumptions change. Evidence reuse follows existing progressive verification rules.

## 4. Verification relationship

`RELEASE_FULL` is the full candidate/distribution acceptance check at the release-candidate boundary. It does not push, merge, tag, publish artifacts, or deploy.

`INTEGRATION_GATE` is evaluated immediately before integration/publication actions that depend on a mutable canonical target. It re-resolves Base Freshness and prior evidence validity. If candidate or material target assumptions changed, affected/full reverification occurs as existing rules require.

Resulting-state confirmation after an exact verified fast-forward/publication may reuse valid candidate evidence rather than rerunning a full release verification solely because the commit was transported.

## 5. Approval and authority

The contract separates local implementation completion from shared/external side effects:

- local design/edit/test/commit authority does not imply push;
- push does not imply merge authority;
- merge does not imply release/tag/artifact publication;
- release approval does not imply deployment;
- deployment approval does not imply disclosure of secrets or unrelated external context.

A persistent `[Goal]` includes publication only when its authorization scope says so explicitly. `commit ≠ push` remains binding.

## 6. Release record and evidence

No mandatory new semantic slot or `REL-*`-like release family is introduced. Material release/publication facts are preserved through existing homes:

- `10 Change Log` — material state transitions/events;
- `13 Evidence Registry / EVD-*` — reconstructable candidate, verification, publication/deployment evidence when material;
- `03 Current State` — current summary;
- `09 Handoff` — continuation/pending publication when relevant;
- `15 Action Registry` — execution action/envelope;
- `91` — outcome/gate/risk/change-request objects when materially applicable.

Repository-native releases/tags/package registries/deployment systems remain external/source-native evidence, not Project authority by themselves.

## 7. Partial and failed publication

A multi-step publication may be partially complete. The Framework reports dimension-specific truth rather than collapsing it into one success/failure flag.

Examples:

```text
PUSHED + NOT_MERGED
MERGED + NOT_RELEASED
RELEASED + ARTIFACT NOT_PUBLISHED
RELEASED + DEPLOYMENT NOT_APPLICABLE
ARTIFACT PUBLISHED + DEPLOYMENT FAILED/NOT_DEPLOYED
```

When a required durable reconciliation cannot be written after an external publication succeeds, existing `PERSISTENCE_PENDING` semantics apply. The external fact remains reported as observed; Project Source is not falsely declared reconciled.

## 8. Retraction, rollback, and supersession

Release correction distinguishes:

- **rollback** — runtime/deployment or integration is moved back to a prior accepted state;
- **retraction** — a published release/artifact is declared withdrawn where the external system supports it;
- **supersession** — a newer release replaces an earlier one without erasing history.

Historical release evidence is preserved. Tags/artifacts are never deleted or rewritten automatically merely to make history look clean. If an external platform cannot retract an artifact, record the limitation and superseding state rather than claiming deletion.

## 9. Optional assurance

Immutable tags, signed commits, checksums, package attestations, protected branches, release notes, and artifact signatures may increase assurance when applicable. They are optional unless the Project explicitly requires them. Missing optional assurance must not be fabricated into a blocker or provenance claim.

## 10. Set 1 integration

TASK-037 uses these publication dimensions to reason about trust crossings for repositories, artifacts, releases, deployment targets, and privileged runtimes. TASK-035 therefore precedes TASK-037 in Set 1.

## 11. GREENFIELD/Brownfield

GREENFIELD declares only publication dimensions that are applicable to its actual delivery model. It does not synthesize CI/CD, package registries, tags, release bots, or deployment environments.

Brownfield adoption maps existing practices to the new dimensions without rewriting historical release facts or inventing candidate identities/approvals.

## 12. Affected surfaces and verification

Implementation updates current release/amendment/Core/SKILL/README/migration/templates/task/tests and relevant starter guidance. It creates no CI/CD, release bot, tag, package publisher, deployment automation, or remote push.

Pressure/AFFECTED verification must prove orthogonal state separation; `commit ≠ push`; RC identity/evidence invalidation; RELEASE_FULL versus INTEGRATION_GATE; partial publication truth; PERSISTENCE_PENDING after external success/local reconciliation failure; retraction/rollback/supersession preservation; optional assurance; authority separation; no publication automation.
