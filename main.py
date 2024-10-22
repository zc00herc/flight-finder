from time import strftime

from data_manager import DataManager
import time
from datetime import datetime, timedelta
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# initialize run
data_manager = DataManager()
sheet_data = data_manager.fetch_sheet_data()

from flight_search import FlightSearch
flight_search = FlightSearch()

DEPARTURE_CITY = "LON"

# Update Data in Spreadsheet
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.lookup_city(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_rows()

# Find Flights
destination = "PAR"
tomorrow = datetime.now()+timedelta(days=1)
departure_date = tomorrow.strftime("%Y-%m-%d")
six_months_from_now = datetime.now()+timedelta(days=(6*30))
to_date = six_months_from_now.strftime("%Y-%m-%d")
avail_flights=flight_search.getflights(DEPARTURE_CITY,destination,departure_date,to_date)
print(avail_flights)