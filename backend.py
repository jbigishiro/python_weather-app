import requests
import os

API_KEY = os.getenv("OPEN_WEATHER_API")


def get_data(place, forecasted_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecasted_days
    filtered_data = filtered_data[:nr_values]

    return filtered_data


if __name__ == "__main__":
    data = get_data(place="Goma", forecasted_days=1)
    rain = [dt["weather"][0]["main"] for dt in data]
    print(rain)
    temp = [dt["dt_txt"] for dt in data]
    print(temp)
