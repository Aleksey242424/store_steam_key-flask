from flask import Blueprint,g
from app.form import SearchForm


def generate_search(bp:Blueprint):
    @bp.before_app_request
    def generate():
        g.search = SearchForm()