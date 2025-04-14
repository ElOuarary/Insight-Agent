from dotenv import load_dotenv
import os
import requests


load_dotenv()
API_KEY = os.getenv('API_KEY')

URL = 'https://api.openaq.org/v3'
HEADERS = {
    'x-api-key': API_KEY
}

def fetch_countries(id: int = None):
    if id:
        url = f'{URL}/countries/{id}'
    else:
        url = f'{URL}/countries'
    responce: requests.Response = requests.get(url, headers=HEADERS)
    if responce.status_code == 200:
        return responce.json()
    else:
        return f'Status code {responce.status_code}'
    
def fetch_parameters(iso: str = None, countries_id: int = None):
    parms = {}
    if iso:
        parms['iso'] = iso
    if countries_id:
        parms['countries_id'] = countries_id
    url = f'{URL}/parameters'
    responce: requests.Response = requests.get(url, parms=parms,headers=HEADERS)
    if responce.status_code == 200:
        return responce.json()
    else:
        return f'Status code {responce.status_code}'
    
def fetch_locations(iso: str = None, countries_id: int = None):
    parms = {}
    if iso:
        parms['iso'] = iso
    if countries_id:
        parms['countries_id'] = countries_id
    url = f'{URL}/locations'
    responce: requests.Response = requests.get(url, parms=parms,headers=HEADERS)
    if responce.status_code == 200:
        return responce.json()
    else:
        return f'Status code {responce.status_code}'