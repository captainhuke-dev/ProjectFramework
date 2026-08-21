# Changelog

## 4.2.0

- Separated the HUMAN walkthrough from the canonical Agent installation protocol.
- Added a Minimal Bootstrap Kernel before Skill discovery and full `UAAC-BOOT`.
- Added Project Binding, Boot Receipt, Agent Adapter Registry, material-task floor, freshness modes, attempt preconditions, pre-write recheck, and visibility states.
- Added nested-Project boundary semantics and receiver-visible canonical-surface requirements.
- Added atomic publication/base-freshness contracts and `S-INSTALL-14` through `S-INSTALL-23`.
- Preserved stable law IDs `CONST-001` through `CONST-025`.

## 4.1.0

- Defined **Install Project Constitution / ติดตั้งรัฐธรรมนูญ Project** as protocol `UAAC-INSTALL-001` rather than a copy operation.
- Added one standard Project front door at `governance/UAAC-BOOT.md` with no truth or authority effect.
- Added byte-identical shared boot contracts for ChatGPT, Codex/AGENTS, and generic Agent wrappers.
- Added Project Document Registry with semantic roles for Project Definition, Requirements/PRD, and Current State.
- Added Project Capability Pack and applicability-driven constitutional procedures.
- Replaced a single global continuation pointer with a Project Continuation Index and lineage-local pointers.
- Added terminal lineage retention and conflict-controlled continuation updates.
- Added cross-agent bootstrap convergence and interrupted-work recovery as installation acceptance criteria.
- Added Greenfield/Brownfield installation runbook, threat model, templates, schemas, installed-project fixture, and installation validator.
- Added 12 `S-INSTALL-*` conformance scenarios.
- Hardened installation validation against path traversal, duplicate lineages, failed static checks, unrun convergence, and mismatched effective authority receipts.
- Hardened installation templates to fail-safe defaults and blocked unresolved placeholders from substantiating positive installation/adoption claims.
- Removed machine-local path leakage from structural validation receipts; installed fixture locators are package-relative and portable.
- Modularized the Constitution entrypoint, conformance scenarios, and MUST coverage artifacts so canonical law text is not duplicated and agents can load only applicable sections.
- Preserved all 25 stable law IDs.

## 4.0.0

- Applied Systems Thinking to actor incentives, state flows, feedback loops, recurring failure archetypes, and unintended consequences.
- Replaced single Project state location with State Authority Map and Current Continuation Pointer.
- Added potential/applicable/rejected external-constraint lifecycle.
- Reworked claim substantiation into Claim Contract Registry with explicit safe fallbacks.
- Split proven capability, task-required level, and attempt operating level.
- Replaced fixed seven-Skill file obligation with conditional functional outcomes while shipping seven reference Skills.
- Added schemas, templates, examples, validators, release receipt, and systems-health metrics.
