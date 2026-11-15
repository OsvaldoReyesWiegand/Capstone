@echo off
title Sistema Predictivo Capstone
echo ===================================================
echo   SISTEMA DE REABASTECIMIENTO TEXTIL - INICIANDO...
echo ===================================================
echo.
echo 1. Levantando Motor de Inteligencia Artificial (API)...
start cmd /k "uvicorn api_reabastecimiento:app --reload"

echo Esperando 4 segundos para sincronizar puertos...
timeout /t 4 /nobreak > NUL

echo 2. Levantando Plataforma Web (Streamlit)...
start cmd /k "streamlit run app_web.py"