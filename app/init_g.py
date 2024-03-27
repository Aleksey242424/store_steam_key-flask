from flask import Blueprint,g
from app.form import SearchForm
from os import path
from app.cache_orders import get_count_order
from jwt import encode

def generate_search(bp:Blueprint):
    @bp.before_app_request
    def generate():
        g.search = SearchForm()
        g.check_exists_image = path.exists
        g.order_count = get_count_order
        g.generate_token = generate_token

def generate_token(name,value):
    try:
        token = encode({name:value},key="secret",algorithm="HS256")
        return token
    except TypeError:
        return
    