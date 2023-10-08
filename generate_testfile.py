from simple_dwd_weatherforecast import dwdforecast
import json

with open("development/MOSMIX_L_2023100809.kml", "rb") as kml:
    dwd_weather = dwdforecast.Weather("N4333")
    dwd_weather.parse_kml(kml)
    with open("tests/dummy_data.py", "w") as f:
        f.write("parsed_data = " + repr(dwd_weather.forecast_data))

with open("development/MOSMIX_L_2023100809_stripped.kml", "rb") as kml:
    dwd_weather = dwdforecast.Weather("L511")
    dwd_weather.parse_kml(kml)
    with open("tests/dummy_data_full.py", "w") as f:
        f.write("parsed_data = " + json.dumps(dwd_weather.forecast_data))
