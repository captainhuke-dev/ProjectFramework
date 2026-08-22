---
document_type: UAAC_PROJECT_INSTALL_PROTOCOL
protocol_id: UAAC-INSTALL-001
protocol_version: '2.0'
constitution_release: 4.2.0
agent_execution: EXECUTE_WHEN_AUTHORIZED
authority_effect: NONE
truth_authority: NONE
standard_front_door: governance/UAAC-BOOT.md
---

# ติดตั้งรัฐธรรมนูญ Project — Canonical Agent Protocol

เอกสารนี้เป็น canonical procedure สำหรับคำสั่ง **“ติดตั้งรัฐธรรมนูญ Project”** Agent ต้องใช้ exact release identity ของเอกสารนี้และ package ที่เกี่ยวข้อง ห้ามตีความ tutorial, chat summary, README example หรือ remembered procedure เป็น protocol แทน

## Success contract

```text
COPIED ≠ CORE_INSTALLED ≠ INSTALLATION_VALIDATED ≠ EFFECTIVE
```

การติดตั้งสำเร็จเชิงเทคนิคเมื่อ package/Project artifacts ตรวจผ่านและ intended agents resolve state ตรงกัน; adoption มีผลเมื่อ Project authority อนุมัติ `EFFECTIVE` แยกต่างหาก

## 0. Resolve authority, target, and immutable source

ก่อน mutation ต้อง resolve:

```text
installer identity/capability/authority
actual Project root and declared boundary
canonical repository/ref policy
expected current base/ref identities
exact UAAC release commit/package/hash
write/commit/push/merge authority
```

Mutable branch URL ใช้ discovery ได้ แต่ effective Constitution ต้อง pin immutable identity หาก Project/root/repository/authority ไม่ชัด ให้หยุด affected action ไม่เดา

## 1. Inventory before mutation

จำแนก `GREENFIELD`, `BROWNFIELD`, หรือ `MONOREPO/NESTED` และ inventory:

- existing Git/nested repos, symlinks/junctions/worktrees
- Project Law/instructions/authority records
- Project definition, PRD/requirements, architecture/current state
- state/evidence/runtime/continuation stores
- platform launchers and existing Skills/procedures
- secrets/private data and external constraints

Brownfield ต้อง map/reconcile source เดิม ห้าม overwrite หรือสร้าง canonical truth ซ้ำเพื่อให้ template ดูครบ

## 2. Stage outside effective governance

ใช้ isolated workspace/adoption branch หรือ equivalent transaction boundary ห้ามวาง payload chunks, self-deleting assembly workflow หรือ partial front door บน effective branch

Vendor exact release side-by-side เช่น:

```text
vendor/uaac/v4.2.0/
```

ห้ามแก้ vendored Constitution เพื่อทำ Project-specific law; เขียนความต่างใน Project Law

## 3. Establish Minimal Bootstrap Kernel and Project Binding

ติดตั้ง launcher/kernel ขนาดเล็กที่ทำได้เพียง:

```text
resolve actual Project root/boundary
resolve PROJECT-BINDING.yaml
resolve exactly one governance/UAAC-BOOT.md for that boundary
compare Project ID/repository/ref/root/front-door identity
route to registries/full UAAC-BOOT
stop on mismatch/unavailability
```

Kernel ไม่ใช่ Skill, law, authority หรือ Current Truth และต้องทำงานก่อน Skill discovery

Project Binding ต้องตรวจ local root/worktree, remote origin/equivalent, Project ID, canonical ref policy และ front door หากไม่ตรง emit `PROJECT_BINDING_MISMATCH`

Nested Project ที่ประกาศ binding ของตนเองถูก exclude จาก parent front-door scan; หนึ่ง effective front door ใช้ต่อหนึ่ง declared Project boundary

## 4. Create/reconcile Project governance

อย่างน้อยต้อง resolve:

```text
governance/BOOTSTRAP-KERNEL.md
governance/PROJECT-BINDING.yaml
governance/UAAC-BOOT.md
governance/CONSTITUTION-ADOPTION.yaml
governance/PROJECT-LAWS/PROJECT_RULES.md
governance/STATE-AUTHORITY-MAP.yaml
governance/PROJECT-DOCUMENT-REGISTRY.yaml
governance/PROJECT-CAPABILITY-PACK.yaml
governance/AGENT-ADAPTER-REGISTRY.yaml
governance/SKILL-REGISTRY.yaml
governance/CLAIM-CONTRACT-REGISTRY.yaml
governance/BOOT-RECEIPT.yaml
governance/CURRENT-CONTINUATION.yaml
governance/INSTALLATION-VALIDATION.yaml
governance/LLM-WIKI/index.md
```

`UAAC-BOOT.md` เป็น router เท่านั้น:

```yaml
authority_effect: NONE
truth_authority: NONE
```

## 5. Resolve Project documents by semantic role

Project Document Registry ต้อง map อย่างน้อย:

```text
PROJECT_DEFINITION
REQUIREMENTS
CURRENT_STATE
```

ใช้ source ที่มีอยู่จริงและ identity/freshness ที่ตรวจได้ ถ้ายังไม่มีข้อมูล ให้คง `BLOCKED` และขอ Project authority ระบุ ไม่แต่ง PRD/intent เพื่อเปลี่ยนสถานะเป็น `RESOLVED`

