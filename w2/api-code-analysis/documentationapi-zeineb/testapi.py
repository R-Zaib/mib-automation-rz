import requests

# Base URL for NWS Aviation Weather API
base_url = "https://aviationweather.gov/adds/dataserver_current/httpparam"


response_nonexistent = requests.get(base_url + "/fer75tddd")
print("Status code:", response_nonexistent.status_code) 

# Example station code 
station = "KJFK"
response_taf = requests.get(base_url + "/taf?stationString=" + station)

print(" Status code:", response_taf.status_code)

# Fetch METAR data for the station
response_metar = requests.get(base_url + "/metar?")

print("Status code:", response_metar.status_code)




