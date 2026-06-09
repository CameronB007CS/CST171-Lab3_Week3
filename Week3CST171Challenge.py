import requests
from datetime import datetime
from collections import defaultdict


API_KEY  = "df6980c689a7d11b19b585d5c7d37f76"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"


def fetch_forecast(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)

        if response.status_code == 401:
            print("  [401 Unauthorized] Invalid API key. Please check your API_KEY.")
            return None

        elif response.status_code == 404:
            print(f"  [404 Not Found] City '{city}' not found.")
            return None

        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout:
        print("  [Timeout] Request timed out. Try again later.")
    except requests.exceptions.ConnectionError:
        print("  [Connection Error] Could not connect. Check your internet.")
    except requests.exceptions.RequestException as e:
        print(f"  [Error] Something went wrong: {e}")

    return None


def organise_by_day(forecast_data):
    days = defaultdict(list)

    for entry in forecast_data["list"]:
        date = datetime.fromtimestamp(entry["dt"]).strftime("%A %d %B")
        days[date].append(entry)

    return days


def display_summary(days):
    print("\n5-Day Weather Forecast Summary:")
    print("=" * 60)

    for i, (date, entries) in enumerate(days.items()):
        temps       = [e["main"]["temp"] for e in entries]
        conditions  = [e["weather"][0]["description"] for e in entries]
        most_common = max(set(conditions), key=conditions.count).capitalize()

        print(f"\n[{i + 1}] {date}")
        print(f"      High       : {max(temps):.1f}°C")
        print(f"      Low        : {min(temps):.1f}°C")
        print(f"      Condition  : {most_common}")

    print("\n" + "=" * 60)


def display_detailed(days, day_number):
    date    = list(days.keys())[day_number - 1]
    entries = list(days.values())[day_number - 1]

    print(f"\nDetailed forecast for {date}:")
    print("=" * 60)

    for entry in entries:
        time        = datetime.fromtimestamp(entry["dt"]).strftime("%I:%M %p")
        temp        = entry["main"]["temp"]
        feels_like  = entry["main"]["feels_like"]
        humidity    = entry["main"]["humidity"]
        condition   = entry["weather"][0]["description"].capitalize()
        wind        = entry["wind"]["speed"]

        print(f"\n  {time}")
        print(f"    Condition   : {condition}")
        print(f"    Temperature : {temp:.1f}°C (Feels like {feels_like:.1f}°C)")
        print(f"    Humidity    : {humidity}%")
        print(f"    Wind Speed  : {wind} m/s")
        print("  " + "-" * 40)


def main():
    city = input("Enter a city name: ")

    data = fetch_forecast(city)
    if not data:
        return

    city_name = data["city"]["name"]
    country   = data["city"]["country"]
    print(f"\nFetching 5-day forecast for {city_name}, {country}...")

    days = organise_by_day(data)

    display_summary(days)

    while True:
        choice = input("\nEnter a day number (1-5) for detailed info, or 0 to quit: ")

        if not choice.isdigit():
            print("  Please enter a valid number.")
            continue

        choice = int(choice)

        if choice == 0:
            print("Goodbye!")
            break

        elif 1 <= choice <= len(days):
            display_detailed(days, choice)

        else:
            print(f"  Please enter a number between 1 and {len(days)}.")


if __name__ == "__main__":
    main()