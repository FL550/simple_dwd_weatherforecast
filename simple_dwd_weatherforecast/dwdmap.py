from typing import Iterable
import requests
import math
from io import BytesIO
from PIL import Image, ImageFile
from enum import Enum
from collections import deque
from datetime import datetime, timedelta, timezone


class WeatherMapType(Enum):
    NIEDERSCHLAGSRADAR = "dwd:Niederschlagsradar,dwd:NCEW_EU"
    MAXTEMP = "dwd:GefuehlteTempMax"
    UVINDEX = "dwd:UVI_CS"
    POLLENFLUG = "dwd:Pollenflug"
    SATELLITE_RGB = "dwd:Satellite_meteosat_1km_euat_rgb_day_hrv_and_night_ir108_3h"
    SATELLITE_IR = "dwd:Satellite_worldmosaic_3km_world_ir108_3h"
    WARNUNGEN_GEMEINDEN = "dwd:Warnungen_Gemeinden"
    WARNUNGEN_KREISE = "dwd:Warnungen_Landkreise"


class WeatherBackgroundMapType(Enum):
    LAENDER = "dwd:Laender"
    BUNDESLAENDER = "dwd:Warngebiete_Bundeslaender"
    KREISE = "dwd:Warngebiete_Kreise"
    GEMEINDEN = "dwd:Warngebiete_Gemeinden"
    SATELLIT = "dwd:bluemarble"
    GEWAESSER = "dwd:Gewaesser"


class germany_boundaries:
    minx = 4.4
    miny = 46.4
    maxx = 16.1
    maxy = 55.6


def get_from_location(
    longitude,
    latitude,
    radius_km,
    map_type: WeatherMapType,
    background_type: WeatherBackgroundMapType = WeatherBackgroundMapType.BUNDESLAENDER,
    image_width=520,
    image_height=580,
):
    if radius_km <= 0:
        raise ValueError("Radius must be greater than 0")
    if latitude < -90 or latitude > 90:
        raise ValueError("Latitude must be between -90 and 90")
    if longitude < -180 or longitude > 180:
        raise ValueError("Longitude must be between -180 and 180")
    radius = math.fabs(radius_km / (111.3 * math.cos(latitude)))
    return get_map(
        latitude - radius,
        longitude - radius,
        latitude + radius,
        longitude + radius,
        map_type,
        background_type,
        image_width,
        image_height,
    )


def get_germany(
    map_type: WeatherMapType,
    background_type: WeatherBackgroundMapType = WeatherBackgroundMapType.BUNDESLAENDER,
    image_width=520,
    image_height=580,
):
    return get_map(
        germany_boundaries.minx,
        germany_boundaries.miny,
        germany_boundaries.maxx,
        germany_boundaries.maxy,
        map_type,
        background_type,
        image_width,
        image_height,
    )


def get_map(
    minx,
    miny,
    maxx,
    maxy,
    map_type: WeatherMapType,
    background_type: WeatherBackgroundMapType,
    image_width=520,
    image_height=580,
):
    if image_width > 1200 or image_height > 1400:
        raise ValueError(
            "Width and height must not exceed 1200 and 1400 respectively. Please be kind to the DWD servers."
        )
    if background_type in [
        WeatherBackgroundMapType.SATELLIT,
        WeatherBackgroundMapType.KREISE,
        WeatherBackgroundMapType.GEMEINDEN,
    ]:
        layers = f"{background_type.value}, {map_type.value}"
    else:
        layers = f"{map_type.value}, {background_type.value}"
    url = f"https://maps.dwd.de/geoserver/dwd/wms?service=WMS&version=1.1.0&request=GetMap&layers={layers}&bbox={minx},{miny},{maxx},{maxy}&width={image_width}&height={image_height}&srs=EPSG:4326&styles=&format=image/png"
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        image = Image.open(BytesIO(request.content))
        return image


class ImageLoop:
    _last_update: datetime
    _images: deque[ImageFile.ImageFile]

    _minx: float
    _miny: float
    _maxx: float
    _maxy: float
    _map_type: WeatherMapType
    _background_type: WeatherBackgroundMapType
    _image_width: int
    _image_height: int

    def __init__(
        self,
        minx: float,
        miny: float,
        maxx: float,
        maxy: float,
        map_type: WeatherMapType,
        background_type: WeatherBackgroundMapType,
        steps: int = 6,
        image_width: int = 520,
        image_height: int = 580,
    ):
        if image_width > 1200 or image_height > 1400:
            raise ValueError(
                "Width and height must not exceed 1200 and 1400 respectively. Please be kind to the DWD servers."
            )
        self._minx = minx
        self._miny = miny
        self._maxx = maxx
        self._maxy = maxy
        if map_type != WeatherMapType.NIEDERSCHLAGSRADAR:
            raise ValueError("Only NIEDERSCHLAGSRADAR is supported in a loop")
        self._map_type = map_type
        self._background_type = background_type
        self._steps = steps
        self._image_width = image_width
        self._image_height = image_height

        self._images = deque([], steps)

        self._full_reload()

    def __getitem__(self, key):
        return self._images[key]

    def get_images(self) -> Iterable[ImageFile.ImageFile]:
        return self._images

    def _full_reload(self):
        self._images.clear()
        now = get_time_last_5_min(datetime.now(timezone.utc))
        self._last_update = now - timedelta(minutes=5) * self._steps

        while now > self._last_update:
            self._last_update += timedelta(minutes=5)
            self._images.append(self._get_image(self._last_update))

    def update(self):
        now = get_time_last_5_min(datetime.now(timezone.utc))

        # If last update is older than the buffer can hold, reload the whole buffer
        if now - self._last_update > self._steps * timedelta(minutes=5):
            self._full_reload()
        # Update the buffer and fetch only the new images
        else:
            while now > self._last_update:
                self._last_update += timedelta(minutes=5)
                self._images.append(self._get_image(self._last_update))

    def _get_image(self, date: datetime) -> ImageFile.ImageFile:
        if self._background_type in [
            WeatherBackgroundMapType.SATELLIT,
            WeatherBackgroundMapType.KREISE,
            WeatherBackgroundMapType.GEMEINDEN,
        ]:
            layers = f"{self._background_type.value}, {self._map_type.value}"
        else:
            layers = f"{self._map_type.value}, {self._background_type.value}"
        url = f"https://maps.dwd.de/geoserver/dwd/wms?service=WMS&version=1.1.0&request=GetMap&layers={layers}&bbox={self._minx},{self._miny},{self._maxx},{self._maxy}&width={self._image_width}&height={self._image_height}&srs=EPSG:4326&styles=&format=image/png&TIME={date.strftime("%Y-%m-%dT%H:%M:00.0Z")}"
        request = requests.get(url, stream=True)
        if request.status_code != 200:
            raise ConnectionError("Error during image request from DWD servers")
        return Image.open(BytesIO(request.content))


def get_time_last_5_min(date: datetime) -> datetime:
    minute = math.floor(date.minute / 5) * 5
    return date.replace(minute=minute, second=0, microsecond=0)
