---
law_id: CONST-004
version: 4.2.0
status: ACTIVE
derogation: STRICTER_ONLY
applies_when: ALWAYS
min_conformance: L1
---

# CONST-004 — Agent and entity identity

An entity is anything that can initiate, approve, prepare, execute, observe, or materially influence a governed action.

Projects define the entity classes that exist in their scope.

An entity without a stable, verifiable identity MUST NOT hold or receive governed authority.

This is written as a prohibition rather than as a permission because the permissive form, "only an entity with an identity may hold authority", reads as a grant to everything that has one.

An AI agent performing material work MUST declare enough identity to make its actions attributable.

Where available, identity SHOULD include agent type, model, model version, runtime, instance ID, capability profile, and limitations.

A new session or runtime instance MUST NOT be assumed to share memory, state, authority, workspace, or history with another instance.

<!-- END_OF_LAW: CONST-004 version=4.2.0 sha256=5ce6c4a65a537df2f1ed4a85a822d622ea34d369dbbd4aa32d020fc31c42afe3 nonce=5ce6c4a65a53 -->
