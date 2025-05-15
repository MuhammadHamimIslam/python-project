import requests 
import json
"""
This project uses python requests library and 'ipwho' API to get ip address, location 
"""
header = {"user-agent": "python-project"}
#api_provider_url = "https://ipinfo.io/json"
api_provider_url = "https://ipwho.is/"
res = requests.get(api_provider_url, headers=header)

data = json.loads(res.text)

print(f"Ip Address is: {data['ip']}") # print the ip address 
print(f"Ip type: {data['type']}") # returns the ip type e.g. IPv4, IPv6
print(f"county is: {data['country']}") # returns the country name
print(f"county code is: {data['country_code']}") # returns the country code
print(f"region is: {data['region']}") # returns the region name
print(f"region code is: {data['region_code']}") # returns the region code
print(f"city name is: {data['city']}") # returns the city name
print(f"latitude is: {data['latitude']}") # returns the latitude 
print(f"longitude is: {data['longitude']}") # returns the longitude 
print(f"calling code is: {data['calling_code']}") # returns the calling code 
print(f"capital is: {data['capital']}") # returns the capital 
print(f"borders is: {data['borders']}") # returns the borders 
print(f"flag is: {data['flag']}") # returns the flag as dict 
print(f"connection is: {data['connection']}") # returns the connection obj like provider, isp
print(f"time zone is: {data['timezone']}") # returns the timezone as dict
