# 🚀 Get Your Live URL - 5 Minute Guide

## Step 1: Install Git (if not installed)
Download from: https://git-scm.com/download/win

## Step 2: Create GitHub Repository
1. Go to https://github.com/new
2. Repository name: `team-task-manager`
3. Make it **PUBLIC** (required for Railway free tier)
4. Don't initialize with README
5. Click "Create repository"

## Step 3: Push Code to GitHub
Open Command Prompt/PowerShell and run:
```bash
cd "c:\Users\91701\OneDrive\Desktop\ethara.ai\team-task-manager"

git init
git add .
git commit -m "Initial commit: Team Task Manager"

git remote add origin https://github.com/YOUR_USERNAME/team-task-manager.git
git branch -M main
git push -u origin main
```
*(Replace YOUR_USERNAME with your GitHub username)*

## Step 4: Deploy to Railway
1. Go to https://railway.app
2. Click "Login with GitHub"
3. Click "New Project" → "Deploy from GitHub repo"
4. Select `team-task-manager` repository
5. Click "Deploy Now"

## Step 5: Set Environment Variables
In Railway dashboard → Variables tab, add:
```
SECRET_KEY=your-super-secret-key-change-this-12345
JWT_SECRET_KEY=your-jwt-secret-change-this-67890
DATABASE_URL=sqlite:///team_task_manager.db
```

## Step 6: Get Your Live URL
After deployment (2-5 minutes):
1. Go to your Railway project
2. Click "Settings" tab
3. Your live URL will be displayed (e.g., `https://team-task-manager-production.up.railway.app`)

## 🎯 Your Live URL Format:
```
https://[your-app-name].up.railway.app
```

## ✅ Test Your Live App
1. Open the URL in browser
2. Register as admin user
3. Create project and test all features

## 📞 Need Help?
- Check Railway deployment logs if issues occur
- Ensure environment variables are set correctly
- Verify GitHub repository is PUBLIC

**Your live URL will be ready in 5-10 minutes!** 🚀
