"""Base map from BKG TopPlusOpen to put underneath DWD weather layers.

The background layers of the DWD map server are area polygons or a satellite
mosaic; none of them shows towns, roads or rivers. TopPlusOpen, published by the
German Federal Agency for Cartography and Geodesy (BKG), is served for the same
bounding box, coordinate system and image size, so a transparent DWD image fits
on top of it without any reprojection.

Data source: https://sgx.geodatenzentrum.de/wms_topplus_open
Licence: dl-de/by-2-0 (https://www.govdata.de/dl-de/by-2-0). It requires a source
note, which BaseMap.apply() draws onto the image. See also BaseMap.attribution.
"""

from __future__ import annotations

import hashlib
import logging
import threading
from datetime import UTC, datetime, timedelta
from enum import Enum
from functools import lru_cache
from io import BytesIO
from pathlib import Path

import numpy as np
import requests
from PIL import Image, ImageChops, ImageDraw, ImageFont

_LOGGER = logging.getLogger(__name__)

BASEMAP_URL = "https://sgx.geodatenzentrum.de/wms_topplus_open"
_LAYER = "web_light"
_DATA_SOURCES_URL = (
    "https://sgx.geodatenzentrum.de/web_public/gdz/datenquellen/"
    "datenquellen_topplusopen.html"
)

_TIMEOUT = 30

# The map changes a few times a year, so it is downloaded rarely and kept.
_MAX_AGE = timedelta(days=90)

# How long to leave the server alone after a failed download: without any map,
# and with an old copy that can still be shown.
_RETRY_AFTER = timedelta(minutes=1)
_RETRY_AFTER_STALE = timedelta(days=1)

_NOTE_FONT_SIZE = 12
_NOTE_PADDING = 4


class BaseMapStyle(Enum):
    """Available styles of the base map."""

    LIGHT = "light"
    DARK = "dark"


class BaseMapNotAvailableError(Exception):
    """Raised when there is neither a stored base map nor a reachable server."""


