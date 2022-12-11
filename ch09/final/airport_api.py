import requests
from weather_api import *

class Airport:
    def __init__(self,code):
        self.code = code #LGA
        self.api_url = "https://api.aviationapi.com/v1/airports?apt="+str(self.code)
        self.info = {}

    def get(self):
        self.response = requests.get(self.api_url)
        self.info = self.response.json()

    def airportInfo(self):
        self.city = self.info[self.code][0]['city']
        self.airport_name = self.info[self.code][0]['facility_name']
        self.faa_ident = self.info[self.code][0]['faa_ident']
        self.icao_ident = self.info[self.code][0]['icao_ident']

    def update(self):
        self.get()
        self.airportInfo()
        print("\n" + self.airport_name + " is located in " + self.city + ".")
        print("Current information about " + self.city + " include: \n")
        Weather(self.city).update()