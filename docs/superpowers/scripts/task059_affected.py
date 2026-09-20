#!/usr/bin/env python3
# TASK-059 AFFECTED verification suite (cumulative).
# Run from anywhere: python task059_affected.py [repo_root]
import re, sys, os, subprocess, glob

root = sys.argv[1] if len(sys.argv) > 1 else "E:/GitHub/ProjectFramework"
results = []

def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))

def rd(path):
    with open(os.path.join(root, path), "rb") as f:
        return f.read()

def txt(path):
    return rd(path).decode("utf-8")

def git(*args):
    return subprocess.run(list(args), cwd=root, capture_output=True, text=True).stdout.strip()

# ---------- A. Release identity ----------
y = txt("Framework-Source/FRAMEWORK-RELEASE.yaml")
check("A1 descriptor framework_version == 1.21.0", re.search(r'framework_version: "1.21.0"', y))
check("A2 descriptor schema_version == 1.0.0", re.search(r'schema_version: "1.0.0"', y))
check("A3 descriptor release_format_version == 3", re.search(r'release_format_version: 3', y))
check("A4 latest_framework_amendment == TASK-059 amendment",
      'latest_framework_amendment: "references/framework-governance-amendment-260920-task059-v3-forward-port-runtime-contract.md"' in y)

am = txt("Framework-Source/references/framework-governance-amendment-260920-task059-v3-forward-port-runtime-contract.md")
check("A5 amendment Framework 1.21.0", "Framework: `1.21.0`" in am)
check("A6 amendment Schema 1.0.0", "Schema: `1.0.0`" in am)
check("A7 amendment release format 3", "Release format: `3`" in am)
check("A8 amendment Source Task TASK-059", "Source Task: `TASK-059`" in am)
check("A9 amendment predecessor == TASK-058 Wave A V2 amendment",
      "framework-governance-amendment-260916-task058-wave-a-v2-deterministic-execution-foundation.md" in am)

# ---------- B. Normative content present in amendment ----------
for token, name in [
    ("record_type: RUNTIME_EVENT", "B1 RUNTIME_EVENT shape"),
    ("record_type: EXECUTION_CHECKPOINT", "B2 EXECUTION_CHECKPOINT shape"),
    ("record_type: EFFECT_POLICY", "B3 EFFECT_POLICY shape"),
    ("record_type: EFFECT_PERMIT", "B4 EFFECT_PERMIT shape"),
    ("record_type: RLM_EXECUTION_PROFILE", "B5 RLM_EXECUTION_PROFILE shape"),
    ("RECOVERY_BLOCKED", "B6 RECOVERY_BLOCKED fail-closed"),
    ("(runtime_generation, fence_epoch)", "B7 generation-paired fence identity"),
    ("APPLIED | NOT_APPLIED | PARTIAL | STILL_UNKNOWN", "B8 reconciliation outcomes"),
    ("MANUAL_RESOLUTION_REQUIRED", "B9 manual resolution disposition"),
    ("BUDGET_EXHAUSTED", "B10 budget exhaustion disposition"),
    ("WAITING_FOR_REAUTHORIZATION", "B11 reauth disposition"),
    ("max_recursion_depth", "B12 RLM max_recursion_depth"),
    ("parent consumption + sum(child allocations) <= root budget", "B13 hierarchical budget invariant"),
    ("PARTIALLY_COMPENSATED", "B14 partial compensation truth"),
    ("BACKWARD_COMPATIBLE", "B15 upgrade compatibility class"),
    ("REQUIRES_MIGRATION", "B16 migration class"),
    ("INCOMPATIBLE", "B17 incompatible class"),
    ("REFERENCE_ONLY", "B18 secret minimization REFERENCE_ONLY"),
    ("HASH_ONLY", "B19 secret minimization HASH_ONLY"),
    ("Python 3.14", "B20 handoff Python 3.14"),
    ("Prime Agent role != ProjectFramework dependency", "B21 Prime Agent non-dependency"),
    ("single-use", "B22 permit single-use"),
    ("non-transferable", "B23 permit non-transferable"),
    ("MEDIATED_BY_EFFECT_GATEWAY", "B24 mediation class"),
    ("EXPLICITLY_PROHIBITED", "B25 prohibited/confined class"),
    ("PRECONDITION_CONFLICT", "B26 stale precondition outcome"),
    ("IDEMPOTENT | CONDITIONALLY_IDEMPOTENT | NON_IDEMPOTENT | UNKNOWN", "B27 idempotency classes"),
    ("REVERSIBLE_ATOMIC | COMPENSATABLE | IRREVERSIBLE | UNKNOWN", "B28 reversibility classes"),
    ("CONTRACT_READY", "B29 completion gate state"),
]:
    check(name, token in am)

