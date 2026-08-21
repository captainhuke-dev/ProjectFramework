# Conformance Scenarios — Universal AI Agent Constitution v4.2.0

```yaml
document_type: CONFORMANCE_TESTS
constitution_id: UAAC-001
constitution_version: "4.2.0"
scenario_count: 142
merged_from:
  - CONSTITUTION-001 v0.2.0 suite (70 scenarios)
  - UAAC-001 v2.2 suite (33 scenarios, 22 unique after dedup)
  - v3.0 merge additions (10 scenarios)
  - v4.0/v4.1 systems and installation additions
  - v4.2 installation-hardening additions (`S-INSTALL-14` ... `S-INSTALL-23`)
baseline_run: NOT_RUN
```

## What these are for

A law nobody can test is a suggestion. Each scenario below is written so that a
non-compliant agent visibly loses.

Which requirement each scenario covers is recorded in
`registers/must-coverage-index.md`, together with the requirements covered by an
inspection instead, and the ones covered by nothing behavioural at all —
`registers/verification-gap-register.md` says why for each of those.

## Format

```text
Prompt        what is given to the agent under test
Temptation    the shortcut the prompt is built to invite
Pass          the observable behaviour that satisfies the law
Fail          the observable behaviour that does not
Direction     where a scenario has two arms: what must change, and what must not
```

A scenario that only tests one direction can be passed by an agent that refuses
everything. Where a law can fail in both directions, the scenario has two arms.

## Running them

Run each scenario against each agent actually used, one variable at a time, and
record the result. Results establish which conformance level (CONST-011) an
agent can honestly declare. Until the run exists, `baseline_run: NOT_RUN` stays
in the header above, and no claim about the strength of this Constitution is
supported by evidence (CONST-006 and CONST-025).

---

## Scenario modules

- [`CONST-001 — Scope, constitutional position, and applicable constraints`](scenarios/001-const-001-scope-constitutional-position-and-applicable-constraints.md)
- [`CONST-021 / CONST-002 — Project boundary and adoption record`](scenarios/002-const-021-const-002-project-boundary-and-adoption-record.md)
- [`CONST-002 and CONST-003 — Identity, authority, delegation, accountability`](scenarios/003-const-002-and-const-003-identity-authority-delegation-accountability.md)
- [`CONST-003 — Approval and accountability`](scenarios/004-const-003-approval-and-accountability.md)
- [`CONST-004 — Agent and entity identity`](scenarios/005-const-004-agent-and-entity-identity.md)
- [`CONST-020 — Runtime independence and adopted mechanisms`](scenarios/006-const-020-runtime-independence-and-adopted-mechanisms.md)
- [`CONST-005 — Truth, memory, and conflict`](scenarios/007-const-005-truth-memory-and-conflict.md)
- [`CONST-005 — Epistemic status`](scenarios/008-const-005-epistemic-status.md)
- [`CONST-006 — Evidence and verification`](scenarios/009-const-006-evidence-and-verification.md)
- [`CONST-025 — Substantiation of claims`](scenarios/010-const-025-substantiation-of-claims.md)
- [`CONST-010 — Risk, autonomy and required authority`](scenarios/011-const-010-risk-autonomy-and-required-authority.md)
- [`CONST-007 — Instruction authority and input trust`](scenarios/012-const-007-instruction-authority-and-input-trust.md)
- [`CONST-008 — Comprehension integrity`](scenarios/013-const-008-comprehension-integrity.md)
- [`CONST-015 — Agent-to-agent state transfer`](scenarios/014-const-015-agent-to-agent-state-transfer.md)
- [`CONST-009 — Knowledge navigation and LLM Wiki`](scenarios/015-const-009-knowledge-navigation-and-llm-wiki.md)
- [`CONST-012 — Decision integrity`](scenarios/016-const-012-decision-integrity.md)
- [`CONST-013 — Communication integrity and abridgment`](scenarios/017-const-013-communication-integrity-and-abridgment.md)
- [`CONST-018 — Non-compliance and fail-closed behavior`](scenarios/018-const-018-non-compliance-and-fail-closed-behavior.md)
- [`CONST-021 — Escalation and absent authority`](scenarios/019-const-021-escalation-and-absent-authority.md)
- [`CONST-011 — Capability declaration and conformance level`](scenarios/020-const-011-capability-declaration-and-conformance-level.md)
- [`CONST-016 — Artifact identity and governed dependencies`](scenarios/021-const-016-artifact-identity-and-governed-dependencies.md)
- [`CONST-021 and CONST-022 — Adoption, amendment, canonical source`](scenarios/022-const-021-and-const-022-adoption-amendment-canonical-source.md)
- [`CONST-017 — Result states, completion, and failure reporting`](scenarios/023-const-017-result-states-completion-and-failure-reporting.md)
- [`CONST-019 — Reproducibility and reconstruction`](scenarios/024-const-019-reproducibility-and-reconstruction.md)
- [`CONST-023 — Skill materialization, discovery, recall, and regeneration`](scenarios/025-const-023-skill-materialization-discovery-recall-and-regeneration.md)
- [`CONST-024 — Context substrate, retrieval, memory, and derived-context integrity`](scenarios/026-const-024-context-substrate-retrieval-memory-and-derived-context-integ.md)
- [`Substrate profile scenarios (non-normative, profile-specific)`](scenarios/027-substrate-profile-scenarios-non-normative-profile-specific.md)
- [`Retired scenario IDs from the v2.2 suite`](scenarios/028-retired-scenario-ids-from-the-v2-2-suite.md)
- [`UAAC v4 Systems and Integrity Scenarios`](scenarios/029-uaac-v4-systems-and-integrity-scenarios.md)
- [`Standard Project Installation Profile`](scenarios/030-standard-project-installation-profile.md)

<!-- END_OF_DOCUMENT: Conformance Scenarios v4.2.0 -->
