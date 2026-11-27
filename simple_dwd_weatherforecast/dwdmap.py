from typing import Iterable
import requests
import math
from io import BytesIO
from PIL import Image, ImageFile, ImageDraw
from enum import Enum
from collections import deque
from datetime import datetime, timedelta, timezone

from simple_dwd_weatherforecast.basemap import (
    BaseMap,
    BaseMapNotAvailableError,
    BaseMapStyle,
    get_basemap,
)


class WeatherMapType(Enum):
    NIEDERSCHLAGSRADAR = "dwd:Radar_rv_product_1x1km_ger"
    BLITZSCHLAG = "dwd:NCEW_EU"
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
    # Not a DWD layer: map by BKG with towns, roads and rivers, see basemap.py
    TOPPLUS_LIGHT = "bkg:topplus_light"
    TOPPLUS_DARK = "bkg:topplus_dark"


BASEMAP_STYLES = {
    WeatherBackgroundMapType.TOPPLUS_LIGHT: BaseMapStyle.LIGHT,
    WeatherBackgroundMapType.TOPPLUS_DARK: BaseMapStyle.DARK,
}


class germany_boundaries:
    minx = 4.4
    miny = 46.4
    maxx = 16.1
    maxy = 55.6


class MarkerShape(Enum):
    CIRCLE = "circle"
    SQUARE = "square"
    CROSS = "cross"


class Marker:
    def __init__(
        self,
        latitude: float,
        longitude: float,
        shape: MarkerShape,
        size: int,
        colorRGB: tuple[int, int, int],
        width: int = 0,
    ):
        if (
            latitude is None
            or longitude is None
            or shape is None
            or size is None
            or colorRGB is None
        ):
            raise ValueError("All values have to be defined")
        self.latitude = latitude
        self.longitude = longitude
        self.shape = shape
        self.size = size
        self.colorRGB = colorRGB
        self.width = width


class ImageBoundaries:
    minX: float
    maxX: float
    minY: float
    maxY: float

    def __init__(self, minX: float, maxX: float, minY: float, maxY: float) -> None:
        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY


def get_from_location(
    longitude,
    latitude,
    radius_km,
    map_types: list[WeatherMapType],
    background_types: list[WeatherBackgroundMapType] = [
        WeatherBackgroundMapType.BUNDESLAENDER
    ],
    image_width=520,
    image_height=580,
    markers: list[Marker] = [],
    dark_mode: bool = False,
    basemap_cache_dir: str | None = None,
    basemap_blend: bool = False,
):
    if radius_km <= 0:
        raise ValueError("Radius must be greater than 0")
    if latitude < -90 or latitude > 90:
        raise ValueError("Latitude must be between -90 and 90")
    if longitude < -180 or longitude > 180:
        raise ValueError("Longitude must be between -180 and 180")
    radius = math.fabs(radius_km / (111.3 * math.cos(latitude)))
    return get_map(
        longitude - radius,
        latitude - radius,
        longitude + radius,
        latitude + radius,
        map_types,
        background_types,
        image_width,
        image_height,
        markers,
        dark_mode,
        basemap_cache_dir,
        basemap_blend,
    )


def get_germany(
    map_types: list[WeatherMapType],
    background_types: list[WeatherBackgroundMapType] = [
        WeatherBackgroundMapType.BUNDESLAENDER
    ],
    image_width=520,
    image_height=580,
    markers: list[Marker] = [],
    dark_mode: bool = False,
    basemap_cache_dir: str | None = None,
    basemap_blend: bool = False,
):
    return get_map(
        germany_boundaries.minx,
        germany_boundaries.miny,
        germany_boundaries.maxx,
        germany_boundaries.maxy,
        map_types,
        background_types,
        image_width,
        image_height,
        markers,
        dark_mode,
        basemap_cache_dir,
        basemap_blend,
    )


