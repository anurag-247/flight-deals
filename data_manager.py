import requests
from flight_search import FlightSearch

Token = FlightSearch().Token


class Sheety:

    def __init__(self):
        self.sheety_url = "hhttps://api.sheety.co/8bc66461a293e2821289e168040c8857/flightDeals/prices"
        self.sheety_header = {
            "Authorization": "Bearer fsjgjfshkv76dt67eiukghwru"
        }
        self.url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

    def get_sheety_data(self):
        response = requests.get(self.sheety_url, headers=self.sheety_header)
        return response.json()


# Lowest_Price = Sheety().get_sheety_data()["prices"][0]["lowestPrice"]
# print(Sheety().get_sheety_data()["prices"][0])
# city = Sheety().get_sheety_data()["prices"][0]["city"]
# sheet_id = Sheety().get_sheety_data()["prices"][0]["id"]



class DataManager:

    def __init__(self):
        self.url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        self.parameters = {
            "keyword": city,
            "max": 2
        }
        self.header = {
            "Authorization": "Bearer " + Token
        }

    def get_data(self):
        response = requests.get(self.url, params=self.parameters, headers=self.header)
        # print(response.json())
        return response.json()["data"][0]["iataCode"]


# print(iata)
# print(city)


class SheetsManager:

    def __init__(self):
        self.url = f"https://api.sheety.co/8bc66461a293e2821289e168040c8857/flightDeals/prices/{sheet_id}"
        self.parameters = {
            "price": {
                "city": city,
                "iataCode": iata,
                "lowestPrice": Lowest_Price
            }
        }
        self.header = {
            "Authorization": "Bearer fsjgjfshkv76dt67eiukghwru"
        }

    def get_data(self):
            response = requests.put(url=self.url, json=self.parameters, headers=self.header)
            print(response)
            print(response.json())

sid = 2
# v = len(Sheety().get_sheety_data()["prices"]) + 2
print(Sheety().get_sheety_data())
# while sid < v:
#     city = Sheety().get_sheety_data()["prices"][sid - 2]["city"]
#     iata = DataManager().get_data()
#     Lowest_Price = Sheety().get_sheety_data()["prices"][sid - 2]["lowestPrice"]
#     print(Sheety().get_sheety_data()["prices"][sid - 2])
#     sheet_id = Sheety().get_sheety_data()["prices"][sid - 2]["id"]
#     sid = int(sheet_id)
#     sid += 1
#     SheetsManager().get_data()
