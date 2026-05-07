# Team Task Manager

A full-stack web application for team collaboration and task management with role-based access control.

## Features

- **Authentication**: User signup and login with JWT tokens
- **Project Management**: Create and manage projects with team members
- **Task Management**: Create, assign, and track tasks with status updates
- **Role-Based Access**: Admin and Member roles with appropriate permissions
- **Dashboard**: Overview of projects, tasks, and overdue items
- **Real-time Updates**: Task status tracking and team collaboration

## Tech Stack

### Backend
- **Flask**: Python web framework
- **SQLAlchemy**: ORM for database operations
- **JWT**: Authentication tokens
- **SQLite**: Database (easily switchable to PostgreSQL/MySQL)

### Frontend
- **React**: User interface library
- **React Router**: Client-side routing
- **Tailwind CSS**: Utility-first CSS framework
- **Lucide React**: Icon library
- **Axios**: HTTP client for API calls

## Installation

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm or yarn

### Backend Setup

1. Navigate to the project directory:
```bash
cd team-task-manager
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your secret keys
```

5. Initialize the database:
```bash
python app.py
```

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

## Usage

1. Start the backend server:
```bash
python app.py
```

2. Start the frontend development server:
```bash
cd frontend && npm start
```

3. Open your browser and navigate to `http://localhost:3000`

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login user

### Projects
- `GET /api/projects` - Get user's projects
- `POST /api/projects` - Create new project
- `GET /api/projects/:id` - Get project details
- `POST /api/projects/:id/members` - Add project member

### Tasks
- `POST /api/projects/:id/tasks` - Create new task
- `PUT /api/tasks/:id` - Update task

### Dashboard
- `GET /api/dashboard` - Get dashboard statistics

## Database Schema

### Users
- id, username, email, password_hash, role, created_at

### Projects
- id, name, description, created_by, created_at, updated_at

### Project Members
- id, project_id, user_id, role, joined_at

### Tasks
- id, title, description, status, priority, project_id, assigned_to, created_by, due_date, created_at, updated_at

## Deployment

This application is configured for deployment on Railway:

1. Push your code to GitHub
2. Connect your GitHub repository to Railway
3. Railway will automatically detect the Flask app and deploy it
4. Set environment variables in Railway dashboard

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.
