import requests
from io import BytesIO
from zipfile import ZipFile
from enum import Enum
from lxml import etree
from datetime import datetime, timedelta, timezone
import time
import math

from .stations import stations


def is_valid_station_id(station_id: str):
    for line in stations.splitlines():
        if len(line) > 0 and line[0].isdigit():
            if line[12:18].strip() == station_id:
                return True
    return False


def get_nearest_station_id(lat: float, lon: float):
    result = ""
    distance = 99999999
    for line in stations.splitlines():
        if len(line) > 0 and line[0].isdigit():
            _lat = line[45:51].strip().split(".")
            _lat = round(float(_lat[0]) + float(_lat[1]) / 60, 2)
            _lon = line[52:59].strip().split(".")
            _lon = round(float(_lon[0]) + float(_lon[1]) / 60, 2)
            distance_temp = get_distance(lat, lon, _lat, _lon)
            if distance > distance_temp:
                distance = distance_temp
                result = line[12:18].strip()
    return result


def get_distance(lat, lon, _lat, _lon):
    lat_diff = lat - _lat
    lon_diff = lon - _lon
    return math.sqrt(math.pow(lat_diff, 2) + math.pow(lon_diff, 2))


class WeatherDataType(Enum):
    CONDITION = "condition"
    TEMPERATURE = "TTT"  # Unit: K
    DEWPOINT = "Td"  # Unit: K
    PRESSURE = "PPPP"  # Unit: Pa
    WIND_SPEED = "FF"  # Unit: m/s
    WIND_DIRECTION = "DD"  # Unit: Degrees
    WIND_GUSTS = "FX1"  # Unit: m/s
    PRECIPITATION = "RR1c"  # Unit: kg/m2
    PRECIPITATION_PROBABILITY = "wwP"  # Unit: % (0..100)
    PRECIPITATION_DURATION = "DRR1"  # Unit: s
    CLOUD_COVERAGE = "N"  # Unit: % (0..100)
    VISIBILITY = "VV"  # Unit: m
    SUN_DURATION = "SunD1"  # Unit: s
    SUN_IRRADIANCE = "Rad1h"  # Unit: kJ/m2
    FOG_PROBABILITY = "wwM"  # Unit: % (0..100)


