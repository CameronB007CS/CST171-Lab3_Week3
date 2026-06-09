import requests


API_KEY = "df6980c689a7d11b19b585d5c7d37f76"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Use Celsius; change to "imperial" for Fahrenheit
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)

        if response.status_code == 401:
            print("  [401 Unauthorized] Invalid API key. Please check your API_KEY.")
            return

        elif response.status_code == 404:
            print(f"  [404 Not Found] City '{city}' not found. Please check the name.")
            return

        response.raise_for_status()

        data = response.json()

        city_name      = data["name"]
        country        = data["sys"]["country"]
        temperature    = data["main"]["temp"]
        feels_like     = data["main"]["feels_like"]
        humidity       = data["main"]["humidity"]
        description    = data["weather"][0]["description"].capitalize()
        wind_speed     = data["wind"]["speed"]

        print(f"\nWeather for {city_name}, {country}:")
        print("=" * 40)
        print(f"  Condition   : {description}")
        print(f"  Temperature : {temperature}°C (Feels like {feels_like}°C)")
        print(f"  Humidity    : {humidity}%")
        print(f"  Wind Speed  : {wind_speed} m/s")
        print("=" * 40)

    except requests.exceptions.Timeout:
        print("  [Timeout] The request timed out. Try again later.")

    except requests.exceptions.ConnectionError:
        print("  [Connection Error] Could not connect. Check your internet connection.")

    except requests.exceptions.RequestException as e:
        print(f"  [Error] Something went wrong: {e}")


if __name__ == "__main__":
    city = input("Enter a city name: ")
    get_weather(city)