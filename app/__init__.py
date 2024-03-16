from flask import Flask
from config import Config

def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)
    from app.auth import auth_bp
    from app.store import store_bp
    app.register_blueprint(auth_bp,url_prefix="/auth/")
    app.register_blueprint(store_bp,url_prefix="/")
    return app