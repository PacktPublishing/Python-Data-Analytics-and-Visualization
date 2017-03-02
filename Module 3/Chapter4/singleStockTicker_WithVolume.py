import datetime

import matplotlib.finance as finance
import matplotlib.dates as mdates
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

startdate = datetime.date(2013,3,1)
today = enddate = datetime.date.today()

rect = [0.1, 0.3, 0.8, 0.4]   

fig = plt.figure(facecolor='white', figsize=(10,9))  
ax = fig.add_axes(rect, axisbg='#f6f6f6')

def plotSingleTickerWithVolume(ticker, startdate, enddate):
    
    global ax

    fh = finance.fetch_historical_yahoo(ticker, startdate, enddate)
    
    # a numpy record array with fields: 
    #     date, open, high, low, close, volume, adj_close
    r = mlab.csv2rec(fh); 
    fh.close()
    r.sort()
    
    plt.rc('axes', grid=True)
    plt.rc('grid', color='0.78', linestyle='-', linewidth=0.5)
    
    axt = ax.twinx()
    prices = r.adj_close

    fcolor = 'darkgoldenrod'

    ax.plot(r.date, prices, color=r'#1066ee', lw=2, label=ticker)
    ax.fill_between(r.date, prices, 0, prices, facecolor='#BBD7E5')
    ax.set_ylim(0.5*prices.max())

    ax.legend(loc='upper right', shadow=True, fancybox=True)
    
    volume = (r.close*r.volume)/1e6  # dollar volume in millions
    vmax = volume.max()
   
    axt.fill_between(r.date, volume, 0, label='Volume', 
                 facecolor=fcolor, edgecolor=fcolor)

    axt.set_ylim(0, 5*vmax)
    axt.set_yticks([])
    
    for axis in ax, axt:  
        for label in axis.get_xticklabels():
            label.set_rotation(30)
            label.set_horizontalalignment('right')
    
        axis.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')

plotSingleTickerWithVolume ('MSFT', startdate, enddate)
plt.show()

