from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models import User
from app.auth import create_access_token


bp = Blueprint('auth_routes', __name__)


@bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    hashed = generate_password_hash(data['password'])
    user = User(name=data['name'], email=data['email'], password_hash=hashed)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201


@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password_hash, data['password']):
        token = create_access_token(user.id)
        return jsonify({'access_token': token}), 200
    return jsonify({'error': 'Invalid credentials'}), 401