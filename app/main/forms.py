from flask_pagedown.fields import PageDownField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('姓名：', validators=[DataRequired()])
    submit = SubmitField('提交')
class PostForm(FlaskForm):
    body = PageDownField('What\'s on your mind?', validators=[DataRequired()])
    submit = SubmitField('Submit')