# ---------- C. Authority invariants ----------
for token, name in [
    ("Supervisor decision != AUTH", "C1 supervisor != AUTH"),
    ("Supervisor liveness != Execution Ownership Grant", "C2 liveness != ownership"),
    ("Heartbeat != completion evidence", "C3 heartbeat != completion"),
    ("Effect Permit ≠ AUTH-*", "C4 permit != AUTH (core)"),
    ("Model proposal ≠ Runtime decision", "C5 proposal != decision"),
    ("Cancellation ≠ rollback", "C6 cancellation != rollback"),
    ("Compensation ≠ history erasure", "C7 compensation != erasure"),
    ("Runtime Event Journal ≠ Checkpoint ≠ Project Source ≠ canonical Task lifecycle truth", "C8 journal hierarchy"),
    ("Task DONE ≠ MERGED ≠ PUSHED ≠ RELEASED ≠ ARTIFACT_PUBLISHED ≠ DEPLOYED", "C9 done != publication chain"),
    ("R4_CTX ≠ Risk R4", "C10 R4_CTX != Risk"),
]:
    check(name, token in am)

# ---------- D. Wave A V2 preservation (no duplication/override) ----------
wave_a = txt("Framework-Source/references/framework-governance-amendment-260916-task058-wave-a-v2-deterministic-execution-foundation.md")
check("D1 Wave A V2 amendment intact (777 lines)", wave_a.count("\n") >= 770)
check("D2 Wave A V2 amendment still Framework 1.20.0", "Framework: `1.20.0`" in wave_a)
check("D3 amendment declares Wave A V2 preserved unchanged", "preserved unchanged and remain authoritative" in am)
check("D4 amendment extends compositionally", "extends them compositionally; it creates no parallel equivalents" in am)
check("D5 no new semantic slot", "changes no Project Source semantic slot" in am)
check("D6 no new Stable-ID family", "no Project Source Stable-ID family" in am)
check("D7 no new Registered Command", "no Registered Command set" in am)
check("D8 Risk remains R0-R3", "Risk remains exactly `R0–R3`" in am)
check("D9 no canonical Task lifecycle change", "no canonical Task lifecycle value" in am)

# ---------- E. Core Governance projection ----------
cg = txt("Framework-Source/references/core-governance-rules.md")
check("E1 core gov TASK-059 section", "## Framework 1.21.0 V3 Forward-Port Runtime Control Contract (TASK-059)" in cg)
check("E2 core gov Wave A V2 section preserved", "## Framework 1.20.0 Wave A V2 Deterministic Execution Foundation (TASK-058)" in cg)
check("E3 core gov TASK-057 section preserved", "TASK-057 ships governance/documentation contracts" in cg)
check("E4 core gov references TASK-059 amendment", "framework-governance-amendment-260920-task059-v3-forward-port-runtime-contract.md" in cg)
check("E5 core gov permit invariant", "Effect Permit ≠ AUTH-*" in cg)

# ---------- F. SKILL guidance ----------
sk = txt("Framework-Source/SKILL.md")
check("F1 SKILL TASK-059 section", "## Framework 1.21.0 V3 Forward-Port Runtime Control Contract" in sk)
check("F2 SKILL Wave A V2 section preserved", "## Framework 1.20.0 Wave A V2 Deterministic Execution Foundation" in sk)
check("F3 SKILL references amendment", "framework-governance-amendment-260920-task059-v3-forward-port-runtime-contract.md" in sk)
check("F4 SKILL no-runtime boundary", "no runtime, queue, database, scheduler, daemon" in sk)

# ---------- G. Pressure scenarios ----------
ps = txt("Framework-Source/tests/pressure-scenarios.md")
nums = [int(m) for m in re.findall(r"^## Scenario (\d+) —", ps, re.M)]
check("G1 scenarios contiguous 1..620", nums == list(range(1, 621)), "count=%d" % len(nums))
check("G2 no duplicates", len(nums) == len(set(nums)))
check("G3 ceiling is 620", max(nums) == 620)
# 557-590 unchanged vs baseline (git)
base_557_590 = subprocess.run(
    ["git", "show", "04b718446d7579f0336d5cdac24a66037e0f20e0:Framework-Source/tests/pressure-scenarios.md"],
    cwd=root, capture_output=True, text=True).stdout
def scenario_block(text, n):
    m = re.search(r"(^## Scenario %d —.*?)(?=^## Scenario %d —|\Z)" % (n, n + 1), text, re.M | re.S)
    return m.group(1) if m else None
unchanged = all(scenario_block(base_557_590, n) == scenario_block(ps, n) for n in range(557, 591))
check("G4 Wave A V2 scenarios 557-590 byte-identical to baseline", unchanged)
new_blocks = [n for n in range(591, 621) if scenario_block(ps, n)]
check("G5 all 30 new scenarios 591-620 present", len(new_blocks) == 30)
# each new scenario has the 4-part structure
struct_ok = all(
    all(k in scenario_block(ps, n) for k in ("**Prompt:**", "**Temptation:**", "**Pass:**", "**Fail:**", "**GREEN expectation:**"))
    for n in range(591, 621))
