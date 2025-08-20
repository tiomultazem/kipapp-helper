@echo off
setlocal enabledelayedexpansion

:: Nama folder tempat python akan dipasang
set PYDIR=python-portable
set PYEXE=%~dp0%PYDIR%\python.exe

:: Cek apakah Python sudah terinstall
if exist "%PYEXE%" (
    echo Python sudah terinstall.
    goto RUN
)

echo Mengunduh Python 3.12.7...
set "URL=https://www.python.org/ftp/python/3.12.7/python-3.12.7-amd64.exe"
set "DEST=%~dp0python-installer.exe"

REM --- 0) kalau sudah ada file hasil download, skip ---
if exist "%DEST%" for %%S in ("%DEST%") do if %%~zS gtr 0 goto :HAVE_INSTALLER

REM --- 1) coba nyalakan service BITS (kalau mati) lalu download pakai BITS ---
sc query bits | find /i "RUNNING" >nul || (net start bits >nul 2>&1)
bitsadmin /transfer downloadPython /priority high "%URL%" "%DEST%" >nul 2>&1

REM --- 2) fallback PowerShell (TLS1.2) ---
if not exist "%DEST%" powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "[Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12; try { Invoke-WebRequest -Uri '%URL%' -OutFile '%DEST%'; } catch { exit 1 }"  >nul 2>&1

REM --- 3) fallback curl (Windows 10+ ada bawaan) ---
if not exist "%DEST%" curl -L "%URL%" -o "%DEST%"  >nul 2>&1

REM --- 4) fallback certutil (hampir selalu ada) ---
if not exist "%DEST%" certutil -urlcache -split -f "%URL%" "%DEST%"  >nul 2>&1

if not exist "%DEST%" (
    echo Gagal mengunduh Python installer. Cek koneksi/proxy/izin folder.
    pause
    exit /b
)

:HAVE_INSTALLER

if not exist "%~dp0python-installer.exe" (
    echo Gagal mengunduh Python installer.
    pause
    exit /b
)

echo Menginstal Python ke direktori portabel...
"%~dp0python-installer.exe" /quiet InstallAllUsers=0 TargetDir="%~dp0%PYDIR%" Include_pip=1 PrependPath=0

if not exist "%PYEXE%" (
    echo Gagal menginstal Python.
    pause
    exit /b
)

:RUN
echo Menjalankan main.py...
"%PYEXE%" -m pip install --upgrade pip
"%PYEXE%" -m pip install -r "%~dp0requirements.txt" 2>nul
"%PYEXE%" "%~dp0main.py"

pause