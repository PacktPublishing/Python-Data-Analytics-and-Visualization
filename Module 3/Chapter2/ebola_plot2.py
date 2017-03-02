import matplotlib.pyplot as plt  
import csv 
import operator 
import datetime as dt  

with open('/Users/MacBook/Downloads/Book_Code/Chapter2/ebola.csv', 'rt') as f: 
  filtereddata = [row for row in csv.reader(f) if row[3] != "0.0" and 
  row[3] != "0" and "deaths" in row[0]] 

sorteddata = sorted(filtereddata, key=operator.itemgetter(1))  

guineadata  = [row for row in sorteddata if row[1] == "Guinea" and 
    row[0] == "Cumulative number of confirmed, probable and suspected Ebola deaths"] 
sierradata  = [row for row in sorteddata if row[1] == "Sierra Leone" and 
    row[0] == "Cumulative number of confirmed, probable and suspected Ebola deaths"] 
liberiadata = [row for row in sorteddata if row[1] == "Liberia" and 
    row[0] == "Cumulative number of confirmed, probable and suspected Ebola deaths"] 

g_x = [dt.datetime.strptime(row[2], '%Y-%m-%d').date() for 
       row in guineadata] 
g_y = [row[3] for row in guineadata] 

s_x = [dt.datetime.strptime(row[2], '%Y-%m-%d').date() for 
       row in sierradata] 
s_y = [row[3] for row in sierradata] 

l_x = [dt.datetime.strptime(row[2], '%Y-%m-%d').date() for
       row in liberiadata] 
l_y = [row[3] for row in liberiadata] 

plt.plot(g_x,g_y, color='red') 
plt.plot(s_x,s_y, color='orange') 
plt.plot(l_x,l_y, color='blue')  
plt.show()
