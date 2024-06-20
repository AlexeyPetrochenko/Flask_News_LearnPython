from flask import Flask, render_template, flash, url_for, redirect
from flask_login import LoginManager, login_user, logout_user, current_user, login_required

from webapp.weather import weather_by_city
from webapp.model import db, News, User
from webapp.forms import LoginForm


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def index():
        title = 'Новости Python'
        news_python = News.query.order_by(News.published.desc()).all()
        weather_now = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        return render_template('index.html', page_title=title, weather=weather_now, news_python=news_python)

    @app.route('/login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))

        title = 'Авторизация'
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    @app.route('/logout')
    def logout():
        logout_user()
        flash('Вы успешно вышли из сессии')
        return redirect(url_for('index'))

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter(User.username == form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Вы успешно авторизовались')
                return redirect(url_for('index'))
        flash('Неверный логин или пароль')
        return redirect(url_for('login'))

    @app.route('/personal-area')
    @login_required
    def personal_area():
        if current_user.is_admin:
            return f'Личный кабинет администратора: {current_user}'
        else:
            return f'Личный кабинет лошка: {current_user}'
    return app


# export FLASK_APP=webapp && export FLASK_ENV=development && flask run
