import requests
from bs4 import BeautifulSoup

from datetime import datetime

from webapp.db import db
from webapp.news.models import News


def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.RequestException:
        print('Сетевая ошибка')
        return False


def get_news_python():
    html = get_html('https://www.python.org/')
    if html:
        soup = BeautifulSoup(html.text, 'lxml')
        list_tags_li = soup.select('.medium-widget.blog-widget .menu li')
        for tag_li in list_tags_li:
            date_str = tag_li.find(name='time').text
            try:
                news_date = datetime.strptime(date_str, '%Y-%m-%d')
            except ValueError:
                news_date = datetime.now()
            news = tag_li.find('a').text
            url_news = tag_li.find('a')['href']
            save_news(news, url_news, news_date)


def save_news(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    print(news_exists)
    if not news_exists:
        news_news = News(title=title, url=url, published=published)
        db.session.add(news_news)
        db.session.commit()

