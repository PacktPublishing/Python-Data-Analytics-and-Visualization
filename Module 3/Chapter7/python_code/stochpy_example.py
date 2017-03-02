import stochpy as stp
smod = stp.SSA()

from pylab import rcParams
# set the graph display size as 10 by 10 inches
rcParams['figure.figsize'] = 12, 12

smod.Model('dsmts-003-04.xml.psc')
smod.DoStochSim(end=35,mode='time',trajectories=2000)
smod.GetRegularGrid()
smod.PlotAverageSpeciesTimeSeries()

