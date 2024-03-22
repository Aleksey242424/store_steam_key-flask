from flask import Blueprint

store_bp = Blueprint("store_bp",__name__,template_folder="templates")

from app.route import generate_search
generate_search(store_bp)

from app.store import route

