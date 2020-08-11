# Simple DWD weather forecast

DISCLAIMER: This project is a private open source project and doesn't have any connection with Deutscher Wetterdienst.

## IMPORTANT: v1 changes the methods to access the data

This is a python package for simple access to hourly forecast data for the next 10 days. The data is updated every six hours and updated when needed.

Available station-IDs can be found [here](simple_dwd_weatherforecast/stations.py) in the third column or you can use the method `dwdforecast.get_nearest_station_id(latitude, longitude)` which tries to find it for you.

Forecasted weather conditions are evaluated using this [table](https://www.dwd.de/DE/leistungen/opendata/help/schluessel_datenformate/kml/mosmix_element_weather_xls.xlsx?__blob=publicationFile&v=4) and then converted into these possible weather conditions:

- sunny
- partlycloudy
- cloudy
- rainy
- snowy-rainy
- snowy
- pouring
- lightning-rainy

## Installation

```python
python3 -m pip install simple_dwd_weatherforecast
```

## Usage

```python
from simple_dwd_weatherforecast import dwdforecast
from datetime import datetime, timedelta, timezone

#Find nearest Station-ID automatically
#id = dwdforecast.get_nearest_station_id(50.1109221, 8.6821267)

dwd_weather = dwdforecast.Weather("10385") # Station-ID For BERLIN-SCHOENEFELD
time_now = datetime.now(timezone.utc)
temperature_now = dwd_weather.get_forecast_data(dwdforecast.WeatherDataType.TEMPERATURE, time_now)
time_tomorrow = datetime.now(timezone.utc)+timedelta(days=1)
temperature_tomorrow = dwd_weather.get_forecast_data(dwdforecast.WeatherDataType.TEMPERATURE, time_tomorrow)
```

### Available methods

All methods return their values as string. The datetime value has to be in UTC. If no data is available for this datetime, None will be returned. With the optional boolean `shouldUpdate` an automated check for new updates can be prevented by setting this parameter to `False`. Otherwise data is updated if new data is available with every function call.

```python
dwdforecast.is_valid_station_id(station_id) #Checks if given station_id is valid

dwdforecast.get_nearest_station_id(latitude, longitude) #Returns nearest Station-ID for the coordinates. latitude and longitude expect float values.

get_station_name(optional bool shouldUpdate) #Return Station name

class WeatherDataType(Enum):
    CONDITION = "condition"
    TEMPERATURE = "TTT" # Unit: K
    DEWPOINT = "Td" # Unit: K
    PRESSURE = "PPPP" # Unit: Pa
    WIND_SPEED = "FF" # Unit: m/s
    WIND_DIRECTION = "DD" # Unit: Degrees
    WIND_GUSTS = "FX1" # Unit: m/s
    PRECIPITATION = "RR1c" # Unit: kg/m2
    PRECIPITATION_PROBABILITY = "wwP" # Unit: % (0..100)
    PRECIPITATION_DURATION = "DRR1" # Unit: s
    CLOUD_COVERAGE = "N" # Unit: % (0..100)
    VISIBILITY = "VV" # Unit: m
    SUN_DURATION = "SunD1" # Unit: s
    SUN_IRRADIANCE = "Rad1h" # Unit: kJ/m2
    FOG_PROBABILITY = "wwM" # Unit: % (0..100)

get_forecast_data(weatherDataType: see WeatherDataType , datetime, optional bool shouldUpdate) # Returns the requestes weather data

get_daily_max(weatherDataType: see WeatherDataType , datetime, optional bool shouldUpdate) # Returns the maximum daily value

get_daily_min(weatherDataType: see WeatherDataType , datetime, optional bool shouldUpdate) # Returns the minimum daily value

get_daily_sum(weatherDataType: see WeatherDataType , datetime, optional bool shouldUpdate) # Returns the daily sum of that value

get_forecast_condition(datetime, optional bool shouldUpdate) #Result is condition as text

get_daily_condition(datetime, optional bool shouldUpdate) #Result is worst condition at this day
```

### Advanced Usage

If you want to access the forecast data for the next 10 days directly for further processing, you can do so. All data is stored in dictonary and can be accessed like this:

```python
from simple_dwd_weatherforecast import dwdforecast

dwd_weather​ ​=​ ​dwdforecast​.​Weather​(​"10385"​) # Station-ID For BERLIN-SCHOENEFELD​
dwd_weather.update() # This has to be done manually to fetch the data from the DWD server
access_forecast_dict = dwd_weather.forecast_data # dwd_weather.forecast_data contians the forecast as a dict
```

Keep in mind that the weather condition is stored as the original digit value as provided by DWD. So if you want to use them, you have to convert these yourself. You can use my simplified conversion from the source code in the variable `weather_codes` or the original conversion available [here](https://www.dwd.de/DE/leistungen/opendata/help/schluessel_datenformate/kml/mosmix_element_weather_xls.xlsx?__blob=publicationFile&v=4).

## Help and Contribution

Feel free to open an issue if you find one and I will do my best to help you. If you want to contribute, your help is appreciated! If you want to add a new feature, add a pull request first so we can chat about the details.

## Licenses

This package uses public data from [DWD OpenData](https://www.dwd.de/DE/leistungen/opendata/opendata.html). The Copyright can be viewed [here](https://www.dwd.de/DE/service/copyright/copyright_node.html).
