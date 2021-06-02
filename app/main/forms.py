from flask_pagedown.fields import PageDownField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('姓名：', validators=[DataRequired()])
    submit = SubmitField('提交')


class PostForm(FlaskForm):
    body = PageDownField('What\'s on your mind?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class FindForm(FlaskForm):
    certification = RadioField('certification', choices=[('0', 'SZ'),('1','SH')])
    prompt = StringField('请输入代码', validators=[DataRequired()])
    submit = SubmitField('提交')
