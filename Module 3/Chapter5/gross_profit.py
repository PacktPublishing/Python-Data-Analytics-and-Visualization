principle_value=10000  #invested amount
grossReturn = 1.06     # Rt

return_amt = []
x = []
y = [10000]
year=2010
return_amt.append(principle_value)
x.append(year)

for i in range(1,15):
  return_amt.append(return_amt[i-1] * grossReturn)
  print "Year-",i," Returned:",return_amt[i]
  
  year += 1
  x.append(year)
  y.append(833.33*(year-2010)+principle_value)

# set the grid to appear
plt.grid()

# plot the return values curve
plt.plot(x,return_amt, color='r')
plt.plot(x,y, color='b')


