import requests
import smtplib
MY_LAT = 51.292641
MY_LONG = -114.008858
APPID = "5c0f29f1a59b29642d7c85c3ea649779"

my_email = "gvic0302@gmail.com"
password = "nqjhuyepukchgbru"

parameters = {
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":APPID,
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_id = weather_data["list"][0]["weather"][0]["id"]
condition_codes = []

for hour_data in weather_data["list"]:
    condition_codes.append(hour_data["weather"][0]["id"])
    
will_rain = False
for i in condition_codes:
    if i < 700:
        will_rain = True

if will_rain:
    rain_msg = "Bring an Umbrella"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="yeyonritu@gmail.com", msg=f"Subject: WARNING RAIN INCOMING!!!\n\n{rain_msg}")