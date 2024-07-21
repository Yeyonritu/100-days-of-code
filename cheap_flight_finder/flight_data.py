import requests
post = "https://api.sheety.co/5350a1816a6d14869c9c15d3c0408814/flightDeals/prices"
SHEETY_ENDPOINT = "https://api.sheety.co/5350a1816a6d14869c9c15d3c0408814/flightDeals/prices"

class FlightData():
    
    def __init__(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.sheet_data = data["prices"]
        
    def get_sheet_data(self):
        return self.sheet_data
        
    #This class is responsible for structuring the flight data.
    