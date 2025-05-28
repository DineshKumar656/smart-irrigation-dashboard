# irrigation_logic.py

import requests
from config import OPENWEATHER_API_KEY, CITY_NAME

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)

    if not response.text.strip():
        raise Exception("❌ Empty response from OpenWeatherMap")

    data = response.json()

    if "main" not in data:
        raise Exception("Weather data missing 'main' section")

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    rainfall = data.get("rain", {}).get("1h", 0)

    return temp, humidity, rainfall

def should_irrigate(temp, humidity, rainfall):
    return temp > 30 and humidity < 50 and rainfall < 1
