---
name: uaac-handoff
description: Transfer verified state and obtain receiver acceptance
metadata:
  constitution_id: UAAC-001
  constitution_version: 4.2.0
  function: HANDOFF
  source_laws:
  - CONST-002
  - CONST-003
  - CONST-014
  - CONST-015
  - CONST-016
  - CONST-017
  - CONST-025
  authority_effect: NONE
  volatile_truth_embedded: false
---

# uaac-handoff

Sender:
1. Checkpoint and update the lineage pointer plus Project Continuation Index.
2. Produce handoff packet with state/document authorities, Capability Pack/procedures, Continuation Index/lineage pointer, artifacts, verification, uncertainty, and exact next action.
Receiver:
3. Verify Project boundary, State Authority Map, Project documents, Capability Pack/Procedure Registry, Continuation Index/lineage pointer, context binding, artifact identity, and current state.
4. Resolve authority independently.
5. Issue receiver receipt or HANDOFF_UNVERIFIED/HANDOFF_INVALID with evidence.
