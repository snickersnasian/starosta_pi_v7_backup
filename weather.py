from pyowm import OWM
from pyowm.utils.config import get_default_config
from config import owm_token

### погода ###
def weather_def():
    config_dict = get_default_config()
    config_dict['language'] = 'ru'

    place = "Moscow, RU"
    owm = OWM(owm_token, config_dict)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather

    t = w.temperature("celsius")
    t1 = t['temp']
    t2 = t['feels_like']
    wi = w.wind()['speed']
    humi = w.humidity
    dt = w.detailed_status

    weather_exit = (
        f"На данный момент погода: \n\n"
        f"🌡&#4448;Tемпература:&#4448;{round(t1)} °C \n"
        f"👅&#4448;Ощущается как:&#4448;{round(t2)} °C \n"
        f"💨&#4448;Скорость ветра:&#4448;{wi} м/с \n"
        f"💧&#4448;Влажность:&#4448;{humi}% \n"
    )

    return(weather_exit)