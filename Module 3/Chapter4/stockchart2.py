from pylab import plotfile, show
import matplotlib.cbook as cbook  
fname = cbook.get_sample_data('/Users/MacBook/Downloads/Book_code/Chapter4/amzn.csv', asfileobj=False) 
plotfile(fname, (0,1,5), plotfuncs={5:'bar'}) 
show()

