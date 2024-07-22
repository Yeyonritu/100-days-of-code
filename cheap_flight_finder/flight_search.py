import requests

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token/"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = "AgwqC2hUS3jsM7A9bii63NzQMnMd055Z"
        self._api_secret = "JDAYbqK1PL48sguk"
        self._token = self._get_new_token()
    
    def get_destination_code(self, city_name):
        self.code = "TESTING"
        return self.code
    
    def _get_new_token(self):
        
       header = {
           'Content-Type': "Content-Type: application/x-www-form-urlencoded"   
        }
       
       body = {
           'grant_type': 'client_credentials',
           'client_id': self._api_key,
           'client_secret': self._api_secret
       }
       
       response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
       
       return response.json()['access_token']
    