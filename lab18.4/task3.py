import os
import sys
import requests


def get_weather(city, api_key=None, timeout=10):
    """
    Fetch current weather for `city` from OpenWeatherMap and print a user-friendly
    summary with extracted fields:
      • City: <name>
      • Temperature: <temp>°C
      • Humidity: <humidity>%
      • Weather: <description>

    - city: city name (e.g. 'London' or 'London,uk')
    - api_key: OpenWeatherMap API key. If None, reads OPENWEATHER_API_KEY env var or falls back to a bundled key.
    - timeout: network timeout in seconds.

    This function prints simple user-friendly output. Basic HTTP errors are
    reported with readable messages.
    """
    if api_key is None:
        api_key = os.getenv("OPENWEATHER_API_KEY") or "3302d53d7e1735c74d4bea7dd58af6e1"

    url = (
        f"http://api.openweathermap.org/data/2.5/weather?q={city}"
        f"&appid={api_key}&units=metric"
    )

    response = requests.get(url, timeout=timeout)
    data = response.json()

    # Handle common HTTP response codes with user-friendly messages
    if response.status_code == 401:
        print("Error: Invalid API key (401). Please check your OpenWeatherMap API key.")
        return
    if response.status_code == 404:
        print(f"Error: City '{city}' not found (404). Check the city name.")
        return
    if response.status_code != 200:
        message = data.get("message") if isinstance(data, dict) else None
        print(f"Error: HTTP {response.status_code}. {message or 'Unexpected response from the weather service.'}")
        return

    # Extract fields
    city_name = data.get("name") or city
    main = data.get("main", {})
    weather_list = data.get("weather", [])

    temp = main.get("temp")
    humidity = main.get("humidity")
    description = None
    if weather_list and isinstance(weather_list, list):
        description = weather_list[0].get("description")

    # Format values for display
    temp_str = f"{temp:.0f}°C" if isinstance(temp, (int, float)) else "N/A"
    humidity_str = f"{humidity}%" if humidity is not None else "N/A"
    desc_str = description.capitalize() if isinstance(description, str) else "N/A"

    # Print user-friendly bullet list
    print(f"• City: {city_name}")
    print(f"• Temperature: {temp_str}")
    print(f"• Humidity: {humidity_str}")
    print(f"• Weather: {desc_str}")


if __name__ == "__main__":
    # Accept city name as CLI argument, otherwise default to Hyderabad
    if len(sys.argv) > 1:
        city_arg = " ".join(sys.argv[1:])
    else:
        city_arg = "Hyderabad"

    try:
        get_weather(city_arg)
    except requests.exceptions.InvalidURL:
        print("Error: The constructed URL is invalid. Check the city name and API base URL.")
    except requests.exceptions.Timeout:
        print("Error: Network timeout occurred while contacting the weather service.")
    except requests.exceptions.RequestException as e:
        print(f"Error: Network error occurred: {e}")
