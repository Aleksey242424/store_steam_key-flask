from flask import Blueprint

profile_bp = Blueprint(name="profile_bp",import_name=__name__,template_folder="templates")

from app.init_g import init_g
init_g(profile_bp)

from app.profile import route