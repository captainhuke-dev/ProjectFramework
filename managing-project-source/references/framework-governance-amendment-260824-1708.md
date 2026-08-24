---
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.3.0"
project_source_framework_version: "1.3.1"
project_source_schema_version: "1.0.0"
approval_basis: "USER_EXPLICIT_IMPLEMENTATION_APPROVAL_2026-08-24"
compatibility: "BACKWARD_COMPATIBLE_PROJECT_UPGRADE_COMMAND_GOVERNANCE"
---

# Framework 1.3.1 — Project Upgrade Command Governance Amendment

Framework `1.3.1` preserves Framework `1.3.0` semantics unless explicitly refined here. Project Source Schema remains `1.0.0`; no semantic slot, Stable-ID family, Project lifecycle state, Git freshness state, Epistemic Status value, authority family, branch-authority field, or executable enforcement runtime is added.

Existing initialized Projects remain governed by their locally pinned active `FRAMEWORK-001`. Canonical upstream is a target candidate for comparison and never silently replaces the current Project Framework authority.

## Registered `[Project Upgrade]` Command

Framework `1.3.1` extends the registered command registry with:

```text
[Project Upgrade] : fresh-compare the active Project Framework with canonical upstream and offer governed upgrade preparation when they differ
```

Existing registered-command rules remain binding: literal `[` and `]` are required; matching inside the brackets is case-insensitive; natural-language command discovery lists only registered commands.

`[Project Upgrade]` is read-only through comparison and reporting. For an initialized Project it resolves current Framework identity from the active local `FRAMEWORK-001`, then fresh-resolves the applicable canonical upstream target. A cached remote-tracking ref, chat memory, prior command output, recent workspace ranking, similarly named repository, or other inferred fallback is insufficient for a current/latest upstream claim.

Minimum comparison considers Framework version, Schema version, observable source/distribution identity, and freshness evidence. Report vocabulary is exactly:

```text
UP_TO_DATE
UPGRADE_AVAILABLE
SOURCE_DIVERGENCE
VERIFICATION_REQUIRED
```

These values are command-report vocabulary only. They do not create new lifecycle, Epistemic Status, Git freshness, authority, migration, or health state families. Equal version strings do not override a material source/distribution conflict; such a conflict is surfaced as `SOURCE_DIVERGENCE` or `VERIFICATION_REQUIRED` rather than silently reported `UP_TO_DATE`.

If the verified target differs from the current local pin, `UPGRADE_AVAILABLE` asks whether the user wants to **prepare** an upgrade. A positive answer authorizes current→target cumulative assessment and Preview preparation only; it is not mutation approval.

## Governed Upgrade Handoff

Actual Project mutation continues to use the existing Direct-to-Latest architecture:

```text
materialize reconstructable current truth
→ resolve selected target Framework
→ compare current state directly with target semantics
→ classify FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED
→ Preview required delta + preservation + rollback/reversibility
→ separate explicit mutation approval
→ apply approved current→target changes only
→ affected/risk-scoped verification
→ RELEASE_FULL once on the final unchanged target candidate
→ governed promotion and history preservation
```

Upgrade preparation preserves applicable Stable IDs, Project-specific rules, current truth, Requirements, Decisions, Project Location and other governed bindings, authority/delegation state, Task/Action truth, migration/history/provenance, approval, rollback/reversibility, validation, and evidence. Intermediate historical Framework execution remains non-mandatory. The maintained latest starter remains a NEW-Project target representation, not a default destructive rebuild mechanism for initialized Projects.

`[Project Upgrade]` creates no Bootstrap/Project Location mutation authority, branch/worktree authority, Canonical Integration Target, Canonical Implementation Source, Runtime/Persistent-State authority, automatic updater, command parser service, CLI, validator, hook, bot, CI/CD workflow, scheduler, watcher, or background automation runtime.

All existing location/authority separation, Base Freshness, task-completion, progressive verification, response-close, secret-reference, and history-preservation contracts remain binding. `commit ≠ push` remains unchanged.
