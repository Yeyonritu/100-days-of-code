import requests
from datetime import datetime 

# "ea5bf4b1e3edfe39961c9539390fd4b0	—"
GENDER = "male"
WEIGHT_KG = "76"
HEIGHT_CM = "187"
AGE = 20

exercise_key = "ea5bf4b1e3edfe39961c9539390fd4b0"
exercise_id = "2272b97f"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")

sheet_endpoint = f"https://api.sheety.co/5350a1816a6d14869c9c15d3c0408814/workoutsTest/workouts"

exercise_param = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    'x-app-id': exercise_id,
    'x-app-key': exercise_key,
}

response = requests.post(url=exercise_endpoint, json=exercise_param, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d%m%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout":{
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    
    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)
    print(sheet_response.text)