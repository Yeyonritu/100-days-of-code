#API's
#This are outlines used by programmers to create software or interact with an external system
#API Endpoint(Data Storage Location)
MY_LAT = 51.292641
MY_LONG = -114.008858
import requests
from datetime import datetime
#API request
#Response Codes: 1XX- Hold On, 2XX- Sucess, 3XX- Go Away, 4XX- You Screwed Up, 5XX- I Screwed Up (httpstatuses.com)
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
# longitude = data['iss_position']["longitude"]
# latitude = data['iss_position']["latitude"]
# location = (longitude, latitude)
# print(location)
#API Parameters
parameters = {
        "lat": MY_LAT,
        "lng":MY_LONG,
        "formatted":0   
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]['sunrise'].split("T")[1].split(":")[0]
sunset = data["results"]['sunset'].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)
