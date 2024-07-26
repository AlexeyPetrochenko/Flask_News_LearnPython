import os
from datetime import timedelta


WEATHER_DEFAULT_CITY = 'Roslavl, Russia'
WEATHER_API_KEY = '15046c99472f46d5af0120527241107'
WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = '%sadkjfh%^$sfssdf'
REMEMBER_COOKIE_DURATION = timedelta(days=5)
