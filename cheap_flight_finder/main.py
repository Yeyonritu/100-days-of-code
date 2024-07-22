#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager
from pprint import pprint

data = FlightData()

sheet_data = data.get_sheet_data()
to_manage = DataManager()
to_manage.update()

pprint(sheet_data)
for i in sheet_data:
    if i["iataCode"] == "":
        search = FlightSearch() 
        for i in sheet_data:
            i["iataCode"] = search.get_destination_code(i["city"])
        pprint(sheet_data)
        
        


