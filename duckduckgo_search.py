# uses external library requests 
# need pip install requests 
import requests 

def search_ddg(query, region="en-us"): 
    url = "https://api.duckduckgo.com/"
    params = {"q": query, "format": "json", "kl": region}
    
    res = requests.get(url, params=params)
    return res.json()

def instant_answer(query, region): 
    result = search_ddg(query, region)
    return result.get("AbstractText", "No abstract answer found!")

def image_search(query): 
    url = "https://api.duckduckgo.com/"
    params = {"q": query, "format": "json", "ia": "images"}
    res = requests.get(url, params=params)
    return res.json()

def advance_search(query, category): 
    url = "https://api.duckduckgo.com/"
    params = {"q": query, "format": "json", "ia": category}
    res = requests.get(url, params=params)
    return res.json()

help_msg = """1. To simple search 
2. To get instant answer 
3. To search by image 
4. To advance search with category
5. To print this help message 
"""

def main(): 
    print(help_msg)
    choice = input("Choose one: ").strip()
    match choice: 
        case "1": 
            query = input("Enter your search query: ").strip()
            region = input("Enter region (e.g. en-us) leave it blank if you want en-us").strip()
            print(search_ddg(query, region))
        case "2": 
            query = input("Enter your search query: ").strip()
            region = input("Enter region (e.g. en-us) leave it blank if you want en-us").strip()
            print(instant_answer(query, region))
        case "3": 
            query = input("Enter your search query: ").strip()
            print(image_search(query))
        case "4": 
            query = input("Enter your search query: ").strip()
            category = input("Enter search category (e.g. news, image, video)").strip()
            print(advance_search(query, category))
        case "5": 
            print(help_msg)
        case _: 
            print("Invalid choice")
            
if __name__ == '__main__':
    main()