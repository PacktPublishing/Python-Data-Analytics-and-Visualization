import numpy as np
import matplotlib.pyplot as plt

# create n values of x from 0 to 2*pi 
x = np.linspace(0, 8*np.pi, 100)
y = np.sin(x/2)

#interpolate new y-values 
yinterp = np.interp(x, x, y)

#plot x,y values using circle marker (line style)
plt.plot(x, y, 'o')  

#plot interpolated curve using dash x marker
plt.plot(x, yinterp, '-x')  
plt.show()

