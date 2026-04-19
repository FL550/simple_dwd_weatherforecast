import asyncio
from enum import Enum
import importlib
import importlib.resources
import json
import math
import requests
import csv
from typing import Literal
from datetime import datetime, timezone

MISSING_VALUE = -999.0

airquality_data_types = Literal["hourly", "daily"]


class AirQualityDataType(Enum):
    STICKSTOFFDIOXID = "Stickstoffdioxid"
    OZON = "Ozon"
    PM10 = "PM10"
    PM2_5 = "PM2_5"


class AirQuality:
    @staticmethod
    async def get_station_from_location(
        latitude: float, longitude: float, data_type: airquality_data_types
    ) -> "AirQuality":
        station_id = await get_nearest_airquality_station_id(latitude, longitude)
        return await AirQuality.create(station_id, data_type)

    @classmethod
    async def create(
        cls, station_id: str, data_type: airquality_data_types
    ) -> "AirQuality":
        station = await get_station(station_id)
        return cls(station_id, data_type, station=station)

    def __init__(
        self,
        station_id: str,
        data_type: airquality_data_types,
        station: dict | None = None,
    ) -> None:
        self.etags = {}
        self.station_id = station_id
        self.data_type = data_type
        self.data = {}

        if station is None:
            raise ValueError(
                "Station metadata must be preloaded. Use AirQuality.create() instead."
            )
        if station is None:
            raise ValueError(f"Station ID {station_id} not found.")
        self.station_name = station["name"]
        self.lat = station["lat"]
        self.lon = station["lon"]
        self.altitude = station["altitude"]

    def update(self, with_current_day: bool = False):
        if self.data_type == "hourly":
            self._fetch_hourly()
        if self.data_type == "daily":
            self._fetch_daily(with_current_day)

    def get_current(self, air_quality_data_type: AirQualityDataType):
        return self.data[0][air_quality_data_type.value]

    def get_forecast(self, air_quality_data_type: AirQualityDataType):
        return [entry[air_quality_data_type.value] for entry in self.data[1:]]

    def _fetch_hourly(self, average_current_day: bool = False):

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
                if average_current_day:
                    if self.station_id in data:
                        remaining_hours = data[self.station_id][
                            1 : 1 + max(0, 23 - datetime.now(timezone.utc).hour)
                        ]
                        components = {
                            key
                            for hour_data in data[self.station_id]
                            for key in hour_data
                        }
                        return {
                            component: (
                                round(sum(values) / len(values), 1) if values else None
                            )
                            for component in components
                            for values in (
                                [
                                    hour_data.get(component)
                                    for hour_data in remaining_hours
                                    if hour_data.get(component) is not None
                                ],
                            )
                        }

                elif self.station_id in data:
                    self.data = data[self.station_id]
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

    def _fetch_daily(self, with_current_day: bool = False):
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
                if with_current_day:
                    self.data["today"] = self._fetch_hourly(average_current_day=True)
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
                result[row["Station"]] = {
                    "tomorrow": {},
                    "day_after": {},
                    "three_days": {},
                }
            component = row["Komponente"].strip()
            result[row["Station"]]["tomorrow"][component] = (
                row["Mittel1"] if row["Mittel1"] != str(MISSING_VALUE) else None
            )
            result[row["Station"]]["day_after"][component] = (
                row["Mittel2"] if row["Mittel2"] != str(MISSING_VALUE) else None
            )
            result[row["Station"]]["three_days"][component] = (
                row["Mittel3"] if row["Mittel3"] != str(MISSING_VALUE) else None
            )
        return result


async def get_nearest_airquality_station_id(latitude: float, longitude: float) -> str:
    sorted_stations = await get_stations_sort_by_distance(latitude, longitude)
    return sorted_stations[0]["station_id"]


async def get_stations_sort_by_distance(latitude: float, longitude: float) -> list[dict]:
    stationen = await _load_stations()
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


async def get_station(station_id: str) -> dict | None:
    stationen = await _load_stations()
    return stationen.get(station_id, None)


async def _load_stations() -> dict:
    return await asyncio.to_thread(_load_stations_sync)


def _load_stations_sync() -> dict:
    with (
        importlib.resources.files("simple_dwd_weatherforecast")
        .joinpath("airquality_stations.json")
        .open("r", encoding="utf-8") as file
    ):
        return json.load(file)
