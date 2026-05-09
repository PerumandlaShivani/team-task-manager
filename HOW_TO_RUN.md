# 🚀 How to Execute Team Task Manager

## Prerequisites
- Python 3.8+ installed
- Node.js 14+ installed
- Git installed

## Step 1: Backend Setup

### 1.1 Create Virtual Environment
```bash
cd "c:\Users\91701\OneDrive\Desktop\ethara.ai\team-task-manager"

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
# source venv/bin/activate
```

### 1.2 Install Python Dependencies
```bash
# Make sure virtual environment is activated
pip install -r requirements.txt
```

### 1.3 Set Environment Variables
```bash
# Copy environment template
copy .env.example .env

# Edit .env file with your secrets
# SECRET_KEY=your-secret-key-here
# JWT_SECRET_KEY=jwt-secret-string
# DATABASE_URL=sqlite:///team_task_manager.db
```

### 1.4 Start Backend Server
```bash
# Make sure you're in team-task-manager directory
python app.py
```

Backend will start at: **http://localhost:5000**

## Step 2: Frontend Setup

### 2.1 Install Node.js Dependencies
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install
```

### 2.2 Start Frontend Development Server
```bash
# Still in frontend directory
npm start
```

Frontend will start at: **http://localhost:3000**

## Step 3: Access Your Application

### Main Application URL
```
http://localhost:3000
```

### API Endpoints (for testing)
```
http://localhost:5000/api/auth/register
http://localhost:5000/api/auth/login
http://localhost:5000/api/projects
http://localhost:5000/api/dashboard
```

## Step 4: Test the Application

### 4.1 Register First User
1. Open http://localhost:3000
2. Click "create a new account"
3. Fill in:
   - Username: admin
   - Email: admin@example.com
   - Password: password123
   - Role: admin
4. Click "Create account"

### 4.2 Login and Test
1. Login with your credentials
2. You'll see the dashboard
3. Create a project
4. Add team members
5. Create and assign tasks

## Step 5: Common Issues & Solutions

### Backend Issues:
**"Module not found" errors:**
```bash
# Make sure virtual environment is activated
venv\Scripts\activate
pip install -r requirements.txt
```

**"Python not found":**
- Install Python from https://python.org
- Add Python to PATH during installation

### Frontend Issues:
**"npm not found":**
- Install Node.js from https://nodejs.org

**Port already in use:**
```bash
# Kill processes on ports 3000 and 5000
netstat -ano | findstr :3000
netstat -ano | findstr :5000
# Kill the process using its PID
taskkill /PID <PID_NUMBER> /F
```

## Step 6: Quick Start Commands

### All-in-One (Windows):
```batch
@echo off
cd "c:\Users\91701\OneDrive\Desktop\ethara.ai\team-task-manager"

echo Starting Backend...
start cmd /k "venv\Scripts\activate && python app.py"

echo Starting Frontend...
cd frontend
start cmd /k "npm start"

echo Both servers starting...
echo Backend: http://localhost:5000
echo Frontend: http://localhost:3000
pause
```

## Step 7: Database

The application uses SQLite by default:
- Database file: `team_task_manager.db`
- Created automatically on first run
- No additional setup required

## Step 8: Production Deployment

Once tested locally, deploy to Railway:
1. Push to GitHub (already done)
2. Deploy to Railway: https://railway.app
3. Set environment variables
4. Get live URL

## 🎯 Success!

Your Team Task Manager is now running locally at:
- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:5000

Ready for testing and development! 🚀
