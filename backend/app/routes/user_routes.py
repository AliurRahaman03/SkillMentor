from flask import Blueprint, request, jsonify
from app import db
from app.models import User


bp = Blueprint('user_routes', __name__)


@bp.route('/', methods=['GET'])
def get_user():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'user_id query parameter required'}), 400
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email}), 200


@bp.route('/', methods=['POST'])
def create_user():
    data = request.json or {}
    name = data.get('name')
    email = data.get('email')
    if not email:
        return jsonify({'error': 'email is required'}), 400
    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id}), 201
