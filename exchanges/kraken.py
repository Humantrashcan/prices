from decimal import Decimal
from helpers import *
import requests

TICKER_URL = 'https://api.kraken.com/0/public/Ticker?pair=XLTCZEUR,XXBTZEUR,XXBTZUSD,XLTCZUSD,XXBTXLTC'

def get_current_bid_LTCEUR():
    data = get_response(TICKER_URL)
    price = data['result']['XLTCZEUR']['b'][0]
    return Decimal(price)

def get_current_ask_LTCEUR():
    data = get_response(TICKER_URL)
    price = data['result']['XLTCZEUR']['a'][0]
    return Decimal(price)

def get_current_bid_XBTEUR():
    data = get_response(TICKER_URL)
    price = data['result']['XXBTZEUR']['b'][0]
    return (price, price2)

def get_current_ask_XBTEUR():
    data = get_response(TICKER_URL)
    price = data['result']['XXBTZEUR']['a'][0]
    return Decimal(price)
	
def get_current_bid_XBTUSD():
    data = get_response(TICKER_URL)
    price = data['result']['XXBTZUSD']['b'][0]
    return (price, price2)

def get_current_ask_XBTUSD():
    data = get_response(TICKER_URL)
    price = data['result']['XXBTZUSD']['a'][0]
    return Decimal(price)
	
def get_current_bid_LTCUSD():
    data = get_response(TICKER_URL)
    price = data['result']['XLTCZUSD']['b'][0]
    return (price, price2)

def get_current_ask_LTCUSD():
    data = get_response(TICKER_URL)
    price = data['result']['XLTCZUSD']['a'][0]
    return Decimal(price)
	
def get_current_bid_XBTLTC():
    data = get_response(TICKER_URL)
    price = data['result']['XXBTXLTC']['b'][0]
    return (price, price2)

def get_current_ask_XBTLTC():
    data = get_response(TICKER_URL)
    price = data['result']['XXBTXLTC']['a'][0]
    return Decimal(price)