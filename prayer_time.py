import requests
from datetime import datetime

city = input("Enter your city: ")
country = input("Enter your country: ")

params = {
    "address": f"{city}, {country}",
    "method": 2
}

res = requests.get("https://api.aladhan.com/v1/timingsByAddress", params=params)

data = res.json()

for salah, time_str in data["data"]["timings"].items():
    time_24 = datetime.strptime(time_str, "%H:%M")
    time_12 = time_24.strftime("%I:%M %p")
    print(salah, ": ", time_12)