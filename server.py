from flask import Flask
from weather import weather_by_city

app = Flask(__name__)


@app.route('/')
def index():
    weather = weather_by_city('Roslavl, Russia')
    if weather:
        return (f'В Рославле сейчас {weather["lang_ru"][0]["value"]}, {weather["temp_C"]}C '
                f'ощущается как {weather["FeelsLikeC"]}C.')
    return f'К сожалению мы не смогли найти данные о погоде'


if __name__ == '__main__':
    app.run(debug=True)