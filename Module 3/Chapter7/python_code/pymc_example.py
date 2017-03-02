import pymc as mc

from pylab import rcParams

# set the graph display size as 10 by 10 inches
rcParams['figure.figsize'] = 12, 12
z = -1.

#instead of 0 and 1, some unknown mu and std goes here:
X = mc.Normal( "x", 0, 1, value = -3. ) 

#Here below, one can place unknowns here in place of 1, 0.4
@mc.potential
def Y(x=X, z=z): 
  return mc.lognormal_like( z-x, 1, 0.4,  )

mcmc = mc.MCMC([X])
mcmc.sample(10000,500)
mc.Matplot.plot(mcmc)

