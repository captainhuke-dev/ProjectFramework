---
law_id: CONST-021
version: 4.2.0
status: ACTIVE
derogation: FORBIDDEN
applies_when: ALWAYS
min_conformance: L1
---

# CONST-021 — Project adoption, pinning, and local Project Law

A Project adopts this Constitution explicitly and MUST record a pinned constitutional identity appropriate to the source system.

A Project MUST NOT depend on a mutable upstream branch as its effective constitutional identity.

The adoption record MUST identify at least:

```text
Project boundary
constitutional identity and local pinned locator
Project Law
verified applicable-constraint register
materiality policy
authorized instruction channels
canonical governance source/ref policy
State Authority Map
Project Document Registry
Project Capability Pack / reusable-procedure registry
Current Continuation Index policy
agent conformance records
Project LLM Wiki and fallback route
claim-contract registry
adopted extensions/frameworks/context substrates
installation validation and effective authority reference
escalation policy
system-health feedback policy
```

Project Law MAY add stricter requirements and Project-specific rules. It MUST NOT weaken `FORBIDDEN` constitutional protections.

The Project MUST maintain its own knowledge-navigation surface and a direct fallback route to governance, state authorities, Project documents, continuation, checkpoints, handoffs, and Procedure Registry.

The Project MUST register every external obligation it has verified as applicable. The record MUST distinguish verified applicable constraints, potential constraints awaiting verification, and rejected constraints. Absence from the register does not extinguish a real external obligation; it means the Project has not yet established applicability for governed operation.

The Project MUST declare materiality, authorized channels, state classes and canonical authorities, claim contracts, Project-document roles, procedure applicability, and conformance policy before relying on them.

## Standard Project Installation Profile

The phrase **Install Project Constitution** or an equivalent declared trigger MAY invoke the Standard Project Installation Profile.

The profile is an installation mechanism under this Constitution. It does not make one repository system, path syntax, or tool a universal constitutional dependency. A Project MAY use an equivalent profile if it preserves the same semantics and records the variance.

The standard profile requires:

```text
one effective Project governance front door
pinned/vendored constitutional release
Project Law and applicable constraints
State Authority Map
Project Document Registry
Project Capability Pack and Procedure Registry
Project Continuation Index with lineage pointers
Claim Contract Registry
Project knowledge navigation
configured Agent entrypoints
installation validation evidence
separate effective-adoption authority
```

The standard Project front door is:

```text
governance/UAAC-BOOT.md
```

It is a router with:

```text
authority_effect: NONE
truth_authority: NONE
```

It MUST NOT duplicate law or volatile state as a second authority. One Project governance boundary MUST NOT have more than one effective front door. Multiple active candidates produce `GOVERNANCE_BOOT_CONFLICT`.

The effective governance source/ref policy MUST be explicit. A pending feature-branch or local governance change MUST NOT become effective by observation alone.

## Install, validate, and effective adoption

Installation copies/configures the operating artifacts. Validation proves required locators, schemas, Project-document resolution, procedures, continuation, access, and cross-agent convergence. Effective adoption requires competent Project authority.

```text
INSTALLED != INSTALLATION_VALIDATED != EFFECTIVE
```

A positive installation/effective state MUST use registered claim contracts.

## Project Document Registry

The standard profile MUST resolve semantic document roles rather than require one universal filename.

At minimum:

```text
PROJECT_DEFINITION
REQUIREMENTS
CURRENT_STATE
```

A role MAY map to an existing PRD, specification, research plan, policy charter, state record, or equivalent canonical artifact.

A Brownfield installation MUST inventory and map existing sources before creating replacements. It MUST NOT create a duplicate Project Law, requirements source, PRD, or current-state source merely to satisfy a template.

Unresolved equal-authority sources produce `PROJECT_DOCUMENT_CONFLICT` / `PROJECT_DOCUMENTS_UNRESOLVED` and block affected effective installation.

## Vendoring and upgrade

The standard profile SHOULD vendor the exact constitutional package inside the Project or use an equivalently complete immutable local mechanism. It SHOULD NOT use a partially fetched dependency as the default when intended agents may lack the same content.

An upgrade SHOULD preserve the prior installed release, assess impact, revalidate affected Project Law/documents/procedures/agents, and switch the adoption identity only after authorization.

## Escalation

A Project MUST define escalation for unresolved authority, conflict, potential external obligations, state-authority conflict, Project-document conflict, unavailable procedures, unavailable principals, and unavailable canonical systems.

Reference policy:

```yaml
escalation_policy:
  when_principal_unavailable: BLOCK | CHECKPOINT_AND_STOP | PROCEED_ON_DEFAULTS
  timeout:
  pre_authorized_defaults: []
  never_proceed_on: []
```

`never_proceed_on` MUST include irreversible actions, actions touching secrets, external publication, and R3 actions. Project Law MAY add items and MUST NOT remove this floor.

An agent that stops MUST leave resumable state identifying the missing decision, competent decision owner, affected scope, and exact next action.

## Project boundary and nested Projects

One effective governance front door applies per declared Project boundary, not necessarily per repository. A monorepo MAY contain parent and nested Projects when each boundary has its own verified Project binding.

When validating a parent Project, declared nested Project roots MUST be excluded from the parent's single-front-door search. Multiple effective front doors inside the same Project boundary MUST produce `GOVERNANCE_BOOT_CONFLICT`; a valid nested Project MUST NOT be treated as that conflict.

Filesystem aliases, junctions, symlinks, nested repositories, and worktrees MUST be resolved before mutation so an installer or Agent does not escape or misidentify the authorized Project boundary.

## Minimal Bootstrap Kernel and Auto-Boot

A platform launcher MUST provide a minimal Bootstrap Kernel capable of resolving Project binding and exactly one effective front door before the Skill/Procedure Registry is available. The Kernel is routing logic only; it is not law, authority, Current Truth, or a reusable Skill.

For an `EFFECTIVE` Project, the registered `UAAC-BOOT` procedure MUST be invoked at Project/session entry, resume, and before every material task without requiring the user to repeat UAAC or name a Skill.

A task is material when it changes source/artifacts, commits/pushes/merges, changes Project state or requirements, issues a controlling status claim, checkpoints/handoffs, changes authority, causes an external effect, publishes, deploys, or can materially affect cost/risk. Unknown materiality with a plausible Project-state or external effect MUST be treated as material until resolved.

Auto-Boot MUST perform identity, freshness, applicability, materiality/risk, authority, and bounded-reading checks. It MUST select applicable registered procedures automatically and MUST NOT blindly load every law or Skill on every non-material prompt.

`FULL` boot is required for a new session, changed binding/governance/Project Law/requirements/authority, changed continuation identity, handoff, publish/deploy, or unresolved material uncertainty. `DELTA` or `LIGHT` reuse is allowed only when the relevant identities are proven unchanged.

<!-- END_OF_LAW: CONST-021 version=4.2.0 sha256=a0d3802d0a1bcf24ee80ecf9d8d25e8cb20212506be103eff8653ed968e35421 nonce=a0d3802d0a1b -->
