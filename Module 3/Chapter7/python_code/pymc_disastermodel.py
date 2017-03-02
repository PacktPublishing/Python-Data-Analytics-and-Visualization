from pymc.examples import disaster_model
from pymc import MCMC

from pylab import hist, show, rcParams

rcParams['figure.figsize'] = 10, 10

M = MCMC(disaster_model)
M.sample(iter=65536, burn=8000, thin=16)

hist(M.trace('late_mean')[:], color='#b02a2a')

show()

