# import urllib2
import requests
# import requests_mock
import os
# import json

weather_key = os.environ['WKEY']

current_location = input("Please enter your zip-code: ")
print("You entered: {}". format(current_location))

# print("Weather key: {}".format(weather_key))    # used to verify key
# print("Current zip: {}".format(current_location))   # used to verify zip

'''Verified that key and zipcode properly passed into url'''
'''Reporting on city, weather, temperature_string, relative_humidity,
    wind_string, wind_gust_mph and dewpoint_string. '''


def current_conditions(weather_key, current_location):

    res = requests.get('http://api.wunderground.com/api/{}/conditions/q/{}.json'.   # noqa
                       format(weather_key, current_location)).json()  # noqa
    loc = res['current_observation']['display_location']['city']
    wea = res['current_observation']['weather']
    ts = res['current_observation']['temperature_string']
    rh = res['current_observation']['relative_humidity']
    winds = res['current_observation']['wind_mph']
    windd = res['current_observation']['wind_dir']
    windg = res['current_observation']['wind_gust_mph']
    dews = res['current_observation']['dewpoint_string']

    print("\nHere is the local weather conditions for {}:".format(loc))
    print("In general the weather is {}.".format(wea))
    print("The temperature is {} with {} relative humidity and {} dewpoint.".
          format(ts, rh, dews))
    print("Winds are {} mph {} with gusts of {} mph.".
          format(winds, windd, windg))


def ten_day_forcast(weather_key, current_location):

    ten = requests.get('http://api.wunderground.com/api/{}/forecast10day/q/{}.json'.   # noqa
                       format(weather_key, current_location)).json()  # noqa

    P1 = ten['forecast']['txt_forecast']['forecastday'][0]['title']
    P2 = ten['forecast']['txt_forecast']['forecastday'][0]['fcttext']
    P3 = ten['forecast']['txt_forecast']['forecastday'][1]['title']
    P4 = ten['forecast']['txt_forecast']['forecastday'][1]['fcttext']
    P5 = ten['forecast']['txt_forecast']['forecastday'][2]['title']
    P6 = ten['forecast']['txt_forecast']['forecastday'][2]['fcttext']
    P7 = ten['forecast']['txt_forecast']['forecastday'][3]['title']
    P8 = ten['forecast']['txt_forecast']['forecastday'][3]['fcttext']
    P9 = ten['forecast']['txt_forecast']['forecastday'][4]['title']
    P10 = ten['forecast']['txt_forecast']['forecastday'][4]['fcttext']
    P11 = ten['forecast']['txt_forecast']['forecastday'][5]['title']
    P12 = ten['forecast']['txt_forecast']['forecastday'][5]['fcttext']
    P13 = ten['forecast']['txt_forecast']['forecastday'][6]['title']
    P14 = ten['forecast']['txt_forecast']['forecastday'][6]['fcttext']
    P15 = ten['forecast']['txt_forecast']['forecastday'][7]['title']
    P16 = ten['forecast']['txt_forecast']['forecastday'][7]['fcttext']
    P17 = ten['forecast']['txt_forecast']['forecastday'][8]['title']
    P18 = ten['forecast']['txt_forecast']['forecastday'][8]['fcttext']
    P19 = ten['forecast']['txt_forecast']['forecastday'][9]['title']
    P20 = ten['forecast']['txt_forecast']['forecastday'][9]['fcttext']

    print("\nDay 1 forecast: {}".format(P1))
    print("Day 1 forecast: {}".format(P2))
    print("Day 2 forecast: {}".format(P3))
    print("Day 2 forecast: {}".format(P4))
    print("Day 3 forecast: {}".format(P5))
    print("Day 3 forecast: {}".format(P6))
    print("Day 4 forecast: {}".format(P7))
    print("Day 4 forecast: {}".format(P8))
    print("Day 5 forecast: {}".format(P9))
    print("Day 5 forecast: {}".format(P10))
    print("Day 6 forecast: {}".format(P11))
    print("Day 6 forecast: {}".format(P12))
    print("Day 7 forecast: {}".format(P13))
    print("Day 7 forecast: {}".format(P14))
    print("Day 8 forecast: {}".format(P15))
    print("Day 8 forecast: {}".format(P16))
    print("Day 9 forecast: {}".format(P17))
    print("Day 9 forecast: {}".format(P18))
    print("Day10 forecast: {}".format(P19))
    print("Day10 forecast: {}".format(P20))


def sunrise_sunset(weather_key, current_location):

    ten = requests.get('http://api.wunderground.com/api/{}/forecast10day/q/{}.json'.   # noqa
                       format(weather_key, current_location)).json()  # noq


def full_set(w, c):
    current_conditions(weather_key, current_location)
    ten_day_forcast(weather_key, current_location)

full_set(weather_key, current_location)
