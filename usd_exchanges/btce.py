from decimal import Decimal
from helpers import *
import requests

TICKER_URL = 'https://btc-e.com/api/3/ticker/btc_usd'

def get_current_price():
    data = get_response(TICKER_URL)
    price = data['btc_usd']['last']
    return Decimal(price)

def get_current_bid():
    data = get_response(TICKER_URL)
    price = data['btc_usd']['buy']
    return Decimal(price)

def get_current_ask():
    data = get_response(TICKER_URL)
    price = data['btc_usd']['sell']
    return Decimal(price)