import datetime
import requests
from requests.exceptions import Timeout
from bs4 import BeautifulSoup
import json
import re
import pandas as pd

print("Retrieving MOSMIX stations catalogue...")
while True:
    request = requests.get(
        "https://www.dwd.de/DE/leistungen/met_verfahren_mosmix/mosmix_stationskatalog.cfg?view=nasPublication"
    )
    if request.status_code == 200:
        break

request.encoding = request.apparent_encoding
mosmix_data = request.text.split("\n")
print("Done.")

print("Retrieving POI stations catalogue...")
while True:
    request = requests.get("https://opendata.dwd.de/weather/weather_reports/poi/")
    if request.status_code == 200:
        break
soup = BeautifulSoup(request.text, "html.parser")
print("Parsing...")
poi_links = [link.text[0:-9].replace("_", "") for link in soup.find_all("a")]
print("Done.")

range_iter = iter(range(len(mosmix_data) - 1))
first_run = True
stations = {}
with open("development/bundeslaender.json", "r", encoding="utf-8") as f:
    bundeslaender = json.load(f)

for i in range_iter:
    if first_run:
        mosmix_data[i] += f" POI REGION"
        next(range_iter)
        first_run = False
        continue
    group = re.search(
        "^(?P<id>\S*)\s*(?P<icao>\S*)\s+(?P<name>.+?)\s+(?P<lat>-?\d{1,2}\.\d{2})\s*(?P<lon>-?\d{1,3}\.\d{2})\s+(?P<elev>-*\d+)$",
        mosmix_data[i],
    ).group
    group_id = group("id")
    station = {
        "icao": group("icao"),
        "report_available": 1 if group_id in poi_links else 0,
        "bundesland": "",
    }
    station.update(
        {
            "name": group("name").title(),
            "lat": group("lat"),
            "lon": group("lon"),
            "elev": group("elev"),
            "bundesland": bundeslaender[f'{group("lat")};{group("lon")}']
            if f'{group("lat")};{group("lon")}' in bundeslaender
            else "",
        }
    )
    stations[group_id] = station

with open("simple_dwd_weatherforecast/stations.json", "w", encoding="utf-8") as f:
    json.dump(stations, f, ensure_ascii=False)
