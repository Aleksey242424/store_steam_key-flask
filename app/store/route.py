from app.store import store_bp
from app.store.cache_orders import cache_order
from app.system_db.orders import CRUDOrders
from flask import render_template,request,abort,session
from os import listdir
from config import Config

@store_bp.route("/")
def store():
    session["user_id"] = request.remote_addr
    print(session)
    if request.args.get("page"):
        page = request.args.get("page")
    else:
        page = 1
    orders = CRUDOrders.get(page)
    return render_template("store/store.html",orders=orders)

@store_bp.route("/order/<order_id>")
def order(order_id):
    order = cache_order(session.get("user_id"),order_id)
    
    if not order:
        abort(404)

    images_path = order["images"]
    images_list = listdir(Config.abs_path_static+"\\"+'\\'.join(dir_ for dir_ in images_path.split("/")))
    images_list = [images_path+"/"+image for image in images_list]
    return render_template("store/order.html",order=order,images_list=images_list)