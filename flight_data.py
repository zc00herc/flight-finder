
#Flight_API = test.api.amadeus.com/v2/shopping/flight-offers



class FlightData:
    def __init__(self):
        self.body = {
            "originLocationCode": "LON",
            "destinationLocationCode": city_code,
            "departureDate": "2024-10-23",
            # "returnDate": something,
            "adults": 1,
            # "children": 0,
            # "infants": 0,
            "nonStop": True,
            "currencyCode": "GBP",
        }