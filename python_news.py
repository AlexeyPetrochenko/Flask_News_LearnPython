import requests
from bs4 import BeautifulSoup

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
        all_news = []
        for tag_li in list_tags_li:
            news_date = tag_li.find(name='time').text
            news = tag_li.find('a').text
            url_news = tag_li.find('a')['href']
            all_news.append({
                'date': news_date,
                'news': news,
                'url': url_news
            })
        return all_news
    return False

