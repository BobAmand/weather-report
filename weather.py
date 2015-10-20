# import urllib
import requests
import requests_mock
import os

weather_key = os.environ['WKEY']


with requests_mock.mock() as m:
    m.get('http://api.wunderground.com/api/WKEY/currenthurricane/view.json',
          text='Successful test')
    res = requests.get('http://api.wunderground.com/api/WKEY/currenthurricane/view.json')
    print(res.text)



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
#
#
# current_location = input("Please enter your zip-code: ")
# print("You entered: {}". format(current_location))
