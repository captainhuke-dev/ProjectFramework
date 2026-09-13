# Upgrade Preview

Standard state-bound transaction contract for an initialized-Project Framework upgrade. Fill only from observed current state and the exact selected target; never invent values. This template is executable documentation, not normative authority — Core Governance and the latest amendment win on conflict.

## 1. Current Project and target identity

```text
Current Project / repository identity: <verified identity>
Current local pin (FRAMEWORK-001):      <Framework / Schema / amendment pointer>
Exact Target Framework:                 <version>
Target Schema:                          <version>
Target release format:                  <integer>
Target source / ref:                    <observed source/ref or UNKNOWN>
Target tree / content identity:         <observed SHA/digest or UNKNOWN>
Path Classification:                    FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED
One-Session Eligibility:                ELIGIBLE | NOT_ELIGIBLE | VERIFICATION_REQUIRED
```

`One-Session Eligibility` is Preview working vocabulary only; it is not lifecycle, Risk, authority, migration status, Epistemic Status, or a Stable-ID family.

## 2. Comparison and cumulative assessment

```text
[Project Upgrade] report: UP_TO_DATE | UPGRADE_AVAILABLE | SOURCE_DIVERGENCE | VERIFICATION_REQUIRED
Migration notes for target: <pointer or "none exist">
Cumulative current→target assessment: <bounded summary>
Material assumptions: <candidate / compatibility / dependency / authority assumptions>
```

`[Project Upgrade]` performs this read-only comparison, assessment, classification, eligibility assessment, and exact Preview in one pass. No separate “prepare?” approval is required before this read-only work.

## 3. Affected transaction surfaces

List only surfaces the exact target transaction will mutate:

```text
Project Source: <exact slots/documents or NONE>
Root FRAMEWORK-001: <successor delta or NONE>
PROJECT-BOOTSTRAP: <delta or NONE>
Other governed local artifacts: <exact list or NONE>
```

## 4. Preservation invariants

Every applicable item must have an observed preservation basis before mutation approval:

```text
[ ] Project UUID / identity
[ ] current truth documents
[ ] Project-specific rules
[ ] Stable IDs / references
[ ] Project Location Binding values
[ ] repository / Drive / local / storage bindings when applicable
[ ] predecessor history / provenance
[ ] active Goal / Authority / Task truth
[ ] secrets remain references only
```

## 5. Rollback / recovery route

```text
Pre-upgrade durable state: <commit/ref/current active revisions>
Reversal mechanism:       <exact bounded recovery route>
Verification after rollback: <minimum sufficient resulting-state checks>
Partial-transaction recovery: <how durable completed effects are detected/reused>
```

## 6. Framework Release Evidence Reuse Decision

```text
Framework Release Acceptance evidence: <EVD/path/commit/tree or NONE>
Observed target tree/content identity:   <exact identity>
Evidence binding match:                  MATCH | MISMATCH | VERIFICATION_REQUIRED
Release proof reuse:                     REUSE | DO_NOT_REUSE | VERIFICATION_REQUIRED
Reason:                                  <bounded state-based reason>
```

Framework Release Acceptance is distinct from Project Upgrade Acceptance. Reuse is allowed only when exact target identity/tree/content and material assumptions match committed current state-bound evidence.

## 7. Project Upgrade Verification Plan

```text
Project affected verification: REQUIRED
Affected invariants: <Root / Project Source / routing / Bootstrap / UUID / Stable IDs / bindings / history / rollback / other>
RELEASE_FULL for consuming upgrade: 0 when exact release proof is reusable; otherwise at most 1 when genuinely required on the exact unchanged candidate
Terminal resulting-state confirmation: <exact checks>
```

Release-proof reuse never removes Project-specific affected verification.

## 8. Publication / integration and canonical self-host scope

```text
Local upgrade mutation scope:       <exact authorized scope>
Integration / publication scope:    <authorized exact target or NOT_AUTHORIZED>
Canonical self-host applicable:     YES | NO | VERIFICATION_REQUIRED
Self-host mutation scope:           <exact approved Root/Project Source/Bootstrap delta or NOT_AUTHORIZED>
INTEGRATION_GATE required:          YES when mutable-target action is applicable
```

When the same exact Preview and authority cover canonical integration plus post-merge self-host reconciliation, those steps may chain in one transaction after fresh merged-result verification. Missing Root authority stops at `RECONCILIATION_REQUIRED`.

## 9. Exact mutation authority requested

```text
Human mutation approval requested for: <exact bounded transaction>
Explicit exclusions / stop boundaries: <push / merge / Root / Binding / disclosure / destructive / other as applicable>
Approval binds to target candidate:    <exact tree/content identity>
Preview fingerprint / assumptions:     <reconstructable identity of this Preview and material assumptions>
```

## 10. Approval validity

```text
Mutation approval: <PENDING | APPROVED by ACTOR-001/date/evidence | REJECTED>
```

Approval is state-bound to this exact Preview/candidate. Material candidate/tree, path-class, semantic-scope, compatibility, binding, rollback, or required-authority changes require re-Preview and reapproval.

Deterministic monotonic revision numbers, timestamps, successor filenames, and routing/index/manifest references implied by the approved transaction do not require reapproval by themselves.

## 11. Known stop boundaries

```text
MAJOR_MIGRATION_REQUIRED          → stop One-Session Fast Path
missing mutation authority        → no Material upgrade mutation
local-only authority              → stop before integration
integration authority without Root authority → integration may complete, then RECONCILIATION_REQUIRED
unknown shared/non-idempotent result → RESULT_VERIFICATION_REQUIRED before retry
material approved assumption change → re-Preview / reapproval
```
