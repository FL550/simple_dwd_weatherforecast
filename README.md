# Simple DWD weather forecast

[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

DISCLAIMER: This project is a private open source project and doesn't have any connection with Deutscher Wetterdienst.

**If you like my work, I would be really happy if you buy me some coffee: [Buy Me A Coffee][buymecoffee]**

## Weather data

This is a python package for simple access to hourly forecast data for the next 10 days. The data is updated every six hours and updated when needed. Some stations also have actual reported weather, which you can also retrieve.

Available station-IDs can be found [here](simple_dwd_weatherforecast/stations.json) or you can use the method `dwdforecast.get_nearest_station_id(latitude, longitude)` which tries to find it for you.

Forecasted weather conditions are evaluated using this [table](https://www.dwd.de/DE/leistungen/opendata/help/schluessel_datenformate/kml/mosmix_element_weather_xls.xlsx?__blob=publicationFile&v=4) and then converted into these possible weather conditions:

- cloudy
- fog
- lightning-rainy
- partlycloudy
- pouring
- rainy
- snowy
- snowy-rainy
- sunny

The reported weather is delayed (roughly one hour), so have a close look at the time within the presented data.

The weather report for the region which is available on the DWD homepage (see an example [here](https://www.dwd.de/DWD/wetter/wv_allg/deutschland/text/vhdl13_dwoh.html)) can also be retrieved via a method which maps the station to the relevant region.

## Weather maps

You can also retrieve weather maps from the DWD GeoServer with this package.

## Installation

```python
python3 -m pip install simple_dwd_weatherforecast
```

## Usage

### Weather data

#### Usage example
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

#### Available methods

All methods return their values as string. The datetime value has to be in UTC. If no data is available for this datetime, None will be returned. With the optional boolean `shouldUpdate` an automated check for new updates can be prevented by setting this parameter to `False`. Otherwise data is updated if new data is available with every function call.

There is also data available which is updated every hour by DWD. Be careful though, as this will download each time roughly 37MB of data. Furthermore, some elements are missing from this data:
- PRECIPITATION_PROBABILITY
- PRECIPITATION_DURATION

You can use this data by using the optional parameter `force_hourly=True`.

```python
is_valid_station_id(station_id) #Checks if given station_id is valid

get_nearest_station_id(latitude, longitude) #Returns nearest Station-ID for the coordinates. latitude and longitude expect float values.

update(optional bool force_hourly) #Force fetch of new data from the DWD server. With this parameter set to True, there will be missing the precipitation forecast. See above.

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
    SUN_IRRADIANCE = "Rad1h" # Unit: W/m2
    FOG_PROBABILITY = "wwM" # Unit: % (0..100)
    HUMIDITY = "humidity"  # Unit: %
    EVAPORATION = ("PEvap", "evaporation")  # In the last 24h Unit: kg/m2

class Weather:

    get_station_name(optional bool shouldUpdate) # Return Station name

    get_forecast_data(weatherDataType: see WeatherDataType, datetime, optional bool shouldUpdate) # Returns the requested weather data

    get_get_reported_weather(weatherDataType: see WeatherDataType, optional bool shouldUpdate) # Returns the latest actual reported value if available for this station

    get_daily_max(weatherDataType: see WeatherDataType, datetime, optional bool shouldUpdate) # Returns the maximum daily value

    get_timeframe_max(weatherDataType: see WeatherDataType, datetime, timeframe: hours after datetime as int, optional bool shouldUpdate) # Returns the maximum of that value within the time frame

    get_daily_min(weatherDataType: see WeatherDataType, datetime, optional bool shouldUpdate) # Returns the minimum daily value

    get_timeframe_min(weatherDataType: see WeatherDataType, datetime, timeframe: hours after datetime as int, optional bool shouldUpdate) # Returns the minimum of that value within the time frame

    get_daily_sum(weatherDataType: see WeatherDataType, datetime, optional bool shouldUpdate) # Returns the daily sum of that value

    get_timeframe_sum(weatherDataType: see WeatherDataType, datetime, timeframe: hours after datetime as int, optional bool shouldUpdate) # Returns the sum of that value within the time frame

    get_daily_avg(weatherDataType: see WeatherDataType, datetime, optional bool shouldUpdate) # Returns the daily average of that value

    get_timeframe_avg(weatherDataType: see WeatherDataType, datetime, timeframe: hours after datetime as int, optional bool shouldUpdate) # Returns the average of that value within the time frame

    get_forecast_condition(datetime, optional bool shouldUpdate) # Result is condition as text

    get_daily_condition(datetime, optional bool shouldUpdate) # Result is an approximate "feeled" condition at this day

    get_timeframe_condition(datetime, timeframe: hours after datetime as int, optional bool shouldUpdate) # Result is an approximate "feeled" condition at this time frame

    get_weather_report(optional bool shouldUpdate) # Returns the weather report for the geographical region of the station as HTML

    get_uv_index(int day_from_today (values: 0-2)) # Returns the UV index for the nearest station available for today, tomorrow or the day after tomorrow

    update(self, optional bool force_hourly (default: False), optional bool with_forecast (default: True), optional bool with_measurements (default: False), optional bool with_report (default: False), optional bool with_uv (default: True)) # Updates the weather data
```

#### Advanced Usage

If you want to access the forecast data for the next 10 days directly for further processing, you can do so. All data is stored in dictonary and can be accessed like this:

```python
from simple_dwd_weatherforecast import dwdforecast

dwd_weather​ ​=​ ​dwdforecast​.​Weather​(​"10385"​) # Station-ID For BERLIN-SCHOENEFELD​
dwd_weather.update() # This has to be done manually to fetch the data from the DWD server
access_forecast_dict = dwd_weather.forecast_data # dwd_weather.forecast_data contains the forecast as a dict
```

Keep in mind that the weather condition is stored as the original digit value as provided by DWD. So if you want to use them, you have to convert these yourself. You can use my simplified conversion from the source code in the variable `weather_codes` or the original conversion available [here](https://www.dwd.de/DE/leistungen/opendata/help/schluessel_datenformate/kml/mosmix_element_weather_xls.xlsx?__blob=publicationFile&v=4).

## Weather maps

You can download weather maps from the DWD GeoServer with this package. There are different options for the displayed foreground and background data. See below for further information.

![example picture of a map produced with this package](/map_example.png?raw=true "Example picture of a map produced with this package")

#### Usage example
```python
from simple_dwd_weatherforecast import dwdmap

image = dwdmap.get_from_location(51.272, 8.84, radius_km=100, map_type=dwdmap.WeatherMapType.NIEDERSCHLAGSRADAR, background_type=dwdmap.WeatherBackgroundMapType.BUNDESLAENDER)

image.save("niederschlag.png")

image = dwdmap.get_germany(map_type=dwdmap.WeatherMapType.UVINDEX, image_width=520, image_height=580)

image.save("uvindex.png")
```

#### Available methods

```python

class WeatherMapType(Enum):
    NIEDERSCHLAGSRADAR = "dwd:Niederschlagsradar"
    MAXTEMP = "dwd:GefuehlteTempMax"
    UVINDEX = "dwd:UVI_CS"
    POLLENFLUG = "dwd:Pollenflug"
    SATELLITE_RGB = "dwd:Satellite_meteosat_1km_euat_rgb_day_hrv_and_night_ir108_3h"
    SATELLITE_IR = "dwd:Satellite_worldmosaic_3km_world_ir108_3h"
    WARNUNGEN_GEMEINDEN = "dwd:Warnungen_Gemeinden"
    WARNUNGEN_KREISE = "dwd:Warnungen_Landkreise"

class WeatherBackgroundMapType(Enum):
    LAENDER = "dwd:Laender"
    BUNDESLAENDER = "dwd:Warngebiete_Bundeslaender"
    KREISE = "dwd:Warngebiete_Kreise"
    GEMEINDEN = "dwd:Warngebiete_Gemeinden"
    SATELLIT = "dwd:bluemarble"

get_from_location(longitude, latitude, radius_km, map_type: WeatherMapType, background_type: WeatherBackgroundMapType, optional integer image_width, optional integer image_height) #Returns map as pillow image with given radius from coordinates

get_germany(map_type: WeatherMapType, optional WeatherBackgroundMapType background_type, optional integer image_width, optional integer image_height, optional string save_to_filename) #Returns map as pillow image of whole germany

get_map(minx,miny,maxx,maxy, map_type: WeatherMapType, background_type: WeatherBackgroundMapType, optional integer image_width, optional integer image_height, optional string save_to_filename) #Returns map as pillow image
```


### Image loop

There is also the possibility to retrieve multiple images as a loop. This can be done by the class ImageLoop. This however only works for the precipitation radar.


#### Usage example
```python
from simple_dwd_weatherforecast import dwdmap

maploop = dwdmap.ImageLoop(
    dwdmap.germany_boundaries.minx,
    dwdmap.germany_boundaries.miny,
    dwdmap.germany_boundaries.maxx,
    dwdmap.germany_boundaries.maxy,
    dwdmap.WeatherMapType.NIEDERSCHLAGSRADAR,
    dwdmap.WeatherBackgroundMapType.BUNDESLAENDER,
    steps=5,
)

for image in enumerate(maploop._images):
    image[1].save(f"image{image[0]}.png")

```

#### Available methods

```python
ImageLoop(minx: float, miny: float, maxx: float, maxy: float, map_type: WeatherMapType, background_type: WeatherBackgroundMapType,
        steps: int = 6, image_width: int = 520,image_height: int = 580) -> ImageLoop

get_images() -> Iterable[ImageFile.ImageFile] # Returns the image loop

update() # Updates the loop to the most recent files

```

## Help and Contribution

Feel free to open an issue if you find one and I will do my best to help you. If you want to contribute, your help is appreciated! If you want to add a new feature, add a pull request first so we can chat about the details.

## Licenses

This package uses public data from [DWD OpenData](https://www.dwd.de/DE/leistungen/opendata/opendata.html). The Copyright can be viewed [here](https://www.dwd.de/DE/service/copyright/copyright_node.html).

[buymecoffee]: https://www.buymeacoffee.com/FL550
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow?style=for-the-badge
