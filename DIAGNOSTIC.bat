@echo off
echo ========================================
echo    Team Task Manager - Diagnostic Tool
echo ========================================
echo.

echo [1/5] Checking Python installation...
python --version 2>nul
if errorlevel 1 (
    echo ❌ Python NOT found or not in PATH
    echo 📥 Download from: https://python.org
    echo 💡 After install, RESTART computer
) else (
    echo ✅ Python is installed
    python --version
)

echo.
echo [2/5] Checking Node.js installation...
node --version 2>nul
if errorlevel 1 (
    echo ❌ Node.js NOT found or not in PATH
    echo 📥 Download from: https://nodejs.org
    echo 💡 After install, RESTART computer
) else (
    echo ✅ Node.js is installed
    node --version
)

echo.
echo [3/5] Checking project files...
if exist app.py (
    echo ✅ app.py found
) else (
    echo ❌ app.py NOT found
)

if exist frontend\package.json (
    echo ✅ package.json found
) else (
    echo ❌ package.json NOT found
)

echo.
echo [4/5] Checking virtual environment...
if exist venv (
    echo ✅ Virtual environment exists
) else (
    echo ❌ Virtual environment NOT found
    echo 💡 Creating virtual environment...
    python -m venv venv
    if exist venv (
        echo ✅ Virtual environment created successfully
    ) else (
        echo ❌ Failed to create virtual environment
    )
)

echo.
echo [5/5] Testing manual startup...
echo Testing backend...
if exist venv\Scripts\activate (
    echo ✅ Activation script found
    call venv\Scripts\activate
    echo ✅ Virtual environment activated
    
    echo Installing dependencies...
    pip install -r requirements.txt
    
    echo Starting backend...
    start "Backend Test" cmd /k "python app.py"
    timeout /t 3 >nul
    
    echo Testing backend connection...
    curl http://localhost:5000 2>nul
    if errorlevel 1 (
        echo ❌ Backend not responding on port 5000
    ) else (
        echo ✅ Backend is responding on port 5000
    )
) else (
    echo ❌ Cannot activate virtual environment
)

echo.
echo Testing frontend...
cd frontend
if exist node_modules (
    echo ✅ Node modules exist
) else (
    echo ❌ Node modules missing, installing...
    npm install
)

echo Starting frontend...
start "Frontend Test" cmd /k "npm start"
timeout /t 5 >nul

echo.
echo ========================================
echo    Diagnostic Complete!
echo ========================================
echo.
echo 📱 Open these URLs to test:
echo    Backend: http://localhost:5000
echo    Frontend: http://localhost:3000
echo.
echo 💡 If both URLs work, application is running!
echo 💡 If not, check error messages above.
echo.
pause
