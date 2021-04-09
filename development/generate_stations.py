from secret import API_KEY
import requests
from requests.exceptions import Timeout

in_file = open("stations.txt", "r")
data = in_file.readlines()
in_file.close()
for i in range(3):
    data[i] = data[i][12:-13]

range_iter = iter(range(len(data) - 3))
for i in range_iter:
    if len(data[i + 3]) <= 1:
        next(range_iter)
        next(range_iter)
        next(range_iter)
        continue
    data[i + 3] = data[i + 3][12:-13]
    _lat = data[i + 3][33:39].strip().split(".")
    _lat = round(float(_lat[0]) + float(_lat[1]) / 60, 2)
    _lon = data[i + 3][41:47].strip().split(".")
    _lon = round(float(_lon[0]) + float(_lon[1]) / 60, 2)
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={_lat},{_lon}&location_type=APPROXIMATE&result_type=administrative_area_level_1&language=de&key={API_KEY}"
    try:
        request = requests.get(url, timeout=10)
    except Timeout:
        print("Timeout")
    else:
        region = ""
        request = request.json()
        if request["status"] == "OK":
            region = request["results"][0]["address_components"][0]["long_name"]
            print(region)
        data[i + 3] += f" {region}"

f = open("stations.py", "w")
f.write('stations = """\n')
data_iter = iter(data[1:])
for line in data_iter:
    if len(line) <= 1:
        next(data_iter)
        next(data_iter)
        next(data_iter)
        continue
    f.write(line)
    f.write("\n")
f.write('"""')
f.close()