# 🚀 Push to GitHub: perumandlashivani

## Step 1: Create GitHub Repository
1. Go to https://github.com/new
2. Repository name: `team-task-manager`
3. Make it **PUBLIC** (required for Railway)
4. Don't initialize with README
5. Click "Create repository"

## Step 2: Push Code to Your GitHub
Open Command Prompt/PowerShell and run these commands:

```bash
# Navigate to project directory
cd "c:\Users\91701\OneDrive\Desktop\ethara.ai\team-task-manager"

# Initialize Git repository
git init

# Add all files
git add .

# Make initial commit
git commit -m "Initial commit: Team Task Manager full-stack application"

# Add your GitHub repository
git remote add origin https://github.com/perumandlashivani/team-task-manager.git

# Set main branch
git branch -M main

# Push to GitHub
git push -u origin main
```

## Step 3: Verify Repository
Your project will be available at:
```
https://github.com/perumandlashivani/team-task-manager
```

## Step 4: Deploy to Railway
1. Go to https://railway.app
2. Login with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select `team-task-manager` repository
5. Click "Deploy Now"

## Step 5: Set Environment Variables
In Railway dashboard → Variables tab:
```
SECRET_KEY=your-super-secret-key-change-this-12345
JWT_SECRET_KEY=your-jwt-secret-change-this-67890
DATABASE_URL=sqlite:///team_task_manager.db
```

## Step 6: Get Live URL
After deployment (2-5 minutes), your app will be live at:
```
https://team-task-manager-production.up.railway.app
```

## ✅ Ready for Demo!
Once deployed, you'll have:
- **GitHub Repo**: https://github.com/perumandlashivani/team-task-manager
- **Live App URL**: https://team-task-manager-production.up.railway.app

Both ready for your demo! 🎉
