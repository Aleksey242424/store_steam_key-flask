from flask import Blueprint,g
from app.form import SearchForm
from os import path


def generate_search(bp:Blueprint):
    @bp.before_app_request
    def generate():
        g.search = SearchForm()
        g.check_exists_image = path.exists
