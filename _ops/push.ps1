# SophaisImagination - clear sandbox git locks if present, then push.
# Run from the repo root in PowerShell:  .\_ops\push.ps1
$ErrorActionPreference = "Stop"
Set-Location (Split-Path -Parent $PSScriptRoot)

Remove-Item ".git\index.lock",".git\HEAD.lock",".git\objects\maintenance.lock" -Force -ErrorAction SilentlyContinue
Get-ChildItem ".git\objects" -Recurse -Filter "tmp_obj_*" -ErrorAction SilentlyContinue | Remove-Item -Force -ErrorAction SilentlyContinue

git push -u origin main
