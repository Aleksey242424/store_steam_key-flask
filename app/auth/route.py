from app.auth import auth_bp
from app.auth.form import LoginForm
from flask import render_template,flash,redirect,url_for,request,session,g
from app.auth.messages import auth_mail

@auth_bp.route("/",methods={"GET","POST"})
def login():
    form = LoginForm()
    form_search = g.get("search",None)
    if form.validate_on_submit() or form_search.validate_on_submit():
        if request.form.get("send"):
            search = form_search.search.data
            form_search.search.data = ''
            return redirect(url_for("store_bp.search_orders",search=search)) 
        elif request.form.get("login"):
            if session.get("next_page"):
                auth_mail(email=form.email.data,next_page=session.pop("next_page"))
            else:
                auth_mail(email=form.email.data)
            flash("Проверьте свою почту")
            return redirect(url_for("auth_bp.login"))
    if form.errors:
        flash("Данные не коректны")
    return render_template("auth/login.html",form=form,search_form=form_search)
