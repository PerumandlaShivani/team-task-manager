from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-here')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///team_task_manager.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'jwt-secret-string')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)

db = SQLAlchemy(app)
jwt = JWTManager(app)
CORS(app)
migrate = Migrate(app, db)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default='member')  # 'admin' or 'member'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    projects_created = db.relationship('Project', backref='creator', lazy=True)
    project_memberships = db.relationship('ProjectMember', backref='user', lazy=True)
    assigned_tasks = db.relationship('Task', backref='assignee', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    members = db.relationship('ProjectMember', backref='project', lazy=True, cascade='all, delete-orphan')
    tasks = db.relationship('Task', backref='project', lazy=True, cascade='all, delete-orphan')

class ProjectMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    role = db.Column(db.String(20), default='member')  # 'admin' or 'member'
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    __table_args__ = (db.UniqueConstraint('project_id', 'user_id'),)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default='todo')  # 'todo', 'in_progress', 'completed'
    priority = db.Column(db.String(10), default='medium')  # 'low', 'medium', 'high'
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    assigned_to = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    due_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Routes
@app.route('/api/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 400
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already exists'}), 400
    
    user = User(
        username=data['username'],
        email=data['email'],
        role=data.get('role', 'member')
    )
    user.set_password(data['password'])
    
    db.session.add(user)
    db.session.commit()
    
    access_token = create_access_token(identity=user.id)
    
    return jsonify({
        'message': 'User created successfully',
        'access_token': access_token,
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': user.role
        }
    }), 201

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    
    user = User.query.filter_by(username=data['username']).first()
    
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify({
            'access_token': access_token,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'role': user.role
            }
        })
    
    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/api/projects', methods=['GET'])
@jwt_required()
def get_projects():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    # Get projects where user is creator or member
    projects = Project.query.filter(
        (Project.created_by == user_id) |
        (Project.members.any(user_id=user_id))
    ).all()
    
    result = []
    for project in projects:
        project_data = {
            'id': project.id,
            'name': project.name,
            'description': project.description,
            'created_by': project.created_by,
            'creator_name': project.creator.username,
            'created_at': project.created_at.isoformat(),
            'updated_at': project.updated_at.isoformat(),
            'member_count': len(project.members),
            'task_count': len(project.tasks)
        }
        result.append(project_data)
    
    return jsonify(result)

@app.route('/api/projects', methods=['POST'])
@jwt_required()
def create_project():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    project = Project(
        name=data['name'],
        description=data.get('description', ''),
        created_by=user_id
    )
    
    db.session.add(project)
    db.session.commit()
    
    # Add creator as admin member
    member = ProjectMember(
        project_id=project.id,
        user_id=user_id,
        role='admin'
    )
    db.session.add(member)
    db.session.commit()
    
    return jsonify({
        'id': project.id,
        'name': project.name,
        'description': project.description,
        'created_by': project.created_by,
        'created_at': project.created_at.isoformat()
    }), 201

@app.route('/api/projects/<int:project_id>', methods=['GET'])
@jwt_required()
def get_project(project_id):
    user_id = get_jwt_identity()
    
    # Check if user has access to this project
    project = Project.query.filter(
        (Project.id == project_id) &
        ((Project.created_by == user_id) | (Project.members.any(user_id=user_id)))
    ).first()
    
    if not project:
        return jsonify({'error': 'Project not found'}), 404
    
    # Get project members
    members = []
    for member in project.members:
        members.append({
            'id': member.user.id,
            'username': member.user.username,
            'email': member.user.email,
            'role': member.role,
            'joined_at': member.joined_at.isoformat()
        })
    
    # Get project tasks
    tasks = []
    for task in project.tasks:
        tasks.append({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'priority': task.priority,
            'assigned_to': task.assigned_to,
            'assignee_name': task.assignee.username if task.assignee else None,
            'due_date': task.due_date.isoformat() if task.due_date else None,
            'created_at': task.created_at.isoformat()
        })
    
    return jsonify({
        'id': project.id,
        'name': project.name,
        'description': project.description,
        'created_by': project.created_by,
        'creator_name': project.creator.username,
        'created_at': project.created_at.isoformat(),
        'updated_at': project.updated_at.isoformat(),
        'members': members,
        'tasks': tasks
    })

@app.route('/api/projects/<int:project_id>/tasks', methods=['POST'])
@jwt_required()
def create_task(project_id):
    user_id = get_jwt_identity()
    data = request.get_json()
    
    # Check if user has access to this project
    project = Project.query.filter(
        (Project.id == project_id) &
        ((Project.created_by == user_id) | (Project.members.any(user_id=user_id)))
    ).first()
    
    if not project:
        return jsonify({'error': 'Project not found'}), 404
    
    # Parse due_date if provided
    due_date = None
    if data.get('due_date'):
        due_date = datetime.fromisoformat(data['due_date'].replace('Z', '+00:00'))
    
    task = Task(
        title=data['title'],
        description=data.get('description', ''),
        status=data.get('status', 'todo'),
        priority=data.get('priority', 'medium'),
        project_id=project_id,
        assigned_to=data.get('assigned_to'),
        created_by=user_id,
        due_date=due_date
    )
    
    db.session.add(task)
    db.session.commit()
    
    return jsonify({
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'status': task.status,
        'priority': task.priority,
        'project_id': task.project_id,
        'assigned_to': task.assigned_to,
        'due_date': task.due_date.isoformat() if task.due_date else None,
        'created_at': task.created_at.isoformat()
    }), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