class Weather:
    """A class for interacting with weather data from dwd.de"""

    station_id = ""
    station_name = ""
    issue_time = None
    forecast_data = None

    namespaces = {
        "kml": "http://www.opengis.net/kml/2.2",
        "dwd": "https://opendata.dwd.de/weather/lib/pointforecast_dwd_extension_V1_0.xsd",
    }

    weather_codes = {
        "1": ("sunny", 29),
        "0": ("sunny", 28),
        "2": ("partlycloudy", 27),
        "3": ("cloudy", 26),
        "45": ("fog", 25),
        "49": ("fog", 24),
        "51": ("rainy", 20),
        "53": ("rainy", 19),
        "55": ("rainy", 18),
        "56": ("rainy", 3),
        "57": ("rainy", 2),
        "61": ("rainy", 23),
        "63": ("rainy", 22),
        "65": ("rainy", 21),
        "66": ("rainy", 5),
        "67": ("rainy", 4),
        "68": ("rainy", 17),
        "69": ("snowy-rainy", 16),
        "71": ("snowy", 15),
        "73": ("snowy", 14),
        "75": ("snowy", 13),
        "80": ("rainy", 12),
        "81": ("pouring", 11),
        "82": ("pouring", 10),
        "83": ("snowy-rainy", 9),
        "84": ("snowy-rainy", 8),
        "85": ("snowy-rainy", 7),
        "86": ("snowy-rainy", 6),
        "95": ("lightning-rainy", 1),
    }

    def __init__(self, station_id):
        if is_valid_station_id(station_id):
            self.station_id = station_id
        else:
            raise ValueError("Not a valid station_id")

    def get_station_name(self, shouldUpdate=False):
        if self.station_name == "" or shouldUpdate:
            self.update()
        return self.station_name

    def is_in_timerange(self, timestamp: datetime):
        return (
            list(self.forecast_data.keys())[0]
            <= self.strip_to_hour_str(timestamp)
            <= list(self.forecast_data.keys())[-1]
        )

    def is_valid_timeframe(_, timeframe: int) -> bool:
        if 24 < timeframe or timeframe <= 0:
            return False
        return 24 % timeframe == 0

    def get_forecast_data(
        self, weatherDataType: WeatherDataType, timestamp: datetime, shouldUpdate=True
    ):
        if shouldUpdate:
            self.update()
        if self.is_in_timerange(timestamp):
            return self.forecast_data[self.strip_to_hour_str(timestamp)][
                weatherDataType.value
            ]
        return None

    def get_forecast_condition(self, timestamp: datetime, shouldUpdate=True):
        if shouldUpdate:
            self.update()

        if self.is_in_timerange(timestamp):
            return str(
                self.weather_codes[
                    self.forecast_data[self.strip_to_hour_str(timestamp)][
                        WeatherDataType.CONDITION.value
                    ]
                ][0]
            )
        return None

    def get_timeframe_condition(
        self, timestamp: datetime, timeframe: int, shouldUpdate=True
    ):
        if shouldUpdate:
            self.update()
        if self.is_valid_timeframe(timeframe) and self.is_in_timerange(timestamp):
            return self.get_condition(self.get_timeframe_values(timestamp, timeframe))
        return None

    def get_daily_condition(self, timestamp: datetime, shouldUpdate=True):
        if shouldUpdate:
            self.update()
        if self.is_in_timerange(timestamp):
            return self.get_condition(self.get_day_values(timestamp))
        return None

    def get_condition(self, weather_data):
        priority = 99
        condition_text = ""
        for item in weather_data:
            if item[WeatherDataType.CONDITION.value] != "-":
                condition = self.weather_codes[item[WeatherDataType.CONDITION.value]]
                if condition[1] < priority:
                    priority = condition[1]
                    condition_text = condition[0]
        return str(condition_text)

    def get_timeframe_max(
        self,
        weatherDataType: WeatherDataType,
        timestamp: datetime,
        timeframe: int,
        shouldUpdate=True,
    ):
        if shouldUpdate:
            self.update()
        if self.is_in_timerange(timestamp) and self.is_valid_timeframe(timeframe):
            return self.get_max(
                self.get_timeframe_values(timestamp, timeframe), weatherDataType
            )
        return None

    def get_daily_max(
        self, weatherDataType: WeatherDataType, timestamp: datetime, shouldUpdate=True
    ):
        if shouldUpdate:
            self.update()
        if self.is_in_timerange(timestamp):
            return self.get_max(self.get_day_values(timestamp), weatherDataType)
        return None

    def get_max(_, weather_data, weatherDataType: WeatherDataType):
        value = None
        for item in weather_data:
            value_new = item[weatherDataType.value]
            if value_new:
                if not value:
                    value = -9999999
                if value_new > value:
                    value = value_new
        if value:
            return round(value, 2)
        return None

    def get_timeframe_min(
        self,
        weatherDataType: WeatherDataType,
        timestamp: datetime,
        timeframe: int,
        shouldUpdate=True,
    ):
        if shouldUpdate:
            self.update()
        if self.is_in_timerange(timestamp) and self.is_valid_timeframe(timeframe):
            return self.get_min(
                self.get_timeframe_values(timestamp, timeframe), weatherDataType
            )
        return None

    def get_daily_min(
        self, weatherDataType: WeatherDataType, timestamp: datetime, shouldUpdate=True
    ):
        if shouldUpdate:
            self.update()
        if self.is_in_timerange(timestamp):
            return self.get_min(self.get_day_values(timestamp), weatherDataType)
        return None

    def get_min(_, weather_data, weatherDataType: WeatherDataType):
        value = None
        for item in weather_data:
            value_new = item[weatherDataType.value]
            if value_new:
                if not value:
                    value = 9999999
                if value_new < value:
                    value = value_new

        if value:
            return round(value, 2)
        return None

    def get_timeframe_sum(
        self,
        weatherDataType: WeatherDataType,
        timestamp: datetime,
        timeframe: int,
        shouldUpdate=True,
    ):
        if shouldUpdate:
            self.update()
        if self.is_valid_timeframe(timeframe) and self.is_in_timerange(timestamp):
            return self.get_sum(
                self.get_timeframe_values(timestamp, timeframe), weatherDataType
            )
        return None

    def get_daily_sum(
        self, weatherDataType: WeatherDataType, timestamp: datetime, shouldUpdate=True
    ):
        if shouldUpdate:
            self.update()
        if self.is_in_timerange(timestamp):
            return self.get_sum(self.get_day_values(timestamp), weatherDataType)
        return None

    def get_sum(_, weather_data, weatherDataType):
        value_sum = 0.0
        for item in weather_data:
            value = item[weatherDataType.value]
            if value:
                value_sum += float(value)
        return round(value_sum, 2)

    def get_timeframe_values(self, timestamp: datetime, timeframe: int):
        "timestamp has to be checked prior to be in timerange"
        result = []
        time_step = self.strip_to_hour(timestamp)
        for _ in range(timeframe):
            hour_str = self.strip_to_hour_str(time_step)
            time_step += timedelta(hours=1)
            if hour_str not in self.forecast_data:
                continue
            result.append(self.forecast_data[hour_str])
        return result

    def get_day_values(self, timestamp: datetime):
        "timestamp has to be checked prior to be in timerange"
        result = []
        first_entry_date = datetime(
            *(
                time.strptime(next(iter(self.forecast_data)), "%Y-%m-%dT%H:%M:%S.%fZ")[
                    0:6
                ]
            ),
            0,
            timezone.utc,
        )
        if timestamp.day != first_entry_date.day:
            time_step = self.strip_to_day(timestamp)
            for _ in range(24):
                hour_str = self.strip_to_hour_str(time_step)
                if hour_str not in self.forecast_data:
                    break
                result.append(self.forecast_data[hour_str])
                time_step += timedelta(hours=1)
        else:
            time_step = first_entry_date
            endtime = (
                datetime(
                    time_step.year,
                    time_step.month,
                    time_step.day,
                    0,
                    0,
                    0,
                    0,
                    timezone.utc,
                )
                + timedelta(days=1)
                + timedelta(hours=-1)
            )
            timediff = endtime - time_step
            for _ in range(round(timediff.total_seconds() / 3600)):
                result.append(self.forecast_data[self.strip_to_hour_str(time_step)])
                time_step += timedelta(hours=1)
        return result

    def strip_to_hour_str(_, timestamp: datetime):
        return timestamp.strftime("%Y-%m-%dT%H:00:00.000Z")

    def strip_to_hour(_, timestamp: datetime):
        return datetime(timestamp.year, timestamp.month, timestamp.day, timestamp.hour)

    def strip_to_day(_, timestamp: datetime):
        return datetime(timestamp.year, timestamp.month, timestamp.day)

    def update(self):
        if (self.issue_time is None) or (
            datetime.now(timezone.utc) - self.issue_time >= timedelta(hours=6)
        ):
            kml = download_latest_kml(self.station_id)
            self.parse_kml(kml)

    def get_weather_type(self, kmlTree, weatherDataType: WeatherDataType):
        """ Parses the kml-File to the requested value and returns the items as array"""

        result = kmlTree.xpath(
            '//kml:ExtendedData/dwd:Forecast[@dwd:elementName="{}"]/dwd:value'.format(
                weatherDataType.value
            ),
            namespaces=self.namespaces,
        )[0].text
        items = []
        for elem in result.split():
            if elem != "-":
                items.append(round(float(elem), 2))
            else:
                items.append(None)
        return items

    def parse_kml(self, kml):
        tree = etree.parse(BytesIO(kml))
        result = tree.xpath("//dwd:IssueTime", namespaces=self.namespaces)[0].text
        issue_time_new = datetime(
            *(time.strptime(result, "%Y-%m-%dT%H:%M:%S.%fZ")[0:6]), 0, timezone.utc
        )
        # print(f"parsekml self.issue:{self.issue_time} new_issue:{issue_time_new}")
        # if self.issue_time is None or issue_time_new > self.issue_time:
        self.issue_time = issue_time_new

        result = tree.xpath(
            "//dwd:ForecastTimeSteps/dwd:TimeStep", namespaces=self.namespaces
        )
        timesteps = []
        for elem in result:
            timesteps.append(elem.text)
        # print(f"timesteps: {timesteps}")
        self.station_name = tree.xpath(
            "//kml:Placemark/kml:description", namespaces=self.namespaces
        )[0].text

        result = tree.xpath(
            '//kml:ExtendedData/dwd:Forecast[@dwd:elementName="ww"]/dwd:value',
            namespaces=self.namespaces,
        )[0].text
        conditions = []
        for elem in result.split():
            conditions.append(elem.split(".")[0])

        temperatures = self.get_weather_type(tree, WeatherDataType.TEMPERATURE)

        dewpoints = self.get_weather_type(tree, WeatherDataType.DEWPOINT)

        pressure = self.get_weather_type(tree, WeatherDataType.PRESSURE)

        wind_dir = self.get_weather_type(tree, WeatherDataType.WIND_DIRECTION)

        wind_speed = self.get_weather_type(tree, WeatherDataType.WIND_SPEED)

        wind_gusts = self.get_weather_type(tree, WeatherDataType.WIND_GUSTS)

        prec_sum = self.get_weather_type(tree, WeatherDataType.PRECIPITATION)

        prec_prop = self.get_weather_type(
            tree, WeatherDataType.PRECIPITATION_PROBABILITY
        )

        prec_dur = self.get_weather_type(tree, WeatherDataType.PRECIPITATION_DURATION)

        cloud_cov = self.get_weather_type(tree, WeatherDataType.CLOUD_COVERAGE)

        visibility = self.get_weather_type(tree, WeatherDataType.VISIBILITY)

        sun_dur = self.get_weather_type(tree, WeatherDataType.SUN_DURATION)

        sun_irr = self.get_weather_type(tree, WeatherDataType.SUN_IRRADIANCE)

        fog_prop = self.get_weather_type(tree, WeatherDataType.FOG_PROBABILITY)

        merged_list = {}
        for i in range(len(timesteps)):
            item = {
                WeatherDataType.TEMPERATURE.value: temperatures[i],
                WeatherDataType.DEWPOINT.value: dewpoints[i],
                WeatherDataType.CONDITION.value: conditions[i],
                WeatherDataType.PRESSURE.value: pressure[i],
                WeatherDataType.WIND_DIRECTION.value: wind_dir[i],
                WeatherDataType.WIND_SPEED.value: wind_speed[i],
                WeatherDataType.WIND_GUSTS.value: wind_gusts[i],
                WeatherDataType.PRECIPITATION.value: prec_sum[i],
                WeatherDataType.PRECIPITATION_PROBABILITY.value: prec_prop[i],
                WeatherDataType.PRECIPITATION_DURATION.value: prec_dur[i],
                WeatherDataType.CLOUD_COVERAGE.value: cloud_cov[i],
                WeatherDataType.VISIBILITY.value: visibility[i],
                WeatherDataType.SUN_DURATION.value: sun_dur[i],
                WeatherDataType.SUN_IRRADIANCE.value: sun_irr[i],
                WeatherDataType.FOG_PROBABILITY.value: fog_prop[i],
            }
            merged_list[timesteps[i]] = item
        # print(f"temperatures: {self.forecast_data}")
        self.forecast_data = merged_list


def download_latest_kml(stationid):
    url = (
        "https://opendata.dwd.de/weather/local_forecasts/mos/MOSMIX_L/single_stations/"
        + stationid
        + "/kml/MOSMIX_L_LATEST_"
        + stationid
        + ".kmz"
    )
    request = requests.get(url)
    file = BytesIO(request.content)
    kmz = ZipFile(file, "r")
    kml = kmz.open(kmz.namelist()[0], "r").read()
    return kml
