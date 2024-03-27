from app.store import store_bp
from app.cache_orders import (cache_order,get_orders,get_orders_by_id,
                                    get_order_history_list,get_order_by_id,
                                    get_count_group,del_count_orders)
from app.system_db.orders import CRUDOrders
from app.system_db.pay_users import CRUDPayUsers
from flask import (render_template,request,abort,
                   session,g,redirect,url_for,jsonify)
from os import listdir,path
from config import Config
from app.store.form import PayForm,CardForm
from random import choice
from string import ascii_letters

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
    return render_template("store/store.html",
                           orders=orders,
                           search_form=search_form,
                           count_group = get_count_group(),
                           page = int(page),
                           abs_path_img = Config.abs_path_static)

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
                           count_orders = count_orders,
                           abs_path_img = Config.abs_path_static)

@store_bp.route("/register_pay/<order_id>",methods={"GET","POST"})
def register_pay(order_id):
    if request.args.get("data") == '1':
        del_count_orders(order_id)
        user_id = session.get("auth_id")
        steam_key = ''.join(choice(ascii_letters) for i in range(10))
        CRUDPayUsers.add(user_id=user_id,order_id=int(order_id),steam_key=steam_key)
        return jsonify({"response":steam_key})
    return jsonify({"response":0})

@store_bp.route("/order/<int:order_id>/buy",methods={"GET","POST"})
def buy_order(order_id):
    if session.get("auth_id"):
        buy_form = CardForm()
        order = get_order_by_id(order_id)
        return render_template("store/pay.html",order=order,buy_form=buy_form)
    session['next_page'] = request.path
    return redirect(url_for("auth_bp.login"))

@store_bp.route("/order/<order_id>",methods={'GET','POST'})
def order(order_id):
    search_form = getattr(g,"search",None)
    pay_form = PayForm()
    order = cache_order(session.get("user_id"),order_id)
    if not order:
        abort(404)
    images_path = order["images"]

    if not path.exists(Config.abs_path_static + "\\" + order["main_image"]):
        order["main_image"] = "images/orders/default_image.jpg"
    try:
        images_list = listdir(Config.abs_path_static+"\\"+'\\'.join(dir_ for dir_ in images_path.split("/")))
    except FileNotFoundError:
        images_list = []
    images_list = [images_path+"/"+image for image in images_list]

    if request.method == "POST":
        if request.form.get("send") == "search":
            search = search_form.search.data
            search_form.search.data = ''
            return redirect(url_for("store_bp.search_orders",search=search))
        if request.form.get("pay"):
            return redirect(url_for("store_bp.buy_order",order_id=order["order_id"]))
    return render_template("store/order.html",
                           order=order,
                           images_list=images_list,
                           search_form=search_form,
                           form_pay = pay_form)

@store_bp.route("/orders/list_history")
def list_history():
    search_form = getattr(g,"search",None)
    if search_form.validate_on_submit():
        search = search_form.search.data
        search_form.search.data = ''
        return redirect(url_for("store_bp.search_orders",search=search))
    orders = get_order_history_list(request.remote_addr)
    return render_template("store/list_history.html",
                           orders=orders,
                           search_form=search_form,
                           abs_path_img = Config.abs_path_static)

