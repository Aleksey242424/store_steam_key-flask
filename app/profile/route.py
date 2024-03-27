from app.profile import profile_bp
from jwt import decode,encode
from app.system_db.users import CRUDUsers
from app.system_db.pay_users import CRUDPayUsers
from app.system_db.comments import CRUDComments
from flask import session,render_template,redirect,url_for,request
from app.cache_orders import get_user_buy,get_order_by_id
from app.profile.form import CommentsForm,UpdateComment,ChangeName


@profile_bp.route("/<token>",methods=["GET","POST"])
def profile(token):
    if not session.get("email"):
        
        email = decode(token,key="secret",algorithms=["HS256"])
        email = email["email"]
        CRUDUsers.add(email)
        user_id = CRUDUsers.get_user_id(email)
        if user_id:
            session["auth_id"] = user_id
            session["email"] = email
        else:
            return redirect(url_for('auth_bp.login'))
        if request.args.get("next_page"):
            return redirect(request.args.get("next_page"))
    buy_order = CRUDPayUsers.get(session.get("auth_id"))
    orders = [get_user_buy(order_id.order_id,order_id.steam_key) for order_id in buy_order][::-1]
    return render_template("profile/profile.html",orders=orders,token=token)

@profile_bp.route("/<token>/buy_order/<order_id>/<steam_key>",methods=["GET","POST"])
def buy_order(order_id,steam_key,token):
    if session.get("auth_id"):
        user_comment = CRUDComments.get_user_comment(session.get('auth_id'),order_id)
        form_comment = CommentsForm()
        form_update = UpdateComment()
        form_username = ChangeName()
        
        if request.method == "POST":
            if request.form.get("send_comment"):
                comment = form_comment.comment.data
                CRUDComments.add(comment=comment,user_id=session.get("auth_id"),order_id=order_id)
            elif request.form.get("update_comment"):
                CRUDComments.update(user_id=session.get('auth_id'),order_id=order_id,comment=form_update.comment.data)
            elif request.form.get("update"):
                CRUDUsers.update_username(session.get("auth_id"),form_username.username.data)
            return redirect(url_for('profile_bp.buy_order',
                                    token=token,
                                    steam_key=steam_key,
                                    order_id=order_id))
        order = get_order_by_id(order_id)
        steam_key_dec = decode(steam_key,key="secret",algorithms=["HS256"])
        comments = CRUDComments.get(order_id)[::-1]
        form_username.username.data = CRUDUsers.get_username(session.get("auth_id"))
        return render_template("profile/buy_order.html",
                            order=order,
                            steam_key=steam_key,
                            steam_key_dec=steam_key_dec,
                            form_comment=form_comment,
                            token=token,
                            order_id=order_id,
                            comments=comments,
                            user_comment = user_comment,
                            form_update=form_update,
                            form_username=form_username)
    return redirect(url_for('auth_bp.login'))