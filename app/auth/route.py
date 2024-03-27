from app.auth import auth_bp
from app.auth.form import LoginForm
from flask import render_template,flash,redirect,url_for,request,session
from app.auth.messages import auth_mail

@auth_bp.route("/",methods={"GET","POST"})
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if session.get("next_page"):
            auth_mail(email=form.email.data,next_page=session.pop("next_page"))
        else:
            auth_mail(email=form.email.data)
        flash("Проверьте свою почту")
        return redirect(url_for("auth_bp.login"))
    return render_template("auth/login.html",form=form)
