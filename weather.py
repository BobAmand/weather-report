import requests
import os

weather_key = os.environ['WKEY']

res = requests.get('http://api.wunderground.com/api/WKEY/currenthurricane/view.json')
# header={'ddd': weather_key})

print(res.json())
#
#
# current_location = input("Please enter your zip-code: ")
# print("You entered: {}". format(current_location))
