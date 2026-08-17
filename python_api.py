# api's
import requests

# We need coordinates to get weather data
latitude = 33.6844   # Paris latitude
longitude = 73.0479   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data)