def get_map(
    minx,
    miny,
    maxx,
    maxy,
    map_types: list[WeatherMapType],
    background_types: list[WeatherBackgroundMapType],
    image_width=520,
    image_height=580,
    markers: list[Marker] = [],
    dark_mode: bool = False,
    basemap_cache_dir: str | None = None,
    basemap_blend: bool = False,
):
    if image_width > 1200 or image_height > 1400:
        raise ValueError(
            "Width and height must not exceed 1200 and 1400 respectively. Please be kind to the DWD servers."
        )
    basemap, background_types = split_basemap(
        background_types,
        minx,
        miny,
        maxx,
        maxy,
        image_width,
        image_height,
        basemap_cache_dir,
    )
    # Separate special layers and others for background types
    special_layers = [
        layer.value
        for layer in background_types
        if layer
        in [
            WeatherBackgroundMapType.SATELLIT,
            WeatherBackgroundMapType.KREISE,
            WeatherBackgroundMapType.GEMEINDEN,
        ]
    ]
    other_layers = [
        layer.value
        for layer in background_types
        if layer
        not in [
            WeatherBackgroundMapType.SATELLIT,
            WeatherBackgroundMapType.KREISE,
            WeatherBackgroundMapType.GEMEINDEN,
        ]
    ]
    # Combine map types into a single string
    map_layers = ",".join(map_type.value for map_type in map_types)
    # Combine layers with special layers first, then map types, then other layers
    layers = f"{','.join(special_layers)},{map_layers},{','.join(other_layers)}".lstrip(
        ","
    ).rstrip(",")
    bgcolor = "0xFFFFFF"
    if dark_mode:
        bgcolor = "0x1C1C1C"
    url = f"https://maps.dwd.de/geoserver/dwd/wms?service=WMS&version=1.3.0&request=GetMap&layers={layers}&bbox={miny},{minx},{maxy},{maxx}&width={image_width}&height={image_height}&srs=EPSG:4326&styles=&format=image/png&bgcolor={bgcolor}"
    if basemap is not None:
        url += "&transparent=true"

    request = requests.get(url, stream=True)
    if request.status_code == 200:
        try:
            image = Image.open(BytesIO(request.content))
        except Exception as e:
            raise RuntimeError(
                f"Error during image request from DWD servers: {url}"
            ) from e
        if basemap is not None:
            image, _ = put_on_basemap(image, basemap, dark_mode, basemap_blend)
        image = draw_marker(image, ImageBoundaries(minx, maxx, miny, maxy), markers)
        return image
    else:
        raise ConnectionError(f"Error during image request from DWD servers: {url}")


