# Completed Work → Canonical Main Integration — Release Evidence

## Evidence identity

- **Scope:** integrate completed ProjectFramework work from `task025-project-knowledge`, `set1-foundation-suite`, and `task042-response-finalization-hardening` into canonical `main`.
- **Integration target at start:** `origin/main` = `5b95718f74b53685d9b6fa8c8bf21b87837fd557`.
- **User authorization:** explicit instruction on 2026-09-02 to merge completed work into `main`.
- **Push policy:** non-force canonical-main publication only after cumulative verification.

## Integration order and Base Freshness

1. `task025-project-knowledge` merged first because Set 1 is STACKED_WORK on TASK-025.
2. `set1-foundation-suite` merged second; no textual merge conflict occurred after TASK-025.
3. Direct TASK-042 merge was rejected after material conflicts showed `STALE_SEMANTIC`: the original TASK-042 line targeted Framework 1.9.1 while cumulative main had advanced through TASK-025 and Set 1 to Framework 1.12.0. Direct merge would downgrade current release/starter state and collide with scenario numbers already allocated to TASK-025/Set 1.
4. TASK-042 approved semantics were forward-ported onto the cumulative base as Framework 1.12.1. Original TASK-042 scenarios 269–280 remain historical evidence; cumulative integration scenarios are 339–350 so the final pressure-scenario range is 1–350 contiguous/unique.
5. Original TASK-042 branch ancestry was then connected with a history-only merge after the forward-port tree was verified, so Git records the branch as integrated without replacing the cumulative 1.12.1 tree with stale 1.9.1 content.

## Preserved completed work

- **TASK-025 Project Knowledge:** original AFFECTED 175/175 PASS; RELEASE_FULL 120/120 PASS; Project Knowledge templates and Knowledge≠Authority contract preserved.
- **Set 1 Foundation Suite:** TASK-033 / TASK-027 / TASK-034 / TASK-035 / TASK-037 DONE; original cumulative AFFECTED 75/75 PASS; RELEASE_FULL 108/108 PASS; Project-Execution tools/capabilities/trust and release/publication contracts preserved.
- **TASK-042 Response Finalization Hardening:** original branch AFFECTED 110/110 PASS; RELEASE_FULL 171/171 PASS. First-response bootstrap and unskippable final-response close semantics are forward-ported unchanged in intent onto Framework 1.12.1.

## Final cumulative candidate

```text
Candidate HEAD: 7b98161ceda1d53794e5f2b16855f257c560db4b
Candidate tree: d6c16007fa7280bb909272c3747c14eb5fc359c5
Framework-Source tree: 993b481c0d36057108df0eb87e41194bead64577
Release: Framework 1.12.1 / Schema 1.0.0 / release format 3
Scenarios: 1–350 contiguous/unique
Maintained Project Source starter stamps: 24 at Framework 1.12.1 / Schema 1.0.0
Launcher lengths: ChatGPT 716 / Claude 715
```

## Final verification

```text
INTEGRATION_AFFECTED 180/180 PASS
INTEGRATION_RELEASE_FULL 14/14 PASS
TASK025 ancestry: PASS
SET1 ancestry: PASS
TASK042 ancestry: PASS
Origin-main base ancestry: PASS
Git diff check: PASS
Unresolved conflict markers: NONE
Working tree at candidate freeze: CLEAN
```

The final RELEASE_FULL was run once on the unchanged candidate identified above. No Framework-Source mutation occurred after that run before this evidence file was written.

## Publication boundary

At evidence capture, canonical `origin/main` still points to the pre-integration base. This evidence authorizes no force push and does not itself prove remote publication. Project Source reconciliation must persist the integration candidate/evidence and the subsequent push must be fresh-verified before publication is reported complete.
