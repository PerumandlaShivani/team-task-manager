@echo off
echo Pushing Team Task Manager to GitHub...
echo.

REM Navigate to project directory
cd /d "c:\Users\91701\OneDrive\Desktop\ethara.ai\team-task-manager"

REM Initialize Git
echo Initializing Git repository...
git init

REM Add all files
echo Adding files...
git add .

REM Make initial commit
echo Creating initial commit...
git commit -m "Initial commit: Team Task Manager full-stack application"

REM Add your GitHub repository
echo Adding remote repository...
git remote add origin https://github.com/perumandlashivani/team-task-manager.git

REM Set main branch
git branch -M main

REM Push to GitHub
echo Pushing to GitHub...
git push -u origin main

echo.
echo ✅ Successfully pushed to GitHub!
echo Repository: https://github.com/perumandlashivani/team-task-manager
echo.
pause
