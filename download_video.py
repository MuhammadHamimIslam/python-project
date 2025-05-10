import requests 

url = "https://www.w3schools.com/html/mov_bbb.mp4?spm=a2ty_o01.29997173.0.0.36a1c921Bpq35O&file=mov_bbb.mp4"

r = requests.get(url)

try:
    print("Download started!")
    with open('test.mp4', 'wb') as f:
        f.write(r.content)
except Exception as e:
    print(e)
else:
    print("Downloaded successfully!")