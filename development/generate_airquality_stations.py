import csv
from datetime import datetime, timezone
import json
import requests

stationen = {}
# File from https://www.env-it.de/stationen/public/downloadRequest.do
with open("Bericht_EU_Meta_Stationen.csv", encoding="windows-1252") as file:
    content = file.read()
    # Remove the first line (header) from the content
    content = "\n".join(content.splitlines()[1:])
    content = csv.DictReader(content.splitlines(), delimiter=";")
    for row in content:
        station_id = row["station_code"]
        end_date = row["station_end_date"]
        if end_date != "":
            end_date = datetime.strptime(end_date, "%Y%m%d")
            if end_date < datetime.now(tz=timezone.utc).replace(tzinfo=None):
                print(f"Skipping deactivated station {station_id} ended at {end_date}")
                continue
        name = row["station_name"]
        lat = float(row["station_latitude_d"])
        lon = float(row["station_longitude_d"])
        altitude = (
            int(row["station_altitude"]) if row["station_altitude"] != "" else None
        )
        stationen[station_id] = {
            "name": name,
            "lat": lat,
            "lon": lon,
            "altitude": altitude,
        }

print(f"Found {len(stationen)} active air quality stations.")

now = datetime.now(timezone.utc).strftime("%Y%m%d%H")
url = f"https://opendata.dwd.de/climate_environment/health/forecasts/air_quality/lq_forecast_{now}.csv"
try:
    response = requests.get(url, timeout=30)
    if response.status_code == requests.codes.ok:
        content = response.content
        reader = csv.DictReader(content.decode("utf-8").splitlines(), delimiter=";")
    else:
        # Handle other status codes
        print(f"Failed to download report. Status code: {response.status_code}")
except Exception as error:
    print(f"Error in download_latest_report: {type(error)} args: {error.args}")


active_stationen = set()
for row in reader:
    active_stationen.add(row["Station"].replace("'", ""))

stationen = {k: v for k, v in stationen.items() if k in active_stationen}

print(f"Found {len(stationen)} stations with air quality data.")

with open(
    "../simple_dwd_weatherforecast/airquality_stations.json", "w", encoding="utf-8"
) as f:
    json.dump(stationen, f, ensure_ascii=False)
