import requests 

url = "https://images.unsplash.com/photo-1506744038136-46273834b3fb?spm=a2ty_o01.29997173.0.0.36a15171lkfHF9"

r = requests.get(url)

try:
    print("Download started!")
    with open('beautiful.jpeg', 'wb') as f:
        f.write(r.content)
except Exception as e:
    print(e)
else:
    print("Downloaded successfully!")