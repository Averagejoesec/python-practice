import requests
from dotenv import load_dotenv
import os
from flask import Flask

load_dotenv()

# Replace with your OpenWeatherMap API key
API_KEY = os.environ.get('WEATHER_API_KEY')

def get_temperature(city):
    """Fetches the current temperature for a given city.

    Args:
    city: The name of the city to get weather data for.

    Returns:
    A string containing the current temperature in Celsius or None if an error occurs.
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        return f"Current temperature in {city}: {temp:.1f}°C"
    else:
        print(f"Error: {response.status_code}")
        return None


if __name__ == "__main__":
    city = input("Enter City: ")

    temperature = get_temperature(city)
    if temperature:
        print(temperature)
    else:
        print("Failed to retrieve temperature.") 