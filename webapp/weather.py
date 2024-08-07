import requests
from flask import current_app


def weather_by_city(name_city: str):
    url_weather = current_app.config['WEATHER_URL']
    params = {
        'key': current_app.config['WEATHER_API_KEY'],
        'q': name_city,
        'format': 'json',
        'num_of_days': 1,
        'lang': 'ru'
    }

    try:
        response = requests.get(url_weather, params=params)
        response.raise_for_status()
        json_response = response.json()
        if 'data' in json_response:
            if 'current_condition' in json_response['data']:
                try:
                    weather_today = json_response['data']['current_condition'][0]
                    return weather_today
                except (KeyError, TypeError):
                    return False
    except (requests.exceptions.RequestException, ValueError) as err:
        print(f'Сетевая ошибка! - {err}')
        return False
    return False

