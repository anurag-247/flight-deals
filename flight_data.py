from flight_search import FlightSearch
from data_manager import Sheety
city = ""
# This class is responsible for structuring the flight data.
# pass


class FlightData:

    def __init__(self):
        self.data = FlightSearch().get_results(city)
        self.flight_price = self.data["data"][0]["price"]["total"]

        print(self.flight_price)


sid = 2
# v = len(Sheety().get_sheety_data()["prices"]) + 2
print(Sheety().get_sheety_data())
# while sid < v:
#     city = Sheety().get_sheety_data()["prices"][sid - 2]["city"]
#     sid += 1
#     FlightData()
