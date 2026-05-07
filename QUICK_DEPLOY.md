# Quick Deployment Guide

## 🚀 Deploy in 5 Minutes

### Step 1: Install Git (if needed)
Download from: https://git-scm.com/download/win

### Step 2: Push to GitHub
```bash
# Open Command Prompt/PowerShell
cd "c:\Users\91701\OneDrive\Desktop\ethara.ai\team-task-manager"

# Initialize Git
git init
git add .
git commit -m "Initial commit: Team Task Manager"

# Create GitHub repository at https://github.com/new
# Repository name: team-task-manager
# Make it PUBLIC

# Push to GitHub (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/team-task-manager.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy to Railway
1. Go to https://railway.app
2. Login with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select `team-task-manager` repository
5. Click "Deploy Now"

### Step 4: Set Environment Variables
In Railway dashboard → Variables tab:
```
SECRET_KEY=your-super-secret-key-change-this-12345
JWT_SECRET_KEY=your-jwt-secret-change-this-67890
DATABASE_URL=sqlite:///team_task_manager.db
```

### Step 5: Get Live URL
After deployment (2-5 minutes), your app will be live at:
`https://your-app-name.up.railway.app`

## 🎯 Test Your App
1. Register as admin user
2. Create a project
3. Add team members
4. Create and assign tasks
5. Check dashboard

## ✅ Done! Your Team Task Manager is now live!
