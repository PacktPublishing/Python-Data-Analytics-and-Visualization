import numpy as np
from time import time

def incrembyone(x):
    return x + 1

dataarray=np.linspace(1,5,1000000)

t1=time()
lendata = len(dataarray)
print "Len = "+str(lendata)
print dataarray[1:7]
for i in range(lendata):
    dataarray[i]+=1
print " time for loop (No vectorization)->" + str(time() - t1)

t2=time()

vecincr = np.vectorize(incrembyone)
vecincr(dataarray)
print " time for vectorized version-1:" + str(time() - t2)
t3 = time()

dataarray+=1  # how does this achieve the results
print dataarray[1:7]
print " time for vectorized version-2:" + str(time() - t3)

