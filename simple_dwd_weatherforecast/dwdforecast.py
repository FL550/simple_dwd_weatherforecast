import csv
import importlib
import json
import math
from collections import OrderedDict, defaultdict
from datetime import datetime, timedelta, timezone
from enum import Enum
from io import BytesIO
from zipfile import ZipFile
import httpx
from stream_unzip import stream_unzip

import arrow
import requests
from lxml import etree

with importlib.resources.files("simple_dwd_weatherforecast").joinpath(  # type: ignore
    "stations.json"
).open("r", encoding="utf-8") as file:
    stations = json.load(file)

with importlib.resources.files("simple_dwd_weatherforecast").joinpath(  # type: ignore
    "uv_stations.json"
).open("r", encoding="utf-8") as file:
    uv_stations = json.load(file)


def load_station_id(station_id: str):
    if station_id in stations:
        return stations[station_id]
    return None


def get_station_by_name(station_name: str):
    for station in stations.items():
        if station[1]["name"] == station_name:
            return station
    return None


def get_nearest_station_id(lat: float, lon: float):
    return get_stations_sorted_by_distance(lat, lon)[0][0]


def get_stations_sorted_by_distance(lat: float, lon: float):
    """
    Return stations sort by distance.

    Given a latitude and longitude, this function returns a list of stations sorted by
    their distance from the provided location.

    Args:
    ----
        lat: The latitude of the location.
        lon: The longitude of the location.

    Returns:
    -------
        list: A list of stations sorted by distance, where each element is a list
           containing the station ID and its distance from the location.

    """
    result = []
    for station in stations.items():
        _lat = float(station[1]["lat"])
        _lon = float(station[1]["lon"])
        distance_temp = get_distance(lat, lon, _lat, _lon)
        result.append([station[0], distance_temp])
    result.sort(key=lambda x: x[1])
    return result


def get_distance(lat, lon, _lat, _lon):
    """Calculate the distance between two points. Result is returned in km."""

    lon_diff = 111.3 * math.cos((lat + _lat) / 2 * 0.01745) * (lon - _lon)
    lat_diff = 111.3 * (lat - _lat)

    return round(math.sqrt(math.pow(lon_diff, 2) + math.pow(lat_diff, 2)), 1)


def get_region(station_id: str):
    if (
        station_id in stations
        and stations[station_id]["bundesland"] in Weather.region_codes
    ):
        return stations[station_id]["bundesland"]
    return None


class WeatherDataType(Enum):
    CONDITION = ("condition", "present_weather")
    TEMPERATURE = ("TTT", "dry_bulb_temperature_at_2_meter_above_ground")  # Unit: K
    DEWPOINT = ("Td", "dew_point_temperature_at_2_meter_above_ground")  # Unit: K
    PRESSURE = ("PPPP", "pressure_reduced_to_mean_sea_level")  # Unit: Pa
    WIND_SPEED = (
        "FF",
        "maximum_wind_speed_as_10_minutes_mean_during_last_hour",
    )  # Unit: m/s
    WIND_DIRECTION = (
        "DD",
        "mean_wind_direction_during_last_10 min_at_10_meters_above_ground",
    )  # Unit: Degrees
    WIND_GUSTS = ("FX1", "maximum_wind_speed_last_hour")  # Unit: m/s
    PRECIPITATION = ("RR1c", "precipitation_amount_last_hour")  # Unit: kg/m^2
    PRECIPITATION_PROBABILITY = ("wwP", "")  # Unit: % (0..100)
    PRECIPITATION_DURATION = ("DRR1", "")  # Unit: s
    CLOUD_COVERAGE = ("N", "cloud_cover_total")  # Unit: % (0..100)
    VISIBILITY = ("VV", "horizontal_visibility")  # Unit: m
    SUN_DURATION = ("SunD1", "")  # Unit: s
    SUN_IRRADIANCE = ("Rad1h", "global_radiation_last_hour")  # Unit: kJ/m^2
    FOG_PROBABILITY = ("wwM", "")  # Unit: % (0..100)
    HUMIDITY = ("humidity", "relative_humidity")  # Unit: %
    EVAPORATION = ("PEvap", "evaporation")  # Unit: kg/m2


