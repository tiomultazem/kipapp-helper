@echo off
set msg=%*

:: ===== 1. Jalankan builder =====
python builder.py
timeout /t 2 >nul

:: ===== 2. Commit ke Git BPS (SEMUA FILE) dari v3 =====
git add .
git commit -m "%msg%"
git push bps main

:: ===== 3.Copy ke public =====
python public.py
timeout /t 2 >nul

:: ===== 3.2 Commit ke GitHub dari public/ (TIDAK salin file) =====
cd /d "..\public"
git add .
git commit -m "%msg%"
git push origin main

:: ===== 4. balik lagi ke v3
cd /d "..\v3"