# Framework Governance Amendment — TASK-049 Canonical Self-Hosting Release Reconciliation

Status: **CURRENT / APPROVED**
Framework: **1.16.0**
Project Source Schema: **1.0.0**
Release format: **3**
Classification: **BACKWARD_COMPATIBLE_CANONICAL_SELF_HOSTING_LIFECYCLE_CLARIFICATION**

## 1. Purpose

Close the canonical-upstream self-hosting gap without weakening ordinary consuming-Project pinning. `captainhuke-dev/ProjectFramework` is both the canonical Framework distribution repository and an initialized Project using ProjectFramework governance. Once a verified Framework release is merged to its verified canonical integration target, the repository's own active Project Source and root Bootstrap must converge to that same release through a governed post-merge reconciliation rather than waiting for a redundant `[Project Upgrade]` invocation.

## 2. Canonical Self-Hosting Eligibility

The exception applies only when all of the following are freshly verified:

```text
repository identity = FRAMEWORK-RELEASE canonical_repository
canonical integration target = FRAMEWORK-RELEASE canonical_branch
verified Framework release identity/schema/release format are known
verified Framework-Source tree belongs to that merged release
release work has been merged to the canonical integration target
current Project is the canonical ProjectFramework repository itself
```

If any required identity, merge, release, or tree evidence is unresolved or contradictory, do not infer eligibility.

## 3. Mandatory Post-Merge Self-Hosting Reconciliation

For an eligible canonical ProjectFramework release merge, release integration is not fully reconciled until this governed workflow completes:

```text
verified Framework release merge
→ compare merged Framework release identity/tree with canonical ProjectFramework self-host Project Source/bootstrap
→ if already aligned: verify and record alignment
→ if not aligned: RECONCILIATION_REQUIRED
→ create governed FRAMEWORK-001 successor under applicable Root authority
→ preserve Project UUID, Project-specific truth, Stable IDs, bindings, and predecessor history
→ reconcile applicable active Project Source Framework/Schema metadata and routing to the same merged release
→ reconcile PROJECT-BOOTSTRAP.md to the promoted active root/release
→ validate resulting active routing + exact release identity/tree + history/binding preservation
→ record evidence/change/migration as applicable
→ only then treat canonical self-host release integration as reconciled
```

`RECONCILIATION_REQUIRED` is a workflow/diagnostic condition only. It is not a new Project lifecycle state family or Stable-ID family.

A canonical self-host transition under this rule does **not** require the user to invoke `[Project Upgrade]` again. Applicable Root Governance authority remains mandatory; this rule does not grant Root mutation authority by itself.

## 4. Consuming Projects Remain Pinned

This exception is narrow. Every ordinary initialized consuming Project remains locally pinned and continues to use `[Project Upgrade]` plus Direct-to-Latest assessment/Preview/approval/history/verification semantics before adopting a newer upstream Framework release.

Canonical ProjectFramework self-host reconciliation **must not** be generalized into consuming-Project auto-upgrade behavior.

## 5. Failure / Fail-Closed Contract

If the merged release identity/tree, canonical repository/branch identity, active Project Source, Bootstrap target, Root successor validity, or resulting reconciliation cannot be verified:

- keep/report `RECONCILIATION_REQUIRED` for the affected release-integration claim;
- do not fabricate a Framework pin, root successor, Bootstrap target, or migration result;
- do not claim canonical self-host release integration complete;
- preserve the last valid active Root and history until a valid successor can be promoted.

A Git merge alone is insufficient proof of completed self-host reconciliation.

## 6. Automation Boundary

“Automatic post-merge reconciliation” means an **unskippable governed workflow step** performed by an authorized Human/Agent when processing canonical release integration. TASK-049 creates no daemon, bot, watcher, Git hook, CI/CD mutation job, scheduler, auto-updater, runtime router, validator/CLI, or background self-modifying service.

## 7. Compatibility

Framework remains `1.16.0`, Project Source Schema remains `1.0.0`, and release format remains `3`. This amendment clarifies canonical repository release/self-host lifecycle behavior; it does not change semantic slots, Stable-ID families, Registered Commands, consuming-Project upgrade semantics, or runtime implementation scope.
