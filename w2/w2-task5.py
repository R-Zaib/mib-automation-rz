"""
5. IP weather
   - Create a program that gets an IP address as user input then it prints the weather on the IP address location.
   - Use one of the following APIs:
     - https://www.geojs.io/docs/v1/endpoints/geo/
     - https://open-meteo.com/en
"""
import requests

def get_location(ip_address):
    # GeoJS API endpoint for IP address geolocation
    geojs_url = f'https://get.geojs.io/v1/ip/geo/{ip_address}.json'
    
    # Send HTTP request to GeoJS API
    response = requests.get(geojs_url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        location_data = response.json()
        return location_data
    else:
        print(f"Error: Unable to retrieve location data. Status code: {response.status_code}")
        return None

def get_weather(latitude, longitude):
    # Open-Meteo API endpoint for weather information
    open_meteo_url = f'https://api.open-meteo.com/weather?latitude={latitude}&longitude={longitude}&daily=temperature_2m_min_max_7d'
    
    # Send HTTP request to Open-Meteo API
    response = requests.get(open_meteo_url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error: Unable to retrieve weather data. Status code: {response.status_code}")
        return None

# Get user input for the IP address
ip_address = input("Enter an IP address: ")

# Get location data using GeoJS API
location_info = get_location(ip_address)

if location_info:
    # Extract latitude and longitude from location data
    latitude = location_info['latitude']
    longitude = location_info['longitude']
    
    # Get weather data using Open-Meteo API
    weather_info = get_weather(latitude, longitude)

    if weather_info:
        # Print relevant weather information
        print(f"\nWeather information for {ip_address} location:")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
        print("Temperature (Min/Max):", weather_info['daily']['temperature_2m_min_max_7d'])
    else:
        print("Weather information could not be retrieved.")
else:
    print("Location information could not be retrieved.")
