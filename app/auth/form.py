from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,SubmitField
from wtforms.validators import Email,DataRequired


class LoginForm(FlaskForm):
    email = EmailField(label="email",render_kw={"placeholder":"email"},validators=[DataRequired(),Email()])
    login = SubmitField(label="Войти")