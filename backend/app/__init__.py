from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_object='app.config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_object)
    CORS(app)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    #Register Blueprints
    from app.routes import auth_routes, user_routes, skill_routes, ai_routes
    app.register_blueprint(auth_routes.bp, url_prefix='/api/auth')
    app.register_blueprint(user_routes.bp, url_prefix='/api/user')
    app.register_blueprint(skill_routes.bp, url_prefix='/api/skills')
    app.register_blueprint(ai_routes.bp, url_prefix='/api/ai')
    
    return app