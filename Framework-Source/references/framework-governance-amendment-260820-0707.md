# Project Source Framework Governance Amendment — 1.1.2

```yaml
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.1.1"
project_source_framework_version: "1.1.2"
project_source_schema_version: "1.0.0"
approved_at: "2026-08-20T07:07:00+07:00"
approval_basis: "USER_EXPLICIT_APPROVAL"
compatibility: "BACKWARD_COMPATIBLE_BOOTSTRAP_CLARIFICATION"
```

## Purpose

Make the existing Project Source semantic-slot namespace concrete at bootstrap time. Framework 1.1.1 already defined the authoritative `00–17`, reserved `18–19`, and extended `20–99` taxonomy, but the distribution exposed that mapping mainly through prose and a consolidated skeleton file. Framework 1.1.2 adds a canonical mockup/starter representation so a new agent can see *which number means which document* without reconstructing the filesystem mentally.

## Binding Changes

1. The distribution MUST include `templates/project-source-mockup/README.md` with the authoritative slot-to-document view copied from Core Governance.
2. The distribution MUST include `.template.md` starter files for semantic slots `00–17`.
3. The presence of templates does not change applicability: `06 Architecture`, `07 Implementation Plan`, and `08 Open Issues` remain CONDITIONAL and MUST NOT be created as empty active documents merely to look complete.
4. Slots `18–19` remain RESERVED and MUST NOT be materialized as active documents or default starter outputs.
5. Extended taxonomy `20–99` remains create-on-demand; it is mapped in the mockup README but not pre-created as empty files.
6. Active Project Source filenames continue to use governed revision/timestamp naming. `.template.md` filenames are distribution artifacts, not active-document names.
7. The mockup is executable documentation, not higher authority. Core Governance and the active Framework remain normative. Any mockup/rule mismatch is Framework distribution drift and blocks release readiness until repaired.

## Bootstrap Behavior

For GREENFIELD creation after Preview → explicit user approval:

```text
read canonical repo
→ read SKILL + Core Governance + Framework/skeleton templates
→ read project-source-mockup/README.md
→ create 00 first
→ create mandatory 01–05 and 09–17
→ evaluate 06–08 and create only if applicable
→ keep 18–19 reserved
→ create 20–99 only for real project needs
→ validate Index / Manifest / readiness
```

The mockup templates contain placeholders only. Agents MUST replace them with verified/user-confirmed project facts or explicit epistemic states; they MUST NOT promote placeholder text as truth.

## Compatibility and Migration

Project Source Framework version changes from `1.1.1` to `1.1.2`; Project Source Schema remains `1.0.0`. This is a backward-compatible bootstrap/documentation clarification and does not add a mandatory document type beyond the namespace already defined by Core Governance.

Existing Projects remain pinned to their locally approved Framework/Schema versions and do not auto-upgrade. Adoption of 1.1.2 by an existing Project uses the governed `MIG-*` flow when an upgrade is desired.

## Non-Goals

This amendment does not add an executable generator, CLI, validator, migration engine, background automation, or live dependency on the upstream repository. New projects bootstrap from the repository, then pin their imported Framework/Schema locally.

## Precedence

For bootstrap mockup structure and slot/document discoverability, this 1.1.2 amendment is the latest binding clarification. The 1.1.1 materialized-current-state amendment remains binding for Current Truth, Stable-ID resolution, Manifest/CURRENT completeness, and archive independence.
