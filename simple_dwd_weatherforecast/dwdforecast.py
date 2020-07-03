import requests
from io import BytesIO
from zipfile import ZipFile
from lxml import etree
from datetime import datetime, timedelta


class Weather:
    """A class for interacting with weather data from dwd.de"""
    station_id = ""
    station_name = ""
    issue_time = None
    forecast_data = None

    def __init__(self, stationid):
        self.station_id = stationid

    def get_forecast_temperature(self, timestamp: datetime):
        self.update()
        time = self.strip_to_hour_str(timestamp)
        if list(self.forecast_data.keys())[0] < time < list(
                self.forecast_data.keys())[-1]:
            return str(self.forecast_data[time]["temp"])
        return None

    def get_forecast_pressure(self, timestamp: datetime):
        self.update()
        time = self.strip_to_hour_str(timestamp)
        if list(self.forecast_data.keys())[0] < time < list(
                self.forecast_data.keys())[-1]:
            return str(self.forecast_data[time]["pressure"])
        return None

    def get_forecast_wind_direction(self, timestamp: datetime):
        self.update()
        time = self.strip_to_hour_str(timestamp)
        if list(self.forecast_data.keys())[0] < time < list(
                self.forecast_data.keys())[-1]:
            return str(self.forecast_data[time]["wind_dir"])
        return None

    def get_forecast_wind_speed(self, timestamp: datetime):
        self.update()
        time = self.strip_to_hour_str(timestamp)
        if list(self.forecast_data.keys())[0] < time < list(
                self.forecast_data.keys())[-1]:
            return str(self.forecast_data[time]["wind_speed"])
        return None

    def get_forecast_precipitation(self, timestamp: datetime):
        self.update()
        time = self.strip_to_hour_str(timestamp)
        if list(self.forecast_data.keys())[0] < time < list(
                self.forecast_data.keys())[-1]:
            return str(self.forecast_data[time]["prec_sum"])
        return None

    def get_forecast_precipitation_probability(self, timestamp: datetime):
        self.update()
        time = self.strip_to_hour_str(timestamp)
        if list(self.forecast_data.keys())[0] < time < list(
                self.forecast_data.keys())[-1]:
            return str(self.forecast_data[time]["prec_prop"])
        return None

    def get_forecast_cloud_coverage(self, timestamp: datetime):
        self.update()
        time = self.strip_to_hour_str(timestamp)
        if list(self.forecast_data.keys())[0] < time < list(
                self.forecast_data.keys())[-1]:
            return str(self.forecast_data[time]["cloud_cov"])
        return None

    def get_forecast_visibility(self, timestamp: datetime):
        self.update()
        time = self.strip_to_hour_str(timestamp)
        if list(self.forecast_data.keys())[0] < time < list(
                self.forecast_data.keys())[-1]:
            return str(self.forecast_data[time]["visibility"])
        return None

    def get_forecast_sun_duration(self, timestamp: datetime):
        self.update()
        time = self.strip_to_hour_str(timestamp)
        if list(self.forecast_data.keys())[0] < time < list(
                self.forecast_data.keys())[-1]:
            return str(self.forecast_data[time]["sun_dur"])
        return None

    def get_daily_temp_max(self, timestamp: datetime):
        self.update()
        if list(self.forecast_data.keys())[0] < self.strip_to_hour_str(timestamp) \
            < list(self.forecast_data.keys())[-1]:
            weather_data = self.get_day_values(timestamp)
            temp = -9999999
            for item in weather_data:
                temp_new = item["temp"]
                if temp_new > temp:
                    temp = temp_new
            return str(temp)
        return None

    def get_daily_temp_min(self, timestamp: datetime):
        self.update()
        if list(self.forecast_data.keys())[0] < self.strip_to_hour_str(timestamp) \
            < list(self.forecast_data.keys())[-1]:
            weather_data = self.get_day_values(timestamp)
            temp = 9999999
            for item in weather_data:
                temp_new = item["temp"]
                if temp_new < temp:
                    temp = temp_new
            return str(temp)
        return None

    def get_day_values(self, timestamp: datetime):
        result = []
        if timestamp.day != datetime.now().day:
            time = self.strip_to_day(timestamp)
            for _i in range(24):
                result.append(self.forecast_data[self.strip_to_hour_str(time)])
                time += timedelta(hours=1)
        else:
            time = datetime(timestamp.year, timestamp.month,
                               timestamp.day, timestamp.hour)
            endtime = datetime(timestamp.year, timestamp.month,
                               timestamp.day + 1) - timedelta(hours=-1)
            timediff = endtime - time
            for _i in range(round(timediff.total_seconds()/3600)):
                result.append(self.forecast_data[self.strip_to_hour_str(time)])
                time += timedelta(hours=1)
        return result

    def strip_to_hour_str(self, timestamp):
        return timestamp.strftime("%Y-%m-%dT%H:00:00.000Z")

    def strip_to_day(self, timestamp):
        return datetime(timestamp.year, timestamp.month, timestamp.day)

    def update(self):
        if (self.issue_time == None) or (datetime.now() - self.issue_time >
                                         timedelta(hours=6)):
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
        self.issue_time = datetime.strptime(result, '%Y-%m-%dT%H:%M:%S.%fZ')

        result = tree.xpath('//dwd:ForecastTimeSteps/dwd:TimeStep',
                            namespaces=namespaces)
        timesteps = []
        for elem in result:
            timesteps.append(elem.text)

        self.station_name = tree.xpath('//kml:Placemark/kml:description',
                                       namespaces=namespaces)[0].text

        result = tree.xpath(
            '//kml:ExtendedData/dwd:Forecast[@dwd:elementName="TTT"]/dwd:value',
            namespaces=namespaces)[0].text
        temperatures = []
        for elem in result.split():
            temperatures.append(round(float(elem) - 273.15, 2))

        result = tree.xpath(
            '//kml:ExtendedData/dwd:Forecast[@dwd:elementName="PPPP"]/dwd:value',
            namespaces=namespaces)[0].text
        pressure = []
        for elem in result.split():
            pressure.append(float(elem) / 100)

        result = tree.xpath(
            '//kml:ExtendedData/dwd:Forecast[@dwd:elementName="DD"]/dwd:value',
            namespaces=namespaces)[0].text
        wind_dir = []
        for elem in result.split():
            wind_dir.append(elem)

        result = tree.xpath(
            '//kml:ExtendedData/dwd:Forecast[@dwd:elementName="FF"]/dwd:value',
            namespaces=namespaces)[0].text
        wind_speed = []
        for elem in result.split():
            wind_speed.append(elem)

        result = tree.xpath(
            '//kml:ExtendedData/dwd:Forecast[@dwd:elementName="RR1c"]/dwd:value',
            namespaces=namespaces)[0].text
        prec_sum = []
        for elem in result.split():
            prec_sum.append(elem)

        result = tree.xpath(
            '//kml:ExtendedData/dwd:Forecast[@dwd:elementName="wwP"]/dwd:value',
            namespaces=namespaces)[0].text
        prec_prop = []
        for elem in result.split():
            prec_prop.append(elem)

        result = tree.xpath(
            '//kml:ExtendedData/dwd:Forecast[@dwd:elementName="N"]/dwd:value',
            namespaces=namespaces)[0].text
        cloud_cov = []
        for elem in result.split():
            cloud_cov.append(elem)

        result = tree.xpath(
            '//kml:ExtendedData/dwd:Forecast[@dwd:elementName="VV"]/dwd:value',
            namespaces=namespaces)[0].text
        visibility = []
        for elem in result.split():
            visibility.append(elem)

        result = tree.xpath(
            '//kml:ExtendedData/dwd:Forecast[@dwd:elementName="SunD1"]/dwd:value',
            namespaces=namespaces)[0].text
        sun_dur = []
        for elem in result.split():
            sun_dur.append(round(float(elem) / 60))

        merged_list = {}
        for i in range(len(timesteps)):
            item = {
                "temp": temperatures[i],
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
