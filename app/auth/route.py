from app.auth import auth_bp
from flask import render_template

@auth_bp.route("/")
def login():
    return render_template("auth/login.html")