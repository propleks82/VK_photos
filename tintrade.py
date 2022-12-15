import requests
import json

url = 'https://tinkoff.github.io › invest-openapi'
tintrade = requests.get(url)
print(tintrade.status_code)