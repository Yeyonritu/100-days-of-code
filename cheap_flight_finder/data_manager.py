import requests

UPDATE_ENDPOINT = "https://api.sheety.co/5350a1816a6d14869c9c15d3c0408814/flightDeals/prices"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.response = requests.get(url=UPDATE_ENDPOINT)
        self.data = self.response.json()
        
    def update(self):
        for price in self.data["prices"]:
            
            sheet_inputs = {
                "price":{
                    "IATA Code": price["iataCode"]
                }
            }
            
        update_url = f"{UPDATE_ENDPOINT}/{price['id']}"
            
        self.sheet_response = requests.post(url=update_url, json=sheet_inputs)
        print(self.sheet_response.text)