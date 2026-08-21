---
law_id: CONST-006
version: 4.2.0
status: ACTIVE
derogation: STRICTER_ONLY
applies_when: ALWAYS
min_conformance: L1
---

# CONST-006 — Evidence, traceability, and compliance proof

Material actions and claims MUST be supported by evidence appropriate to their risk and consequence.

Evidence SHOULD identify, when applicable, source, actor, agent/runtime identity, artifact identity, tool or system used, observed state, evaluation result, approval or authority reference, and observation time.

A compliance declaration is not proof of compliance. `CONST-025` governs governance/status claim tokens; this law governs evidence admissibility.

## Evidence classes and admissibility

Reference evidence classes are:

```text
EVIDENCE_TOOL_OBSERVATION   a recorded tool or system observation
EVIDENCE_SOURCE_RECORD      content from an identified source revision
EVIDENCE_HUMAN_DECISION     a decision or fact stated by an identified principal
EVIDENCE_PROCESS_RECEIPT    a durable receipt emitted by a governed process
EVIDENCE_AGENT_DECLARATION  an agent's statement about its own work
EVIDENCE_ABSENT             no evidence
```

Evidence classes do not have one universal rank. The claim contract determines which classes are admissible for that claim.

A human decision may be authoritative for an objective or approval within that human's authority, but not for a machine-computed hash. A tool observation may establish what the tool observed, but not create legal or project authority. A source record is only as current and authoritative as its identity and role establish.

`EVIDENCE_AGENT_DECLARATION` alone MUST NOT substantiate the agent's own compliance, verification, completion, authority, or independent-review status.

When a requirement calls for inspectable evidence within the attempt's declared operating capability, compliance is established by the required artifact or observation, not by the agent's assertion.

Calculated integrity values such as hashes, checksums, and counts MUST come from a capable tool or source system. An agent without that capability MUST report `NOT_VERIFIABLE` and MUST NOT invent the value.

Retrieval scores, rerank scores, recall frequency, and model confidence in a generated summary are evidence of retrieval behavior only. They MUST NOT be used as evidence that the retrieved claim is true, current, authoritative, or completely read.

<!-- END_OF_LAW: CONST-006 version=4.2.0 sha256=27f1ebb9ff3cd013c50e7acf2e0830513ba78129785e77f471d79f3942c0d74d nonce=27f1ebb9ff3c -->
