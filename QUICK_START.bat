@echo off
echo Starting Team Task Manager...
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found. Please install Python from https://python.org
    echo Then run this file again.
    pause
    exit /b
)

REM Check if Node.js is available
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js not found. Please install Node.js from https://nodejs.org
    echo Then run this file again.
    pause
    exit /b
)

echo Step 1: Setting up Python environment...
cd /d "c:\Users\91701\OneDrive\Desktop\ethara.ai\team-task-manager"

if not exist venv (
    python -m venv venv
    echo Virtual environment created
)

call venv\Scripts\activate
pip install -r requirements.txt >nul 2>&1
if not exist .env (
    copy .env.example .env >nul
    echo Environment file created
)

echo Step 2: Starting Backend Server...
start "Backend Server" cmd /k "call venv\Scripts\activate && python app.py"

echo Step 3: Starting Frontend Server...
cd frontend
if not exist node_modules (
    npm install >nul 2>&1
    echo Frontend dependencies installed
)
start "Frontend Server" cmd /k "npm start"

echo.
echo ========================================
echo Team Task Manager is starting...
echo.
echo Backend: http://localhost:5000
echo Frontend: http://localhost:3000
echo.
echo Opening application in browser...
timeout /t 5 >nul
start http://localhost:3000
echo.
echo Press any key to close this window...
pause >nul
