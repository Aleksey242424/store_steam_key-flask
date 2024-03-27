from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Length

class CommentsForm(FlaskForm):
    comment = StringField(label='comment',render_kw={"placeholder":"comment"},validators=[DataRequired(),Length(0,2500)])
    send_comment = SubmitField(label='send')

class UpdateComment(FlaskForm):
    comment = StringField(label='comment',render_kw={"placeholder":"comment"},validators=[DataRequired(),Length(0,2500)])
    update_comment = SubmitField(label='update')

class ChangeName(FlaskForm):
    username = StringField(label="change_name",render_kw={"placeholder":"username"},validators=[DataRequired(),Length(0,255)])
    update = SubmitField(label='Изменить')