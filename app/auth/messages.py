from app import mail
from flask_mail import Message
from flask import render_template
from jwt import encode

def auth_mail(email,next_page=None):
    msg = Message(subject="Поддтвердите почту",recipients=[email])
    token = encode({"email":email},key="secret",algorithm="HS256")
    msg.html = render_template("auth/auth_mail.html",token=token,next_page=next_page)
    mail.send(msg)