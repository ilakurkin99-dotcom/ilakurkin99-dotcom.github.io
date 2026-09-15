@echo off
title GTA 5 RP - ТУЛЕВО ЗА РОНАЛДУ
cd /d "%~dp0"
echo ===================================================
echo   Запуск GTA 5 RP Shootout Arena (Three.js)
echo ===================================================

set "REAL_PY=C:\Users\Admin\AppData\Local\Python\bin\python.exe"
if exist "%REAL_PY%" (
    "%REAL_PY%" run.py
) else (
    python run.py
)
pause
