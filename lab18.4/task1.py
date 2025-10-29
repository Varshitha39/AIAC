import os
import requests
import json




def get_weather(city):
    api_key = "3302d53d7e1735c74d4bea7dd58af6e1"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    print(json.dumps(response.json(), indent=4))


    """
    Fetch current weather for `city` from OpenWeatherMap and print JSON.

    - city: city name (e.g. 'London,uk' or 'Beijing')
    - api_key: OpenWeatherMap API key. If None, reads OPENWEATHER_API_KEY env var.

    This function intentionally has no error handling per the user's request.
    It prints the raw JSON response (pretty-printed) to stdout.
    """

# Example usage
get_weather("Hyderabad")
