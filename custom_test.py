from datetime import datetime
from simple_dwd_weatherforecast import dwdmap, dwdforecast
from PIL import Image
from datetime import datetime, timedelta, timezone
import tracemalloc
from memory_profiler import profile
import httpx
from stream_unzip import stream_unzip


tracemalloc.start()

dwd_weather = dwdforecast.Weather("N4333")  # Station-ID For BERLIN-SCHOENEFELD


def zipped_chunks():
    # Iterable that yields the bytes of a zip file
    with httpx.stream(
        "GET",
        "https://opendata.dwd.de/weather/local_forecasts/mos/MOSMIX_S/all_stations/kml/MOSMIX_S_LATEST_240.kmz",
    ) as r:
        yield from r.iter_bytes(chunk_size=65536)


from lxml import etree


def get_placemark_xml():
    placemark = b""
    for file_name, file_size, unzipped_chunks in stream_unzip(zipped_chunks()):
        # unzipped_chunks must be iterated to completion or UnfinishedIterationError will be raised
        chunk1 = b""
        chunk2 = b""
        first_chunk = None

        save_next = False
        save_next_next = False
        for chunk in unzipped_chunks:
            if not first_chunk:
                first_chunk = chunk
            if save_next_next:
                placemark = chunk1 + chunk2 + chunk
                save_next_next = False
            if save_next:
                chunk2 = chunk
                save_next_next = True
                save_next = False

            if b"N4333" in chunk:
                chunk1 = chunk
                save_next = True

    header = first_chunk[: first_chunk.find(b"<kml:Placemark>")]
    placemark = placemark[placemark.find(b"<kml:Placemark>\n") :]
    placemark = placemark[: placemark.find(b"</kml:Placemark>\n") + 17]

    result = header + placemark + b"</kml:Document></kml:kml>"
    return result


placemark = get_placemark_xml()

xml = etree.fromstring(placemark)

timesteps = dwd_weather.parse_timesteps(xml)
issue_time_new = dwd_weather.parse_issue_time(xml)

tree = dwd_weather.parse_placemark(xml)

print(timesteps)
print(issue_time_new)

first_size, first_peak = tracemalloc.get_traced_memory()

print(f"{first_size=}, {first_peak=}")
