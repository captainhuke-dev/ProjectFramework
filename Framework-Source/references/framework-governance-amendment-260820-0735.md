# Project Source Framework Governance Amendment — 1.1.3

```yaml
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.1.2"
project_source_framework_version: "1.1.3"
project_source_schema_version: "1.0.0"
approved_at: "2026-08-20T07:35:00+07:00"
approval_basis: "USER_EXPLICIT_APPROVAL"
compatibility: "BACKWARD_COMPATIBLE_PLATFORM_BOOTSTRAP_CLARIFICATION"
```

## Purpose

Make ChatGPT Projects and Claude Projects first-class bootstrap entrypoints for the public ProjectFramework distribution without creating a second governance authority. The platform-specific instruction files tell an agent how to locate and initialize the canonical Project Source, then self-limit once a valid local pinned Project Source exists.

## Binding Changes

1. The distribution MUST include `managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md` for copy/paste into ChatGPT Project instructions.
2. The distribution MUST include `managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md` for copy/paste into Claude Project instructions.
3. Both files MUST contain the same byte-identical block between `PROJECTFRAMEWORK-SHARED-CONTRACT:START` and `PROJECTFRAMEWORK-SHARED-CONTRACT:END`. Platform-specific wrapper text MAY differ only to identify the platform and placement surface.
4. The shared contract MUST distinguish GREENFIELD bootstrap from an initialized existing project:
   - NEW project → bootstrap from canonical public repository `main`, then pin Framework/Schema locally.
   - Existing initialized project → local pinned Project Source is authoritative; upstream `main` is not a live replacement.
5. Platform project instructions are bootstrap/continuation launchers only. They MUST NOT replace, weaken, bypass, or override an active local `FRAMEWORK-001`.
6. Existing projects MUST NOT auto-upgrade when upstream advances. Upgrade or migration assessment uses the governed `MIG-*` process and explicit approval.
7. If required upstream or local Project Source content cannot be accessed, the agent MUST state the limitation and stop the affected governance mutation rather than reconstructing rules, slot mappings, authority, or facts from memory.
8. Active Framework distribution templates and bootstrap mockups for this release MUST pin Project Source Framework `1.1.3`; Project Source Schema remains `1.0.0`.

## Platform Placement

### ChatGPT Projects

Copy `CHATGPT-PROJECT-INSTRUCTIONS.md` into the Project's **Project settings → Instructions** field.

### Claude Projects

Copy `CLAUDE-PROJECT-INSTRUCTIONS.md` into the Project's **Set project instructions** field.

These placement instructions are distribution guidance. They do not alter the internal Project Source authority order.

## Shared Bootstrap Semantics

```text
platform project instructions
→ detect valid local Project-Source
   → if present: read local 00 → 01 → 03; local pin governs
   → if absent: read canonical repo main
      → README → SKILL → latest amendment → Core Governance
      → Framework template → skeletons → mockup
      → Preview → explicit approval
      → create 00 first
      → mandatory 01–05 and 09–17
      → conditional 06–08 only when applicable
      → 18–19 reserved; 20–99 on demand
      → pin Framework/Schema locally
```

## Compatibility and Migration

Project Source Framework changes from `1.1.2` to `1.1.3`; Project Source Schema remains `1.0.0`. This is a backward-compatible platform-bootstrap clarification. It adds distribution entrypoint artifacts, not a new Project Source semantic slot or mandatory active Project Source document.

Existing Projects remain pinned to their locally approved Framework/Schema versions. Adoption of 1.1.3 by an existing Project uses the governed `MIG-*` flow when an upgrade is desired.

## Non-Goals

This amendment does not add executable generation, validation, migration software, background automation, or a live dependency on GitHub. It does not add or define `CLAUDE.md` / Claude Code repository instructions; Claude Code integration is separate future scope if explicitly requested.

## Precedence

This 1.1.3 amendment is the latest binding clarification for platform Project bootstrap instructions. The 1.1.2 bootstrap mockup amendment remains binding for semantic-slot starter representation, and the 1.1.1 amendment remains binding for Materialized Current State, Stable-ID resolution, Manifest/CURRENT completeness, and archive independence.
