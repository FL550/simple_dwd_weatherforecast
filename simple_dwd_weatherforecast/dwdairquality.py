from enum import Enum
import json
import math
import requests
import csv
from typing import Literal
from datetime import datetime, timedelta, timezone

MISSING_VALUE = -999.0

airquality_data_types = Literal["hourly", "daily"]


class AirQualityDataType(Enum):
    STICKSTOFFDIOXID = "Stickstoffdioxid"
    OZON = "Ozon"
    PM10 = "PM10"
    PM2_5 = "PM2_5"


class AirQuality:
    @staticmethod
    def get_station_from_location(
        latitude: float, longitude: float, data_type: airquality_data_types
    ) -> "AirQuality":
        station_id = get_nearest_airquality_station_id(latitude, longitude)
        return AirQuality(station_id, data_type)

    def __init__(self, station_id: str, data_type: airquality_data_types) -> None:
        self.etags = {}
        self.station_id = station_id
        self.data_type = data_type
        self.data = {}

    def update(self, with_current: bool = False):
        if self.data_type == "hourly" or with_current:
            self._fetch_hourly()
        if self.data_type == "daily":
            self._fetch_daily()

    def get_current(self, air_quality_data_type: AirQualityDataType):
        return self.data[0][air_quality_data_type.value]

    def get_forecast(self, air_quality_data_type: AirQualityDataType):
        return [entry[air_quality_data_type.value] for entry in self.data[1:]]

    def _fetch_hourly(self, hourly_before=False):
        if hourly_before:
            now = (datetime.now(timezone.utc) - timedelta(hours=1)).strftime("%Y%m%d%H")
        else:
            now = datetime.now(timezone.utc).strftime("%Y%m%d%H")
        url = f"https://opendata.dwd.de/climate_environment/health/forecasts/air_quality/lq_forecast_{now}.csv"
        headers = {"If-None-Match": self.etags.get(url, "")}
        try:
            response = requests.get(url, headers=headers, timeout=30)
            if response.status_code == requests.codes.ok:
                content = response.content
                reader = csv.DictReader(
                    content.decode("utf-8").splitlines(), delimiter=";"
                )
                data = self._parse_hourly(reader)
                if self.station_id in data:
                    self.data = data[self.station_id]
            elif response.status_code == requests.codes.not_found:
                self._fetch_hourly(hourly_before=True)
            elif response.status_code == requests.codes.not_modified:
                # The report is already up to date
                pass
            else:
                print(f"Failed to download report. Status code: {response.status_code}")
        except Exception as error:
            print(f"Error in download_latest_report: {type(error)} args: {error.args}")

    def _parse_hourly(self, reader: csv.DictReader[str]):
        result = {}
        for row in reader:
            station = row["Station"].replace("'", "")
            if station not in result:
                result[station] = [{} for i in range(97)]
            component = row["Komponente"].strip().replace("'", "")
            value = row.get("-01h")
            if value is not None:
                value = float(value)
            if value == MISSING_VALUE:
                value = None
            result[station][0][component] = value
            for i in range(96):
                key = f"+0{i + 1}h" if i < 10 else f"+{i + 1}h"
                value = row.get(key)
                if value is not None:
                    value = float(value)
                if value == -999.0:
                    value = None
                result[station][i + 1][component] = value
        return result

    def _fetch_daily(self, hourly_before: bool = False):
        if hourly_before:
            now = (datetime.now(timezone.utc) - timedelta(hours=1)).strftime("%Y%m%d%H")
        else:
            now = datetime.now(timezone.utc).strftime("%Y%m%d%H")
        url = f"https://opendata.dwd.de/climate_environment/health/forecasts/air_quality/lq_average_allstats_{now}.csv"
        headers = {"If-None-Match": self.etags.get(url, "")}
        try:
            response = requests.get(url, headers=headers, timeout=30)
            if response.status_code == requests.codes.ok:
                content = response.content
                reader = csv.DictReader(
                    content.decode("utf-8").splitlines(), delimiter=";"
                )
                data = self._parse_daily(reader)
            if self.station_id in data:
                self.data = data[self.station_id]
            elif response.status_code == requests.codes.not_found:
                self._fetch_daily(hourly_before=True)
            elif response.status_code == requests.codes.not_modified:
                # The report is already up to date
                pass
            else:
                # Handle other status codes
                print(
                    f"Failed to download airquality daily. Status code: {response.status_code}"
                )
        except Exception as error:
            print(
                f"Error in download_airquality_dailyes: {type(error)} args: {error.args}"
            )

    def _parse_daily(self, reader: csv.DictReader[str]):
        result = {}
        for row in reader:
            if row["Station"] not in result:
                result[row["Station"]] = {"today": {}, "tomorrow": {}, "day_after": {}}
            component = row["Komponente"].strip()
            result[row["Station"]]["today"][component] = (
                row["Mittel1"] if row["Mittel1"] != str(MISSING_VALUE) else None
            )
            result[row["Station"]]["tomorrow"][component] = (
                row["Mittel2"] if row["Mittel2"] != str(MISSING_VALUE) else None
            )
            result[row["Station"]]["day_after"][component] = (
                row["Mittel3"] if row["Mittel3"] != str(MISSING_VALUE) else None
            )
        return result


def get_nearest_airquality_station_id(latitude: float, longitude: float) -> str:
    sorted_stations = get_stations_sort_by_distance(latitude, longitude)
    return sorted_stations[0]["station_id"]


def get_stations_sort_by_distance(latitude: float, longitude: float) -> list[dict]:
    stationen = _load_stations()
    for station_id, station in stationen.items():
        station["station_id"] = station_id
        lon_diff = (
            111.3
            * math.cos((station["lat"] + latitude) / 2 * 0.01745)
            * (station["lon"] - longitude)
        )
        lat_diff = 111.3 * (station["lat"] - latitude)

        station["distance"] = round(
            math.sqrt(math.pow(lon_diff, 2) + math.pow(lat_diff, 2)), 1
        )
    return sorted(stationen.values(), key=lambda x: x["distance"])


def _load_stations() -> dict:
    with open(
        "simple_dwd_weatherforecast/airquality_stations.json", encoding="utf-8"
    ) as f:
        return json.load(f)
