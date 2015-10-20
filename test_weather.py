# import urllib
import requests
import requests_mock
import os

weather_key = os.environ['WKEY']
#  'noqa' will allow override of long url flag in PEP8


def test_geolookup():  # zip code data for applying to state + city
    with requests_mock.mock() as m:
        m.get('http://api.wunderground.com/api/WKEY/geolookup/q/94107.json',  # noqa
              text='Successful test: Zip code mock data')
        res = requests.get('http://api.wunderground.com/api/WKEY/geolookup/q/94107.json')  # noqa
        print(res.text)


def test_forecast10_day():  # 10 day forecast (at zip)
    with requests_mock.mock() as m:
        m.get('http://api.wunderground.com/api/WKEY/forecast10day/q/CA/San_Francisco.json',  # noqa
              text='Successful test: 10 Day Forecast mock data')
        res = requests.get('http://api.wunderground.com/api/WKEY/forecast10day/q/CA/San_Francisco.json')  # noqa
        print(res.text)


def test_astronomy():      # sunrise + sunset (at zip)
    with requests_mock.mock() as m:
        m.get('http://api.wunderground.com/api/WKEY/astronomy/q/Australia/Sydney.json',  # noqa
              text='Successful test: Sunrise + Sunset mock data')
        res = requests.get('http://api.wunderground.com/api/WKEY/astronomy/q/Australia/Sydney.json')  # noqa
        print(res.text)


def test_alerts():          # alerts of any kind (at zip)
    with requests_mock.mock() as m:
        m.get('http://api.wunderground.com/api/WKEY/alerts/q/IA/Des_Moines.json',  # noqa
              text='Successful test: Alerts mock data')
        res = requests.get('http://api.wunderground.com/api/WKEY/alerts/q/IA/Des_Moines.json')  # noqa
        print(res.text)


def test_hurricane():       # hurricanes anywhere
    with requests_mock.mock() as m:
        m.get('http://api.wunderground.com/api/WKEY/currenthurricane/view.json',  # noqa
              text='Successful test: Hurricane mock data')
        res = requests.get('http://api.wunderground.com/api/WKEY/currenthurricane/view.json')  # noqa
        print(res.text)


def test_run():
    test_geolookup()
    test_forecast10_day()
    test_astronomy()
    test_alerts()
    test_hurricane()

test_run()
