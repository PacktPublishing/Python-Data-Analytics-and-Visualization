fibvalues = {0: 0, 1: 1, 2:1, 3:2, 4:3, 5:5}

def fibonacci(n):
    if n not in fibvalues: 
        sumvalue = fibonacci(n-1) + fibonacci(n-2)
        fibvalues[n] = sumvalue  
    return fibvalues[n]

fibonacci(40)

