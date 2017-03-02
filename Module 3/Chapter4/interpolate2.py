import numpy as np 
import matplotlib.pyplot as plt
from scipy.interpolate import splprep, splev

t = np.arange(0, 2.5, .1)
x = np.sin(2*np.pi*t)
y = np.cos(2*np.pi*t)

tcktuples,uarray = splprep([x,y], s=0)
unew = np.arange(0, 1.01, 0.01)

splinevalues = splev(unew, tcktuples)

plt.figure(figsize=(10,10))
plt.plot(x, y, 'x', splinevalues[0], splinevalues[1], 
np.sin(2*np.pi*unew), np.cos(2*np.pi*unew), x, y, 'b')

plt.legend(['Linear', 'Cubic Spline', 'True'])
plt.axis([-1.25, 1.25, -1.25, 1.25])
plt.title('Parametric Spline Interpolation Curve')

plt.show()

