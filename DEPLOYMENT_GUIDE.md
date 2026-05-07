# Deployment Guide for Team Task Manager

This guide will help you deploy the Team Task Manager application to Railway and set up the GitHub repository.

## Prerequisites

1. **Git installed** on your system
2. **GitHub account** 
3. **Railway account** (free tier is sufficient)
4. **Credit card** on file with Railway (required for free tier)

## Step 1: Set Up GitHub Repository

1. **Install Git** (if not already installed):
   - Windows: Download from https://git-scm.com/download/win
   - Mac: `brew install git`
   - Linux: `sudo apt-get install git`

2. **Initialize Git Repository**:
   ```bash
   cd team-task-manager
   git init
   git add .
   git commit -m "Initial commit: Team Task Manager full-stack application"
   ```

3. **Create GitHub Repository**:
   - Go to https://github.com
   - Click "New repository"
   - Name: `team-task-manager`
   - Description: `Full-stack team task management application with role-based access`
   - Make it **Public** (required for Railway free tier)
   - Don't initialize with README (we already have one)
   - Click "Create repository"

4. **Push to GitHub**:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/team-task-manager.git
   git branch -M main
   git push -u origin main
   ```

## Step 2: Deploy to Railway

1. **Sign Up/Login to Railway**:
   - Go to https://railway.app
   - Sign up/login with GitHub

2. **Create New Project**:
   - Click "New Project" or "Deploy from GitHub repo"
   - Connect your GitHub account if not already connected
   - Search for and select `team-task-manager` repository
   - Click "Deploy Now"

3. **Configure Environment Variables**:
   - Once deployment starts, click on your project
   - Go to "Variables" tab
   - Add these environment variables:
     ```
     SECRET_KEY=your-very-secure-secret-key-here-change-this
     JWT_SECRET_KEY=your-jwt-secret-key-here-change-this
     DATABASE_URL=sqlite:///team_task_manager.db
     ```

4. **Wait for Deployment**:
   - Railway will automatically detect the Flask app
   - Deployment takes 2-5 minutes
   - You'll see logs in the deployment tab

5. **Get Your Live URL**:
   - Once deployed, click on "Settings" tab
   - Your live URL will be displayed (e.g., `https://your-app-name.up.railway.app`)

## Step 3: Test the Application

1. **Visit Your Live URL**:
   - Open the URL in your browser
   - You should see the Team Task Manager login page

2. **Test Registration**:
   - Click "create a new account"
   - Register as an admin user
   - Verify you can login

3. **Test Core Features**:
   - Create a new project
   - Add team members (they need to register first)
   - Create tasks and assign them
   - Update task status
   - Check the dashboard

## Step 4: Frontend Deployment (Optional)

The current setup serves the React frontend through the Flask backend. For production, you might want to:

1. **Build the React App**:
   ```bash
   cd frontend
   npm run build
   ```

2. **Serve Static Files**:
   - The Flask app is configured to serve the React build files
   - Update the `app.py` to serve from the `build` directory

## Troubleshooting

### Common Issues:

1. **Build Failures**:
   - Check the deployment logs in Railway
   - Ensure all dependencies are in `requirements.txt`
   - Verify Python version compatibility

2. **Database Issues**:
   - Railway uses ephemeral storage by default
   - For production, consider using Railway's PostgreSQL addon
   - Update `DATABASE_URL` environment variable

3. **CORS Issues**:
   - The app includes CORS configuration
   - Ensure the frontend URL is properly configured

4. **Authentication Issues**:
   - Verify JWT secrets are set correctly
   - Check token expiration settings

### Environment Variables for Production:

```bash
SECRET_KEY=generate-a-long-random-string-here
JWT_SECRET_KEY=generate-another-long-random-string-here
DATABASE_URL=postgresql://username:password@host:port/database
FLASK_ENV=production
```

## Production Optimizations

1. **Use PostgreSQL**:
   - Add PostgreSQL addon in Railway
   - Update `DATABASE_URL` accordingly

2. **Enable HTTPS**:
   - Railway provides HTTPS automatically

3. **Add Domain**:
   - You can add a custom domain in Railway settings

4. **Monitor Logs**:
   - Use Railway's logging to monitor application health

## What's Included

✅ **Complete Backend API**:
- User authentication with JWT
- Project management CRUD
- Task management with assignments
- Role-based access control
- Dashboard statistics

✅ **Modern Frontend**:
- React with hooks
- Tailwind CSS for styling
- Responsive design
- Real-time updates

✅ **Database Schema**:
- Users, Projects, Tasks, ProjectMembers
- Proper relationships and constraints
- Role-based permissions

✅ **Deployment Ready**:
- Railway configuration
- Environment variables setup
- Production-ready structure

## Next Steps

1. Follow this guide to deploy your application
2. Test all features thoroughly
3. Consider adding more features like:
   - File attachments
   - Email notifications
   - Advanced filtering and search
   - Team chat/messaging
   - Time tracking

Your Team Task Manager is now ready for deployment! 🚀
