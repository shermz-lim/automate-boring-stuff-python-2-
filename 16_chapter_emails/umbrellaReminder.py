#! python3 
# This program checks whether it is raining. If it is, then it will text me
# a reminder to bring an umbrella before leaving the house 

import textmyself, requests, json

apiId = input("Enter your openweather API id:")

# requesting openWeatherMap API url & checking for error
url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format('singapore', apiId)
response = requests.get(url)
response.raise_for_status()

# Converting json to python values 
jsonWeatherData = response.text
weatherData = json.loads(jsonWeatherData)

# Accessing rain information
weather = weatherData['weather'][0]['main']
print(weather)

# Send text message if it is raining today
if weather == 'Rain':
    print("It is raining today. Sent text message to you.")
    textmyself.textmyself("It is raining today. Remember to bring an umbrella when you go out.")
else: 
    print("It is not raining today.")    