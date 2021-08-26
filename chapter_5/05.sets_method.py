a={1,2,3,4,5,1,(8,9)}
print(a)
print(len(a)) # it print the length of sets
a.remove(2)#it remove the value 2,if vlue is not prsent which we want remove then throw error
print(a)
print(a.pop())# it removes an arbitrary value from sets and return the element removed
print(a.clear())# it delete all sets value


#------------sets_function[union and intersection]------------------------
b={2,4,6,(10,12)}
c={10,20,6}
print(b.union(c))# it print union of set b and c
print(b.intersection(c)) # it print intersection of b and c
