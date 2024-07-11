from flask_login import login_user, logout_user, current_user
from flask import render_template, flash, url_for, redirect, Blueprint

from webapp.user.models import User
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.db import db


blueprint = Blueprint('user', __name__, url_prefix='/user')


@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))

    title = 'Авторизация'
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Вы успешно авторизовались')
            return redirect(url_for('news.index'))
    flash('Неверный логин или пароль')
    return redirect(url_for('news.index'))


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Вы успешно вышли из сессии')
    return redirect(url_for('news.index'))

@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        redirect(url_for('news.index'))
    form = RegistrationForm()
    title = 'Регистрация'
    return render_template('user/registration.html', form=form, page_title=title)


@blueprint.route('/process-register', methods=['POST'])
def process_register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, role='user')
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрироавлись')
        return redirect(url_for('user.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Ошибка в поле {getattr(form, field).label.text}: {error}')
        return redirect(url_for('user.register'))