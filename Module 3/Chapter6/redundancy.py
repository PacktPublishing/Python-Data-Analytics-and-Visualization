import matplotlib.pyplot as plt
import csv

gender=[]
x=[]
y=[]
with open('/Users/MacBook/Downloads/Book_Code/Chapter6/height_weight.csv', 'r') as csvf:
  reader = csv.reader(csvf, delimiter=',')
  count=0
  for row in reader:
    if count > 0:
        if row[0] == "f": gender.append(0)
        else:  gender.append(1)
        height = float(row[3])
        weight = float(row[4])
        x.append(height)
        y.append(weight)
    count += 1

plt.figure(figsize=(11,11))
plt.scatter(y,x,c=gender,s=300)
plt.grid(True)
plt.xlabel('Weight', fontsize=18)
plt.ylabel('Height', fontsize=18)
plt.title("Height vs Weight (Students)", fontsize=20)
plt.legend()

plt.show()

