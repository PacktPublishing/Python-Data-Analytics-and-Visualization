import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import animation  

# Set up the figure, axis, and the plot element to be animated 
fig = plt.figure() 
ax = plt.axes(xlim=(0, 3.2), ylim=(-2.14, 2.14)) 
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(0, 2, 1000)
    xval = 2 * np.pi * (x - 0.01 * i)
    y = np.cos(xval) # Here we are trying to animate cos function
    line.set_data(x, y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,\
            frames=200, interval=20, blit=True)
anim.save('basic_animation.mp4', fps=30)
plt.show()

