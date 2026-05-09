@echo off
echo ========================================
echo    Team Task Manager - Auto Start
echo ========================================
echo.

echo [1/4] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Python not found. Please install Python from https://python.org
    pause
    exit /b
)

echo [2/4] Activating virtual environment...
call venv\Scripts\activate

echo [3/4] Installing Python dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b
)

echo [4/4] Copying environment file...
if not exist .env (
    copy .env.example .env
    echo Environment file created from template
)

echo.
echo ========================================
echo    Starting Backend Server...
echo    Backend will run on: http://localhost:5000
echo ========================================
echo.

start cmd /k "call venv\Scripts\activate && python app.py"

echo.
echo ========================================
echo    Starting Frontend Server...
echo    Frontend will run on: http://localhost:3000
echo ========================================
echo.

cd frontend
start cmd /k "npm install && npm start"

echo.
echo ========================================
echo    Team Task Manager is starting...
echo    Please wait for servers to load...
echo    
echo    Access your app at: http://localhost:3000
echo ========================================
echo.

timeout /t 10
start http://localhost:3000

echo Press any key to exit this window...
pause
