import jwt
from datetime import datetime, timedelta
from flask import current_app


def create_access_token(identity):
    payload = {
        'sub': identity,
        'exp': datetime.utcnow() + timedelta(hours=1)
    }
    return jwt.encode(payload, current_app.config['JWT_SECRET_KEY'], algorithm='HS256')


def decode_token(token):
    try:
        return jwt.decode(token, current_app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
    except Exception:
        return None