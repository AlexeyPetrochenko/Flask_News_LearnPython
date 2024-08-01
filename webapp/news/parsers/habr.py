from bs4 import BeautifulSoup
from datetime import datetime

from webapp.news.parsers.utils import get_html, save_news
from webapp.news.models import News
from webapp.db import db


def get_news_snippets():
    html = get_html('https://habr.com/ru/search/?target_type=posts&q=python&order_by=date')
    if html:
        soup = BeautifulSoup(html.text, 'lxml')
        list_news = soup.select('.tm-articles-list .tm-articles-list__item')
        print(len(list_news))
        for news in list_news:
            title = news.find(class_='tm-title tm-title_h2').text
            url_news = 'https://habr.com' + news.find(class_='tm-title__link')['href']
            date = news.find('time').get('datetime')
            try:
                date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
            except ValueError:
                print(f'{date} ошибка')
                date = datetime.now()
            save_news(title, url_news, date)


def get_content_snippets():
    empty_news = News.query.filter(News.text.is_(None))
    for news in empty_news:
        html = get_html(news.url)
        if html:
            soup = BeautifulSoup(html.text, 'lxml')
            text_news = soup.find('div', id='post-content-body').encode_contents()
            if text_news:
                news.text = text_news
                db.session.add(news)
                db.session.commit()
