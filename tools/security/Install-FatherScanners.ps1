# FATHER Security Scanner Lab - non-destructive bootstrap (Windows PowerShell)
# Usage: powershell -NoProfile -ExecutionPolicy Bypass -File .\tools\security\Install-FatherScanners.ps1
# Optional: -SkipSemgrep -AuditOnly
[CmdletBinding()]
param(
  [switch]$SkipSemgrep,
  [switch]$AuditOnly,
  [string]$LabRoot = "$env:USERPROFILE\FATHER_SECURITY_LAB"
)
$ErrorActionPreference = "Stop"
New-Item -ItemType Directory -Path $LabRoot -Force | Out-Null
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$log = Join-Path $LabRoot "install-$stamp.log"
Start-Transcript -Path $log | Out-Null
$findings = New-Object 'System.Collections.Generic.List[object]'
function Add-Result([string]$name,[string]$state,[string]$detail) {
    $findings.Add([pscustomobject]@{ Tool=$name; Status=$state; Detail=$detail })
    Write-Host "[$state] $name : $detail"
}
function Find-Tool([string]$name) {
    return Get-Command $name -ErrorAction SilentlyContinue
}
function Install-Winget([string]$name,[string]$wingetId) {
    if (Find-Tool $name) {
        $version = (& $name --version 2>&1 | Select-Object -First 1)
        Add-Result $name 'PRESENT' "$version (no changes)"
        return
    }
    if ($AuditOnly) { Add-Result $name 'MISSING' 'AuditOnly: install skipped'; return }
    if (-not (Find-Tool 'winget')) {
        Add-Result $name 'BLOCKED' 'winget not found. Install Windows App Installer.'
        return
    }
    Write-Host "Installing $name via WinGet: $wingetId"
    & winget install --id $wingetId --exact --source winget --accept-package-agreements --accept-source-agreements --disable-interactivity
    $exit = $LASTEXITCODE
    if ($exit -ne 0) { Add-Result $name 'INSTALL_FAILED' "winget exit=$exit"; return }
    # WinGet PATH may require opening a new terminal; do not claim success without finding binary.
    if (Find-Tool $name) {
        $version = (& $name --version 2>&1 | Select-Object -First 1)
        Add-Result $name 'INSTALLED' "$version"
    } else {
        Add-Result $name 'INSTALLED_NEEDS_NEW_TERMINAL' 'WinGet completed, executable not on current PATH'
    }
}
try {
    Write-Host "FATHER scanner setup - $(Get-Date -Format o)"
    Write-Host "Lab folder: $LabRoot"
    Write-Host "Existing programs will NOT be uninstalled/updated. No remote hosts will be scanned."
    Install-Winget 'trivy' 'AquaSecurity.Trivy'
    Install-Winget 'grype' 'Anchore.Grype'
    Install-Winget 'osv-scanner' 'Google.OSVScanner'
    if (-not $SkipSemgrep) {
        $py = Find-Tool 'py'
        if (-not $py) {
            Add-Result 'semgrep' 'BLOCKED' 'Python launcher py.exe not found. Install Python and rerun.'
        } else {
            $venv = Join-Path $LabRoot 'semgrep-venv'
            $semgrep = Join-Path $venv 'Scripts\semgrep.exe'
            if ((Test-Path $semgrep) -and $AuditOnly) {
                Add-Result 'semgrep' 'PRESENT' "$semgrep"
            } elseif ($AuditOnly) {
                Add-Result 'semgrep' 'MISSING' 'AuditOnly: install skipped'
            } else {
                if (-not (Test-Path $semgrep)) {
                    & py -3 -m venv $venv
                    if ($LASTEXITCODE -ne 0) { throw "Could not create isolated Semgrep venv" }
                    & (Join-Path $venv 'Scripts\python.exe') -m pip install --disable-pip-version-check 'semgrep'
                    if ($LASTEXITCODE -ne 0) { throw "Semgrep pip install failed" }
                }
                if (Test-Path $semgrep) { Add-Result 'semgrep' 'INSTALLED' "$semgrep" }
                else { Add-Result 'semgrep' 'INSTALL_FAILED' 'semgrep.exe missing after installation' }
            }
        }
    } else { Add-Result 'semgrep' 'SKIPPED' 'SkipSemgrep switch enabled' }
    Add-Result 'Greenbone' 'DEFERRED' 'Heavy multi-container network scanner. Requires separate resource and network review, not automatically installed.'
    Add-Result 'Network scans' 'DISABLED' 'Only scan explicit owned/authorized targets in a separate lab.'
    $json = Join-Path $LabRoot "install-status-$stamp.json"
    $findings | ConvertTo-Json -Depth 5 | Set-Content -Path $json -Encoding UTF8
    Write-Host "Status file: $json"
} catch {
    Add-Result 'bootstrap' 'ERROR' $_.Exception.Message
    $json = Join-Path $LabRoot "install-status-$stamp.json"
    $findings | ConvertTo-Json -Depth 5 | Set-Content -Path $json -Encoding UTF8
    Write-Error $_.Exception.Message
} finally {
    Stop-Transcript | Out-Null
    Write-Host "Transcript: $log"
}
