---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-OVERVIEW-001"
document_type: "PROJECT_OVERVIEW"
semantic_slot: "02"
revision: 7
document_status: "ACTIVE"
supersedes: "02-Project-Overview-r006-260916-1332.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-16T14:15:47.931+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "USER_CONFIRMED"
freshness_class: "STABLE"
project_source_framework_version: "1.19.0"
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
- Windows local workspace binding: `E:\GitHub\ProjectFramework` (routing binding only; current branch/worktree is dynamic and must be freshly observed when material).

## Known Constraints

- ProjectFramework canonical self-host Project Source Framework pin: `1.19.0`; Schema: `1.0.0`.
- Canonical reusable Framework distribution: Framework `1.19.0` / Schema `1.0.0` / release format `3`.
- Initialized Project does not auto-upgrade merely because upstream Framework advances after this pin.
- `commit ≠ push ≠ merge ≠ release ≠ deployment`.
- Google Drive and generic external File Storage are `NOT_APPLICABLE` for this Project.
- ProjectFramework is documentation/governance first; this Project Source does not imply an application runtime.

## Current High-Level Context

The repository contains the reusable Framework distribution under `Framework-Source/` and development records under `docs/superpowers/`. The authoritative `Project-Source/` governs ProjectFramework itself and is self-host reconciled to Framework `1.19.0` through `MIG-005`. Framework distribution truth and Project-local governance truth remain separate authorities even when canonical self-hosting requires their release identity to converge.

## Authoritative External Sources

- Canonical repository: `https://github.com/captainhuke-dev/ProjectFramework`.
- No external file-storage authority is applicable.

## Project Lineage

`Project-Source/` was initialized on 2026-08-29 for an existing repository. Historical repository/task history predates this Project Source and remains in Git/source-native records; initialization and upgrade do not fabricate retroactive `DEC-*`, `REQ-*`, or other governance records. `MIG-002` preserves predecessor Project Source revisions under `Project-Source/archive/`.

## Project-Specific Terminology

- **Framework Source / Framework distribution:** reusable ProjectFramework package at `Framework-Source/`; historical pre-1.8.0 directory name was `managing-project-source/`.
- **Project Source:** authoritative governance/current truth for this Project at `Project-Source/`.
- **Framework upstream release:** verified reusable distribution release, currently `1.19.0` with TASK-057 AI-ControlTower Governance Support Layer layered on TASK-051/TASK-052 and TASK-049 canonical self-hosting.
- **Project Source Framework pin:** Framework revision governing this canonical self-host Project, currently `1.19.0`.