## 6. Resolve Capability Pack, Skills, and platform adapters

ทุก Project ต้องมี `BOOT` และ `REPORT`; เพิ่มตาม applicability:

- multi-session/multi-agent: `RECALL`, `CHECKPOINT`, `HANDOFF`
- material decision support: `DECISION`
- human-facing transformation: `COMMUNICATION`

Skill เป็น procedure ไม่ใช่ authority/current truth. Global Skill ต้องเป็น Project-neutral router

Agent Adapter Registry ต้อง map intended platform/Agent ไปยัง launcher, Kernel identity, `UAAC-BOOT`, trigger และ behavioral invocation evidence การมีไฟล์/ข้อความอย่างเดียวเป็น `FILE_ONLY` ไม่ใช่ `VERIFIED`

## 7. Enable Auto-Boot with freshness modes

สำหรับ Project ที่ `EFFECTIVE` ทุก material task ต้อง trigger `UAAC-BOOT` โดยไม่ให้ผู้ใช้เตือน UAAC/Skill ซ้ำ

Auto-Boot ต้อง:

1. classify materiality
2. select `FULL|DELTA|LIGHT`
3. check binding/governance/doc/state/adapter identities
4. establish bounded reading scope
5. select applicable registered Skills automatically
6. record Boot receipt and attempt preconditions

ห้าม blind-load ทุก law/Skill ทุก prompt และห้าม reuse prior scope เมื่อ invalidation trigger เปลี่ยน

## 8. Continuation, visibility, and pre-write recheck

ใช้ Project Continuation Index + lineage-local pointer; terminal lineage ต้องยัง reconstruct ได้

Visibility:

```text
LOCAL_ONLY
PENDING_CANONICAL_PUBLICATION
CANONICAL_VISIBLE
REMOTE_STALE
```

ก่อน material write/commit/push/merge/state change/checkpoint/handoff/publish/deploy ให้ compare expected/observed governance, Project Law, continuation predecessor และ artifact base จาก Boot receipt หากเปลี่ยน emit `TASK_CONTEXT_STALE`

Cross-Agent handoff ต้องมี canonical surface ที่ผู้รับอ่านและ verify ได้จริง; local-only state ห้ามอ้างว่า shared

## 9. Configure platform launchers

Launcher ของ ChatGPT/Codex/Claude/Hermes/CLI ต้องใช้ shared Kernel/Boot semantics และชี้กลับ Project front door เดียวกัน เนื้อหา platform-specific ทำได้เฉพาะ access method ห้ามสร้าง Project Law คนละชุด

Ultra-short ChatGPT Project Instructions:

```text
Project นี้ใช้ UAAC: <PROJECT_UAAC_BOOT_URL>
ทุก material task ให้ Auto-Boot จาก UAAC-BOOT ใช้ applicable Skills เอง และทำต่อจาก canonical Project state เท่านั้น; ถ้าอ่าน/ยืนยันไม่ได้ให้หยุดและรายงาน — memory != Current Truth
```

## 10. Register evidence-backed claim contracts

อย่างน้อยต้องมี non-positive fallbacks สำหรับ:

```text
INSTALLATION_VALIDATED
EFFECTIVE
BOOTSTRAP_CONVERGENCE_FAILED
PROJECT_BINDING_MATCH
AUTO_BOOT_VALID
TASK_CONTEXT_CURRENT
CANONICAL_SURFACE_VISIBLE
PLATFORM_ADAPTER_INVOKED
BASE_FRESHNESS_MATCH
ATOMIC_PUBLICATION_VERIFIED
```

Unregistered/unsupported status = `STATUS_UNKNOWN`; ห้ามอนุมานเป็น opposite positive

## 11. Validate before effectiveness

Run:

```bash
python tools/validate_installation.py --project <PROJECT_ROOT> --package <PINNED_UAAC_PACKAGE>
```

Installation validation ต้องพิสูจน์อย่างน้อย:

- one front door per declared Project boundary
- binding/schema/locators/document roles/capability/procedures valid
- Kernel precedes Skill discovery
- platform adapters actually invoke on ordinary material task
- Auto-Boot freshness reuse/invalidation
- pre-write stale-context detection
- local/remote visibility and receiver access
- active + terminal lineage recovery
- cross-agent convergence of material identities
- required `S-INSTALL-*` scenarios for the Project profile

`INSTALLATION_VALIDATED` ห้ามออกจาก copied templates หรือ self-report

## 12. Commit/publish Project installation atomically

Before ref update recheck current base and expected old ref. Final Project commit/tree must contain front door and every linked target together and exclude temporary payloads/caches/probes

After push, perform remote readback from each intended Agent access surface and compare exact identities

## 13. Effective adoption

Only competent Project authority may set `EFFECTIVE`, referencing the validated installation and exact pinned release. A feature-branch governance proposal is not effective until promoted by the declared policy

## 14. Required final report

Report separately:

```yaml
core_installed:
installation_validated:
effective:
project_binding:
canonical_front_door:
pinned_uaac_identity:
project_document_routes:
capability_pack:
adapter_invocation_evidence:
boot_freshness:
continuation_and_visibility:
test_results:
remote_readback:
known_limitations:
blockers:
exact_next_action:
```

Never use unqualified `DONE` to imply states not evidenced
