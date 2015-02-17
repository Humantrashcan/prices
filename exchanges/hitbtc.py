from decimal import Decimal
from helpers import *
import requests

TICKER_URL = 'https://api.hitbtc.com/api/1/public/ticker'

def get_current_bid_BCNBTC():
    data = get_response(TICKER_URL)
    price = data['BCNBTC']['bid']
    return Decimal(price)

def get_current_ask_BCNBTC():
    data = get_response(TICKER_URL)
    price = data['BCNBTC']['ask']
    return Decimal(price)

def get_current_bid_BTCEUR():
    data = get_response(TICKER_URL)
    price = data['BTCEUR']['bid']
    return Decimal(price)

def get_current_ask_BTCEUR():
    data = get_response(TICKER_URL)
    price = data['BTCEUR']['ask']
    return Decimal(price)

def get_current_bid_BTCUSD():
    data = get_response(TICKER_URL)
    price = data['BTCUSD']['bid']
    return Decimal(price)

def get_current_ask_BTCUSD():
    data = get_response(TICKER_URL)
    price = data['BTCUSD']['ask']
    return Decimal(price)

def get_current_bid_DOGEBTC():
    data = get_response(TICKER_URL)
    price = data['DOGEBTC']['bid']
    return Decimal(price)

def get_current_ask_DOGEBTC():
    data = get_response(TICKER_URL)
    price = data['DOGEBTC']['ask']
    return Decimal(price)

def get_current_bid_EURGBP():
    data = get_response(TICKER_URL)
    price = data['EURGBP']['bid']
    return Decimal(price)

def get_current_ask_EURGBP():
    data = get_response(TICKER_URL)
    price = data['EURGBP']['ask']
    return Decimal(price)

def get_current_bid_EURUSD():
    data = get_response(TICKER_URL)
    price = data['EURUSD']['bid']
    return Decimal(price)

def get_current_ask_EURUSD():
    data = get_response(TICKER_URL)
    price = data['EURUSD']['ask']
    return Decimal(price)

def get_current_bid_FCNBTC():
    data = get_response(TICKER_URL)
    price = data['FCNBTC']['bid']
    return Decimal(price)

def get_current_ask_FCNBTC():
    data = get_response(TICKER_URL)
    price = data['FCNBTC']['ask']
    return Decimal(price)

def get_current_bid_GBPUSD():
    data = get_response(TICKER_URL)
    price = data['GBPUSD']['bid']
    return Decimal(price)

def get_current_ask_GBPUSD():
    data = get_response(TICKER_URL)
    price = data['GBPUSD']['ask']
    return Decimal(price)

def get_current_bid_LTCBTC():
    data = get_response(TICKER_URL)
    price = data['LTCBTC']['bid']
    return Decimal(price)

def get_current_ask_LTCBTC():
    data = get_response(TICKER_URL)
    price = data['LTCBTC']['ask']
    return Decimal(price)

def get_current_bid_LTCEUR():
    data = get_response(TICKER_URL)
    price = data['LTCEUR']['bid']
    return Decimal(price)

def get_current_ask_LTCEUR():
    data = get_response(TICKER_URL)
    price = data['LTCEUR']['ask']
    return Decimal(price)

def get_current_bid_LTCUSD():
    data = get_response(TICKER_URL)
    price = data['LTCUSD']['bid']
    return Decimal(price)

def get_current_ask_LTCUSD():
    data = get_response(TICKER_URL)
    price = data['LTCUSD']['ask']
    return Decimal(price)

def get_current_bid_NXTBTC():
    data = get_response(TICKER_URL)
    price = data['NXTBTC']['bid']
    return Decimal(price)

def get_current_ask_NXTBTC():
    data = get_response(TICKER_URL)
    price = data['NXTBTC']['ask']
    return Decimal(price)

def get_current_bid_QCNBTC():
    data = get_response(TICKER_URL)
    price = data['QCNBTC']['bid']
    return Decimal(price)

def get_current_ask_QCNBTC():
    data = get_response(TICKER_URL)
    price = data['QCNBTC']['ask']
    return Decimal(price)

def get_current_bid_XDNBTC():
    data = get_response(TICKER_URL)
    price = data['XDNBTC']['bid']
    return Decimal(price)

def get_current_ask_XDNBTC():
    data = get_response(TICKER_URL)
    price = data['XDNBTC']['ask']
    return Decimal(price)

def get_current_bid_XMRBTC():
    data = get_response(TICKER_URL)
    price = data['XMRBTC']['bid']
    return Decimal(price)

def get_current_ask_XMRBTC():
    data = get_response(TICKER_URL)
    price = data['XMRBTC']['ask']
    return Decimal(price)