setoftrees = { 'Basswood', 'Red Pine', 'Chestnut', 'Gray Birch', 'Black Cherry'} 

newtree = 'Tulip Tree' 
if newtree not in setoftrees:  setoftrees.add(newtree)

setoftrees
{'Basswood', 'Black Cherry', 'Chestnut', 'Gray Birch', 'Red Pine', 'Tulip Tree'}


#example of set operation on letters
charsinmath = set('mathematics')
charsinchem = set('chem')

print "Showing charsinmath"
charsinmath

print "Showing charsinchem"
charsinchem

#take away letters from charsinchem from charsinmath
print "Showing charsinmath-charsinchem"
charsinmath-charsinchem

