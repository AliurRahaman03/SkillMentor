from datetime import datetime
from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120))
    password_hash = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    skills = db.relationship('Skill', backref='user', lazy=True)
    learning_paths = db.relationship('LearningPath', backref='user', lazy=True)
    
class Skill(db.Model):
    __tablename__ = 'skills'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    level = db.Column(db.String(20)) # e.g., beginner, intermediate, advanced
    
class LearningPath(db.Model):
    __tablename__ = 'learning_paths'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(200))
    ai_metadata = db.Column(db.JSON)  # original AI JSON from AI service
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    tasks = db.relationship('Task', backref='learning_path', lazy=True)
    
class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    learning_path_id = db.Column(db.Integer, db.ForeignKey('learning_paths.id'))
    name = db.Column(db.String(300))
    week = db.Column(db.Integer)
    completed = db.Column(db.Boolean, default=False)