import requests 

url = "https://www.dhakacitycollege.edu.bd/upload/N_08_05_2025_12_32_10.pdf"

try:
    print("Download started!")
    response = requests.get(url)
    with open('notice.pdf', 'wb') as f:
        f.write(response.content)
except Exception as e:
    print(f"Download failed with status code {response.status_code}")
else:
    print("Downloaded successfully!")