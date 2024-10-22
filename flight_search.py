import requests
import os

from flight_data import FlightData


# use amadeus api to get flight data
# city search api =
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = "IibJxzZqRpS1xkhQNC2Njkr5SUHbWg6o"
        self.api_secret = "ZPy7T8TTd21tcuEB"
        self.api_token = self.getnewtoken()

    def getnewtoken(self):
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }
        response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token",headers=header,data=body)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")

        return response.json()["access_token"]

    def lookup_city(self,city):
        header = {"Authorization": f"Bearer {self.api_token}"}
        query = {
            "keyword": city,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(url="https://test.api.amadeus.com/v1/reference-data/locations/cities",headers=header,params=query)
        response.raise_for_status()
        try:
            city_code = response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"IndexError: No airport code found for {city}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city}.")
            return "Not Found"
        return city_code

    def getflights(self,departure_city,destination_city,departure_date,to_date):
        header = {"Authorization": f"Bearer {self.api_token}"}
        query = {
            "originLocationCode": departure_city,
            "destinationLocationCode": destination_city,
            "departureDate": departure_date,
            "returnDate": to_date,
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10"
        }
        response = requests.get(url="https://test.api.amadeus.com/v2/shopping/flight-offers", headers=header,
                                params=query)
        response.raise_for_status()
        return response.json()
