import scipy as sp

# function that multiplies two polynomials
def multiplyPoly():  
    #cubic1 has coefficients 3, 4, 5 and 5 
    cubic1 = sp.poly1d([3, 4, 5, 5])  
 
    #cubic2 has coefficients 4, 1, -3 and 3
    cubic2 = sp.poly1d([4, 1, -3, 3]) 

    print cubic1   
    print cubic2 

    print '-' * 36

    #print results of polynomial multiplication
    print cubic1 * cubic2

multiplyPoly()

