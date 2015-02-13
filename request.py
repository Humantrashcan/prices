from exchanges import helpers
from exchanges import bitfinex
from exchanges import bitstamp
from exchanges import okcoin
from exchanges import cex
from exchanges import btce
from time import sleep
import csv


# PREPARE OUTPUT FILE

# tell computer where to put CSV
outfile_path='csvoutput.csv'

# open it up, the w means we will write to it
writer = csv.writer(open(outfile_path, 'w'))

#create a list with headings for our columns
headers = ['bitstamp_price', 'bitstamp_bid', 'bitstamp_ask', 'bitfinex_price', 'bitfinex_bid', 'bitfinex_ask', 'okcoin_price', 'okcoin_bid', 'okcoin_ask', 'cex_price', 'cex_bid', 'cex_ask', 'btc-e_price', 'btc-e_bid', 'btc_ask']

#write the row of headings to our CSV file
writer.writerow(headers)



# GET DATA, PUT INTO FILE - LOOP FOR A CERTAIN TIME

#set a counter telling us how many times we've gone through the loop, this is the first time, so we'll set it at 1
i = 1

#loop through pages of JSON returned, 100 is an arbitrary number
while i < 100:
  #print out what number loop we are on, which will make it easier to track down problems when they appear
  print i


  #initialize the row
  row = []
  
  #add every 'cell' to the row list, identifying the item just like an index in a list
  row.append(bitstamp.get_current_price())
  row.append(bitstamp.get_current_bid())
  row.append(bitstamp.get_current_ask())
  row.append(bitfinex.get_current_price())
  row.append(bitfinex.get_current_bid())
  row.append(bitfinex.get_current_ask())
  row.append(okcoin.get_current_price())	
  row.append(okcoin.get_current_bid())
  row.append(okcoin.get_current_ask())
  row.append(cex.get_current_price())	
  row.append(cex.get_current_bid())
  row.append(cex.get_current_ask())
  row.append(btce.get_current_price())	
  row.append(btce.get_current_bid())
  row.append(btce.get_current_ask())  
  
  
  
  
  #once you have all the cells in there, write the row to your csv
  writer.writerow(row)
  
  #increment our loop counter, now we're on the next time through the loop
  i = i + 1
  #tell Python to rest for 5 secs, so we don't exceed our rate limit
  sleep(5)