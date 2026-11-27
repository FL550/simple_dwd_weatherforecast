import csv
import gzip
import io
import math
from datetime import datetime

import httpx

BASE_URL = "https://opendata.dwd.de/climate_environment/CDC/derived_germany/fire_danger_index"
# index kind -> (directory, file prefix, column prefix, file version)
INDEXES = {
    "woodland": ("woodland", "wbi", "v2-3--0"),
    "grassland": ("grassland", "glfi", "v2-0--0"),
}
LEVELS = {1: "very low", 2: "low", 3: "medium", 4: "high", 5: "very high"}
_HEADERS = {"user-agent": "Mozilla/5.0 (compatible; simple_dwd_weatherforecast)"}

_stations: dict[str, dict] | None = None


def _url(kind: str, suffix: str) -> str:
    directory, _, version = INDEXES[kind]
    return (
        f"{BASE_URL}/{directory}/forecast/recent/"
        f"derived_germany_fire_danger_index_{directory}_forecast_recent_{suffix}"
    ).replace("{v}", version)


def parse_station_list(raw: bytes) -> dict[str, dict]:
    """Parse the Latin-1, semicolon separated station list.

    Columns: Stationsindex; Hoehe; Breite; Laenge; Name; Bundesland
    """
    result = {}
    lines = raw.decode("latin-1").splitlines()
    for line in lines[1:]:
        parts = [p.strip() for p in line.split(";")]
        if len(parts) < 6:
            continue
        try:
            result[parts[0]] = {
                "name": parts[4],
                "lat": float(parts[2]),
                "lon": float(parts[3]),
                "height": float(parts[1]),
                "state": parts[5],
            }
        except ValueError:
            continue
    return result


def parse_series(gz: bytes, prefix: str) -> dict | None:
    """Parse the last row of a station file into the issue date and 7 daily levels."""
    text = gzip.decompress(gz).decode("utf-8", errors="replace")
    rows = list(csv.DictReader(io.StringIO(text), delimiter=";"))
    if not rows:
        return None
    last = rows[-1]
    last = {k.strip(): v for k, v in last.items() if k}
    try:
        issued = datetime.strptime(last["Termin"].strip()[:8], "%Y%m%d").date()
        values = [int(last[f"{prefix}_{i}"]) for i in range(7)]
    except (KeyError, ValueError):
        return None
    if not all(1 <= v <= 5 for v in values):
        return None
    return {"issued": issued, "values": values}


def load_stations() -> dict[str, dict]:
    global _stations
    if _stations is None:
        url = _url("woodland", "{v}_stations_list.txt")
        response = httpx.get(url, headers=_HEADERS, timeout=30)
        response.raise_for_status()
        _stations = parse_station_list(response.content)
    return _stations


def nearest_station_id(lat: float, lon: float) -> str | None:
    nearest, nearest_distance = None, math.inf
    for station_id, station in load_stations().items():
        d = math.hypot(
            (station["lat"] - lat), (station["lon"] - lon) * math.cos(math.radians(lat))
        )
        if d < nearest_distance:
            nearest, nearest_distance = station_id, d
    return nearest


def download_fire_index(kind: str, station_id: str) -> dict | None:
    _, prefix, _ = INDEXES[kind]
    response = httpx.get(
        _url(kind, f"{station_id}_{{v}}.csv.gz"), headers=_HEADERS, timeout=30
    )
    response.raise_for_status()
    return parse_series(response.content, prefix)
