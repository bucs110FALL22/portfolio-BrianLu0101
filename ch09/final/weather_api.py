import requests

class Weather:
    def __init__(self,location):
        '''
        Definition:
        Initialization and variables. Also latitude and longitude changes depending on location.

        Parameters:
        location = pulled from Airport() module and is used to determine latitude and longitude to be appended onto api url.
        '''
        self.location = location.lower()
        if str(self.location) == "new york":
            self.lat = '40.71'
            self.long = '-74.01'
        if str(self.location) == "binghatmon":
            self.lat = '42.10'
            self.long = '-75.92'
        if str(self.location) == "buffalo":
            self.lat = '42.89'
            self.long = '-78.88'
        if str(self.location) == "white plains":
            self.lat = '41.03'
            self.long = '-73.76'
        if str(self.location) == "albany":
            self.lat = '42.65'
            self.long = '-73.76'
        if str(self.location) == "rochester":
            self.lat = '43.15'
            self.long = '-77.62'
        if str(self.location) == "syracuse":
            self.lat = '43.05'
            self.long = '-76.15'
        if str(self.location) == "farmingdale":
            self.lat = '40.73'
            self.long = '-73.45'
        if str(self.location) == "montgomery":
            self.lat = '41.53'
            self.long = '-74.24'
        if str(self.location) == "ithaca":
            self.lat = '42.44'
            self.long = '-76.50'
        if str(self.location) == "niagara falls":
            self.lat = '43.09'
            self.long = '-79.06'
        if str(self.location) == "westhampton beach":
            self.lat = '40.80'
            self.long = '-72.61'
        if str(self.location) == "plattsburgh":
            self.lat = '44.70'
            self.long = '-73.45'
        if str(self.location) == "endicott":
            self.lat = '42.10'
            self.long = '-76.05'
        self.api_url = "https://api.open-meteo.com/v1/forecast?latitude="+self.lat+"&longitude="+self.long+"&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&current_weather=true&temperature_unit=fahrenheit&windspeed_unit=kn&precipitation_unit=inch&timezone=auto"
        self.info = {}

    def get(self):
        '''
        Definition:
        API request and related information dictionary.

        Parameters:
        
        '''
        self.response = requests.get(self.api_url)
        self.info = self.response.json()

    def weatherInfo(self):
        '''
        Definition:
        Pulls and sets variables for necessary information that changes based on input.

        Parameters:
        
        '''
        self.temperature = self.info['current_weather']['temperature']
        self.windspeed = self.info['current_weather']['windspeed']
        self.time = self.info['current_weather']['time']
        self.tempUnit = self.info['daily_units']['temperature_2m_max']
        self.dailyPrecip = self.info['daily']['precipitation_sum'][0]
        self.precipUnit = self.info['daily_units']['precipitation_sum']

    def update(self):
        '''
        Definition:
        Updates and runs class Weather(). Also prints related information.

        Parameters:
        
        '''
        self.get()
        self.weatherInfo()
        print("Current Time: " + self.time)
        print("\nThe current temperature of " + self.location.upper() + " is " + str(self.temperature) + " " + self.tempUnit + " and the wind speed today is " + str(self.windspeed) + " knots.")
        print("There is currently around " + str(self.dailyPrecip) + " " + self.precipUnit + " of rain at this hour.")
        if int(self.temperature) >= 57 and int(self.temperature) <= 61 and int(self.dailPrecip) == 0.0:
            print("\nFlight conditions are ideal. Maximized travel time. (Not including wind speed and direction).")
        elif int(self.temperature) <= 57 and int(self.dailyPrecip) >= 0.0:
            print("\nFlight conditions are OK. Risk of icing during flight and increased power output. Decreased travel time. (Not including wind speed and direction).")
        elif int(self.temperature) >= 61 and int(self.dailyPrecip) >= 0.0:
            print("\nFlight conditions are OK. Risk of overheat during starting and lower power output. Increase travel time. (Not including wind speed and direction).")