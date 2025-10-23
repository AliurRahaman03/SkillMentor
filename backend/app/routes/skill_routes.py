from flask import Blueprint, request, jsonify
from app import db
from app.models import Skill


bp = Blueprint('skill_routes', __name__)


@bp.route('/', methods=['GET'])
def get_skills():
    user_id = request.args.get('user_id')
    skills = Skill.query.filter_by(user_id=user_id).all()
    return jsonify([{'id': s.id, 'name': s.name, 'level': s.level} for s in skills])


@bp.route('/', methods=['POST'])
def add_skill():
    data = request.json
    skill = Skill(user_id=data['user_id'], name=data['name'], level=data['level'])
    db.session.add(skill)
    db.session.commit()
    return jsonify({'message': 'Skill added'}), 201