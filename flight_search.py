import requests
# city = ""


class FlightSearch:

    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.flight = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.body = {
            "grant_type": "client_credentials",
            "client_id": "PUOAGifgKSwtYk216aTt0r3wvuu4Aal6",
            "client_secret": "iSG72qsnPmf3pRQH"
        }
        self.token_header = {
            "content-type": "application/x-www-form-urlencoded"
        }
        self.response = requests.post(self.flight, data=self.body, headers=self.token_header)
        self.Token = self.response.json()["access_token"]
        self.flight_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        self.header = {
            "Authorization": "Bearer " + self.Token
        }

    def get_results(self, city):
        parameters = {
            "originLocationCode": "BOS",
            "destinationLocationCode": city,
            "departureDate": "2024-08-28",
            "adults": 1,
            "maxPrice": 500,
            "max": 1,
            "currencyCode": "USD"
        }
        response = requests.get(self.flight_url, headers=self.header, params=parameters)
        # print(response.text)
        print(response)
        return response.json()



