import matplotlib.pyplot as plt
from treePlotter import createPlot

branchNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt,      xycoords='axes fraction',    xytext=centerPt, textcoords='axes fraction', va="center",      ha="center",bbox=nodeType, arrowprops=arrow_args,fontsize=14)

def createTwoNodes():
  fig = plt.figure(1, facecolor='white', figsize=(10,10))
  fig.clf()
  createPlot.ax1 = plt.subplot(111, frameon=False)
  plotNode('a decision node', (0.3, 0.2), (0.7, 0.5), branchNode) 
  plotNode('a leaf node', (0.7, 0.1), (0.8, 0.5), leafNode) 


  plt.show()

createTwoNodes()
