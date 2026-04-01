"""DWD rain radar composite data for short-term precipitation forecasts.

This module provides access to the DWD (Deutscher Wetterdienst) rain radar
composite data, which delivers precipitation forecasts for the next ~2 hours
in 5-minute steps with 1 km resolution across Germany.

Data source: DWD OpenData (https://opendata.dwd.de)
"""

from __future__ import annotations

import math
import struct
import tarfile
from datetime import UTC, datetime, timedelta
from io import BytesIO

import requests

RADAR_URL = "https://opendata.dwd.de/weather/radar/composite/rv/DE1200_RV_LATEST.tar.bz2"

_XSIZE = 1100
_YSIZE = 1200


class NotInAreaError(Exception):
    """Raised when a location is outside the DWD radar coverage area (Germany)."""


class RadarNotAvailableError(Exception):
    """Raised when radar data has not been downloaded yet."""


def _linear_interp(x: float, xp: list[float], fp: list[float]) -> float:
    """
    Perform linear interpolation.

    Args:
        x: The x-value to interpolate at.
        xp: Sorted list of known x-values.
        fp: Corresponding y-values for xp.

    Returns:
        Interpolated y-value.

    """
    if not xp:
        return 0.0
    if x <= xp[0]:
        return fp[0]
    if x >= xp[-1]:
        return fp[-1]
    for i in range(len(xp) - 1):
        if xp[i] <= x <= xp[i + 1]:
            t = (x - xp[i]) / (xp[i + 1] - xp[i])
            return fp[i] * (1 - t) + fp[i + 1] * t
    return fp[-1]


