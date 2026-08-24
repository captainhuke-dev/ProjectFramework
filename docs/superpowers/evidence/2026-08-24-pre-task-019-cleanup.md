# Pre-TASK-019 Cleanup and Tai-F3 WSL Repair Evidence

Captured: `2026-08-24T21:09:00+07:00`

Purpose: close legacy state before starting `TASK-019` and preserve the exact continuation point for the WSL repair that requires a Windows restart.

## 1. TASK-018 post-merge reconciliation

- PR `#20` was verified `MERGED`.
- Merge commit: `ba817a6c4a6ccbe5a33cab63868e90330095b5e6`.
- `docs/superpowers/PROJECT-TASKS.md` was reconciled from transient `PUBLISHED_TO_PR_20` state to `MERGED_TO_MAIN`.
- `docs/superpowers/plans/2026-08-24-project-upgrade-command.md` was reconciled to the same merge truth.
- Reconciliation commit: `31175eb8522074a3aa44f89335772a3a15a7fbca`.
- Fresh Git verification after push: local `main` and remote `origin/main` both resolve to `31175eb8522074a3aa44f89335772a3a15a7fbca`.

## 2. Legacy worktree and merged-branch cleanup

All removed worktrees were verified clean and their HEAD commits were already incorporated into `main` before deletion.

Removed worktrees:

- `.worktrees/agent-1051f814`
- `.worktrees/agent-334a679c`
- `.worktrees/agent-5d610662`
- `.worktrees/agent-64fe16ad`
- `.worktrees/agent-671799ca`
- `.worktrees/agent-820933bb`
- `.worktrees/framework-1.2.6-bootstrap-location-design`
- `.worktrees/project-upgrade-command`

Deleted merged local branches:

- `framework-1.2.5-implementation`
- `framework-1.2.6-bootstrap-location-design`
- `framework-1.2.6-design-reconciled`
- `framework-1.2.6-implementation`
- `reconcile-framework-1.3-task8`
- `work/framework-1.3-command-upgrade`
- `work/project-upgrade-command`

Deleted merged remote branches:

- `framework-1.2.6-bootstrap-location-design`
- `framework-1.2.6-implementation`
- `work/framework-1.3-command-upgrade`
- `work/project-upgrade-command`
- `framework-1.2.6-project-path-correction` — current remote head `e0ea351b9fc0aa9d4929b038504e9a6c808a70b8` matched merged PR `#16` head exactly, so deletion was safe despite non-ancestor history from the merge method.

Intentionally preserved because they contain unmerged work:

- local `framework-next-improvement-planning`
- remote `hz-framework` — contains substantial UAAC history not present in `main`; no merged PR establishes safe deletion.

After cleanup, `git worktree list` contains only the canonical root worktree.

## 3. Tai-F3 WSL repair

### Root cause observed

Before repair:

- Tai-F3 `wsl_exec`: `available=false`, `ready=false`, reason `wsl_status_failed`.
- Tai-F3 `wsl_fs`: `available=false`, `ready=false`, reason `wsl_status_failed`.
- `wsl.exe --status` failed.
- `LxssManager` service did not exist.
- `WslService` service did not exist.

This established that WSL was not merely stopped; the Windows WSL component/package was not active/installed completely.

### Repair applied

Executed:

`wsl.exe --install --no-distribution`

Observed successful installation phases:

- `Virtual Machine Platform has been installed.`
- `Windows Subsystem for Linux has been installed.`
- Installer exit code: `0`.
- Windows reported: `Changes will not be effective until the system is rebooted.`

Post-install, pre-reboot `wsl.exe --status` still returns `WSL_E_WSL_OPTIONAL_COMPONENT_REQUIRED`, which is expected while the newly installed optional component is pending activation by reboot.

Tai-F3 health therefore remains pre-reboot:

- `wsl_exec`: `available=false`, `ready=false`, reason `wsl_status_failed`.
- `wsl_fs`: `available=false`, `ready=false`, reason `wsl_status_failed`.

### Required post-reboot verification

After Windows restart, verify in this order:

1. `wsl.exe --status` succeeds.
2. Tai-F3 `health(check_tool=wsl_exec)` no longer reports `wsl_status_failed`.
3. Tai-F3 `health(check_tool=wsl_fs)` no longer reports `wsl_status_failed`.
4. Check installed distributions. The repair intentionally used `--no-distribution`, so no Linux distribution was guessed or installed without a user-selected target. If Tai-F3 execution requires a distro, select/install one explicitly after component health is confirmed.

## Current checkpoint

- TASK-018 reconciliation: `COMPLETE`.
- merged worktree/branch cleanup: `COMPLETE` for safely deletable merged state.
- WSL component repair: `INSTALLED / REBOOT_REQUIRED`.
- `TASK-019` must not begin until post-reboot WSL verification resolves the remaining environment state.
