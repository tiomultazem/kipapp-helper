@echo off
setlocal enabledelayedexpansion
color 0C
mode con: cols=80 lines=25
title WARNING - SYSTEM BREACH

REM === FAKE JUMPSCARE START ===
echo.
echo.
echo KOMPUTERMU SUDAH KUHACK
echo.
echo HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA
timeout /t 3 >nul

echo.
echo Mengambil kendali sistem...
ping localhost -n 3 >nul
echo Menghapus file sistem penting...
ping localhost -n 3 >nul
echo Membajak keyboard...
ping localhost -n 2 >nul
echo [GAGAL] Windows berhasil mengambilalih. Operasi hack gagal.
timeout /t 2 >nul

color 07
cls
echo Tenang aja, becanda kok :D 
timeout /t 2 >nul
echo Lanjut ngejalanin script beneran ya...

REM ========================
REM SETUP
REM ========================
set "MAIN_SCRIPT=%~dp0main.py"
set "PORTABLE_PYTHON=%~dp0python_full\python.exe"
set "INSTALLER_URL=https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe"

REM ========================
REM CARI PYTHON SISTEM
REM ========================
where python >nul 2>&1
if %errorlevel%==0 (
    echo [INFO] Python sistem ditemukan.
    set "PYTHON_EXE=python"
    goto ensure_pip
) else (
    goto install_python
)

REM ========================
REM CARI PYTHON PORTABLE
REM ========================
if exist "%PORTABLE_PYTHON%" (
    echo [INFO] Python portable ditemukan.
    set "PYTHON_EXE=%PORTABLE_PYTHON%"
    goto ensure_pip
)

REM ========================
REM INSTALL PYTHON PORTABLE
REM ========================
:install_python
echo [INFO] Python tidak ditemukan. Mengunduh installer...
curl -L -o python-installer.exe %INSTALLER_URL%

if not exist python-installer.exe (
    echo [ERROR] Gagal mengunduh Python.
    pause
    goto install_python
)

echo [INFO] Menginstall Python ke folder lokal...
python-installer.exe /quiet InstallAllUsers=0 PrependPath=0 TargetDir="%~dp0python_full"

if not exist "%PORTABLE_PYTHON%" (
    echo.
    echo [ERROR] Gagal menginstall Python.
    echo Silakan klik file "python-installer.exe" secara manual, pilih "Repair", lalu ulangi.
    pause
    goto install_python
)

set "PYTHON_EXE=%PORTABLE_PYTHON%"

REM ========================
REM CEK PIP
REM ========================
:ensure_pip
echo [INFO] Mengecek pip...
"%PYTHON_EXE%" -m pip --version >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [INFO] pip tidak ditemukan. Mencoba install...
    "%PYTHON_EXE%" -m ensurepip
    "%PYTHON_EXE%" -m pip install --upgrade pip
)

REM ========================
REM JALANKAN SCRIPT
REM ========================
echo [INFO] Menjalankan %MAIN_SCRIPT%...
"%PYTHON_EXE%" "%MAIN_SCRIPT%" 2>error.log

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ===============================
    echo   TERJADI ERROR SAAT MENJALANKAN SCRIPT
    echo ===============================
    echo Lihat isi file error.log:
    type error.log
    echo.
    pause
    exit /b 1
)

echo.
echo [SELESAI] Script berhasil dijalankan.
pause
exit /b 0