class DWDRadar:
    """
    Short-term precipitation forecasts from the DWD rain radar composite.

    Downloads and parses the DE1200_RV radar composite, which provides
    precipitation intensities (mm/h) for the next ~2 hours in 5-minute steps
    on a 1 km grid covering Germany.

    Usage::

        from simple_dwd_weatherforecast.dwdradar import DWDRadar

        radar = DWDRadar()
        radar.update()

        # Precipitation forecast for a location (e.g. Berlin)
        forecast = radar.get_precipitation_values(52.52, 13.41)

        # Next rain event details
        next_rain = radar.get_next_precipitation(52.52, 13.41)

    """

    def __init__(self) -> None:
        """Initialize the DWDRadar instance."""
        self._radars: dict[datetime, bytes] | None = None

    def update(self) -> None:
        """Download and parse the latest radar composite data from DWD OpenData."""
        try:
            response = requests.get(RADAR_URL, timeout=30)
            response.raise_for_status()
            with tarfile.open(fileobj=BytesIO(response.content), mode="r:bz2") as tar:
                radars: dict[datetime, bytes] = {}
                for member in tar.getmembers():
                    try:
                        radar_minute_delta = int(member.name[-3:])
                        radar_time = datetime.strptime(
                            member.name[-14:-4], "%y%m%d%H%M"
                        ).replace(tzinfo=UTC) + timedelta(minutes=radar_minute_delta)
                        f = tar.extractfile(member)
                        if f is None:
                            continue
                        raw = f.read()
                        # Binary data follows the first ETX (\x03) separator
                        content = raw.split(b"\x03", 1)[1]
                        radars[radar_time] = content
                    except (ValueError, IndexError):
                        continue
                self._radars = radars
        except Exception as error:  # noqa: BLE001
            print(f"Error in DWDRadar.update: {type(error)} args: {error.args}")  # noqa: T201

    def _get_grid_index(self, lat: float, lon: float) -> tuple[int, int]:
        """
        Convert geographic coordinates to radar grid indices.

        Uses the DWD stereographic projection for the DE1200 composite.

        Args:
            lat: Latitude in decimal degrees.
            lon: Longitude in decimal degrees.

        Returns:
            Tuple of (x_cart, y_cart) grid indices.

        Raises:
            NotInAreaError: If the location is outside the radar coverage area.
            RadarNotAvailableError: If radar data has not been downloaded yet.

        """
        if self._radars is None:
            raise RadarNotAvailableError
        x_cart = int(
            6370.04
            * (1 + math.sin(60 / 180 * math.pi))
            / (1 + math.sin(lat / 180 * math.pi))
            * math.cos(lat / 180 * math.pi)
            * math.sin((lon - 10) / 180 * math.pi)
            + 543.4622
        )
        y_cart = int(
            -6370.04
            * (1 + math.sin(60 / 180 * math.pi))
            / (1 + math.sin(lat / 180 * math.pi))
            * math.cos(lat / 180 * math.pi)
            * math.cos((lon - 10) / 180 * math.pi)
            + 4808.645
        )
        if not (0 <= y_cart < _YSIZE) or not (0 <= x_cart < _XSIZE):
            raise NotInAreaError
        return x_cart, y_cart

    def _decode_value(self, raw: int) -> float:
        """
        Decode a raw uint16 radar value to precipitation intensity in mm/h.

        The radar data uses the following encoding:

        - Bits 0-11: raw value (0-4095)
        - Bit 13 set: no valid data (treat as 0)
        - Value in mm/h = raw_value / 100 * 12

        """
        if raw & 0b0010000000000000:
            return 0.0
        return float(raw & 0b0000111111111111) / 100 * 12

    def get_precipitation_values(
        self, lat: float, lon: float
    ) -> dict[datetime, float]:
        """
        Get precipitation values for a location at all available time steps.

        Args:
            lat: Latitude in decimal degrees.
            lon: Longitude in decimal degrees.

        Returns:
            Ordered dictionary mapping UTC datetime objects to precipitation
            intensity in mm/h.

        Raises:
            NotInAreaError: If the location is outside the radar coverage area.
            RadarNotAvailableError: If radar data has not been downloaded yet.

        """
        if self._radars is None:
            raise RadarNotAvailableError
        x_cart, y_cart = self._get_grid_index(lat, lon)
        values: dict[datetime, float] = {}
        for radar_time, content in self._radars.items():
            idx = y_cart * _XSIZE + x_cart
            (raw,) = struct.unpack_from("<H", content, idx * 2)
            values[radar_time] = self._decode_value(raw)
        return dict(sorted(values.items()))

    def get_current_precipitation(
        self, lat: float, lon: float, timestamp: datetime
    ) -> float:
        """
        Get the interpolated precipitation intensity at a specific time.

        Args:
            lat: Latitude in decimal degrees.
            lon: Longitude in decimal degrees.
            timestamp: The datetime to query (timezone-aware recommended).

        Returns:
            Interpolated precipitation intensity in mm/h.

        Raises:
            NotInAreaError: If the location is outside the radar coverage area.
            RadarNotAvailableError: If radar data has not been downloaded yet.

        """
        values = self.get_precipitation_values(lat, lon)
        times = list(values.keys())
        precip = list(values.values())
        return _linear_interp(
            timestamp.timestamp(),
            [t.timestamp() for t in times],
            precip,
        )

    def get_next_precipitation(
        self, lat: float, lon: float
    ) -> dict[str, datetime | timedelta | float | None]:
        """
        Get details about the next precipitation event.

        Scans the forecast time steps and identifies the first rain event
        (start, end, duration, intensity).

        Args:
            lat: Latitude in decimal degrees.
            lon: Longitude in decimal degrees.

        Returns:
            Dictionary with the following keys:

            - ``start``: UTC datetime when precipitation begins, or ``None``
              if no rain is forecast.
            - ``end``: UTC datetime when precipitation ends, or ``None`` if
              rain is forecast until the end of the available data.
            - ``length``: timedelta of the precipitation duration, or ``None``.
            - ``max``: Maximum precipitation intensity in mm/h.
            - ``sum``: Total precipitation amount in mm.

        Raises:
            NotInAreaError: If the location is outside the radar coverage area.
            RadarNotAvailableError: If radar data has not been downloaded yet.

        """
        rain_start: datetime | None = None
        rain_end: datetime | None = None
        rain_max = 0.0
        rain_sum = 0.0

        for rain_time, precipitation in self.get_precipitation_values(
            lat, lon
        ).items():
            if rain_start is None and precipitation > 0:
                rain_start = rain_time
                rain_max = precipitation
                rain_sum = precipitation
                continue
            if rain_start is not None:
                rain_max = max(rain_max, precipitation)
                rain_sum += precipitation
            if rain_start is not None and rain_end is None and precipitation == 0:
                rain_end = rain_time
                continue
            if rain_start is not None and rain_end is not None and precipitation != 0:
                rain_end = None
                continue
            if rain_start is not None and rain_end is not None and precipitation == 0:
                break

        rain_length: timedelta | None = None
        if rain_start is not None:
            if rain_end is not None:
                rain_length = rain_end - rain_start
            # Each sample covers 5 minutes (1/12 of an hour); convert sum to mm
            rain_sum = rain_sum / 12

        return {
            "start": rain_start,
            "end": rain_end,
            "length": rain_length,
            "max": rain_max,
            "sum": rain_sum,
        }
