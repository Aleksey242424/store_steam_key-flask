from flask import Blueprint

auth_bp = Blueprint("auth_bp",__name__,template_folder="templates")

from app.auth import route