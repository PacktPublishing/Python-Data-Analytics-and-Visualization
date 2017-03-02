import numpy as np


arr = np.arange(10000000)
listarr = arr.tolist()

def scalar_multiple(alist, scalar):
    for i, val in enumerate(alist):
        alist[i] = val * scalar
    return alist

# Using IPython's magic timeit command
#timeit  arr +arr
timeit retv = scalar_multiple(listarr, 2.4)

