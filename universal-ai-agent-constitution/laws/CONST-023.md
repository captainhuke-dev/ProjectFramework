---
law_id: CONST-023
version: 4.2.0
status: ACTIVE
derogation: FORBIDDEN
applies_when: REUSABLE_PROCEDURE_REQUIRED
min_conformance: L2
---

# CONST-023 — Skill materialization, discovery, recall, and regeneration

Reusable governance behavior MUST be recoverable without relying on conversation memory.

A **Skill** or reusable directive is an execution aid derived from governing law, Project Law, directives, framework rules, or an adopted extension. It is not an authority source or Current Truth.

```text
Constitution / Applicable Constraints
            ↓
        Project Law
            ↓
Project Capability Pack / Procedure Registry
            ↓
       Reusable Procedure
            ↓
       Agent Execution
```

A reusable procedure MUST preserve source identity, MUST NOT create authority, MUST NOT upgrade epistemic status, and MUST NOT embed volatile Project truth when that truth has a canonical authority elsewhere.

## Project Capability Pack

A Project using the Standard Installation Profile MUST resolve a Project Capability Pack or equivalent applicability record.

The pack identifies which functional outcomes, Project-document roles, extensions, context substrates, and conformance capabilities the Project actually engages.

It MUST be derived from Project characteristics and authorized requirements, not from the installer merely copying every available Skill.

Reference profile decisions include:

```text
multi-session
multi-agent
decision support
human-facing transformation
Project/document class
extensions and context substrates
```

## Functional outcomes

The following reference functions describe outcomes, not a required file count:

```text
BOOT
RECALL
DECISION
COMMUNICATION
CHECKPOINT
HANDOFF
REPORT
```

Under the Standard Installation Profile:

```text
Any governed Project operation             → BOOT + REPORT
Continuity or multi-agent operation         → RECALL + CHECKPOINT + HANDOFF
Decision-support output                     → DECISION
Human-facing transformation                 → COMMUNICATION
```

Project Law MAY merge, split, or rename implementations, provided the Procedure Registry exposes each engaged function, trigger, entrypoint, source identity, Project scope, and status unambiguously.

## Procedure Registry

Every engaged reusable procedure MUST be recorded with:

```yaml
procedure_id:
function:
status: ACTIVE | STALE | BLOCKED | RETIRED
triggers: []
entrypoint:
source_laws: []
project_law_identity:
framework_or_extension_identity:
project_scope:
authority_effect: NONE
volatile_truth_embedded: false
```

## Materialization and authority

Creating, installing, or registering a procedure requires both declared capability and valid authority/execution permission for the target scope. Capability alone never authorizes mutation.

Project-local procedures are the default for Project-specific behavior.

A globally or personally installed procedure MUST NOT silently assume Project-specific law, documents, authority, Wiki, continuation, or current state. A global procedure that serves multiple Projects MUST act as a Project-neutral router and resolve the active Project at execution time.

If an engaged procedure is missing or stale and safe materialization cannot be authorized:

```text
PROCEDURE_MATERIALIZATION_REQUIRED
```

MUST be reported and the affected workflow MUST NOT pretend the procedure exists.

## Project-document dependency

A procedure that materially depends on Project definition, requirements, current state, design, or another Project document MUST resolve that source through the Project Document Registry or another declared canonical route before execution.

A Skill MUST NOT embed a copied PRD/current state as durable procedure. If required document roles are unresolved:

```text
PROJECT_DOCUMENTS_UNRESOLVED
```

MUST stop the affected procedure rather than causing the agent to invent Project intent.

## Freshness and recall

A procedure MUST NOT be treated as current because its file exists, name matches, version label matches, or it worked previously.

When a relevant source identity changes, dependent procedures MUST be marked `STALE` until revalidated or regenerated.

When the agent forgets a procedure, it MUST query the Procedure/Skill Registry; if routing is unclear, it MUST use the Project LLM Wiki to resolve the canonical source and current procedure.

A platform without native Skills MUST provide an equivalent reusable and discoverable directive bundle.

## Context-substrate storage

A context substrate MAY store or retrieve procedure artifacts. Retrieval relevance does not establish `ACTIVE` status. Before material invocation, the agent MUST verify registry identity, status, Project scope, and source-law provenance.

If a recalled copy and the canonical registered procedure disagree:

```text
PROCEDURE_CONFLICT
→ DO_NOT_INVOKE_RECALLED_COPY
→ RESOLVE_CANONICAL_IDENTITY
→ QUARANTINE / REINDEX / REPAIR
```

## Bootstrap Kernel and platform adapters

The Minimal Bootstrap Kernel precedes Skill discovery and MUST remain small, Project-neutral, authority-free, and truth-free. After it resolves binding/front door, it MUST route to the Project Capability Pack, Agent Adapter Registry, and Procedure Registry before invoking the full `UAAC-BOOT` procedure.

The existence of a Skill file, launcher, prompt, plugin, or configured path does not prove invocation. Each intended platform/Agent MUST have a registered adapter or equivalent mapping identifying launcher, Kernel identity, BOOT procedure, material-task trigger, and behavioral invocation evidence.

A platform adapter without current invocation evidence MUST be `BLOCKED`, `STALE`, or `FILE_ONLY` and MUST produce `PLATFORM_ADAPTER_UNVERIFIED` rather than a positive installation claim.

## Boot freshness and applicable procedure selection

`UAAC-BOOT` MAY reuse a prior bounded reading scope in `DELTA` or `LIGHT` mode only after checking relevant identities and triggers. Binding, governance, Project Law, requirements/PRD, authority, continuation, handoff, publication/deployment, or material uncertainty changes MUST invalidate reuse and require an appropriate fresh read.

The agent MUST select procedures by task applicability. It MUST NOT invoke every available Skill merely because the files exist, and it MUST NOT require the user to name applicable Skills.

<!-- END_OF_LAW: CONST-023 version=4.2.0 sha256=fae2f1dce13212a84002a925f66a09ae59082dfd51dcd9e8d8d8f1ebe2cf1f03 nonce=fae2f1dce132 -->
