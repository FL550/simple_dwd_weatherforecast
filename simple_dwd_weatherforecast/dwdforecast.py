import requests
from io import BytesIO
from zipfile import ZipFile
from lxml import etree
from datetime import datetime, timedelta, timezone
import time
import math

from .stations import stations

def is_valid_station_id(station_id: str):
    for line in stations.splitlines():
        if (len(line) > 0 and line[0].isdigit()):
            if line[12:18].strip() == station_id:
                return True
    return False

def get_nearest_station_id(lat: float, lon: float):
    result = ""
    distance = 99999999
    for line in stations.splitlines():
        if (len(line) > 0 and line[0].isdigit()):
            _lat = float(line[45:51].strip())
            _lon = float(line[52:59].strip())
            distance_temp = get_distance(lat, lon, _lat, _lon)
            if distance > distance_temp:
                distance = distance_temp
                result = line[12:18].strip()
    return result


def get_distance(lat, lon, _lat, _lon):
    lat_diff = lat - _lat
    lon_diff = lon - _lon
    return math.sqrt(math.pow(lat_diff, 2) + math.pow(lon_diff, 2))


class Weather:
    """A class for interacting with weather data from dwd.de"""
    station_id = ""
    station_name = ""
    issue_time = None
    forecast_data = None

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

    def get_station_name(self, shouldUpdate=True):
        if self.station_name == '' and shouldUpdate:
            self.update()
        return self.station_name

    def get_forecast_condition(self, timestamp: datetime, shouldUpdate=True):
        if (shouldUpdate):
            self.update()
        time = self.strip_to_hour_str(timestamp)
        if list(self.forecast_data.keys())[0] <= time <= list(
                self.forecast_data.keys())[-1]:
            return str(
                self.weather_codes[self.forecast_data[time]["condition"]][0])
        return None

    def get_forecast_temperature(self, timestamp: datetime, shouldUpdate=True):
        if (shouldUpdate):
            self.update()
        time = self.strip_to_hour_str(timestamp)
        if list(self.forecast_data.keys())[0] <= time <= list(
                self.forecast_data.keys())[-1]:
            return str(self.forecast_data[time]["temp"])
        return None

    def get_forecast_pressure(self, timestamp: datetime, shouldUpdate=True):
        if (shouldUpdate):
            self.update()
        time = self.strip_to_hour_str(timestamp)
        if list(self.forecast_data.keys())[0] <= time <= list(
                self.forecast_data.keys())[-1]:
            return str(self.forecast_data[time]["pressure"])
        return None

    def get_forecast_wind_direction(self,
                                    timestamp: datetime,
                                    shouldUpdate=True):
        if (shouldUpdate):
            self.update()
        time = self.strip_to_hour_str(timestamp)
        if list(self.forecast_data.keys())[0] <= time <= list(
                self.forecast_data.keys())[-1]:
            return str(self.forecast_data[time]["wind_dir"])
        return None

    def get_forecast_wind_speed(self, timestamp: datetime, shouldUpdate=True):
        if (shouldUpdate):
            self.update()
        time = self.strip_to_hour_str(timestamp)
        if list(self.forecast_data.keys())[0] <= time <= list(
                self.forecast_data.keys())[-1]:
            return str(self.forecast_data[time]["wind_speed"])
        return None

    def get_forecast_precipitation(self,
                                   timestamp: datetime,
                                   shouldUpdate=True):
        if (shouldUpdate):
            self.update()
        time = self.strip_to_hour_str(timestamp)
        if list(self.forecast_data.keys())[0] <= time <= list(
                self.forecast_data.keys())[-1]:
            return str(self.forecast_data[time]["prec_sum"])
        return None

    def get_forecast_precipitation_probability(self,
                                               timestamp: datetime,
                                               shouldUpdate=True):
        if (shouldUpdate):
            self.update()
        time = self.strip_to_hour_str(timestamp)
        if list(self.forecast_data.keys())[0] <= time <= list(
                self.forecast_data.keys())[-1]:
            return str(self.forecast_data[time]["prec_prop"])
        return None

    def get_forecast_cloud_coverage(self,
                                    timestamp: datetime,
                                    shouldUpdate=True):
        if (shouldUpdate):
            self.update()
        time = self.strip_to_hour_str(timestamp)
        if list(self.forecast_data.keys())[0] <= time <= list(
                self.forecast_data.keys())[-1]:
            return str(self.forecast_data[time]["cloud_cov"])
        return None

    def get_forecast_visibility(self, timestamp: datetime, shouldUpdate=True):
        if (shouldUpdate):
            self.update()
        time = self.strip_to_hour_str(timestamp)
        if list(self.forecast_data.keys())[0] <= time <= list(
                self.forecast_data.keys())[-1]:
            return str(self.forecast_data[time]["visibility"])
        return None

    def get_forecast_sun_duration(self, timestamp: datetime, shouldUpdate=True):
        if (shouldUpdate):
            self.update()
        time = self.strip_to_hour_str(timestamp)
        if list(self.forecast_data.keys())[0] <= time <= list(
                self.forecast_data.keys())[-1]:
            return str(self.forecast_data[time]["sun_dur"])
        return None

    def get_daily_condition(self, timestamp: datetime, shouldUpdate=True):
        if (shouldUpdate):
            self.update()
        if list(self.forecast_data.keys())[0] <= self.strip_to_hour_str(
                timestamp) <= list(self.forecast_data.keys())[-1]:
            weather_data = self.get_day_values(timestamp)
            priority = 99
            condition_text = ""
            for item in weather_data:
                condition = self.weather_codes[item["condition"]]
                if condition[1] < priority:
                    priority = condition[1]
                    condition_text = condition[0]
            return str(condition_text)
        return None

    def get_daily_temp_max(self, timestamp: datetime, shouldUpdate=True):
        if (shouldUpdate):
            self.update()
        if list(self.forecast_data.keys())[0] <= self.strip_to_hour_str(
                timestamp) <= list(self.forecast_data.keys())[-1]:
            weather_data = self.get_day_values(timestamp)
            temp = None
            for item in weather_data:
                temp_new = item["temp"]
                if temp_new:
                    if not temp:
                        temp = -9999999
                    if temp_new > temp:
                        temp = temp_new
            return str(temp)
        return None

    def get_daily_temp_min(self, timestamp: datetime, shouldUpdate=True):
        if (shouldUpdate):
            self.update()
        if list(self.forecast_data.keys())[0] <= self.strip_to_hour_str(
                timestamp) <= list(self.forecast_data.keys())[-1]:
            weather_data = self.get_day_values(timestamp)
            temp = None
            for item in weather_data:
                temp_new = item["temp"]
                if temp_new:
                    if not temp:
                        temp = 9999999
                    if temp_new < temp:
                        temp = temp_new
            return str(temp)
        return None

    def get_daily_precipitation(self, timestamp: datetime, shouldUpdate=True):
        if (shouldUpdate):
            self.update()
        if list(self.forecast_data.keys())[0] <= self.strip_to_hour_str(
                timestamp) <= list(self.forecast_data.keys())[-1]:
            weather_data = self.get_day_values(timestamp)
            precipitation = None
            for item in weather_data:
                value = item["prec_sum"]
                if (value):
                    if not precipitation:
                        precipitation = 0.0
                    precipitation += float(value)
            return str(precipitation)
        return None

    def get_daily_precipitation_probability(self,
                                            timestamp: datetime,
                                            shouldUpdate=True):
        if (shouldUpdate):
            self.update()
        if list(self.forecast_data.keys())[0] <= self.strip_to_hour_str(
                timestamp) <= list(self.forecast_data.keys())[-1]:
            weather_data = self.get_day_values(timestamp)
            prec_prop = None
            for item in weather_data:
                value = item["prec_prop"]
                if value:
                    if not prec_prop:
                        prec_prop = 0.0
                    prec_prop_new = float(value)
                    if prec_prop_new > prec_prop:
                        prec_prop = prec_prop_new
            return str(int(prec_prop))
        return None

    def get_day_values(self, timestamp: datetime):
        result = []
        if timestamp.day != datetime.now().day:
            time = self.strip_to_day(timestamp)
            for _i in range(24):
                result.append(self.forecast_data[self.strip_to_hour_str(time)])
                time += timedelta(hours=1)
        else:
            time = datetime(timestamp.year, timestamp.month, timestamp.day,
                            timestamp.hour)
            endtime = datetime(timestamp.year, timestamp.month,
                               timestamp.day + 1) - timedelta(hours=-1)
            timediff = endtime - time
            for _i in range(round(timediff.total_seconds() / 3600)):
                result.append(self.forecast_data[self.strip_to_hour_str(time)])
                time += timedelta(hours=1)
        return result

    def strip_to_hour_str(self, timestamp):
        return timestamp.strftime("%Y-%m-%dT%H:00:00.000Z")

    def strip_to_day(self, timestamp):
        return datetime(timestamp.year, timestamp.month, timestamp.day)

    def update(self):
        if (self.issue_time is None) or (datetime.now(timezone.utc) -
                                         self.issue_time > timedelta(hours=6)):
            kml = self.download_latest_kml(self.station_id)
            self.parse_kml(kml)

    def parse_kml(self, kml):
        namespaces = {
            'kml':
                'http://www.opengis.net/kml/2.2',
            'dwd':
                'https://opendata.dwd.de/weather/lib/pointforecast_dwd_extension_V1_0.xsd'
        }
        tree = etree.parse(BytesIO(kml))
        result = tree.xpath('//dwd:IssueTime', namespaces=namespaces)[0].text
        self.issue_time = datetime(
            *(time.strptime(result, '%Y-%m-%dT%H:%M:%S.%fZ')[0:6]), 0,
            timezone.utc)

        result = tree.xpath('//dwd:ForecastTimeSteps/dwd:TimeStep',
                            namespaces=namespaces)
        timesteps = []
        for elem in result:
            timesteps.append(elem.text)

        self.station_name = tree.xpath('//kml:Placemark/kml:description',
                                       namespaces=namespaces)[0].text

        result = tree.xpath(
            '//kml:ExtendedData/dwd:Forecast[@dwd:elementName="ww"]/dwd:value',
            namespaces=namespaces)[0].text
        conditions = []
        for elem in result.split():
            conditions.append(elem.split('.')[0])

        result = tree.xpath(
            '//kml:ExtendedData/dwd:Forecast[@dwd:elementName="TTT"]/dwd:value',
            namespaces=namespaces)[0].text
        temperatures = []
        for elem in result.split():
            if (elem != "-"):
                temperatures.append(round(float(elem) - 273.15, 2))
            else:
                temperatures.append(None)

        result = tree.xpath(
            '//kml:ExtendedData/dwd:Forecast[@dwd:elementName="PPPP"]/dwd:value',
            namespaces=namespaces)[0].text
        pressure = []
        for elem in result.split():
            if (elem != "-"):
                pressure.append(float(elem) / 100)
            else:
                pressure.append(None)
        result = tree.xpath(
            '//kml:ExtendedData/dwd:Forecast[@dwd:elementName="DD"]/dwd:value',
            namespaces=namespaces)[0].text
        wind_dir = []
        for elem in result.split():
            if (elem != "-"):
                wind_dir.append(elem)
            else:
                wind_dir.append(None)
        result = tree.xpath(
            '//kml:ExtendedData/dwd:Forecast[@dwd:elementName="FF"]/dwd:value',
            namespaces=namespaces)[0].text
        wind_speed = []
        for elem in result.split():
            if (elem != "-"):
                wind_speed.append(elem)
            else:
                wind_speed.append(None)
        result = tree.xpath(
            '//kml:ExtendedData/dwd:Forecast[@dwd:elementName="RR1c"]/dwd:value',
            namespaces=namespaces)[0].text
        prec_sum = []
        for elem in result.split():
            if (elem != "-"):
                prec_sum.append(elem)
            else:
                prec_sum.append(None)
        result = tree.xpath(
            '//kml:ExtendedData/dwd:Forecast[@dwd:elementName="wwP"]/dwd:value',
            namespaces=namespaces)[0].text
        prec_prop = []
        for elem in result.split():
            if (elem != "-"):
                prec_prop.append(elem)
            else:
                prec_prop.append(None)
        result = tree.xpath(
            '//kml:ExtendedData/dwd:Forecast[@dwd:elementName="N"]/dwd:value',
            namespaces=namespaces)[0].text
        cloud_cov = []
        for elem in result.split():
            if (elem != "-"):
                cloud_cov.append(elem)
            else:
                cloud_cov.append(None)
        result = tree.xpath(
            '//kml:ExtendedData/dwd:Forecast[@dwd:elementName="VV"]/dwd:value',
            namespaces=namespaces)[0].text
        visibility = []
        for elem in result.split():
            if (elem != "-"):
                visibility.append(elem)
            else:
                visibility.append(None)
        result = tree.xpath(
            '//kml:ExtendedData/dwd:Forecast[@dwd:elementName="SunD1"]/dwd:value',
            namespaces=namespaces)[0].text
        sun_dur = []
        for elem in result.split():
            if (elem != "-"):
                sun_dur.append(round(float(elem) / 60))
            else:
                sun_dur.append(None)
        merged_list = {}
        for i in range(len(timesteps)):

            item = {
                "temp": temperatures[i],
                "condition": conditions[i],
                "pressure": pressure[i],
                "wind_dir": wind_dir[i],
                "wind_speed": wind_speed[i],
                "prec_sum": prec_sum[i],
                "prec_prop": prec_prop[i],
                "cloud_cov": cloud_cov[i],
                "visibility": visibility[i],
                "sun_dur": sun_dur[i]
            }
            merged_list[timesteps[i]] = item
        self.forecast_data = merged_list

    def download_latest_kml(self, stationid):
        url = 'https://opendata.dwd.de/weather/local_forecasts/mos/MOSMIX_L/single_stations/' \
            + stationid + '/kml/MOSMIX_L_LATEST_' + stationid + '.kmz'
        request = requests.get(url)
        file = BytesIO(request.content)
        kmz = ZipFile(file, 'r')
        kml = kmz.open(kmz.namelist()[0], 'r').read()
        return kml
