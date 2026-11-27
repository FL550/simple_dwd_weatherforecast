import gzip
from datetime import date

from simple_dwd_weatherforecast import dwdfire


def test_parse_station_list():
    raw = "Stationsindex;Hoehe;Breite;Laenge;Name;Bundesland\n10;5;52.5;13.4;Bärlin;Berlin\n".encode("latin-1")
    assert dwdfire.parse_station_list(raw)["10"]["name"] == "Bärlin"


def test_parse_series_and_url():
    header = "Termin;" + ";".join(f"wbi_{i}" for i in range(7))
    gz = gzip.compress(f"{header}\n2025061500;1;1;1;1;1;1;1\n2025061600;1;2;3;4;5;4;3\n".encode())
    assert dwdfire.parse_series(gz, "wbi") == {"issued": date(2025, 6, 16), "values": [1, 2, 3, 4, 5, 4, 3]}
    assert dwdfire._url("grassland", "42_{v}.csv.gz").endswith("grassland_forecast_recent_42_v2-0--0.csv.gz")
