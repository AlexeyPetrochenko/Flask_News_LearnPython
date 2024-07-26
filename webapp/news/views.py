from flask import abort, render_template, Blueprint, current_app

from webapp.news.models import News
from webapp.weather import weather_by_city


blueprint = Blueprint('news', __name__)


@blueprint.route('/')
def index():
    title = 'Новости Python'
    news_python = News.query.filter(News.text.isnot(None)).order_by(News.published.desc()).all()
    weather_now = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])
    return render_template('news/index.html', page_title=title, weather=weather_now, news_python=news_python)


@blueprint.route('/news/<int:news_id>')
def single_news(news_id):
    my_news = News.query.filter(News.id == news_id).first()
    text_news = my_news.text.decode('utf-8')
    if not my_news:
        abort(404)
    return render_template('news/single_news.html', news=text_news, page_title=my_news.title)

