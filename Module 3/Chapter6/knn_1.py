import csv
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

count=0
x=[]
y=[]
z=[]

with open('/Users/MacBook/Downloads/Book_Code/Chapter6/fruits_data.csv', 'r') as csvf:
  reader = csv.reader(csvf, delimiter=',')
  for row in reader:
    if count > 0:
      x.append(row[0])
      y.append(row[1])
      if ( row[2] == 'Apple' ): z.append('r')
      elif ( row[2] == 'Pear' ): z.append('g')
      else: z.append('y')
    count += 1

plt.figure(figsize=(11,11))

recs=[]
classes=['Apples', 'Pear', 'Bananas']
class_colours = ['r','g','y']
plt.title("Apples, Bananas and Pear by Weight and Shape", fontsize=18)

plt.xlabel("Shape category number", fontsize=14)
plt.ylabel("Weight in ounces", fontsize=14)

plt.scatter(x,y,s=600,c=z)

