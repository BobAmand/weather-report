# import urllib
import requests
import requests_mock
import os

weather_key = os.environ['WKEY']
#  'noqa' will allow override of long url flag in PEP8

def test_forecast10_day():  # 10 day forecast (at zip)
    with requests_mock.mock() as m:
        m.get('http://api.wunderground.com/api/WKEY/forecast10day/q/CA/San_Francisco.json',  # noqa
              text='10 Day Forecast mock data: Successful test')
        res = requests.get('http://api.wunderground.com/api/WKEY/forecast10day/q/CA/San_Francisco.json')  # noqa
        print(res.text)


def test_astronomy():      # sunrise + sunset (at zip)
    with requests_mock.mock() as m:
        m.get('http://api.wunderground.com/api/WKEY/astronomy/q/Australia/Sydney.json',  # noqa
              text='Sunrise + Sunset mock data: Successful test')
        res = requests.get('http://api.wunderground.com/api/WKEY/astronomy/q/Australia/Sydney.json')  # noqa
        print(res.text)


def test_alerts():          # alerts of any kind (at zip)
    with requests_mock.mock() as m:
        m.get('http://api.wunderground.com/api/WKEY/alerts/q/IA/Des_Moines.json',  # noqa
              text='Alerts mock data: Successful test')
        res = requests.get('http://api.wunderground.com/api/WKEY/alerts/q/IA/Des_Moines.json')  # noqa
        print(res.text)


def test_hurricane():       # hurricanes anywhere
    with requests_mock.mock() as m:
        m.get('http://api.wunderground.com/api/WKEY/currenthurricane/view.json',  # noqa
              text='Hurricane mock data: Successful test')
        res = requests.get('http://api.wunderground.com/api/WKEY/currenthurricane/view.json')  # noqa
        print(res.text)


def test_run():
    test_forecast10_day()
    test_astronomy()
    test_alerts()
    test_hurricane()

test_run()
