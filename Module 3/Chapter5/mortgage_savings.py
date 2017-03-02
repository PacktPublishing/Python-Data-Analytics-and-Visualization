from decimal import Decimal
import matplotlib.pyplot as plt

colors = [(31, 119, 180),(174, 199, 232),(255,128,0),(255, 15, 14),
      (44, 160, 44),(152, 223, 138),(214, 39, 40),(255,173, 61),
      (148, 103, 189),(197, 176, 213),(140, 86, 75),(196, 156, 148),
      (227, 119, 194),(247, 182, 210),(127, 127, 127),
      (199, 199, 199),(188, 189, 34), (219, 219, 141), 
      (23, 190, 207), (158, 218, 229)]

# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
for i in range(len(colors)):
    r, g, b = colors[i]
    colors[i] = (r / 255., g / 255., b / 255.)

def printHeaders(term, extra):
    # Print headers
    print "\nExtra-Payment: $"+str(extra)+" Term:"+str(term)+" years"
    print "---------------------------------------------------------"
    print 'Pmt no'.rjust(6), ' ', 'Beg. bal.'.ljust(13), ' ',
    print 'Payment'.ljust(9), ' ', 'Principal'.ljust(9), ' ',
    print 'Interest'.ljust(9), ' ', 'End. bal.'.ljust(13)
    print ''.rjust(6, '-'), ' ', ''.ljust(13, '-'), ' ',
    print ''.rjust(9, '-'), ' ', ''.ljust(9, '-'), ' ',
    print ''.rjust(9, '-'), ' ', ''.ljust(13, '-'), ' '

def amortization_table(principal, rate, term, extrapayment, printData=False):
    xarr=[]
    begarr = []

    original_loan = principal
    money_saved=0
    total_payment=0
    payment = pmt(principal, rate, term)
    begBal = principal

    # Print data
    num=1
    endBal=1
    if printData == True: printHeaders(term, extrapayment)
    while  (num < term + 1) and (endBal >0):

        interest = round(begBal * (rate / (12 * 100.0)), 2)
        applied = extrapayment+round(payment - interest, 2)
        endBal = round(begBal - applied, 2)
        if (num-1)%12 == 0 or (endBal < applied+extrapayment):
          begarr.append(begBal)
          xarr.append(num/12)
          if printData == True:
              print '{0:3d}'.format(num).center(6), ' ',
              print '{0:,.2f}'.format(begBal).rjust(13), ' ',
              print '{0:,.2f}'.format(payment).rjust(9), ' ',
              print '{0:,.2f}'.format(applied).rjust(9), ' ',
              print '{0:,.2f}'.format(interest).rjust(9), ' ',
              print '{0:,.2f}'.format(endBal).rjust(13)
        total_payment += applied+extrapayment
        num +=1
        begBal = endBal
    if extrapayment > 0 :
      money_saved = abs(original_loan - total_payment)
      print '\nTotal Payment:','{0:,.2f}'.format(total_payment).rjust(13)
      print '  Money Saved:','{0:,.2f}'.format(money_saved).rjust(13)
    return xarr, begarr, '{0:,.2f}'.format(money_saved)

def pmt(principal, rate, term):

    ratePerTwelve = rate / (12 * 100.0)

    result = principal * (ratePerTwelve / (1 - (1 + ratePerTwelve) ** (-term)))

    # Convert to decimal and round off to two decimal
    # places.
    result = Decimal(result)
    result = round(result, 2)
    return result

plt.figure(figsize=(18, 14))

#amortization_table(150000, 4, 180, 500)
i=0
markers = ['o','s','D','^','v','*','p','s','D','o','s','D','^','v','*','p','s','D']
markersize=[8,8,8,12,8,8,8,12,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]

for extra in range(100,1700,100):
  xv, bv, saved = amortization_table(450000, 5, 360, extra, False)
  if extra == 0:
    plt.plot(xv, bv, color=colors[i], lw=2.2, label='Principal only', marker=markers[i], markersize=markersize[i])
  else:
    plt.plot(xv, bv, color=colors[i], lw=2.2, label="Principal plus\$"+str(extra)+str("/month, Saved:\$")+saved, marker=markers[i], markersize=markersize[i])
  i +=1


plt.grid(True)
plt.xlabel('Years', fontsize=18)
plt.ylabel('Mortgage Balance', fontsize=18)
plt.title("Mortgage Loan For $350,000 With Additional Payment Chart", fontsize=20)
plt.legend()
plt.show()

