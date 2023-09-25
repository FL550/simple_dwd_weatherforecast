import datetime
from secret import API_KEY
import requests
from requests.exceptions import Timeout
from bs4 import BeautifulSoup
import json
import re

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
stations_list = {}
rows_html = soup.table.find_all("tr")
for row in rows_html:
    cols = row.find_all("td")
    if len(cols) > 5 and "." in cols[10].text:
        end_year = int(cols[10].text.split(".")[2])
        if end_year >= datetime.datetime.now().year:
            stations_list[cols[3].text.strip()] = {
                "name": cols[0].text.strip(),
                "lat": cols[4].text.strip(),
                "lon": cols[5].text.strip(),
                "elev": cols[6].text.strip(),
                "bundesland": cols[8].text.strip(),
                "report_available": 1 if cols[3].text.strip() in poi_links else 0,
            }
print(f"Found {len(stations_list.keys())} active stations.")
range_iter = iter(range(len(mosmix_data) - 1))
first_run = True
stations = {}
for i in range_iter:
    if first_run:
        mosmix_data[i] += f" POI REGION"
        next(range_iter)
        first_run = False
        continue
    print(mosmix_data[i])
    groups = re.search(
        "^(?P<id>\S*)\s*(?P<icao>\S*)\s+(?P<name>.+?)\s+(?P<lat>-?\d{1,2}\.\d{2})\s*(?P<lon>-?\d{1,3}\.\d{2})\s+(?P<elev>-*\d+)$",
        mosmix_data[i],
    )
    is_in_stations_list = groups.group("id") in stations_list.keys()
    region = ""
    if is_in_stations_list:
        region = stations_list[groups.group("id")]["bundesland"]
    else:
        _lat = groups.group("lat").split(".")
        _lat = round(float(_lat[0]) + float(_lat[1]) / 60, 2)
        _lon = groups.group("lon").split(".")
        _lon = round(float(_lon[0]) + float(_lon[1]) / 60, 2)
        url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={_lat},{_lon}&location_type=APPROXIMATE&result_type=administrative_area_level_1&language=de&key={API_KEY}"
        try:
            request = requests.get(url, timeout=10)
        except Timeout:
            print("Timeout")
        else:
            region = ""
            request = request.json()
            if request["status"] == "OK":
                region = request["results"][0]["address_components"][0]["long_name"]
                if region == "Hessen":
                    region = "HE"
                elif region == "Nordrhein-Westfalen":
                    region = "NW"
                elif region == "Rheinland-Pfalz":
                    region = "RP"
                elif region == "Saarland":
                    region = "SL"
                elif region == "Baden-Württemberg":
                    region = "BW"
                elif region == "Bayern":
                    region = "BY"
                elif region == "Berlin":
                    region = "BE"
                elif region == "Brandenburg":
                    region = "BB"
                elif region == "Mecklenburg-Vorpommern":
                    region = "MV"
                elif region == "Sachsen":
                    region = "SN"
                elif region == "Sachsen-Anhalt":
                    region = "ST"
                elif region == "Thüringen":
                    region = "TH"
                elif region == "Hamburg":
                    region = "HH"
                elif region == "Bremen":
                    region = "HB"
                elif region == "Schleswig-Holstein":
                    region = "SH"
                elif region == "Niedersachsen":
                    region = "NI"

    stations[groups.group("id")] = {
        "name": stations_list[groups.group("id")]["name"]
        if is_in_stations_list
        else groups.group("name").title(),
        "icao": groups.group("icao"),
        "lat": stations_list[groups.group("id")]["lat"]
        if is_in_stations_list
        else groups.group("lat"),
        "lon": stations_list[groups.group("id")]["lon"]
        if is_in_stations_list
        else groups.group("lon"),
        "elev": stations_list[groups.group("id")]["elev"]
        if is_in_stations_list
        else groups.group("elev"),
        "bundesland": region,
        "report_available": 1 if groups.group("id") in poi_links else 0,
    }

with open("../stations.json", "w", encoding="utf-8") as f:
    json.dump(stations, f, ensure_ascii=False)
