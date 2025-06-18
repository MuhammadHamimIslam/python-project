import speedtest

st = speedtest.Speedtest() # initialize the speed test 

def get_internet_speed_info(): 
    print("basic info: ", st.best) # get basic info
    print("closest info: ", st.closest) # get closest 
    download_speed = st.download() / 8000 # download speed 
    upload_speed = st.upload() / 8000 # upload speed 
    print(f"{download_speed = } KB/s")
    print(f"{upload_speed = } KB/s")
    print("config: ", st.config) # get the configuration 
    print("best servers: ", st.get_best_server()) # get the best server 
    print("closest servers: ", st.get_closest_servers()) # get the closest server
    print("configuration: ", st.get_config()) # get configuration 
    print("latitude & longitude: ", st.lat_lon) # latitude and longitude 
    print("servers: ", st.get_servers()) # get the servers
    print("result: ", st.results) # get the results 
    print("servers: ", st.servers) # server info
    
    
get_internet_speed_info()