import numpy as np
import matplotlib.pyplot as plt

"""
  SquareBox diagrams are useful for visualizing values of a 2D array,
  Where black color representing sparse areas.  
"""
def sparseDisplay(nonzero, squaresize, ax=None):
    ax = ax if ax is not None else plt.gca()

    ax.patch.set_facecolor('black')
    ax.set_aspect('equal', 'box')
    for row in range(0,squaresize):
      for col in range(0,squaresize):
        if (row,col) in nonzero.keys():
           el = nonzero[(row,col)]
           if el == 0:  color='black' 
           else:  color = '#008000'
           rect = plt.Rectangle([col,row], 1, 1, 
                   facecolor=color, edgecolor=color)
           ax.add_patch(rect)

    ax.autoscale_view()
    ax.invert_yaxis()

if __name__ == '__main__': 
    nonzero={(0,4): 2, (0,7): 1, (1,1): 4, (1,3): 3, (1,8): 1, 
(2,0): 6, (0,9): 2, (2,2): 1, (2,5): 7, (3,9): 1, (5,0): 3, 
(5,2): 2, (5,8): 3, (6,3): 2, (6,6): 1, (7,8): 1, (8,0): 3, (8,2): 2, (8,9): 1, (9,1): 3}
    
    plt.figure(figsize=(4,4))
    sparseDisplay(nonzero, 10)
    plt.show()