class ImageLoop:
    _last_update: datetime
    _images: deque[ImageFile.ImageFile]

    _minx: float
    _miny: float
    _maxx: float
    _maxy: float
    _map_types: list[WeatherMapType]
    _background_types: list[WeatherBackgroundMapType]
    _image_width: int
    _image_height: int

    def __init__(
        self,
        minx: float,
        miny: float,
        maxx: float,
        maxy: float,
        map_types: list[WeatherMapType],
        background_types: list[WeatherBackgroundMapType],
        steps: int = 6,
        image_width: int = 520,
        image_height: int = 580,
        markers: list[Marker] = [],
        dark_mode: bool = False,
        basemap_cache_dir: str | None = None,
        basemap_blend: bool = False,
    ):
        if WeatherMapType.NIEDERSCHLAGSRADAR not in map_types:
            raise ValueError("Only NIEDERSCHLAGSRADAR is supported in a loop")
        if image_width > 1200 or image_height > 1400:
            raise ValueError(
                "Width and height must not exceed 1200 and 1400 respectively. Please be kind to the DWD servers."
            )
        self._minx = minx
        self._miny = miny
        self._maxx = maxx
        self._maxy = maxy
        self._map_types = map_types
        self._background_types = background_types
        self._basemap, self._dwd_background_types = split_basemap(
            background_types,
            minx,
            miny,
            maxx,
            maxy,
            image_width,
            image_height,
            basemap_cache_dir,
        )
        self._basemap_blend = basemap_blend
        self._basemap_missing = False
        self._steps = steps
        self._image_width = image_width
        self._image_height = image_height
        self.markers = markers
        self.dark_mode = dark_mode
        self._images = deque([], steps)

        self._full_reload()

    def __getitem__(self, key):
        return self._images[key]

    def get_images(self) -> Iterable[ImageFile.ImageFile]:
        return self._images

    def _full_reload(self):
        self._images.clear()
        self._basemap_missing = False
        now = get_time_last_5_min(datetime.now(timezone.utc))
        self._last_update = now - timedelta(minutes=5) * self._steps

        self._load_images(now)

    def update(self):
        now = get_time_last_5_min(datetime.now(timezone.utc))

        # If last update is older than the buffer can hold, reload the whole buffer
        if now - self._last_update > self._steps * timedelta(minutes=5):
            self._full_reload()
        # Images drawn while the base map was not available have a blank background
        elif self._basemap_missing and self._basemap.available:
            self._full_reload()
        # Update the buffer and fetch only the new images
        else:
            self._load_images(now)

    def _load_images(self, now):
        while now > self._last_update:
            self._last_update += timedelta(minutes=5)
            # Lightning in the NCEW_EU layer is only available in the last 5 minutes
            try:
                image = self._get_image(
                    self._last_update,
                    with_lightning=(now - self._last_update) < timedelta(minutes=5),
                )
            except ConnectionError as e:
                raise ConnectionAbortedError(
                    f"Connection to DWD map servers failed: {e}"
                )
            except RuntimeError as e:
                raise RuntimeError(f"Error: {e}") from e
            except TypeError:
                try:
                    image = self._get_image(
                        self._last_update,
                        with_lightning=False,
                    )
                except ConnectionError as e:
                    raise ConnectionAbortedError(
                        f"Connection to DWD map servers failed: {e}"
                    )
                except TypeError as e:
                    raise TypeError(
                        f"Unexpected content type: {e}. Please check the DWD map servers."
                    ) from e
            self._images.append(image)

    def _get_image(
        self,
        date: datetime,
        with_lightning: bool = False,
    ) -> ImageFile.ImageFile:
        # Combine map types into a single string
        map_layers = ",".join(map_type.value for map_type in self._map_types)
        if with_lightning:
            map_layers += ",dwd:NCEW_EU"
        # Separate special layers and others for background types
        special_layers = [
            layer.value
            for layer in self._dwd_background_types
            if layer
            in [
                WeatherBackgroundMapType.SATELLIT,
                WeatherBackgroundMapType.KREISE,
                WeatherBackgroundMapType.GEMEINDEN,
            ]
        ]
        other_layers = [
            layer.value
            for layer in self._dwd_background_types
            if layer
            not in [
                WeatherBackgroundMapType.SATELLIT,
                WeatherBackgroundMapType.KREISE,
                WeatherBackgroundMapType.GEMEINDEN,
            ]
        ]
        # Combine layers with special layers first, then map types, then other layers
        layers = (
            f"{','.join(special_layers)},{map_layers},{','.join(other_layers)}".lstrip(
                ","
            ).rstrip(",")
        )
        bgcolor = "0xFFFFFF"
        if self.dark_mode:
            bgcolor = "0x1C1C1C"
        url = f"https://maps.dwd.de/geoserver/dwd/wms?service=WMS&version=1.3.0&request=GetMap&layers={layers}&bbox={self._miny},{self._minx},{self._maxy},{self._maxx}&width={self._image_width}&height={self._image_height}&srs=EPSG:4326&styles=&format=image/png&TIME={date.strftime('%Y-%m-%dT%H:%M:00.0Z')}&bgcolor={bgcolor}"
        if self._basemap is not None:
            url += "&transparent=true"
        request = requests.get(url, stream=True)
        if request.status_code != 200:
            raise ConnectionError(f"Error during image request from DWD servers: {url}")
        elif request.headers["content-type"] != "image/png":
            raise TypeError(
                f"Unexpected content type: {request.headers['content-type']}"
            )
        try:
            image = Image.open(BytesIO(request.content))
        except Exception as e:
            raise RuntimeError(f"Error during image parsing: {url}") from e
        if self._basemap is not None:
            image, complete = put_on_basemap(
                image, self._basemap, self.dark_mode, self._basemap_blend
            )
            if not complete:
                self._basemap_missing = True
        image = draw_marker(
            image,
            ImageBoundaries(self._minx, self._maxx, self._miny, self._maxy),
            self.markers,
        )
        return image


