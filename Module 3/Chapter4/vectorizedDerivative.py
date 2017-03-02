import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi/2, np.pi/2, 44)
y = 1/(1+np.cos(x)*np.cos(x))
dy_actual = np.sin(2*x)/(1+np.cos(x)*np.cos(x))**2

fig = plt.figure(figsize=(10,10))
ax=fig.add_subplot(111,axisbg='white')

# we need to specify the size of dy ahead because diff returns 
dy = np.zeros(y.shape, np.float) #we know it will be this size
dy[0:-1] = np.diff(y) / np.diff(x)
dy[-1] = (y[-1] - y[-2]) / (x[-1] - x[-2])

plt.plot(x,y)
plt.plot(x,dy_actual,label='actual derivative')
plt.plot(x,dy,label='forward diff')
plt.legend(loc='upper center')
plt.show()

