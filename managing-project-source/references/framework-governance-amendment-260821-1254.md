---
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.2.0"
project_source_framework_version: "1.2.1"
project_source_schema_version: "1.0.0"
approved_at: "2026-08-21T12:54:00+07:00"
approval_basis: "USER_EXPLICIT_APPROVAL"
compatibility: "BACKWARD_COMPATIBLE_MCP_PERSISTENCE_AND_CHAT_LIFECYCLE_GOVERNANCE"
---

# Framework Governance Amendment — MCP Persistence and Chat Lifecycle

## Binding Change

Framework `1.2.1` adds **Externalized Working Memory and Chat Lifecycle** governance while preserving the Project Source Schema `1.0.0`, semantic-slot namespace, and existing Project-local pinning model.

The binding changes are:

1. Connector/MCP activity is classified as **Material Project Work** or **Transient MCP Activity**. Transient reads/searches/comparisons do not require persistence by default.
2. Material Project Work is persisted at a **Logical Checkpoint**, not once per tool call.
3. GitHub-backed Material work persists to the owning repository artifact or canonical Project Source semantic home. Google Drive Material work updates an existing designated progress `.md`; if none exists and durable continuation state is required, one stable `PROJECT-PROGRESS.md` may be used as a continuation cache, not authority.
4. Cross-system continuation uses pointers to source-native owners. Do not create a third duplicate source of truth.
5. Do not persist raw MCP/tool payloads, long search dumps, full diffs, repetitive intermediate state, or private intermediate reasoning merely for audit convenience. `09 Handoff` remains a continuation contract, not an MCP transcript.
6. If required durable state cannot be written, record/report `PERSISTENCE_PENDING`, identify what remains unpersisted, and default to `CONTINUE_CURRENT_CHAT`.
7. Chat lifecycle vocabulary is exactly `CONTINUE_CURRENT_CHAT` or `START_NEW_CHAT`. A safe `START_NEW_CHAT` recommendation requires durable current state, blocker/pending state, Exact Next Action, and Required Read locations outside Chat.
8. A new chat/session must be able to continue from persisted state and Required Read pointers without the old chat transcript as a prerequisite.
9. Every governed response ends with `ทำอะไรไป?` then `และถัดไปคืออะไร?`; the second section includes `Next Action`, `Chat`, `Reason`, and `Required Read`, with no content after it.
10. Complete ChatGPT and Claude Project launchers remain `<= 4,500` Unicode characters, and the text between shared-contract markers remains byte-identical.
11. Project Source Schema remains `1.0.0`; no semantic-slot or Stable-ID namespace change is introduced. Existing initialized Projects remain locally pinned and never auto-upgrade from upstream.

## Scope Boundary

This amendment changes governance/workflow semantics only. It does not authorize application code, Docker/runtime artifacts, executable validators, CI/CD, schedulers, background agents, connector transcript storage, or enforcement software.

## Compatibility

Framework `1.2.1` is backward compatible with Schema `1.0.0`. Existing Projects continue under their approved local Framework pin until a governed migration explicitly upgrades them.
