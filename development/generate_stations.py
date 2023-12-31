import requests
from bs4 import BeautifulSoup
import json
import re
import math


def get_distance(lat, lon, _lat, _lon):
    """Calculate the distance between two points. Result is returned in km."""

    lon_diff = 111.3 * math.cos((lat + _lat) / 2 * 0.01745) * (lon - _lon)
    lat_diff = 111.3 * (lat - _lat)

    return round(math.sqrt(math.pow(lon_diff, 2) + math.pow(lat_diff, 2)), 1)


def get_bundesland_with_smallest_distance(station, bundeslaender):
    smallest_distance = float("inf")
    smallest_distance_bundesland = ""
    for key in bundeslaender.keys():
        coords = key.split(";")
        temp_distance = get_distance(
            station["lat"], station["lon"], float(coords[0]), float(coords[1])
        )

        if temp_distance < smallest_distance:
            smallest_distance = temp_distance
            smallest_distance_bundesland = bundeslaender[key]
    return smallest_distance_bundesland if smallest_distance < 50 else ""


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

print("Parsing MOSMIX...")
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
    lat = round(
        float(group("lat").split(".")[0]) + float(group("lat").split(".")[1]) / 60, 3
    )
    lon = round(
        float(group("lon").split(".")[0]) + float(group("lon").split(".")[1]) / 60, 3
    )
    station.update(
        {
            "name": group("name").title(),
            "lat": lat,
            "lon": lon,
            "elev": group("elev"),
            "bundesland": bundeslaender[f'{group("lat")};{group("lon")}']
            if f'{group("lat")};{group("lon")}' in bundeslaender
            else "",
        }
    )
    stations[group_id] = station
print("Done.")

print("Adding missing bundeslaender...")
# Add bundesland for those missing
for key, station in stations.items():
    if station["bundesland"] == "":
        station["bundesland"] = get_bundesland_with_smallest_distance(
            station, bundeslaender
        )
print("Done.")

with open("simple_dwd_weatherforecast/stations.json", "w", encoding="utf-8") as f:
    json.dump(stations, f, ensure_ascii=False)
