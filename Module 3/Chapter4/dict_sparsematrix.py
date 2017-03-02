def getElement(row, col):
    if (row,col) in A.keys():
       r = A[row,col]
    else:
       r = 0
    return r

A={(0,4): 2, (0,7): 1, (1,1): 4, (1,3):3, (1,8): 1, (2,0): 6, (0,9): 2, (2,2):1, (2,5): 7, (3,9): 1, (5,0): 3, (5,2): 2, (5,8): 3, (6,3): 2, (6,6):1, (7,8): 1, (8,0): 3, (8,2): 2, (8,9): 1, (9,1): 3}

print getElement(1,3)

print getElement(1,2)