check("G6 new scenarios have Prompt/Temptation/Pass/Fail/GREEN structure", struct_ok)
# GREEN expectations reference the TASK-059 amendment
refs_ok = all("TASK-059 amendment" in scenario_block(ps, n) for n in range(591, 621))
check("G7 new scenarios cite TASK-059 amendment sections", refs_ok)

# ---------- H. Starters ----------
starters = {
    "runtime-contract.md": ("RUNTIME_CONTRACT", "record_type: RUNTIME_CONTRACT"),
    "runtime-event-journal.md": ("RUNTIME_EVENT", "record_type: RUNTIME_EVENT"),
    "execution-checkpoint.md": ("EXECUTION_CHECKPOINT", "record_type: EXECUTION_CHECKPOINT"),
    "effect-policy.md": ("EFFECT_POLICY+PERMIT", "record_type: EFFECT_POLICY"),
    "rlm-executor-profile.md": ("RLM_EXECUTION_PROFILE", "record_type: RLM_EXECUTION_PROFILE"),
}
for fname, (label, token) in starters.items():
    p = "Framework-Source/templates/project-execution/" + fname
    check("H starter %s exists with %s" % (fname, label), os.path.exists(os.path.join(root, p)) and token in txt(p))
ep = txt("Framework-Source/templates/project-execution/effect-policy.md")
check("H6 effect-policy starter includes EFFECT_PERMIT shape", "record_type: EFFECT_PERMIT" in ep)
check("H7 all starters record_version 1.0",
      all('record_version: "1.0"' in txt("Framework-Source/templates/project-execution/" + f) for f in starters))
readme = txt("Framework-Source/templates/project-execution/README.md")
check("H8 README lists 5 TASK-059 starters",
      all(s in readme for s in ("runtime-contract.md", "runtime-event-journal.md", "execution-checkpoint.md", "effect-policy.md", "rlm-executor-profile.md")))
check("H9 README TASK-059 section", "TASK-059 (Framework `1.21.0`)" in readme)
check("H10 README Wave A V2 section preserved", "TASK-058 (Framework `1.20.0`)" in readme)

# ---------- I. No runtime code ----------
bad = []
for dirpath, dirnames, filenames in os.walk(os.path.join(root, "Framework-Source")):
    for fn in filenames:
        if fn.endswith((".py", ".js", ".ts", ".ps1", ".sh", ".go", ".rs", ".exe", ".bin")):
            bad.append(fn)
check("I1 no executable files in Framework-Source", not bad, str(bad))

# ---------- J. Release surfaces ----------
mock = sorted(glob.glob(os.path.join(root, "Framework-Source/templates/project-source-mockup/*.md")))
stamps = [txt(f) for f in mock]
check("J1 22 mockup templates", len(mock) == 22, str(len(mock)))
check("J2 all mockup stamps 1.21.0/1.0.0",
      all('project_source_framework_version: "1.21.0"' in t and 'project_source_schema_version: "1.0.0"' in t for t in stamps))
t00 = txt("Framework-Source/templates/00-project-source-framework.md")
check("J3 root template stamp 1.21.0", 'project_source_framework_version: "1.21.0"' in t00)
check("J4 root template 12.5 section", "### 12.5 Framework 1.21 V3 Forward-Port Runtime Control Contract" in t00)
check("J5 root template 12.4 Wave A V2 preserved", "### 12.4 Framework 1.20 Wave A V2 Deterministic Execution Foundation" in t00)
cs = txt("Framework-Source/templates/core-document-skeletons.md")
check("J6 skeleton stamp 1.21.0", 'project_source_framework_version: "1.21.0"' in cs)
check("J7 skeleton 1.21 section", "## Framework 1.21.0 V3 Forward-Port Runtime Control Contract Semantics" in cs)
check("J8 skeleton 1.20 section preserved", "## Framework 1.20.0 Wave A V2 Deterministic Execution Foundation Semantics" in cs)
r = txt("README.md")
check("J9 README version 1.21.0", "- Project Source Framework: **1.21.0**" in r)
check("J10 README 1.21 section", "## Framework 1.21.0 V3 Forward-Port Runtime Control Contract" in r)
check("J11 README 1.20 section preserved", "## Framework 1.20.0 Wave A V2 Deterministic Execution Foundation" in r)
mn = txt("Framework-Source/MIGRATION-NOTES.md")
check("J12 migration notes 1.20→1.21 current", "## 1.20.0 → 1.21.0 (current)" in mn)
check("J13 migration notes 1.19→1.20 previous", "## 1.19.0 → 1.20.0 (previous)" in mn)
check("J14 migration notes scenario 591-620", "591–620" in mn)

