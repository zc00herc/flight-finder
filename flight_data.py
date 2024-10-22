import requests
#Flight_API = test.api.amadeus.com/v2/shopping/flight-offers



class FlightData:
    def __init__(self):
        self.api_key = "IibJxzZqRpS1xkhQNC2Njkr5SUHbWg6o"
        self.api_secret = "ZPy7T8TTd21tcuEB"
        self.api_token = self.getnewtoken()
        # self.departure_airport_code = self.getdepartureairportcode()

