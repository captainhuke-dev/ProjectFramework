---
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.3.1"
project_source_framework_version: "1.4.0"
project_source_schema_version: "1.0.0"
approval_basis: "USER_EXPLICIT_IMPLEMENTATION_APPROVAL_2026-08_25"
compatibility: "BACKWARD_COMPATIBLE_UPGRADE_ACCELERATION_GOVERNANCE"
---

# Framework 1.4.0 Amendment — Upgrade Acceleration

Framework `1.4.0` preserves `1.3.1` unless refined here; Project Source Schema stays `1.0.0`; release format stays `3`. No new semantic slot, Stable-ID family, lifecycle state, authority family, or runtime artifact is created.

## 1. Per-release MIGRATION-NOTES

The distribution gains `managing-project-source/MIGRATION-NOTES.md`, a documentation surface with one section per release starting at the `1.3.x → 1.4.0` transition. Each section lists affected distribution surfaces and a short upgrade checklist. `FRAMEWORK-RELEASE.yaml` gains the optional field `migration_notes:` pointing at the current notes. Historical releases are not retroactively documented; where notes do not exist, that absence is stated explicitly and never invented. Migration notes are routing/documentation aids — they are not normative authority and never override Core Governance.

## 2. FAST_PATH RELEASE_FULL scope rule

For an initialized Project classified `FAST_PATH`, when the exact target candidate tree already carries committed state-bound evidence (the recorded tree SHA matches the observed target tree exactly), the upgrade may use proportional resulting-state confirmation — identity plus affected checks — instead of rerunning one full verification from scratch. Any change to the candidate after its evidence was captured invalidates reuse and fails closed back to the full requirement. `ASSESSED_PATH` and `MAJOR_MIGRATION_REQUIRED` keep the existing one-final-`RELEASE_FULL` requirement unchanged. This rule reuses Framework `1.2.5` evidence-reuse semantics; it adds no new verification state family.

## 3. Upgrade Preview template

The distribution gains `templates/upgrade-preview.md`: a standardized Preview structure for upgrade preparation covering current-vs-target identity, path classification (`FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED`), affected surfaces drawn from migration notes when present, a preservation checklist (current truth, Stable IDs, Project rules, bindings, history), rollback plan, and explicit approval block. The template is executable documentation, not normative authority.

## 4. Launcher compaction policy

Launcher maintenance adds an explicit compaction policy while keeping the `<=4,500` Unicode character ceiling unchanged: prose explanations may be compacted; canonical tokens, registered commands, lifecycle values, report labels, response-close fields, and marker identity may never be compacted, renamed, or dropped. Compaction must preserve byte-identical shared marker bodies between platform launchers.

## 5. `[Project Upgrade]` report references migration notes

When `[Project Upgrade]` reports `UPGRADE_AVAILABLE`, the report includes the target release's migration-notes pointer when such notes exist, so affected surfaces are visible before the user decides whether to prepare. When no notes exist for the target, the report states their absence explicitly. This changes only the report's content contract; comparison vocabulary and approval boundaries are unchanged.

## Non-goals

Framework `1.4.0` adds no automatic updater, parser service, validator product, CLI, hook, bot, CI/CD, scheduler, watcher, or runtime enforcement. Existing initialized Projects remain locally pinned and do not auto-upgrade.
