@echo off
setlocal enabledelayedexpansion

:: Nama direktori dan environment
set BASEDIR=%~dp0
set CONDADIR=%BASEDIR%miniconda
set ENVNAME=myenv
set PYEXE=%CONDADIR%\envs\%ENVNAME%\python.exe

:: Cek apakah environment sudah dibuat
if exist "%PYEXE%" (
    echo Miniconda environment sudah ada.
    goto RUN
)

echo Mengunduh Miniconda...
bitsadmin /transfer downloadConda /priority high https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe "%BASEDIR%miniconda-installer.exe"

if not exist "%BASEDIR%miniconda-installer.exe" (
    echo Gagal mengunduh Miniconda installer.
    pause
    exit /b
)

echo Menginstal Miniconda secara silent...
"%BASEDIR%miniconda-installer.exe" /InstallationType=JustMe /AddToPath=0 /RegisterPython=0 /S /D=%CONDADIR%

if not exist "%CONDADIR%\Scripts\conda.exe" (
    echo Gagal menginstal Miniconda.
    pause
    exit /b
)

echo Menyetujui Terms of Service...
call "%CONDADIR%\Scripts\conda.exe" tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
call "%CONDADIR%\Scripts\conda.exe" tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
call "%CONDADIR%\Scripts\conda.exe" tos accept --override-channels --channel https://repo.anaconda.com/pkgs/msys2

echo Membuat environment dengan Python 3.12.7...
call "%CONDADIR%\Scripts\activate.bat"
call "%CONDADIR%\Scripts\conda.exe" create -y -n %ENVNAME% python=3.12.7

if not exist "%PYEXE%" (
    echo Gagal membuat environment.
    pause
    exit /b
)

:RUN
echo Menjalankan main.py...
call "%CONDADIR%\Scripts\activate.bat" %ENVNAME%
"%PYEXE%" -m pip install --upgrade pip
"%PYEXE%" -m pip install -r "%BASEDIR%requirements.txt" 2>nul
"%PYEXE%" "%BASEDIR%main.py"

pause
