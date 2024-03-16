from flask import Blueprint

store_bp = Blueprint("store_bp",__name__,template_folder="templates")

from app.store import route

