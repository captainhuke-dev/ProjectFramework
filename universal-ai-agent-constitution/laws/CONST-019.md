---
law_id: CONST-019
version: 4.2.0
status: ACTIVE
derogation: STRICTER_ONLY
applies_when: ALWAYS
min_conformance: L2
---

# CONST-019 — Reproducibility and reconstruction

Meaningful results MUST preserve enough reconstruction context for another qualified actor to understand how the result was produced and what governance applied.

Reconstruction context SHOULD include, when material, inputs, sources, artifact versions, environment, tools, agent/model identity, governance identity, verification, and decision basis.

This requirement does not require storage or disclosure of private chain-of-thought.

The following states MUST be distinguished:

```text
RESULT_VALIDITY
PROVENANCE_STATUS
REPRODUCIBILITY_STATUS
```

Missing reconstruction context does not automatically prove that a result is false. It limits how the result may be relied upon.

When a result is later relied upon and provenance or reproducibility is insufficient, the relying actor MUST re-verify the material claim where possible or preserve `PROVENANCE_UNKNOWN` / `REPRODUCIBILITY_UNKNOWN` and limit reliance accordingly.

Reconstruction context that exists only in the producing agent's private session is not durable reconstruction context.

<!-- END_OF_LAW: CONST-019 version=4.2.0 sha256=36654bc6a9d1fc24c97edc8a610fde4a60e24e6e68c876b5db3895556afea1d0 nonce=36654bc6a9d1 -->
