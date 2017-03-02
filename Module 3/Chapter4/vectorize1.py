import numpy as np

def posquare(x):
  if x >= 0: return x**2
  else: return -x

i = np.random.randint(25)
poly1 = np.arange(i,i+10)

print poly1
vecfunc = np.vectorize(posquare, otypes=[float]) 
vecfunc(poly1)

