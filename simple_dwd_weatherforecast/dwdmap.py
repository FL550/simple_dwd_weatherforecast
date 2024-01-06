import requests
import math
from io import BytesIO
from PIL import Image
from enum import Enum


class WeatherMapType(Enum):
    NIEDERSCHLAGSRADAR = "dwd:Niederschlagsradar"
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

def get_from_location(longitude, latitude, radius_km, map_type: WeatherMapType, background_type: WeatherBackgroundMapType = WeatherBackgroundMapType.BUNDESLAENDER, image_width=520, image_height=580):
    if radius_km <= 0:
        raise ValueError("Radius must be greater than 0")
    if latitude < -90 or latitude > 90:
        raise ValueError("Latitude must be between -90 and 90")
    if longitude < -180 or longitude > 180:
        raise ValueError("Longitude must be between -180 and 180")
    radius = math.fabs(radius_km / (111.3 * math.cos(latitude)))
    return get_map(latitude-radius, longitude-radius, latitude+radius, longitude+radius, map_type, background_type, image_width, image_height)

def get_germany(map_type: WeatherMapType, background_type: WeatherBackgroundMapType = WeatherBackgroundMapType.BUNDESLAENDER, image_width=520, image_height=580):
    return get_map(4.4, 46.4, 16.1, 55.6, map_type, background_type, image_width, image_height)

def get_map(minx,miny,maxx,maxy, map_type: WeatherMapType, background_type: WeatherBackgroundMapType, image_width=520, image_height=580):
    if image_width > 1200 or image_height > 1400:
        raise ValueError("Width and height must not exceed 1200 and 1400 respectively. Please be kind to the DWD servers.")

    url = f"https://maps.dwd.de/geoserver/dwd/wms?service=WMS&version=1.1.0&request=GetMap&layers={map_type.value},{background_type.value}&bbox={minx},{miny},{maxx},{maxy}&width={image_width}&height={image_height}&srs=EPSG:4326&styles=&format=image/png"
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        image = Image.open(BytesIO(request.content))
        return image