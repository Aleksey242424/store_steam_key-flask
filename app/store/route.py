from app.store import store_bp
from app.store.cache_orders import cache_order,get_orders,get_orders_by_id
from app.system_db.orders import CRUDOrders
from flask import render_template,request,abort,session,g,redirect,url_for
from os import listdir
from config import Config

@store_bp.route("/",methods={"GET","POST"})
def store():
    search_form = getattr(g,"search",None)
    if search_form.validate_on_submit():
        search = search_form.search.data
        search_form.search.data = ''
        return redirect(url_for("store_bp.search_orders",search=search))
    session["user_id"] = request.remote_addr
    if request.args.get("page"):
        page = request.args.get("page")
    else:
        page = 1
    orders = get_orders(page)
    
    return render_template("store/store.html",orders=orders,search_form=search_form)

@store_bp.route("/orders/<search>",methods={'GET',"POST"})
def search_orders(search):
    search_form = getattr(g,"search",None)
    if search_form.validate_on_submit():
        search = search_form.search.data
        search_form.search.data = ''
        return redirect(url_for("store_bp.search_orders",search=search))
    orders_id = CRUDOrders.search_orders(search)
    orders = get_orders_by_id(orders_id)
    count_orders =  len(orders)
    return render_template("store/search_orders.html",
                           search=search,
                           orders_id=orders_id,
                           orders=orders,
                           search_form=search_form,
                           count_orders = count_orders)

@store_bp.route("/order/<order_id>",methods={'GET','POST'})
def order(order_id):
    search_form = getattr(g,"search",None)
    if search_form.validate_on_submit():
        search = search_form.search.data
        search_form.search.data = ''
        return redirect(url_for("store_bp.search_orders",search=search))
    order = cache_order(session.get("user_id"),order_id)
    if not order:
        abort(404)
    images_path = order["images"]
    try:
        images_list = listdir(Config.abs_path_static+"\\"+'\\'.join(dir_ for dir_ in images_path.split("/")))
    except FileNotFoundError:
        images_list = []
    images_list = [images_path+"/"+image for image in images_list]
    return render_template("store/order.html",
                           order=order,
                           images_list=images_list,
                           search_form=search_form)