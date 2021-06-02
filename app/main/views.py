import csv
import pandas as pd

from flask import render_template, flash, session, redirect, url_for, current_app
from werkzeug.utils import secure_filename

from .forms import NameForm, FindForm
from .. import db, create_app
from ..models import Role, User
from ..my_email import send_email
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    form = FindForm()
    if form.validate_on_submit():
        prompt = form.prompt.data
        certification=form.certification.choices
        index = form.certification.data
        with open('predict.csv', 'r') as f:
            reader = csv.DictReader(f)
            column = [row for row in reader]
            df = pd.DataFrame(column)
            a=certification[int(index)][1]
            value = df[(df['Stock'] == (a+prompt))]['Predict'].values
            value= None if len(value)==0 else value[0]
            form.prompt.data = value

    return render_template('index.html', form=form)


@main.route('/user/<name>', methods=['GET', 'POST'])
def user(name):
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)

            if current_app.config['FLASKY_ADMIN']:
                send_email(current_app.config['FLASKY_ADMIN'], '新用户',
                           'new_user', user=user)
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('你更改的名称为' + form.name.data)
        session['name'] = form.name.data
        name = form.name.data
        form.name.data = ''
        return redirect(url_for('main.user', name=name))

    return render_template('user.html', form=form, name=name)
