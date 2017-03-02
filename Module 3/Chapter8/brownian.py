from numpy.random import standard_normal
from numpy import zeros, sqrt
import matplotlib.pyplot as plt

S_init = 20.222
T =1
tstep =0.0002
sigma = 0.4
mu = 1
NumSimulation=6

colors = [ (214,27,31), (148,103,189), (229,109,0), (41,127,214), 
(227,119,194),(44,160,44),(227,119,194), (72,17,121), (196,156,148)]  

# Scale the RGB values to the [0, 1] range.  

for i in range(len(colors)):  
    r, g, b = colors[i]  
    colors[i] = (r / 255., g / 255., b / 255.)  
    
plt.figure(figsize=(12,12))

Steps=round(T/tstep); #Steps in years
S = zeros([NumSimulation, Steps], dtype=float)
x = range(0, int(Steps), 1)

for j in range(0, NumSimulation, 1):

    S[j,0]= S_init
    for i in x[:-1]:
       S[j,i+1]=S[j,i]+S[j,i]*(mu-0.5*pow(sigma,2))*tstep+ \
          sigma*S[j,i]*sqrt(tstep)*standard_normal()
    plt.plot(x, S[j], linewidth=2., color=colors[j])

plt.title('%d Simulation using %d Steps, \n$\sigma$=%.6f $\mu$=%.6f $S_0$=%.6f ' % (int(NumSimulation), int(Steps), sigma, mu, S_init), 
          fontsize=18)
plt.xlabel('steps', fontsize=16)
plt.grid(True)
plt.ylabel('stock price', fontsize=16)
plt.ylim(0,90)

plt.show()

