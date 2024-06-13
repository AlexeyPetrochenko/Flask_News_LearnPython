from flask import Flask, render_template

from webapp.weather import weather_by_city
from webapp.python_news import get_news_python
from webapp.model import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        title = 'Новости Python'
        news_python = get_news_python()
        weather_now = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        return render_template('index.html', page_title=title, weather=weather_now, news_python=news_python)

    return app


# export FLASK_APP=webapp && export FLASK_ENV=development && flask run
