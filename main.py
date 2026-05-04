import requests
import datetime as dt
import os

headers = {
    "x-app-id" : os.getenv("APP_ID"),
    "x-app-key" : os.getenv("APP_KEY"),
}

BASE_URL = "https://app.100daysofpython.dev"

CALORIES_ENDPOINT = f"{BASE_URL}/v1/nutrition/natural/exercise"

exercise = input("Tell me which exercises you did today : ")

cal_config = {
    "query" : exercise,
}

response = requests.post(CALORIES_ENDPOINT, headers=headers, json=cal_config )
data = response.json()
print(data)
print((data["exercises"][0]["name"]).title())
print((data["exercises"][0]["duration_min"]))
print(data["exercises"][0]["nf_calories"])

date = dt.datetime.now()
print(date.strftime("%d/%m/%Y"))
print(date.strftime("%X"))

SHEETY_URL = os.getenv("SHEETY_ENDPOINT")

sheety_config = {
    "workout": {
        "date": date.strftime("%d/%m/%Y"),
        "time": date.strftime("%X"),
        "exercise": data["exercises"][0]["name"].title(),
        "duration": data["exercises"][0]["duration_min"],
        "calories": data["exercises"][0]["nf_calories"]
    }
}

sheety_headers = {
    "Authorization": os.getenv("TOKEN")
}

add_row = requests.post(url=SHEETY_URL, json=sheety_config, headers=sheety_headers)
print(add_row.text)
print(add_row.status_code)

print("APP_ID:", os.getenv("APP_ID"))
print("APP_KEY:", os.getenv("APP_KEY"))
print("TOKEN:", os.getenv("TOKEN"))
print("INPUT:", exercise)
print("EXERCISES:", data["exercises"])
