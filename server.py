from flask import Flask, render_template
from weather import weather_by_city
from python_news import get_news_python
import logging

app = Flask(__name__)


@app.route('/')
def index():
    title = 'Новости Python'
    news_python = get_news_python()
    weather = weather_by_city('Roslavl, Russia')

    return render_template('index.html', page_title=title, weather=weather, news_python=news_python)


if __name__ == '__main__':
    app.run(debug=True)