import math, numpy

from math import log, sqrt, exp, sin, cos, degrees, radians, atan2, acos
from numpy import cross, dot, array
from matplotlib import pyplot
from random import gauss

def meanAngle(angles, inDegrees=True):
  sumCos = 0.0
  sumSin = 0.0
  
  for angle in angles:
    if inDegrees:
      angle = radians(angle)
    sumCos += cos(angle)
    sumSin += sin(angle)
    
  N = len(angles)
  meanAngle = atan2(sumSin/N, sumCos/N)

  if inDegrees:
    meanAngle = degrees(meanAngle)

  return meanAngle

def transposeMatrix(x):
  nrows = len(x)
  ncols = len(x[0])
  return [[x[n][m] for n in range(nrows)] for m in range(ncols)]
  
  
def multiplyMatrices(x, y):
  rowsX = len(x)
  colsX = len(x[0])
  rowsY = len(y)
  colsY = len(y[0])

  if colsX != rowsY:
    message = 'x is %d x %d; inconsistent with y which is %d x %d'
    raise Exception(message % (rowsX, colsX, rowsY, colsY))
  z = rowsX * [0]   # Constructs a list of zeros, of size rowsX
  for i in range(rowsX):
    z[i] = colsY * [0]
    for j in range(colsX):
      for k in range(colsY):
        z[i][k] += x[i][j] * y[j][k]
  return z


def getRotationMatrix(axis, angle):
  vLen = math.sqrt( sum([xyz*xyz for xyz in axis]) )
  x, y, z = [xyz/vLen for xyz in axis]
  c = math.cos(angle)
  d = 1-c
  s = math.sin(angle)
  R = [[c+d*x*x,   d*x*y-s*z, d*x*z+s*y],
       [d*y*x+s*z, c+d*y*y,   d*y*z-s*x],
       [d*z*x-s*y, d*z*y+s*x, c+d*z*z  ]]
  return R


def calcTorsionAngle(coord1, coord2, coord3, coord4):
  bondVec12 = coord1 - coord2
  bondVec32 = coord3 - coord2
  bondVec43 = coord4 - coord3

  perpVec13 = cross(bondVec12, bondVec32)
  perpVec24 = cross(bondVec43, bondVec32)

  projection   = dot(perpVec13, perpVec24)
  squareDist13 = dot(perpVec13, perpVec13)
  squareDist24 = dot(perpVec24, perpVec24)

  cosine = projection / sqrt(squareDist13*squareDist24)
  cosine = min(1.0, max(-1.0, cosine))
  angle = acos(cosine)

  if dot(perpVec13, cross(perpVec24, bondVec32)) < 0:
    angle = -angle

  return angle


