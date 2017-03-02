import datetime
import numpy as np

import matplotlib.finance as finance
import matplotlib.dates as mdates
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

startdate = datetime.date(2014,4,12)
today = enddate = datetime.date.today()

plt.rc('axes', grid=True)
plt.rc('grid', color='0.75', linestyle='-', linewidth=0.5)
rect = [0.4, 0.5, 0.8, 0.5]

fig = plt.figure(facecolor='white', figsize=(12,11))

axescolor = '#f6f6f6' # the axes background color

ax = fig.add_axes(rect, axisbg=axescolor)
ax.set_ylim(10,800)

def plotTicker(ticker, startdate, enddate, fillcolor):
  """
     matplotlib.finance has fetch_historical_yahoo() which fetches 
     stock price data the url where it gets the data from is 
     http://ichart.yahoo.com/table.csv stores in a numpy record 
     array with fields: 
      date, open, high, low, close, volume, adj_close
  """

  fh = finance.fetch_historical_yahoo(ticker, startdate, enddate) 
  r = mlab.csv2rec(fh); 
  fh.close()
  r.sort()

  ### plot the relative strength indicator
  prices = r.adj_close

  ### plot the price and volume data
  
  ax.plot(r.date, prices, color=fillcolor, lw=2, label=ticker)
  ax.legend(loc='top right', shadow=True, fancybox=True)

  # set the labels rotation and alignment 
  for label in ax.get_xticklabels():
    # To display date label slanting at 30 degrees
    label.set_rotation(30)
    label.set_horizontalalignment('right')

  ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')

#plot the tickers now
plotTicker('BIDU', startdate, enddate, 'red')
plotTicker('GOOG', startdate, enddate, '#1066ee')
plotTicker('AMZN', startdate, enddate, '#506612')

#One may also use thse
#plotTicker('TWTR', startdate, enddate, '#c72020')
#plotTicker('LNKD', startdate, enddate, '#103474')
#plotTicker('FB', startdate, enddate, '#506612')


plt.show()