# ---------- K. Self-host NOT promoted (remains 1.20.0 active) ----------
ps_dir = os.path.join(root, "Project-Source")
active = [f for f in os.listdir(ps_dir) if re.match(r"^\d{2}-.+\.md$", f)]
stamps2 = [txt(os.path.join(ps_dir, f)) for f in active]
check("K1 16 active Project Source documents", len(active) == 16, str(len(active)))
check("K2 active Project Source still 1.20.0/1.0.0 (self-host not promoted pre-merge)",
      all('project_source_framework_version: "1.20.0"' in t and 'project_source_schema_version: "1.0.0"' in t for t in stamps2))

# ---------- L. Launchers / Registered Commands unchanged ----------
base = "04b718446d7579f0336d5cdac24a66037e0f20e0"
for f in ["Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md", "Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md",
          "PROJECT-BOOTSTRAP.md", "Framework-Source/templates/PROJECT-BOOTSTRAP.md"]:
    now = git("hash-object", f)
    then = git("rev-parse", base + ":" + f)
    check("L %s byte-identical to baseline" % f, now == then)
boot = txt("PROJECT-BOOTSTRAP.md")
cmds = ["[Project Status]", "[Project Path]", "[Project Upgrade]", "[Project Audit]", "[Session]", "[Goal]", "[Meeting]"]
check("L5 Registered Commands unchanged (7)", all(c in boot for c in cmds))

# ---------- M. Historical integrity ----------
hist_am = "Framework-Source/references/framework-governance-amendment-260916-task058-wave-a-v2-deterministic-execution-foundation.md"
check("M1 TASK-058 amendment blob unchanged", git("hash-object", hist_am) == git("rev-parse", base + ":" + hist_am))
check("M2 TASK-057 amendment blob unchanged",
      git("hash-object", "Framework-Source/references/framework-governance-amendment-260914-task057-ai-controltower-governance-support-layer.md")
      == git("rev-parse", base + ":Framework-Source/references/framework-governance-amendment-260914-task057-ai-controltower-governance-support-layer.md"))
check("M3 historical V3 spec untouched (source material only)",
      git("hash-object", "docs/superpowers/specs/2026-09-16-task058-deterministic-execution-runtime-contract-design.md")
      == git("rev-parse", base + ":docs/superpowers/specs/2026-09-16-task058-deterministic-execution-runtime-contract-design.md"))
check("M4 TASK-058 release evidence untouched",
      git("hash-object", "docs/superpowers/evidence/2026-09-16-task-058-wave-a-v2-deterministic-execution-foundation-release-full.md")
      == git("rev-parse", base + ":docs/superpowers/evidence/2026-09-16-task-058-wave-a-v2-deterministic-execution-foundation-release-full.md"))

# ---------- N. Hygiene ----------
check("N1 git diff --check clean", git("diff", "--check") == "")
check("N2 working tree clean", git("status", "--porcelain") == "")
crlf_ok = True
crlf_bad = []
for dirpath, dirnames, filenames in os.walk(os.path.join(root, "Framework-Source")):
    for fn in filenames:
        if fn.endswith(".md"):
            d = rd(os.path.relpath(os.path.join(dirpath, fn), root))
            if d.count(b"\n") - d.count(b"\r\n") != 0:
                crlf_ok = False
                crlf_bad.append(fn)
check("N3 all Framework-Source .md files CRLF-consistent", crlf_ok, str(crlf_bad))

# ---------- O. RED→GREEN proof ----------
base_fs = subprocess.run(["git", "archive", base, "Framework-Source"], cwd=root, capture_output=True).stdout
import io, zipfile
z = zipfile.ZipFile(io.BytesIO(base_fs))
base_am_names = z.namelist()
check("O1 TASK-059 amendment is new (not in baseline tree)",
      "Framework-Source/references/framework-governance-amendment-260920-task059-v3-forward-port-runtime-contract.md" not in base_am_names)
base_cg = z.read("Framework-Source/references/core-governance-rules.md").decode("utf-8")
check("O2 baseline core gov had no Effect Permit contract", "Effect Permit" not in base_cg)
check("O3 baseline core gov had no Runtime Event Journal contract", "Runtime Event Journal" not in base_cg)
check("O4 current core gov has both (GREEN)", "Effect Permit" in cg and "Runtime Event Journal" in cg)

# ---------- report ----------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("TASK059_AFFECTED %d/%d %s" % (passed, total, "PASS" if passed == total else "FAIL"))
for name, ok, detail in results:
    if not ok:
        print("FAIL: %s %s" % (name, detail))
sys.exit(0 if passed == total else 1)