@jwt_required()
def update_task(task_id):
    user_id = get_jwt_identity()
    data = request.get_json()
    
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    # Check if user has access to this task's project
    project_access = Project.query.filter(
        (Project.id == task.project_id) &
        ((Project.created_by == user_id) | (Project.members.any(user_id=user_id)))
    ).first()
    
    if not project_access:
        return jsonify({'error': 'Access denied'}), 403
    
    # Update task fields
    if 'title' in data:
        task.title = data['title']
    if 'description' in data:
        task.description = data['description']
    if 'status' in data:
        task.status = data['status']
    if 'priority' in data:
        task.priority = data['priority']
    if 'assigned_to' in data:
        task.assigned_to = data['assigned_to']
    if 'due_date' in data and data['due_date']:
        task.due_date = datetime.fromisoformat(data['due_date'].replace('Z', '+00:00'))
    elif 'due_date' in data and data['due_date'] is None:
        task.due_date = None
    
    task.updated_at = datetime.utcnow()
    db.session.commit()
    
    return jsonify({
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'status': task.status,
        'priority': task.priority,
        'assigned_to': task.assigned_to,
        'assignee_name': task.assignee.username if task.assignee else None,
        'due_date': task.due_date.isoformat() if task.due_date else None,
        'updated_at': task.updated_at.isoformat()
    })

@app.route('/api/dashboard', methods=['GET'])
@jwt_required()
def get_dashboard():
    user_id = get_jwt_identity()
    
    # Get user's projects
    projects = Project.query.filter(
        (Project.created_by == user_id) |
        (Project.members.any(user_id=user_id))
    ).all()
    
    # Get user's tasks
    tasks = Task.query.filter(
        (Task.assigned_to == user_id) |
        (Task.created_by == user_id)
    ).all()
    
    # Calculate statistics
    total_projects = len(projects)
    total_tasks = len(tasks)
    completed_tasks = len([t for t in tasks if t.status == 'completed'])
    in_progress_tasks = len([t for t in tasks if t.status == 'in_progress'])
    todo_tasks = len([t for t in tasks if t.status == 'todo'])
    
    # Get overdue tasks
    now = datetime.utcnow()
    overdue_tasks = []
    for task in tasks:
        if task.due_date and task.due_date < now and task.status != 'completed':
            overdue_tasks.append({
                'id': task.id,
                'title': task.title,
                'project_name': task.project.name,
                'due_date': task.due_date.isoformat(),
                'days_overdue': (now - task.due_date).days
            })
    
    # Get recent tasks
    recent_tasks = []
    for task in sorted(tasks, key=lambda x: x.created_at, reverse=True)[:5]:
        recent_tasks.append({
            'id': task.id,
            'title': task.title,
            'project_name': task.project.name,
            'status': task.status,
            'priority': task.priority,
            'created_at': task.created_at.isoformat()
        })
    
    return jsonify({
        'stats': {
            'total_projects': total_projects,
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'in_progress_tasks': in_progress_tasks,
            'todo_tasks': todo_tasks
        },
        'overdue_tasks': overdue_tasks,
        'recent_tasks': recent_tasks
    })

@app.route('/api/projects/<int:project_id>/members', methods=['POST'])
@jwt_required()
def add_project_member(project_id):
    user_id = get_jwt_identity()
    data = request.get_json()
    
    # Check if user is admin of this project
    project = Project.query.filter(
        (Project.id == project_id) &
        (Project.created_by == user_id)
    ).first()
    
    if not project:
        return jsonify({'error': 'Project not found or access denied'}), 404
    
    # Check if user to add exists
    user_to_add = User.query.filter_by(email=data['email']).first()
    if not user_to_add:
        return jsonify({'error': 'User not found'}), 404
    
    # Check if user is already a member
    existing_member = ProjectMember.query.filter_by(
        project_id=project_id,
        user_id=user_to_add.id
    ).first()
    
    if existing_member:
        return jsonify({'error': 'User is already a member'}), 400
    
    # Add member
    member = ProjectMember(
        project_id=project_id,
        user_id=user_to_add.id,
        role=data.get('role', 'member')
    )
    
    db.session.add(member)
    db.session.commit()
    
    return jsonify({
        'id': member.id,
        'user_id': member.user_id,
        'username': user_to_add.username,
        'email': user_to_add.email,
        'role': member.role,
        'joined_at': member.joined_at.isoformat()
    }), 201

@app.route('/')
def index():
    return jsonify({
        'message': 'Team Task Manager API is running',
        'version': '1.0.0',
        'status': 'healthy'
    })

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'database': 'connected'
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
