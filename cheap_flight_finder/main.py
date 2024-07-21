#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager
from pprint import pprint

data = FlightData()
sheet_data = data.get_sheet_data()
search = FlightSearch(sheet_data) 
to_manage = DataManager()
to_manage.update()

