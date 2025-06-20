import requests
from dotenv import load_dotenv
import os

load_dotenv() # load dot env for api key and search engine id

API_KEY = os.getenv("GOOGLE_SEARCH_API") # load the api key from .env
CX = os.getenv("CUSTOM_SEARCH_ENGINE_ID")  # load Custom Search Engine ID from .env

def google_search(query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": API_KEY,
        "cx": CX,
        "q": query,
    }
    response = requests.get(url, params=params)
    results = response.json().get("items", [])

    for item in results:
        print("Title:", item.get("title"))
        print("Link:", item.get("link"))
        print("Snippet:", item.get("snippet"))
        print("-" * 40)

if __name__ == "__main__":
    q = input("Enter search query: ")
    google_search(q)