from pylab import plotfile, show, gca 
import matplotlib.cbook as cbook  
fname = cbook.get_sample_data('/Users/MacBook/Downloads/Book_Code/Chapter4/amzn.csv', asfileobj=False) 
plotfile(fname, ('date', 'high', 'low', 'close'), subplots=False) 
show()

