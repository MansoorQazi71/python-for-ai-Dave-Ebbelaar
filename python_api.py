# api's
import requests

# We need coordinates to get weather data
# latitude = 33.6844   # Home latitude
# longitude = 73.0479   # Home longitude

# # Build the API URL with our parameters
# url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# # Make the request
# response = requests.get(url)
# data = response.json()

# print(data)

import requests

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

# Get temperature for different cities
paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)
home_temp = get_weather(33.6844, 73.0479)

print(f"Paris: {paris_temp}°C")
print(f"London: {london_temp}°C")
print(f"Tokyo: {tokyo_temp}°C")
print(f"Home: {home_temp}°C")