---
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.2.6"
project_source_framework_version: "1.3.0"
project_source_schema_version: "1.0.0"
approval_basis: "USER_EXPLICIT_APPROVAL_ALL_PENDING_TASKS_2026-08-23"
compatibility: "BACKWARD_COMPATIBLE_COMMAND_DISCOVERY_RESPONSE_RENDERING_AND_DIRECT_TO_LATEST_UPGRADE_GOVERNANCE"
---

# Framework 1.3.0 — Command Contract and Direct-to-Latest Upgrade Governance Amendment

Framework `1.3.0` preserves Framework `1.2.1–1.2.6` semantics unless explicitly refined here. Project Source Schema remains `1.0.0`; no semantic slot, Stable-ID family, Project lifecycle state, Git freshness state, Epistemic Status value, authority family, branch-authority field, or executable enforcement runtime is added.

Existing initialized Projects remain governed by their locally pinned active `FRAMEWORK-001` and do not auto-upgrade merely because upstream ProjectFramework advances to `1.3.0`.

## Registered Bracketed Project Commands

Framework `1.3.0` defines a small semantic command registry for common Project inspection. A registered command requires literal `[` and `]` delimiters; command-name matching inside the brackets is case-insensitive. Missing brackets do not invoke the registered command token.

Initial registry:

```text
[Project Status] : fresh Project/Task/Git/verification/blocker status dashboard
[Project Path]   : show/verify configured bootstrap path values and route explicit change requests through existing location governance
```

Natural-language command-help requests list only commands registered by the active Framework/Project as `[XXX] : purpose`. They do not authorize invention of new commands.

### `[Project Status]`

`[Project Status]` is read-only and fresh-observation driven. When applicable it reports Identity, Project Health, Remain Tasks, Git Sync, Working Tree, Verification, and Blockers. Project Health reuses `GREEN | AMBER | RED | UNKNOWN`. Task count comes from the applicable Task source; Git working-tree changes are a separate dimension and MUST NOT be converted into a logical Task count.

A verified Workspace-vs-Remote sync claim requires current remote freshness evidence appropriate to the report. Unavailable/unresolved dimensions remain explicit `UNKNOWN` / `VERIFICATION_REQUIRED`; chat memory, cached remote refs, recent workspace selection, or previous status output do not become current truth automatically.

### `[Project Path]`

`[Project Path]` surfaces the configured Project Settings/bootstrap values for Framework Remote Path, Git Remote Path, Storage Path, MCP Path, and Workspace Path. A value still represented by an angle-bracket placeholder such as `<STORAGE>` or `<WS>` means **unset / not configured**, never a literal filesystem/network path.

The command may carry an explicit request to change a path, but creates no mutation authority. One-off exact targets remain action-specific. Persistent Bootstrap/Project Location changes continue to require explicit approval and, where active Root Governance is affected, the existing `FRAMEWORK-001` revision → validate → promote → supersede/archive flow. Missing/unset paths never authorize fallback to recent, active, mounted, search-ranked, or similarly named locations.

## Markdown-Safe Mandatory Response Close

Framework `1.3.0` preserves the canonical semantic response-close labels and lifecycle tokens while hardening their Markdown presentation. Because a bare paragraph beginning `[Chat]: value` may be interpreted by some Markdown renderers as reference-definition syntax, a Markdown-safe presentation wrapper SHOULD be used:

```text
**[Next Action]:** <one exact next action or ไม่มีขั้นตอนถัดไป>

**[Chat]:** CONTINUE_CURRENT_CHAT | START_NEW_CHAT

**[Reason]:** <concise reason>

**[Required Read]:** <canonical locations or ไม่มี>
```

The wrapper is presentation-only. Semantic labels remain `[Next Action]:`, `[Chat]:`, `[Reason]:`, `[Required Read]:`; lifecycle vocabulary remains exactly `CONTINUE_CURRENT_CHAT | START_NEW_CHAT`. The Response Close Completeness Gate validates one visible semantic field of each kind, in order, lifecycle-consistent, with Required Read final. User-reported rendering omissions remain regression evidence without inventing the loss layer.

## Direct-to-Latest / Cumulative Target-State Upgrade

Framework `1.3.0` changes the default **upgrade execution architecture**, not Project history preservation.

Core invariant:

> Upgrade cost SHOULD scale with the affected semantic difference between current reconstructable Project state and the approved target Framework, not with the number of releases skipped.

An initialized Project does not execute every historical Framework migration/amendment sequentially merely because intermediate releases existed. Historical amendments, Git history, existing `MIG-*`, superseded revisions, and provenance remain preserved rationale/history and are not deleted.

Governed flow:

```text
resolve active current Project/local pin
→ materialize current reconstructable truth
→ resolve explicitly selected target Framework
→ compare current state directly with target required semantics
→ classify cumulative semantic delta
→ choose upgrade path
→ Preview delta + preservation + rollback
→ explicit approval
→ apply required current→target changes only
→ affected/risk-scoped verification
→ RELEASE_FULL once on the final unchanged target candidate
→ promote target Framework revision and preserve superseded/history state
```

Assessment labels may use `ALREADY_SATISFIED | REQUIRED | NOT_APPLICABLE | VERIFICATION_REQUIRED | CONFLICT_REVIEW` as migration-report vocabulary only; they do not create new Framework state families.

Direct-upgrade path classes are exactly:

```text
FAST_PATH
ASSESSED_PATH
MAJOR_MIGRATION_REQUIRED
```

- `FAST_PATH` — bounded compatible target delta with reconstructable current truth and no material unresolved conflict.
- `ASSESSED_PATH` — one cumulative `MIG-*` assessment/plan is required, but direct current→target migration is safely bounded without replaying each intermediate release.
- `MAJOR_MIGRATION_REQUIRED` — breaking schema/namespace/root semantics, non-reconstructable current truth, or unresolved material conflicts/unknowns prevent safe bounded direct migration.

Skipping intermediate **execution** never skips compatibility assessment, authorization, Preview/approval, rollback/reversibility, validation, evidence, promotion, or history preservation.

The maintained current starter is the target representation for NEW Projects. It is **not** the default destructive upgrade mechanism for initialized Projects. Full reconstruction from the starter is reserved for explicitly approved `MAJOR_MIGRATION_REQUIRED` work with preservation/mapping controls.

Framework `1.3.0` reuses Framework `1.2.5` progressive verification: affected/risk-scoped checks during migration, `CHECKPOINT_INTEGRITY` at logical checkpoints, one `RELEASE_FULL` for the final unchanged candidate, and `INTEGRATION_GATE` evidence-validity/Base-Freshness checks. It does not require one full verification run per skipped historical release.

## Compatibility and Scope

This amendment authorizes governance/documentation/bootstrap semantics only. It adds no automatic updater, migration engine, command parser service, CLI, validator product, hook, bot, CI/CD workflow, scheduler, watcher, branch switcher, workspace auto-selector, credential store, or runtime enforcement.

All existing location/authority separation, Base Freshness, Canonical Implementation Source, Runtime Truth, persistence, task-completion, verification, secret-reference, and history-preservation contracts remain binding.
