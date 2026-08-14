[CmdletBinding()]
param(
    [switch]$ClearStaleLocks
)

# SophaisImagination - verify the public artifact and push main safely.
# Run from the repo root in PowerShell: .\_ops\push.ps1
# If verified-stale Git locks remain after a crashed process:
#   .\_ops\push.ps1 -ClearStaleLocks

$ErrorActionPreference = "Stop"
$RepoRoot = (Resolve-Path (Split-Path -Parent $PSScriptRoot)).Path
$GitRoot = Join-Path $RepoRoot ".git"
Set-Location -LiteralPath $RepoRoot

if (-not (Test-Path -LiteralPath $GitRoot -PathType Container)) {
    throw "Expected a Git worktree at $RepoRoot."
}

$LockCandidates = @(
    (Join-Path $GitRoot "index.lock"),
    (Join-Path $GitRoot "HEAD.lock"),
    (Join-Path $GitRoot "objects\maintenance.lock")
)
$LockCandidates += @(
    Get-ChildItem -LiteralPath (Join-Path $GitRoot "objects") -Recurse -File -Filter "tmp_obj_*" -ErrorAction SilentlyContinue |
        Select-Object -ExpandProperty FullName
)
$LockCandidates = @($LockCandidates | Where-Object { Test-Path -LiteralPath $_ } | Sort-Object -Unique)

if ($LockCandidates.Count -gt 0 -and -not $ClearStaleLocks) {
    $List = ($LockCandidates | ForEach-Object { "  - $_" }) -join [Environment]::NewLine
    throw @"
Git lock or temporary-object files exist:
$List

Do not delete them while Git is running. Confirm that no Git operation is active,
then rerun with -ClearStaleLocks only if these files are stale.
"@
}

if ($LockCandidates.Count -gt 0 -and $ClearStaleLocks) {
    $GitProcesses = @(Get-Process -Name "git", "git-lfs" -ErrorAction SilentlyContinue)
    if ($GitProcesses.Count -gt 0) {
        $ProcessList = ($GitProcesses | ForEach-Object { "$($_.ProcessName) (PID $($_.Id))" }) -join ", "
        throw "Refusing to clear Git locks while Git processes are active: $ProcessList"
    }

    $GitRootWithSeparator = $GitRoot.TrimEnd("\", "/") + [IO.Path]::DirectorySeparatorChar
    foreach ($Candidate in $LockCandidates) {
        $ResolvedCandidate = [IO.Path]::GetFullPath($Candidate)
        if (-not $ResolvedCandidate.StartsWith($GitRootWithSeparator, [StringComparison]::OrdinalIgnoreCase)) {
            throw "Refusing to remove a path outside .git: $ResolvedCandidate"
        }
        Remove-Item -LiteralPath $ResolvedCandidate -Force
        Write-Host "Removed verified-stale Git file: $ResolvedCandidate"
    }
}

$LocalEmail = (git config --local --get user.email 2>$null | Select-Object -First 1)
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($LocalEmail)) {
    throw @"
No repository-local Git email is configured. Set the GitHub noreply address first:
  git config --local user.email "68042811+castleism@users.noreply.github.com"
"@
}
$LocalEmail = $LocalEmail.Trim()
if ($LocalEmail -notmatch '^[^@\s]+@users\.noreply\.github\.com$') {
    throw "Repository-local user.email must use a GitHub noreply address. The configured address was not printed."
}

$CurrentBranch = (git branch --show-current 2>$null | Select-Object -First 1)
if ($LASTEXITCODE -ne 0 -or $CurrentBranch.Trim() -ne "main") {
    throw "This helper only verifies and publishes refs/heads/main. Switch to main first."
}

git rev-parse --verify --quiet refs/remotes/origin/main *> $null
if ($LASTEXITCODE -ne 0) {
    throw "refs/remotes/origin/main is unavailable. Fetch origin/main before publishing."
}

$CommitRange = "refs/remotes/origin/main..refs/heads/main"
$CommitLines = @(git log $CommitRange --format='%H%x09%ae%x09%ce')
if ($LASTEXITCODE -ne 0) {
    throw "Could not inspect commit emails for $CommitRange."
}

$BadCommitHashes = @()
foreach ($Line in $CommitLines) {
    if ([string]::IsNullOrWhiteSpace($Line)) { continue }
    $Parts = $Line -split "`t"
    if ($Parts.Count -lt 3) {
        throw "Unexpected git log output while checking commit emails; values were not printed."
    }
    foreach ($Address in $Parts[1..2]) {
        if ($Address -notmatch '^[^@\s]+@users\.noreply\.github\.com$') {
            $BadCommitHashes += $Parts[0]
        }
    }
}
$BadCommitHashes = @($BadCommitHashes | Sort-Object -Unique)
if ($BadCommitHashes.Count -gt 0) {
    throw @"
$($BadCommitHashes.Count) unpushed commit(s) use a non-noreply author or committer address.
The addresses were not printed. Commit hashes:
$($BadCommitHashes -join "`n")
"@
}

$WorkingTreeChanges = @(git status --porcelain --untracked-files=normal)
if ($LASTEXITCODE -ne 0) {
    throw "Could not inspect the working tree before push."
}
if ($WorkingTreeChanges.Count -gt 0) {
    throw @"
The working tree has $($WorkingTreeChanges.Count) uncommitted or untracked change(s).
File names were not printed. Commit or intentionally remove them before pushing so
the verifier checks the exact commit that GitHub Pages will deploy.
"@
}

$Python = Get-Command "python" -ErrorAction SilentlyContinue
if ($null -ne $Python) {
    & $Python.Source "scripts\verify_site.py"
} else {
    $PyLauncher = Get-Command "py" -ErrorAction SilentlyContinue
    if ($null -eq $PyLauncher) {
        throw "Python 3 is required to run scripts\verify_site.py before pushing."
    }
    & $PyLauncher.Source -3 "scripts\verify_site.py"
}
if ($LASTEXITCODE -ne 0) {
    throw "Site verification failed; push cancelled."
}

git diff --check $CommitRange
if ($LASTEXITCODE -ne 0) {
    throw "git diff --check failed for the unpushed commit range; push cancelled."
}

git push -u origin refs/heads/main:refs/heads/main
if ($LASTEXITCODE -ne 0) {
    throw "git push failed with exit code $LASTEXITCODE."
}