if __name__ == '__main__':
  x = 2.0

  a = math.log(x)       # logarithm, base e, of x
  b = math.sqrt(x)      # square root of x
  c = math.exp(x)       # e to the power of x


  a = log(x)
  b = sqrt(x)
  c = exp(x)


  angles = [0, 30, 45, 60, 90, 180]
  sines = [math.sin(math.radians(angle)) for angle in angles]
  # [0.000, 0.500, 0.707, 0.866, 1.000, 0.000] (rounded to 3 places)

  angles = [math.degrees(math.asin(sine)) for sine in sines]

  math.floor(5.25)          # 5.0
  math.ceil(5.25)           # 6.0

  int(math.floor(5.25))     # 5
  int(math.ceil(5.25))      # 6

  int(math.floor(-5.25))    # -6; the integer less than the value
  int(-5.25)                # -5; the integer part of the value

  round(8.49)           # 8.0    ; rounded down
  round(8.51)           # 9.0    ; rounded up
  round(3.141592, 1)    # 3.1    ; to one decimal place
  round(3.141592, 3)    # 3.142  ; to three decimal places
  round(9621, -2)       # 9600.0 ; to nearest hundred


  # Matplotlib graphs and charts
  
  # One line plot
  values = [x*x for x in range(10)]
  pyplot.plot(values)
  pyplot.show()

  # Two line plots
  valuesA = [x*x for x in range(1,10)]
  valuesB = [100.0/x for x in range(1,10)]

  pyplot.plot(valuesA)
  pyplot.plot(valuesB)
  pyplot.show()
  
  # X- and Y-axis values specified
  xVals = range(21,30)
  yVals = [100.0/x for x in range(1,10)]

  pyplot.plot(xVals, yVals)
  pyplot.show()

  # Change draw style
  pyplot.plot(xVals, yVals, color='purple',
              linewidth=3.0, label='DataName')
  pyplot.legend()
  pyplot.ylim(0, 101)
  pyplot.yticks([0, 25, 50, 75, 100])
  
  # Save to file
  pyplot.savefig("TestGraph.png", dpi=72)
  pyplot.show()
  
  # Scatter plot
  valsA = range(100)
  valsB = [gauss(0.0, 1.0) for x in valsA]
  pyplot.scatter(valsA, valsB, s=40, marker='*')
  pyplot.show()
  
  # Bar chart
  pyplot.bar(valsA, valsB, color='green')
  pyplot.show()

  # Histogram
  pyplot.hist(valsB, bins=20, range=(-2.0, 2.0))
  pyplot.show()
  
  # Pie chart
  sizes  = [83, 8, 4, 5]
  labels = ['Arthropoda', 'Mollusca', 'Cordata', 'Others']
  colors = ['#B00000', '#D0D000', '#008000', '#4040FF']
  pyplot.pie(sizes, labels=labels, colors=colors)
  pyplot.show()
  
  # Arrays and matrices

  x = [[1,2,3],[4,5,6]]

  y = x[1][2]        # Value in row 1 column 2 (y equals 6)
  x[0][1] = 7        # Value in row 0 column 1 set to 7
                     # x becomes [[1,7,3],[4,5,6]]

  row = x[0]           # Gives [1,2,3]

  cols = [y[2] for y in x]  # Gives [3,6]

  len(x)             # 2
  len(x[0])          # 3

  x = [[1,7,3],[4,5,6]]
  y = transposeMatrix(x)    # y = [[1,4],[7,5],[3,6]]


  #for i in range(m):
  #  z[i] = colsY * [0]

  x = numpy.array([[1,2,3],[4,5,6]])

  x[1][1]                      # 5
  x[1,2]                       # 6

  x = numpy.array([[1,2,3],[4,5,6]], dtype=numpy.float)

  x.shape                      # (2, 3)

  x.size                       # 6 (= 2 x 3)

  len(x.shape)                 # 2

  x = numpy.zeros((2,3))            # 2 x 3 matrix full of 0.0
  x = numpy.ones((3,2))             # 3 x 2 matrix full of 1.0
  x = numpy.identity(3)             # 3 x 3 identity; floating point
  x = numpy.identity(3, numpy.int)  # 3 x 3 identity; integer

  x = numpy.array([1.0, 2.0, 3.0])
  y = numpy.array([3.0, 4.0, 5.0])
  x + y    # array([4.0, 6.0, 8.0])     i.e. 1+3, 2+4, 3+5
  x * y    # array([3.0, 8.0, 15.0])
  x - y    # array([-2.0, -2.0, -2.0])
  x / y    # array([0.33333333, 0.5, 0.6])

  x + 1.0  # array([2.0, 3.0, 4.0])
  y * 5.0  # array([15.0, 20.0, 25.0])

  angles = numpy.array([30.0, 60.0, 90.0, 135.0])
  radians = numpy.radians(angles)
  cosines = numpy.cos(radians)    # array([0.866, 0.50, 0.0, -0.707])
  numpy.log([10.0, 2.71828, 1.0]) # array([2.302585, 1.0, 0.0])
  numpy.exp([2.302585, 1.0, 0.0]) # array([10.0, 2.71828, 1.0])

  x = numpy.array([[1,2,3], [4,5,6]])
  x[0]         # array([1, 2, 3])        - row zero
  x[0,:]       # array([1, 2, 3])        - row zero, as above
  x[:,2]       # array([3, 6])           - column two
  x[-1,:]      # array([4, 5, 6])        - last row
  x[:,1:]      # array([[2, 3],[5, 6]])  - column one onwards
  x[1,0:2]     # array([4, 5])           - row one, first two columns
  x[::-1,:]    # array([[4, 5, 6],[1, 2, 3]]) - reversed rows
  x[:,(2,1,0)] # array([[3, 1, 2],[6, 4, 5]]) - new column order

  x = numpy.array([[4,4], [5,1], [8,3], [7,2]])
  y = numpy.argsort(x[:,1]) # array([1, 3, 2, 0]) - column one order
  x[y,:] # array([[5,1], [7,2], [8,3], [4,4]])
         # re-ordered rows, by column one value

  x = numpy.array([[1,1,1], [1,1,1], [1,1,1]])
  x[1]   = (2,3,4)  #  x; array([[1,1,1], [2,3,4], [1,1,1]])
                    #  new row one
  x[:,2] = (5,6,7)  #  x; array([[1,1,5], [2,3,6], [1,1,7]])
                    #  new column two
  y = numpy.zeros((2,2))
  x[:2,:2] = y      #  x; array([[0,0,5], [0,0,6], [1,1,7]])
                    #  replace 2 x 2 elements with 0
  x[:,:] = 3        #  x; array([[3,3,3], [3,3,3], [3,3,3]])
                    #  replace all elements with 3

  x = numpy.array([[3,6], [2,1], [5,4]])
  x.min()          # 1 ; minimum value
  x.max()          # 6 ; maximum value
  x.max(0)         # array([5,6]) ; maximum value row
  x.max(axis=0)    # same as above
  x.sum()          # 21 ; summation of all elements
  x.sum(0)         # array([10, 11])  ; add rows together
  x.sum(1)         # array([9, 3, 9]) ; add columns together
  x.mean()         # 3.5  ; the mean value of the elements
  x.mean(1)        # array([4.5, 1.5, 4.5]) # mean of each row

  x = numpy.array(range(1,7))  # array([1, 2, 3, 4, 5, 6])
  x = x.reshape((2, 3))        # array([[1, 2, 3], [4, 5, 6]])


  y = x.reshape((3, 2))        # array([[1, 2], [3, 4], [5, 6]])


  y = x.T                      # array([[1, 4], [2, 5], [3, 6]])

  y = x.transpose()            # array([[1, 4], [2, 5], [3, 6]])

  x = numpy.array(((1,1),(1,0)))
  y = numpy.array(((0,1),(1,1)))
  z = numpy.dot(x, y)            # array([[1, 2], [0, 1]])

  z = x * y                    # array([[0, 1], [1, 0]])


  x = numpy.array(((1,1),(1,0)))
  y = numpy.linalg.inv(x)      # array([[0., 1.], [1., -1.]])

  x1, y1, z1 = [1.0, 2.0, 3.0]
  x2, y2, z2 = [3.0, 4.0, 5.0]

  vec1 = (x1, y1, z1)
  vec2 = (x2, y2, z2)
  dotProduct = x1*x2 + y1*y2 + z1*z2
  crossProduct = (y1*z2-z1*y2, z1*x2-x1*z2, x1*y2-y1*x2)

  axis = (1, 1, 1)
  angle = math.radians(60)  # convert from degrees to radians
  rotMatrix = numpy.array(getRotationMatrix(axis, angle))

  vector1 = numpy.array([2, -1, -1])
  vector2 = rotMatrix.dot(vector1)  # [1, -2,  1]

  p1 = array([2,1,1])
  p2 = array([2,0,0])
  p3 = array([3,0,0])
  p4 = array([3,1,-1])
  angle = calcTorsionAngle(p1, p2, p3, p4)
  print(degrees(angle))      # -90.0
