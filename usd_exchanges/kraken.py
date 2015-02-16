from decimal import Decimal
from helpers import *
import requests

TICKER_URL = 'https://api.kraken.com/0/public/Ticker?pair=XXBTZUSD,XXBTZEUR'

def get_current_price():
    data = get_response(TICKER_URL)
    price = data['result']['XXBTZEUR']['b'][0]
    price2 = data['result']['XXBTZUSD']['b']
    return (price, price2)

def get_current_bid():
    data = get_response(TICKER_URL)
    price = data['btc_usd']['buy']
    return Decimal(price)

def get_current_ask():
    data = get_response(TICKER_URL)
    price = data['btc_usd']['sell']
    return Decimal(price)
	
print get_current_price()