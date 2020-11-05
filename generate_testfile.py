from simple_dwd_weatherforecast import dwdforecast

in_file = open("TEST_N4333.kml", "rb")
data = in_file.read()
in_file.close()

dwd_weather = dwdforecast.Weather("N4333")
dwd_weather.parse_kml(data)
f = open('test_data.py', 'w')
f.write('parsed_data = ' + repr(dwd_weather.forecast_data))
f.close()