class BaseMap:
    """Base map of one map section in one image size.

    The image is kept in memory and, if cache_dir is given, on disk. All methods
    are thread safe; concurrent calls cause a single download.
    """

    def __init__(
        self,
        minx: float,
        miny: float,
        maxx: float,
        maxy: float,
        image_width: int,
        image_height: int,
        style: BaseMapStyle = BaseMapStyle.LIGHT,
        cache_dir: str | None = None,
    ) -> None:
        """Define the map section; nothing is downloaded yet."""
        self._bbox = (minx, miny, maxx, maxy)
        self._size = (image_width, image_height)
        self._style = style
        self._cache_dir = cache_dir
        self._image: Image.Image | None = None
        self._loaded: datetime | None = None
        self._retry_after: datetime | None = None
        self._lock = threading.Lock()

    @property
    def attribution(self) -> str:
        """The complete source note required by the licence."""
        return attribution(self._style, self._year())

    @property
    def available(self) -> bool:
        """Whether a base map can be drawn, downloading it if necessary."""
        try:
            self.get_image()
        except BaseMapNotAvailableError:
            return False
        return True

    def get_image(self) -> Image.Image:
        """Return the base map from memory, from disk or from the server.

        An image older than 90 days is downloaded again. If that fails, the old
        one stays in use.
        """
        with self._lock:
            if self._image is None:
                self._read_from_disk()
            if self._image is None or self._is_outdated():
                self._download()
            if self._image is None:
                msg = f"Base map not available from {BASEMAP_URL}"
                raise BaseMapNotAvailableError(msg)
            return self._image

    def apply(self, weather_image: Image.Image, *, blend: bool = False) -> Image.Image:
        """Put a transparent weather image onto the base map.

        With blend the map stays readable below the weather. The result is opaque
        and contains the source note.
        """
        weather = weather_image.convert("RGBA")
        if blend:
            image = self._blend(weather)
        else:
            image = Image.alpha_composite(self.get_image(), weather).convert("RGB")
        self._draw_source_note(image)
        return image

    def _blend(self, weather: Image.Image) -> Image.Image:
        # Opacity would shift the colors, which are a scale. Multiplying leaves them
        # as they are on the white of the light map and lets its dark names show
        # through. Screening does the same for the black and the light names of the
        # dark map.
        dark = self._style is BaseMapStyle.DARK
        operation = ImageChops.screen if dark else ImageChops.multiply
        base = self.get_image().convert("RGB")
        blended = operation(base, weather.convert("RGB"))
        return Image.composite(blended, base, weather.getchannel("A"))

    def _year(self) -> int:
        return (self._loaded or datetime.now(UTC)).year

    def _is_outdated(self) -> bool:
        return self._loaded is None or datetime.now(UTC) - self._loaded > _MAX_AGE

    def _cache_file(self) -> Path | None:
        if self._cache_dir is None:
            return None
        section = ",".join(str(value) for value in self._bbox)
        digest = hashlib.sha256(section.encode()).hexdigest()[:12]
        width, height = self._size
        name = f"topplus_{self._style.value}_{width}x{height}_{digest}.png"
        return Path(self._cache_dir) / name

    def _read_from_disk(self) -> None:
        path = self._cache_file()
        if path is None or not path.is_file():
            return
        try:
            with Image.open(path) as image:
                self._image = image.convert("RGBA")
            self._loaded = datetime.fromtimestamp(path.stat().st_mtime, UTC)
        except (OSError, ValueError) as e:
            _LOGGER.warning("Could not read base map %s: %s", path, e)

    def _download(self) -> None:
        now = datetime.now(UTC)
        # Many frames may be drawn in a row: do not retry for every one of them.
        if self._retry_after is not None and now < self._retry_after:
            return
        try:
            image = self._request_image()
        except (requests.RequestException, OSError, ValueError) as e:
            wait = _RETRY_AFTER if self._image is None else _RETRY_AFTER_STALE
            self._retry_after = now + wait
            _LOGGER.warning("Could not download base map, next try in %s: %s", wait, e)
            return
        self._image = image
        self._loaded = now
        self._retry_after = None
        self._write_to_disk()

    def _request_image(self) -> Image.Image:
        minx, miny, maxx, maxy = self._bbox
        width, height = self._size
        url = (
            f"{BASEMAP_URL}?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap"
            f"&LAYERS={_LAYER}&STYLES=&CRS=EPSG:4326&BBOX={miny},{minx},{maxy},{maxx}"
            f"&WIDTH={width}&HEIGHT={height}&FORMAT=image/png"
        )
        response = requests.get(url, timeout=_TIMEOUT)
        response.raise_for_status()
        # A service exception arrives as XML with status 200; it is no image either.
        image = Image.open(BytesIO(response.content)).convert("RGBA")
        if image.size != self._size:
            msg = f"Unexpected image size: {image.size}"
            raise ValueError(msg)
        if self._style is BaseMapStyle.DARK:
            image = invert_lightness(image)
        return image

    def _write_to_disk(self) -> None:
        path = self._cache_file()
        if path is None or self._image is None:
            return
        # Not being able to store the map must not cost the map itself.
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            temporary = path.with_suffix(".tmp")
            self._image.save(temporary, format="PNG")
            temporary.replace(path)
        except OSError as e:
            _LOGGER.warning("Could not store base map %s: %s", path, e)

    def _draw_source_note(self, image: Image.Image) -> None:
        dark = self._style is BaseMapStyle.DARK
        text = f"© BKG ({self._year()}) dl-de/by-2-0"
        if dark:
            text += " (modified)"
        font = ImageFont.load_default(size=_NOTE_FONT_SIZE)
        draw = ImageDraw.Draw(image)
        _, _, width, height = draw.textbbox((0, 0), text, font=font)
        top = image.height - height - 2 * _NOTE_PADDING
        # The text alone would be lost between the place names.
        draw.rectangle(
            (0, top, width + 2 * _NOTE_PADDING, image.height),
            fill=(20, 20, 20) if dark else (255, 255, 255),
        )
        draw.text(
            (_NOTE_PADDING, top + _NOTE_PADDING),
            text,
            fill=(150, 150, 150) if dark else (90, 90, 90),
            font=font,
        )


@lru_cache(maxsize=4)
def get_basemap(
    minx: float,
    miny: float,
    maxx: float,
    maxy: float,
    image_width: int,
    image_height: int,
    style: BaseMapStyle = BaseMapStyle.LIGHT,
    cache_dir: str | None = None,
) -> BaseMap:
    """Return the shared BaseMap of a map section, so it is downloaded only once."""
    return BaseMap(minx, miny, maxx, maxy, image_width, image_height, style, cache_dir)


def attribution(
    style: BaseMapStyle = BaseMapStyle.LIGHT, year: int | None = None
) -> str:
    """Return the complete source note required by the licence.

    The year is the one of the last download, the current year by default.
    """
    year = year or datetime.now(UTC).year
    modified = ", Daten verändert" if style is BaseMapStyle.DARK else ""
    return (
        f"Kartendarstellung: © BKG ({year}) dl-de/by-2-0{modified}, "
        f"Datenquellen: {_DATA_SOURCES_URL}"
    )


def invert_lightness(image: Image.Image) -> Image.Image:
    """Turn a light map into a dark one, keeping hue and saturation.

    Inverting RGB would turn blue rivers orange. The lightness of a pixel is
    (max + min) / 2, so adding 255 - max - min to all three channels mirrors it
    and leaves the differences between them, hence hue and saturation, untouched.
    """
    pixels = np.asarray(image.convert("RGBA"), dtype=np.int16).copy()
    rgb = pixels[..., :3]
    shift = 255 - rgb.max(axis=2, keepdims=True) - rgb.min(axis=2, keepdims=True)
    pixels[..., :3] = rgb + shift
    return Image.fromarray(pixels.astype(np.uint8))
