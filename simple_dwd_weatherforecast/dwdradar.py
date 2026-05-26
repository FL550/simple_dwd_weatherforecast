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

RADAR_URL = (
    "https://opendata.dwd.de/weather/radar/composite/rv/DE1200_RV_LATEST.tar.bz2"
)

_XSIZE = 1100
_YSIZE = 1200

# Compass directions (name, dx, dy) – dx positive = East, dy positive = South
# The grid's y-axis increases southward, so "north" means negative dy.
_DIRECTIONS = [
    ("N", 0, -1),
    ("NE", 1, -1),
    ("E", 1, 0),
    ("SE", 1, 1),
    ("S", 0, 1),
    ("SW", -1, 1),
    ("W", -1, 0),
    ("NW", -1, -1),
]

# Meteorological bearing (degrees from north, clockwise) for each compass label.
_DIRECTION_DEGREES: dict[str, float] = {
    "N": 0.0,
    "NE": 45.0,
    "E": 90.0,
    "SE": 135.0,
    "S": 180.0,
    "SW": 225.0,
    "W": 270.0,
    "NW": 315.0,
}

# How many 5-minute look-back frames to examine when determining direction.
_DIRECTION_LOOKBACK_STEPS = 3
# Radius in grid cells (≈ km) to scan in each compass direction.
_DIRECTION_SCAN_RADIUS = 20
# Local noise filter defaults for isolated false echoes.
_NOISE_WINDOW_RADIUS = 3
_NOISE_MIN_CONNECTED_PIXELS = 4
_NOISE_INTENSITY_THRESHOLD = 0.12


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
        self._etag: str | None = None

    def update(self) -> None:
        """Download and parse the latest radar composite data from DWD OpenData."""
        try:
            headers = {"If-None-Match": self._etag} if self._etag else None
            response = requests.get(RADAR_URL, timeout=30, headers=headers)
            if response.status_code == 304:
                return
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
                self._etag = response.headers.get("ETag")
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

    def _get_grid_value(self, x: int, y: int, content: bytes) -> float:
        """
        Read a decoded precipitation value from a radar frame at grid position (x, y).

        Args:
            x: Grid x-index (0 … _XSIZE-1).
            y: Grid y-index (0 … _YSIZE-1).
            content: Raw binary radar frame.

        Returns:
            Precipitation intensity in mm/h, or 0.0 if the position is out of bounds.

        """
        if not (0 <= x < _XSIZE) or not (0 <= y < _YSIZE):
            return 0.0
        idx = y * _XSIZE + x
        (raw,) = struct.unpack_from("<H", content, idx * 2)
        return self._decode_value(raw)

    def _is_valid_precipitation_pixel(self, x: int, y: int, content: bytes) -> bool:
        """Return whether a pixel belongs to a sufficiently large local wet area."""
        if self._get_grid_value(x, y, content) < _NOISE_INTENSITY_THRESHOLD:
            return False

        min_x = max(0, x - _NOISE_WINDOW_RADIUS)
        max_x = min(_XSIZE - 1, x + _NOISE_WINDOW_RADIUS)
        min_y = max(0, y - _NOISE_WINDOW_RADIUS)
        max_y = min(_YSIZE - 1, y + _NOISE_WINDOW_RADIUS)

        visited: set[tuple[int, int]] = set()
        stack = [(x, y)]
        connected = 0

        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in visited:
                continue
            visited.add((cx, cy))
            if self._get_grid_value(cx, cy, content) < _NOISE_INTENSITY_THRESHOLD:
                continue
            connected += 1
            if connected >= _NOISE_MIN_CONNECTED_PIXELS:
                return True

            for nx in range(max(min_x, cx - 1), min(max_x, cx + 1) + 1):
                for ny in range(max(min_y, cy - 1), min(max_y, cy + 1) + 1):
                    if nx == cx and ny == cy:
                        continue
                    if (nx, ny) not in visited:
                        stack.append((nx, ny))

        return False

    def _get_filtered_grid_value(self, x: int, y: int, content: bytes) -> float:
        """Return filtered precipitation value (suppresses isolated local echoes)."""
        value = self._get_grid_value(x, y, content)
        if value < _NOISE_INTENSITY_THRESHOLD:
            return 0.0
        if not self._is_valid_precipitation_pixel(x, y, content):
            return 0.0
        return value

    def _scan_directions(
        self, x_cart: int, y_cart: int, content: bytes, radius: int
    ) -> dict[str, float]:
        """
        Scan precipitation in 8 compass directions around a grid point.

        For each direction a line of *radius* pixels is sampled and the
        average intensity is returned.

        Args:
            x_cart: Grid x-index of the location.
            y_cart: Grid y-index of the location.
            content: Raw binary radar frame.
            radius: Number of pixels to scan in each direction.

        Returns:
            Dictionary mapping compass label (e.g. ``"N"``) to average
            precipitation intensity in mm/h along that direction.

        """
        result: dict[str, float] = {}
        for label, dx, dy in _DIRECTIONS:
            total = 0.0
            for step in range(1, radius + 1):
                total += self._get_filtered_grid_value(
                    x_cart + dx * step, y_cart + dy * step, content
                )
            result[label] = total / radius
        return result

    def _determine_rain_direction(
        self, x_cart: int, y_cart: int, rain_start: datetime
    ) -> tuple[float, str] | tuple[None, None]:
        """
        Estimate the compass direction from which precipitation is approaching.

        Analyses the radar frames *before* ``rain_start`` and identifies
        the direction that shows the highest average precipitation signal
        (i.e. the region the rain cell is coming from).

        Args:
            x_cart: Grid x-index of the location.
            y_cart: Grid y-index of the location.
            rain_start: UTC datetime when precipitation was detected at the
                location.

        Returns:
            A ``(degrees, label)`` tuple where *degrees* is the meteorological
            bearing (0 = N, 90 = E, …) and *label* is the compass string
            (``"N"``, ``"NE"``, …).  Returns ``(None, None)`` when there are
            no look-back frames available.

        """
        assert self._radars is not None  # guaranteed by callers
        sorted_times = sorted(self._radars)
        pre_start = [t for t in sorted_times if t < rain_start]
        if not pre_start:
            return None, None
        frames = pre_start[-_DIRECTION_LOOKBACK_STEPS:]
        # Accumulate directional precipitation across look-back frames.
        totals: dict[str, float] = {label: 0.0 for label, *_ in _DIRECTIONS}
        for t in frames:
            scan = self._scan_directions(
                x_cart, y_cart, self._radars[t], _DIRECTION_SCAN_RADIUS
            )
            for label, value in scan.items():
                totals[label] += value
        best_label = max(totals, key=lambda k: totals[k])
        return _DIRECTION_DEGREES[best_label], best_label

    def get_precipitation_values(self, lat: float, lon: float) -> dict[datetime, float]:
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
            values[radar_time] = self._get_filtered_grid_value(x_cart, y_cart, content)
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
    ) -> dict[str, datetime | timedelta | float | str | None]:
        """
        Get details about the next precipitation event.

        Scans the forecast time steps and identifies the first rain event
        (start, end, duration, intensity, direction).

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
            - ``direction_deg``: Meteorological bearing (float, 0 = N clockwise)
              of the direction from which the rain is approaching, or ``None``
              if it cannot be determined (no look-back frames available or no
              rain forecast).
            - ``direction``: Compass label (e.g. ``"NW"``) corresponding to
              ``direction_deg``, or ``None``.

        Raises:
            NotInAreaError: If the location is outside the radar coverage area.
            RadarNotAvailableError: If radar data has not been downloaded yet.

        """
        rain_start: datetime | None = None
        rain_end: datetime | None = None
        rain_max = 0.0
        rain_sum = 0.0

        x_cart, y_cart = self._get_grid_index(lat, lon)

        for rain_time, precipitation in self.get_precipitation_values(lat, lon).items():
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

        direction_deg: float | None = None
        direction: str | None = None
        if rain_start is not None:
            direction_deg, direction = self._determine_rain_direction(
                x_cart, y_cart, rain_start
            )

        return {
            "start": rain_start,
            "end": rain_end,
            "length": rain_length,
            "max": rain_max,
            "sum": rain_sum,
            "direction_deg": direction_deg,
            "direction": direction,
        }
