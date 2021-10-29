# www.github.com/baptisteCanac
import requests
import json

headers = {
    'x-rapidapi-key': "45b20fe2fdmsh7fdc8a8e38f20ddp1bd462jsna65b10c1743c",
    'x-rapidapi-host': "coinpaprika1.p.rapidapi.com"
    }
params = {
    "start": "1",
    "limit": "5",
    "convert": "usd"
}

url = "https://coinpaprika1.p.rapidapi.com/tickers"

response = requests.request("GET", url, params=params, headers=headers)

print(response.text)
#print(response.text)