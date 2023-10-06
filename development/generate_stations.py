import datetime
import requests
from requests.exceptions import Timeout
from bs4 import BeautifulSoup
import json
import re
import pandas as pd

success = False
print("Retrieving MOSMIX stations catalogue...")
while not success:
    request = requests.get(
        "https://www.dwd.de/DE/leistungen/met_verfahren_mosmix/mosmix_stationskatalog.cfg?view=nasPublication"
    )
    if request.status_code == 200:
        success = True

request.encoding = request.apparent_encoding
mosmix_data = request.text.split("\n")
print("Done.")

success = False
print("Retrieving POI stations catalogue...")
while not success:
    request = requests.get("https://opendata.dwd.de/weather/weather_reports/poi/")
    if request.status_code == 200:
        success = True
soup = BeautifulSoup(request.text, "html.parser")
print("Parsing...")
links_html = soup.find_all("a")
poi_links = []
for link in links_html:
    link = link.text[0:-9]
    link = link.replace("_", "")
    poi_links.append(link)
print("Done.")

success = False
print("Retrieving station name catalogue...")
while not success:
    request = requests.get(
        "https://www.dwd.de/DE/leistungen/klimadatendeutschland/statliste/statlex_html.html?view=nasPublication"
    )
    if request.status_code == 200:
        success = True
print("Parsing...")
soup = BeautifulSoup(request.text, "html.parser")
print("Done.")
stations_list = []
rows_html = soup.table.find_all("tr")

for row in rows_html:
    cols = row.find_all("td")
    if len(cols) > 5 and "." in cols[10].text:
        end_year = int(cols[10].text.split(".")[2])
        if end_year >= datetime.datetime.now().year:
            stations_list.append(
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

stations_list = pd.DataFrame(
    stations_list,
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
stations_list = stations_list[
    stations_list["date"] == stations_list.groupby("id")["date"].transform("max")
]
stations_list = stations_list.drop_duplicates()
print(f"Found {len(stations_list)} active stations.")
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
    # print(mosmix_data[i])
    groups = re.search(
        "^(?P<id>\S*)\s*(?P<icao>\S*)\s+(?P<name>.+?)\s+(?P<lat>-?\d{1,2}\.\d{2})\s*(?P<lon>-?\d{1,3}\.\d{2})\s+(?P<elev>-*\d+)$",
        mosmix_data[i],
    )
    is_in_stations_list = groups.group("id") in stations_list["kennung"].values
    region = ""
    if is_in_stations_list:
        region = stations_list[stations_list["kennung"] == groups.group("id")][
            "bundesland"
        ].values[0]
    elif f'{groups.group("lat")};{groups.group("lon")}' in bundeslaender:
        region = bundeslaender[f'{groups.group("lat")};{groups.group("lon")}']

    stations[groups.group("id")] = {
        "name": stations_list[stations_list["kennung"] == groups.group("id")][
            "name"
        ].values[0]
        if is_in_stations_list
        else groups.group("name").title(),
        "icao": groups.group("icao"),
        "lat": stations_list[stations_list["kennung"] == groups.group("id")][
            "lat"
        ].values[0]
        if is_in_stations_list
        else groups.group("lat"),
        "lon": stations_list[stations_list["kennung"] == groups.group("id")][
            "lon"
        ].values[0]
        if is_in_stations_list
        else groups.group("lon"),
        "elev": stations_list[stations_list["kennung"] == groups.group("id")][
            "elev"
        ].values[0]
        if is_in_stations_list
        else groups.group("elev"),
        "bundesland": region,
        "report_available": 1 if groups.group("id") in poi_links else 0,
    }

with open("../stations.json", "w", encoding="utf-8") as f:
    json.dump(stations, f, ensure_ascii=False)
