import requests 

url = "https://orangefreesounds.com/wp-content/uploads/2025/02/Spring-bird-song-sound-effect.mp3"

try:
    print("Download started!")
    response = requests.get(url)
    with open('bird_singing.mp3', 'wb') as f:
        f.write(response.content)
except Exception as e:
    print(f"Download failed with status code {response.status_code}")
else:
    print("Downloaded successfully!")