def split_basemap(
    background_types: list[WeatherBackgroundMapType],
    minx: float,
    miny: float,
    maxx: float,
    maxy: float,
    image_width: int,
    image_height: int,
    cache_dir: str | None = None,
) -> tuple[BaseMap | None, list[WeatherBackgroundMapType]]:
    """Return the base map, if one is requested, and the remaining DWD layers."""
    dwd_types = [layer for layer in background_types if layer not in BASEMAP_STYLES]
    styles = [
        BASEMAP_STYLES[layer] for layer in background_types if layer in BASEMAP_STYLES
    ]
    if not styles:
        return None, dwd_types
    basemap = get_basemap(
        minx, miny, maxx, maxy, image_width, image_height, styles[0], cache_dir
    )
    return basemap, dwd_types


def put_on_basemap(
    image: Image.Image,
    basemap: BaseMap,
    dark_mode: bool = False,
    blend: bool = False,
) -> tuple[Image.Image, bool]:
    """Put a transparent weather image onto the base map.

    With blend the map stays readable below the weather. Without a base map the weather is shown on a blank background. The second
    value tells whether the base map was available.
    """
    try:
        return basemap.apply(image, blend=blend), True
    except BaseMapNotAvailableError:
        blank = Image.new(
            "RGBA", image.size, (28, 28, 28) if dark_mode else (255, 255, 255)
        )
        return Image.alpha_composite(blank, image.convert("RGBA")).convert("RGB"), False


def get_time_last_5_min(date: datetime) -> datetime:
    minute = math.floor(date.minute / 5) * 5
    return date.replace(minute=minute, second=0, microsecond=0)


def draw_marker(
    image: ImageFile.ImageFile,
    image_bounderies: ImageBoundaries,
    marker_list: list[Marker],
):
    draw = ImageDraw.ImageDraw(image)
    for marker in marker_list:
        if (
            marker.longitude < image_bounderies.minX
            or marker.longitude > image_bounderies.maxX
            or marker.latitude < image_bounderies.minY
            or marker.latitude > image_bounderies.maxY
        ):
            raise ValueError("Marker location out of boundaries")
        location_relative_to_image = (
            (
                (marker.longitude - image_bounderies.minX)
                / (image_bounderies.maxX - image_bounderies.minX)
            )
            * image.width,
            (
                (image_bounderies.maxY - marker.latitude)
                / (image_bounderies.maxY - image_bounderies.minY)
            )
            * image.height,
        )
        if marker.shape == MarkerShape.CIRCLE:
            draw.circle(
                location_relative_to_image,
                round(marker.size / 2, 0),
                fill=marker.colorRGB,
            )
        elif marker.shape == MarkerShape.CROSS:
            size = round(marker.size / 2, 0)
            draw.line(
                [
                    (
                        location_relative_to_image[0] - size,
                        location_relative_to_image[1],
                    ),
                    (
                        location_relative_to_image[0] + size,
                        location_relative_to_image[1],
                    ),
                ],
                marker.colorRGB,
                marker.width,
            )
            draw.line(
                [
                    (
                        location_relative_to_image[0],
                        location_relative_to_image[1] - size,
                    ),
                    (
                        location_relative_to_image[0],
                        location_relative_to_image[1] + size,
                    ),
                ],
                marker.colorRGB,
                marker.width,
            )
        elif marker.shape == MarkerShape.SQUARE:
            size = round(marker.size / 2, 0)
            draw.rectangle(
                [
                    (
                        location_relative_to_image[0] - size,
                        location_relative_to_image[1] - size,
                    ),
                    (
                        location_relative_to_image[0] + size,
                        location_relative_to_image[1] + size,
                    ),
                ],
                marker.colorRGB,
            )
    return image
