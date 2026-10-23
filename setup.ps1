# ==============================================================================
# S2 Legal AI Pro - Python Backend & RAG Environment Setup Script (Windows PowerShell)
# Research-Grade Router-Based Agentic RAG Architecture
# ==============================================================================

[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"

Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host "  S2 LEGAL AI PRO: ENVIRONMENT INITIALIZATION & DEPENDENCY SETUP" -ForegroundColor Cyan
Write-Host "=================================================================" -ForegroundColor Cyan

# Step 1: Create Directory Hierarchy
Write-Host "`n[1/4] Creating Directory Structure..." -ForegroundColor Yellow
$Directories = @(
    "backend",
    "backend\data",
    "backend\db",
    "backend\db\chroma_data"
)

foreach ($dir in $Directories) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
        Write-Host "  + Created directory: $dir" -ForegroundColor Green
    } else {
        Write-Host "  . Directory exists: $dir" -ForegroundColor Gray
    }
}

# Step 2: Verify Python Availability
Write-Host "`n[2/4] Verifying Python 3 Installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "  Found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Error "Python is not found in PATH. Please install Python 3.10+ and add it to PATH."
    exit 1
}

# Step 3: Initialize Virtual Environment (.venv)
Write-Host "`n[3/4] Initializing Virtual Environment (.venv)..." -ForegroundColor Yellow
$VenvPath = ".venv"
$VenvPython = Join-Path $VenvPath "Scripts\python.exe"
$VenvActivate = Join-Path $VenvPath "Scripts\Activate.ps1"

if (-not (Test-Path $VenvPython)) {
    Write-Host "  Creating new virtual environment at .venv..." -ForegroundColor Cyan
    python -m venv .venv
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Failed to create virtual environment."
        exit 1
    }
    Write-Host "  + Virtual environment successfully created." -ForegroundColor Green
} else {
    Write-Host "  . Existing virtual environment found at .venv" -ForegroundColor Gray
}

# Step 4: Install Dependencies from requirements.txt
Write-Host "`n[4/4] Installing / Updating Backend Dependencies..." -ForegroundColor Yellow
if (-not (Test-Path "requirements.txt")) {
    Write-Error "requirements.txt not found in current directory."
    exit 1
}

Write-Host "  Upgrading pip in virtual environment..." -ForegroundColor Cyan
& $VenvPython -m pip install --upgrade pip --quiet

Write-Host "  Installing packages from requirements.txt (this may take a couple of minutes)..." -ForegroundColor Cyan
& $VenvPython -m pip install -r requirements.txt

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n=================================================================" -ForegroundColor Green
    Write-Host "  ENVIRONMENT INITIALIZATION COMPLETE!" -ForegroundColor Green
    Write-Host "=================================================================" -ForegroundColor Green
    Write-Host "`nTo activate your environment in PowerShell, run:" -ForegroundColor White
    Write-Host "  .\.venv\Scripts\Activate.ps1" -ForegroundColor Yellow
    Write-Host "`nNext Steps:" -ForegroundColor White
    Write-Host "  1. Ingest Constitutional corpus:  python backend/ingest.py" -ForegroundColor Cyan
    Write-Host "  2. Start FastAPI Agentic Router:  uvicorn backend.main:app --reload --port 8000" -ForegroundColor Cyan
    Write-Host "  3. Start Vite React Frontend:     npm run dev" -ForegroundColor Cyan
} else {
    Write-Error "Failed to install some requirements. Please inspect the log above."
    exit 1
}
