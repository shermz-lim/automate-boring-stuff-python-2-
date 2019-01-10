#!python3 
# quickWeather.py - Prints the weather for a location from the command line.
import json, requests, sys 

#checks that user provided location 
try: 
    assert len(sys.argv) >= 2
except AssertionError:
    print("Please enter a location. Usage: quickWeather.py $location.")
    sys.exit()

location = ' '.join(sys.argv[1:])

#need to sign up for an openWeather account to obtain an API key 
apiId = 'secret'
# requesting openWeatherMap API url & checking for error
url = "http://api.openweathermap.org/data/2.5/forecast?q={}&appid={}".format(location, apiId)
response = requests.get(url)
response.raise_for_status()

# Converting json to python values 
jsonWeatherData = response.text
weatherData = json.loads(jsonWeatherData)
forecasts = weatherData['list']

# Printing results...
print("Weather for {}:".format(location))
# API url shows 5 days of weather forecast in 3h intervals . Printing this shows 5 days of forecast.
for i in range(0, 40, 8):
    print("Forecast for {} is {}".format(forecasts[i]['dt_txt'], forecasts[i]['weather'][0]['main']))

    