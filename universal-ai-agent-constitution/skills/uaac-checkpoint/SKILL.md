---
name: uaac-checkpoint
description: Write durable continuation state and update the pointer
metadata:
  constitution_id: UAAC-001
  constitution_version: 4.2.0
  function: CHECKPOINT
  source_laws:
  - CONST-014
  - CONST-016
  - CONST-019
  - CONST-025
  authority_effect: NONE
  volatile_truth_embedded: false
---

# uaac-checkpoint

1. Read State Authority Map, Project Continuation Index, and current lineage pointer.
2. Write checkpoint with lineage, governance identity, state, artifacts, uncertainty, blocker, and exact next action.
3. Create a new lineage-pointer epoch linked to predecessor and update the Project Continuation Index using its precondition.
4. Detect competing pointer updates; do not last-write-wins reconcile.
5. Never store secrets or private chain-of-thought.
