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

print("Retrieving station name catalogue...")
while True:
    request = requests.get(
        "https://www.dwd.de/DE/leistungen/klimadatendeutschland/statliste/statlex_html.html?view=nasPublication"
    )
    if request.status_code == 200:
        break
print("Parsing...")
soup = BeautifulSoup(request.text, "html.parser")
print("Done.")
stations_catalogue = []
now = datetime.datetime.now()
for row in soup.table.find_all("tr"):
    cols = row.find_all("td")
    if len(cols) > 5 and "." in cols[10].text:
        end_year = int(cols[10].text.split(".")[2])
        if end_year >= now.year:
            stations_catalogue.append(
                {
                    "id": cols[1].text.strip(),
                    "kennung": cols[3].text.strip(),
                    "name": cols[0].text.strip(),
                    "lat": cols[4].text.strip(),
                    "lon": cols[5].text.strip(),
                    "elev": cols[6].text.strip(),
                    "bundesland": cols[8].text.strip(),
                    "report_available": 1 if cols[3].text.strip() in poi_links else 0,
                    "date": datetime.datetime.strptime(
                        cols[10].text.strip(), "%d.%m.%Y"
                    ),
                }
            )

stations_catalogue = pd.DataFrame(
    stations_catalogue,
    columns=[
        "id",
        "kennung",
        "name",
        "lat",
        "lon",
        "elev",
        "bundesland",
        "report_available",
        "date",
    ],
)
stations_catalogue = stations_catalogue[
    stations_catalogue["date"]
    == stations_catalogue.groupby("id")["date"].transform("max")
].drop_duplicates()
print(f"Found {len(stations_catalogue)} active stations.")
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
    try:
        station.update(
            [
                (
                    k,
                    stations_catalogue[stations_catalogue["kennung"] == group("id")][
                        k
                    ].values[0],
                )
                for k in ("name", "lat", "lon", "elev", "bundesland")
            ]
        )
    except IndexError or KeyError:
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

with open("./stations.json", "w", encoding="utf-8") as f:
    json.dump(stations, f, ensure_ascii=False)
