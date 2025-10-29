import os
import json
import requests
from datetime import datetime


def get_weather_and_save(city, api_key=None, timeout=10, results_file="results.json"):
    """
    Fetch current weather for `city` from OpenWeatherMap, print user-friendly output,
    and append the results to a JSON file.

    Args:
        city: City name (e.g. 'London' or 'New York')
        api_key: OpenWeatherMap API key (optional)
        timeout: Request timeout in seconds
        results_file: Path to the JSON file for storing results

    The function:
    1. Prints formatted weather to console
    2. Appends results to results.json as:
       [
         {"city": "London", "temp": 18, "humidity": 60, "weather": "Clear sky"},
         {"city": "New York", "temp": 22, "humidity": 55, "weather": "Few clouds"}
       ]
    """
    if api_key is None:
        api_key = os.getenv("OPENWEATHER_API_KEY") or "3302d53d7e1735c74d4bea7dd58af6e1"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url, timeout=timeout)
        data = response.json()

        if response.status_code == 401:
            print("Error: Invalid API key. Please check your API key.")
            return
        if response.status_code == 404:
            print("Error: City not found. Please enter a valid city.")
            return
        if response.status_code != 200:
            message = data.get("message") if isinstance(data, dict) else None
            print(f"Error: HTTP {response.status_code}. {message or 'Unexpected response.'}")
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

        # Print user-friendly output to console
        print(f"City: {city_name}")
        print(f"Temperature: {temp_str}")
        print(f"Humidity: {humidity_str}")
        print(f"Weather: {desc_str}")

        # Prepare data for JSON storage
        weather_data = {
            "city": city_name,
            "temp": round(temp) if isinstance(temp, (int, float)) else None,
            "humidity": humidity,
            "weather": description.capitalize() if description else None,
            "timestamp": datetime.now().isoformat()  # Add timestamp for reference
        }

        # Load existing data or create empty list
        try:
            with open(results_file, 'r') as f:
                stored_data = json.load(f)
                if not isinstance(stored_data, list):
                    stored_data = []
        except (FileNotFoundError, json.JSONDecodeError):
            stored_data = []

        # Append new data and save
        stored_data.append(weather_data)
        with open(results_file, 'w') as f:
            json.dump(stored_data, f, indent=2)

    except requests.exceptions.InvalidURL:
        print("Error: The constructed URL is invalid. Check the city name and API base URL.")
    except requests.exceptions.Timeout:
        print("Error: Network timeout occurred while contacting the weather service.")
    except requests.exceptions.RequestException as e:
        print(f"Error: Network error occurred: {e}")
    except Exception as e:
        print(f"Error: Failed to save results: {e}")


if __name__ == "__main__":
    while True:
        # Prompt for city name
        city = input("Enter city name (or press Enter to quit): ").strip()
        if not city:
            break
        
        # Get and save weather data
        get_weather_and_save(city)
        print("\nResults have been appended to results.json")
        print("-" * 40 + "\n")
