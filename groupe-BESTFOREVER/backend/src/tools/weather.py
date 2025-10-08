
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather(city: str) -> dict:
    """
    Fetches the current weather for a given city using the OpenWeatherMap API.

    Args:
        city: The name of the city.

    Returns:
        A dictionary containing the weather data, or an error message.
    """
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return {"error": "OpenWeather API key not found."}

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"An error occurred: {e}"}

