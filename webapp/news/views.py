from flask import render_template, Blueprint, current_app

from webapp.news.models import News
from webapp.weather import weather_by_city


blueprint = Blueprint('news', __name__)


@blueprint.route('/')
def index():
    title = 'Новости Python'
    news_python = News.query.order_by(News.published.desc()).all()
    weather_now = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])
    return render_template('news/index.html', page_title=title, weather=weather_now, news_python=news_python)