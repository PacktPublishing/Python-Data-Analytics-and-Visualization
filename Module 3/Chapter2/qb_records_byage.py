import csv
import matplotlib.pyplot as plt

# The following functions can be in a separate file
#    -- functions Begin -- 
def num(s):
    try:
      return int(s)
    except ValueError:
      return 0  

def getcolors():
    colors = [(31, 119, 180), (255,0,0), (0,255,0), (148, 103, 189), (140, 86, 75), (218, 73, 174), (127, 127, 127), (140,140,26), (23, 190, 207), (65,200,100), (200, 65,100), (125,255,32), (32,32,198), (255,191,201), (172,191,201), (0,128,0), (244,130,150), (255, 127, 14), (128,128,0), (10,10,10), (44, 160, 44), (214, 39, 40), (206,206,216)]

    for i in range(len(colors)):
         r, g, b = colors[i]
         colors[i] = (r / 255. , g / 255. , b / 255.)
    return colors

def getQbNames():
    qbnames = ['Peyton Manning']
    name=''
    i=0
    with open('/Users/MacBook/java/qb_data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if ( row['Name'] != name and qbnames[i] != row['Name']):
                qbnames.append(row['Name'])
                i = i+1
    return qbnames

def readQbdata():
    resultdata = []
    with open('/Users/MacBook/java/qb_data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        resultdata = [row for row in reader]
    return resultdata

fdata=[]
prevysum=0

#    -- functions End -- 


qbnames = getQbNames()
fdata = readQbdata()

i=0
rank=0
prevysum=0
lastyr=0
highrank=244
colorsdata = getcolors() 

fig = plt.figure(figsize=(15,13))
ax=fig.add_subplot(111,axisbg='white')

# limits for TD
plt.ylim(10, 744)
#change xlimit to have age ranges 
plt.xlim(20, 50)

colindex=0
lastage=20

for qbn in qbnames:
    x=[]
    y=[]
    prevysum=0
    for row in fdata: 
        if ( row['Name'] == qbn and row['Year'] != 'Career'):
            yrval = num(row['Year'])
            lastage = num(row['Age'])
            prevysum += num(row['TD'])
            lastyr = yrval
            x += [lastage]
            y += [prevysum]

    if ( rank > highrank):
        if ( lastage == 44):
            plt.plot(x,y, color='red', label=qbn, linewidth=3.5)
        else:
            plt.plot(x,y, color=colorsdata[colindex], label=qbn, linewidth=2.5)
            plt.legend(loc=0, prop={'size':10}) 

        colindex = (colindex+1)%22
        plt.text(lastage-1, prevysum+2, qbn+"("+str(prevysum)+"):" +str(lastage), fontsize=9)
 
    else:
        if ( lastage == 44):
            plt.plot(x,y, color='red', label=qbn, linewidth=3.5)
            plt.text(lastage-1, prevysum+2, qbn+"("+str(prevysum)+"):" +str(lastage), fontsize=9)
        else:         
            plt.plot(x,y, color=colorsdata[22], linewidth=1.5) 
        rank = rank +1 

plt.show() 

