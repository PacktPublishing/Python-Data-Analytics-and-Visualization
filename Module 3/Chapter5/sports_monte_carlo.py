import numpy as np
import matplotlib.pyplot as plt

colors = [(31, 119, 180), (174, 199, 232), (255, 127,  14),
   (255, 187, 120), (44, 160, 44), (214,  39,  40), (148,103,189),
   (152, 223, 138), (255,152,150), (197, 176, 213), (140, 86, 75),
   (196, 156, 148), (227,119,194), (247, 182, 210), (127,127,127),
   (199, 199, 199),(188,189, 34),(219, 219, 141), (23, 190,207),
   (158, 218, 229),(217,217,217)]

# Scale RGB values to the [0, 1] range, format matplotlib accepts.
for i in range(len(colors)):
  r, g, b = colors[i]
  colors[i] = (r / 255., g / 255., b / 255.)

    
def takeThree():
    if np.random.randint(0, high=100) < threePtPercent:
        if np.random.randint(0, high=100) < overtimePercent:
            return True #We won!!
    return False #We either missed the 3 or lost in OT

#takeTwo determines if we win in a given trials when we take a 2, foul and hope for another possession
def takeTwo():
  havePossession = True
  pointsDown = 3
  timeLeft = 30
  while (timeLeft > 0):
    #What to do if we have possession
    if (havePossession):
      #If we are down by 3 or more, we take the
      #2 quickly.  If we are down by 2 or less
      #We run down the clock first
      if (pointsDown >= 3):
        timeLeft -= timeToShoot2
      else:
        timeLeft = 0

      #Do we make the shot?
      if (np.random.randint(0, high=100) < twoPtPercent):
        pointsDown -= 2
        havePossession = False
    else:
      #Does the opponent team rebound?
      #If so, we lose possession.
      #This doesn't really matter when we run
      #the clock down
      if (np.random.randint(0, high=100) >= offenseReboundPercent):
        havePossession = False
      else:   #cases where we don't have possession
        if (pointsDown > 0):  #foul to get back possession

          #takes time to foul
          timeLeft -= timeToFoul

          #opponent takes 2 free throws
          if (np.random.randint(0, high=100) < oppFtPercent):
            pointsDown += 1

          if (np.random.randint(0, high=100) < oppFtPercent):
            pointsDown += 1
            havePossession = True
        else:
          if (np.random.randint(0, high=100) >= ftReboundPercent):
            #you were able to rebound the missed ft
            havePossession = True
          else:  
            #tied or up so don't want to foul; 
            #assume opponent to run out clock and take
            if (np.random.randint(0, high=100) < oppTwoPtPercent):
              pointsDown += 2 #They made the 2
            timeLeft = 0


  if (pointsDown > 0):
    return False
  else:
    if (pointsDown < 0):
      return True
    else:
      if (np.random.randint(0, high=100) < overtimePercent):
        return True
      else:
        return False

            
plt.figure(figsize=(14,14))
names=['Lebron James', 'Kyrie Irving', 'Steph Curry', 
       'Kyle Krover', 'Dirk Nowitzki']
threePercents = [35.4,46.8,44.3,49.2, 38.0]
twoPercents = [53.6,49.1,52.8, 47.0,48.6]

colind=0
for i in range(3):
    x=[]
    y1=[]
    y2=[]
    trials = 300 #Number of trials to run for simulation
    threePtPercent = threePercents[i] #Your % chance of making 3-pt shot
    twoPtPercent = twoPercents[i] #Your % chance of making a 2-pt shot
    oppTwoPtPercent = 40 #Opponent % chance making 2-pter
    oppFtPercent = 80 #Opponent's FT %
    timeToShoot2 = 5 #How many seconds elapse to shoot a 2
    timeToFoul = 5 #How many seconds elapse to foul opponent
    offenseReboundPercent = 25 #% of regular offense rebound
    ftReboundPercent = 15 #% of offense rebound after missed FT
    overtimePercent = 50 #% chance of winning in overtime
    
    winsTakingThree = 0
    lossTakingThree = 0
    winsTakingTwo = 0
    lossTakingTwo = 0
    curTrial = 1
    
    #Each time draw() is called, we run another trial and update
    #graphics
    while curTrial < trials:
            
            #run a trial take the 3
            if (takeThree()):
                winsTakingThree += 1        
            else:
                lossTakingThree += 1
            #run a trial taking a 2
            if takeTwo() == True :
                winsTakingTwo += 1
            else:
                lossTakingTwo += 1
            
            #print " winsTakingThree=",winsTakingThree," ->percentage",(100.0*winsTakingThree/curTrial),"winsTakingTwo=",winsTakingTwo," ->percentage",(100.0*winsTakingTwo/curTrial)
            x.append(curTrial)
            y1.append(winsTakingThree)
            y2.append(winsTakingTwo)
            curTrial += 1
    	 
    
    plt.plot(x,y1, color=colors[colind], label=names[i]+" Wins Taking Three Point")
    plt.plot(x,y2, color=colors[20], label=names[i]+" Wins Taking Two Point")
    colind += 2
    
legend = plt.legend(loc='upper left', shadow=True,)  
for legobj in legend.legendHandles:
    legobj.set_linewidth(2.4)
plt.show()

