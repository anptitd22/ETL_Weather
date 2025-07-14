import os
import requests
import json
from datetime import datetime
from dotenv import load_dotenv

#load env
path_env = "../.env"

load_dotenv(path_env)

KEY = os.getenv("API_WEATHER_KEY")

# file json from api
FILENAME = "weather_data.json"

def get_weather_data():
    #call api
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "lat": 21.0278,
        "lon": 105.8342,
        "appid": KEY,
        "units": "metric",
        "lang": "vi",
        "dt": "1751983169"
    }

    response = requests.get(url, params=params)

    #200: success
    if response.status_code == 200:
        #convert json
        data = response.json()

        #write
        with open(FILENAME, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(f"Dữ liệu đã lưu: {FILENAME}")
        return FILENAME
    else:
        raise Exception(f"Lỗi API: {response.status_code} - {response.text}")

if __name__ == "__main__":
    get_weather_data()