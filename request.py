from exchanges import helpers
from exchanges import hitbtc
from time import sleep
from datetime import datetime
import csv


# PREPARE OUTPUT FILE

# tell computer where to put CSV and to name it
filename = datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
outfile_path='csvoutput'+filename+'.csv'

# open it up, the w means we will write to it
writer = csv.writer(open(outfile_path, 'w'))

#create a list with headings for our columns
headers = ['datetime','hitbtc_BCNBTC_bid','hitbtc_BCNBTC_ask',
'hitbtc_BTCEUR_bid','hitbtc_BTCEUR_ask',
'hitbtc_BTCUSD_bid','hitbtc_BTCUSD_ask',
'hitbtc_DOGEBTC_bid','hitbtc_DOGEBTC_ask',
'hitbtc_EURGBP_bid','hitbtc_EURGBP_ask',
'hitbtc_EURUSD_bid','hitbtc_EURUSD_ask',
'hitbtc_FCNBTC_bid','hitbtc_FCNBTC_ask',
'hitbtc_GBPUSD_bid','hitbtc_GBPUSD_ask',
'hitbtc_LTCBTC_bid','hitbtc_LTCBTC_ask',
'hitbtc_LTCEUR_bid','hitbtc_LTCEUR_ask',
'hitbtc_LTCUSD_bid','hitbtc_LTCUSD_ask',
'hitbtc_NXTBTC_bid','hitbtc_NXTBTC_ask',
'hitbtc_QCNBTC_bid','hitbtc_QCNBTC_ask',
'hitbtc_XDNBTC_bid','hitbtc_XDNBTC_ask',
'hitbtc_XMRBTC_bid','hitbtc_XMRBTC_ask',


]

#write the row of headings to our CSV file
writer.writerow(headers)



# GET DATA, PUT INTO FILE - LOOP FOR A CERTAIN TIME

#set a counter telling us how many times we've gone through the loop, this is the first time, so we'll set it at 1
i = 1

#loop through pages of JSON returned, 100 is an arbitrary number
while i < 200:
  #print out what number loop we are on, which will make it easier to track down problems when they appear
  print i


  #initialize the row
  row = []
  
  #add every 'cell' to the row list, identifying the item just like an index in a list
  row.append(datetime.now())
 
 # HITBTC
  row.append(hitbtc.get_current_bid_BCNBTC())
  row.append(hitbtc.get_current_ask_BCNBTC())
  row.append(hitbtc.get_current_bid_BTCEUR())	
  row.append(hitbtc.get_current_ask_BTCEUR())
  row.append(hitbtc.get_current_bid_BTCUSD())	
  row.append(hitbtc.get_current_ask_BTCUSD())
  row.append(hitbtc.get_current_bid_DOGEBTC())	
  row.append(hitbtc.get_current_ask_DOGEBTC())
  row.append(hitbtc.get_current_bid_EURGBP())	
  row.append(hitbtc.get_current_ask_EURGBP())
  row.append(hitbtc.get_current_bid_EURUSD())	
  row.append(hitbtc.get_current_ask_EURUSD())
  row.append(hitbtc.get_current_bid_FCNBTC())	
  row.append(hitbtc.get_current_ask_FCNBTC())
  row.append(hitbtc.get_current_bid_GBPUSD())	
  row.append(hitbtc.get_current_ask_GBPUSD())
  row.append(hitbtc.get_current_bid_LTCBTC())	
  row.append(hitbtc.get_current_ask_LTCBTC())
  row.append(hitbtc.get_current_bid_LTCEUR())	
  row.append(hitbtc.get_current_ask_LTCEUR())
  row.append(hitbtc.get_current_bid_LTCUSD())	
  row.append(hitbtc.get_current_ask_LTCUSD())
  row.append(hitbtc.get_current_bid_NXTBTC())	
  row.append(hitbtc.get_current_ask_NXTBTC())
  row.append(hitbtc.get_current_bid_QCNBTC())	
  row.append(hitbtc.get_current_ask_QCNBTC())
  row.append(hitbtc.get_current_bid_XDNBTC())	
  row.append(hitbtc.get_current_ask_XDNBTC())
  row.append(hitbtc.get_current_bid_XMRBTC())	
  row.append(hitbtc.get_current_ask_XMRBTC())

  
  #once you have all the cells in there, write the row to your csv
  writer.writerow(row)
  
  #increment our loop counter, now we're on the next time through the loop
  i = i + 1
  #tell Python to rest for 5 secs, so we don't exceed our rate limit
  sleep(5)