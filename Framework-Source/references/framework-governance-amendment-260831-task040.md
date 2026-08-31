---
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.8.0"
project_source_framework_version: "1.8.0"
project_source_schema_version: "1.0.0"
approval_basis: "USER_EXPLICIT_COMMAND_RENAME_APPROVAL_2026-08-31"
compatibility: "CURRENT_COMMAND_RENAME_ENV_SEMANTICS_UNCHANGED"
---

# Framework 1.8.0 Amendment — Canonical `[Session]` Command Rename

This amendment changes only the current registered command name for bounded session/task operation scope. Existing `ENV-*` semantics, authority boundaries, lifecycle behavior, Stable-ID ownership, and Project Source Schema remain unchanged. Historical amendments/specs/plans/evidence retain the command spelling that was true when captured.

## 1. Canonical command identity

The current registered command is exactly:

```text
[Session] : declare, show, or close the user-pre-approved scope of operations for the current session/task
```

The historical longer command name is no longer a registered current alias. Literal brackets remain required and registered-name matching inside brackets remains case-insensitive. Natural-language help lists `[Session]`, not the historical spelling.

## 2. Semantics remain unchanged

`[Session] declare` records a bounded `ENV-*` entry in `15 Action Registry` with allowed operation types, target surfaces, expiry, and prohibited zones. `show` displays the active Envelope and remaining validity. `close` ends it early. Goal-derived `ENV-*` remains equal to or narrower than valid parent Goal `AUTH-*`. No `SESSION-*` family is introduced.

## 3. Fail-closed boundaries remain unchanged

The rename grants no new authority. Project Location/Binding changes, Root Governance mutation, schema/slot authority, secret handling, push/publication, destructive actions, external disclosure, and higher-level platform/tool confirmations retain their existing gates. Ambiguous or out-of-scope operations fail closed to normal approval.

## 4. Current vs historical surfaces

Current Core Governance, SKILL, launchers, README, maintained starter surfaces, migration guidance, and pressure scenarios use `[Session]`. Historical TASK-021/TASK-024 amendments, completed specs/plans/evidence, archived Project Source, and Git history are not rewritten merely to modernize terminology.

## Non-goals

No Framework version bump, Schema change, new semantic slot, new Stable-ID family, runtime parser, alias layer, migration engine, automation, or authorization expansion is introduced.
