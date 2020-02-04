import requests
import json
from datetime import datetime

class Airprobe:
    def __init__(self):
        print("please use the weather_extractor function to get the weather update")    
    def weather_extractor(self):
        location = input("Please enter the location to get weather forecast\n")
        #Using the mapbox geocoding API to fetch coordinates of the entered place 
        url = 'https://api.mapbox.com/geocoding/v5/mapbox.places/'+location+'.json?access_token=pk.eyJ1IjoiZGV2LXR5YWdpOSIsImEiOiJjazRtZ3h3NnIwNG14M25wNXVydTE3MWhmIn0.o6HRmaOSRiGQ7GRAhO1W4Q&limit=1'

        response = requests.get(url=url)
        data = response.json()
        latitude = data["features"][0]["geometry"]["coordinates"][1] 
        longitude = data["features"][0]["geometry"]["coordinates"][0]


        print("Fetching ....")

        body = {
            "lat": latitude,
            "lon": longitude,
            "model": "gfs",
            "parameters": ["wind", "temp"],
            "levels": ["surface"],
            "key": "ijtl9cE82p3Q9b2DhJ43l5Cn4eMB2Jjt"
        }
        url1 = 'https://api.windy.com/api/point-forecast/v2'
        response = requests.post(url=url1,json=body)
        res=response.json()
        ts=float(res["ts"][0])/1000
        # print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
        # print(datetime.datetime.now())
        print("\n\n     Time                |     temperature(°C)" )
        print("----------------------------------------------------")
        #displaying the wind speed to the console    
        for i in range(0,len(res["ts"])):
            val = datetime.utcfromtimestamp(float(res["ts"][i])/1000).strftime('%Y-%m-%d %H:%M:%S')
            temp = res["temp-surface"][i]-273.15
            # if val == datetime.today().day:
            print(val,"     |       ",round(temp, 3))

        #displaying the wind speed to the console    
        print("\n\n     Time                |     Wind(ms^-1)" )
        print("----------------------------------------------------")
        for i in range(0,len(res["ts"])):
            val = datetime.utcfromtimestamp(float(res["ts"][i])/1000).strftime('%Y-%m-%d %H:%M:%S')
            wind_u = res["wind_u-surface"][i]
            # wind_v = res["wind_v-surface"][i]
            # if val == datetime.today().day:
            print(val,"     |       ",round(wind_u, 2))#,"    ",round(wind_v, 2)

        # the console displays the temp of the next 10 days with 8 measurements in a day taken at an interval of 3 hours