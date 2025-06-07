import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("WEATHER_API")
city = input("Enter the city: ")

res = requests.get(f"http://api.weatherapi.com/v1/astronomy.json?key={api_key}&q={city}")

if res.status_code == 200: 
    print(res.text)
else:
    print("Error: ", res.status_code)