from flask import Blueprint

auth_bp = Blueprint(name="auth_bp",import_name=__name__,template_folder="templates")

from app.auth import route