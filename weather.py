import urllib2
import requests
# import requests_mock
import os
import json

weather_key = os.environ['WKEY']

current_location = input("Please enter your zip-code: ")
print("You entered: {}". format(current_location))

print("Weather key: {}".format(weather_key))    # used to verify key
print("Current zip: {}".format(current_location))  # used to verify zip


'''Verified that key and zipcode properly passed into url'''
'''Reporting on city, weather, temperature_string, relative_humidity,
    wind_string, wind_gust_mph and dewpoint_string. '''


def current_conditions(weather_key, current_location):
    f = urllib2.urlopen('http://api.wunderground.com/api/{}/conditions/q/{}.json'.   # noqa
                       format(weather_key, current_location))  # noqa
    json_string = f.read()
    res = json.loads(json_string)
    # r = requests.get('http://api.wunderground.com/api/{}/conditions/q/{}.json'.   # noqa
    #                    format(weather_key, current_location))  # noqa
    loc = res['current_observation']['display_location']['city']
    wea = res['current_observation']['weather']
    ts = res['current_observation']['temperature_string']
    rh = res['current_observation']['relative_humidity']
    winds = res['current_observation']['wind_mph']
    windd = res['current_observation']['wind_dir']
    windg = res['current_observation']['wind_gust_mph']
    dews = res['current_observation']['dewpoint_string']

    print("Here is the local weather conditions for {}:".format(loc))
    print("In general the weather is {}.".format(wea))
    print("The temperature is {} with {} relative humidity and {} dewpoint.".
          format(ts, rh, dews))
    print("Winds are {} mph {} with gusts of {} mph.".
          format(winds, windd, windg))
    f.close()

current_conditions(weather_key, current_location)


# class SearchAlbums:
#     def __init__(self, q_string):
#         self.q_string = q_string
#
#     def run(self):
#         url = 'https://________q={}'.format(urllib.quote_plus(self.q_string))
#
# def main():
#     call = SearchAlbums('thriller')
#     res = call.run()
# header={'ddd': weather_key})

# print(res.json())

# import urllib2
# import json
# f = urllib2.urlopen('http://api.wunderground.com/api/key/geolookup/conditions/zip.json') # noqa
# json_string = f.read()
# parsed_json = json.loads(json_string)
# location = parsed_json['location']['city']
# temp_f = parsed_json['current_observation']['temp_f']
# print "Current temperature in {} is: {}" % (location, temp_f)
# f.close()
