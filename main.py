from data_manager import DataManager
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

#city search
# CITY_API_KEY = "IibJxzZqRpS1xkhQNC2Njkr5SUHbWg6o"
# CITY_API_SECRET = "ZPy7T8TTd21tcuEB"

data_manager = DataManager()
sheet_data = data_manager.fetch_sheet_data()
if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.lookup_city(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_rows()
