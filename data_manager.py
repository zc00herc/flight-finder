import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()
SHEETY_ENDPOINT = "https://api.sheety.co/7a68b96f49d65cd1d3b0ef4965b2ae87/flightDeals/prices"
class DataManager:
    def __init__(self):
        self._user = os.getenv("SHEETY_USER")
        self._pass = os.getenv("SHEETY_PASS")
        self._authorization = os.getenv("SHEETY_TOKEN_AUTH")
        self.header = {
            "Authorization": "Basic emMwMDpnb29nbHltb29nbHkxMDI5"
        }
        self._authorization = HTTPBasicAuth(self._user,self._pass)
        self.destination_data = {}

    def fetch_sheet_data(self):
        response = requests.get(url=SHEETY_ENDPOINT,headers=self.header)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_rows(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(f"{SHEETY_ENDPOINT}/{city["id"]}",
                                headers=self.header,
                                json=new_data)
            response.raise_for_status()