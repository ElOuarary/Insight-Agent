from dotenv import load_dotenv
import os
import pandas as pd
import requests


load_dotenv()
API_KEY = os.getenv('API_KEY')

URL = 'https://api.openaq.org/v3'
HEADERS = {
    'x-api-key': API_KEY
}


# Fetch the responce for the countries endpoint
def fetch_countries(id: int = None):
    url = f'{URL}/countries/{id}' if id else f'{URL}/countries'
    responce: requests.Response = requests.get(url, headers=HEADERS)
    if responce.status_code == 200:
        return responce.json()
    return f'Status code {responce.status_code}'


# Fetch the responce for the parameters endpoint
def fetch_parameters():
    url = f'{URL}/parameters'
    responce = requests.get(url, headers=HEADERS)
    if responce.status_code == 200:
        return responce.json()
    return f'Status code {responce.status_code}'
    
    
# Fetch the responce from the location endpoint
def fetch_location(countries_id: int):
    url = f'{URL}/locations'
    params = {'countries_id': countries_id}
    responce = requests.get(url, params, headers=HEADERS)
    if responce.status_code == 200:
        return responce.json()
    return f'Status code {responce.status_code}'


# Fetch the responce from the instruments endpoint
def fetch_instruments(id: int = None):
    url = f'{URL}/instuments/{id}' if id else f'{URL}/instruments'
    responce = requests.get(url, headers=HEADERS)
    if responce.status_code == 200:
        return responce.json()
    return f'Status code {responce.status_code}'

