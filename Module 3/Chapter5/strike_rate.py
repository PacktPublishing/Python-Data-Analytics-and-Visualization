from math import log, sqrt, exp
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt

colors = [(31, 119, 180), (174, 199, 232), (255,128,0), (255, 15, 14), 
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
for i in range(len(colors)):
    r, g, b = colors[i]
    colors[i] = (r / 255., g / 255., b / 255.)
def black_scholes_merton(S, r, sigma, X, T):
  
  S = float(S)  # convert to float
  logsoverx = log (S/X)
  halfsigmasquare = 0.5 * sigma ** 2
  sigmasqrtT = sigma * sqrt(T)

  d1 = logsoverx + ((r + halfsigmasquare) * T) / sigmasqrtT
  d2 = logsoverx + ((r - halfsigmasquare) * T) / sigmasqrtT

  value = (S * stats.norm.cdf(d1, 0.0, 1.0) - X * exp(-r * T) * stats.norm.cdf(d2, 0.0, 1.0))
  return value
  
def vega(S, r, sigma, X, T):

  S = float(S)
  logsoverx = log (S/X)
  halfsigmasquare = 0.5 * sigma ** 2
  sigmasqrtT = sigma * sqrt(T)  
  d1 = logsoverx + ((r + halfsigmasquare) * T) / sigmasqrtT
  
  vega = S * stats.norm.cdf(d1, 0.0, 1.0) * sqrt(T)
  return vega  

def impliedVolatility(S, r, sigma_est, X, T, Cstar, it):
  
  for i in range(it):
    numer = (black_scholes_merton(S, r, sigma_est, X, T) - Cstar)
    denom = vega(S,r, sigma_est, X, T)
    sigma_est -= numer/denom
  return sigma_est
  

h5 = pd.HDFStore('/Users/MacBook/Downloads/vstoxx_data_31032014.h5', 'r')
futures_data = h5['futures_data'] # VSTOXX futures data
options_data = h5['options_data'] # VSTOXX call option data
h5.close()

#print "----------------------------------------------------"
#print "This ", options_data.index

options_data['IMP_VOL'] = 0.0
V0 = 17.6639
r=0.04
sigma_est=2
tol = 0.5 # tolerance level for moneyness
for option in options_data.index:
  # iterating over all option quotes
  futureval = futures_data[futures_data['MATURITY'] == 
      options_data.loc[option]['MATURITY']]['PRICE'].values[0]
  # picking the right futures value
   
  if (futureval * (1 - tol) < options_data.loc[option]['STRIKE'] 
     < futureval * (1 + tol)):
    impliedVol = impliedVolatility(V0,r,sigma_est,
            options_data.loc[option]['STRIKE'], 
            options_data.loc[option]['TTM'], 
            options_data.loc[option]['PRICE'],  #Cn
            it=40)                             #iterations 
    options_data['IMP_VOL'].loc[option] = impliedVol
  
plot_data = options_data[options_data['IMP_VOL'] > 0]
maturities = sorted(set(options_data['MATURITY']))

plt.figure(figsize=(15, 10))
i=0
for maturity in maturities:
  data = plot_data[options_data.MATURITY == maturity]
  # select data for this maturity
  plt.plot(data['STRIKE'], data['IMP_VOL'],
  label=maturity.date(), marker='o', color=colors[i], lw=3, markersize=8)
  i += 1

  #plt.plot(data['STRIKE'], data['IMP_VOL'], 'r.')
plt.grid(True)
plt.xlabel('Strike')
plt.ylabel('Implied volatility of volatility')
plt.legend()
plt.show()


