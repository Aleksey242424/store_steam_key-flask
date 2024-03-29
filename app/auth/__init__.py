from flask import Blueprint

auth_bp = Blueprint(name="auth_bp",import_name=__name__,template_folder="templates")

from app.init_g import init_g
init_g(auth_bp)
from app.auth import route