from exchanges import helpers
from exchanges import kraken
from decimal import Decimal

### Kraken opportunities
#### ARBITRAGE OPPORTUNITY 1
def opportunity_1():
  sellLTCbuyEUR = kraken.get_current_bid_LTCEUR()
  sellEURbuyXBT = kraken.get_current_ask_XBTEUR()
  sellXBTbuyLTC = kraken.get_current_ask_XBTLTC()
  opport = 1-((sellLTCbuyEUR/sellEURbuyBTX)*sellXBTbuyLTC)
  return Decimal(opport)
  
def opportunity_2():
  sellEURbuyLTC = kraken.get_current_ask_LTCEUR()
  sellLTCbuyXBT = kraken.get_current_ask_XBTLTC()
  sellXBTbuyEUR = kraken.get_current_bid_XBTEUR()
  opport = 1-(((1/sellEURbuyLTC)/sellLTCbuyXBT)*sellXBTbuyEUR)
  return Decimal(opport)