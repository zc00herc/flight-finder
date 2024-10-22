import requests
#Flight_API = test.api.amadeus.com/v2/shopping/flight-offers



class FlightData:
    def __init__(self,flight_data):
        flight = flight_data["data"]
        flight_price = flight[0]["price"]["grandTotal"]
        destination_city = flight[0]["itineraries"][0]["arrival"]["iataCode"]
        print(flight_price, destination_city)

