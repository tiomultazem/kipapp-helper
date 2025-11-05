@echo off
setlocal
cd /d "%~dp0"
chcp 65001 >nul

python src\gui.py || py src\gui.py
