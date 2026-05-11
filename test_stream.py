from simple_dwd_weatherforecast import dwdforecast
from datetime import datetime, timedelta, timezone
import tracemalloc

tracemalloc.start()

timestamp = datetime.now(timezone.utc)

dwd_weather = dwdforecast.Weather("L511")

with open("development/MOSMIX_S_2023091815_240.kml", "rb") as in_file:
    data = in_file.read()
dwd_weather.parse_kml(data)

print(dwd_weather.get_forecast_data(dwdforecast.WeatherDataType.PRECIPITATION_PROBABILITY, timestamp))
