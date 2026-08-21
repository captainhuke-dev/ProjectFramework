---
law_id: CONST-008
version: 4.2.0
status: ACTIVE
derogation: FORBIDDEN
applies_when: ALWAYS
min_conformance: L1
---

# CONST-008 — Comprehension integrity and complete reading

Access is not knowledge. Discovery is not reading. Partial reading is not complete reading.

Required coverage states:

```text
DISCOVERED
COVERAGE_PARTIAL
COVERAGE_COMPLETE
COVERAGE_UNKNOWN
READ_VERIFIED
APPLIED
```

`COVERAGE_UNKNOWN` is treated as `COVERAGE_PARTIAL`.

Search results, snippets, summaries, first chunks, truncated output, remembered content, titles, and tables of contents MUST NOT establish complete coverage.

An AI agent MUST NOT issue a conclusion, recommendation, mutation, approval, or governance-dependent result that materially depends on a required source unless that source has complete required coverage.

Project mechanisms MAY use section manifests, end markers, nonces, tool-based hashes, or other inspectable methods to establish coverage.

A read receipt written by the same agent is a declaration unless supported by the required evidence.

Read completeness MUST be scoped to applicable law and sources. The Constitution does not require reading unrelated material.

## Bounded reading scope

The mandatory reading scope MUST be bounded and declared before the reading starts. `LAW-MANIFEST.yaml` supplies the constitutional part of that scope per conformance level; Project Law supplies the rest.

Unbounded reading is a failure of the same kind as partial reading, and it arrives at the same place. An agent that reads everything it can reach exhausts its working context and truncates, which is the condition this law exists to prevent. An agent that tries hardest to comply walks into it.

An agent that finds the declared scope insufficient MUST stop and re-declare rather than continue reading without limit.

A coverage claim is a claim token and is governed by `CONST-025`.


## Derived-summary coverage

A generated abstract, overview, index preview, retrieval snippet, compressed session summary, or other derived representation MAY establish relevance and routing. It MUST NOT establish `COVERAGE_COMPLETE` for a governed source whose full content is required.

Where a context system exposes progressive layers, only the layer that contains the required full source content, or a fresh read of the canonical source itself, MAY satisfy complete-reading requirements.

Known stale, sampled, partial, pending, or asynchronously generated summaries MUST be treated as partial routing aids rather than complete source coverage.

<!-- END_OF_LAW: CONST-008 version=4.2.0 sha256=5fb97a3b38a5db467453ae662c0241c98dd764858ffb48b3e67a1b4cecd6e17b nonce=5fb97a3b38a5 -->
