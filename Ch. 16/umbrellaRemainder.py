#! python3
# Automate Boring Stuff Practice Project - Chapter 16
# umbrellaRemainder.py - Sends a text message remainder if rain is forecasted
#
# NOTE: This script uses textMyself.py module provided in this directory.
#       Please refer to textMyself.py for information on how to set atomated
#       messages account
#       For information on weather.gov api please refer toL
#       https://www.weather.gov/documentation/services-web-api

import os 

# This fuction gets current weather data from weather.gov api based on
# a location provided
def getCurrentWeather(_cwa_, _gridX_, _gridY_):
  import json, requests

  # Download the JSON data from weather.org's API.
  url = 'https://api.weather.gov/gridpoints/' + _cwa_ + '/' + _gridX_ + ',' + \
  _gridY_ + '/forecast'
  response = requests.get(url)
  response.raise_for_status()

  # Load JSON data into a Python variable.
  weatherData = json.loads(response.text)

  return weatherData

# User can modify the location for the current weather query by updating the
# location data below. Please check
# https://www.weather.gov/documentation/services-web-api
# for more information
cwa = 'HGX'
gridX = '47'
gridY = '93'

# Get current forecast by using the getCurrentWeather function
forecast = getCurrentWeather(cwa, gridX, gridY)
#print(forecast['properties']['periods'][0]['shortForecast'])
todaysForecast = forecast['properties']['periods'][0]['shortForecast']

# Determine if today's forecast includes rain
if 'Rain' in todaysForecast:
  myMessage = "Get your umbrella ready, today's weather forecast is: %s" \
  % todaysForecast
else:
  myMessage = "No need for umbrella today, today's weather forecast is: %s" \
  % todaysForecast

# Send message
import textMyself
textMyself.textmyself(myMessage)

#pprint.pprint(forecast)
