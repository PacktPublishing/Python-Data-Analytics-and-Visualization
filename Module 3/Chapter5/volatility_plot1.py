import pandas.io.data as stockdata
import numpy as np

r,g,b=(31,  119, 180)
colornow=(r/255.,g/255.,b/255.)
ibmquotes = stockdata.DataReader(name='IBM', data_source='yahoo', start='2005-10-1')
ibmquotes['Volatility'] = np.log(ibmquotes['Close']/
    ibmquotes['Close'].shift(1))
ibmquotes[['Close', 'Volatility']].plot(figsize=(12,10),subplots=True, color=colornow) 

