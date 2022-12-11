import requests
from weather_api import Weather

class Airport:
    def __init__(self,code):
        '''
        Definition:
        Initialization and variables.

        Parameters:
        code = airport designation code.
        '''
        self.code = code #LGA
        self.api_url = "https://api.aviationapi.com/v1/airports?apt="+str(self.code)
        self.info = {}

    def get(self):
        '''
        Defintion:
        API request and related information dictionary.

        Parameters:
        
        '''
        self.response = requests.get(self.api_url)
        self.info = self.response.json()

    def airportInfo(self):
        '''
        Definition:
        Pulls and sets variables for necessary information that change depending on input.

        Parameters:
        
        '''
        self.city = self.info[self.code][0]['city']
        self.airport_name = self.info[self.code][0]['facility_name']
        self.faa_ident = self.info[self.code][0]['faa_ident']
        self.icao_ident = self.info[self.code][0]['icao_ident']

    def update(self):
        '''
        Definition:
        Updates and runs the for class Airport() while providing information for module Weather(). Also prints information utilized in this module.

        Parameters:
        '''
        self.get()
        self.airportInfo()
        print("\n" + self.airport_name + " is located in " + self.city + ".")
        print("Current information about " + self.city + " include: \n")
        Weather(self.city).update()
