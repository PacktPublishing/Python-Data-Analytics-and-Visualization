from math import pow, sqrt
dist=[]
def determineFruit(xv, yv, threshold_radius):
  for i in range(1,len(x)):
    xdif=pow(float(x[i])-xv, 2)
    ydif=pow(float(y[i])-yv, 2)
    sqrtdist = sqrt(xdif+ydif)
    if ( xdif < threshold_radius and 
         ydif < threshold_radius and sqrtdist < threshold_radius):
      dist.append(sqrtdist)
    else:
      dist.append(99)
  pear_count=0
  apple_count=0
  banana_count=0
  for i in range(1,len(dist)):
      if dist[i] < threshold_radius:
        if z[i] == 'g': pear_count += 1
        if z[i] == 'r': apple_count += 1
        if z[i] == 'y': banana_count += 1
  if ( apple_count >= pear_count and apple_count >= banana_count ):
    return "apple"
  elif ( pear_count >= apple_count and pear_count >= banana_count):
    return "pear"
  elif ( banana_count >= apple_count and banana_count >= pear_count):
    return "banana"

dist=[]
determine = determineFruit(3.5,6.2, 1)
print determine

