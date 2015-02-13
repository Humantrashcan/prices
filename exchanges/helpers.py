# this file checks the status of the URL, and the status of the JSON

import requests
from datetime import datetime

def get_datetime():
    return datetime.now().strftime('%Y-%m-%d')

def get_response(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
