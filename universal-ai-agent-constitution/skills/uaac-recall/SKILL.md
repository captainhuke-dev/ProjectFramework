---
name: uaac-recall
description: Recover current source and procedure without conversation memory
metadata:
  constitution_id: UAAC-001
  constitution_version: 4.2.0
  function: RECALL
  source_laws:
  - CONST-005
  - CONST-008
  - CONST-009
  - CONST-023
  - CONST-024
  authority_effect: NONE
  volatile_truth_embedded: false
---

# uaac-recall

1. State the exact uncertainty.
2. Query the Project LLM Wiki for routing.
3. Resolve State Authority Map, Project Document Registry, Project Continuation Index/current lineage, and canonical source.
4. Fresh-read the required source; summaries and memory are routing aids only.
5. Resolve the current registered procedure and verify freshness.
6. Preserve UNKNOWN or CONFLICTED when resolution fails.
