from flask import abort, render_template, Blueprint, current_app, flash, redirect, url_for, request
from flask_login import current_user, login_required

from sqlalchemy.exc import SQLAlchemyError
from webapp.news.forms import CommentForm
from webapp.news.models import News, Comment
from webapp.weather import weather_by_city
from webapp.db import db
from webapp.utils import get_redirect_target

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
    comment_form = CommentForm(news_id=my_news.id)
    return render_template('news/single_news.html', news=my_news,text_news=text_news,  page_title=my_news.title, comment_form=comment_form)


@blueprint.route('/news/comment', methods=['POST'])
@login_required
def add_comment():
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(text=form.comment_text.data, news_id=form.news_id.data, user_id=current_user.id)
        db.session.add(comment)
        try:
            db.session.commit()
            flash('Комментарий успешно добавлен')
        except SQLAlchemyError:
            db.session.rollback()
            raise
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Ошибка в поле {getattr(form, field).label.text}: {error}')
    return redirect(get_redirect_target())
