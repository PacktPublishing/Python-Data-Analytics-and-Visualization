import matplotlib.pyplot as plt

fig = plt.figure(figsize=(15,10), facecolor='w')
ax = fig.add_subplot(111)

def plotCircle(x,y,radius,color, alphaval):
  circle = plt.Circle((x, y), radius=radius, fc=color, alpha=alphaval)
  fig.gca().add_patch(circle)
  nofcircle = plt.Circle((x, y), radius=radius, ec=color, fill=False)
  fig.gca().add_patch(nofcircle)

x = [55,83,90,13,55,82,96,55,69,19,55,95,62,96,82,30,22,39,54,50,69,
   56,58,55,55,47,55,20,86,78,56]
y = [5,3,4,0,1,0,1,3,5,2,2,0,2,4,6,0,0,1,0,0,0,0,1,1,0,0,3,0,0,1,0]
r = [23,17,15,13,13,12,12,11,11,10,10,10,10,10,9,9,9,8,8,8,8,8,8,
   8,7,7,7,7,6,6,6]
for i in range(0,len(x)):
  plotCircle(x[i],y[i],r[i],'b', 0.1)

plt.axis('scaled')
plt.show()

