import os
from datetime import timedelta


WEATHER_DEFAULT_CITY = 'Roslavl, Russia'
WEATHER_API_KEY = 'fa0e05c81f4148398d0140136243105'
WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')

SECRET_KEY = '%sadkjfh%^$sfssdf'
REMEMBER_COOKIE_DURATION = timedelta(days=5)