class Weather:
    """A class for interacting with weather data from dwd.de."""

    NOT_AVAILABLE = "---"

    station_id = ""
    issue_time = None
    forecast_data = None
    report_data = None
    weather_report = None
    uv_reports = {}
    etags = None

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

    actual_report_codes = {
        1: "wolkenlos",
        2: "heiter",
        3: "bewoelkt",
        4: "bedeckt",
        5: "Nebel",
        6: "gefrierender Nebel",
        7: "leichter Regen",
        8: "Regen",
        9: "kraeftiger Regen",
        10: "gefrierender Regen",
        11: "kraeftiger gefrierender Regen",
        12: "Schneeregen",
        13: "kraeftiger Schneeregen",
        14: "leichter Schneefall",
        15: "Schneefall",
        16: "kraeftiger Schneefall",
        17: "Eiskoerner",
        18: "Regenschauer",
        19: "kraeftiger Regenschauer",
        20: "Schneeregenschauer",
        21: "kraeftiger Schneeregenschauer",
        22: "Schneeschauer",
        23: "kraeftiger Schneeschauer",
        24: "Graupelschauer",
        25: "kraeftiger Graupelschauer",
        26: "Gewitter ohne Niederschlag",
        27: "Gewitter",
        28: "kraeftiges Gewitter",
        29: "Gewitter mit Hagel",
        30: "kraeftiges Gewitter mit Hagel",
        31: "Sturm",
    }

    region_codes = {
        "NW": "dweh",  # Nordrhein-Westfalen
        "NI": "dwhg",  # Niedersachsen
        "HB": "dwhg",  # Bremen
        "SH": "dwhh",  # Schleswig-Holstein
        "HH": "dwhh",  # Hamburg
        "SN": "dwlg",  # Sachsen
        "ST": "dwlh",  # Sachsen-Anhalt
        "TH": "dwli",  # Thueringen
        "BY": "dwmg",  # Bayern
        "BW": "dwsg",  # Baden-Württemberg
        "HE": "dwoh",  # Hessen
        "RP": "dwoi",  # Rheinland-Pfalz
        "SL": "dwoi",  # Saarland
        "BB": "dwpg",  # Brandenburg
        "BE": "dwpg",  # Berlin
        "MV": "dwph",  # Mecklenburg-Vorpommern
    }

    uv_index_stations_reference_names = {
        "Weinbiet": "Weinbiet",
        "Hamburg": "Hamburg Innenstadt",
        "Seehausen": "Seehausen",
        "Osnabrück": "Osnabrueck",
        "Leipzig": "Leipzig",
        "Stuttgart": "Stuttgart-Schn.",
        "Frankfurt/Main": "Frankfurt/M",
        "Norderney": "Norderney",
        "Berlin": "Berlin-Alex.",
        "Großer Arber": "Gr.Arber",
        "Weimar": "Weimar",
        "Sankt Peter-Ording": "St.Peter-Ording",
        "Konstanz": "Konstanz",
        "Düsseldorf": "Duesseldorf",
        "Freiburg": "Freiburg",
        "Magdeburg": "Magdeburg",
        "Wernigerode": "Wernigerode",
        "Neubrandenburg": "Neubrandenburg",
        "Bonn": "Bonn-Roleber",
        "Marienleuchte": "Bisdorf",
        "Cottbus": "Cottbus",
        "Kiel": "Kiel-H.",
        "List auf Sylt": "List/Sylt",
        "Arkona": "Arkona",
        "Hannover": "Hannover",
        "München": "Muenchen Stadt",
        "Waren": "Waren",
        "Kahler Asten": "K.Asten",
        "Hahn": "Hahn",
        "Bremen": "Bremen",
        "Würzburg": "Wuerzburg",
        "Rostock": "Rostock-Stadt",
        "Ulm": "Ulm",
        "Regensburg": "Regensburg",
        "Kassel": "Kassel",
        "Dresden": "Dresden-Stadt",
        "Zugspitze": "Zugspitze",
        "Nürnberg": "Nuernberg",
    }

    def __init__(self, station_id):
        self.etags = {}
        self.station = load_station_id(station_id)
        if self.station:
            self.station_id = station_id
            self.region = get_region(station_id)
            self.nearest_uv_index_station = self.get_nearest_station_id_with_uv()
        else:
            msg = "Not a valid station_id"
            raise ValueError(msg)

    def get_nearest_station_id_with_uv(self):
        nearest_distance = float("inf")
        nearest_station_id = None
        _station = self.station
        for station in uv_stations.items():
            distance = get_distance(
                self.station["lat"],  # type: ignore
                self.station["lon"],  # type: ignore
                station[1]["lat"],
                station[1]["lon"],
            )

            if distance < nearest_distance:
                nearest_distance = distance
                nearest_station_id = station[0]

        return nearest_station_id

    def get_station_name(self):
        return self.station["name"]  # type: ignore

    def is_in_timerange(self, timestamp: datetime):
        return (
            list(self.forecast_data.keys())[0]  # type: ignore
            <= self.strip_to_hour_str(timestamp)
            <= list(self.forecast_data.keys())[-1]  # type: ignore
        )

    def is_in_timerange_day(self, timestamp: datetime):
        return (
            self.strip_to_day(
                arrow.get(
                    list(self.forecast_data.keys())[0],  # type: ignore
                    "YYYY-MM-DDTHH:mm:ss.SSSZ",  # type: ignore
                ).datetime
            )
            <= self.strip_to_day(timestamp)
            <= self.strip_to_day(
                arrow.get(
                    list(self.forecast_data.keys())[-1],  # type: ignore
                    "YYYY-MM-DDTHH:mm:ss.SSSZ",  # type: ignore
                ).datetime
            )
        )

    def is_valid_timeframe(self, timeframe: int) -> bool:
        if timeframe > 24 or timeframe <= 0:
            return False
        return 24 % timeframe == 0

    def has_measurement(self, station_id):
        if load_station_id(station_id):
            return stations[station_id]["report_available"] == 1
        return False

    def get_forecast_data(
        self, weatherDataType: WeatherDataType, timestamp: datetime, shouldUpdate=True
    ):
        if shouldUpdate:
            self.update()
        if self.is_in_timerange(timestamp):
            return self.forecast_data[self.strip_to_hour_str(timestamp)][  # type: ignore
                weatherDataType.value[0]
            ]
        return None

    def get_forecast_condition(self, timestamp: datetime, shouldUpdate=True):
        if shouldUpdate:
            self.update()

        if self.is_in_timerange(timestamp):
            return str(
                self.weather_codes[
                    self.forecast_data[self.strip_to_hour_str(timestamp)][  # type: ignore
                        WeatherDataType.CONDITION.value[0]
                    ]
                ][0]
            )
        return None

    def get_timeframe_condition(
        self, timestamp: datetime, timeframe: int, shouldUpdate=True
    ):
        if shouldUpdate:
            self.update()
        if self.is_valid_timeframe(timeframe):
            result = self.get_condition(self.get_timeframe_values(timestamp, timeframe))
            if result != "":
                return result
        return None

    def get_daily_condition(self, timestamp: datetime, shouldUpdate=True):
        if shouldUpdate:
            self.update()
        if self.is_in_timerange_day(timestamp):
            return self.get_condition(self.get_day_values(timestamp))
        return None

    def get_condition(self, weather_data):
        if len(weather_data) == 0:
            return None
        if len(weather_data) == 1:
            return self.weather_codes[
                weather_data[0][WeatherDataType.CONDITION.value[0]]
            ][0]

        priority = 99
        weight = defaultdict(lambda: 0, {"sunny": 1, "cloudy": 1})
        for item in weather_data:
            entry = item[WeatherDataType.CONDITION.value[0]]
            if entry != "-":
                (_condition, _priority) = self.weather_codes[entry]
                weight[_condition] = weight[_condition] + 1

                if _priority < priority:
                    priority = _priority
                    condition_text = _condition

        if (weight["cloudy"] + 0.5 * weight["partlycloudy"]) / weight["sunny"] > 0.7:
            condition_text = "cloudy"
        elif (weight["cloudy"] + 0.5 * weight["partlycloudy"]) / weight["sunny"] > 0.2:
            condition_text = "partlycloudy"
        else:
            condition_text = "sunny"

        # Check for special weather
        if weight["fog"] / len(weather_data) > 0.5:
            condition_text = "fog"
        if weight["snowy"] / len(weather_data) > 0.2:
            condition_text = "snowy"
        # Check for rain
        if weight["rainy"] / len(weather_data) > 0.2:
            if condition_text == "snowy":
                condition_text = "snowy-rainy"
            else:
                condition_text = "rainy"
        # Check for thunder
        if weight["lightning-rainy"] > 0:
            condition_text = "lightning-rainy"

        return condition_text

    def get_reported_weather(self, weatherDataType: WeatherDataType, shouldUpdate=True):
        if not self.has_measurement(self.station_id):
            print("no report for this station available")
            return None
        if shouldUpdate:
            self.update(with_measurements=True)
        if self.report_data is not None:
            if weatherDataType == WeatherDataType.CONDITION:
                return self.actual_report_codes[
                    self.report_data[WeatherDataType.CONDITION.value[0]]
                ]
            else:
                return (
                    self.report_data[weatherDataType.value[0]]
                    if weatherDataType.value[0] in self.report_data
                    else None
                )
        else:
            print("no report for this station available. Have you updated first?")

    def get_uv_index(self, days_from_today: int, shouldUpdate=True) -> int | None:
        if not self.uv_reports and shouldUpdate:
            self.update(
                force_hourly=False,
                with_forecast=False,
                with_measurements=False,
                with_report=False,
                with_uv=True,
            )
        if days_from_today < 0 or days_from_today > 2:
            print("days_from_today must be between 0 and 2")
            return None
        if days_from_today == 0:
            day = "today"
        elif days_from_today == 1:
            day = "tomorrow"
        elif days_from_today == 2:
            day = "dayafter_to"
        return (
            self.uv_reports[self.nearest_uv_index_station]["forecast"][day]
            if self.uv_reports
            else None
        )

    def get_timeframe_max(
        self,
        weatherDataType: WeatherDataType,
        timestamp: datetime,
        timeframe: int,
        shouldUpdate=True,
    ):
        if shouldUpdate:
            self.update()
        if self.is_valid_timeframe(timeframe):
            return self.get_max(
                self.get_timeframe_values(timestamp, timeframe), weatherDataType
            )
        return None

    def get_daily_max(
        self, weatherDataType: WeatherDataType, timestamp: datetime, shouldUpdate=True
    ):
        if shouldUpdate:
            self.update()
        if self.is_in_timerange_day(timestamp):
            return self.get_max(self.get_day_values(timestamp), weatherDataType)
        return None

    def get_max(self, weather_data, weatherDataType: WeatherDataType):
        value = None
        for item in weather_data:
            value_new = item[weatherDataType.value[0]]
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
        if self.is_valid_timeframe(timeframe):
            return self.get_min(
                self.get_timeframe_values(timestamp, timeframe), weatherDataType
            )
        return None

    def get_daily_min(
        self, weatherDataType: WeatherDataType, timestamp: datetime, shouldUpdate=True
    ):
        if shouldUpdate:
            self.update()
        if self.is_in_timerange_day(timestamp):
            return self.get_min(self.get_day_values(timestamp), weatherDataType)
        return None

    def get_min(self, weather_data, weatherDataType: WeatherDataType):
        value = None
        for item in weather_data:
            value_new = item[weatherDataType.value[0]]
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
        if self.is_valid_timeframe(timeframe):
            return self.get_sum(
                self.get_timeframe_values(timestamp, timeframe), weatherDataType
            )
        return None

    def get_daily_sum(
        self, weatherDataType: WeatherDataType, timestamp: datetime, shouldUpdate=True
    ):
        if shouldUpdate:
            self.update()
        if self.is_in_timerange_day(timestamp):
            return self.get_sum(self.get_day_values(timestamp), weatherDataType)
        return None

    def get_sum(self, weather_data, weatherDataType):
        value_sum = 0.0
        for item in weather_data:
            value = item[weatherDataType.value[0]]
            if value:
                value_sum += float(value)
        return round(value_sum, 2)

    def get_timeframe_avg(
        self,
        weatherDataType: WeatherDataType,
        timestamp: datetime,
        timeframe: int,
        shouldUpdate=True,
    ):
        if shouldUpdate:
            self.update()
        if self.is_valid_timeframe(timeframe):
            return self.get_avg(
                self.get_timeframe_values(timestamp, timeframe), weatherDataType
            )
        return None

    def get_daily_avg(
        self, weatherDataType: WeatherDataType, timestamp: datetime, shouldUpdate=True
    ):
        if shouldUpdate:
            self.update()
        if self.is_in_timerange_day(timestamp):
            return self.get_avg(self.get_day_values(timestamp), weatherDataType)
        return None

    def get_avg(self, weather_data, weatherDataType):
        value_sum = 0.0
        count = len(weather_data)
        if count != 0:
            for item in weather_data:
                value = item[weatherDataType.value[0]]
                if value:
                    value_sum += float(value)
            return round(value_sum / len(weather_data), 2)
        else:
            return None

    def get_timeframe_values(self, timestamp: datetime, timeframe: int):
        "timestamp has to be checked prior to be in timerange"
        result = []
        time_step = self.strip_to_hour(timestamp)
        for _ in range(timeframe):
            hour_str = self.strip_to_hour_str(time_step)
            time_step += timedelta(hours=1)
            if hour_str not in self.forecast_data:  # type: ignore
                continue
            result.append(self.forecast_data[hour_str])  # type: ignore
        return result

    def get_day_values(self, timestamp: datetime):
        "timestamp has to be checked prior to be in timerange"
        result = []
        first_entry_date = arrow.get(
            next(iter(self.forecast_data)),  # type: ignore
            "YYYY-MM-DDTHH:mm:ss.SSSZ",  # type: ignore
        ).datetime  # type: ignore
        if timestamp.day != first_entry_date.day:
            time_step = self.strip_to_day(timestamp)
            for _ in range(24):
                hour_str = self.strip_to_hour_str(time_step)
                if hour_str not in self.forecast_data:  # type: ignore
                    break
                result.append(self.forecast_data[hour_str])  # type: ignore
                time_step += timedelta(hours=1)
        else:
            time_step = first_entry_date
            endtime = datetime(
                time_step.year,
                time_step.month,
                time_step.day,
                0,
                0,
                0,
                0,
                timezone.utc,
            ) + timedelta(days=1)
            timediff = endtime - time_step
            for _ in range(round(timediff.total_seconds() / 3600)):
                result.append(self.forecast_data[self.strip_to_hour_str(time_step)])  # type: ignore
                time_step += timedelta(hours=1)
        return result

    def strip_to_hour_str(self, timestamp: datetime):
        return timestamp.strftime("%Y-%m-%dT%H:00:00.000Z")

    def strip_to_hour(self, timestamp: datetime):
        return datetime(timestamp.year, timestamp.month, timestamp.day, timestamp.hour)

    def strip_to_day(self, timestamp: datetime):
        return datetime(timestamp.year, timestamp.month, timestamp.day)

    def update(
        self,
        force_hourly=False,
        with_forecast=True,
        with_measurements=False,
        with_report=False,
        with_uv=True,
    ):
        if with_measurements and self.has_measurement(self.station_id):
            self.download_latest_report()

        if with_report and self.region is not None:
            self.download_weather_report(self.region_codes[self.region])

        if with_forecast and (
            (self.issue_time is None)
            or (datetime.now(timezone.utc) - self.issue_time >= timedelta(hours=6))
            or force_hourly
        ):
            self.download_latest_kml(self.station_id, force_hourly)
        if with_uv:
            self.download_uv_index()

    def get_weather_type(self, kmlTree, weatherDataType: WeatherDataType):
        """Parses the kml-File to the requested value and returns the items as array"""

        items = []
        result = kmlTree.xpath(
            './kml:Document/kml:Placemark/kml:ExtendedData/dwd:Forecast[@dwd:elementName="{}"]/dwd:value'.format(
                weatherDataType.value[0]
            ),
            namespaces=self.namespaces,
        )
        if len(result) == 0:
            return items

        result = result[0].text

        for elem in result.split():
            if elem != "-":
                items.append(round(float(elem), 2))
            else:
                items.append(None)
        return items

    def parse_kml(self, kml):
        tree = etree.fromstring(kml)  # type: ignore
        timesteps = self.parse_timesteps(tree)
        issue_time_new = self.parse_issue_time(tree)

        self.issue_time = issue_time_new

        self.loaded_station_name = self.parse_station_name(tree)

        def value(wdt):
            return self.get_weather_type(tree, wdt)

        values = [
            (wdt, value(wdt))
            for wdt in (
                WeatherDataType.TEMPERATURE,
                WeatherDataType.DEWPOINT,
                WeatherDataType.PRESSURE,
                WeatherDataType.WIND_DIRECTION,
                WeatherDataType.WIND_SPEED,
                WeatherDataType.WIND_GUSTS,
                WeatherDataType.PRECIPITATION,
                WeatherDataType.PRECIPITATION_PROBABILITY,
                WeatherDataType.PRECIPITATION_DURATION,
                WeatherDataType.CLOUD_COVERAGE,
                WeatherDataType.VISIBILITY,
                WeatherDataType.SUN_DURATION,
                WeatherDataType.SUN_IRRADIANCE,
                WeatherDataType.FOG_PROBABILITY,
                WeatherDataType.EVAPORATION,
            )
        ]
        values.extend(
            [
                (WeatherDataType.CONDITION, self.parse_condition(tree)),
                (
                    WeatherDataType.HUMIDITY,
                    [
                        self.get_relative_humidity(t, d)
                        for (t, d) in zip(
                            value(WeatherDataType.TEMPERATURE),
                            value(WeatherDataType.DEWPOINT),
                        )
                    ],
                ),
            ]
        )
        self.forecast_data = OrderedDict(
            (t, {wdt.value[0]: (v[i] if len(v) else None) for (wdt, v) in values})
            for (i, t) in enumerate(timesteps)
        )

    def parse_issue_time(self, tree):
        issue_time_new = arrow.get(
            tree.xpath("//dwd:IssueTime", namespaces=self.namespaces)[0].text,
            "YYYY-MM-DDTHH:mm:ss.SSSZ",
        ).datetime
        return issue_time_new

    def parse_station_name(self, tree):
        return tree.xpath(
            "./kml:Document/kml:Placemark/kml:description", namespaces=self.namespaces
        )[0].text

    def parse_timesteps(self, tree):
        return [
            elem.text
            for elem in tree.xpath(
                "//dwd:ForecastTimeSteps/dwd:TimeStep", namespaces=self.namespaces
            )
        ]

    def parse_condition(self, tree):
        return [
            elem.split(".")[0]
            for elem in tree.xpath(
                './kml:Document/kml:Placemark/kml:ExtendedData/dwd:Forecast[@dwd:elementName="ww"]/dwd:value',
                namespaces=self.namespaces,
            )[0].text.split()
        ]

    def get_relative_humidity(self, temperature, dewpoint):
        if None in (temperature, dewpoint):
            return

        def celsius(t):
            return t - 273.1

        T = celsius(temperature)
        TD = celsius(dewpoint)

        rh_c2 = 17.5043
        rh_c3 = 241.2
        return round(
            100 * math.exp((rh_c2 * TD / (rh_c3 + TD)) - (rh_c2 * T / (rh_c3 + T))),
            1,
        )

    def parse_csv_row(self, row: dict):
        self.report_data = {
            "time": row["Parameter description"],
            "date": row["surface observations"],
            WeatherDataType.CONDITION.value[0]: (
                int(row[WeatherDataType.CONDITION.value[1]])
                if row[WeatherDataType.CONDITION.value[1]] != self.NOT_AVAILABLE
                else None
            ),
            WeatherDataType.TEMPERATURE.value[0]: (
                round(
                    float(
                        row[WeatherDataType.TEMPERATURE.value[1]]
                        .replace(self.NOT_AVAILABLE, "0.0")
                        .replace(",", ".")
                    )
                    + 273.1,
                    1,
                )
                if row[WeatherDataType.TEMPERATURE.value[1]] != self.NOT_AVAILABLE
                else None
            ),
            WeatherDataType.DEWPOINT.value[0]: (
                round(
                    float(row[WeatherDataType.DEWPOINT.value[1]].replace(",", "."))
                    + 273.1,
                    1,
                )
                if row[WeatherDataType.DEWPOINT.value[1]] != self.NOT_AVAILABLE
                else None
            ),
            WeatherDataType.PRESSURE.value[0]: (
                float(row[WeatherDataType.PRESSURE.value[1]].replace(",", ".")) * 100
                if row[WeatherDataType.PRESSURE.value[1]] != self.NOT_AVAILABLE
                else None
            ),
            WeatherDataType.WIND_SPEED.value[0]: (
                round(
                    float(row[WeatherDataType.WIND_SPEED.value[1]].replace(",", "."))
                    / 3.6,
                    1,
                )
                if row[WeatherDataType.WIND_SPEED.value[1]] != self.NOT_AVAILABLE
                else None
            ),
            WeatherDataType.WIND_DIRECTION.value[0]: (
                int(row[WeatherDataType.WIND_DIRECTION.value[1]])
                if row[WeatherDataType.WIND_DIRECTION.value[1]] != self.NOT_AVAILABLE
                else None
            ),
            WeatherDataType.WIND_GUSTS.value[0]: (
                round(
                    float(row[WeatherDataType.WIND_GUSTS.value[1]].replace(",", "."))
                    / 3.6,
                    1,
                )
                if row[WeatherDataType.WIND_GUSTS.value[1]] != self.NOT_AVAILABLE
                else None
            ),
            WeatherDataType.PRECIPITATION.value[0]: (
                float(row[WeatherDataType.PRECIPITATION.value[1]].replace(",", "."))
                if row[WeatherDataType.PRECIPITATION.value[1]] != self.NOT_AVAILABLE
                else None
            ),
            WeatherDataType.CLOUD_COVERAGE.value[0]: (
                float(row[WeatherDataType.CLOUD_COVERAGE.value[1]].replace(",", "."))
                if row[WeatherDataType.CLOUD_COVERAGE.value[1]] != self.NOT_AVAILABLE
                else None
            ),
            WeatherDataType.VISIBILITY.value[0]: (
                float(row[WeatherDataType.VISIBILITY.value[1]].replace(",", ".")) * 1e3
                if row[WeatherDataType.VISIBILITY.value[1]] != self.NOT_AVAILABLE
                else None
            ),
            WeatherDataType.SUN_IRRADIANCE.value[0]: (
                round(
                    float(
                        row[WeatherDataType.SUN_IRRADIANCE.value[1]].replace(",", ".")
                    )
                    * 3.6,
                    1,
                )
                if row[WeatherDataType.SUN_IRRADIANCE.value[1]] != self.NOT_AVAILABLE
                else None
            ),
            WeatherDataType.HUMIDITY.value[0]: (
                float(row[WeatherDataType.HUMIDITY.value[1]].replace(",", "."))
                if row[WeatherDataType.HUMIDITY.value[1]] != self.NOT_AVAILABLE
                else None
            ),
        }

    def get_weather_report(self, shouldUpdate=False):
        if (shouldUpdate or self.weather_report is None) and self.region is not None:
            self.update(with_report=True)
        return self.weather_report

    def download_uv_index(self):
        url = "https://opendata.dwd.de/climate_environment/health/alerts/uvi.json"
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.116 Safari/537.36"
        }
        headers["If-None-Match"] = self.etags[url] if url in self.etags else ""  # type: ignore
        try:
            request = requests.get(url, headers=headers, timeout=30)
            # If resource has not been modified, return
            if request.status_code == 304:
                return
            elif request.status_code != 200:
                raise Exception(f"Unexpected status code {request.status_code}")
            self.etags[url] = request.headers["ETag"]  # type: ignore
            uv_reports = json.loads(request.text)["content"]
            # Match with existing stations
            for uv_report in uv_reports:
                station = get_station_by_name(
                    self.uv_index_stations_reference_names[uv_report["city"]]
                )
                # uv_report.update({"lat": station[1]["lat"], "lon": station[1]["lon"]})
                self.uv_reports[station[0]] = uv_report  # type: ignore
        except Exception as error:
            print(f"Error in download_uv_index: {type(error)} args: {error.args}")

    def download_weather_report(self, region_code):
        url = f"https://www.dwd.de/DWD/wetter/wv_allg/deutschland/text/vhdl13_{region_code}.html"
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.116 Safari/537.36"
        }
        headers["If-None-Match"] = self.etags[url] if url in self.etags else ""  # type: ignore
        try:
            request = requests.get(url, headers=headers, timeout=30)
            # If resource has not been modified, return
            if request.status_code == 304:
                return
            self.etags[url] = request.headers["ETag"]  # type: ignore
            weather_report = request.text
            a = weather_report.find(">")
            if a != -1:
                weather_report = weather_report[a + 1 :]
            self.weather_report = weather_report
        except Exception as error:
            print(f"Error in download_weather_report: {type(error)} args: {error.args}")

    def download_small_kml(self, stationid) -> bytes | None:
        url = f"https://opendata.dwd.de/weather/local_forecasts/mos/MOSMIX_L/single_stations/{stationid}/kml/MOSMIX_L_LATEST_{stationid}.kmz"
        headers = {"If-None-Match": self.etags[url] if url in self.etags else ""}  # type: ignore
        try:
            request = requests.get(url, headers=headers, timeout=30)
            # If resource has not been modified, return
            if request.status_code == 304:
                return
            self.etags[url] = request.headers["ETag"]  # type: ignore
            with ZipFile(BytesIO(request.content), "r") as kmz:
                with kmz.open(kmz.namelist()[0], "r") as kml:
                    return kml.read()

        except Exception as error:
            print(f"Error in download_latest_kml: {type(error)} args: {error.args}")

    def get_chunks(self, url):
        def zipped_chunks(url):
            # Iterable that yields the bytes of a zip file
            with httpx.stream(
                "GET",
                url,
            ) as r:
                self.etags[url] = r.headers["etag"]  # type: ignore
                yield from r.iter_bytes(chunk_size=171072)

        return stream_unzip(zipped_chunks(url))

    def download_large_kml(self, stationid):
        placemark = b""
        url = "https://opendata.dwd.de/weather/local_forecasts/mos/MOSMIX_S/all_stations/kml/MOSMIX_S_LATEST_240.kmz"
        # Check if content has updated
        headers = {"If-None-Match": self.etags[url] if url in self.etags else ""}  # type: ignore
        r = httpx.head(
            url,
            headers=headers,
        )
        if r.status_code == 304:
            return

        for file_name, file_size, unzipped_chunks in self.get_chunks(url):
            chunk1 = b""
            chunk2 = b""
            first_chunk = None

            save_next = False
            save_next_next = False
            stop = False
            # unzipped_chunks must be iterated to completion or UnfinishedIterationError will be raised
            for chunk in unzipped_chunks:
                if stop:
                    continue
                if not first_chunk:
                    first_chunk = chunk
                if save_next_next:
                    placemark = chunk1 + chunk2 + chunk
                    save_next_next = False
                    stop = True
                if save_next:
                    chunk2 = chunk
                    save_next_next = True
                    save_next = False

                if f"<kml:name>{stationid}</kml:name>".encode() in chunk:
                    chunk1 = chunk
                    save_next = True

            if not chunk1:
                raise BufferError("Station not found")
            if first_chunk:
                start = placemark.find(b"<kml:Placemark>\n")

                result = (
                    first_chunk[: first_chunk.find(b"<kml:Placemark>")]
                    + placemark[
                        start : placemark.find(b"</kml:Placemark>\n", start) + 17
                    ]
                    + b"</kml:Document></kml:kml>"
                )
                return result

    def download_latest_kml(self, stationid, force_hourly=False):
        kml = (
            self.download_large_kml(stationid)
            if force_hourly
            else self.download_small_kml(stationid)
        )
        if kml is not None:
            self.parse_kml(kml)

    def download_latest_report(self):
        station_id = self.station_id
        if len(station_id) == 4:
            station_id = station_id + "_"
        url = (
            f"https://opendata.dwd.de/weather/weather_reports/poi/{station_id}-BEOB.csv"
        )
        headers = {"If-None-Match": self.etags[url] if url in self.etags else ""}  # type: ignore
        try:
            response = requests.get(url, headers=headers, timeout=30)
            if response.status_code == 200:
                content = response.content
                reader = csv.DictReader(
                    content.decode("utf-8").splitlines(), delimiter=";"
                )
                is_first_run = True
                backuprows = []
                for row in reader:
                    if is_first_run:
                        is_first_run = False
                        reader.__next__()
                        continue
                    backuprows.append(reader.__next__())
                    backuprows.append(reader.__next__())
                    backuprows.append(reader.__next__())

                    # Some items are only reported each hour
                    for backuprow in backuprows:
                        if row["cloud_cover_total"] == self.NOT_AVAILABLE:
                            row["cloud_cover_total"] = backuprow["cloud_cover_total"]
                        if row["horizontal_visibility"] == self.NOT_AVAILABLE:
                            row["horizontal_visibility"] = backuprow[
                                "horizontal_visibility"
                            ]
                        if row["present_weather"] == self.NOT_AVAILABLE:
                            row["present_weather"] = backuprow["present_weather"]
                    self.parse_csv_row(row)
                    # We only want the latest report
                    break

            elif response.status_code == 304:
                # The report is already up to date
                print("Report is already up to date")
            else:
                # Handle other status codes
                print(f"Failed to download report. Status code: {response.status_code}")
        except Exception as error:
            print(f"Error in download_latest_report: {type(error)} args: {error.args}")
