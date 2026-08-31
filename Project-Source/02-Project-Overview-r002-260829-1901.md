---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-OVERVIEW-001"
document_type: "PROJECT_OVERVIEW"
semantic_slot: "02"
revision: 2
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-08-29T19:01:09+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "USER_CONFIRMED"
freshness_class: "STABLE"
project_source_framework_version: "1.7.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 02 — Project Overview

## Project Identity

- Project Name: `ProjectFramework`
- Project ID: `PROJECTFRAMEWORK`
- Project UUID: `00575e76-17ce-4dd3-ad24-377494a4a45b` (immutable)

## Purpose / Objective

Develop and maintain ProjectFramework as a vendor-neutral, documentation-first governance framework that helps Humans and AI Agents create, manage, develop, verify, migrate, release, and hand off Projects with explicit source of truth, authority, continuity, and verification boundaries.

## In Scope

- ProjectFramework governance and Framework distribution development.
- Framework roadmap and task lifecycle in `docs/superpowers/PROJECT-TASKS.md`.
- Framework release, migration, verification, documentation, and repository integration work.
- This repository's own Project governance through `Project-Source/`.

## Out of Scope

- Treating the reusable Framework distribution as this Project's own Project Source.
- Automatically governing or mutating external consuming Projects.
- Runtime/application automation not separately authorized by an applicable Task/design.

## Stakeholders / Systems

- Project owner/user: approval authority under Framework rules.
- AI Agents working on the repository: governed execution/review participants; capability does not grant authority.
- GitHub repository: `captainhuke-dev/ProjectFramework`.
- Windows local workspace: `E:\GitHub\ProjectFramework`.

## Known Constraints

- ProjectFramework local Project Source Framework pin: `1.7.0`; Schema: `1.0.0`.
- Canonical reusable upstream distribution currently reports Framework `1.8.0` / Schema `1.0.0`.
- Initialized Project does not auto-upgrade merely because upstream Framework advances.
- `commit ≠ push`.
- Google Drive and generic external File Storage are `NOT_APPLICABLE` at initialization.

## Current High-Level Context

The repository contains the reusable Framework distribution under `Framework-Source/` and development records under `docs/superpowers/`. The authoritative `Project-Source/` governs ProjectFramework itself and remains locally pinned to Framework 1.7.0 until a separately governed Project upgrade changes that pin.

## Authoritative External Sources

- Canonical repository: `https://github.com/captainhuke-dev/ProjectFramework`.
- No external file-storage authority is applicable.

## Project Lineage

`Project-Source/` was initialized on 2026-08-29 for an existing repository. Historical repository/task history predates this Project Source and remains in Git/source-native records; initialization does not fabricate retroactive `DEC-*`, `REQ-*`, or other governance records.

## Project-Specific Terminology

- **Framework Source / Framework distribution:** reusable ProjectFramework package at `Framework-Source/`; the historical pre-1.8.0 directory name was `managing-project-source/`.
- **Project Source:** authoritative governance/current truth for this Project at `Project-Source/`.
- **Framework upstream release:** current reusable distribution release, presently `1.8.0`.
- **Project Source Framework pin:** Framework revision governing this initialized Project, presently `1.7.0`.
