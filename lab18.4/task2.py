import os
import requests
import json


def get_weather(city, api_key=None, timeout=10):
    """
    Fetch current weather for `city` from OpenWeatherMap and print JSON.

    - city: city name (e.g. 'London,uk' or 'Beijing')
    - api_key: OpenWeatherMap API key. If None, reads OPENWEATHER_API_KEY env var or falls back to a bundled key.
    - timeout: network timeout in seconds.

    This function includes basic error handling for:
      - Invalid URL
      - Network timeout
      - Wrong API key (401)
      - City not found (404)
      - Other network/HTTP errors

    On success it prints the weather JSON (pretty-printed). On error it prints a user-friendly message.
    """
    if api_key is None:
        api_key = os.getenv("OPENWEATHER_API_KEY") or "3302d53d7e1735c74d4bea7dd58af61"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url, timeout=timeout)
        # Try to parse JSON body
        data = response.json()

        if response.status_code == 200:
            print(json.dumps(data, indent=4))
        elif response.status_code == 401:
            print("Error: Invalid API key (401). Please check your OpenWeatherMap API key.")
        elif response.status_code == 404:
            print(f"Error: City '{city}' not found (404). Check the city name.")
        else:
            # Try to include API-provided message when available
            message = data.get("message") if isinstance(data, dict) else None
            print(f"Error: HTTP {response.status_code}. {message or 'Unexpected response from the weather service.'}")

    except requests.exceptions.InvalidURL:
        print("Error: The constructed URL is invalid. Check the city name and API base URL.")
    except requests.exceptions.Timeout:
        print("Error: Network timeout occurred while contacting the weather service.")
    except requests.exceptions.RequestException as e:
        print(f"Error: Network error occurred: {e}")


# Example usage
if __name__ == "__main__":
    get_weather("Hyderabad")
