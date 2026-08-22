---
law_id: CONST-017
version: 4.2.0
status: ACTIVE
derogation: FORBIDDEN
applies_when: ALWAYS
min_conformance: L1
---

# CONST-017 — Result states, completion, and failure reporting

Completion language MUST distinguish materially different states.

Reference progression:

```text
EXECUTED
VERIFIED
ACCEPTED
PUBLISHED
DEPLOYED
OPERATIONALLY_VERIFIED
CLOSED
```

No agent may use unqualified `DONE`, `COMPLETE`, or `FINISHED` to imply states that have not been established.

```text
Executed != Verified
Verified != Accepted
Accepted != Published
Published != Deployed
Deployed != Operationally Verified
Operationally Verified != Closed
```

Each governance/status state used to control work MUST have a claim contract under `CONST-025` that identifies the substantiating artifact and safe fallback.

Failure is a first-class result. Reference outcome/continuation states include:

```text
SUCCESS
FAILED
BLOCKED
INTERRUPTED
CANCELLED
ABANDONED
SUPERSEDED
```

A failed, blocked, interrupted, cancelled, abandoned, superseded, or closed task MUST NOT disappear when it materially affects future work. Project Law MUST define terminal accounting for work it starts durably.

A result record SHOULD distinguish result validity, verification state, publication/deployment state, closure state, known limitations, and exact next action.

## Installation and adoption states

A standard Project installation MUST distinguish at least:

```text
STAGED
CORE_INSTALLED
PROJECT_PROFILE_RESOLVED
PROJECT_DOCUMENTS_RESOLVED
SKILLS_MATERIALIZED
AGENT_ENTRYPOINTS_CONFIGURED
INSTALLATION_VALIDATED
EFFECTIVE
```

Copying constitutional files establishes neither `INSTALLATION_VALIDATED` nor `EFFECTIVE`.

`INSTALLATION_VALIDATED` means the registered installation checks and required cross-agent/access tests produced valid evidence. `EFFECTIVE` means the competent Project authority accepted the validated adoption. They are separate claim tokens with separate evidence and safe fallbacks.

A Project MAY expose more detailed internal lifecycle states, but MUST NOT collapse installation, validation, and effective adoption into one unqualified completion word.

<!-- END_OF_LAW: CONST-017 version=4.2.0 sha256=549a545406c4fd5d1211ea8c0ac06ed5bcb34abacd7420b0a378f045c79ad36c nonce=549a545406c4 -->
