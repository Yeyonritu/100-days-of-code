from flight_data import FlightData


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, list):
        for i in list:
            if i["iataCode"] == "":
                i["iataCode"] = "TESTING"
                
        
    