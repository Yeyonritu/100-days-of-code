import requests
from datetime import datetime

USERNAME = "yeyonritu"
TOKEN = "billykoneuman"
GRAPHID = "graph01"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)#Gives response back as text

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "calorie tracker v1",
    "unit": "calory",
    "type": "float",
    "color": "sora"
    
}

headers = {
    "X-USER-TOKEN": TOKEN
}
#Creates It
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime.now()

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many calories did you eat today?: ")
}

date = post_config["date"]
#enter value
response = requests.post(url=post_endpoint, json=post_config, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{date}"

update_config = {
    "quantity": "45.7"
}
 
# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{date}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)