import requests
import json

uv_index_stations = {
    "Weinbiet": "Weinbiet",
    "Hamburg": "Hamburg Innenstadt",
    "Seehausen": "Seehausen",
    "Osnabrück": "Osnabrueck",
    "Leipzig": "Leipzig",
    "Stuttgart": "Stuttgart-Schn.",
    "Frankfurt/Main": "Frankfurt/M",
    "Norderney": "Norderney",
    "Berlin": "Berlin-Alex.",
    "Großer Arber": "Gr.Arber",
    "Weimar": "Weimar",
    "Sankt Peter-Ording": "St.Peter-Ording",
    "Konstanz": "Konstanz",
    "Düsseldorf": "Duesseldorf",
    "Freiburg": "Freiburg",
    "Magdeburg": "Magdeburg",
    "Wernigerode": "Wernigerode",
    "Neubrandenburg": "Neubrandenburg",
    "Bonn": "Bonn-Roleber",
    "Marienleuchte": "Bisdorf",
    "Cottbus": "Cottbus",
    "Kiel": "Kiel-H.",
    "List auf Sylt": "List/Sylt",
    "Arkona": "Arkona",
    "Hannover": "Hannover",
    "München": "Muenchen Stadt",
    "Waren": "Waren",
    "Kahler Asten": "K.Asten",
    "Hahn": "Hahn",
    "Bremen": "Bremen",
    "Würzburg": "Wuerzburg",
    "Rostock": "Rostock-Stadt",
    "Ulm": "Ulm",
    "Regensburg": "Regensburg",
    "Kassel": "Kassel",
    "Dresden": "Dresden-Stadt",
    "Zugspitze": "Zugspitze",
    "Nürnberg": "Nuernberg",
}

with open("simple_dwd_weatherforecast/stations.json", "r", encoding="utf-8") as f:
    stations = json.load(f)


def get_station_by_name(station_name: str):
    for station in stations.items():
        if station[1]["name"] == station_name:
            return station


url = "https://opendata.dwd.de/climate_environment/health/alerts/uvi.json"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.116 Safari/537.36"
}
request = requests.get(url, headers=headers)
if request.status_code != 200:
    raise Exception(f"Unexpected status code {request.status_code}")

uv_stations = {}
uv_reports = json.loads(request.text)["content"]
# Match with existing stations
for uv_report in uv_reports:
    station = get_station_by_name(uv_index_stations[uv_report["city"]])
    uv_report.update({"lat": station[1]["lat"], "lon": station[1]["lon"]})
    del uv_report["forecast"]
    uv_stations[station[0]] = uv_report

with open("simple_dwd_weatherforecast/uv_stations.json", "w", encoding="utf-8") as f:
    json.dump(uv_stations, f, ensure_ascii=False)
