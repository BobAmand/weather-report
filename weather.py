import requests
import requests_mock
import os

weather_key = os.environ['WKEY']

with requests_mock.mock() as m:
    m.get('http://api.wunderground.com/api/WKEY/currenthurricane/view.json',
          text='Successful test')
    res = requests.get('http://api.wunderground.com/api/WKEY/currenthurricane/view.json')
    print(res.text)

# header={'ddd': weather_key})

# print(res.json())
#
#
# current_location = input("Please enter your zip-code: ")
# print("You entered: {}". format(current_location))
