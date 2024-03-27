from flask import Flask
from flask_mail import Mail
from config import Config

mail = Mail()

def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)
    mail.init_app(app)
    from app.auth import auth_bp
    from app.store import store_bp
    from app.profile import profile_bp
    app.register_blueprint(store_bp,url_prefix="/")
    app.register_blueprint(auth_bp,url_prefix="/auth/")
    app.register_blueprint(profile_bp,url_prefix="/profile/")
    return app