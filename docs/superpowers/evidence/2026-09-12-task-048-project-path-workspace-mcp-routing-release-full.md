# TASK-048 Project Path Workspace & MCP Routing — RELEASE_FULL Evidence

Date: `2026-09-12`
Task: `TASK-048`
Result: `LOCAL_VERIFIED_COMPLETE / PUBLICATION_NOT_AUTHORIZED`

## Release Identity

```text
Framework: 1.16.0
Schema: 1.0.0
Release format: 3
Candidate commit: abc4b5316a7f3bbc9b4a8c0f5b5c509904a26185
Candidate tree: 266b2cf7d03d516c9bcab9f81790a92f3c84d9c7
Framework-Source tree: 5e06595f419d21b03ed2ef8e959189594628dbf2
Execution base: 9160410b3dfc0420379b5995926c83f0de4ff536
Branch: task048-framework116
```

The final verified Framework candidate is the exact unchanged candidate above. The active ProjectFramework consuming Project Source remains pinned to Framework `1.15.0`; TASK-048 distribution development did not upgrade or mutate that local Project Source pin.

## Implementation Checkpoints

```text
79843e3  test(task048): define project path routing scenarios
90b1e68  feat(framework): add project path routing contract
bb67ef5  docs(framework): define workspace relocation and production applicability
2b88f54  docs(framework): add MCP fallback and failback profile
004c631  docs(framework): propagate project path routing release
d7876ba  first candidate freeze — invalidated by verifier infrastructure failure
abc4b53  replacement candidate freeze — final verified candidate
```

## TDD / Progressive Verification

```text
TDD RED:                TASK048_RED 9/18 (expected pre-implementation failure)
Structural GREEN:       TASK048_STRUCTURAL 18/18 PASS
Cumulative AFFECTED:    TASK048_AFFECTED 47/47 PASS
Post-verifier repair:   TASK048_AFFECTED 47/47 PASS
Final RELEASE_FULL:     TASK048_RELEASE_FULL 56/56 PASS
Scenario range:         1–468 contiguous and unique
TASK-048 scenarios:     433–468
Starter stamps:         22/22 at Framework 1.16.0 / Schema 1.0.0
```

`git diff --check` passed for each implementation checkpoint and the final base-to-candidate release scope.

## Invalidated Candidate / Verifier Repair

Candidate `d7876ba288f9f113f831cc4540d5069494f84736` (tree `c01d6a105b40a515e74f16c10a7ea0ec4f025c27`, same Framework-Source tree `5e06595f419d21b03ed2ef8e959189594628dbf2`) was invalidated when the first release-mode invocation terminated before semantic release assertions: the scratch Python verifier decoded `git show` output through Windows `cp874` and raised `UnicodeDecodeError` on Unicode scenario content.

This was a verifier-infrastructure failure, not a Framework semantic failure. The ignored scratch verifier was repaired to decode Git subprocess output explicitly as UTF-8, AFFECTED was rerun `47/47 PASS`, the invalidation was persisted in the Task ledger, and replacement candidate `abc4b5316a7f3bbc9b4a8c0f5b5c509904a26185` was frozen.

The replacement candidate then received exactly one `release_full` invocation and passed `56/56`. The passing candidate was not rerun.

## Verified TASK-048 Contract

### Strict `[Project Path]`

The current Framework distribution preserves exactly eight top-level sections in order:

```text
Framework Path
→ Git Path
→ Storage Path
→ Develop Workspace
→ Production Workspace
→ MCP Execution
→ Build / Deployment Mapping
→ Continuity
```

Command-body strictness remains governed by TASK-043, and TASK-045 visible response-close semantics remain unchanged.

### Canonical ownership

Verification confirms:

```text
FRAMEWORK-001 / Project Location Binding
  = repository + environment-scoped Local Workspace routing only

40 Technical Design / Development Workspace Contract
  = active Develop Workspace role/type/locator/durability/source relationship

60 Deployment Plan
  = Production applicability/runtime target/artifact/deployment mapping

Project-Execution/tools.md
  = exact MCP selection policy

Project-Execution/fallback-log.md
  = append-only actual fallback/recovery incident history
```

`project_location_binding.local_workspaces` does not acquire `workspace_role`, `source_mutation`, active Develop Workspace, Canonical Implementation Source, or Production runtime authority.

### Develop / Production workspace boundary

Develop Workspace owns edit/build/test/package/verify routing. Local ↔ Remote Durable relocation is symmetric and requires durable checkpointing of required source state plus repository/source identity, intended revision, durability/recovery, and working-tree verification. Git Remote is explicitly not a Remote Durable Develop Workspace locator. Promotion yields one active Develop Workspace per affected scope unless a separately governed multi-writer architecture exists.

Production applicability is exact `APPLICABLE | NOT_APPLICABLE | VERIFICATION_REQUIRED`. Direct Production source mutation is `FORBIDDEN`; implementation correction returns through canonical Develop source → verification/build/package → deployment → runtime verification.

### MCP fallback / unknown-result / failback

Verification confirms:

- exact Primary MCP when eligible;
- fallback only through explicit `ORDERED_ALLOW_LIST` / declared `fallback_order`;
- no fallback eligibility from availability, recency, similarity, ranking, or connected state;
- eligibility includes applicable capability/tool availability, active policy, and verified bound target identity;
- Material fallback mutation requires durable `FALLBACK_STARTED` incident persistence first;
- unknown potentially-applied effects enter `RESULT_VERIFICATION_REQUIRED` and are verified before retry;
- unprovable result is `FAIL_CLOSED`;
- `CHECKPOINT_FAILBACK` prevents mid-action switching and returns the next action to reverified Primary after the current checkpoint is completed/persisted/verified;
- fallback-to-next-fallback transitions follow declared order and are logged.

`fallback-log.md` is applicability-driven, append-only, outside Project Source authority, not an `AUTH-*` surface, not a Stable-ID registry, and stores no credentials/secret values.

## Compatibility / Preservation

Verified preservation includes:

- Framework `1.16.0` / Schema `1.0.0` / release format `3`;
- exactly seven Registered Commands, with no new workspace/failover command;
- TASK-043 Command Contract Completeness Gate before TASK-045 Response Close Completeness Gate;
- historical scenarios `1–432` byte-prefix preserved, with TASK-048 appended as `433–468`;
- TASK-043 and TASK-045 historical amendment files unchanged;
- thin ChatGPT/Claude launchers and maintained bootstrap template unchanged;
- root `PROJECT-BOOTSTRAP.md` still identifies the initialized Project as Framework `1.15.0`;
- active `Project-Source/00` still carries `project_source_framework_version: "1.15.0"`;
- no Project-Source file changed from the TASK-048 execution base;
- all TASK-048 Framework changes are Markdown/YAML governance/distribution artifacts; no runtime/code artifact was introduced;
- Direct-to-Latest upgrade behavior remains in migration guidance.

## Publication Boundary

Fresh remote observation was performed before final release verification. Remote branch `task048-framework116` was absent from `origin`.

```text
Publication authorization: NOT_AUTHORIZED
Push: NOT_PUSHED
Merge: NOT_MERGED
Release publication: NOT_RELEASED
```

`commit ≠ push`. This evidence establishes local verified Framework 1.16.0 completion only; it does not authorize publication, merge, Project Upgrade, or mutation of the initialized Project's active Framework pin.
