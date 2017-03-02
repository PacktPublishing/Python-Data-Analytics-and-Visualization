import numpy as np
from math import log

import matplotlib.pyplot as plt

x=[]
y=[]

#Equation that defines Profit
def generateProfit(d):

   global s

   if d >= s: 
     return 0.6*s
   else:
     return 0.6*d - 0.4*(s-d)

# Although y comes from uniform distribution in [80,140]
# we are running simulation for d in [20,305]

maxprofit=0

for s in range (20, 305):

  # Run a simulation for n = 1000 
  # Even if we run for n = 10,000 the result would
  # be almost the same
  for i in range(1,1000):

     # generate a random value of d 
     d = np.random.randint(10,high=200)

     # for this random value of d, find profit and
     # update maxprofit
     profit = generateProfit(d)
     if profit > maxprofit:
        maxprofit = profit
  
  #store the value of s to be plotted along X axis 
  x.append(s)

  #store the value of maxprofit plotted along Y axis 
  y.append(log(maxprofit)) # plotted on log scale

plt.plot(x,y)
print "Max Profit:",maxprofit


