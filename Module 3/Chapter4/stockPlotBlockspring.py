import blockspring 
import json  

print blockspring.runParsed("stock-price-comparison", 
   { "tickers": "FB, LNKD, TWTR", 
   "start_date": "2014-01-01", "end_date": "2015-01-01" }).params

