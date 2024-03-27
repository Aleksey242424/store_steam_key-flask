from flask_wtf import FlaskForm
from wtforms import SubmitField,IntegerField,StringField
from wtforms.validators import Length,DataRequired,NumberRange

class PayForm(FlaskForm):
    pay = SubmitField(label='pay')

class CardForm(FlaskForm):
    num_card = StringField(render_kw={"placeholder":"0000 0000 0000 0000"},validators=[Length(0,16),DataRequired()])
    month = StringField(label="MM",render_kw={"placeholder":"MM"},validators=[DataRequired(),Length(0,2)])
    years = StringField(label="YYYY",render_kw={"placeholder":"YYYY"},validators=[DataRequired(),Length(0,4)])
    username = StringField(label="username",render_kw={"placeholder":"username"},validators=[DataRequired(),Length(0,255)])
    cvc = StringField(label="cvc",render_kw={"placeholder":"cvc"},validators=[DataRequired(),Length(3,3)])
    buy = SubmitField(label="buy")