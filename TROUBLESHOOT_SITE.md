# 🔧 Site Can't Be Reached - Troubleshooting Guide

## 🚨 Common Issues & Solutions

### Issue 1: Backend Server Not Starting
**Symptoms:**
- Browser shows "Site can't be reached"
- Frontend loads but shows errors

**Solution:**
```bash
# Check if backend is running
# Look for "Backend Server" terminal window
# Should show: "Running on http://127.0.0.1:5000"

# If not running, start manually:
cd "c:\Users\91701\OneDrive\Desktop\ethara.ai\team-task-manager"
venv\Scripts\activate
python app.py
```

### Issue 2: Port Conflicts
**Symptoms:**
- "Port already in use" error
- Backend or frontend fails to start

**Solution:**
```bash
# Kill processes on ports 3000 and 5000
netstat -ano | findstr :3000
netstat -ano | findstr :5000

# Kill processes (replace PID with actual process ID)
taskkill /PID <PID> /F
```

### Issue 3: Python/Node.js Not in PATH
**Symptoms:**
- "python not found" or "npm not found"
- Batch file fails immediately

**Solution:**
1. **Install Python:** https://python.org
2. **Install Node.js:** https://nodejs.org
3. **Restart computer** after installation

### Issue 4: Virtual Environment Problems
**Symptoms:**
- Module import errors
- Flask not found

**Solution:**
```bash
cd "c:\Users\91701\OneDrive\Desktop\ethara.ai\team-task-manager"

# Delete and recreate venv
rmdir /s /q venv
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Issue 5: Frontend Dependencies Missing
**Symptoms:**
- React compilation errors
- "Module not found" in browser

**Solution:**
```bash
cd "c:\Users\91701\OneDrive\Desktop\ethara.ai\team-task-manager\frontend"
rmdir /s /q node_modules
npm install
npm start
```

## 🔍 Step-by-Step Diagnosis

### Step 1: Check Backend Status
1. Look for "Backend Server" terminal window
2. Should show: `* Running on http://127.0.0.1:5000`
3. If missing, backend isn't running

### Step 2: Check Frontend Status
1. Look for "Frontend Server" terminal window
2. Should show: `Compiled successfully!`
3. Should show: `Local: http://localhost:3000`

### Step 3: Test Individual URLs
1. **Backend Test:** Open http://localhost:5000 in browser
   - Should show "Hello World" or error message
2. **Frontend Test:** Open http://localhost:3000 in browser
   - Should show React app or error

## 🛠️ Quick Fix Commands

### Reset Everything:
```batch
@echo off
cd /d "c:\Users\91701\OneDrive\Desktop\ethara.ai\team-task-manager"

echo Stopping all processes...
taskkill /f /im python.exe 2>nul
taskkill /f /im node.exe 2>nul

echo Cleaning up...
rmdir /s /q venv 2>nul
rmdir /s /q frontend\node_modules 2>nul

echo Rebuilding...
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt

cd frontend
npm install
cd ..

echo Starting fresh...
start "Backend" cmd /k "call venv\Scripts\activate && python app.py"
cd frontend
start "Frontend" cmd /k "npm start"

echo Done! Check both terminal windows.
pause
```

## 📱 Manual Start (If Auto-Start Fails)

### Backend Only:
```bash
cd "c:\Users\91701\OneDrive\Desktop\ethara.ai\team-task-manager"
venv\Scripts\activate
python app.py
```

### Frontend Only:
```bash
cd "c:\Users\91701\OneDrive\Desktop\ethara.ai\team-task-manager\frontend"
npm start
```

## 🎯 What Should Work

1. **Backend terminal shows:** `* Running on http://127.0.0.1:5000`
2. **Frontend terminal shows:** `Compiled successfully!` and `Local: http://localhost:3000`
3. **Browser opens to:** http://localhost:3000
4. **Login page appears** without errors

## 🚨 If Still Not Working

### Check Windows Firewall:
1. Open Windows Defender Firewall
2. Allow Python and Node.js through firewall
3. Add ports 3000 and 5000 as exceptions

### Check Antivirus:
1. Temporarily disable antivirus
2. Try running the application
3. Re-enable after testing

### Try Different Browser:
- Chrome, Firefox, Edge, or Safari
- Clear browser cache first

## 📞 Last Resort

If nothing works:
1. Restart your computer
2. Run QUICK_START.bat again
3. Check for Windows updates

**The issue is usually one of these common problems!** 🔧
