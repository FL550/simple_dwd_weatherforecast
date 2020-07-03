# Simple DWD weather forecast

DISCLAIMER: This project is a private open source project and doesn't have any connection with Deutscher Wetterdienst.

This is a python package for simple access to hourly forecast data for the next 10 days. The data is updated every six hours and updated when needed.

Available station-IDs can be found [here](https://www.dwd.de/DE/leistungen/met_verfahren_mosmix/mosmix_stationskatalog.cfg?view=nasPublication&nn=16102) in the third column.

## Installation

```python
python3 -m pip install simple_dwd_weatherforecast
```

## Usage

```python
from simple_dwd_weatherforecast import dwdforecast
from datetime import datetime, timedelta

dwd_weather = dwdforecast.Weather("10385") # Station-ID For BERLIN-SCHOENEFELD
time_now = datetime.now()
temperature_now = dwd_weather.get_forecast_temperature(time_now)
time_tomorrow = datetime.now()+timedelta(days=1)
temperature_tomorrow = dwd_weather.get_forecast_temperature(time_tomorrow)
```

### Available methods

All methods return their values as string. If no data is available for this datetime, None will be returned.

```python
get_forecast_temperature(datetime) #Result is in degrees Celcius

get_forecast_pressure(datetime) #Result is in hPa

get_forecast_wind_direction(datetime) #Result is in degrees magnetic

get_forecast_wind_speed(datetime) #Result is in m/s

get_forecast_precipitation(datetime) #Result is in kg/m2

get_forecast_precipitation_probability(datetime) #Result is in percent

get_forecast_cloud_coverage(datetime) #Result is in percent

get_forecast_visibility(datetime) #Result is in meters

get_forecast_sun_duration(datetime) #Result is in minutes of the last hour

get_daily_temp_max(datetime) #Result is in degrees Celcius

get_daily_temp_min(datetime) #Result is in degrees Celcius
```

## Licenses

This package uses public data from [DWD OpenData](https://www.dwd.de/DE/leistungen/opendata/opendata.html). The Copyright can be viewed [here](https://www.dwd.de/DE/service/copyright/copyright_node.html).
