import requests
import csv
from typing import Literal


class AirQuality:
    def __init__(self, data_type: Literal["hourly", "daily"]) -> None:
        self.etags = {}
        self.data_type = data_type
        self.data = {}

    def update(self):
        if self.data_type == "hourly":
            self._download_hourly()
        elif self.data_type == "daily":
            self._download_daily()

    def _download_hourly(self):
        # TODO change to real date
        now = "2025121911"
        url = f"https://opendata.dwd.de/climate_environment/health/forecasts/air_quality/lq_forecast_{now}.csv"
        headers = {"If-None-Match": self.etags[url] if url in self.etags else ""}  # type: ignore
        try:
            response = requests.get(url, headers=headers, timeout=30)
            if response.status_code == requests.codes.ok:
                content = response.content
                reader = csv.DictReader(
                    content.decode("utf-8").splitlines(), delimiter=";"
                )
                self.data = self._parse_hourly(reader)

            elif response.status_code == requests.codes.not_modified:
                # The report is already up to date
                print("Report is already up to date")
            else:
                # Handle other status codes
                print(f"Failed to download report. Status code: {response.status_code}")
        except Exception as error:
            print(f"Error in download_latest_report: {type(error)} args: {error.args}")

    def _parse_hourly(self, reader: csv.DictReader[str]):
        result = {}
        for row in reader:
            station = row["Station"].replace("'", "")
            if station not in result:
                result[station] = [{} for i in range(96)]
            component = row["Komponente"].strip().replace("'", "")
            for i in range(96):
                key = f"+0{i + 1}h" if i < 10 else f"+{i + 1}h"
                value = row.get(key)
                if value is not None:
                    value = float(value)
                if value == -999.0:
                    value = None
                result[station][i][component] = value
        return result

    def _download_daily(self):
        # TODO change to real date
        now = "2025121911"
        url = f"https://opendata.dwd.de/climate_environment/health/forecasts/air_quality/lq_average_allstats_{now}.csv"
        headers = {"If-None-Match": self.etags[url] if url in self.etags else ""}  # type: ignore
        try:
            response = requests.get(url, headers=headers, timeout=30)
            if response.status_code == requests.codes.ok:
                content = response.content
                reader = csv.DictReader(
                    content.decode("utf-8").splitlines(), delimiter=";"
                )
                self.data = self._parse_daily(reader)

            elif response.status_code == requests.codes.not_modified:
                # The report is already up to date
                print("Report is already up to date")
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
            result[row["Station"]]["today"][component] = row["Mittel1"]
            result[row["Station"]]["tomorrow"][component] = row["Mittel2"]
            result[row["Station"]]["day_after"][component] = row["Mittel3"]
        return result
