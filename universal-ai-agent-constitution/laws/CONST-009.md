---
law_id: CONST-009
version: 4.2.0
status: ACTIVE
derogation: STRICTER_ONLY
applies_when: ALWAYS
min_conformance: L2
---

# CONST-009 — Knowledge navigation and LLM Wiki

Every adopting project MUST maintain a knowledge-navigation layer suitable for AI and human recovery. This Constitution refers to that function as the **Project LLM Wiki**.

The Project LLM Wiki is a Navigation Layer, Recovery Layer, and Knowledge Index. It is not, by itself, an Authority Layer, Truth Layer, or Decision Layer.

When uncertain, forgetful, conflicted, or unable to identify the correct source, an agent MUST formulate the uncertainty and consult the Project LLM Wiki before guessing.

Recovery flow:

```text
UNCERTAINTY_DETECTED
        ↓
STATE_EXACT_UNCERTAINTY
        ↓
QUERY_PROJECT_LLM_WIKI
        ↓
FOLLOW_CANONICAL_SOURCE
        ↓
FRESH_READ
        ↓
RESOLVE_OR_PRESERVE_UNKNOWN
```

Every entry MUST carry a source. An entry with no source is an assumption and MUST be labelled `ASSUMED` under `CONST-005`.

A stale Wiki entry MUST NOT silently override fresher canonical state.

## Method reference

A project MAY follow any published methodology for designing an LLM-oriented Wiki. This Constitution names none, and the normative text carries no external locator: a locator in a law body is a dependency on a surface that can change underneath every project that adopted the law, which `CONST-016` forbids elsewhere in this same document. Method references belong in the non-normative profiles, pinned to an immutable identity.

A method reference is read once when the Wiki is designed. It MUST NOT be the destination for an agent asking what the current project state is. A rule that directs an uncertain agent to a document that cannot contain the answer costs the context the agent needed and returns nothing.

Projects MUST maintain their own Project LLM Wiki location in their adoption record.


A Project MAY implement or accelerate its LLM Wiki with a context substrate, semantic index, vector store, memory system, or other retrieval mechanism. Doing so does not change the Wiki's constitutional role: it remains navigation to canonical sources, not a replacement for them.

If the navigation substrate is unavailable, the Project SHOULD retain a human-readable or otherwise directly discoverable fallback route to constitutional adoption, Project Law, current state, checkpoints, handoffs, and Skill Registry sufficient for governed recovery.

<!-- END_OF_LAW: CONST-009 version=4.2.0 sha256=35ff09997e44e62527aa582683b183ff288ae9aa2680beafff26b7ed98019a7a nonce=35ff09997e44 -->
