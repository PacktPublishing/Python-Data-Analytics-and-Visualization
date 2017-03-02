from random import uniform, seed
from math import sqrt
import matplotlib.pyplot as plt

num = 250             # These many agents of a particular type
numNeighbors = 12     # Number of agents regarded as neighbors
requireSameType = 8   # At least this many neighbors to be same type

seed(10)  # for reproducible random numbers

class StudentAgent:

    def __init__(self, type):
        #Students of different type will be shown in colors
        self.type = type
        self.show_position()

    def show_position(self):
        # position changed by using uniform(x,y)
        self.position = uniform(0, 1), uniform(0, 1)

    def get_distance(self, other):
        #returns euclidean distance between self and other agent.
        a = (self.position[0] - other.position[0])**2
        b = (self.position[1] - other.position[1])**2
        return sqrt(a + b)

    def happy(self, agents):
        "returns True if reqd number of neighbors are the same type."
        distances = []

        for agent in agents:
            if self != agent:
                distance = self.get_distance(agent)
                distances.append((distance, agent))
        distances.sort()
        neighbors = [agent for d, agent in distances[:numNeighbors]]
        numSameType = sum(self.type == agent.type 
            for agent in neighbors)
        return numSameType >= requireSameType

    def update(self, agents):
        "If not happy, randomly choose new positions until happy."
        while not self.happy(agents):
            self.show_position()


def plot_distribution(agents, cycle_num):
    
    x1,y1 = [],[]
    x2,y2 = [],[]
    x3,y3 = [],[]
    
    for agent in agents:
        x, y = agent.position
        if agent.type == 0:
            x1.append(x); y1.append(y)
        elif agent.type == 1:
            x2.append(x); y2.append(y)        
        else:
            x3.append(x); y3.append(y)

    fig, ax = plt.subplots(figsize=(10,10))
    plot_args = {'markersize' : 8, 'alpha' : 0.65, 'markersize': 14}
    ax.set_axis_bgcolor('#ffffff')
    ax.plot(x1, y1, 'o', markerfacecolor='#1b62a5',  **plot_args)
    ax.plot(x2, y2, 'o', markerfacecolor='#279321', **plot_args)
    ax.plot(x3, y3, 'D', markerfacecolor='#fd6610', **plot_args)
    ax.set_title('Iteration {}'.format(cycle_num))
    plt.show()

agents = [StudentAgent(0) for i in range(num)]
agents.extend(StudentAgent(1) for i in range(num))
agents.extend(StudentAgent(2) for i in range(num))
count = 1
terminate=False
while terminate == False:
    plot_distribution(agents, count)
    count += 1
    no_one_moved = True
    for agent in agents:
        old_position = agent.position
        agent.update(agents)
        if agent.position != old_position:
            no_one_moved = False
    if no_one_moved:
        terminate=True

