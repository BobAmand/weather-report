import requests
import os

weather_key = os.environ['WKEY']

res = request.get('http://......', header={'ddd': weather_key})

print(res.json())
