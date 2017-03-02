import random

print random.random() # between 0.0 and 1.0
print random.uniform(2.54, 12.2) # between 2.54 and 12.2
print random.randint(5,10)  # random integer between 5 and 10

print random.randrange(25)  # random number between 0 and 25
#  random numbers from the range of 5 to 500 with step 5
print random.randrange(5,500,5) 

# three random number from the list 
print random.sample([13,15,29,31,43,46,66,89,90,94], 3) 
# Random choice from a list
random.choice([1, 2, 3, 5, 9])

